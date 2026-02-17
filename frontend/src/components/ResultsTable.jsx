export default function ResultsTable({ columns, rows }) {
  return (
    <table className="w-full text-left border-collapse rounded">
      <thead className="bg-primary text-text">
        <tr>
          {columns.map(col => (
            <th key={col} className="p-2 border-b border-accent">{col}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {rows.map((row, idx) => (
          <tr key={idx} className="hover:bg-accent/10">
            {columns.map(col => (
              <td key={col} className="p-2 border-b border-secondary">
                {row[col]}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
