<div align="center">

# 🦠 COVID Patients Analysis 🦠

**Exploratory Data Analysis of COVID-19 Patient Records**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

## 📖 Project Overview

This repository contains an **exploratory data analysis (EDA)** of **COVID-19 patient data**, aimed at uncovering trends, patterns, risk factors, outcomes, and demographic insights from real-world records.

The project focuses on:
- Cleaning and preprocessing raw patient-level data
- Visualizing key variables (age, symptoms, comorbidities, recovery/death rates, etc.)
- Identifying correlations (e.g., age vs severity, location vs cases)
- Generating interpretable charts and statistical summaries

Perfect for students, researchers, or anyone studying pandemic epidemiology or healthcare data analysis.

---

## 🛠️ Technologies & Libraries Used

| Library/Tool       | Purpose                              | Link / Badge                                      |
|--------------------|--------------------------------------|---------------------------------------------------|
| Python             | Core language                        | ![Python](https://img.shields.io/badge/Python-3.8+-blue) |
| Jupyter Notebook   | Interactive analysis & presentation  | ![Jupyter](https://img.shields.io/badge/Jupyter-F37626) |
|  NumPy   | Numerical operations                 | —                                                 |

Dependencies → see [`requirements.txt`](requirements.txt) (if present) or install manually.

---
## 📊 About the Data

This project analyzes **daily COVID-19 hospital and ICU occupancy data** for Ontario, Canada, broken down by health region (`oh_region`). The records cover **April 2020 – November 2024** (~4.5 years, ~10,200 rows), sourced from official Ontario health reporting (likely public health or ministry dashboards).

### Key Dataset Characteristics

- **Time span**: 2020-04-01 to 2024-11-25
- **Regions** (`oh_region`): CENTRAL, EAST, NORTH EAST, NORTH WEST, TORONTO, WEST
- **Rows**: ~10,200 (daily entries × 6 regions)
- **Granularity**: One row per region per day
- **Missing values**: None apparent in core numeric fields
- **Data types note**: Several ICU columns are stored as strings/objects (possibly due to "N/A", "<5" suppression, or formatting), but most are numeric in practice.

### Main Columns Explained

| Column Name                | Data Type | Description                                                                 | Importance / Why Analyzed                              | Typical Values / Notes                                      |
|----------------------------|-----------|-----------------------------------------------------------------------------|--------------------------------------------------------|-------------------------------------------------------------|
| _id                        | Integer   | Unique record identifier (auto-incrementing)                                | Internal key / ordering                                | 30361 → 40560                                               |
| date                       | String (ISO) | Date of the daily snapshot (YYYY-MM-DD)                                    | Time-series analysis, trends, waves                    | 2020-04-01T00:00:00 to 2024-11-25T00:00:00                 |
| oh_region                  | String    | Ontario Health region name                                                  | Regional comparison (e.g. Toronto vs rural)            | CENTRAL, EAST, NORTH EAST, NORTH WEST, TORONTO, WEST        |
| icu_current_covid          | Integer/String | Current number of ICU beds occupied by **active/confirmed COVID patients** | Primary indicator of acute COVID pressure on ICUs      | 0–100+ (peaks in 2020–2021, lower in 2023–2024)             |
| icu_current_covid_vented   | Integer/String | Of the above, how many are on mechanical ventilation                        | Severity of current cases                              | Usually 50–80% of icu_current_covid in early waves          |
| hospitalizations           | Integer   | Total patients currently hospitalized with COVID (acute + ICU)              | Overall hospital burden                                | 0–1200+ (highest during 2020–2022 waves)                    |
| icu_crci_total             | Integer/String | Total ICU beds occupied by **CRCI** (COVID-Related Critical Illness) patients | Broader COVID-related critical care load               | Includes current + recovering; often higher than current    |
| icu_crci_total_vented      | Integer/String | Of the CRCI total, how many ventilated                                      | Ventilation demand over time                           | —                                                           |
| icu_former_covid           | Integer/String | ICU beds occupied by patients who **previously had COVID** (recovered but still in ICU) | Long COVID / post-acute impact                         | Usually low (0–15), appears more from mid-2020              |
| icu_former_covid_vented    | Integer/String | Of the former COVID, how many ventilated                                    | Severity of prolonged critical care                    | Very low numbers                                            |

**Key Insights from Structure:**
- Focus is on **ICU pressure** (current COVID vs former/recovered) and **hospital load**.
- Early data (2020) shows rapid rise in ICU_current_covid, then decline through 2021–2022, with smaller fluctuations later.
- Some fields occasionally appear as strings (possibly "<5" or "N/A" in raw source), but most values are clean integers.
- **No case counts, deaths, or testing data** — purely **occupancy / burden** metrics.
- Excellent for time-series visualization (line plots by region), comparisons (Toronto vs others), and identifying peak waves.

To explore the full dataset yourself, run in a notebook:

```python
import pandas as pd
df = pd.read_csv("path/to/your_file.csv")
print(df.info())
print(df['oh_region'].value_counts())
print(df.groupby('oh_region')['icu_current_covid'].max())  # peak ICU per region
df['date'] = pd.to_datetime(df['date'])  # fix date type
```
---


## 📁 Repository Structure

```text
covid-patients-analysis/
├── .vscode/                # VS Code settings (optional)
├── Data/                   # Raw & processed COVID-19 patient datasets (.csv)
├── src/                    # Python scripts / modules (data utils, functions)
├── notebooks/              # Jupyter Notebooks (.ipynb) – main analysis files
├── outputs/                # Saved charts, tables, dashboards (png, pdf, etc.)
├── scripts/                # Automation / ETL scripts
├── requirements.txt        # Python dependencies (if added)
└── README.md               # This file
```

---

## 📊 Key Features

✅ Clean preprocessing of raw COVID data  
✅ Exploratory analysis with plots and trend lines  
✅ Correlation and statistical insights  
✅ Summary dashboards ready for publication  
✅ Notebook examples for reproducible research

---



## 💾 Installation & Setup

```markdown
## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Basic familiarity with Jupyter Notebook
- (Optional) Git installed to clone the repo

### Step-by-step instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/kirmanioussema12/covid-patients-analysis.git
   cd covid-patients-analysis

1. **Clone the repo**

```bash
git clone https://github.com/kirmanioussema12/covid-patients-analysis.git
cd covid-patients-analysis

## 📂 Repository Structure
