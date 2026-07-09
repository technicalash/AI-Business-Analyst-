import { useState } from "react";

function PlotGallery({ plots }) {
  const [showPlot, setShowPlot] = useState(false);
  if (!plots || plots.length === 0) {
    return null;
  }
  return (
    <div>
      <button onClick={() => setShowPlot(!showPlot)}>
        {showPlot ? "Hide Plots" : "View Data Plots"}
      </button>
      {showPlot && (
        <div>
          <h2>Generated Visualizations</h2>

          {plots.map((plot, index) => (
            <div
              key={index}
              style={{
                border: "1px solid #ccc",
                padding: "15px",
                marginBottom: "20px",
                borderRadius: "8px",
              }}
            >
              <h3>{plot.title}</h3>

              <p>
                <strong>Reason:</strong> {plot.reason}
              </p>

              <img
                src={`http://127.0.0.1:8000${plot.path}`}
                alt={plot.title}
                style={{
                  width: "100%",
                  maxWidth: "700px",
                  borderRadius: "6px",
                }}
              />
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default PlotGallery;
