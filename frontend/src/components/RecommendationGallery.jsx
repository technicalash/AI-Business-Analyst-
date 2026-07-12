import { useState } from "react";

function RecommendationGallery({ recommendations }) {
  const [showRecommendations, setShowRecommendations] = useState(false);

  if (
    !recommendations ||
    !recommendations.recommendations ||
    recommendations.recommendations.length === 0
  ) {
    return null;
  }

  const badgeColor = (priority) => {
    switch (priority) {
      case "High":
        return "bg-red-100 text-red-700";

      case "Medium":
        return "bg-yellow-100 text-yellow-700";

      default:
        return "bg-green-100 text-green-700";
    }
  };

  return (
    <div className="bg-white rounded-2xl shadow-lg p-8">
      <h2 className="text-3xl font-bold text-gray-800">
        💡 AI Recommendations
      </h2>

      <p className="text-gray-500 mt-2 mb-6">
        These recommendations are generated using AI based on the insights
        extracted from your dataset.
      </p>

      <button
        onClick={() => setShowRecommendations(!showRecommendations)}
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
        {showRecommendations ? "Hide Recommendations" : "View Recommendations"}
      </button>

      {showRecommendations && (
        <div className="mt-8 space-y-6">
          {recommendations.recommendations.map((recommendation, index) => (
            <div
              key={index}
              className="
                bg-slate-50
                rounded-xl
                border
                shadow
                p-6
                hover:shadow-xl
                hover:-translate-y-1
                transition
                duration-300
              "
            >
              <span
                className={`
                  inline-block
                  px-3
                  py-1
                  rounded-full
                  text-sm
                  font-semibold
                  ${badgeColor(recommendation.priority)}
                `}
              >
                {recommendation.priority} Priority
              </span>

              <h3 className="text-2xl font-bold mt-4 text-gray-800">
                {recommendation.title}
              </h3>

              <div className="mt-5">
                <h4 className="font-semibold text-blue-600">Recommendation</h4>

                <p className="text-gray-700 mt-2">
                  {recommendation.recommendation}
                </p>
              </div>

              <div className="mt-5">
                <h4 className="font-semibold text-blue-600">Why?</h4>

                <p className="text-gray-700 mt-2">{recommendation.reason}</p>
              </div>

              <div className="mt-5">
                <h4 className="font-semibold text-blue-600">Business Impact</h4>

                <p className="text-gray-700 mt-2">
                  {recommendation.expected_impact}
                </p>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default RecommendationGallery;
