import pandas as pd


class ProfilingAgent:
    def __init__(self):
        pass

    def profile(self, df: pd.DataFrame) -> dict:
        """Produce a lightweight profile for the input dataframe."""
        profile = {}
        profile["rows"] = int(df.shape[0])
        profile["columns"] = int(df.shape[1])

        cols = {}
        for col in df.columns:
            s = df[col]
            cols[col] = {
                "dtype": str(s.dtype),
                "n_missing": int(s.isna().sum()),
                "pct_missing": float(s.isna().mean()),
                "n_unique": int(s.nunique(dropna=True)),
            }
            try:
                if pd.api.types.is_numeric_dtype(s):
                    cols[col]["mean"] = float(s.mean()) if s.count() else None
                    cols[col]["median"] = float(s.median()) if s.count() else None
                else:
                    cols[col]["top"] = s.mode().iloc[0] if not s.mode().empty else None
            except Exception:
                pass

        profile["columns_profile"] = cols
        return profile
