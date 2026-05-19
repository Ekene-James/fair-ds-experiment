# Unit Mapping

## Dataset

Austrian Traffic Accident Dataset

---

## Column Unit Mapping

| Column Name | Data Type | Unit / Format | Description |
|---|---|---|---|
| accident_date | date | YYYY-MM-DD | Date of accident |
| accident_time | time | HH:MM | Time of accident |
| temperature | numeric | °C | Weather temperature |
| rainfall | numeric | mm | Rainfall amount |
| vehicle_count | integer | count | Number of vehicles involved |
| road_type | categorical | text | Type of road |
| accident_severity | categorical | label | Severity classification |
| speed_limit | numeric | km/h | Road speed limit |

---

## Metadata Notes

The dataset uses structured CSV formatting and standardized units to improve interoperability and reproducibility.

Date and time fields follow ISO-compatible formatting conventions where possible.

Numeric measurements use commonly accepted SI-related units.

---

## FAIR Compliance Notes

This unit mapping document improves:
- interoperability
- machine readability
- reproducibility
- metadata quality

for FAIR-compliant data science workflows.
