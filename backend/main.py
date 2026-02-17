from fastapi import FastAPI
from pydantic import BaseModel
from backend.models import SQLRequest
from backend.graph import app_graph
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

