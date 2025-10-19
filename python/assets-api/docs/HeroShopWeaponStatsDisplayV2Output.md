# HeroShopWeaponStatsDisplayV2Output


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
from assets-deadlock-api-client.models.hero_shop_weapon_stats_display_v2_output import HeroShopWeaponStatsDisplayV2Output

# TODO update the JSON string below
json = "{}"
# create an instance of HeroShopWeaponStatsDisplayV2Output from a JSON string
hero_shop_weapon_stats_display_v2_output_instance = HeroShopWeaponStatsDisplayV2Output.from_json(json)
# print the JSON string representation of the object
print(HeroShopWeaponStatsDisplayV2Output.to_json())

# convert the object into a dict
hero_shop_weapon_stats_display_v2_output_dict = hero_shop_weapon_stats_display_v2_output_instance.to_dict()
# create an instance of HeroShopWeaponStatsDisplayV2Output from a dict
hero_shop_weapon_stats_display_v2_output_from_dict = HeroShopWeaponStatsDisplayV2Output.from_dict(hero_shop_weapon_stats_display_v2_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


