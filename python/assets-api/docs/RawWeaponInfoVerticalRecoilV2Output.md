# RawWeaponInfoVerticalRecoilV2Output


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | [**Range**](Range.md) |  | [optional] 
**burst_exponent** | **float** |  | [optional] 
**burst_constant** | **float** |  | [optional] 
**burst_slope** | **float** |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.raw_weapon_info_vertical_recoil_v2_output import RawWeaponInfoVerticalRecoilV2Output

# TODO update the JSON string below
json = "{}"
# create an instance of RawWeaponInfoVerticalRecoilV2Output from a JSON string
raw_weapon_info_vertical_recoil_v2_output_instance = RawWeaponInfoVerticalRecoilV2Output.from_json(json)
# print the JSON string representation of the object
print(RawWeaponInfoVerticalRecoilV2Output.to_json())

# convert the object into a dict
raw_weapon_info_vertical_recoil_v2_output_dict = raw_weapon_info_vertical_recoil_v2_output_instance.to_dict()
# create an instance of RawWeaponInfoVerticalRecoilV2Output from a dict
raw_weapon_info_vertical_recoil_v2_output_from_dict = RawWeaponInfoVerticalRecoilV2Output.from_dict(raw_weapon_info_vertical_recoil_v2_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


