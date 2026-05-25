# RawItemWeaponInfoBulletSpeedCurve


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_maxs** | **List[float]** |  | 
**domain_mins** | **List[float]** |  | 
**spline** | [**List[RawItemWeaponInfoBulletSpeedCurveSpline]**](RawItemWeaponInfoBulletSpeedCurveSpline.md) |  | [optional] 

## Example

```python
from deadlock_api_client.models.raw_item_weapon_info_bullet_speed_curve import RawItemWeaponInfoBulletSpeedCurve

# TODO update the JSON string below
json = "{}"
# create an instance of RawItemWeaponInfoBulletSpeedCurve from a JSON string
raw_item_weapon_info_bullet_speed_curve_instance = RawItemWeaponInfoBulletSpeedCurve.from_json(json)
# print the JSON string representation of the object
print(RawItemWeaponInfoBulletSpeedCurve.to_json())

# convert the object into a dict
raw_item_weapon_info_bullet_speed_curve_dict = raw_item_weapon_info_bullet_speed_curve_instance.to_dict()
# create an instance of RawItemWeaponInfoBulletSpeedCurve from a dict
raw_item_weapon_info_bullet_speed_curve_from_dict = RawItemWeaponInfoBulletSpeedCurve.from_dict(raw_item_weapon_info_bullet_speed_curve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


