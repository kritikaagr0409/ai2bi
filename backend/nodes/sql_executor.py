from ..models import SQLResponse, SQLExecutionResult
from ..database import execute_sql


def sql_execution_node(input: SQLResponse) -> SQLExecutionResult:
    rows = execute_sql(input.sql)
    columns = list(rows[0].keys()) if rows else []

    return SQLExecutionResult(
        sql=input.sql,
        columns=columns,
        rows=rows
    )
