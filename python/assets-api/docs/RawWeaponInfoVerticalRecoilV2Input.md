# RawWeaponInfoVerticalRecoilV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_range** | [**MRange**](MRange.md) |  | [optional] 
**m_fl_burst_exponent** | **float** |  | [optional] 
**m_fl_burst_constant** | **float** |  | [optional] 
**m_fl_burst_slope** | **float** |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.raw_weapon_info_vertical_recoil_v2_input import RawWeaponInfoVerticalRecoilV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of RawWeaponInfoVerticalRecoilV2Input from a JSON string
raw_weapon_info_vertical_recoil_v2_input_instance = RawWeaponInfoVerticalRecoilV2Input.from_json(json)
# print the JSON string representation of the object
print(RawWeaponInfoVerticalRecoilV2Input.to_json())

# convert the object into a dict
raw_weapon_info_vertical_recoil_v2_input_dict = raw_weapon_info_vertical_recoil_v2_input_instance.to_dict()
# create an instance of RawWeaponInfoVerticalRecoilV2Input from a dict
raw_weapon_info_vertical_recoil_v2_input_from_dict = RawWeaponInfoVerticalRecoilV2Input.from_dict(raw_weapon_info_vertical_recoil_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


