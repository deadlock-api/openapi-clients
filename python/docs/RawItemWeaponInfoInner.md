# RawItemWeaponInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_bullet_speed_curve** | [**RawItemWeaponInfoBulletSpeedCurve**](RawItemWeaponInfoBulletSpeedCurve.md) |  | [optional] 

## Example

```python
from deadlock_api_client.models.raw_item_weapon_info_inner import RawItemWeaponInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of RawItemWeaponInfoInner from a JSON string
raw_item_weapon_info_inner_instance = RawItemWeaponInfoInner.from_json(json)
# print the JSON string representation of the object
print(RawItemWeaponInfoInner.to_json())

# convert the object into a dict
raw_item_weapon_info_inner_dict = raw_item_weapon_info_inner_instance.to_dict()
# create an instance of RawItemWeaponInfoInner from a dict
raw_item_weapon_info_inner_from_dict = RawItemWeaponInfoInner.from_dict(raw_item_weapon_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


