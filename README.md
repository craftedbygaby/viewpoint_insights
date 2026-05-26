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


## Data Limitations

1. **Brazilian dataset — pre-aggregation by state:** The Ministério do Turismo data aggregates less common state entries into "Outras Unidades da Federação" — meaning only the top states are visible individually. Granular state-level analysis is limited.

2. **UNWTO dataset — annual data only:** The UN Tourism database only provides yearly totals with no monthly or seasonal breakdown. Monthly and seasonal fluctuation analysis is only possible with the Brazilian dataset.

3. **UNWTO dataset — voluntary reporting:** Countries self-report their data to the UN. If a country does not report, their data is missing — this can introduce bias in global comparisons and rankings, particularly for less developed tourism markets.

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

**Note on data sourcing:** The UN Tourism raw Excel file was downloaded directly from [untourism.int](https://www.untourism.int/tourism-statistics/tourism-statistics-database) and processed manually. Values were cross-verified against Our World in Data's published CSV — exact match confirmed. Brazil total arrivals were also cross-verified against the Ministério do Turismo dataset — totals are consistent between both sources.

---

## Project Structure

```
Brazil_Road_Back/
├── 01. Data/          ← raw source files and cleaned datasets
├── 02. Notebooks/     ← Jupyter notebooks (cleaning pipeline and EDA)
├── 03. Visualizations/ ← exported charts from the EDA notebook and Tableau workbook (.twbx)
├── src/               ← reusable Python functions and brand assets
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


---

## Tableau Dashboards

Published on Tableau Public: **[link coming soon]**

The full Tableau workbook (`.twbx`) is also available in the repository for local exploration.

**D1 — World Panorama:** Global arrivals context, continent breakdown, Brazil vs world ranking.

**D2 — Brazil Deep Dive:** Recovery timeline, who visits, entry routes, seasonality heatmap, state map.

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
