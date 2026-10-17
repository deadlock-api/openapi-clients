# HeroBuildStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_average_badge** | Option<**f64**> | Average badge (tier = first digits, subtier = last digit) of the matches with this build that have one; 0 without any. See more: <https://api.deadlock-api.com/v1/assets/ranks> | [optional]
**bucket** | **u32** | The bucket value (depends on the bucket query parameter, 0 without one). | 
**hero_build_id** | **u64** | The ID of the hero build. The `hero_build_id` is the first build the player had selected when the game started. | 
**hero_id** | **u32** | The ID of the hero. See more: <https://api.deadlock-api.com/v1/assets/heroes> | 
**losses** | **u64** | The number of losses with this build. | 
**matches** | **u64** | The total number of matches played with this build (`wins + losses`). | 
**players** | **u64** | The number of unique players who used this build. | 
**total_assists** | Option<**u64**> |  | [optional]
**total_boss_damage** | Option<**u64**> |  | [optional]
**total_creep_damage** | Option<**u64**> |  | [optional]
**total_creep_kills** | Option<**u64**> |  | [optional]
**total_damage_mitigated** | Option<**u64**> |  | [optional]
**total_deaths** | Option<**u64**> |  | [optional]
**total_denies** | Option<**u64**> |  | [optional]
**total_duration_s** | Option<**u64**> | Sum of the match durations (seconds), for per-minute rates. | [optional]
**total_hero_bullets_hit** | Option<**u64**> | Bullets that hit an enemy hero. | [optional]
**total_hero_bullets_hit_crit** | Option<**u64**> | Hero hits that were crits (headshots). | [optional]
**total_kills** | Option<**u64**> | Sum of the kills of every match with this build. Average per match: `total_kills / matches`. This and the other totals are only present with `include_performance=true`. | [optional]
**total_last_hits** | Option<**u64**> |  | [optional]
**total_level** | Option<**u64**> | Sum of the final hero levels. | [optional]
**total_max_health** | Option<**u64**> |  | [optional]
**total_net_worth** | Option<**u64**> | Sum of the final net worth (souls). | [optional]
**total_neutral_damage** | Option<**u64**> |  | [optional]
**total_neutral_kills** | Option<**u64**> |  | [optional]
**total_player_damage** | Option<**u64**> |  | [optional]
**total_player_damage_taken** | Option<**u64**> |  | [optional]
**total_player_healing** | Option<**u64**> |  | [optional]
**total_self_healing** | Option<**u64**> |  | [optional]
**total_shots_hit** | Option<**u64**> |  | [optional]
**total_shots_missed** | Option<**u64**> |  | [optional]
**total_teammate_healing** | Option<**u64**> |  | [optional]
**wins** | **u64** | The number of wins with this build. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


