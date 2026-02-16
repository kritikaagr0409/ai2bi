
```markdown
# 🚀 AI2BI – NL2SQL Conversational Business Intelligence Engine

AI2BI is a backend-powered conversational analytics engine that converts Natural Language queries into executable SQL queries using a local LLM (Ollama + Mistral), validates them securely, executes them on PostgreSQL, and returns structured results.

This project is designed as a startup-grade foundation for building a configurable AI-powered BI system.

---

## 🔥 Features

- 🧠 Natural Language → SQL conversion
- 🛡 SQL safety validation (SELECT-only guardrails)
- ⚡ PostgreSQL execution layer
- 🧩 Modular LangGraph orchestration
- 🏗 Structured state-based architecture
- 🖥 FastAPI backend
- 🧠 Local LLM (Ollama – no API key required)

---

## 🏗 Architecture

```

User Query
↓
FastAPI Endpoint
↓
LangGraph Pipeline
↓
SQL Generator (Ollama - Mistral)
↓
SQL Validator (Security Layer)
↓
SQL Executor (PostgreSQL)
↓
Structured JSON Response

```

---

## 📁 Project Structure

```

AITOBI/
│
├── backend/
│   ├── main.py
│   ├── graph.py
│   ├── models.py
│   ├── database.py
│   ├── validator.py
│   ├── config.py
│   │
│   └── nodes/
│       ├── sql_generator.py
│
├── .env
└── README.md

````

---

## ⚙️ Requirements

- Python 3.10+
- PostgreSQL
- Ollama
- Mistral model

---

## 🧠 Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd AITOBI
````

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate (Windows):

```bash
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pymongo python-dotenv langgraph langchain-core langchain-ollama sqlparse
```

---

### 4️⃣ Install Ollama

Download from:

[https://ollama.com/download](https://ollama.com/download)

After installation:

```bash
ollama pull mistral
```

Test:

```bash
ollama run mistral
```

Exit with:

```
/bye
```

---

### 5️⃣ Setup PostgreSQL

Create database:

```sql
CREATE DATABASE ai2bi_db;
```

Create table:

```sql
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    order_date DATE,
    region TEXT,
    revenue FLOAT,
    profit_margin FLOAT
);
```

Insert sample data:

```sql
INSERT INTO sales (order_date, region, revenue, profit_margin)
VALUES
('2024-01-01', 'North', 10000, 0.25),
('2024-01-05', 'South', 15000, 0.30),
('2024-02-01', 'East', 20000, 0.15),
('2024-02-10', 'West', 18000, 0.22);
```

---

### 6️⃣ Configure Environment Variables

Create `.env` file:

```
SQL_DATABASE_URL=postgresql://postgres:password@localhost:5432/ai2bi_db
MONGO_URL=mongodb://localhost:27017
```

---

## 🚀 Running the Server

From project root:

```bash
uvicorn backend.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Example API Call

### Request

```json
{
  "query": "Show total revenue by region"
}
```

### Response

```json
{
  "query": "Show total revenue by region",
  "db_schema": "...",
  "sql": "SELECT region, SUM(revenue) FROM sales GROUP BY region;",
  "columns": ["region", "sum"],
  "rows": [
    {"region": "North", "sum": 10000},
    {"region": "South", "sum": 15000}
  ]
}
```

---

## 🔐 Security Features

* Only SELECT queries allowed
* DROP/DELETE/UPDATE/INSERT blocked
* SQL sanitized before execution
* LLM output cleaned before validation

---

## 🧠 How It Works

1. User submits NL query
2. Ollama (Mistral) generates SQL
3. Output is cleaned (markdown removal)
4. SQL is validated
5. SQL executed on PostgreSQL
6. Structured response returned

---

## 🛠 Future Enhancements

* Insight generation layer (AI explanation)
* Multi-tenant schema support
* Dynamic schema retrieval
* SQL auto-retry mechanism
* Confidence scoring
* Streamlit frontend
* Role-based access
* Query logging & monitoring

---

