import pandas as pd

def execute_preprocessing_plan(df: pd.DataFrame, preprocessing_plan: dict):

    for step in preprocessing_plan["operations"]:
        try:
            operation = step["operation"]
            parameters = step["parameters"]
            print(f"Executing: {operation}")
            if operation == "fill_missing":
                df = _fill_missing(df, parameters)
            elif operation == "remove_outliers":
                df = _remove_outliers(df, parameters)
            elif operation == "drop_columns":
                df = _drop_columns(df, parameters)
            elif operation == "change_dtype":
                df = _change_dtype(df, parameters)
            elif operation == "feature_engineering":
                df = _feature_engineering(df, parameters)
            elif operation == "remove_sparse_rows":
                df = _remove_sparse_rows(df, parameters)
            elif operation == "remove_sparse_columns":
                df = _remove_sparse_columns(df, parameters)
        except Exception as e:
            print(f"Operation {operation} failed: {e}")
    return df
            

        

def _fill_missing(df: pd.DataFrame, parameters: dict):

    column = parameters["column"]
    method = parameters["method"]

    if method == "mean":
        df[column] = df[column].fillna(df[column].mean())

    elif method == "median":
        df[column] = df[column].fillna(df[column].median())

    elif method == "mode":
        df[column] = df[column].fillna(df[column].mode()[0])
    
    elif method == "constant":
        value = parameters["value"]
        df[column] = df[column].fillna(value)

    return df

def _remove_outliers(df: pd.DataFrame, parameters: dict):
    column = parameters["column"]
    method = parameters["method"]

    if method == "iqr":

        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        df = df[(df[column] >= lower) & (df[column] <= upper)]

    elif method == "zscore":

        mean = df[column].mean()
        std = df[column].std()

        z = ((df[column] - mean) / std).abs()

        df = df[z <= 3]

    return df


def _drop_columns(df: pd.DataFrame, parameters: dict):
    if "columns" in parameters:
        columns = parameters["columns"]
    else:
        columns = [parameters["column"]]

    df = df.drop(columns=columns)

    return df


def _change_dtype(df: pd.DataFrame, parameters: dict):
    column = parameters["column"]
    dtype = parameters["dtype"]

    df[column] = df[column].astype(dtype)

    return df


def _feature_engineering(df: pd.DataFrame, parameters: dict):
    new_column = parameters["new_column"]
    formula = parameters["formula"]

    df[new_column] = df.eval(formula)

    return df

def _remove_sparse_rows(df, parameters):

    threshold = parameters["threshold"]

    minimum_non_null = int((1 - threshold) * len(df.columns))

    df = df.dropna(thresh=minimum_non_null)

    return df

def _remove_sparse_columns(df, parameters):

    threshold = parameters["threshold"]

    minimum_non_null = int((1 - threshold) * len(df))

    df = df.dropna(axis=1, thresh=minimum_non_null)

    return df