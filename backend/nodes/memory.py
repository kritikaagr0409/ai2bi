from backend.mongo import store_chat

def memory_node(state):
    store_chat(
        tenant_id="default",
        query=state.get("query"),
        sql=state.get("sql"),
        result=state.get("rows", [])
    )
    return {}
