import { downloadDataset } from "../services/api";
import { useState } from "react";

function ReportCard({ report }) {
  const [showData, setShowData] = useState(false);
  if (!report) return null;
  return (
    <div>
      <button onClick={() => setShowData(!showData)}>
        {showData ? "Hide Processed Operations" : "View Processed Operations"}
      </button>
      {showData && (
        <div>
          <h3>Preprocessing Operations</h3>
          {report.preprocessing_report.operations.map((step, index) => (
            <div key={index}>
              <p>
                <strong>Operation:</strong> {step.operation}
              </p>
              <p>Parameters:</p>

              <pre>{JSON.stringify(step.parameters, null, 2)}</pre>
            </div>
          ))}
        </div>
      )}
      <button onClick={() => downloadDataset(report.processed_filename)}>
        Download Cleaned Dataset
      </button>
    </div>
  );
}

export default ReportCard;
