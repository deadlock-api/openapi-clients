# DeadlockApiClient.Model.AnalyticsHeroStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Bucket** | **int** |  | 
**HeroId** | **int** | See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**Losses** | **long** |  | 
**Matches** | **long** |  | 
**MatchesPerBucket** | **long** |  | 
**PermanentBuffMatches** | **long** | Matches that carry buff pickup counts. Equals &#x60;matches&#x60;, except on account-scoped queries (&#x60;account_ids&#x60; without item or ability filters): those read a per-account table that only has buff counts for matches ingested since build 6712 (late September 2026). | 
**PermanentBuffTimingMatches** | **long** | Matches with pickup timings. Only matches since build 6712 (2026-09-29) record pickup times, and only players with at least one permanent pickup count here. | 
**TotalAssists** | **long** |  | 
**TotalBossDamage** | **long** |  | 
**TotalCreepDamage** | **long** |  | 
**TotalDeaths** | **long** |  | 
**TotalDenies** | **long** |  | 
**TotalFirstPermanentBuffTimeS** | **long** | Sum of the game time (seconds) of each player&#39;s first permanent buff pickup, over the &#x60;permanent_buff_timing_matches&#x60; matches. Average: &#x60;total_first_permanent_buff_time_s / permanent_buff_timing_matches&#x60;. | 
**TotalKills** | **long** |  | 
**TotalLastHits** | **long** |  | 
**TotalMaxHealth** | **long** |  | 
**TotalNetWorth** | **long** |  | 
**TotalNeutralDamage** | **long** |  | 
**TotalPermanentBuffs** | **long** | Sum of permanent buff (power-up) pickups over the &#x60;permanent_buff_matches&#x60; matches. Average per match: &#x60;total_permanent_buffs / permanent_buff_matches&#x60;. Buff types: &lt;https://api.deadlock-api.com/v1/assets/misc-entities&gt; | 
**TotalPlayerDamage** | **long** |  | 
**TotalPlayerDamageTaken** | **long** |  | 
**TotalShotsHit** | **long** |  | 
**TotalShotsMissed** | **long** |  | 
**Wins** | **long** |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

