from agents.profiling_agent import ProfilingAgent
from agents.fixing_agent import FixingAgent
from agents.explain_agent import ExplainAgent
from memory.memory_bank import MemoryBank


class Orchestrator:
    def __init__(self):
        self.profiling = ProfilingAgent()
        self.fixing = FixingAgent()
        self.explain = ExplainAgent()
        self.memory = MemoryBank()

    def run(self, df):
        """Run the profiling -> fixing -> explain flow and store pipeline in memory."""
        profile = self.profiling.profile(df)
        pipeline, cleaned_df = self.fixing.apply_fixes(df, profile)
        explanation = self.explain.explain(profile, pipeline)

        # Persist a small record to memory
        record_id = self.memory.save_run_summary(profile, pipeline)

        return {"profile": profile, "pipeline": pipeline, "cleaned_df": cleaned_df, "explanation": explanation, "record_id": record_id}
