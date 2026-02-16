from pydantic import BaseModel
from typing import List, Dict, Any


class SQLRequest(BaseModel):
    query: str
    db_schema: str   # ✅ renamed from schema


class SQLResponse(BaseModel):
    sql: str


class SQLExecutionResult(BaseModel):
    sql: str
    columns: List[str]
    rows: List[Dict[str, Any]]


class AggregationRequest(BaseModel):
    column: str
    rows: List[Dict[str, Any]]


class AggregationResult(BaseModel):
    column: str
    sum: float


class InsightRequest(BaseModel):
    query: str
    rows: List[Dict[str, Any]]


class InsightResult(BaseModel):
    insight: str


class PlotRequest(BaseModel):
    x_column: str
    y_column: str
    data: List[Dict[str, Any]]


class PlotResult(BaseModel):
    x_column: str
    y_column: str
    chart_type: str
