# 10 Academy – Week 0 Challenge

Kickstart Your AI Mastery with African Climate Trend Analysis.

Project structure, environment setup, and how to run notebooks are documented here.

Environment setup (recommended - venv):

1. Create and activate virtual environment (Windows PowerShell):

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

2. Jupyter notebook:

```powershell
jupyter notebook
```

3. Streamlit (dashboard):

```powershell
streamlit run app/main.py
```

Repository contents:

- `.github/workflows/ci.yml`: CI workflow
- `requirements.txt`: Python dependencies
- `notebooks/`: EDA notebooks (per-country)
- `src/`: project code
- `scripts/`: helper scripts
- `tests/`: tests

Reproducible commands and contributor notes are included in the project files.
