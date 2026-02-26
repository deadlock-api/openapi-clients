# RawHeroV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**class_name** | **str** |  | 
**item_draft_weights** | **Dict[str, float]** |  | [optional] 
**player_selectable** | **bool** |  | 
**disabled** | **bool** |  | 
**in_development** | **bool** |  | 
**needs_testing** | **bool** |  | 
**assigned_players_only** | **bool** |  | 
**available_in_hero_labs** | **bool** |  | [optional] 
**prerelease_only** | **bool** |  | [optional] 
**limited_testing** | **bool** |  | 
**complexity** | **int** |  | 
**skin** | **int** |  | 
**starting_stats** | [**RawHeroStartingStatsV2**](RawHeroStartingStatsV2.md) |  | 
**icon_hero_card** | **str** |  | [optional] 
**icon_image_small** | **str** |  | [optional] 
**minimap_image** | **str** |  | [optional] 
**name_image** | **str** |  | [optional] 
**hero_card_critical** | **str** |  | [optional] 
**hero_card_gloat** | **str** |  | [optional] 
**top_bar_vertical_image** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**gun_tag** | **str** |  | [optional] 
**hideout_rich_presence** | **str** |  | [optional] 
**hero_type** | [**HeroTypeV2**](HeroTypeV2.md) |  | [optional] 
**shop_stat_display** | [**RawHeroShopStatDisplayV2**](RawHeroShopStatDisplayV2.md) |  | 
**cost_bonuses** | **Dict[str, List[RawHeroMapModCostBonusesV2]]** |  | 
**color_ui** | **List[object]** |  | 
**collision_height** | **float** |  | [optional] 
**collision_radius** | **float** |  | [optional] 
**footstep_sound_travel_distance_meters** | **float** |  | [optional] 
**stealth_speed_meters_per_second** | **float** |  | 
**step_height** | **float** |  | [optional] 
**step_sound_time** | **float** |  | [optional] 
**step_sound_time_sprinting** | **float** |  | [optional] 
**stats_display** | [**RawHeroStatsDisplayV2**](RawHeroStatsDisplayV2.md) |  | 
**hero_stats_ui** | [**RawHeroStatsUIV2**](RawHeroStatsUIV2.md) |  | 
**items** | **Dict[str, str]** |  | 
**item_slot_info** | [**Dict[str, RawHeroItemSlotInfoValueV2]**](RawHeroItemSlotInfoValueV2.md) |  | 
**level_info** | [**Dict[str, RawHeroLevelInfoV2]**](RawHeroLevelInfoV2.md) |  | 
**purchase_bonuses** | **Dict[str, List[RawHeroPurchaseBonusV2]]** |  | [optional] 
**scaling_stats** | [**Dict[str, RawHeroScalingStatV2]**](RawHeroScalingStatV2.md) |  | 
**standard_level_up_upgrades** | **Dict[str, float]** |  | 
**background_image** | **str** |  | [readonly] 

## Example

```python
from assets_deadlock_api_client.models.raw_hero_v2 import RawHeroV2

# TODO update the JSON string below
json = "{}"
# create an instance of RawHeroV2 from a JSON string
raw_hero_v2_instance = RawHeroV2.from_json(json)
# print the JSON string representation of the object
print(RawHeroV2.to_json())

# convert the object into a dict
raw_hero_v2_dict = raw_hero_v2_instance.to_dict()
# create an instance of RawHeroV2 from a dict
raw_hero_v2_from_dict = RawHeroV2.from_dict(raw_hero_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


