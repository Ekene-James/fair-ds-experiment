# T2.2 Semantic Mapping

This file describes how dataset attributes are mapped to semantic concepts.

| Dataset attribute | Semantic meaning | Ontology / concept |
|---|---|---|
| player_name | Football player name | schema:Person |
| age | Player age | schema:age |
| nationality | Player nationality | schema:nationality |
| club | Football club | sport:SportsTeam |
| position | Playing position | sport:position |
| market_value | Player market value | schema:MonetaryAmount |
| season | Football season | schema:temporalCoverage |
| goals | Number of goals | sport:score |
| assists | Number of assists | sport:assist |
| appearances | Number of appearances | sport:appearance |

The semantic mapping improves machine readability and supports FAIR data principles by connecting dataset columns to clear meanings and reusable concepts.
