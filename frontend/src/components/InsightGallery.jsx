import { useState } from "react";

function InsightGallery({ insights }) {
  const [showInsight, setShowInsight] = useState(false);
  if (!insights || !insights.insights || insights.insights.length === 0) {
    return null;
  }
  return (
    <>
      <button onClick={() => setShowInsight(!showInsight)}>
        {showInsight ? "Hide Insights" : "Show Insights"}
      </button>
      {showInsight && (
        <div>
          <h2>AI Business Insights</h2>
          {insights.insights.map((insight, index) => (
            <div
              key={index}
              style={{
                border: "1px solid #ddd",
                borderRadius: "10px",
                padding: "18px",
                marginBottom: "20px",
                boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
              }}
            >
              <h3>{insight.title}</h3>
              <p>
                <strong>Description: </strong>
                {insight.description}
              </p>
              <p>
                <strong>Evidence: </strong>
                {insight.evidence}
              </p>
              <p>
                <strong>Importance: </strong>
                {insight.importance}
              </p>
            </div>
          ))}
        </div>
      )}
    </>
  );
}

export default InsightGallery;
