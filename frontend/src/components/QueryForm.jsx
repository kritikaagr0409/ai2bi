import { useState } from "react";

export default function QueryForm({ onSubmit }) {
  const [text, setText] = useState("");

  return (
    <div className="flex gap-2 w-full">
      <input
        className="flex-grow p-3 bg-primary text-text rounded"
        placeholder="Ask a BI question..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button
        className="px-4 py-2 bg-accent text-black font-bold rounded"
        onClick={() => onSubmit(text)}
      >
        Go
      </button>
    </div>
  );
}
