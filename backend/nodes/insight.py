from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

from ..models import InsightRequest, InsightResult
from ..config import OPENAI_API_KEY

llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.3)


def insight_node(input: InsightRequest) -> InsightResult:
    messages = [
        SystemMessage(content="You are a business analyst."),
        HumanMessage(content=f"""
User Query: {input.query}

Data Sample:
{input.rows[:5]}

Provide a short business insight summary.
""")
    ]

    response = llm(messages)

    return InsightResult(summary=response.content.strip())
