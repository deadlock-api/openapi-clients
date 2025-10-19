# HeroShopStatDisplayV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_e_spirit_stats_display** | [**RawHeroShopSpiritStatsDisplayV2Input**](RawHeroShopSpiritStatsDisplayV2Input.md) |  | 
**m_e_vitality_stats_display** | [**RawHeroShopVitalityStatsDisplayV2Input**](RawHeroShopVitalityStatsDisplayV2Input.md) |  | 
**weapon_stats_display** | [**HeroShopWeaponStatsDisplayV2Input**](HeroShopWeaponStatsDisplayV2Input.md) |  | 

## Example

```python
from assets-deadlock-api-client.models.hero_shop_stat_display_v2_input import HeroShopStatDisplayV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of HeroShopStatDisplayV2Input from a JSON string
hero_shop_stat_display_v2_input_instance = HeroShopStatDisplayV2Input.from_json(json)
# print the JSON string representation of the object
print(HeroShopStatDisplayV2Input.to_json())

# convert the object into a dict
hero_shop_stat_display_v2_input_dict = hero_shop_stat_display_v2_input_instance.to_dict()
# create an instance of HeroShopStatDisplayV2Input from a dict
hero_shop_stat_display_v2_input_from_dict = HeroShopStatDisplayV2Input.from_dict(hero_shop_stat_display_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


