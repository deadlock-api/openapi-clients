# HeroBuildStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_average_badge** | **float** | Average badge (tier &#x3D; first digits, subtier &#x3D; last digit) of the matches with this build that have one; 0 without any. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional]
**bucket** | **int** | The bucket value (depends on the bucket query parameter, 0 without one). |
**hero_build_id** | **int** | The ID of the hero build. The &#x60;hero_build_id&#x60; is the first build the player had selected when the game started. |
**hero_id** | **int** | The ID of the hero. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; |
**losses** | **int** | The number of losses with this build. |
**matches** | **int** | The total number of matches played with this build (&#x60;wins + losses&#x60;). |
**players** | **int** | The number of unique players who used this build. |
**total_assists** | **int** |  | [optional]
**total_boss_damage** | **int** |  | [optional]
**total_creep_damage** | **int** |  | [optional]
**total_creep_kills** | **int** |  | [optional]
**total_damage_mitigated** | **int** |  | [optional]
**total_deaths** | **int** |  | [optional]
**total_denies** | **int** |  | [optional]
**total_duration_s** | **int** | Sum of the match durations (seconds), for per-minute rates. | [optional]
**total_hero_bullets_hit** | **int** | Bullets that hit an enemy hero. | [optional]
**total_hero_bullets_hit_crit** | **int** | Hero hits that were crits (headshots). | [optional]
**total_kills** | **int** | Sum of the kills of every match with this build. Average per match: &#x60;total_kills / matches&#x60;. This and the other totals are only present with &#x60;include_performance&#x3D;true&#x60;. | [optional]
**total_last_hits** | **int** |  | [optional]
**total_level** | **int** | Sum of the final hero levels. | [optional]
**total_max_health** | **int** |  | [optional]
**total_net_worth** | **int** | Sum of the final net worth (souls). | [optional]
**total_neutral_damage** | **int** |  | [optional]
**total_neutral_kills** | **int** |  | [optional]
**total_player_damage** | **int** |  | [optional]
**total_player_damage_taken** | **int** |  | [optional]
**total_player_healing** | **int** |  | [optional]
**total_self_healing** | **int** |  | [optional]
**total_shots_hit** | **int** |  | [optional]
**total_shots_missed** | **int** |  | [optional]
**total_teammate_healing** | **int** |  | [optional]
**wins** | **int** | The number of wins with this build. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
