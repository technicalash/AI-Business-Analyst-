import { useState } from "react";

import Navbar from "../components/Navbar";
import UploadBox from "../components/UploadBox";
import ReportCard from "../components/ReportCard";
import PlotGallery from "../components/PlotGallery";
import InsightGallery from "../components/InsightGallery";
import RecommendationGallery from "../components/RecommendationGallery";

import { Database, Sparkles, BarChart3, BrainCircuit } from "lucide-react";

function Home() {
  const [report, setReport] = useState(null);
  const [plots, setPlots] = useState([]);
  const [insights, setInsights] = useState([]);
  const [recommendations, setRecommendations] = useState([]);

  return (
    <div className="min-h-screen bg-slate-100">
      {/* <Navbar /> */}

      {/* Hero Section */}

      <section className="bg-gradient-to-r from-blue-700 to-indigo-700 text-white">
        <div className="max-w-6xl mx-auto px-6 py-16 text-center">
          <div className="flex justify-center mb-5">
            <Database size={60} />
          </div>

          <h1 className="text-5xl font-bold">AI Business Analyst</h1>

          <p className="mt-5 text-xl text-blue-100 max-w-3xl mx-auto">
            Upload your CSV dataset and let AI automatically clean, analyze,
            visualize and generate business insights and recommendations.
          </p>

          <div className="flex justify-center gap-8 mt-10 flex-wrap">
            <div className="flex items-center gap-2">
              <Sparkles size={22} />
              <span>AI Cleaning</span>
            </div>

            <div className="flex items-center gap-2">
              <BarChart3 size={22} />
              <span>Visualizations</span>
            </div>

            <div className="flex items-center gap-2">
              <BrainCircuit size={22} />
              <span>Insights & Recommendations</span>
            </div>
          </div>
        </div>
      </section>

      {/* Main Content */}

      <main className="max-w-6xl mx-auto px-6 py-10 space-y-8">
        <UploadBox
          report={report}
          setReport={setReport}
          setPlots={setPlots}
          setInsights={setInsights}
          setRecommendations={setRecommendations}
        />

        <ReportCard report={report} />

        <PlotGallery plots={plots} />

        <InsightGallery insights={insights} />

        <RecommendationGallery recommendations={recommendations} />
      </main>
    </div>
  );
}

export default Home;
