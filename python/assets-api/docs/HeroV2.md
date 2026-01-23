# HeroV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**class_name** | **str** |  | 
**name** | **str** |  | 
**description** | [**HeroDescriptionV2**](HeroDescriptionV2.md) |  | 
**item_draft_weights** | **Dict[str, float]** |  | [optional] 
**player_selectable** | **bool** |  | 
**disabled** | **bool** |  | 
**in_development** | **bool** |  | 
**needs_testing** | **bool** |  | 
**assigned_players_only** | **bool** |  | 
**tags** | **List[str]** |  | [optional] 
**gun_tag** | **str** |  | [optional] 
**hideout_rich_presence** | **str** |  | [optional] 
**hero_type** | [**HeroTypeV2**](HeroTypeV2.md) |  | [optional] 
**prerelease_only** | **bool** |  | [optional] 
**limited_testing** | **bool** |  | 
**complexity** | **int** |  | 
**skin** | **int** |  | 
**images** | [**HeroImagesV2**](HeroImagesV2.md) |  | 
**items** | **Dict[str, str]** |  | 
**starting_stats** | [**HeroStartingStatsV2**](HeroStartingStatsV2.md) |  | 
**item_slot_info** | [**Dict[str, RawHeroItemSlotInfoValueV2]**](RawHeroItemSlotInfoValueV2.md) |  | 
**physics** | [**HeroPhysicsV2**](HeroPhysicsV2.md) |  | 
**colors** | [**HeroColorsV2**](HeroColorsV2.md) |  | 
**shop_stat_display** | [**HeroShopStatDisplayV2**](HeroShopStatDisplayV2.md) |  | 
**cost_bonuses** | **Dict[str, List[RawHeroMapModCostBonusesV2]]** |  | [optional] 
**stats_display** | [**RawHeroStatsDisplayV2**](RawHeroStatsDisplayV2.md) |  | 
**hero_stats_ui** | [**RawHeroStatsUIV2**](RawHeroStatsUIV2.md) |  | 
**level_info** | [**Dict[str, HeroLevelInfoV2]**](HeroLevelInfoV2.md) |  | 
**scaling_stats** | [**Dict[str, RawHeroScalingStatV2]**](RawHeroScalingStatV2.md) |  | 
**purchase_bonuses** | **Dict[str, List[RawHeroPurchaseBonusV2]]** |  | 
**standard_level_up_upgrades** | **Dict[str, float]** |  | 

## Example

```python
from assets_deadlock_api_client.models.hero_v2 import HeroV2

# TODO update the JSON string below
json = "{}"
# create an instance of HeroV2 from a JSON string
hero_v2_instance = HeroV2.from_json(json)
# print the JSON string representation of the object
print(HeroV2.to_json())

# convert the object into a dict
hero_v2_dict = hero_v2_instance.to_dict()
# create an instance of HeroV2 from a dict
hero_v2_from_dict = HeroV2.from_dict(hero_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


