from langgraph.graph import StateGraph
from typing import TypedDict, List, Dict, Any

from backend.nodes.sql_generator import sql_generator_node
from backend.validator import validate_sql
from backend.database import execute_sql
from backend.models import SQLRequest


class GraphState(TypedDict, total=False):
    query: str
    db_schema: str
    sql: str
    columns: List[str]
    rows: List[Dict[str, Any]]


# 1️⃣ SQL Generation Node
def generate_sql(state: GraphState) -> GraphState:
    req = SQLRequest(
        query=state["query"],
        db_schema=state["db_schema"]
    )

    response = sql_generator_node(req)

    return {"sql": response.sql}


# 2️⃣ Validation Node
def validate_node(state: GraphState) -> GraphState:
    validate_sql(state["sql"])
    return {}


# 3️⃣ Execution Node
def execute_node(state: GraphState) -> GraphState:
    rows = execute_sql(state["sql"])
    columns = list(rows[0].keys()) if rows else []

    return {
        "rows": rows,
        "columns": columns
    }


# Build Graph
graph = StateGraph(GraphState)

graph.add_node("generate_sql", generate_sql)
graph.add_node("validate", validate_node)
graph.add_node("execute", execute_node)

graph.set_entry_point("generate_sql")

graph.add_edge("generate_sql", "validate")
graph.add_edge("validate", "execute")

app_graph = graph.compile()
