# DeadlockApiClient.Model.HeroBuildStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Bucket** | **int** | The bucket value (depends on the bucket query parameter, 0 without one). | 
**HeroBuildId** | **long** | The ID of the hero build. The &#x60;hero_build_id&#x60; is the first build the player had selected when the game started. | 
**HeroId** | **int** | The ID of the hero. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**Losses** | **long** | The number of losses with this build. | 
**Matches** | **long** | The total number of matches played with this build (&#x60;wins + losses&#x60;). | 
**Players** | **long** | The number of unique players who used this build. | 
**Wins** | **long** | The number of wins with this build. | 
**AvgAverageBadge** | **double** | Average badge (tier &#x3D; first digits, subtier &#x3D; last digit) of the matches with this build that have one; 0 without any. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional] 
**TotalAssists** | **long** |  | [optional] 
**TotalBossDamage** | **long** |  | [optional] 
**TotalCreepDamage** | **long** |  | [optional] 
**TotalCreepKills** | **long** |  | [optional] 
**TotalDamageMitigated** | **long** |  | [optional] 
**TotalDeaths** | **long** |  | [optional] 
**TotalDenies** | **long** |  | [optional] 
**TotalDurationS** | **long** | Sum of the match durations (seconds), for per-minute rates. | [optional] 
**TotalHeroBulletsHit** | **long** | Bullets that hit an enemy hero. | [optional] 
**TotalHeroBulletsHitCrit** | **long** | Hero hits that were crits (headshots). | [optional] 
**TotalKills** | **long** | Sum of the kills of every match with this build. Average per match: &#x60;total_kills / matches&#x60;. This and the other totals are only present with &#x60;include_performance&#x3D;true&#x60;. | [optional] 
**TotalLastHits** | **long** |  | [optional] 
**TotalLevel** | **long** | Sum of the final hero levels. | [optional] 
**TotalMaxHealth** | **long** |  | [optional] 
**TotalNetWorth** | **long** | Sum of the final net worth (souls). | [optional] 
**TotalNeutralDamage** | **long** |  | [optional] 
**TotalNeutralKills** | **long** |  | [optional] 
**TotalPlayerDamage** | **long** |  | [optional] 
**TotalPlayerDamageTaken** | **long** |  | [optional] 
**TotalPlayerHealing** | **long** |  | [optional] 
**TotalSelfHealing** | **long** |  | [optional] 
**TotalShotsHit** | **long** |  | [optional] 
**TotalShotsMissed** | **long** |  | [optional] 
**TotalTeammateHealing** | **long** |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

