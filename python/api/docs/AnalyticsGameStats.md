# AnalyticsGameStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abandon_rate** | **float** |  | 
**avg_accuracy** | **float** |  | 
**avg_assists** | **float** |  | 
**avg_boss_damage** | **float** |  | 
**avg_creep_damage** | **float** |  | 
**avg_creep_kills** | **float** |  | 
**avg_crit_rate** | **float** |  | 
**avg_damage_absorbed** | **float** |  | 
**avg_damage_mitigated** | **float** |  | 
**avg_deaths** | **float** |  | 
**avg_denies** | **float** |  | 
**avg_duration_s** | **float** |  | 
**avg_ending_level** | **float** |  | 
**avg_first_mid_boss_time_s** | **float** |  | 
**avg_gold_boss** | **float** |  | 
**avg_gold_boss_orb** | **float** |  | 
**avg_gold_death_loss** | **float** |  | 
**avg_gold_denied** | **float** |  | 
**avg_gold_lane_creep** | **float** |  | 
**avg_gold_lane_creep_orbs** | **float** |  | 
**avg_gold_neutral_creep** | **float** |  | 
**avg_gold_neutral_creep_orbs** | **float** |  | 
**avg_gold_player** | **float** |  | 
**avg_gold_player_orbs** | **float** |  | 
**avg_gold_treasure** | **float** |  | 
**avg_heal_prevented** | **float** |  | 
**avg_kd_ratio** | **float** |  | 
**avg_kills** | **float** |  | 
**avg_last_hits** | **float** |  | 
**avg_max_health** | **float** |  | 
**avg_net_worth** | **float** |  | 
**avg_neutral_damage** | **float** |  | 
**avg_neutral_kills** | **float** |  | 
**avg_objectives_destroyed_time_s** | **float** |  | 
**avg_player_damage** | **float** |  | 
**avg_player_damage_taken** | **float** |  | 
**avg_player_healing** | **float** |  | 
**avg_possible_creeps** | **float** |  | 
**avg_self_healing** | **float** |  | 
**avg_tech_power** | **float** |  | 
**avg_weapon_power** | **float** |  | 
**bucket** | **int** |  | 
**mid_boss_kill_rate** | **float** |  | 
**team0_wins** | **int** |  | 
**team1_wins** | **int** |  | 
**total_matches** | **int** |  | 

## Example

```python
from deadlock_api_client.models.analytics_game_stats import AnalyticsGameStats

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsGameStats from a JSON string
analytics_game_stats_instance = AnalyticsGameStats.from_json(json)
# print the JSON string representation of the object
print(AnalyticsGameStats.to_json())

# convert the object into a dict
analytics_game_stats_dict = analytics_game_stats_instance.to_dict()
# create an instance of AnalyticsGameStats from a dict
analytics_game_stats_from_dict = AnalyticsGameStats.from_dict(analytics_game_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


