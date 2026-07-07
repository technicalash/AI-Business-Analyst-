import { useState } from "react";
import { uploadDataset } from "../services/api";

function UploadBox({ report, setReport }) {
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
      console.log(response);
    } catch (error) {
      setError("Upload failed.");
    } finally {
      setLoading(false);
    }
  }
  return (
    <>
      <input type="file" accept=".csv" onChange={handleFileChange} />
      {selectedFile ? (
        <p>Selected File: {selectedFile.name}</p>
      ) : (
        <p>No file selected</p>
      )}
      <button onClick={handleUpload}>Analyze Dataset</button>
      {loading && <p>Analyzing dataset...</p>}
      {error && <p>{error}</p>}
      {report && <h3>Dataset processed successfully!✅</h3>}
    </>
  );
}

export default UploadBox;
