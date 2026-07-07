import Navbar from "../components/Navbar";
import UploadBox from "../components/UploadBox";
import ReportCard from "../components/ReportCard";
import { useState } from "react";
function Home() {
  const [report, setReport] = useState(null);
  return (
    <div>
      <Navbar />
      <p>
        Upload your dataset to get AI-powered preprocessing and business
        insights.
      </p>
      <UploadBox report={report} setReport={setReport} />
      <ReportCard report={report} />
    </div>
  );
}

export default Home;
