# RawItemWeaponInfoBulletSpeedCurveV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spline** | [**List[RawItemWeaponInfoBulletSpeedCurveSplineV2]**](RawItemWeaponInfoBulletSpeedCurveSplineV2.md) |  | [optional] 
**domain_maxs** | **List[float]** |  | 
**domain_mins** | **List[float]** |  | 

## Example

```python
from assets-deadlock-api-client.models.raw_item_weapon_info_bullet_speed_curve_v2 import RawItemWeaponInfoBulletSpeedCurveV2

# TODO update the JSON string below
json = "{}"
# create an instance of RawItemWeaponInfoBulletSpeedCurveV2 from a JSON string
raw_item_weapon_info_bullet_speed_curve_v2_instance = RawItemWeaponInfoBulletSpeedCurveV2.from_json(json)
# print the JSON string representation of the object
print(RawItemWeaponInfoBulletSpeedCurveV2.to_json())

# convert the object into a dict
raw_item_weapon_info_bullet_speed_curve_v2_dict = raw_item_weapon_info_bullet_speed_curve_v2_instance.to_dict()
# create an instance of RawItemWeaponInfoBulletSpeedCurveV2 from a dict
raw_item_weapon_info_bullet_speed_curve_v2_from_dict = RawItemWeaponInfoBulletSpeedCurveV2.from_dict(raw_item_weapon_info_bullet_speed_curve_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


