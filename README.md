# FAIR Data Science Experiment

## 📌 Project Title

Predicting the Market Value of Football Players Using Various Factors

---

## 📄 Abstract

This project focuses on predicting the market value of football players using machine learning techniques and FAIR data science practices. The experiment analyses multiple factors influencing player valuation, including player attributes, position, club context, league differences, transfers, career progression, and performance statistics.

The project reuses openly accessible football datasets from Mendeley Data and follows FAIR principles to ensure reproducibility, accessibility, interoperability, and reusability.

The workflow includes:

- data ingestion
- preprocessing and cleaning
- exploratory data analysis
- feature engineering
- machine learning model development
- evaluation and validation
- generation of outputs such as predictions, charts, trained models, and performance metrics

The repository also integrates FAIR metadata standards including FAIR4ML, RO-Crate, CodeMeta, Croissant, and Model Cards.

---

## 📁 File Organisation

The repository is structured as follows:

- `data/` → Input datasets used in the experiment
- `src/` → Source code (scripts, notebooks, pipelines)
- `outputs/` → Generated results (figures, predictions, models)
- `docs/` → Documentation and reports
- `config/` → Configuration files (YAML, JSON, environment settings)
- `models/` → Trained machine learning models
- `notebooks/` → Jupyter notebooks used during analysis
- `tests/` → Reproducibility and metadata validation tests
- `dbrepo/` → DBRepo schema and metadata files

---

## 🧾 File Naming Convention

A consistent naming scheme is used across the project.

### 1. Input Data

Format:

```text
data_<source>_<description>_<version>.<ext>
```

Examples:

```text
data_forward_player_valuation_v1.xlsx
data_transfer_value_determinants_v2.xlsx
```

---

### 2. Output Files

#### Figures

```text
fig_<experiment>_<metric>_<date>.png
```

Example:

```text
fig_market_value_model_accuracy_2026.png
```

#### Model Artefacts

```text
model_<algorithm>_<dataset>_<version>.pkl
```

Example:

```text
model_xgboost_player_value_v1.pkl
```

#### Results

```text
results_<experiment>_<version>.csv
```

Example:

```text
results_market_value_predictions_v1.csv
```

---

### 3. Source Code Scripts

Format:

```text
<step>_<task_description>.py
```

Examples:

```text
01_data_cleaning.py
02_feature_engineering.py
03_exploratory_analysis.py
04_model_training.py
05_model_evaluation.py
```

---

### 4. Configuration Files

Format:

```text
config_<purpose>.yaml
```

Example:

```text
config_training.yaml
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/bilalhussain3223/fair-ds-experiment.git
cd fair-ds-experiment
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Reproducing the Experiment

Run the following scripts in order:

```bash
python src/01_data_cleaning.py
python src/02_feature_engineering.py
python src/03_exploratory_analysis.py
python src/04_model_training.py
python src/05_model_evaluation.py
```

Generated outputs will automatically be stored in the `outputs/` directory.

---

## 📊 Inputs and Outputs

### Input Data

The project uses openly accessible football datasets from Mendeley Data.

### Dataset 1

**Forward football player valuation**

DOI:
https://doi.org/10.17632/cgc33scxg7.1

License:
CC BY 4.0

### Dataset 2

**Transfer Value Determinants**

DOI:
https://doi.org/10.17632/3btg6ptc7b.2

License:
CC BY 4.0

---

### Input Features

The datasets include attributes such as:

- Player age
- Position
- Nationality
- Club
- League
- Market value
- Matches played
- Goals
- Assists
- Minutes played
- Transfer history
- Social media metrics
- Career progression indicators

---

### Generated Outputs

The experiment produces:

- Histograms
- Correlation plots
- Performance comparison charts
- Prediction CSV files
- Trained machine learning models
- Performance evaluation metrics
- Regression evaluation reports
- Visualisations and analytical summaries

Example outputs:

```text
outputs/model_performance.png
outputs/predictions.csv
outputs/regression_metrics.txt
outputs/feature_importance.png
```

---

## 🗄️ DBRepo Integration

The project includes a structured DBRepo schema for managing and organising football player valuation data.

### DBRepo Tables

- `source_dataset`
- `player`
- `club`
- `position`
- `nationality`
- `season`
- `forward_player_valuation`
- `transfer_value_observation`

The schema and ER diagram are available in the `dbrepo/` directory.

---

## 🔁 Reproducibility

The repository is structured to ensure reproducibility of the experiment. All preprocessing, training, and evaluation steps are documented and version controlled.

Metadata standards and FAIR documentation files are included to improve discoverability and reuse of the experiment outputs.

The project includes:

- structured folder organisation
- documented workflows
- version-controlled notebooks and scripts
- FAIR metadata files
- reproducibility tests
- data provenance tracking

---

## 📚 FAIR Metadata Standards

The project integrates the following FAIR-related metadata standards:

- RO-Crate
- CodeMeta
- FAIR4ML
- Croissant
- Model Cards

These metadata artefacts improve interoperability, machine readability, discoverability, and long-term reuse of the experiment.

---

## 📄 Documentation

The repository includes additional documentation files:

- `README.md`
- `docs/model-card.md`
- `docs/unit-mapping.md`
- `docs/dbrepo-verification.md`
- `docs/final-dmp.pdf`
- `ro-crate-metadata.json`
- `codemeta.json`
- `fair4ml.json`

---

# DBRepo REST API Reimplementation

## Overview

The original experiment loaded datasets from local CSV/Excel files using pandas.

To satisfy T2.6, the pipeline was fully reimplemented to retrieve data exclusively through the DBRepo REST API. All local file reads (`pd.read_csv`, `pd.read_excel`) were deprecated and replaced with:

- DBRepo view retrieval
- REST API access
- local pandas reconstruction of denormalized ML-ready datasets because of current DBRepo SDK mapper limitations affecting large multi-table joins

Final workflow:

```text
DBRepo Views
    ↓
REST API Retrieval
    ↓
Local pandas merges
    ↓
ML-ready DataFrames
```

No local CSV or Excel files are used in the final experiment pipeline.

---

## API Configuration

### Base URL

```text
https://test.dbrepo.tuwien.ac.at
```

### Endpoints Used

| Endpoint                                             | Purpose                  |
| ---------------------------------------------------- | ------------------------ |
| `/api/v1/database/{database_id}/view`                | Retrieve available views |
| `/api/v1/database/{database_id}/view/{view_id}/data` | Retrieve view data       |

### Authentication

Authentication is handled through the DBRepo Python SDK using username/password credentials:

```python
client = RestClient(
    base_url="https://test.dbrepo.tuwien.ac.at",
    username=USERNAME,
    password=PASSWORD,
)
```

Credentials are supplied at runtime and are not stored in the repository.

---

## Views Used in the Final Experiment

### Primary ML View

#### `vw_transfer_features`

Main view used in the final regression experiment.

Contains:

- transfer-market numerical features
- player-performance metrics
- target variable: `value_end_mln`
- FK identifiers for lookup reconstruction

Used in:

- preprocessing
- feature engineering
- model training
- evaluation

Retrieved through:

```python
load_transfer_dataset(client)
```

Final dataframe:

```python
merged_transfer_df
```

---

### Lookup Views Used During Reconstruction

The following views were retrieved separately and merged locally through pandas:

| View                    | Purpose                        |
| ----------------------- | ------------------------------ |
| `vw_player_lookup`      | reconstruct `player_name`      |
| `vw_club_lookup`        | reconstruct `club_name`        |
| `vw_position_lookup`    | reconstruct `position_name`    |
| `vw_nationality_lookup` | reconstruct `nationality_name` |

Example reconstruction:

```python
merged_transfer_df = (
    transfer_df
    .merge(player_df, on="player_id", how="left")
    .merge(club_df, on="club_id", how="left")
    .merge(position_df, on="position_id", how="left")
    .merge(nationality_df, on="nationality_id", how="left")
)
```

---

### Additional Implemented Views

The following views were implemented as part of the DBRepo architecture but were not directly used in the final regression workflow:

| View                       | Purpose                            |
| -------------------------- | ---------------------------------- |
| `vw_forward_features`      | Dataset 1 valuation analysis       |
| `vw_combined_player_value` | Cross-dataset exploratory analysis |

Associated reconstructed dataframes:

- `merged_forward_df`
- `merged_combined_df`

---

### Reusable Loader Module

All REST API retrieval and dataframe reconstruction logic was centralized inside:

```text
notebooks/utils/dbrepo_loader.py
```

Main functions:

- `get_client()`
- `fetch_view_df()`
- `load_lookup_tables()`
- `load_transfer_dataset()`
- `load_forward_dataset()`
- `load_combined_dataset()`

---

### Error Handling

Robust error handling was implemented for:

- connection failures
- unexpected response codes
- missing views
- DBRepo internal server errors
- empty responses

### Verification

The REST API implementation preserves:

- identical preprocessing logic
- identical train/test splitting
- identical feature engineering
- identical model configuration

The reimplemented API-based workflow reproduces the same analytical pipeline and equivalent experimental behavior as the original local-file implementation while fully satisfying the DBRepo integration requirements.

# Croissant Metadata

Croissant JSON-LD metadata records were created for both datasets used in the experiment:

- `croissant/forward_valuation_croissant.json`
- `croissant/transfer_value_croissant.json`

The metadata records describe:

- dataset structure
- field names
- datatypes
- units
- dataset provenance
- distributions

## 📜 Licenses

### Input Data

The reused football datasets are distributed under the original CC BY 4.0 licenses provided by the dataset publishers.

### Source Code

The source code in this repository is licensed under the MIT License.

### Generated Outputs

Generated outputs, trained models, visualisations, and evaluation artefacts are shared under the CC BY 4.0 License where legally permissible.

---

## 👥 Contributors

| Role | Name                   | Student ID | ORCID                                 |
| ---- | ---------------------- | ---------- | ------------------------------------- | ------------------------------------- |
| A    | Konrad Szegedy         | 12024699   | https://orcid.org/0009-0009-2299-752X |
| B    | Muhammad Athar Riaz    | 12449141   | Not available                         |
| C    | Muhammad Bilal Hussain | 12442081   | https://orcid.org/0009-0000-2512-9167 |
| D    | Edeh Ekene             | 12451120   | Not available                         | https://orcid.org/0009-0007-2481-389X |

---

## 🔗 Repository

GitHub Repository:

https://github.com/bilalhussain3223/fair-ds-experiment

---

## 📌 DOI

### Model DOI

https://doi.org/10.70124/c35xx-9pb93

Additional repository and dataset DOIs will be added after final repository release and Zenodo integration.

---

## 📄 Citation

A `CITATION.cff` file is included to support proper citation of this experiment and related outputs.

---

## 🎯 Project Goal

The main objective of this project is to investigate which factors most strongly influence football player market value and to develop a robust predictive machine learning model capable of estimating player valuations based on multiple sporting and contextual variables.

The project also demonstrates the integration of FAIR principles into a complete machine learning workflow, improving transparency, reproducibility, and reusability of data science experiments.
