class ExplainAgent:
    def __init__(self):
        pass

    def explain(self, profile: dict, pipeline: list) -> str:
        """Produce a textual explanation for the actions taken.

        This implementation is deterministic and rule-based so it works without external LLM keys.
        """
        cols = profile.get("columns_profile", {})
        reasons = []
        for col, info in cols.items():
            if info.get("pct_missing", 0) > 0.5:
                reasons.append(f"Column '{col}' has >50% missing values: consider dropping or filling cautiously.")
            elif info.get("pct_missing", 0) > 0:
                reasons.append(f"Column '{col}' has {info.get('pct_missing')*100:.1f}% missing values: filled using sensible defaults.")

        if not reasons:
            reasons.append("No major issues detected; minor cleaning steps applied.")

        explanation = "\n".join(reasons)
        if pipeline:
            explanation += "\nPipeline steps: " + ", ".join(pipeline)

        return explanation
