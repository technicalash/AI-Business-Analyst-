import json
from app.services.llm_services import generate_response

def _build_prompt(dataset_metadata):

    prompt = f"""
You are an expert Data Scientist and Business Analyst.

Your task is to recommend the most informative visualizations for the given dataset.

The objective is to help users understand the dataset and discover valuable business insights.

Recommend ONLY meaningful visualizations.

Do NOT recommend redundant, duplicate, or low-value charts.

Recommend between 5 and 10 visualizations ranked by importance.

Allowed plot types ONLY:

- histogram
- bar
- scatter
- boxplot
- line
- heatmap
- pie

Rules:

1. Use ONLY columns that exist in the dataset metadata.

2. Do NOT invent column names.

3. Only use a target column (for example "Survived", "Sales", "Revenue", etc.) if it actually exists.

4. For frequency/count bar charts:
   - Omit the "y" field.
   - Set:
     "aggregation": "count"

5. Scatter plots require both x and y.

6. Histograms require only x.

7. Line charts require x and y.

8. Grouped boxplots require x and y.
   Single-variable boxplots require only y.

9. Heatmaps should not include x or y.
   Instead provide:
   "columns": ["Column1", "Column2", ...]

10. Pie charts should only be recommended for categorical columns having relatively few unique values.

11. For bar, line and pie charts, specify the aggregation whenever applicable.

Allowed aggregation values:

- count
- mean
- median
- sum
- none

Use "none" if no aggregation is required.

12. Rank plots using priority:

- 1 = Most Important
- 2 = Important
- 3 = Optional

13. Generate human-readable axis labels.

Example:

"x_label": "Passenger Survival Status"

instead of

"x_label": "Survived"

14. If a categorical column contains encoded values whose meaning can be confidently inferred from the column name or metadata (for example 0/1, Yes/No, True/False), provide a mapping using:

"value_labels": {{
    "0": "Did Not Survive",
    "1": "Survived"
}}

If the meaning cannot be confidently inferred, omit "value_labels".

15. Do NOT invent category meanings.

16. Every visualization MUST include a short business reason explaining why it is useful.

For every visualization provide:

- type
- title
- x (if required)
- y (if required)
- columns (only for heatmap)
- aggregation
- x_label
- y_label
- value_labels (only if applicable)
- reason
- priority

Return ONLY valid JSON.

Return format:

{{
    "plots": [
        {{
            "type": "bar",
            "title": "Passenger Survival Count",
            "x": "Survived",
            "aggregation": "count",
            "x_label": "Passenger Survival Status",
            "y_label": "Number of Passengers",
            "value_labels": {{
                "0": "Did Not Survive",
                "1": "Survived"
            }},
            "reason": "Shows the number of passengers who survived versus those who did not.",
            "priority": 1
        }},
        {{
            "type": "scatter",
            "title": "Income vs Sales",
            "x": "Income",
            "y": "Sales",
            "aggregation": "none",
            "x_label": "Customer Income",
            "y_label": "Sales Amount",
            "reason": "Shows the relationship between customer income and sales.",
            "priority": 2
        }},
        {{
            "type": "heatmap",
            "title": "Correlation Heatmap",
            "columns": [
                "Age",
                "Fare",
                "FamilySize"
            ],
            "aggregation": "none",
            "x_label": "Features",
            "y_label": "Features",
            "reason": "Shows correlations among numerical variables.",
            "priority": 1
        }}
    ]
}}

The response MUST be valid JSON.

Do NOT include explanations.

Do NOT use markdown.

Do NOT wrap the response inside ```.

Dataset Metadata:

{json.dumps(dataset_metadata, indent=2)}
"""

    return prompt

def generate_visualization_plan(dataset_metadata):

    prompt = _build_prompt(dataset_metadata)

    response = generate_response(prompt)

    plan = json.loads(response)

    return plan