# DeadlockApiClient.Model.HeroStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **int** |  | 
**Accuracy** | **double** |  | 
**Assists** | **long** |  | 
**AssistsPerMin** | **double** |  | 
**CreepsPerMin** | **double** |  | 
**CritShotRate** | **double** |  | 
**DamageMitigatedPerMin** | **double** |  | 
**DamagePerMin** | **double** |  | 
**DamagePerSoul** | **double** |  | 
**DamageTakenPerMin** | **double** |  | 
**DamageTakenPerSoul** | **double** |  | 
**Deaths** | **long** |  | 
**DeathsPerMin** | **double** |  | 
**DeniesPerMatch** | **double** |  | 
**DeniesPerMin** | **double** |  | 
**EndingLevel** | **double** |  | 
**HeroId** | **int** | See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**Kills** | **long** |  | 
**KillsPerMin** | **double** |  | 
**LastHitsPerMin** | **double** |  | 
**LastPlayed** | **int** |  | 
**Matches** | **List&lt;long&gt;** |  | 
**MatchesPlayed** | **long** |  | 
**MvpRankCounts** | **List&lt;long&gt;** | Matches by the MVP rank Valve awarded the player: index 0 is rank 1 (MVP), index 1 is rank 2, index 2 is rank 3. Only the top three players of a match get a rank. | 
**MvpRatedMatches** | **long** | Matches played since Valve started reporting MVP ranks (2026-01-06). Divide &#x60;mvp_rank_counts&#x60; by this, not by &#x60;matches_played&#x60;, when the time range reaches further back. | 
**NetworthPerMin** | **double** |  | 
**ObjDamagePerMin** | **double** |  | 
**ObjDamagePerSoul** | **double** |  | 
**PermanentBuffMatches** | **long** | Matches that carry buff pickup counts. Only matches ingested since build 6712 (late September 2026) have them here, so divide by this rather than &#x60;matches_played&#x60;. | 
**PermanentBuffs** | **long** | Permanent buff (power-up) pickups over the &#x60;permanent_buff_matches&#x60; matches. Buff types: &lt;https://api.deadlock-api.com/v1/assets/misc-entities&gt; | 
**TimePlayed** | **long** |  | 
**TotalBossDamage** | **long** |  | 
**TotalCreepDamage** | **long** |  | 
**TotalNeutralDamage** | **long** |  | 
**TotalPlayerDamage** | **long** |  | 
**TotalPlayerDamageTaken** | **long** |  | 
**Wins** | **long** |  | 
**AvgFirstPermanentBuffTimeS** | **double** | Average game time (seconds) of the first permanent buff pickup, over matches with pickup timings (build 6712+, at least one permanent pickup), &#x60;null&#x60; without any. | [optional] 
**PermanentBuffsPerMin** | **double** | Permanent buff pickups per minute over the &#x60;permanent_buff_matches&#x60; matches, &#x60;null&#x60; without any. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

