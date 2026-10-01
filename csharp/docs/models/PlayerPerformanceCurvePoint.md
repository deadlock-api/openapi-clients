# DeadlockApiClient.Model.PlayerPerformanceCurvePoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AssistsAvg** | **double** | Average assists at this time point | 
**AssistsStd** | **double** | Standard deviation of assists at this time point | 
**DeathsAvg** | **double** | Average deaths at this time point | 
**DeathsStd** | **double** | Standard deviation of deaths at this time point | 
**GameTime** | **int** | The time point of the data. If &#x60;resolution&#x60; (default 10) is &gt; 0, this is a percentage (0, 10, ..., 100). If &#x60;resolution&#x60; is 0, this is the match time in seconds. | 
**GoldAbilityAssassinateAvg** | **double** | Average souls earned from the Assassinate ability at this time point | 
**GoldAssistsAvg** | **double** | Average souls earned from assists at this time point (part of &#x60;gold_player_avg&#x60;) | 
**GoldBossAvg** | **double** | Average souls earned from objectives at this time point | 
**GoldBossOrbAvg** | **double** | Average souls earned from secured objective orbs at this time point | 
**GoldBreakableAvg** | **double** | Average souls earned from breakables (crates, statues) at this time point | 
**GoldDeathLossAvg** | **double** | Average souls lost on death at this time point | 
**GoldDeniedAvg** | **double** | Average souls denied to enemies at this time point | 
**GoldItemCultistSacrificeAvg** | **double** | Average souls earned from the Cultist Sacrifice item at this time point | 
**GoldItemGooseEggAvg** | **double** | Average souls earned from the Golden Goose Egg item at this time point | 
**GoldItemTrophyCollectorAvg** | **double** | Average souls earned from the Trophy Collector item at this time point | 
**GoldLaneCreepAvg** | **double** | Average souls earned from lane creeps at this time point | 
**GoldLaneCreepOrbsAvg** | **double** | Average souls earned from secured lane-creep orbs at this time point | 
**GoldNeutralCreepAvg** | **double** | Average souls earned from neutral (jungle) creeps at this time point | 
**GoldNeutralCreepOrbsAvg** | **double** | Average souls earned from secured neutral-creep orbs at this time point | 
**GoldPlayerAvg** | **double** | Average souls earned from hero kills at this time point, including assist souls (see &#x60;gold_assists_avg&#x60;) | 
**GoldPlayerOrbsAvg** | **double** | Average souls earned from secured hero-kill orbs at this time point | 
**GoldTeamBonusAvg** | **double** | Average souls earned from the team bonus at this time point | 
**GoldTreasureAvg** | **double** | Average souls earned from the urn at this time point | 
**KillsAvg** | **double** | Average kills at this time point | 
**KillsStd** | **double** | Standard deviation of kills at this time point | 
**NetWorthAvg** | **double** | Average net worth at this time point | 
**NetWorthStd** | **double** | Standard deviation of net worth at this time point | 
**PermanentBuffsAvg** | **double** | Average permanent buff (power-up) pickups collected up to this time point. Only matches since build 6712 (2026-09-29) record pickup times, so only players with at least one timed permanent pickup count; &#x60;null&#x60; when there are none. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

