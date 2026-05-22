<img src="src/viewpoint_insights_logo.svg" alt="Viewpoint Insights logo" width="420"/>

# Brazil's Road Back
### International Tourism Recovery Analysis — 2015–2024

---

## Author

- Gabriela Cascione

---

## Overview

End-to-end data analytics project analyzing the recovery of international tourism in Brazil following the COVID-19 pandemic. Using over a decade of official government data, this project investigates who is traveling to Brazil again, how they arrive, and whether the country has fully returned to pre-pandemic levels.

---

## Key Findings

*To be updated as analysis progresses.*

---

## Business Question

> *Has Brazilian international tourism fully recovered from COVID-19, and who is driving that recovery?*

**Audience:** Brazil's tourism board (Embratur / Ministério do Turismo) and state-level tourism planners.

### Research Questions
1. How did total arrivals collapse in 2020–2021 and recover through 2024? Are we back to 2019 levels?
2. Which countries sent the most tourists pre-COVID vs post-COVID? Which markets recovered fastest?
3. Has the balance between air, land, sea and river entries changed since COVID?
4. Did the seasonal pattern shift after COVID? Are there new shoulder-season opportunities?
5. How does Brazil's recovery compare to the global average?

---

## Datasets

| Dataset | Source | Coverage | Used For |
|---|---|---|---|
| Chegadas de Turistas Internacionais | Ministério do Turismo / Polícia Federal | 2015–2024, monthly | All core analysis |
| UN Tourism Statistics Database — Inbound Arrivals | UN World Tourism Organization (UNWTO) | 1995–2024, annual | Global context |

**Note on data sourcing:** The UN Tourism raw Excel file was downloaded directly from [untourism.int](https://www.untourism.int/tourism-statistics/tourism-statistics-database) and processed manually. Values were cross-verified against Our World in Data's published CSV — exact match confirmed.

---

## Project Structure

```
Brazil_Road_Back/
│
├── 01. data/
│   ├── raw/                          ← original source files, never modified
│   └── cleaned/                      ← output of cleaning pipeline
│
├── 02. notebooks/
│   ├── data_discovery.ipynb              ← initial data exploration
│   ├── data_cleaning_wrangling.ipynb     ← full cleaning pipeline
│   └── EDA.ipynb                         ← exploratory data analysis
│
├── 03. Visualizations/               ← exported charts from EDA notebook
│
├── src/
│   ├── functions.py                  ← reusable cleaning functions
│   └── viewpoint_insights_logo.svg   ← brand assets
│
├── .gitignore
└── README.md
```

---

## Pipeline

```
Data Collection → Cleaning & Wrangling → EDA → Tableau Dashboard → Story
                                                        ↓
                                            (Extra) ML Forecasting → Streamlit App
```

| Step | Notebook | Tool | Description |
|---|---|---|---|
| Data Collection | — | — | 10 yearly CSVs (Ministério do Turismo) + UN Tourism Excel file |
| Cleaning & Wrangling | `data_cleaning_wrangling.ipynb` | Python / pandas | Standardize columns, translate Portuguese→English, handle duplicates, create covid_period and season flags, merge 10 yearly files, align UNWTO country names and add continent column |
| EDA & Statistical Analysis | `EDA.ipynb` | Python / matplotlib / seaborn | Univariate (distribution, skewness, kurtosis, boxplot), bivariate (arrivals over time, by country, by route), multivariate (pre/post COVID comparison, seasonality by country, entry route trends) |
| Dashboard | — | Tableau | 5 interactive charts |
| Story | — | Tableau | Narrative arc: past → collapse → recovery → future |
| ML Forecasting ⭐ | — | Python / scikit-learn | Arrival prediction model |
| Streamlit App ⭐ | — | Streamlit | Interactive forecast tool |

*⭐ Extra features — completed if time allows*

---

## Tableau Dashboard

Published on Tableau Public: **[link coming soon]**

| Chart | Type | Insight |
|---|---|---|
| Recovery Timeline | Line chart (2015–2024) | Full collapse and bounce-back of arrivals |
| Who's Traveling Again | Ranked bar chart | Pre vs post-COVID by origin country |
| How They Arrive | Stacked bar / area | Air vs land vs sea recovery |
| Seasonality Heatmap | Heatmap (month × year) | How peak months shifted |
| Brazil vs World | Indexed line chart | Brazil's recovery vs global average |

---

## How to Run

### Requirements
```bash
pip install pandas numpy matplotlib seaborn openpyxl jupyter
```

### Steps
```bash
# 1. Clone the repo
git clone https://github.com/craftedbygaby/brazil-road-back.git
cd brazil-road-back

# 2. Add raw data files to /01. data/raw/
# (see Datasets section for download links)

# 3. Run notebooks in order
jupyter notebook
```

---

## References

- Ministério do Turismo — [dados.turismo.gov.br](https://dados.turismo.gov.br/dataset/chegada-de-turistas-internacionais)
- UN World Tourism Organization — [untourism.int](https://www.untourism.int/tourism-statistics/tourism-statistics-database)

---

*All analysis is for educational and portfolio purposes only.*
