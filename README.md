# Predicting the Market Value of Football Players Using Various Factors

[![DOI](https://zenodo.org/badge/1224517548.svg)](https://doi.org/10.5281/zenodo.20357906)

---

## Abstract

This project predicts the market value of football players using machine learning and FAIR data science practices. It analyses factors including player age, position, club context, nationality, career progression, and performance statistics across multiple seasons.

The project reuses two openly licensed football datasets from Mendeley Data, stores and queries them via DBRepo, and trains an XGBoost regression model to predict end-of-season transfer market value (`value_end_mln`). All data infrastructure, metadata, and experiment outputs follow FAIR principles to ensure reproducibility, accessibility, interoperability, and reusability.

The repository integrates FAIR metadata standards: FAIR4ML, RO-Crate, CodeMeta, Croissant, and Model Cards.

---

## Repository Structure

```
fair-ds-experiment/
├── notebooks/
│   ├── Project.ipynb                        # Original experiment (local file reads)
│   ├── Project_api.ipynb                    # T2.6 reimplementation (DBRepo REST API)
│   ├── dbrepo_create_tables.ipynb           # T2.1 schema creation in DBRepo
│   ├── dbrepo_normalize_clean_export.ipynb  # T2.5 normalisation and CSV export
│   ├── T2_4_create_views.ipynb              # T2.4 view creation and API data retrieval
│   ├── models/                              # Trained model artefacts
│   ├── normalized_exports/                  # Normalised CSVs ready for DBRepo upload
│   └── outputs/                             # Evaluation metrics, predictions, figures
├── dbrepo/
│   └── schema.sql                           # 3NF schema SQL (CREATE TABLE statements)
├── croissant/
│   ├── forward_valuation_croissant.json     # Croissant metadata — Dataset 1
│   └── transfer_value_croissant.json        # Croissant metadata — Dataset 2
├── docs/
│   ├── model-card.md                        # Model Card for XGBoost regressor
│   ├── unit-mapping.md                      # SI unit ontology mappings (T2.3)
│   └── dbrepo-verification.md               # DBRepo schema verification notes
├── ro-crate-metadata.json                   # RO-Crate experiment package description
├── codemeta.json                            # CodeMeta 2.0 software metadata
├── fair4ml.json                             # FAIR4ML model metadata
├── CITATION.cff                             # Citation file referencing Zenodo DOI
├── LICENSE                                  # MIT License (source code)
└── README.md
```

---

## File Naming Convention

### Input Datasets (`data/`)

```
data_<source>_<description>_<version>.<ext>
```

Examples:

```
data_forward_player_valuation_v1.xlsx
data_transfer_value_determinants_v2.xlsx
```

### Output Files (`notebooks/outputs/`)

| Type                | Format                                          | Example                                       |
| ------------------- | ----------------------------------------------- | --------------------------------------------- |
| Figures             | `fig_<experiment>_<metric>_<date>.png`          | `fig_market_value_accuracy_2026.png`          |
| Model artefacts     | `model_<algorithm>_<dataset>_<version>.pkl`     | `model_xgboost_player_value_v1.pkl`           |
| API model artefacts | `model_<algorithm>_<dataset>_<version>_api.pkl` | `model_xgboost_player_value_v1_api.pkl`       |
| Results             | `results_<experiment>_<version>.csv`            | `results_market_value_predictions_v1.csv`     |
| API results         | `results_<experiment>_<version>_api.csv`        | `results_market_value_predictions_v1_api.csv` |

The `_api` suffix distinguishes outputs produced by the DBRepo API reimplementation (`Project_api.ipynb`) from those produced by the original local-file version (`Project.ipynb`).

### Source Code (`notebooks/`)

```
<step>_<task_description>.ipynb / .py
```

Examples:

```
dbrepo_create_tables.ipynb
dbrepo_normalize_clean_export.ipynb
T2_4_create_views.ipynb
Project.ipynb
Project_api.ipynb
```

### Configuration Files (`config/`)

```
config_<purpose>.yaml
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/bilalhussain3223/fair-ds-experiment.git
cd fair-ds-experiment
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Reproducing the Experiment

### Option A — Original local-file version

Place the two input Excel files in `data/`:

- `data_forward_player_valuation_v1.xlsx` (from DOI: 10.17632/cgc33scxg7.1)
- `data_transfer_value_determinants_v2.xlsx` (from DOI: 10.17632/3btg6ptc7b.2)

Then open and run `notebooks/Project.ipynb` top to bottom.

Outputs will be saved to `notebooks/outputs/`:

- `evaluation_metrics.csv`
- `predictions.csv`

And the trained model to `notebooks/models/`:

- `final_model.pkl`

### Option B — DBRepo API reimplementation (T2.6)

Ensure you have a DBRepo account with read access to database `598ce585-d8b5-4a97-8f19-cb085d4a5b1e`.

Open and run `notebooks/Project_api.ipynb`. When prompted, enter your DBRepo credentials. No local data files are required — all data is retrieved from the DBRepo REST API.

API outputs are saved with the `_api` suffix alongside the local outputs:

- `notebooks/outputs/evaluation_metrics_api.csv`
- `notebooks/outputs/predictions_api.csv`
- `notebooks/outputs/transfer_data_from_api.csv` (raw API data audit trail)
- `notebooks/models/final_model_api.pkl`

---

## Input Datasets

Both datasets are reused from Mendeley Data under CC BY 4.0. The group is not the original publisher or rights holder.

### Dataset 1 — Forward Football Player Valuation

| Field     | Value                                 |
| --------- | ------------------------------------- |
| Authors   | Hugo Briseño; José Carlos Rivera      |
| Publisher | Mendeley Data                         |
| Version   | V1                                    |
| DOI       | https://doi.org/10.17632/cgc33scxg7.1 |
| Licence   | CC BY 4.0                             |
| File      | `soccerplayers.xlsx`                  |

Contains 438 forward players with attributes: age, club, market value, matches played, goals, assists, minutes played, minutes per goal, Instagram followers, European league participation.

### Dataset 2 — Transfer Value Determinants

| Field     | Value                                 |
| --------- | ------------------------------------- |
| Author    | Ronald Nisanov                        |
| Publisher | Mendeley Data                         |
| Version   | V2                                    |
| DOI       | https://doi.org/10.17632/3btg6ptc7b.2 |
| Licence   | CC BY 4.0                             |
| File      | `Nisanov_final_data.xlsx`             |

Contains 2,502 player-season observations across 2019–2023 with attributes: position, nationality, club, age, height, total games, goals, assists, minutes, penalty kicks, club performance, relegation, transfer values (start, end, delta) in EUR and millions. **Primary ML training dataset.**

---

## Generated Outputs

| File                                           | Description                                     |
| ---------------------------------------------- | ----------------------------------------------- |
| `notebooks/outputs/evaluation_metrics.csv`     | R², MSE, RMSE, MAE (local version)              |
| `notebooks/outputs/predictions.csv`            | Per-player test set predictions (local version) |
| `notebooks/outputs/evaluation_metrics_api.csv` | Same metrics from DBRepo API version            |
| `notebooks/outputs/predictions_api.csv`        | Same predictions from DBRepo API version        |
| `notebooks/outputs/transfer_data_from_api.csv` | Raw data retrieved from DBRepo (audit trail)    |
| `notebooks/models/final_model.pkl`             | Trained XGBoost pipeline (local version)        |
| `notebooks/models/final_model_api.pkl`         | Trained XGBoost pipeline (API version)          |

---

## DBRepo Data Infrastructure

### Database

| Field        | Value                                                                          |
| ------------ | ------------------------------------------------------------------------------ |
| Instance     | TU Wien DBRepo (test)                                                          |
| Database URL | https://test.dbrepo.tuwien.ac.at/database/598ce585-d8b5-4a97-8f19-cb085d4a5b1e |
| Owner        | Edeh Ekene (Student D)                                                         |
| Schema       | `dbrepo/schema.sql`                                                            |

### Tables

The database implements a 3NF schema with 8 tables:

| Table                        | Description                                     | Rows  |
| ---------------------------- | ----------------------------------------------- | ----- |
| `source_dataset`             | Provenance metadata for both source datasets    | 2     |
| `player`                     | Deduplicated player name lookup                 | —     |
| `club`                       | Deduplicated club name lookup                   | —     |
| `position`                   | Position name lookup (Dataset 2)                | —     |
| `nationality`                | Nationality name lookup (Dataset 2)             | —     |
| `season`                     | Season years 2019–2023 (pre-inserted by schema) | 5     |
| `forward_player_valuation`   | Dataset 1 fact table                            | 438   |
| `transfer_value_observation` | Dataset 2 fact table                            | 2,502 |

The schema SQL with all CREATE TABLE statements is in `dbrepo/schema.sql`. The ER diagram is in `docs/`.

### Views (T2.4)

Created via `notebooks/T2_4_create_views.ipynb`:

| View                       | Primary Table                | Target Variable    | Purpose                           |
| -------------------------- | ---------------------------- | ------------------ | --------------------------------- |
| `vw_transfer_features`     | `transfer_value_observation` | `value_end_mln`    | Primary ML training data          |
| `vw_forward_features`      | `forward_player_valuation`   | `market_value_mln` | Dataset 1 ML features             |
| `vw_combined_player_value` | `forward_player_valuation`   | `market_value_mln` | Cross-dataset exploration         |
| `vw_player_lookup`         | `player`                     | —                  | player_id → player_name           |
| `vw_club_lookup`           | `club`                       | —                  | club_id → club_name               |
| `vw_position_lookup`       | `position`                   | —                  | position_id → position_name       |
| `vw_nationality_lookup`    | `nationality`                | —                  | nationality_id → nationality_name |

Views expose fact table columns without joins (a workaround for a DBRepo SDK mapper limitation with inhomogeneous table schemas). Lookup data is merged locally in pandas after REST API retrieval.

---

## DBRepo REST API Reimplementation (T2.6)

The original experiment (`Project.ipynb`) reads from local Excel files. The reimplemented version (`Project_api.ipynb`) retrieves all data exclusively from the DBRepo REST API — no local file reads are permitted.

### API Base URL

```
https://test.dbrepo.tuwien.ac.at
```

### Endpoints Used

| Endpoint                                         | Method | Purpose          |
| ------------------------------------------------ | ------ | ---------------- |
| `/api/v1/database/{db_id}/view`                  | GET    | List all views   |
| `/api/v1/database/{db_id}/view/{view_id}/data`   | GET    | Fetch view data  |
| `/api/v1/database/{db_id}/table`                 | GET    | List all tables  |
| `/api/v1/database/{db_id}/table/{table_id}/data` | GET    | Fetch table data |

**Database ID:** `598ce585-d8b5-4a97-8f19-cb085d4a5b1e`

### Authentication

HTTP Basic Auth via the DBRepo Python SDK (`dbrepo==1.13.3`). Credentials are entered at runtime and never stored in the repository.

```python
client = RestClient(
    endpoint="https://test.dbrepo.tuwien.ac.at",
    username=USERNAME,
    password=password,   # entered via getpass() at runtime
)
```

### Data Loading Workflow

```
DBRepo REST API
    ↓
get_view_data()        →  vw_transfer_features (2,502 rows)
get_view_data()        →  vw_forward_features (438 rows)
get_table_data()       →  player, club, position, nationality lookup tables
    ↓
pandas merge           →  denormalised ML-ready DataFrames
    ↓
Column rename          →  match original Project.ipynb column names
    ↓
XGBoost training       →  identical pipeline to local version
```

Note: lookup views (`vw_player_lookup` etc.) return HTTP 500 when tables are small due to a DBRepo server bug. These are fetched via `get_table_data()` instead of the view API.

### Results Equivalence

The API reimplementation produces results within 8% of the original local-file version:

| Metric | Local version | API version | Difference |
| ------ | ------------- | ----------- | ---------- |
| R²     | 0.8702        | 0.8689      | 0.15%      |
| RMSE   | 8.0957        | 8.6637      | 7.02%      |
| MAE    | 5.5635        | 5.7851      | 3.98%      |

The minor difference is attributable to two storage effects: (1) `DECIMAL(12,3)` precision rounding applied to `value_start_mln` during database storage, and (2) 17 rows where `start_value_eur` was NULL in the source data but stored as `0.0` in DBRepo due to a NOT NULL column constraint set during table creation. These rows are treated differently by the `SimpleImputer(strategy='median')`, causing a small but measurable shift in predictions. The results are considered equivalent. See Section 12 of `Project_api.ipynb` for the full equivalence check.

### Data Provenance

| Item                  | Value                                                                          |
| --------------------- | ------------------------------------------------------------------------------ |
| Database              | https://test.dbrepo.tuwien.ac.at/database/598ce585-d8b5-4a97-8f19-cb085d4a5b1e |
| Primary view          | `vw_transfer_features`                                                         |
| Source dataset DOI    | https://doi.org/10.17632/3btg6ptc7b.2                                          |
| Source dataset DOI    | https://doi.org/10.17632/cgc33scxg7.1                                          |
| Model deposit (TUWRD) | https://doi.org/10.70124/c35xx-9pb93                                           |
| Code DOI (Zenodo)     | https://doi.org/10.5281/zenodo.20357906                                        |
| SDK version           | dbrepo==1.13.3                                                                 |
| Raw API data saved to | `notebooks/outputs/transfer_data_from_api.csv`                                 |

---

## Croissant Metadata (T3.4)

Croissant JSON-LD metadata records are provided for both input datasets:

| File                                         | Dataset                                       |
| -------------------------------------------- | --------------------------------------------- |
| `croissant/forward_valuation_croissant.json` | Forward football player valuation (Dataset 1) |
| `croissant/transfer_value_croissant.json`    | Transfer Value Determinants (Dataset 2)       |

Each record describes field names, data types, units (referencing QUDT URIs from T2.3), distribution information, and licence.

---

## FAIR Metadata Standards

| Standard   | File                     | Purpose                                                          |
| ---------- | ------------------------ | ---------------------------------------------------------------- |
| RO-Crate   | `ro-crate-metadata.json` | Experiment package description with all entity relationships     |
| CodeMeta   | `codemeta.json`          | Software metadata (authors, dependencies, licence, version)      |
| FAIR4ML    | `fair4ml.json`           | ML model metadata (hyperparameters, metrics, training data DOI)  |
| Croissant  | `croissant/`             | Dataset field-level metadata with units and distributions        |
| Model Card | `docs/model-card.md`     | Model description, intended use, evaluation results, limitations |

---

## Licences

### Input Data

Both source datasets are licensed under **CC BY 4.0** by their original publishers (Mendeley Data). The group reuses the data under the terms of this licence. CC BY 4.0 permits redistribution and adaptation with attribution. It does not impose ShareAlike obligations, so the output data licence is not constrained by the input licence.

### Source Code

The source code in this repository is licensed under the **MIT Licence**. See `LICENSE`. MIT is compatible with CC BY 4.0 input data — it imposes no restrictions that conflict with the attribution-only requirement of CC BY 4.0.

### Generated Outputs

Trained models, predictions, evaluation metrics, and figures are shared under **CC BY 4.0**. This licence is stated in every TUWRD deposit record and in the RO-Crate metadata.

---

## Deposits and Persistent Identifiers

| Artefact                 | Repository    | DOI / URL                                                                      |
| ------------------------ | ------------- | ------------------------------------------------------------------------------ |
| Code repository (Zenodo) | Zenodo        | https://doi.org/10.5281/zenodo.20357906                                        |
| Trained model            | TUWRD (test)  | https://doi.org/10.70124/c35xx-9pb93                                           |
| Generated output data    | TUWRD (test)  | _(add DOI after B completes T3.10)_                                            |
| DMP record               | TUWRD (test)  | _(add DOI after A completes T4.4)_                                             |
| DBRepo database          | DBRepo (test) | https://test.dbrepo.tuwien.ac.at/database/598ce585-d8b5-4a97-8f19-cb085d4a5b1e |
| Dataset 1                | Mendeley Data | https://doi.org/10.17632/cgc33scxg7.1                                          |
| Dataset 2                | Mendeley Data | https://doi.org/10.17632/3btg6ptc7b.2                                          |

---

## Contributors

| Role | Name                   | Student ID | ORCID                                 |
| ---- | ---------------------- | ---------- | ------------------------------------- |
| A    | Konrad Szegedy         | 12024699   | https://orcid.org/0009-0009-2299-752X |
| B    | Muhammad Athar Riaz    | 12449141   | _(not available)_                     |
| C    | Muhammad Bilal Hussain | 12442081   | https://orcid.org/0009-0000-2512-9167 |
| D    | Edeh Ekene             | 12451120   | https://orcid.org/0009-0007-2481-389X |

---

## Citation

A `CITATION.cff` file is included in the repository root. To cite this experiment:

```
Szegedy, K., Riaz, M. A., Hussain, M. B., & Edeh, E. (2026).
Predicting the Market Value of Football Players Using Various Factors.
Zenodo. https://doi.org/10.5281/zenodo.20357906
```

---

## GitHub Repository

https://github.com/Ekene-James/fair-ds-experiment
