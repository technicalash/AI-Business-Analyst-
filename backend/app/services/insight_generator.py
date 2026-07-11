import json
import re
from app.services.llm_services import generate_response

def generate_insights(cleaned_metadata, plot_statistics ):
    prompt = f"""
You are an expert Business Analyst and Senior Data Scientist.

You are given:

1. Dataset metadata.
2. Statistics computed from important visualizations.

Your task is to generate business insights based ONLY on the provided information.

Generate insights that would be valuable to a business analyst.

Rules:

- Use ONLY the provided metadata and visualization statistics.
- Do NOT invent information.
- Do NOT assume relationships that are not supported by the evidence.
- If evidence is weak, clearly state that it is weak instead of exaggerating.
- Avoid simply repeating statistics. Interpret them and explain why they matter.
- Do not generate duplicate or trivial insights.

Prioritize insights in this order:

1. Strong relationships and correlations.
2. Significant differences between groups.
3. Major trends and distributions.
4. Outliers or unusual patterns.
5. Data quality issues only if they significantly impact analysis.

Correlation Guidelines:

- |r| < 0.30 → Weak
- 0.30 ≤ |r| < 0.70 → Moderate
- |r| ≥ 0.70 → Strong

Generate between 5 and 8 insights.

For each insight include:

- title
- description
- evidence
- importance

Importance must be one of:

- High
- Medium
- Low

Return ONLY valid JSON.

The response MUST begin with '{{' and end with '}}'.

Do NOT use Markdown.

Do NOT wrap the JSON inside ``` or ```json.

Do NOT include any explanation, heading, notes, or text before or after the JSON.

Format:

{{
    "insights": [
        {{
            "title": "...",
            "description": "...",
            "evidence": "...",
            "importance": "High"
        }}
    ]
}}

Dataset Metadata:

{json.dumps(cleaned_metadata, indent=2)}

Visualization Statistics:

{json.dumps(plot_statistics, indent=2)}
"""
    return get_insights(prompt)

def parse_llm_json(response: str):

    response = response.strip()

    # Remove ```json
    response = re.sub(
        r"^```(?:json)?\s*",
        "",
        response,
        flags=re.IGNORECASE,
    )

    # Remove ending ```
    response = re.sub(
        r"\s*```$",
        "",
        response,
    )

    response = response.strip()

    return json.loads(response)

def get_insights(prompt):
        response = generate_response(prompt)
        return parse_llm_json(response)