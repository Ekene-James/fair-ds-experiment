# Views Documentation

## Project

**Predicting the Market Value of Football Players Using Various Factors**

This document describes:

- all DBRepo fact views
- all lookup views
- the exact columns stored in each view
- local pandas merge operations
- final ML-ready dataframes used throughout the project

The implementation follows a hybrid architecture:

1. Normalized fact and lookup views are stored in DBRepo
2. Data is retrieved through the DBRepo REST API
3. Final denormalized ML-ready datasets are reconstructed locally through pandas merge operations

This design was chosen due to current DBRepo SDK mapper limitations when combining large-schema tables with joined lookup tables.

---

# 1. Core Fact Views

These views contain the primary numerical and machine-learning relevant attributes.

---

# 1.1 `vw_forward_features`

## Purpose

Stores the primary valuation and performance attributes from Dataset 1.

Acts as the main fact table for the forward-player valuation workflow.

Used later to reconstruct:

- `merged_forward_df`

---

## Source Table

```text
forward_player_valuation
```

---

## Target Variable

```text
market_value_mln
```

---

## Fields Stored in `vw_forward_features`

| Field                     |
| ------------------------- |
| `forward_valuation_id`    |
| `source_dataset_id`       |
| `player_id`               |
| `club_id`                 |
| `player_age_years`        |
| `market_value_mln`        |
| `value_rank`              |
| `plays_in_europe`         |
| `matches_played`          |
| `goals`                   |
| `assists`                 |
| `minutes_per_goal`        |
| `minutes_played`          |
| `instagram_followers_mln` |

---

# 1.2 `vw_transfer_features`

## Purpose

Stores the primary transfer-market and player-performance attributes from Dataset 2.

Acts as the primary machine-learning feature source for the regression workflow.

Used later to reconstruct:

- `merged_transfer_df`

---

## Source Table

```text
transfer_value_observation
```

---

## Target Variable

```text
value_end_mln
```

---

## Fields Stored in `vw_transfer_features`

| Field                     |
| ------------------------- |
| `transfer_observation_id` |
| `source_dataset_id`       |
| `player_id`               |
| `position_id`             |
| `nationality_id`          |
| `club_id`                 |
| `season_year`             |
| `age_then_years`          |
| `age_now_years`           |
| `club_performance`        |
| `relegation`              |
| `success_or_not`          |
| `total_games`             |
| `assists`                 |
| `penalty_kicks`           |
| `total_minutes`           |
| `total_goals`             |
| `height_cm`               |
| `start_value_eur`         |
| `end_value_eur`           |
| `delta_value_eur`         |
| `value_start_mln`         |
| `value_end_mln`           |
| `value_delta_mln`         |

---

# 1.3 `vw_combined_player_value`

## Purpose

Experimental combined-feature view containing valuation-related numerical features shared across both datasets.

Used for:

- exploratory analysis
- feature fusion
- optional advanced ML workflows

Used later to reconstruct:

- `merged_combined_df`

---

## Source Tables

```text
forward_player_valuation
transfer_value_observation
```

---

## Fields Stored in `vw_combined_player_value`

| Field            |
| ---------------- |
| `player_id`      |
| `club_id`        |
| `age_years`      |
| `goals`          |
| `assists`        |
| `minutes_played` |
| `market_value`   |
| `dataset_source` |

---

# 2. Lookup Views

Lookup views contain lightweight categorical metadata used later during local dataframe reconstruction.

---

# 2.1 `vw_player_lookup`

## Source Table

```text
player
```

---

## Fields Stored in `vw_player_lookup`

| Field         |
| ------------- |
| `player_id`   |
| `player_name` |

---

# 2.2 `vw_club_lookup`

## Source Table

```text
club
```

---

## Fields Stored in `vw_club_lookup`

| Field       |
| ----------- |
| `club_id`   |
| `club_name` |

---

# 2.3 `vw_position_lookup`

## Source Table

```text
position
```

---

## Fields Stored in `vw_position_lookup`

| Field           |
| --------------- |
| `position_id`   |
| `position_name` |

---

# 2.4 `vw_nationality_lookup`

## Source Table

```text
nationality
```

---

## Fields Stored in `vw_nationality_lookup`

| Field              |
| ------------------ |
| `nationality_id`   |
| `nationality_name` |

---

# 3. REST API Retrieval

All data retrieval is performed exclusively through the DBRepo REST API.

No local CSV or Excel reads are used in the final implementation.

---

## API Base URL

```text
https://test.dbrepo.tuwien.ac.at
```

---

## Endpoints Used

| Endpoint                                             | Purpose            |
| ---------------------------------------------------- | ------------------ |
| `/api/v1/database/{database_id}/view`                | Retrieve views     |
| `/api/v1/database/{database_id}/view/{view_id}/data` | Retrieve view data |

---

# 4. Local pandas Reconstruction

The final denormalized machine-learning datasets are reconstructed locally through pandas merge operations after REST API retrieval.

---

# 4.1 Reconstruction of `merged_forward_df`

## Base DataFrame

```python
forward_df
```

Retrieved from:

```text
vw_forward_features
```

---

## Columns in `forward_df`

| Column                    |
| ------------------------- |
| `forward_valuation_id`    |
| `source_dataset_id`       |
| `player_id`               |
| `club_id`                 |
| `player_age_years`        |
| `market_value_mln`        |
| `value_rank`              |
| `plays_in_europe`         |
| `matches_played`          |
| `goals`                   |
| `assists`                 |
| `minutes_per_goal`        |
| `minutes_played`          |
| `instagram_followers_mln` |

---

## Merge 1

```python
forward_df.merge(
    player_df,
    on="player_id",
    how="left"
)
```

### Columns Added

| Column        |
| ------------- |
| `player_name` |

---

## Merge 2

```python
.merge(
    club_df,
    on="club_id",
    how="left"
)
```

### Columns Added

| Column      |
| ----------- |
| `club_name` |

---

## Final DataFrame

```python
merged_forward_df
```

---

## Final Columns in `merged_forward_df`

| Column                        |
| ----------------------------- |
| All columns from `forward_df` |
| `player_name`                 |
| `club_name`                   |

---

## Used In

- exploratory analysis
- valuation analysis
- supplementary ML experiments

---

# 4.2 Reconstruction of `merged_transfer_df`

## Base DataFrame

```python
transfer_df
```

Retrieved from:

```text
vw_transfer_features
```

---

## Columns in `transfer_df`

| Column                    |
| ------------------------- |
| `transfer_observation_id` |
| `source_dataset_id`       |
| `player_id`               |
| `position_id`             |
| `nationality_id`          |
| `club_id`                 |
| `season_year`             |
| `age_then_years`          |
| `age_now_years`           |
| `club_performance`        |
| `relegation`              |
| `success_or_not`          |
| `total_games`             |
| `assists`                 |
| `penalty_kicks`           |
| `total_minutes`           |
| `total_goals`             |
| `height_cm`               |
| `start_value_eur`         |
| `end_value_eur`           |
| `delta_value_eur`         |
| `value_start_mln`         |
| `value_end_mln`           |
| `value_delta_mln`         |

---

## Merge 1

```python
transfer_df.merge(
    player_df,
    on="player_id",
    how="left"
)
```

### Columns Added

| Column        |
| ------------- |
| `player_name` |

---

## Merge 2

```python
.merge(
    club_df,
    on="club_id",
    how="left"
)
```

### Columns Added

| Column      |
| ----------- |
| `club_name` |

---

## Merge 3

```python
.merge(
    position_df,
    on="position_id",
    how="left"
)
```

### Columns Added

| Column          |
| --------------- |
| `position_name` |

---

## Merge 4

```python
.merge(
    nationality_df,
    on="nationality_id",
    how="left"
)
```

### Columns Added

| Column             |
| ------------------ |
| `nationality_name` |

---

## Final DataFrame

```python
merged_transfer_df
```

---

## Final Columns in `merged_transfer_df`

| Column                         |
| ------------------------------ |
| All columns from `transfer_df` |
| `player_name`                  |
| `club_name`                    |
| `position_name`                |
| `nationality_name`             |

---

## Used In

This is the PRIMARY ML dataframe used in:

- T2.6 API reimplementation
- model training
- preprocessing
- feature engineering
- regression experiments
- evaluation pipeline

---

# 4.3 Reconstruction of `merged_combined_df`

## Base DataFrame

```python
combined_df
```

Retrieved from:

```text
vw_combined_player_value
```

---

## Columns in `combined_df`

| Column           |
| ---------------- |
| `player_id`      |
| `club_id`        |
| `age_years`      |
| `goals`          |
| `assists`        |
| `minutes_played` |
| `market_value`   |
| `dataset_source` |

---

## Merge 1

```python
combined_df.merge(
    player_df,
    on="player_id",
    how="left"
)
```

### Columns Added

| Column        |
| ------------- |
| `player_name` |

---

## Merge 2

```python
.merge(
    club_df,
    on="club_id",
    how="left"
)
```

### Columns Added

| Column      |
| ----------- |
| `club_name` |

---

## Final DataFrame

```python
merged_combined_df
```

---

## Final Columns in `merged_combined_df`

| Column                         |
| ------------------------------ |
| All columns from `combined_df` |
| `player_name`                  |
| `club_name`                    |

---

## Used In

- cross-dataset exploratory analysis
- optional feature-fusion experiments
- advanced ML experimentation

---

# 5. Architecture Summary

```text
3NF Tables
    ↓
DBRepo Views
    ↓
REST API Retrieval
    ↓
Local pandas Merges
    ↓
ML-Ready DataFrames
```

This workflow preserves:

- normalization
- reproducibility
- FAIR infrastructure integration
- REST API-only access
- machine-learning compatibility
