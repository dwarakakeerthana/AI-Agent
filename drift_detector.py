import pandas as pd


def simple_drift_check(ref: pd.Series, current: pd.Series) -> dict:
    """Compare two series distributions using simple statistics."""
    res = {
        "ref_mean": float(ref.mean()) if not ref.empty else None,
        "cur_mean": float(current.mean()) if not current.empty else None,
        "mean_diff": None,
    }
    try:
        if res["ref_mean"] is not None and res["cur_mean"] is not None:
            res["mean_diff"] = abs(res["ref_mean"] - res["cur_mean"])
    except Exception:
        pass
    return res
