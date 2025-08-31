# HeroShopWeaponStatsDisplayV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_stats** | **List[str]** |  | 
**other_display_stats** | **List[str]** |  | 
**weapon_attributes** | **List[str]** |  | [optional] 
**weapon_image** | **str** |  | [optional] 
**weapon_image_webp** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.hero_shop_weapon_stats_display_v2 import HeroShopWeaponStatsDisplayV2

# TODO update the JSON string below
json = "{}"
# create an instance of HeroShopWeaponStatsDisplayV2 from a JSON string
hero_shop_weapon_stats_display_v2_instance = HeroShopWeaponStatsDisplayV2.from_json(json)
# print the JSON string representation of the object
print(HeroShopWeaponStatsDisplayV2.to_json())

# convert the object into a dict
hero_shop_weapon_stats_display_v2_dict = hero_shop_weapon_stats_display_v2_instance.to_dict()
# create an instance of HeroShopWeaponStatsDisplayV2 from a dict
hero_shop_weapon_stats_display_v2_from_dict = HeroShopWeaponStatsDisplayV2.from_dict(hero_shop_weapon_stats_display_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


