import Navbar from "../components/Navbar";
import UploadBox from "../components/UploadBox";
import ReportCard from "../components/ReportCard";
import PlotGallery from "../components/PlotGallery";
import InsightGallery from "../components/InsightGallery";
import { useState } from "react";
function Home() {
  const [report, setReport] = useState(null);
  const [plots, setPlots] = useState([]);
  const [insights, setInsights] = useState([]);
  return (
    <div>
      <Navbar />
      <p>
        Upload your dataset to get AI-powered preprocessing and business
        insights.
      </p>
      <UploadBox
        report={report}
        setReport={setReport}
        setPlots={setPlots}
        setInsights={setInsights}
      />
      <ReportCard report={report} />
      <PlotGallery plots={plots} />
      <InsightGallery insights={insights} />
    </div>
  );
}

export default Home;
