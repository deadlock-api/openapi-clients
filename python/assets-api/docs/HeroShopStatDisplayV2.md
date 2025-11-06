# HeroShopStatDisplayV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spirit_stats_display** | [**RawHeroShopSpiritStatsDisplayV2**](RawHeroShopSpiritStatsDisplayV2.md) |  | 
**vitality_stats_display** | [**RawHeroShopVitalityStatsDisplayV2**](RawHeroShopVitalityStatsDisplayV2.md) |  | 
**weapon_stats_display** | [**HeroShopWeaponStatsDisplayV2**](HeroShopWeaponStatsDisplayV2.md) |  | 

## Example

```python
from assets-deadlock-api-client.models.hero_shop_stat_display_v2 import HeroShopStatDisplayV2

# TODO update the JSON string below
json = "{}"
# create an instance of HeroShopStatDisplayV2 from a JSON string
hero_shop_stat_display_v2_instance = HeroShopStatDisplayV2.from_json(json)
# print the JSON string representation of the object
print(HeroShopStatDisplayV2.to_json())

# convert the object into a dict
hero_shop_stat_display_v2_dict = hero_shop_stat_display_v2_instance.to_dict()
# create an instance of HeroShopStatDisplayV2 from a dict
hero_shop_stat_display_v2_from_dict = HeroShopStatDisplayV2.from_dict(hero_shop_stat_display_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


