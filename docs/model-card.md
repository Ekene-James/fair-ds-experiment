# Model Card: XGBoost Football Player Market Value Prediction Model

**Model artefact:** `notebooks/models/final_model.pkl` (local version), `notebooks/models/final_model_api.pkl` (API version)  
**Model deposit DOI:** https://doi.org/10.70124/g7pw4-cd077  
**FAIR4ML metadata:** `fair4ml-metadata.json`  
**Repository:** https://github.com/Ekene-James/fair-ds-experiment

---

## Model Description

This model predicts the end-of-season transfer market value of football players in
millions EUR (`value_end_mln`) using an XGBoost gradient boosting regression pipeline.
The pipeline is implemented as a `sklearn.pipeline.Pipeline` wrapping a
`SimpleImputer` (median strategy for numeric features, most-frequent for categorical),
a `OneHotEncoder` (handle_unknown=ignore) for categorical features, and an
`XGBRegressor` (xgboost 3.2.0, scikit-learn 1.8.0). The model is trained on the
Transfer Value Determinants dataset (Nisanov, 2025) covering seasons 2019–2023,
using 14 features including player age, position, nationality, club, height,
performance statistics, and starting transfer value.

Two model artefacts are produced: the local-file version (`final_model.pkl`) trained
from local Excel files, and the API version (`final_model_api.pkl`) trained using data
retrieved exclusively from the DBRepo REST API as part of the T2.6 reimplementation
requirement. Both use identical hyperparameters and train/test splits. The small
difference in evaluation metrics between the two versions is attributable to
DECIMAL(12,3) rounding in database storage and 17 rows where a nullable value was
stored as 0.0 due to a NOT NULL column constraint.

The trained model serialised as a `joblib`/`pickle` file can be loaded with
`joblib.load('notebooks/models/final_model.pkl')` and used to predict player transfer
values from a pandas DataFrame containing the 14 input features. Full hyperparameter
details are documented in `fair4ml-metadata.json`.

---

## Intended Use

The intended use of this model is to support an educational FAIR Data Science experiment
demonstrating reproducible machine learning on reused open football datasets. It shows
a complete workflow from raw data ingestion through DBRepo infrastructure, normalised
storage, API-based retrieval, model training, evaluation, and FAIR metadata
documentation. The model can be used to analyse how structured football performance
and transfer data relates to market value.

The model is intended for academic, exploratory, and reproducibility purposes only.
It demonstrates the integration of FAIR principles into a machine learning pipeline,
including use of DBRepo for structured data storage, Zenodo for code archiving, TUWRD
for model deposit, and metadata standards including FAIR4ML, RO-Crate, CodeMeta,
Croissant, and Model Cards. Results should be interpreted as part of a course project
rather than as a professional football valuation product.

Potential secondary uses include benchmarking regression approaches on sports tabular
data, testing DBRepo API integration patterns, or as a template for FAIR-compliant
ML experiment documentation.

---

## Out-of-Scope Uses

The model must not be used for real transfer negotiations, scouting decisions, contract
valuations, salary benchmarking, or any investment decisions involving individual
players or clubs. Its predictions are estimates derived from historical data under
specific modelling assumptions and should not be treated as authoritative valuations
of any individual. The model has not been validated for operational use in any
professional football context.

The model is not designed for use outside the European football transfer market context
from which the training data was drawn. It must not be applied to other sports, other
labour markets, or financial valuation problems without complete retraining, feature
re-engineering, and independent evaluation. Using the model on data from leagues,
seasons, or player types not represented in the 2019–2023 training data is out of
scope.

The model is also not suitable as a standalone automated decision-making system.
Important real-world factors influencing player market values — including remaining
contract length, injury history, media exposure, agent relationships, and club financial
situation — are absent from the training features. Any deployment beyond educational
demonstration would require substantial additional validation and feature enrichment.

---

## Training Data

The primary training dataset is **Transfer Value Determinants** by Ronald Nisanov
(2025), Mendeley Data V2, DOI: [10.17632/3btg6ptc7b.2](https://doi.org/10.17632/3btg6ptc7b.2),
licence: CC BY 4.0. It contains 2,502 player-season observations across seasons
2019–2023 with features: player position, nationality, club name, age at start of
season, current age, total games, assists, penalty kicks, total minutes, total goals,
height (cm), starting transfer value (EUR and millions), and season year. The target
variable is `value_end_mln` (end-of-season transfer value in millions EUR).

The secondary input dataset is **Forward Football Player Valuation** by Hugo Briseño
and José Carlos Rivera (2024), Mendeley Data V1, DOI:
[10.17632/cgc33scxg7.1](https://doi.org/10.17632/cgc33scxg7.1), licence: CC BY 4.0.
This dataset covers 438 forward players and is documented as a project input but is
not used as training data for this regression model. Both datasets are stored in the
TU Wien DBRepo instance (database ID: `598ce585-d8b5-4a97-8f19-cb085d4a5b1e`) and
are neither collected nor published by the project group — the group re-uses them under
the original CC BY 4.0 licence.

The train/test split uses `test_size=0.30, random_state=42`, resulting in 1,751
training records and 751 test records. Numeric features are imputed using median
strategy; categorical features (position, nationality, club name) are imputed with
most-frequent and one-hot encoded. No feature selection or dimensionality reduction
is applied.

---

## Evaluation Results

This is a regression task. Precision, recall, and F1 are classification metrics and
are not applicable. The equivalent regression metrics are R² (coefficient of
determination), Root Mean Squared Error (RMSE), and Mean Absolute Error (MAE), all
reported on the held-out 30% test set. R² measures the proportion of variance in
`value_end_mln` explained by the model; RMSE and MAE are in the same unit as the
target variable (millions EUR).

The table below reports results for both model versions. The API version shows a small
difference attributable to DECIMAL(12,3) rounding during database storage of
`value_start_mln` and 17 rows where `start_value_eur` was stored as `0.0` instead of
NULL due to a NOT NULL column constraint applied during table creation. The results are
considered equivalent within an 8% tolerance as required by T2.6.

| Model version      | Target        |     R² | RMSE (M EUR) | MAE (M EUR) |   MSE | Train rows | Test rows |
| ------------------ | ------------- | -----: | -----------: | ----------: | ----: | ---------: | --------: |
| Local file version | value_end_mln | 0.8702 |       8.0957 |      5.5635 | 65.54 |       1751 |       751 |
| DBRepo API version | value_end_mln | 0.8689 |       8.6637 |      5.7851 | 75.06 |       1751 |       751 |

Full evaluation output files: `notebooks/outputs/evaluation_metrics.csv` (local
version) and `notebooks/outputs/evaluation_metrics_api.csv` (API version).

---

## Limitations

The model is limited by the quality, completeness, and representativeness of the
training data. Seasons 2019–2023 from a predominantly European football context are
covered; the model may not generalise to other leagues, seasons, or player profiles
outside this distribution. The `club_performance`, `relegation`, and `success_or_not`
features are only available for the 2019 season (NULL in 2020–2023), which reduces
the signal available for those features.

Market value is not a purely objective measurement — it reflects visibility, media
attention, agent influence, and transfer market dynamics that are not captured by
performance statistics alone. The model reproduces patterns and biases present in
the historical transfer market data, including any systematic over- or
under-valuation of players from certain nationalities, leagues, or positions. The
small number of estimators (`n_estimators=20`) and shallow trees (`max_depth=3`) limit
model complexity, which reduces overfitting risk but may also limit predictive capacity
for edge cases.

Seventeen rows have unknown `start_value_eur` in the source data; in the API version
these were stored as `0.0` rather than NULL due to a database constraint, introducing
a systematic bias in the `start_value` feature for those observations. This is
documented in the FAIR4ML metadata and the T4.5 DMP comparison. Further validation
against more recent seasons and additional feature engineering would be needed before
any operational use.

---

## Ethical Considerations

The project uses data about identifiable professional football players. Although the
source data is publicly available and openly licensed under CC BY 4.0, model
predictions about individual players must be presented carefully and in context.
Predictions should not be interpreted as objective assessments of a player's ability,
potential, or professional worth.

The model may reproduce and amplify existing biases in historical transfer market
data — systematic patterns in how players of certain nationalities, positions, or
clubs are valued may be reflected in model outputs. For this reason, aggregated
performance metrics are more appropriate for reporting than individual-level
predictions, and player names in outputs should only be included where necessary
for reproducibility or interpretation. Any publication of player-level predictions
should clearly state the educational and experimental context.

The project does not involve collection of new personal data, automated decision-making
about individuals, or processing of sensitive personal data categories. No ethics
approval is required for the reuse of publicly licensed datasets for academic
demonstration purposes. This section will be updated if the scope or use of the model
changes.

---

## Licence

**Input data:** Both source datasets are published under CC BY 4.0 by their original
publishers (Mendeley Data). The group re-uses the data under these terms. Any reuse of
the source datasets must include attribution to the original creators: Briseño & Rivera
(DOI: [10.17632/cgc33scxg7.1](https://doi.org/10.17632/cgc33scxg7.1)) and Nisanov
(DOI: [10.17632/3btg6ptc7b.2](https://doi.org/10.17632/3btg6ptc7b.2)).

**Source code:** The experiment code, notebooks, and metadata files in this repository
are licensed under the **MIT Licence** (see `LICENSE` in the repository root). MIT is
compatible with CC BY 4.0 — it imposes no restrictions that conflict with the
attribution-only requirement of the input data licence.

**Generated outputs:** The trained model artefacts (`final_model.pkl`,
`final_model_api.pkl`), predictions, and evaluation metrics are licensed under
**CC BY 4.0**. The model deposit is available at
https://doi.org/10.70124/g7pw4-cd077 and the generated data deposit at
https://doi.org/10.5281/zenodo.20377147. These licences are stated in every TUWRD
and Zenodo deposit record and in the RO-Crate metadata (`ro-crate-metadata.json`).
