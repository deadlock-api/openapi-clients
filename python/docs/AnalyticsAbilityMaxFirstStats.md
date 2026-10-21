# AnalyticsAbilityMaxFirstStats

The players who maxed one ability first, or (`ability_id` null) none.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ability_id** | **int** | The ability these players maxed first (unlocked and upgraded three times before any other), null for the players who maxed none. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [optional] 
**losses** | **int** |  | 
**matches** | **int** |  | 
**players** | **int** | Distinct players, counted exactly. | 
**wins** | **int** |  | 

## Example

```python
from deadlock_api_client.models.analytics_ability_max_first_stats import AnalyticsAbilityMaxFirstStats

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsAbilityMaxFirstStats from a JSON string
analytics_ability_max_first_stats_instance = AnalyticsAbilityMaxFirstStats.from_json(json)
# print the JSON string representation of the object
print(AnalyticsAbilityMaxFirstStats.to_json())

# convert the object into a dict
analytics_ability_max_first_stats_dict = analytics_ability_max_first_stats_instance.to_dict()
# create an instance of AnalyticsAbilityMaxFirstStats from a dict
analytics_ability_max_first_stats_from_dict = AnalyticsAbilityMaxFirstStats.from_dict(analytics_ability_max_first_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


