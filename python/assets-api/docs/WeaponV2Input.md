# WeaponV2Input


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
**properties** | [**Dict[str, ItemPropertyV2Input]**](ItemPropertyV2Input.md) |  | [optional] 
**weapon_info** | [**RawWeaponInfoV2Input**](RawWeaponInfoV2Input.md) |  | [optional] 
**type** | **str** |  | [optional] [default to 'weapon']

## Example

```python
from assets-deadlock-api-client.models.weapon_v2_input import WeaponV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of WeaponV2Input from a JSON string
weapon_v2_input_instance = WeaponV2Input.from_json(json)
# print the JSON string representation of the object
print(WeaponV2Input.to_json())

# convert the object into a dict
weapon_v2_input_dict = weapon_v2_input_instance.to_dict()
# create an instance of WeaponV2Input from a dict
weapon_v2_input_from_dict = WeaponV2Input.from_dict(weapon_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


