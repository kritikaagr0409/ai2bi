from fastapi import FastAPI
from pydantic import BaseModel
from backend.models import SQLRequest
from backend.graph import app_graph

app = FastAPI()


class QueryInput(BaseModel):
    query: str


SCHEMA = """
Table: sales
Columns:
- id (int)
- order_date (date)
- region (text)
- revenue (float)
- profit_margin (float)
"""

@app.post("/query")
def query_endpoint(request: QueryInput):
    try:
        result = app_graph.invoke({
            "query": request.query,
            "db_schema": SCHEMA
        })

        return result

    except Exception as e:
        return {"error": str(e)}

