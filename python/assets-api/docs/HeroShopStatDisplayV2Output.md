# HeroShopStatDisplayV2Output


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spirit_stats_display** | [**RawHeroShopSpiritStatsDisplayV2Output**](RawHeroShopSpiritStatsDisplayV2Output.md) |  | 
**vitality_stats_display** | [**RawHeroShopVitalityStatsDisplayV2Output**](RawHeroShopVitalityStatsDisplayV2Output.md) |  | 
**weapon_stats_display** | [**HeroShopWeaponStatsDisplayV2Output**](HeroShopWeaponStatsDisplayV2Output.md) |  | 

## Example

```python
from assets-deadlock-api-client.models.hero_shop_stat_display_v2_output import HeroShopStatDisplayV2Output

# TODO update the JSON string below
json = "{}"
# create an instance of HeroShopStatDisplayV2Output from a JSON string
hero_shop_stat_display_v2_output_instance = HeroShopStatDisplayV2Output.from_json(json)
# print the JSON string representation of the object
print(HeroShopStatDisplayV2Output.to_json())

# convert the object into a dict
hero_shop_stat_display_v2_output_dict = hero_shop_stat_display_v2_output_instance.to_dict()
# create an instance of HeroShopStatDisplayV2Output from a dict
hero_shop_stat_display_v2_output_from_dict = HeroShopStatDisplayV2Output.from_dict(hero_shop_stat_display_v2_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


