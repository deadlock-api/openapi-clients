# SeasonInterval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_timestamp** | **int** | Unix timestamp (seconds) at which the interval ends. | 
**interval** | **int** |  | 
**start_timestamp** | **int** | Unix timestamp (seconds) at which the interval starts. | 

## Example

```python
from deadlock_api_client.models.season_interval import SeasonInterval

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonInterval from a JSON string
season_interval_instance = SeasonInterval.from_json(json)
# print the JSON string representation of the object
print(SeasonInterval.to_json())

# convert the object into a dict
season_interval_dict = season_interval_instance.to_dict()
# create an instance of SeasonInterval from a dict
season_interval_from_dict = SeasonInterval.from_dict(season_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


