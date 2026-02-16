from pymongo import MongoClient
from .config import MONGO_URL
from datetime import datetime

client = MongoClient(MONGO_URL)
db = client["ai2bi"]
chat_collection = db["chat_logs"]


def store_chat(tenant_id, query, sql, result):
    chat_collection.insert_one({
        "tenant_id": tenant_id,
        "query": query,
        "sql": sql,
        "result_count": len(result),
        "timestamp": datetime.utcnow()
    })
