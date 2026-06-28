import pandas as pd

def clean_dataset(df:pd.DataFrame):
    df = _strip_column_names(df)
    df, _ = _remove_duplicate_rows(df)
    df = _convert_data_types(df)

    return df
    
def _strip_column_names(df: pd.DataFrame):
    df.columns = df.columns.str.strip()
    return df

def _remove_duplicate_rows(df: pd.DataFrame):
    rows_before = len(df)

    df = df.drop_duplicates()

    rows_after = len(df)

    duplicates_removed = rows_before - rows_after

    return df, duplicates_removed

def _convert_data_types(df: pd.DataFrame):
    return df.infer_objects(copy=False)