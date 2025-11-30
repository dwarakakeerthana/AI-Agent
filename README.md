# AI-DATA-DOCTOR AGENT, Enterprise Workflow AI for Data Analysts & Data Scientists

An enterprise-grade multi-agent AI system that diagnoses, heals, and explains data issues automatically.

### ✅ Key Capabilities
- Dataset profiling, including schema, stats, missing values, and quality signals
- Automated data cleaning pipeline generation and application
- Data drift detection with metrics
- LLM-powered fix explanations
- Observability with structured logs
- Streamlit deployment for real-world use

### 🧠 Concepts Demonstrated (Kaggle Capstone Requirements)
- Multi-agent orchestration with sequential, parallel, and loop agents
- Custom tools and OpenAI API integration
- Sessions and memory-ready architecture
- Logging, tracing, and metrics for observability
- Agent-style modular deployment

### 🏗 Folder Structure 
[image alt](https://github.com/dwarakakeerthana/AI-Agent/blob/main/Screenshot%202025-11-30%20102946.png?raw=true)

#### Real-World Impact
- Saves analysts 8-12 hours per week on manual debugging and cleaning
- Standardizes cleaning workflows for the company
- Helps non-machine learning teams understand issues using plain language
- Improves data reliability for dashboards, models, and monitoring

### Setup & Run Locally
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app/main.p``

## Security Best Practices

Store API keys in .env and protect them with .gitignore.

Do not push sensitive data to public repositories.
