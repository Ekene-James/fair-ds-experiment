# Views Documentation

## Project
**Predicting the Market Value of Football Players Using Various Factors**

This document describes all DBRepo views, lookup views, local pandas merge operations, and the final ML-ready dataframes used throughout the project.

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

`forward_player_valuation`

---

## Target Variable

`market_value_mln`

---

# 1.2 `vw_transfer_features`

## Purpose

Stores the primary transfer-market and player-performance attributes from Dataset 2.

Acts as the primary machine-learning feature source for the regression workflow.

Used later to reconstruct:
- `merged_transfer_df`

---

## Source Table

`transfer_value_observation`

---

## Target Variable

`value_end_mln`

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

# 2. Lookup Views

## `vw_player_lookup`
- `player_id`
- `player_name`

## `vw_club_lookup`
- `club_id`
- `club_name`

## `vw_position_lookup`
- `position_id`
- `position_name`

## `vw_nationality_lookup`
- `nationality_id`
- `nationality_name`

---

# 3. Local pandas Reconstruction

## Reconstruction of `merged_forward_df`

Base:
- `forward_df`
- from `vw_forward_features`

Merge chain:
1. merge with `player_df` on `player_id`
2. merge with `club_df` on `club_id`

Final dataframe:
- `merged_forward_df`

Used in:
- exploratory analysis
- valuation analysis
- supplementary ML experiments

---

## Reconstruction of `merged_transfer_df`

Base:
- `transfer_df`
- from `vw_transfer_features`

Merge chain:
1. merge with `player_df` on `player_id`
2. merge with `club_df` on `club_id`
3. merge with `position_df` on `position_id`
4. merge with `nationality_df` on `nationality_id`

Final dataframe:
- `merged_transfer_df`

Used in:
- T2.6 API reimplementation
- model training
- preprocessing
- feature engineering
- regression experiments
- evaluation pipeline

---

## Reconstruction of `merged_combined_df`

Base:
- `combined_df`
- from `vw_combined_player_value`

Merge chain:
1. merge with `player_df` on `player_id`
2. merge with `club_df` on `club_id`

Final dataframe:
- `merged_combined_df`

Used in:
- cross-dataset exploratory analysis
- feature-fusion experiments
- advanced ML experimentation

---

# 4. Architecture Summary

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
