import pandas as pd

def detect_column_types(df: pd.DataFrame, threshold: int = 20):
    column_types = {}
    for col in df.columns:
        dtype = df[col].dtype
        if pd.api.types.is_numeric_dtype(dtype):
            unique_vals = df[col].nunique(dropna=True)
            if unique_vals < threshold:
                column_types[col] = "categorical"
            else:
                column_types[col] = "numerical"
        elif pd.api.types.is_string_dtype(dtype):
            avg_len = df[col].dropna().astype(str).map(len).mean()
            if avg_len > 50:
                column_types[col] = "text"
            else:
                column_types[col] = "categorical"
        elif pd.api.types.is_bool_dtype(dtype):
            column_types[col] = "categorical"
        else:
            column_types[col] = "categorical"
    return column_types
