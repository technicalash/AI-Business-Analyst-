import json
from app.services.llm_services import generate_response

def _build_prompt(preprocessing_context):

    prompt = f"""
You are an expert Data Scientist and Data Analyst.

Your task is to analyze the dataset metadata and generate a preprocessing plan.

The goal is to prepare the dataset for business analysis, visualization, and machine learning while preserving as much useful information as possible.

Only use the following operation names exactly as written:

- fill_missing
- drop_columns
- change_dtype
- remove_outliers
- feature_engineering
- remove_sparse_rows
- remove_sparse_columns

Do NOT invent new operation names.

Parameter rules:

1. fill_missing
{{
    "operation": "fill_missing",
    "parameters": {{
        "column": "Column_Name",
        "method": "mean | median | mode | constant",
        "value": "Required only if method is constant"
    }}
}}

2. drop_columns
{{
    "operation": "drop_columns",
    "parameters": {{
        "columns": [
            "Column1",
            "Column2"
        ]
    }}
}}

IMPORTANT:
Always use "columns" (a list), even if only one column needs to be removed.

3. change_dtype
{{
    "operation": "change_dtype",
    "parameters": {{
        "column": "Column_Name",
        "dtype": "int | float | string | datetime | boolean"
    }}
}}

4. remove_outliers
{{
    "operation": "remove_outliers",
    "parameters": {{
        "column": "Column_Name",
        "method": "iqr | zscore"
    }}
}}

5. feature_engineering
{{
    "operation": "feature_engineering",
    "parameters": {{
        "new_column": "New_Column_Name",
        "formula": "ColumnA / ColumnB"
    }}
}}

6. remove_sparse_rows
{{
    "operation": "remove_sparse_rows",
    "parameters": {{
        "threshold": 0.7
    }}
}}

7. remove_sparse_columns
{{
    "operation": "remove_sparse_columns",
    "parameters": {{
        "threshold": 0.7
    }}
}}

Return ONLY a valid JSON object.

The response MUST NOT be a JSON array.

The top-level JSON MUST exactly follow this schema:

{{
    "operations": [
        {{
            "operation": "operation_name",
            "parameters": {{
                ...
            }}
        }}
    ]
}}

Requirements:
- Return a JSON object, not a JSON array.
- The top-level object must contain exactly one key named "operations".
- The value of "operations" must be a JSON array.
- Do NOT return the operations directly as an array.
- The response must begin with a JSON object and end with the matching closing brace.
- Do NOT include explanations.
- Do NOT include markdown.
- Do NOT wrap the response inside ```.

Dataset Metadata:

{json.dumps(preprocessing_context, indent=2)}
"""
    return prompt


def generate_preprocessing_plan(preprocessing_context):
    prompt = _build_prompt(preprocessing_context)

    response = generate_response(prompt)
    print("========== GEMINI RESPONSE ==========")
    print(response)
    print("=====================================")
    
    response = response.strip()

    plan = json.loads(response)
    if isinstance(plan, list):
        plan = {
        "operations": plan
        }
    return plan