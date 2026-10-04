# PlayerPerformanceCurvePoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assists_avg** | **float** | Average assists at this time point | 
**assists_std** | **float** | Standard deviation of assists at this time point | 
**boss_damage_avg** | **float** | Average damage dealt to objectives at this time point | 
**boss_damage_std** | **float** | Standard deviation of &#x60;boss_damage_avg&#x60; at this time point | 
**boss_kills_avg** | **float** | Average objectives killed (last hits) at this time point | 
**boss_kills_std** | **float** | Standard deviation of &#x60;boss_kills_avg&#x60; at this time point | 
**creep_damage_avg** | **float** | Average damage dealt to lane creeps at this time point | 
**creep_damage_std** | **float** | Standard deviation of &#x60;creep_damage_avg&#x60; at this time point | 
**creep_kills_avg** | **float** | Average lane creeps killed (last hits) at this time point | 
**creep_kills_std** | **float** | Standard deviation of &#x60;creep_kills_avg&#x60; at this time point | 
**deaths_avg** | **float** | Average deaths at this time point | 
**deaths_std** | **float** | Standard deviation of deaths at this time point | 
**denies_avg** | **float** | Average lane creeps denied at this time point | 
**denies_std** | **float** | Standard deviation of &#x60;denies_avg&#x60; at this time point | 
**game_time** | **int** | The time point of the data. If &#x60;resolution&#x60; (default 10) is &gt; 0, this is a percentage (0, 10, ..., 100). If &#x60;resolution&#x60; is 0, this is the match time in seconds. | 
**gold_ability_assassinate_avg** | **float** | Average souls earned from the Assassinate ability at this time point | 
**gold_ability_assassinate_std** | **float** | Standard deviation of &#x60;gold_ability_assassinate_avg&#x60; at this time point | 
**gold_assists_avg** | **float** | Average souls earned from assists at this time point (part of &#x60;gold_player_avg&#x60;) | 
**gold_assists_std** | **float** | Standard deviation of &#x60;gold_assists_avg&#x60; at this time point | 
**gold_boss_avg** | **float** | Average souls earned from objectives at this time point | 
**gold_boss_orb_avg** | **float** | Average souls earned from secured objective orbs at this time point | 
**gold_boss_orb_std** | **float** | Standard deviation of &#x60;gold_boss_orb_avg&#x60; at this time point | 
**gold_boss_std** | **float** | Standard deviation of &#x60;gold_boss_avg&#x60; at this time point | 
**gold_breakable_avg** | **float** | Average souls earned from breakables (crates, statues) at this time point | 
**gold_breakable_std** | **float** | Standard deviation of &#x60;gold_breakable_avg&#x60; at this time point | 
**gold_death_loss_avg** | **float** | Average souls lost on death at this time point | 
**gold_death_loss_std** | **float** | Standard deviation of &#x60;gold_death_loss_avg&#x60; at this time point | 
**gold_denied_avg** | **float** | Average souls denied to enemies at this time point | 
**gold_denied_std** | **float** | Standard deviation of &#x60;gold_denied_avg&#x60; at this time point | 
**gold_item_cultist_sacrifice_avg** | **float** | Average souls earned from the Cultist Sacrifice item at this time point | 
**gold_item_cultist_sacrifice_std** | **float** | Standard deviation of &#x60;gold_item_cultist_sacrifice_avg&#x60; at this time point | 
**gold_item_goose_egg_avg** | **float** | Average souls earned from the Golden Goose Egg item at this time point | 
**gold_item_goose_egg_std** | **float** | Standard deviation of &#x60;gold_item_goose_egg_avg&#x60; at this time point | 
**gold_item_trophy_collector_avg** | **float** | Average souls earned from the Trophy Collector item at this time point | 
**gold_item_trophy_collector_std** | **float** | Standard deviation of &#x60;gold_item_trophy_collector_avg&#x60; at this time point | 
**gold_lane_creep_avg** | **float** | Average souls earned from lane creeps at this time point | 
**gold_lane_creep_orbs_avg** | **float** | Average souls earned from secured lane-creep orbs at this time point | 
**gold_lane_creep_orbs_std** | **float** | Standard deviation of &#x60;gold_lane_creep_orbs_avg&#x60; at this time point | 
**gold_lane_creep_std** | **float** | Standard deviation of &#x60;gold_lane_creep_avg&#x60; at this time point | 
**gold_neutral_creep_avg** | **float** | Average souls earned from neutral (jungle) creeps at this time point | 
**gold_neutral_creep_orbs_avg** | **float** | Average souls earned from secured neutral-creep orbs at this time point | 
**gold_neutral_creep_orbs_std** | **float** | Standard deviation of &#x60;gold_neutral_creep_orbs_avg&#x60; at this time point | 
**gold_neutral_creep_std** | **float** | Standard deviation of &#x60;gold_neutral_creep_avg&#x60; at this time point | 
**gold_player_avg** | **float** | Average souls earned from hero kills at this time point, including assist souls (see &#x60;gold_assists_avg&#x60;) | 
**gold_player_orbs_avg** | **float** | Average souls earned from secured hero-kill orbs at this time point | 
**gold_player_orbs_std** | **float** | Standard deviation of &#x60;gold_player_orbs_avg&#x60; at this time point | 
**gold_player_std** | **float** | Standard deviation of &#x60;gold_player_avg&#x60; at this time point | 
**gold_team_bonus_avg** | **float** | Average souls earned from the team bonus at this time point | 
**gold_team_bonus_std** | **float** | Standard deviation of &#x60;gold_team_bonus_avg&#x60; at this time point | 
**gold_treasure_avg** | **float** | Average souls earned from the urn at this time point | 
**gold_treasure_std** | **float** | Standard deviation of &#x60;gold_treasure_avg&#x60; at this time point | 
**kills_avg** | **float** | Average kills at this time point | 
**kills_std** | **float** | Standard deviation of kills at this time point | 
**net_worth_avg** | **float** | Average net worth at this time point | 
**net_worth_std** | **float** | Standard deviation of net worth at this time point | 
**neutral_damage_avg** | **float** | Average damage dealt to neutral (jungle) creeps at this time point | 
**neutral_damage_std** | **float** | Standard deviation of &#x60;neutral_damage_avg&#x60; at this time point | 
**neutral_kills_avg** | **float** | Average neutral (jungle) creeps killed at this time point | 
**neutral_kills_std** | **float** | Standard deviation of &#x60;neutral_kills_avg&#x60; at this time point | 
**permanent_buffs_avg** | **float** | Average permanent buff (power-up) pickups collected up to this time point. Only matches since build 6712 (2026-09-29) record pickup times, so only players with at least one timed permanent pickup count; &#x60;null&#x60; when there are none. | [optional] 
**permanent_buffs_std** | **float** | Standard deviation of &#x60;permanent_buffs_avg&#x60; at this time point; &#x60;null&#x60; when there are no players with timed permanent pickups. | [optional] 
**player_damage_avg** | **float** | Average damage dealt to enemy heroes at this time point | 
**player_damage_std** | **float** | Standard deviation of &#x60;player_damage_avg&#x60; at this time point | 

## Example

```python
from deadlock_api_client.models.player_performance_curve_point import PlayerPerformanceCurvePoint

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerPerformanceCurvePoint from a JSON string
player_performance_curve_point_instance = PlayerPerformanceCurvePoint.from_json(json)
# print the JSON string representation of the object
print(PlayerPerformanceCurvePoint.to_json())

# convert the object into a dict
player_performance_curve_point_dict = player_performance_curve_point_instance.to_dict()
# create an instance of PlayerPerformanceCurvePoint from a dict
player_performance_curve_point_from_dict = PlayerPerformanceCurvePoint.from_dict(player_performance_curve_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


