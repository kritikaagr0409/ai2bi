import axios from "axios";

const API_BASE = "http://127.0.0.1:8000";

export async function sendQuery(query) {
  const response = await axios.post(`${API_BASE}/query`, { query });
  return response.data;
}
