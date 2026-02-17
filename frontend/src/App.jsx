import { useState } from "react";
import QueryForm from "./components/QueryForm";
import LoadingSpinner from "./components/LoadingSpinner";
import ResultsTable from "./components/ResultsTable";
import { sendQuery } from "./api";

export default function App() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  async function handleSubmit(query) {
    setError("");
    setResult(null);
    setLoading(true);
    try {
      const data = await sendQuery(query);
      setResult(data);
    } catch (ex) {
      setError("Failed to fetch");
    }
    setLoading(false);
  }

  return (
    <div className="min-h-screen p-8 text-text">
      <h1 className="text-4xl font-bold mb-6 text-accent text-center">
        AI2BI 🎯
      </h1>

      <QueryForm onSubmit={handleSubmit} />

      {loading && (
        <div className="flex justify-center my-8">
          <LoadingSpinner />
        </div>
      )}

      {error && (
        <div className="text-red-500 font-semibold text-center my-4">
          {error}
        </div>
      )}

      {result && (
        <div className="mt-6 space-y-4">
          <div>
            <strong>SQL:</strong>
            <pre className="bg-primary p-4 rounded text-sm overflow-x-auto">
              {result.sql}
            </pre>
          </div>

          <ResultsTable
            columns={result.columns || []}
            rows={result.rows || []}
          />
        </div>
      )}
    </div>
  );
}
