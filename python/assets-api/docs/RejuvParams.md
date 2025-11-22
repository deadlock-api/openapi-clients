# RejuvParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rejuvinator_expiration_warning_timing** | **float** |  | 
**rejuvinator_buff_duration** | **float** |  | 
**rejuvinator_drop_height** | **float** |  | 
**rejuvinator_drop_duration** | **float** |  | 
**trooper_health_mult** | **List[float]** |  | 
**player_respawn_mult** | **List[float]** |  | 
**rejuvinator_rebirth_duration** | **List[float]** |  | 

## Example

```python
from assets_deadlock_api_client.models.rejuv_params import RejuvParams

# TODO update the JSON string below
json = "{}"
# create an instance of RejuvParams from a JSON string
rejuv_params_instance = RejuvParams.from_json(json)
# print the JSON string representation of the object
print(RejuvParams.to_json())

# convert the object into a dict
rejuv_params_dict = rejuv_params_instance.to_dict()
# create an instance of RejuvParams from a dict
rejuv_params_from_dict = RejuvParams.from_dict(rejuv_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


