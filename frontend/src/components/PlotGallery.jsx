import { useState } from "react";

function PlotGallery({ plots }) {
  const [showPlot, setShowPlot] = useState(false);
  if (!plots || plots.length === 0) {
    return null;
  }
  return (
    <div className="bg-white rounded-2xl shadow-lg p-8">
      <h2 className="text-3xl font-bold text-gray-800">📊 AI Visualizations</h2>

      <p className="text-gray-500 mt-2 mb-6">
        The following charts were automatically generated to help understand
        your dataset.
      </p>
      <button
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
        onClick={() => setShowPlot(!showPlot)}
      >
        {showPlot ? "Hide Plots" : "View Data Plots"}
      </button>
      {showPlot && (
        <div className="grid md:grid-cols-2 gap-8 mt-8">
          {plots.map((plot, index) => (
            <div
              key={index}
              className="
          bg-slate-50
          rounded-xl
          shadow
          border
          p-5
          hover:shadow-xl
          hover:-translate-y-1
          transition
          duration-300
        "
            >
              <h3 className="text-xl font-bold text-gray-800">{plot.title}</h3>

              <div className="mt-4">
                <h4 className="font-semibold text-blue-600">
                  Why this visualization?
                </h4>

                <p className="text-gray-600 mt-2">{plot.reason}</p>
              </div>

              <img
                src={`http://127.0.0.1:8000${plot.path}`}
                alt={plot.title}
                className="w-full rounded-lg mt-6 object-contain"
              />
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default PlotGallery;
