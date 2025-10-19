# RawItemWeaponInfoBulletSpeedCurveV2Output


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spline** | [**List[RawItemWeaponInfoBulletSpeedCurveSplineV2Output]**](RawItemWeaponInfoBulletSpeedCurveSplineV2Output.md) |  | [optional] 
**domain_maxs** | **List[float]** |  | 
**domain_mins** | **List[float]** |  | 

## Example

```python
from assets-deadlock-api-client.models.raw_item_weapon_info_bullet_speed_curve_v2_output import RawItemWeaponInfoBulletSpeedCurveV2Output

# TODO update the JSON string below
json = "{}"
# create an instance of RawItemWeaponInfoBulletSpeedCurveV2Output from a JSON string
raw_item_weapon_info_bullet_speed_curve_v2_output_instance = RawItemWeaponInfoBulletSpeedCurveV2Output.from_json(json)
# print the JSON string representation of the object
print(RawItemWeaponInfoBulletSpeedCurveV2Output.to_json())

# convert the object into a dict
raw_item_weapon_info_bullet_speed_curve_v2_output_dict = raw_item_weapon_info_bullet_speed_curve_v2_output_instance.to_dict()
# create an instance of RawItemWeaponInfoBulletSpeedCurveV2Output from a dict
raw_item_weapon_info_bullet_speed_curve_v2_output_from_dict = RawItemWeaponInfoBulletSpeedCurveV2Output.from_dict(raw_item_weapon_info_bullet_speed_curve_v2_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


