import streamlit as st
import pandas as pd
from agents.orchestrator import Orchestrator


def main():
    st.set_page_config(page_title="Auto Data Doctor", layout="wide")
    st.title("Auto Data Doctor — Quick Demo")

    st.sidebar.header("Upload Data")
    uploaded = st.sidebar.file_uploader("Upload a CSV file", type=["csv"]) 

    if uploaded is None:
        st.info("Upload a CSV file from the sidebar to begin.")
        return

    df = pd.read_csv(uploaded)
    st.subheader("Raw dataset (first 20 rows)")
    st.dataframe(df.head(20))

    orchestrator = Orchestrator()

    if st.sidebar.button("Run Auto-Doctor"):
        with st.spinner("Running profiling and fixes..."):
            result = orchestrator.run(df.copy())

        st.subheader("Profile Summary")
        st.json(result.get("profile", {}))

        st.subheader("Suggested Pipeline")
        for step in result.get("pipeline", []):
            st.markdown(f"- {step}")

        st.subheader("Cleaned Data (first 20 rows)"):
        st.dataframe(result.get("cleaned_df").head(20))

        csv_bytes = result.get("cleaned_df").to_csv(index=False).encode("utf-8")
        st.sidebar.download_button("Download cleaned CSV", data=csv_bytes, file_name="cleaned.csv")


if __name__ == "__main__":
    main()
