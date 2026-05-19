# Group 14 – Task Overview

Legend: ✅ done · 🟡 WIP / waiting · ❌ open

## A – Konrad Szegedy

| Status | Task | Short note |
|---|---|---|
| ✅ | T2.1 DBRepo schema | DBRepo tables created; schema + ER diagram + notebook in repo |
| ✅ | T3.1 RO-Crate | `ro-crate-metadata.json` + validation output in repo |
| ✅ | T3.5 Model Card | `docs/model-card.md` written with final XGBRegressor metrics |
| 🟡 | T3.9 Model deposit | Model DOI exists: `10.70124/c35xx-9pb93`; still needs final cross-links from B/D if missing |
| ❌ | T4.4 Final DMP deposit | Waiting for final DMP PDF from D and maDMP JSON from B |
| ❌ | T5.1/T5.2 OSTrails tests | Need to implement A's 3 assigned tests and make/coordinate PR |
| ❌ | WP6 Review | Only after another group is assigned |
| ❌ | WP7 Final report | Need contribution table and links |

## B – Muhammad Athar Riaz

| Status | Task | Short note |
|---|---|---|
| ❌ | T2.2 Semantic mapping | Map attributes to ontology concepts in DBRepo |
| ❌ | T2.7 WP2 release | Make second GitHub release |
| ❌ | T3.2 CodeMeta | Add `codemeta.json` |
| ❌ | T3.6 Licences | Define input/code/output licences |
| ❌ | T3.10 Generated-data deposit | Upload predictions/results as separate TUWRD dataset; needs A model DOI |
| ❌ | T4.3 maDMP JSON | Export/finalize maDMP JSON |
| ❌ | T4.5 DMP comparison | Compare initial vs final DMP |
| ❌ | T5.3 OSTrails tests B | Implement B's 3 tests |
| ❌ | WP6/WP7 | Review + final report parts |

## C – Muhammad Bilal Hussain

| Status | Task | Short note |
|---|---|---|
| ✅ | T1.3 GitHub setup | Repo exists |
| ✅ | T2.3 Unit mapping | Map numeric units |
| ❌ | T2.5 DBRepo load | Load data into DBRepo and verify views |
| ✅ | T3.3 FAIR4ML | Metadata for model; should reference A model DOI/card |
| ✅ | T3.7 README | Full README with DOI badge, instructions, licences, ORCIDs |
| ✅ | T3.11 Standards overlap | Table for RO-Crate/CodeMeta/FAIR4ML/Croissant/Model Card |
| ✅ | T4.1 Final DMP in DMP Tool | Complete DAMAP/FWF template |
| ❌ | T5.4 OSTrails tests C | Implement C's 3 tests |
| ❌ | WP6/WP7 | Review + final report parts |

## D – Ekene Edeh

| Status | Task | Short note |
|---|---|---|
| ✅ | T1.4 First release | WP1 release exists |
| ❌ | T2.4 Views | Create SQL views for ML pipeline |
| ❌ | T2.6 DBRepo API reimplementation | Final code must read from DBRepo API, not local files |
| ❌ | T3.4 Croissant | Add Croissant JSON-LD for input datasets |
| ❌ | T3.8 Zenodo DOI | Connect GitHub to Zenodo; mint DOI; add badge + CITATION.cff |
| ❌ | T4.2 Final DMP PDF/A | Export/finalize DMP PDF/A |
| ❌ | T5.5 OSTrails tests D | Implement D's 3 tests |
| ❌ | WP6/WP7 | Review + final report parts |

## Deadlines

| Date | What |
|---|---|
| 30.05 | Final DMP submitted |
| 15.06 | Pull request link submitted |
| 22.06 | Review PDF + final report submitted |
| Last week of June | Face-to-face group meeting |

## Immediate blockers

| Blocker | Who needs to act |
|---|---|
| Generated-data DOI needed for A model deposit cross-link | B |
| Zenodo DOI needed for RO-Crate/TUWRD metadata | D |
| FAIR4ML file needed for model deposit/RO-Crate | C |
| Final DMP PDF + maDMP JSON needed for 30.05 | D + B |
| Final README/licence consistency | C + B |
