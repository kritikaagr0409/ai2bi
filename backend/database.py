from sqlalchemy import create_engine, text
from .config import SQL_DATABASE_URL

engine = create_engine(SQL_DATABASE_URL)


def execute_sql(query: str):
    with engine.connect() as connection:
        result = connection.execute(text(query))
        rows = result.fetchall()
        columns = result.keys()

    return [dict(zip(columns, row)) for row in rows]
