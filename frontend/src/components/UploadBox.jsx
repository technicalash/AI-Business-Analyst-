import { useState } from "react";
import { uploadDataset } from "../services/api";

function UploadBox({
  report,
  setReport,
  setPlots,
  setInsights,
  setRecommendations,
}) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  function handleFileChange(event) {
    const file = event.target.files[0];
    setSelectedFile(file);
  }
  async function handleUpload() {
    if (!selectedFile) {
      alert("Please select a CSV file.");
      return;
    }

    setLoading(true);
    setError("");
    try {
      const response = await uploadDataset(selectedFile);
      setReport(response);
      setPlots(response.generated_plots);
      setInsights(response.insights);
      setRecommendations(response.recommendations);
    } catch (error) {
      setError("Upload failed.");
    } finally {
      setLoading(false);
    }
  }
  return (
    <div className="bg-white rounded-2xl shadow-lg p-8 max-w-3xl mx-auto">
      {/* Heading */}

      <h2 className="text-3xl font-bold text-gray-800">📂 Upload Dataset</h2>

      <p className="text-gray-500 mt-2 mb-8">
        Upload a CSV dataset to generate AI-powered preprocessing,
        visualizations, insights and recommendations.
      </p>

      {/* Upload Area */}

      <div className="space-y-5">
        <input
          id="csv-upload"
          type="file"
          accept=".csv"
          onChange={handleFileChange}
          className="hidden"
        />
        <label
          htmlFor="csv-upload"
          className="
    flex
    flex-col
    items-center
    justify-center
    w-full
    p-10
    border-2
    border-dashed
    border-blue-400
    rounded-2xl
    bg-blue-50
    cursor-pointer
    hover:bg-blue-100
    transition
  "
        >
          <span className="text-5xl">📂</span>

          <h3 className="mt-4 text-xl font-semibold text-gray-700">
            Click to Upload CSV
          </h3>

          <p className="text-gray-500 mt-2">
            Select your dataset to begin AI analysis
          </p>
        </label>

        {selectedFile ? (
          <p className="text-green-600 font-medium">✅ {selectedFile.name}</p>
        ) : (
          <p className="text-gray-500">No file selected</p>
        )}

        <button
          onClick={handleUpload}
          disabled={loading}
          className="
            w-full
            bg-blue-600
            hover:bg-blue-700
            text-white
            font-semibold
            py-3
            rounded-xl
            transition
            duration-300
            disabled:bg-gray-400
            disabled:cursor-not-allowed
          "
        >
          {loading ? "Analyzing..." : "🚀 Analyze Dataset"}
        </button>

        {loading && (
          <p className="text-blue-600 font-medium">
            🤖 AI is analyzing your dataset...
          </p>
        )}

        {error && <p className="text-red-600 font-medium">❌ {error}</p>}

        {report && (
          <p className="text-green-600 font-semibold">
            ✅ Dataset processed successfully!
          </p>
        )}
      </div>
    </div>
  );
}

export default UploadBox;
