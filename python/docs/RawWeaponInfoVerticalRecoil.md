# RawWeaponInfoVerticalRecoil


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**burst_constant** | **float** |  | [optional] 
**burst_exponent** | **float** |  | [optional] 
**burst_slope** | **float** |  | [optional] 
**range** | **object** |  | [optional] 

## Example

```python
from deadlock_api_client.models.raw_weapon_info_vertical_recoil import RawWeaponInfoVerticalRecoil

# TODO update the JSON string below
json = "{}"
# create an instance of RawWeaponInfoVerticalRecoil from a JSON string
raw_weapon_info_vertical_recoil_instance = RawWeaponInfoVerticalRecoil.from_json(json)
# print the JSON string representation of the object
print(RawWeaponInfoVerticalRecoil.to_json())

# convert the object into a dict
raw_weapon_info_vertical_recoil_dict = raw_weapon_info_vertical_recoil_instance.to_dict()
# create an instance of RawWeaponInfoVerticalRecoil from a dict
raw_weapon_info_vertical_recoil_from_dict = RawWeaponInfoVerticalRecoil.from_dict(raw_weapon_info_vertical_recoil_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


