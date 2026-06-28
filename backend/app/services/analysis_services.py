import pandas as pd

def analyze_dataset(df: pd.DataFrame):
    return {
        "dataset_info": _get_dataset_info(df),
        "columns": _get_column_info(df),
        "duplicate_rows": _get_duplicate_rows(df),
    }
    
def _get_dataset_info(df: pd.DataFrame):
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "memory_usage_bytes": int(df.memory_usage(deep=True).sum())
    }
    
def _get_missing_values(df: pd.DataFrame):
    return df.isnull().sum().to_dict()

def _get_data_types(df: pd.DataFrame):
    return df.dtypes.astype(str).to_dict()

def _get_numerical_columns(df: pd.DataFrame):
    return df.select_dtypes(include="number").columns.tolist()

def _get_categorical_columns(df: pd.DataFrame):
    return df.select_dtypes(exclude="number").columns.tolist()

def _get_duplicate_rows(df: pd.DataFrame):
    return int(df.duplicated().sum())

def _get_column_info(df: pd.DataFrame):

    column_info = {}

    for column in df.columns:

        series = df[column]

        info = {
            "dtype": str(series.dtype),
            "missing": int(series.isnull().sum()),
            "unique": int(series.nunique()),
            "sample_values": series.dropna().head(5).tolist()
        }

        if pd.api.types.is_numeric_dtype(series):

            info["statistics"] = {
                "min": float(series.min()),
                "max": float(series.max()),
                "mean": float(series.mean()),
                "median": float(series.median()),
                "std": float(series.std())
            }

        column_info[column] = info

    return column_info