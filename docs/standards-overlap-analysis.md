# T3.11 — Metadata Standards Overlap and Complementarity Analysis

This document analyses the overlap, complementarity, conflicts, and inconsistencies
between the five metadata standards applied in this project:
**RO-Crate**, **CodeMeta**, **FAIR4ML**, **Croissant**, and **Model Card**.

The analysis covers all ten pairwise combinations. For each pair:

- **(a)** Fields appearing in both standards
- **(b)** Fields unique to each standard
- **(c)** Conflicts or inconsistencies found in this project

---

## Summary Table

| Field concept             | RO-Crate | CodeMeta | FAIR4ML | Croissant | Model Card |
| ------------------------- | :------: | :------: | :-----: | :-------: | :--------: |
| Title / name              |    ✓     |    ✓     |    ✓    |     ✓     |     ✓      |
| Description               |    ✓     |    ✓     |    —    |     ✓     |     ✓      |
| Creator / author          |    ✓     |    ✓     |    ✓    |     ✓     |     —      |
| Licence                   |    ✓     |    ✓     |    ✓    |     ✓     |     ✓      |
| Version                   |    ✓     |    ✓     |    ✓    |     ✓     |     —      |
| Identifier / DOI          |    ✓     |    ✓     |    ✓    |     ✓     |     ✓      |
| Training dataset DOI      |    ✓     |    —     |    ✓    |     —     |     ✓      |
| Evaluation metrics        |    —     |    —     |    ✓    |     —     |     ✓      |
| Hyperparameters           |    —     |    —     |    ✓    |     —     |     —      |
| Preprocessing steps       |    —     |    —     |    ✓    |     —     |     —      |
| Train/test split          |    —     |    —     |    ✓    |     —     |     —      |
| Features / fields         |    —     |    —     |    ✓    |     ✓     |     —      |
| Field-level units (QUDT)  |    —     |    —     |    —    |     ✓     |     —      |
| Field-level data types    |    —     |    —     |    —    |     ✓     |     —      |
| Software dependencies     |    —     |    ✓     |    —    |     —     |     —      |
| Runtime platform          |    —     |    ✓     |    —    |     —     |     —      |
| Code repository URL       |    ✓     |    ✓     |    —    |     —     |     —      |
| Intended use              |    —     |    —     |    ✓    |     —     |     ✓      |
| Out-of-scope uses         |    —     |    —     |    ✓    |     —     |     ✓      |
| Known limitations         |    —     |    —     |    ✓    |     —     |     ✓      |
| Ethical considerations    |    —     |    —     |    —    |     —     |     ✓      |
| Entity relationships      |    ✓     |    —     |    —    |     —     |     —      |
| Distribution / access URL |    ✓     |    —     |    —    |     ✓     |     —      |
| Keywords                  |    ✓     |    ✓     |    —    |     ✓     |     —      |
| Date published            |    ✓     |    ✓     |    —    |     ✓     |     —      |

---

## Pairwise Analysis

### 1. RO-Crate ↔ CodeMeta

**(a) Fields in both:**
`name`, `creator`/`author`, `license`, `version`, `identifier`, `codeRepository`,
`keywords`, `datePublished`, `description`

**(b) Unique fields:**

| RO-Crate only                          | CodeMeta only                                          |
| -------------------------------------- | ------------------------------------------------------ |
| `hasPart` (entity graph relationships) | `softwareRequirements` (dependency list with versions) |
| `isBasedOn` (provenance links)         | `runtimePlatform`                                      |
| `input` / `output` (workflow links)    | `programmingLanguage` (structured)                     |
| `@type` graph (multiple entity types)  | `developmentStatus`                                    |
| `sameAs` (cross-repository links)      | `releaseNotes`                                         |

**(c) Conflicts / inconsistencies:**
In this project, `creator` in RO-Crate uses fragment IDs (`#edeh-ekene`) with ORCID
in the `identifier` field. CodeMeta uses `author` with `@id` as the ORCID URI directly.
The same people are represented in two structurally different ways. RO-Crate also
expresses licence as a `@id` URL reference to a named entity, while CodeMeta uses an
SPDX licence URL string. Both refer to MIT but the format differs.

---

### 2. RO-Crate ↔ FAIR4ML

**(a) Fields in both:**
`name`, `creator`, `license`, `identifier`/`doi`, `description`,
training dataset reference (via `isBasedOn` in RO-Crate; `training_dataset.doi` in FAIR4ML)

**(b) Unique fields:**

| RO-Crate only                                            | FAIR4ML only                        |
| -------------------------------------------------------- | ----------------------------------- |
| Entity graph (`hasPart`, `isBasedOn`, `input`, `output`) | `hyperparameters`                   |
| `sameAs` cross-links                                     | `preprocessing`                     |
| `datePublished`                                          | `train_test_split`                  |
| `encodingFormat`                                         | `evaluation_metrics` (structured)   |
|                                                          | `features_used` (with types)        |
|                                                          | `algorithm_library_version`         |
|                                                          | `intended_use`, `out_of_scope_uses` |
|                                                          | `known_limitations`                 |

**(c) Conflicts / inconsistencies:**
RO-Crate lists evaluation metrics only indirectly through the output file entity
(`evaluation_metrics.csv`). FAIR4ML contains the actual numeric values inline.
A machine reader of only the RO-Crate cannot determine model performance without
fetching the linked CSV. This is a significant complementarity gap: RO-Crate documents
what exists, FAIR4ML documents what it means.

---

### 3. RO-Crate ↔ Croissant

**(a) Fields in both:**
`name`, `description`, `license`, `creator`, `publisher`, `identifier`,
`datePublished`, `distribution` (access URL and format), `version`

**(b) Unique fields:**

| RO-Crate only                  | Croissant only                              |
| ------------------------------ | ------------------------------------------- |
| Entity relationship graph      | `recordSet` with field-level schema         |
| `isBasedOn`, `input`, `output` | Field `dataType` (sc:Text, sc:Number, etc.) |
| `sameAs`                       | Field-level `unitCode` (QUDT URIs)          |
| Multiple `@type` entities      | `source` linking fields to distribution     |

**(c) Conflicts / inconsistencies:**
Both standards describe the same two datasets but at different granularity levels.
RO-Crate describes the datasets as entities with relationships to the experiment.
Croissant describes their internal structure field by field. In this project, the
`distribution.contentUrl` in both Croissant files points to the Mendeley Data page,
while RO-Crate's `distribution` entity points to the local file path. These describe
the same distribution from different perspectives (remote source vs. local copy) and
are complementary rather than conflicting.

---

### 4. RO-Crate ↔ Model Card

**(a) Fields in both:**
`name`, `license`, `identifier` (dataset DOIs), `creator` (training data authors),
training dataset reference

**(b) Unique fields:**

| RO-Crate only             | Model Card only                           |
| ------------------------- | ----------------------------------------- |
| Entity relationship graph | Intended use (narrative)                  |
| `encodingFormat`          | Out-of-scope uses                         |
| `sameAs`, `hasPart`       | Ethical considerations                    |
| `datePublished`           | Evaluation metrics table (human-readable) |
| `input` / `output` links  | Limitations (narrative)                   |

**(c) Conflicts / inconsistencies:**
The Model Card states evaluation metrics as prose and a markdown table.
RO-Crate references the evaluation metrics CSV as an output entity but contains no
metric values. A reviewer checking only RO-Crate would need to download the CSV to
find the actual numbers. The Model Card provides them inline but in a non-machine-
readable format. FAIR4ML bridges this gap by providing machine-readable metrics.

---

### 5. CodeMeta ↔ FAIR4ML

**(a) Fields in both:**
`name`, `license`, `version`, `identifier`, `author`/`creator`

**(b) Unique fields:**

| CodeMeta only                                 | FAIR4ML only                        |
| --------------------------------------------- | ----------------------------------- |
| `softwareRequirements` (full dependency list) | `hyperparameters`                   |
| `runtimePlatform`                             | `evaluation_metrics`                |
| `programmingLanguage`                         | `features_used`                     |
| `codeRepository`                              | `preprocessing`                     |
| `developmentStatus`                           | `train_test_split`                  |
| `releaseNotes`                                | `training_dataset` (with DOI)       |
|                                               | `intended_use`, `known_limitations` |

**(c) Conflicts / inconsistencies:**
CodeMeta describes the software package as a whole (all notebooks, all scripts).
FAIR4ML describes a specific trained model artefact within that package. They operate
at different levels of granularity and do not conflict directly. However, the
`author` list in CodeMeta and the `contributor` concept in FAIR4ML cover the same
people but in different formats — CodeMeta uses `givenName`/`familyName` with ORCID
`@id`; FAIR4ML uses plain name strings in an array. This creates a consistency
risk if names are spelled differently.

---

### 6. CodeMeta ↔ Croissant

**(a) Fields in both:**
`name`, `license`, `version`, `creator`, `keywords`, `datePublished`, `identifier`

**(b) Unique fields:**

| CodeMeta only          | Croissant only                      |
| ---------------------- | ----------------------------------- |
| `softwareRequirements` | `recordSet` with field-level schema |
| `runtimePlatform`      | Field `dataType`                    |
| `programmingLanguage`  | Field `unitCode` (QUDT URIs)        |
| `codeRepository`       | `distribution` file objects         |
| `developmentStatus`    | `source` linking                    |

**(c) Conflicts / inconsistencies:**
These two standards describe fundamentally different artefact types — CodeMeta
describes software, Croissant describes datasets. There is minimal semantic overlap
beyond administrative metadata. No direct conflicts were found in this project.
The `license` field uses a full URL in Croissant (`https://creativecommons.org/...`)
and an SPDX URL in CodeMeta (`https://spdx.org/licenses/MIT.html`) — different
licence types but consistently expressed as URLs in both.

---

### 7. CodeMeta ↔ Model Card

**(a) Fields in both:**
`name`, `license`, `identifier`, `author` (training data authors referenced)

**(b) Unique fields:**

| CodeMeta only          | Model Card only           |
| ---------------------- | ------------------------- |
| `softwareRequirements` | Intended use (narrative)  |
| `runtimePlatform`      | Out-of-scope uses         |
| `programmingLanguage`  | Ethical considerations    |
| `codeRepository`       | Evaluation metrics table  |
| `developmentStatus`    | Known limitations         |
| `releaseNotes`         | Training data description |

**(c) Conflicts / inconsistencies:**
CodeMeta and Model Card address largely non-overlapping concerns. CodeMeta is
about the software artefact; Model Card is about the model artefact produced by
running that software. They are strongly complementary. The only potential
inconsistency is that CodeMeta's `author` describes who wrote the code, while Model
Card implicitly attributes the model to the same group — but neither standard
provides a field to distinguish "code author" from "model trainer."

---

### 8. FAIR4ML ↔ Croissant

**(a) Fields in both:**
`name`, `license`, `identifier` (dataset DOIs), `features_used` / `field` schema
(both describe input features, though at different levels)

**(b) Unique fields:**

| FAIR4ML only                        | Croissant only               |
| ----------------------------------- | ---------------------------- |
| `hyperparameters`                   | `recordSet` structure        |
| `evaluation_metrics`                | Field `dataType`             |
| `preprocessing`                     | Field `unitCode` (QUDT URIs) |
| `train_test_split`                  | `distribution` file objects  |
| `intended_use`, `known_limitations` | `source` linking             |
| `algorithm_library_version`         | `publisher`                  |

**(c) Conflicts / inconsistencies:**
FAIR4ML's `features_used` lists 14 feature names with types and descriptions.
Croissant's `recordSet.field` entries describe 22 columns from the raw dataset —
all raw columns, not only those selected as model features. The two provide
complementary but non-identical views: Croissant describes the full dataset schema,
FAIR4ML describes the subset actually used for ML. This is not a conflict but
requires a reader to cross-reference both files to understand the feature selection
step. The `unitCode` in Croissant uses QUDT URIs; FAIR4ML uses plain string unit
descriptions — the same measurement concepts are expressed in machine-readable form
in Croissant and in human-readable form in FAIR4ML.

---

### 9. FAIR4ML ↔ Model Card

**(a) Fields in both:**
`name`, `license`, `identifier` (dataset DOIs), `training_dataset` (DOI reference),
`evaluation_metrics` / evaluation results table, `intended_use`, `known_limitations`,
`out_of_scope_uses`, `features_used` / training data description

**(b) Unique fields:**

| FAIR4ML only                    | Model Card only                            |
| ------------------------------- | ------------------------------------------ |
| `hyperparameters` (structured)  | Ethical considerations                     |
| `preprocessing` (structured)    | Prose narrative for each section           |
| `train_test_split` (structured) | Out-of-scope uses (explicit section)       |
| `algorithm_library_version`     | Training data section (detailed narrative) |
| Machine-readable metric values  | Human-readable metrics table               |

**(c) Conflicts / inconsistencies:**
FAIR4ML and Model Card are the most semantically overlapping pair in this project.
They describe the same model artefact from two perspectives: FAIR4ML is machine-
readable and structured; Model Card is human-readable and narrative. In this project,
the evaluation metrics appear in both — FAIR4ML as JSON numeric fields, Model Card as
a markdown table. Both are consistent in values (R²=0.8702, RMSE=8.0957, MAE=5.5635
for the local version). The known limitations are expressed as a JSON array in FAIR4ML
and as prose paragraphs in Model Card — same content, different structure. The
`intended_use` concept exists in both but FAIR4ML constrains it to a single string
while Model Card devotes a full section with multiple paragraphs. No factual conflicts
were identified.

---

### 10. Croissant ↔ Model Card

**(a) Fields in both:**
`name`, `license`, `identifier` (dataset DOI), `creator` (training data authors)

**(b) Unique fields:**

| Croissant only               | Model Card only         |
| ---------------------------- | ----------------------- |
| `recordSet` field schema     | Intended use            |
| Field `dataType`             | Out-of-scope uses       |
| Field `unitCode` (QUDT URIs) | Ethical considerations  |
| `distribution` file objects  | Evaluation metrics      |
| `publisher`                  | Limitations             |
| `source` linking             | Training data narrative |

**(c) Conflicts / inconsistencies:**
Croissant describes the raw input dataset structure in machine-readable form.
Model Card references the same datasets as training data sources but only at
the level of name and DOI. There is no field-level overlap. Croissant's
`recordSet` describes all 22 raw columns from the transfer dataset; Model Card
only mentions the 14 features selected for the model. No conflicts were found —
these two standards are almost entirely complementary in this project.

---

## Discussion

The five standards form a coherent but partially redundant metadata ecosystem
for this experiment. Three patterns emerge from the pairwise analysis.

**Strong complementarity with minimal overlap:** CodeMeta and Croissant,
CodeMeta and Model Card, and Croissant and Model Card have very little semantic
overlap because they address fundamentally different artefact types — software,
datasets, and ML models respectively. These pairs are almost pure complements:
each adds information the other cannot provide.

**High overlap with different levels of machine readability:** FAIR4ML and
Model Card are the most overlapping pair, covering the same model artefact
from machine-readable (FAIR4ML) and human-readable (Model Card) perspectives.
The redundancy here is deliberate — FAIR4ML enables automated processing while
Model Card enables human review. The same metric values, intended use, and
limitations appear in both, creating a desirable consistency constraint.

**RO-Crate as the integrating layer:** RO-Crate is the only standard that
explicitly links all other artefacts through entity relationships (`hasPart`,
`isBasedOn`, `input`, `output`). It overlaps in administrative metadata with all
four other standards but is unique in providing the relational graph connecting
code, datasets, models, and outputs into a single describable package.

The most significant gap across all five standards is **ethical considerations**,
which are captured only in the Model Card with no machine-readable equivalent in
any of the other four standards. Similarly, **field-level unit mappings using QUDT
URIs** are unique to Croissant — FAIR4ML, RO-Crate, CodeMeta, and Model Card do not
provide this level of measurement unit precision. Conversely, **software dependency
management** (library names and versions) is unique to CodeMeta and has no parallel
in the other four standards, despite being critical for reproducibility.

The main consistency risk identified is **licence representation format**: RO-Crate
uses `@id` URL references to named licence entities; CodeMeta uses SPDX licence URLs;
FAIR4ML uses plain strings ("CC BY 4.0"); Croissant uses CC licence URLs; Model Card
uses prose descriptions separated by artefact category. All refer to the same licences
but in five different formats, creating a maintenance burden when licences change.
