# RawWeaponV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **str** |  | 
**start_trained** | **bool** |  | [optional] 
**image** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 
**properties** | [**Dict[str, RawItemPropertyV2]**](RawItemPropertyV2.md) |  | [optional] 
**weapon_info** | [**RawWeaponInfoV2**](RawWeaponInfoV2.md) |  | [optional] 
**css_class** | **str** |  | [optional] 
**type** | **str** |  | [optional] [default to 'weapon']

## Example

```python
from assets_deadlock_api_client.models.raw_weapon_v2 import RawWeaponV2

# TODO update the JSON string below
json = "{}"
# create an instance of RawWeaponV2 from a JSON string
raw_weapon_v2_instance = RawWeaponV2.from_json(json)
# print the JSON string representation of the object
print(RawWeaponV2.to_json())

# convert the object into a dict
raw_weapon_v2_dict = raw_weapon_v2_instance.to_dict()
# create an instance of RawWeaponV2 from a dict
raw_weapon_v2_from_dict = RawWeaponV2.from_dict(raw_weapon_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


