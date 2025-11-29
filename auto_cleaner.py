import pandas as pd
from typing import List


def suggest_pipeline(profile: dict) -> List[str]:
    steps = []
    cols = profile.get("columns_profile", {})
    for col, info in cols.items():
        if info.get("pct_missing", 0) > 0.5:
            steps.append(f"drop_column:{col}")
        elif 0 < info.get("pct_missing", 0) <= 0.5:
            # choose a simple imputation rule
            if info.get("dtype", "").startswith("int") or info.get("dtype", "").startswith("float"):
                steps.append(f"impute_median:{col}")
            else:
                steps.append(f"impute_mode:{col}")

        if info.get("dtype", "").startswith("object") and info.get("n_unique", 0) > 100:
            steps.append(f"encode_topk:{col}:10")

    # de-duplicate rows by default
    steps.insert(0, "drop_duplicates")
    return steps


def apply_pipeline(df: pd.DataFrame, pipeline: List[str]) -> pd.DataFrame:
    for step in pipeline:
        parts = step.split(":")
        op = parts[0]
        if op == "drop_duplicates":
            df = df.drop_duplicates()
        elif op == "drop_column":
            col = parts[1]
            if col in df.columns:
                df = df.drop(columns=[col])
        elif op == "impute_median":
            col = parts[1]
            if col in df.columns:
                median = df[col].median()
                df[col] = df[col].fillna(median)
        elif op == "impute_mode":
            col = parts[1]
            if col in df.columns:
                mode = df[col].mode()
                df[col] = df[col].fillna(mode.iloc[0] if not mode.empty else None)
        elif op == "encode_topk":
            col = parts[1]
            k = int(parts[2]) if len(parts) > 2 else 10
            if col in df.columns:
                top = df[col].value_counts().nlargest(k).index
                df[col] = df[col].where(df[col].isin(top), other="<OTHER>")
        # future ops can be added here

    return df
