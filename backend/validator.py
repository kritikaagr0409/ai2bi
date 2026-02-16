import sqlparse

FORBIDDEN = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER"]


def validate_sql(query: str):
    query = query.strip()

    if not query.upper().startswith("SELECT"):
        raise Exception(f"Only SELECT queries allowed. Generated: {query}")

    for word in FORBIDDEN:
        if word in query.upper():
            raise Exception("Unsafe SQL detected")

    sqlparse.parse(query)
    return True
