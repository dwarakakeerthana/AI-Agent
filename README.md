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
AI-DATA-DOCTOR-AUGENT/
├── src/
│   └── data_doctor/        ← **Primary package root**
│       ├── __init__.py
│       ├── orchestrator.py
│       ├── memory/
│       │   ├── __init__.py
│       │   ├── memory_bank.py
│       │   └── session_service.py
│       ├── agents/
│       │   ├── __init__.py
│       │   ├── profiling_agent.py
│       │   ├── fixing_agent.py
│       │   ├── drift_agent.py
│       │   └── explain_agent.py
│       └── tools/
│           ├── __init__.py
│           ├── api_tool.py
│           ├── auto_cleaner.py
│           ├── code_executor.py
│           └── mcp_tool.py
├── data/
│   ├── examples/.gitkeep
│   ├── cleaned/.gitkeep
│   └── outputs/.gitkeep
├── notebooks/
│   ├── demo.ipynb
│   └── evaluation.ipynb
├── tests/
│   ├── test_agents.py
│   └── test_tools.py
├── docs/                   (optional for competition)
│   └── README.md
├── .gitignore
├── requirements.txt        ← **Keep this, don’t rename**
└── pyproject.toml          (optional, skip if time is low)

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
