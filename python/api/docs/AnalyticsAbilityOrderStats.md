# AnalyticsAbilityOrderStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abilities** | **List[int]** | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**losses** | **int** |  | 
**matches** | **int** |  | 
**players** | **int** |  | 
**total_assists** | **int** |  | 
**total_deaths** | **int** |  | 
**total_kills** | **int** |  | 
**wins** | **int** |  | 

## Example

```python
from openapi_client.models.analytics_ability_order_stats import AnalyticsAbilityOrderStats

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsAbilityOrderStats from a JSON string
analytics_ability_order_stats_instance = AnalyticsAbilityOrderStats.from_json(json)
# print the JSON string representation of the object
print(AnalyticsAbilityOrderStats.to_json())

# convert the object into a dict
analytics_ability_order_stats_dict = analytics_ability_order_stats_instance.to_dict()
# create an instance of AnalyticsAbilityOrderStats from a dict
analytics_ability_order_stats_from_dict = AnalyticsAbilityOrderStats.from_dict(analytics_ability_order_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


