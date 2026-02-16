import os
from dotenv import load_dotenv

load_dotenv()

SQL_DATABASE_URL = os.getenv("SQL_DATABASE_URL")
MONGO_URL = os.getenv("MONGO_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
