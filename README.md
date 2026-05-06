# 10 Academy – Week 0 Challenge: Kickstart Your AI Mastery with African Climate Trend Analysis

## Project Overview

This repository contains a professional analysis of historical climate data from five African countries (Ethiopia, Kenya, Sudan, Tanzania, Nigeria) using NASA POWER climate data (January 2015 – March 2026).

**Context:** Junior Data Analyst at EthioClimate Analytics supporting the Ethiopian Ministry of Planning and Development in preparation for COP32 (UN Climate Change Conference, Addis Ababa 2027).

**Objective:** Produce evidence-backed, negotiation-grade climate insights addressing:
1. **What is changing?** (trends, anomalies, baselines, uncertainty)
2. **What did it cause?** (impact on agriculture, drought, hydropower, GDP, disease, displacement)
3. **What does it demand?** (policy asks: adaptation finance, early warning systems, climate finance, loss-and-damage support)

---

## Repository Structure

```
climate-challenge-week0/
├── .github/workflows/
│   └── ci.yml                      # GitHub Actions: pip install on push to main
├── .vscode/
│   └── settings.json               # VS Code Python interpreter config
├── .gitignore                      # Exclude data/, venv/, CSVs, .ipynb_checkpoints
├── requirements.txt                # Python dependencies (pandas, numpy, matplotlib, etc.)
├── README.md                       # This file
│
├── notebooks/
│   ├── __init__.py
│   ├── README.md
│   ├── ethiopia_eda.ipynb         # Task 2a: Ethiopia EDA (data cleaning + analysis)
│   ├── kenya_eda.ipynb            # Task 2b: Kenya EDA (template clone)
│   ├── sudan_eda.ipynb            # Task 2c: Sudan EDA (template clone)
│   ├── tanzania_eda.ipynb         # Task 2d: Tanzania EDA (template clone)
│   ├── nigeria_eda.ipynb          # Task 2e: Nigeria EDA (template clone)
│   └── compare_countries.ipynb    # Task 3: Cross-country comparison + COP32 findings
│
├── app/
│   └── main.py                    # Streamlit dashboard (bonus)
│
├── src/
│   └── __init__.py               # Python package
│
├── scripts/
│   ├── __init__.py
│   └── README.md
│
└── tests/
    └── __init__.py
```

---

## Quick Start

### Prerequisites
- Python 3.8+ (3.10 recommended)
- Git
- pip (or conda)

### 1. Clone Repository & Setup Environment

**Windows (PowerShell):**
```powershell
# Clone repo
git clone https://github.com/YOUR_USERNAME/climate-challenge-week0.git
cd climate-challenge-week0

# Create virtual environment
python -m venv venv
venv\Scripts\Activate.ps1

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

**macOS/Linux (Bash):**
```bash
git clone https://github.com/YOUR_USERNAME/climate-challenge-week0.git
cd climate-challenge-week0
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Verify Installation
```powershell
python --version          # Check Python version
pip list                  # Verify packages installed
jupyter --version        # Check Jupyter
```

### 3. Run Notebooks

**Option A: Jupyter Notebook (Recommended for development)**
```powershell
jupyter notebook
```
Then navigate to `notebooks/` and open `ethiopia_eda.ipynb`.

**Option B: Jupyter Lab (Enhanced UI)**
```powershell
jupyter lab
```

**Option C: VS Code + Jupyter Extension**
- Open `.ipynb` file in VS Code
- Install "Jupyter" extension (Microsoft)
- Click "Run All" or run cells individually

### 4. Run Streamlit Dashboard (Bonus)
```powershell
streamlit run app/main.py
```
Opens at `http://localhost:8501`

---

## Data Preparation

### Obtain NASA POWER Climate Data

Visit: https://power.larc.nasa.gov/

**Steps:**
1. Select "Daily" temporal resolution
2. Choose parameters: T2M, T2M_MAX, T2M_MIN, T2M_RANGE, PRECTOTCORR, RH2M, WS2M, WS2M_MAX, PS, QV2M
3. Date range: 2015-01-01 to 2026-03-31
4. Select region: Draw bounding box around each country
5. Export as CSV

**Expected files in `data/` folder:**
- `ethiopia.csv`
- `kenya.csv`
- `sudan.csv`
- `tanzania.csv`
- `nigeria.csv`

⚠️ **Important:** Do NOT commit data files. `data/` is in `.gitignore`.

---

## Task Breakdown

### Task 1: Git & Environment Setup ✅
- [x] Initialize Git repository
- [x] Create conventional commits (init, chore, ci, docs)
- [x] Push to `setup-task` branch
- [x] Create Pull Request to main
- [x] Merge setup-task into main

**Git workflow:**
```powershell
git checkout setup-task
git log --oneline           # View commits
git diff main setup-task    # Review changes before merge
```

### Task 2: Data Profiling, Cleaning & EDA (Per-country)
Each notebook performs:
1. **Data Loading & Date Parsing**
   - Replace NASA sentinel `-999` with `np.nan`
   - Convert YEAR+DOY to datetime
   - Add Month and Year columns

2. **Summary Statistics & Missing Values**
   - `df.describe()` with professional interpretation
   - `df.isna().sum()` + missing % analysis
   - Drop duplicates, document findings

3. **Outlier Detection (Z-score)**
   - Flag |Z| > 3 for T2M, T2M_MAX, T2M_MIN, PRECTOTCORR, RH2M, WS2M, WS2M_MAX
   - Decide: drop, cap, or retain with reasoning

4. **Missing Value Handling**
   - Forward fill OR drop rows >30% missing
   - Document tradeoffs

5. **Time Series Analysis**
   - Monthly average T2M line chart (annotate warmest/coolest)
   - Monthly total PRECTOTCORR bar chart (annotate peaks)
   - Markdown interpretation of trends and agricultural impacts

6. **Correlation & Relationships**
   - Correlation heatmap
   - Scatter plots: T2M vs RH2M, T2M_RANGE vs WS2M
   - Identify top 3 correlations + interpretation

7. **Distribution Analysis**
   - Histogram of PRECTOTCORR (log scale if skewed)
   - Bubble chart: T2M vs RH2M (size = PRECTOTCORR)
   - Professional interpretation

8. **Export Cleaned Data**
   - Save `data/<country>_clean.csv`

### Task 3: Cross-Country Comparison
Notebook: `compare_countries.ipynb`

1. **Temperature Trend Comparison**
   - Multi-line chart (all countries on one plot)
   - Summary table: mean, median, std

2. **Precipitation Variability**
   - Side-by-side boxplots
   - Summary statistics table

3. **Extreme Event Frequency**
   - Count days: T2M_MAX > 35°C
   - Count consecutive dry days: PRECTOTCORR < 1 mm
   - Bar charts comparison

4. **Statistical Testing**
   - One-way ANOVA (or Kruskal–Wallis if non-normal)
   - Test T2M differences across countries
   - Interpret p-values

5. **Vulnerability Ranking & COP32 Findings**
   - Create composite ranking (warming trend + precipitation instability + extreme heat + drought)
   - **Five negotiation-grade findings:**
     1. Fastest warming country
     2. Most unstable precipitation country
     3. Climate stress from combined heat + drought
     4. Ethiopia vs neighbors comparison
     5. Which country Ethiopia should champion for climate finance (policy ask)

### Bonus: Streamlit Dashboard
Features:
- Multi-select countries
- Year range slider (2015–2026)
- Variable dropdown (T2M, PRECTOTCORR, T2M_MAX, RH2M)
- Line chart: temperature trends
- Boxplot: precipitation distribution
- Data source: cleaned CSVs (data/ ignored)

---

## Data Dictionary

| Column | Description | Units | Notes |
|--------|-------------|-------|-------|
| YEAR | Year | - | 2015–2026 |
| DOY | Day of year | 1–366 | 1 = Jan 1 |
| T2M | Temperature at 2m | °C | Mean daily |
| T2M_MAX | Max daily temperature | °C | - |
| T2M_MIN | Min daily temperature | °C | - |
| T2M_RANGE | Daily temperature range | °C | T2M_MAX - T2M_MIN |
| PRECTOTCORR | Corrected total precipitation | mm | Daily total |
| RH2M | Relative humidity at 2m | % | 0–100 |
| WS2M | Wind speed at 2m | m/s | Mean daily |
| WS2M_MAX | Max daily wind speed | m/s | - |
| PS | Surface pressure | kPa | - |
| QV2M | Specific humidity at 2m | g/kg | - |

**Missing value sentinel:** NASA POWER uses `-999` (replace with `np.nan`)


## Analytical Framework

Every chart must answer progressively:

| Level | Criteria | Example |
|-------|----------|---------|
| **EDA** | What is changing? | "Temperature increased 0.8°C over 11 years" |
| **Report** | What is changing + What did it cause? | "Temperature rise → increased heat stress → 15% more drought days → crop yield risk" |
| **Position Paper** | What is changing + What caused it + What does it demand? | "Ethiopia warming faster than regional average → demands adapted finance for early warning systems, drought-resistant crops, water infrastructure" |

**Your target:** Position paper level for all major insights.

---

## Best Practices

### Code Quality
- Use PEP 8 style guide
- Add docstrings to functions
- Comment complex logic
- Use type hints (Python 3.9+)

### Notebooks
- Prefix title with H1 (#) markdown
- Add section headers (H2, H3) between analysis steps
- Include assumptions and caveats
- Document data cleaning decisions with reasoning

### Version Control
- Use conventional commits: `type: description`
  - `init:` Initial setup
  - `feat:` New feature
  - `fix:` Bug fix
  - `docs:` Documentation
  - `chore:` Configuration/maintenance
  - `ci:` Automation/CI/CD
  - `refactor:` Code restructuring
  - `test:` Test additions

- Commit frequently (after each major task)
- Write clear, descriptive commit messages

### Data Handling
- **Never** commit CSV files
- Always use relative paths: `data/country.csv` (not absolute paths)
- Verify `.gitignore` includes: `data/`, `*.csv`, `.ipynb_checkpoints/`, `venv/`

---

## Submission Checklist

### Interim Submission (Due: Sunday, 26 Apr 2026, 8:00 PM UTC)
- [ ] GitHub repository created and public
- [ ] `setup-task` branch merged into `main` via Pull Request
- [ ] CI workflow (`.github/workflows/ci.yml`) runs on push
- [ ] README.md complete with setup instructions
- [ ] At least one country EDA notebook started (Ethiopia minimum)
- [ ] Clean data exported locally (not committed)
- [ ] Interim report submitted (below)

### Final Submission
- [ ] All 5 country EDA notebooks complete
- [ ] `compare_countries.ipynb` with COP32 findings
- [ ] Streamlit dashboard deployed
- [ ] Production-ready code (no debug output)
- [ ] Comprehensive README (this file)
- [ ] Final report with policy recommendations

---

## Submission Materials

### Interim Report Template
```
## EthioClimate Analytics – Week 0 Interim Report

### Task 1: Setup & Environment ✅
- Repository: [GitHub link]
- Branch structure: main ← setup-task (merged)
- Commits: 4 conventional commits
- CI status: ✅ Passing

### Task 2: Ethiopia EDA – Approach
- Data source: NASA POWER (2015–2026)
- Records: ~4,000 daily observations
- Cleaning approach:
  - Replace -999 sentinel with NaN
  - Forward-fill missing weather variables
  - Retain physical extremes (heatwaves, heavy rain)
- Key findings (preliminary):
  - [Insert 2–3 main insights]
  - [Expected completion date for other countries]

### Timeline
- Task 2 (all countries): [Target date]
- Task 3 (comparison): [Target date]
- Dashboard & final report: [Target date]
```

---

## Common Mistakes to Avoid

### ❌ Mistake: Committing CSV files
**Fix:** Ensure `data/` is in `.gitignore`, use git rm --cached if already committed

### ❌ Mistake: Not replacing -999 sentinel values
**Fix:** Add step early in notebook: `df = df.replace(-999, np.nan)`

### ❌ Mistake: Absolute file paths
**Fix:** Use relative paths: `pd.read_csv('data/ethiopia.csv')` not `C:\Users\...\data\...`

### ❌ Mistake: No markdown interpretation
**Fix:** After each chart, write 2–3 sentences explaining what it means and why it matters

### ❌ Mistake: Merging without testing
**Fix:** Run CI checks locally: `pip install -r requirements.txt && python --version`

### ❌ Mistake: Treating EDA as final output
**Fix:** Add "So what?" context: link trends to policy demands

---

## Resources

- **NASA POWER:** https://power.larc.nasa.gov/
- **Climate Policy:** https://unfccc.int/
- **Python Data Science:** https://pandas.pydata.org/, https://matplotlib.org/, https://seaborn.pydata.org/
- **Git Guide:** https://git-scm.com/doc
- **Streamlit Docs:** https://docs.streamlit.io/


## Contact & Support

For questions or issues:
1. Check the README first
2. Review notebook comments
3. Consult error messages in detail
4. Search GitHub issues

---

**Prepared:** April 2026  
**Status:** Week 0 Challenge (In Progress)  
**Team:** EthioClimate Analytics
