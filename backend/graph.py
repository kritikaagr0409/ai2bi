from langgraph.graph import StateGraph
from typing import TypedDict, List, Dict, Any

from backend.nodes.sql_generator import sql_generator_node
from backend.validator import validate_sql
from backend.database import execute_sql
from backend.nodes.aggregation import aggregation_node
from backend.nodes.visualization import generate_visualization
from backend.nodes.insight import generate_insight
from backend.nodes.memory import memory_node
from backend.models import SQLRequest, AggregationRequest


class GraphState(TypedDict, total=False):
    query: str
    db_schema: str
    sql: str
    columns: List[str]
    rows: List[Dict[str, Any]]
    aggregation: Dict[str, Any]
    visualization: Dict[str, Any]
    insight: str


def generate_sql(state: GraphState):
    req = SQLRequest(query=state["query"], db_schema=state["db_schema"])
    response = sql_generator_node(req)
    return {"sql": response.sql}


def validate_node(state: GraphState):
    validate_sql(state["sql"])
    return {}


def execute_node(state: GraphState):
    rows = execute_sql(state["sql"])
    columns = list(rows[0].keys()) if rows else []
    return {"rows": rows, "columns": columns}

def aggregate_node_wrapper(state: GraphState):
    from backend.models import AggregationRequest
    from backend.nodes.aggregation import aggregation_node

    rows = state.get("rows", [])
    columns = state.get("columns", [])

    if not rows or not columns:
        return {}

    numeric_col = None
    for col in columns:
        if isinstance(rows[0][col], (int, float)):
            numeric_col = col
            break

    if not numeric_col:
        return {}

    request = AggregationRequest(
        rows=rows,
        column=numeric_col,
        operation="sum"
    )

    result = aggregation_node(request)

    return {"aggregation": result.dict()}

def insight_node_wrapper(state: GraphState):
    from backend.models import InsightRequest
    from backend.nodes.insight import generate_insight

    request = InsightRequest(
        query=state.get("query", ""),
        rows=state.get("rows", [])
    )

    result = generate_insight(request)

    return {"insight": result.insight}
def visualization_node_wrapper(state: GraphState):
    from backend.models import PlotRequest

    columns = state.get("columns", [])
    rows = state.get("rows", [])

    if len(columns) >= 2:
        request = PlotRequest(
            x_column=columns[0],
            y_column=columns[1],
            data=rows
        )
    else:
        request = PlotRequest(
            x_column="",
            y_column="",
            data=rows
        )

    result = generate_visualization(request)

    return {
        "visualization": {
            "chart_type": result.chart_type,
            "x_axis": result.x_column,
            "y_axis": result.y_column
        }
    }

graph = StateGraph(GraphState)

graph.add_node("generate_sql", generate_sql)
graph.add_node("validate", validate_node)
graph.add_node("execute", execute_node)
graph.add_node("aggregate", aggregate_node_wrapper)
graph.add_node("visualize", visualization_node_wrapper)
graph.add_node("insight", insight_node_wrapper)
graph.add_node("memory", memory_node)

graph.set_entry_point("generate_sql")

graph.add_edge("generate_sql", "validate")
graph.add_edge("validate", "execute")
graph.add_edge("execute", "aggregate")
graph.add_edge("aggregate", "visualize")
graph.add_edge("visualize", "insight")
graph.add_edge("insight", "memory")

app_graph = graph.compile()
