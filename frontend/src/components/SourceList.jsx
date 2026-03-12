export default function SourceList({ sources }) {
  if (!sources || sources.length === 0) return null;

  return (
    <div className="sources">
      <h3>Sources</h3>
      {sources.map((src, index) => (
        <div key={index} className="source-card">
          <p><strong>File:</strong> {src.source}</p>
          <p><strong>Chunk:</strong> {src.chunk_id}</p>
          <p><strong>Score:</strong> {src.score.toFixed(4)}</p>
          <p>{src.text.slice(0, 250)}...</p>
        </div>
      ))}
    </div>
  );
}