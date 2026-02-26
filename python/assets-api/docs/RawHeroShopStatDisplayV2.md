# RawHeroShopStatDisplayV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spirit_stats_display** | [**RawHeroShopSpiritStatsDisplayV2**](RawHeroShopSpiritStatsDisplayV2.md) |  | 
**vitality_stats_display** | [**RawHeroShopVitalityStatsDisplayV2**](RawHeroShopVitalityStatsDisplayV2.md) |  | 
**weapon_stats_display** | [**RawHeroShopWeaponStatsDisplayV2**](RawHeroShopWeaponStatsDisplayV2.md) |  | 

## Example

```python
from assets_deadlock_api_client.models.raw_hero_shop_stat_display_v2 import RawHeroShopStatDisplayV2

# TODO update the JSON string below
json = "{}"
# create an instance of RawHeroShopStatDisplayV2 from a JSON string
raw_hero_shop_stat_display_v2_instance = RawHeroShopStatDisplayV2.from_json(json)
# print the JSON string representation of the object
print(RawHeroShopStatDisplayV2.to_json())

# convert the object into a dict
raw_hero_shop_stat_display_v2_dict = raw_hero_shop_stat_display_v2_instance.to_dict()
# create an instance of RawHeroShopStatDisplayV2 from a dict
raw_hero_shop_stat_display_v2_from_dict = RawHeroShopStatDisplayV2.from_dict(raw_hero_shop_stat_display_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


