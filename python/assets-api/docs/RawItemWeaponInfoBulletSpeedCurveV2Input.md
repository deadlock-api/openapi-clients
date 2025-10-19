# RawItemWeaponInfoBulletSpeedCurveV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_spline** | [**List[RawItemWeaponInfoBulletSpeedCurveSplineV2Input]**](RawItemWeaponInfoBulletSpeedCurveSplineV2Input.md) |  | [optional] 
**m_v_domain_maxs** | **List[float]** |  | 
**m_v_domain_mins** | **List[float]** |  | 

## Example

```python
from assets-deadlock-api-client.models.raw_item_weapon_info_bullet_speed_curve_v2_input import RawItemWeaponInfoBulletSpeedCurveV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of RawItemWeaponInfoBulletSpeedCurveV2Input from a JSON string
raw_item_weapon_info_bullet_speed_curve_v2_input_instance = RawItemWeaponInfoBulletSpeedCurveV2Input.from_json(json)
# print the JSON string representation of the object
print(RawItemWeaponInfoBulletSpeedCurveV2Input.to_json())

# convert the object into a dict
raw_item_weapon_info_bullet_speed_curve_v2_input_dict = raw_item_weapon_info_bullet_speed_curve_v2_input_instance.to_dict()
# create an instance of RawItemWeaponInfoBulletSpeedCurveV2Input from a dict
raw_item_weapon_info_bullet_speed_curve_v2_input_from_dict = RawItemWeaponInfoBulletSpeedCurveV2Input.from_dict(raw_item_weapon_info_bullet_speed_curve_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


