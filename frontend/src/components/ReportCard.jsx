import { downloadDataset } from "../services/api";
import { downloadReport } from "../services/api";
import { useState } from "react";

function ReportCard({ report }) {
  const [showData, setShowData] = useState(false);
  if (!report) return null;
  return (
    <div className="bg-white rounded-2xl shadow-lg p-8">
      <h2 className="text-3xl font-bold text-gray-800">📄 Processing Report</h2>
      <p className="text-gray-500 mt-2 mb-6">
        Review the preprocessing operations performed by the AI and download the
        cleaned dataset.
      </p>
      <button
        onClick={() => setShowData(!showData)}
        className="
        w-full
        bg-blue-600
        hover:bg-blue-700
        text-white
        py-3
        rounded-xl
        font-semibold
        transition
      "
      >
        {showData ? "Hide Processing Steps" : "View Processing Steps"}
      </button>
      {showData && (
        <div>
          <h3>Preprocessing Operations</h3>
          {report.preprocessing_report.operations.map((step, index) => (
            <div
              key={index}
              className="
    bg-slate-50
    border
    rounded-xl
    p-5
    mt-5
  "
            >
              <p>
                <h3 className="text-xl font-semibold text-blue-700">
                  ✔ {step.operation}
                </h3>
              </p>
              <p>Parameters:</p>

              <div className="mt-3">
                <h4 className="font-medium mb-2">Parameters</h4>

                <pre className="bg-gray-100 p-4 rounded-lg overflow-auto text-sm">
                  {JSON.stringify(step.parameters, null, 2)}
                </pre>
              </div>
            </div>
          ))}
        </div>
      )}
      <button
        onClick={() => downloadDataset(report.processed_filename)}
        className="
        mt-4
        w-full
        bg-green-600
        hover:bg-green-700
        text-white
        py-3
        rounded-xl
        font-semibold
        transition
      "
      >
        ⬇ Download Cleaned Dataset
      </button>
      <button
        onClick={() => downloadReport(report.report_filename)}
        className="
        mt-4
        w-full
        bg-green-600
        hover:bg-green-700
        text-white
        py-3
        rounded-xl
        font-semibold
        transition
      "
      >
        📄 Download AI Report
      </button>
    </div>
  );
}

export default ReportCard;
