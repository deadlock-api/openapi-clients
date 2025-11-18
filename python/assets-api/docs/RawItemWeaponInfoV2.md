# RawItemWeaponInfoV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bullet_speed_curve** | [**RawItemWeaponInfoBulletSpeedCurveV2**](RawItemWeaponInfoBulletSpeedCurveV2.md) |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.raw_item_weapon_info_v2 import RawItemWeaponInfoV2

# TODO update the JSON string below
json = "{}"
# create an instance of RawItemWeaponInfoV2 from a JSON string
raw_item_weapon_info_v2_instance = RawItemWeaponInfoV2.from_json(json)
# print the JSON string representation of the object
print(RawItemWeaponInfoV2.to_json())

# convert the object into a dict
raw_item_weapon_info_v2_dict = raw_item_weapon_info_v2_instance.to_dict()
# create an instance of RawItemWeaponInfoV2 from a dict
raw_item_weapon_info_v2_from_dict = RawItemWeaponInfoV2.from_dict(raw_item_weapon_info_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


