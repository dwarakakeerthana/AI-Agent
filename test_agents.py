import pandas as pd
from agents.profiling_agent import ProfilingAgent
from agents.fixing_agent import FixingAgent


def test_profile_and_fix():
    df = pd.DataFrame({
        "num": [1, 2, None, 2],
        "cat": ["a", "b", "a", None],
    })
    p = ProfilingAgent()
    profile = p.profile(df)
    assert profile["rows"] == 4

    f = FixingAgent()
    pipeline, cleaned = f.apply_fixes(df, profile)
    assert isinstance(pipeline, list)
    assert cleaned.isnull().sum().sum() == 0
