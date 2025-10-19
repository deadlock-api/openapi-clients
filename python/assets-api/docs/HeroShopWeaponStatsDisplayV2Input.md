# HeroShopWeaponStatsDisplayV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_vec_display_stats** | **List[str]** |  | 
**m_vec_other_display_stats** | **List[str]** |  | 
**weapon_attributes** | **List[str]** |  | [optional] 
**m_str_weapon_image** | **str** |  | [optional] 
**weapon_image_webp** | **str** |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.hero_shop_weapon_stats_display_v2_input import HeroShopWeaponStatsDisplayV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of HeroShopWeaponStatsDisplayV2Input from a JSON string
hero_shop_weapon_stats_display_v2_input_instance = HeroShopWeaponStatsDisplayV2Input.from_json(json)
# print the JSON string representation of the object
print(HeroShopWeaponStatsDisplayV2Input.to_json())

# convert the object into a dict
hero_shop_weapon_stats_display_v2_input_dict = hero_shop_weapon_stats_display_v2_input_instance.to_dict()
# create an instance of HeroShopWeaponStatsDisplayV2Input from a dict
hero_shop_weapon_stats_display_v2_input_from_dict = HeroShopWeaponStatsDisplayV2Input.from_dict(hero_shop_weapon_stats_display_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


