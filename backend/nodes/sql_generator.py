from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from backend.models import SQLRequest, SQLResponse
import re

llm = ChatOllama(model="mistral")


def clean_sql(output: str) -> str:
    # Remove ```sql fences
    output = re.sub(r"```sql", "", output, flags=re.IGNORECASE)
    output = re.sub(r"```", "", output)

    # Remove extra text before SELECT
    match = re.search(r"(SELECT .*?;)", output, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()

    # If no semicolon version found, try without semicolon
    match = re.search(r"(SELECT .*?$)", output, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()

    return output.strip()


def sql_generator_node(input: SQLRequest) -> SQLResponse:
    messages = [
        SystemMessage(content=f"""
You are a PostgreSQL expert.
Generate ONLY a safe SELECT query.
Do NOT explain anything.
Do NOT use markdown.
Return ONLY raw SQL.

Schema:
{input.db_schema}
"""),
        HumanMessage(content=input.query)
    ]

    response = llm.invoke(messages)

    cleaned_sql = clean_sql(response.content)

    return SQLResponse(sql=cleaned_sql)