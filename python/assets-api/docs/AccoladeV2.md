# AccoladeV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **str** |  | 
**id** | **int** |  | 
**tracked_stat_name** | [**TrackedStatName**](TrackedStatName.md) |  | 
**flavor_name** | **str** |  | 
**description** | **str** |  | 
**threshold_type** | [**ThresholdType**](ThresholdType.md) |  | 
**enabled_game_modes** | [**List[GameMode]**](GameMode.md) |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.accolade_v2 import AccoladeV2

# TODO update the JSON string below
json = "{}"
# create an instance of AccoladeV2 from a JSON string
accolade_v2_instance = AccoladeV2.from_json(json)
# print the JSON string representation of the object
print(AccoladeV2.to_json())

# convert the object into a dict
accolade_v2_dict = accolade_v2_instance.to_dict()
# create an instance of AccoladeV2 from a dict
accolade_v2_from_dict = AccoladeV2.from_dict(accolade_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


