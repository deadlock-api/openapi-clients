# AnalyticsHeroStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **int** |  | [optional] 
**hero_id** | **int** | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**losses** | **int** |  | 
**matches** | **int** |  | 
**matches_per_bucket** | **int** |  | 
**players** | **int** |  | 
**total_assists** | **int** |  | 
**total_boss_damage** | **int** |  | 
**total_creep_damage** | **int** |  | 
**total_deaths** | **int** |  | 
**total_denies** | **int** |  | 
**total_kills** | **int** |  | 
**total_last_hits** | **int** |  | 
**total_max_health** | **int** |  | 
**total_net_worth** | **int** |  | 
**total_neutral_damage** | **int** |  | 
**total_player_damage** | **int** |  | 
**total_player_damage_taken** | **int** |  | 
**total_shots_hit** | **int** |  | 
**total_shots_missed** | **int** |  | 
**wins** | **int** |  | 

## Example

```python
from deadlock-api-client.models.analytics_hero_stats import AnalyticsHeroStats

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsHeroStats from a JSON string
analytics_hero_stats_instance = AnalyticsHeroStats.from_json(json)
# print the JSON string representation of the object
print(AnalyticsHeroStats.to_json())

# convert the object into a dict
analytics_hero_stats_dict = analytics_hero_stats_instance.to_dict()
# create an instance of AnalyticsHeroStats from a dict
analytics_hero_stats_from_dict = AnalyticsHeroStats.from_dict(analytics_hero_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


