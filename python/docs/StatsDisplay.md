# StatsDisplay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_header_stats** | **List[str]** |  | 
**health_stats** | **List[str]** |  | 
**magic_header_stats** | **List[str]** |  | 
**magic_stats** | **List[str]** |  | 
**weapon_header_stats** | **List[str]** |  | 
**weapon_stats** | **List[str]** |  | 

## Example

```python
from deadlock_api_client.models.stats_display import StatsDisplay

# TODO update the JSON string below
json = "{}"
# create an instance of StatsDisplay from a JSON string
stats_display_instance = StatsDisplay.from_json(json)
# print the JSON string representation of the object
print(StatsDisplay.to_json())

# convert the object into a dict
stats_display_dict = stats_display_instance.to_dict()
# create an instance of StatsDisplay from a dict
stats_display_from_dict = StatsDisplay.from_dict(stats_display_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


