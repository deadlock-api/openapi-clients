# PlayerPerformanceCurvePoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assists_avg** | **f64** | Average assists at this time point | 
**assists_std** | **f64** | Standard deviation of assists at this time point | 
**boss_damage_avg** | **f64** | Average damage dealt to objectives at this time point | 
**boss_damage_std** | **f64** | Standard deviation of `boss_damage_avg` at this time point | 
**boss_kills_avg** | **f64** | Average objectives killed (last hits) at this time point | 
**boss_kills_std** | **f64** | Standard deviation of `boss_kills_avg` at this time point | 
**creep_damage_avg** | **f64** | Average damage dealt to lane creeps at this time point | 
**creep_damage_std** | **f64** | Standard deviation of `creep_damage_avg` at this time point | 
**creep_kills_avg** | **f64** | Average lane creeps killed (last hits) at this time point | 
**creep_kills_std** | **f64** | Standard deviation of `creep_kills_avg` at this time point | 
**deaths_avg** | **f64** | Average deaths at this time point | 
**deaths_std** | **f64** | Standard deviation of deaths at this time point | 
**denies_avg** | **f64** | Average lane creeps denied at this time point | 
**denies_std** | **f64** | Standard deviation of `denies_avg` at this time point | 
**game_time** | **u32** | The time point of the data. If `resolution` (default 10) is > 0, this is a percentage (0, 10, ..., 100). If `resolution` is 0, this is the match time in seconds. | 
**gold_ability_assassinate_avg** | **f64** | Average souls earned from the Assassinate ability at this time point | 
**gold_ability_assassinate_std** | **f64** | Standard deviation of `gold_ability_assassinate_avg` at this time point | 
**gold_assists_avg** | **f64** | Average souls earned from assists at this time point (part of `gold_player_avg`) | 
**gold_assists_std** | **f64** | Standard deviation of `gold_assists_avg` at this time point | 
**gold_boss_avg** | **f64** | Average souls earned from objectives at this time point | 
**gold_boss_orb_avg** | **f64** | Average souls earned from secured objective orbs at this time point | 
**gold_boss_orb_std** | **f64** | Standard deviation of `gold_boss_orb_avg` at this time point | 
**gold_boss_std** | **f64** | Standard deviation of `gold_boss_avg` at this time point | 
**gold_breakable_avg** | **f64** | Average souls earned from breakables (crates, statues) at this time point | 
**gold_breakable_std** | **f64** | Standard deviation of `gold_breakable_avg` at this time point | 
**gold_death_loss_avg** | **f64** | Average souls lost on death at this time point | 
**gold_death_loss_std** | **f64** | Standard deviation of `gold_death_loss_avg` at this time point | 
**gold_denied_avg** | **f64** | Average souls denied to enemies at this time point | 
**gold_denied_std** | **f64** | Standard deviation of `gold_denied_avg` at this time point | 
**gold_item_cultist_sacrifice_avg** | **f64** | Average souls earned from the Cultist Sacrifice item at this time point | 
**gold_item_cultist_sacrifice_std** | **f64** | Standard deviation of `gold_item_cultist_sacrifice_avg` at this time point | 
**gold_item_goose_egg_avg** | **f64** | Average souls earned from the Golden Goose Egg item at this time point | 
**gold_item_goose_egg_std** | **f64** | Standard deviation of `gold_item_goose_egg_avg` at this time point | 
**gold_item_trophy_collector_avg** | **f64** | Average souls earned from the Trophy Collector item at this time point | 
**gold_item_trophy_collector_std** | **f64** | Standard deviation of `gold_item_trophy_collector_avg` at this time point | 
**gold_lane_creep_avg** | **f64** | Average souls earned from lane creeps at this time point | 
**gold_lane_creep_orbs_avg** | **f64** | Average souls earned from secured lane-creep orbs at this time point | 
**gold_lane_creep_orbs_std** | **f64** | Standard deviation of `gold_lane_creep_orbs_avg` at this time point | 
**gold_lane_creep_std** | **f64** | Standard deviation of `gold_lane_creep_avg` at this time point | 
**gold_neutral_creep_avg** | **f64** | Average souls earned from neutral (jungle) creeps at this time point | 
**gold_neutral_creep_orbs_avg** | **f64** | Average souls earned from secured neutral-creep orbs at this time point | 
**gold_neutral_creep_orbs_std** | **f64** | Standard deviation of `gold_neutral_creep_orbs_avg` at this time point | 
**gold_neutral_creep_std** | **f64** | Standard deviation of `gold_neutral_creep_avg` at this time point | 
**gold_player_avg** | **f64** | Average souls earned from hero kills at this time point, including assist souls (see `gold_assists_avg`) | 
**gold_player_orbs_avg** | **f64** | Average souls earned from secured hero-kill orbs at this time point | 
**gold_player_orbs_std** | **f64** | Standard deviation of `gold_player_orbs_avg` at this time point | 
**gold_player_std** | **f64** | Standard deviation of `gold_player_avg` at this time point | 
**gold_team_bonus_avg** | **f64** | Average souls earned from the team bonus at this time point | 
**gold_team_bonus_std** | **f64** | Standard deviation of `gold_team_bonus_avg` at this time point | 
**gold_treasure_avg** | **f64** | Average souls earned from the urn at this time point | 
**gold_treasure_std** | **f64** | Standard deviation of `gold_treasure_avg` at this time point | 
**kills_avg** | **f64** | Average kills at this time point | 
**kills_std** | **f64** | Standard deviation of kills at this time point | 
**net_worth_avg** | **f64** | Average net worth at this time point | 
**net_worth_std** | **f64** | Standard deviation of net worth at this time point | 
**neutral_damage_avg** | **f64** | Average damage dealt to neutral (jungle) creeps at this time point | 
**neutral_damage_std** | **f64** | Standard deviation of `neutral_damage_avg` at this time point | 
**neutral_kills_avg** | **f64** | Average neutral (jungle) creeps killed at this time point | 
**neutral_kills_std** | **f64** | Standard deviation of `neutral_kills_avg` at this time point | 
**permanent_buffs_avg** | Option<**f64**> | Average permanent buff (power-up) pickups collected up to this time point. Only matches since build 6712 (2026-09-29) record pickup times, so only players with at least one timed permanent pickup count; `null` when there are none. | [optional]
**permanent_buffs_std** | Option<**f64**> | Standard deviation of `permanent_buffs_avg` at this time point; `null` when there are no players with timed permanent pickups. | [optional]
**player_damage_avg** | **f64** | Average damage dealt to enemy heroes at this time point | 
**player_damage_std** | **f64** | Standard deviation of `player_damage_avg` at this time point | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


