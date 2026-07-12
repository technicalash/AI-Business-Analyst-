import json

from app.services.llm_services import generate_response


def generate_recommendations(cleaned_metadata, insights):

    prompt = f"""
You are an experienced Business Consultant and Senior Business Analyst.

You are given:

1. Dataset metadata.
2. AI-generated insights.

Your task is to generate practical recommendations based on the provided insights.

Rules:

- Use simple English.
- Avoid technical jargon.
- Assume the reader has little technical knowledge.
- Recommend only actions supported by the insights.
- Do not invent new findings.
- Do not contradict the insights.
- If the dataset is business-related, provide practical business recommendations.
- If the dataset is not business-related, provide practical recommendations that improve analysis, decision-making, safety, efficiency, or future outcomes based on the insights.
- Explain why each recommendation is useful.
- Explain how following the recommendation may help.
- Keep recommendations realistic and actionable.

Generate between 5 and 8 recommendations.

For every recommendation provide:

- title
- recommendation
- reason
- expected_impact
- priority

Priority values:

- High
- Medium
- Low

Return ONLY valid JSON.

Do NOT include markdown.

Do NOT wrap the response inside ```.

Return format:

{{
    "recommendations": [
        {{
            "title": "...",
            "recommendation": "...",
            "reason": "...",
            "expected_impact": "...",
            "priority": "High"
        }}
    ]
}}

Dataset Metadata

{json.dumps(cleaned_metadata, indent=2)}

Insights

{json.dumps(insights, indent=2)}
"""

    return get_recommendations(prompt)


def get_recommendations(prompt):

    response = generate_response(prompt)

    response = (
        response.replace("```json", "")
                .replace("```", "")
                .strip()
    )

    recommendations = json.loads(response)

    return recommendations