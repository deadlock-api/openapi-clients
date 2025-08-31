# WeaponV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**class_name** | **str** |  | 
**name** | **str** |  | 
**start_trained** | **bool** |  | [optional] 
**image** | **str** |  | [optional] 
**image_webp** | **str** |  | [optional] 
**hero** | **int** |  | [optional] 
**heroes** | **List[int]** |  | [optional] 
**update_time** | **int** |  | [optional] 
**properties** | [**Dict[str, ItemPropertyV2]**](ItemPropertyV2.md) |  | [optional] 
**weapon_info** | [**RawWeaponInfoV2**](RawWeaponInfoV2.md) |  | [optional] 
**type** | **str** |  | [optional] [default to 'weapon']

## Example

```python
from openapi_client.models.weapon_v2 import WeaponV2

# TODO update the JSON string below
json = "{}"
# create an instance of WeaponV2 from a JSON string
weapon_v2_instance = WeaponV2.from_json(json)
# print the JSON string representation of the object
print(WeaponV2.to_json())

# convert the object into a dict
weapon_v2_dict = weapon_v2_instance.to_dict()
# create an instance of WeaponV2 from a dict
weapon_v2_from_dict = WeaponV2.from_dict(weapon_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


