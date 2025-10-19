# WeaponV2Output


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
**properties** | [**Dict[str, ItemPropertyV2Output]**](ItemPropertyV2Output.md) |  | [optional] 
**weapon_info** | [**RawWeaponInfoV2Output**](RawWeaponInfoV2Output.md) |  | [optional] 
**type** | **str** |  | [optional] [default to 'weapon']

## Example

```python
from assets-deadlock-api-client.models.weapon_v2_output import WeaponV2Output

# TODO update the JSON string below
json = "{}"
# create an instance of WeaponV2Output from a JSON string
weapon_v2_output_instance = WeaponV2Output.from_json(json)
# print the JSON string representation of the object
print(WeaponV2Output.to_json())

# convert the object into a dict
weapon_v2_output_dict = weapon_v2_output_instance.to_dict()
# create an instance of WeaponV2Output from a dict
weapon_v2_output_from_dict = WeaponV2Output.from_dict(weapon_v2_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


