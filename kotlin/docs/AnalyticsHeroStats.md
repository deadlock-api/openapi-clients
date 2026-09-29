
# AnalyticsHeroStats

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **bucket** | **kotlin.Int** |  |  |
| **heroId** | **kotlin.Int** | See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; |  |
| **losses** | **kotlin.Long** |  |  |
| **matches** | **kotlin.Long** |  |  |
| **matchesPerBucket** | **kotlin.Long** |  |  |
| **permanentBuffMatches** | **kotlin.Long** | Matches that carry buff pickup counts. Equals &#x60;matches&#x60;, except on account-scoped queries (&#x60;account_ids&#x60; without item or ability filters): those read a per-account table that only has buff counts for matches ingested since build 6712 (late September 2026). |  |
| **permanentBuffTimingMatches** | **kotlin.Long** | Matches with pickup timings. Only matches since build 6712 (2026-09-29) record pickup times, and only players with at least one permanent pickup count here. |  |
| **totalAssists** | **kotlin.Long** |  |  |
| **totalBossDamage** | **kotlin.Long** |  |  |
| **totalCreepDamage** | **kotlin.Long** |  |  |
| **totalDeaths** | **kotlin.Long** |  |  |
| **totalDenies** | **kotlin.Long** |  |  |
| **totalFirstPermanentBuffTimeS** | **kotlin.Long** | Sum of the game time (seconds) of each player&#39;s first permanent buff pickup, over the &#x60;permanent_buff_timing_matches&#x60; matches. Average: &#x60;total_first_permanent_buff_time_s / permanent_buff_timing_matches&#x60;. |  |
| **totalKills** | **kotlin.Long** |  |  |
| **totalLastHits** | **kotlin.Long** |  |  |
| **totalMaxHealth** | **kotlin.Long** |  |  |
| **totalNetWorth** | **kotlin.Long** |  |  |
| **totalNeutralDamage** | **kotlin.Long** |  |  |
| **totalPermanentBuffs** | **kotlin.Long** | Sum of permanent buff (power-up) pickups over the &#x60;permanent_buff_matches&#x60; matches. Average per match: &#x60;total_permanent_buffs / permanent_buff_matches&#x60;. Buff types: &lt;https://api.deadlock-api.com/v1/assets/misc-entities&gt; |  |
| **totalPlayerDamage** | **kotlin.Long** |  |  |
| **totalPlayerDamageTaken** | **kotlin.Long** |  |  |
| **totalShotsHit** | **kotlin.Long** |  |  |
| **totalShotsMissed** | **kotlin.Long** |  |  |
| **wins** | **kotlin.Long** |  |  |



