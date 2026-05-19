# FAIR Data Science Experiment

## 📌 Project Title

Predicting Traffic Accident Severity in Austria Using Machine Learning

---

## 📄 Abstract

This project focuses on predicting traffic accident severity in Austria using machine learning techniques. The experiment uses openly available datasets from the Austrian Open Government Data Portal and follows FAIR data principles to ensure reproducibility, accessibility, interoperability, and reusability.

The workflow includes data preprocessing, feature engineering, model training, evaluation, and generation of outputs such as confusion matrices, predictions, and performance metrics. The project also integrates FAIR metadata standards including FAIR4ML, RO-Crate, CodeMeta, Croissant, and Model Cards.

---

## 📁 File Organisation

The repository is structured as follows:

- `data/` → Input datasets used in the experiment
- `src/` → Source code (scripts, notebooks, pipelines)
- `outputs/` → Generated results (figures, predictions, models)
- `docs/` → Documentation and reports
- `config/` → Configuration files (YAML, JSON, environment settings)

---

## 🧾 File Naming Convention

A consistent naming scheme is used across the project.

### 1. Input Data

Format:

```text
data_<source>_<description>_<version>.<ext>
```

Example:

```text
data_austria_traffic_accidents_v1.csv
```

---

### 2. Output Files

#### Figures

```text
fig_<experiment>_<metric>_<date>.png
```

Example:

```text
fig_accident_model_accuracy_2026.png
```

#### Model Artefacts

```text
model_<algorithm>_<dataset>_<version>.pkl
```

Example:

```text
model_randomforest_accidents_v1.pkl
```

#### Results

```text
results_<experiment>_<version>.csv
```

Example:

```text
results_accident_predictions_v1.csv
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
03_model_training.py
04_model_evaluation.py
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
python src/03_model_training.py
python src/04_model_evaluation.py
```

Generated outputs will automatically be stored in the `outputs/` directory.

---

## 📊 Inputs and Outputs

### Input Data

The project uses traffic accident datasets obtained from the Austrian Open Government Data Portal:

https://www.data.gv.at

The dataset contains:
- Accident date and time
- Location information
- Weather conditions
- Road type
- Number of vehicles involved
- Accident severity labels

---

### Generated Outputs

The experiment produces:

- Histograms
- Confusion matrices
- Prediction CSV files
- Trained machine learning models
- Performance evaluation metrics
- Classification reports

Example outputs:

```text
outputs/confusion_matrix.png
outputs/predictions.csv
outputs/model_accuracy.txt
```

---

## 🔁 Reproducibility

The repository is structured to ensure reproducibility of the experiment. All preprocessing, training, and evaluation steps are documented and version controlled.

Metadata standards and FAIR documentation files are included to improve discoverability and reuse of the experiment outputs.

---

## 📚 FAIR Metadata Standards

The project integrates the following FAIR-related metadata standards:

- RO-Crate
- CodeMeta
- FAIR4ML
- Croissant
- Model Cards

These metadata artefacts improve interoperability, reusability, and machine readability of the experiment.

---

## 📜 Licenses

### Input Data

The input dataset is obtained from the Austrian Open Government Data Portal and follows the original license provided by the data publisher.

### Source Code

The source code in this repository is licensed under the MIT License.

### Generated Outputs

Generated outputs, trained models, and evaluation artefacts are shared under the CC BY 4.0 License.

---

## 👥 Contributors

| Role | Name | Student ID |
|---|---|---|
| A | Konrad Szegedy | 12024699 |
| B | Muhammad Athar Riaz | 12449141 |
| C | Muhammad Bilal Hussain | 12442081 |
| D | Edeh Ekene | 12451120 |

---

## 🔗 Repository

GitHub Repository:

https://github.com/bilalhussain3223/fair-ds-experiment

---

## 📌 DOI

Zenodo DOI will be added after repository release and Zenodo integration.

---

## 📄 Citation

A `CITATION.cff` file will be added to support proper citation of this experiment and related outputs.
