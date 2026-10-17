
# HeroBuildStats

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **bucket** | **kotlin.Int** | The bucket value (depends on the bucket query parameter, 0 without one). |  |
| **heroBuildId** | **kotlin.Long** | The ID of the hero build. The &#x60;hero_build_id&#x60; is the first build the player had selected when the game started. |  |
| **heroId** | **kotlin.Int** | The ID of the hero. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; |  |
| **losses** | **kotlin.Long** | The number of losses with this build. |  |
| **matches** | **kotlin.Long** | The total number of matches played with this build (&#x60;wins + losses&#x60;). |  |
| **players** | **kotlin.Long** | The number of unique players who used this build. |  |
| **wins** | **kotlin.Long** | The number of wins with this build. |  |
| **avgAverageBadge** | **kotlin.Double** | Average badge (tier &#x3D; first digits, subtier &#x3D; last digit) of the matches with this build that have one; 0 without any. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; |  [optional] |
| **totalAssists** | **kotlin.Long** |  |  [optional] |
| **totalBossDamage** | **kotlin.Long** |  |  [optional] |
| **totalCreepDamage** | **kotlin.Long** |  |  [optional] |
| **totalCreepKills** | **kotlin.Long** |  |  [optional] |
| **totalDamageMitigated** | **kotlin.Long** |  |  [optional] |
| **totalDeaths** | **kotlin.Long** |  |  [optional] |
| **totalDenies** | **kotlin.Long** |  |  [optional] |
| **totalDurationS** | **kotlin.Long** | Sum of the match durations (seconds), for per-minute rates. |  [optional] |
| **totalHeroBulletsHit** | **kotlin.Long** | Bullets that hit an enemy hero. |  [optional] |
| **totalHeroBulletsHitCrit** | **kotlin.Long** | Hero hits that were crits (headshots). |  [optional] |
| **totalKills** | **kotlin.Long** | Sum of the kills of every match with this build. Average per match: &#x60;total_kills / matches&#x60;. This and the other totals are only present with &#x60;include_performance&#x3D;true&#x60;. |  [optional] |
| **totalLastHits** | **kotlin.Long** |  |  [optional] |
| **totalLevel** | **kotlin.Long** | Sum of the final hero levels. |  [optional] |
| **totalMaxHealth** | **kotlin.Long** |  |  [optional] |
| **totalNetWorth** | **kotlin.Long** | Sum of the final net worth (souls). |  [optional] |
| **totalNeutralDamage** | **kotlin.Long** |  |  [optional] |
| **totalNeutralKills** | **kotlin.Long** |  |  [optional] |
| **totalPlayerDamage** | **kotlin.Long** |  |  [optional] |
| **totalPlayerDamageTaken** | **kotlin.Long** |  |  [optional] |
| **totalPlayerHealing** | **kotlin.Long** |  |  [optional] |
| **totalSelfHealing** | **kotlin.Long** |  |  [optional] |
| **totalShotsHit** | **kotlin.Long** |  |  [optional] |
| **totalShotsMissed** | **kotlin.Long** |  |  [optional] |
| **totalTeammateHealing** | **kotlin.Long** |  |  [optional] |



