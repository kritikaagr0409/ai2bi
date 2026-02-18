from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from backend.models import InsightRequest, InsightResult

llm = ChatOllama(model="mistral")


def generate_insight(request: InsightRequest) -> InsightResult:
    if not request.rows:
        return InsightResult(insight="No data available.")

    sample = request.rows[:5]

    messages = [
        SystemMessage(content="You are a business analyst."),
        HumanMessage(content=f"""
User Question:
{request.query}

Data Sample:
{sample}

Provide short business insight.
""")
    ]

    response = llm.invoke(messages)

    return InsightResult(insight=response.content.strip())
