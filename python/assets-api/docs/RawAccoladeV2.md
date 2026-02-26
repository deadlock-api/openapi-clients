# RawAccoladeV2


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
from assets_deadlock_api_client.models.raw_accolade_v2 import RawAccoladeV2

# TODO update the JSON string below
json = "{}"
# create an instance of RawAccoladeV2 from a JSON string
raw_accolade_v2_instance = RawAccoladeV2.from_json(json)
# print the JSON string representation of the object
print(RawAccoladeV2.to_json())

# convert the object into a dict
raw_accolade_v2_dict = raw_accolade_v2_instance.to_dict()
# create an instance of RawAccoladeV2 from a dict
raw_accolade_v2_from_dict = RawAccoladeV2.from_dict(raw_accolade_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


