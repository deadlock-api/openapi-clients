# GenericData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aim_spring_strength** | **List[float]** |  | 
**armor_groups** | [**List[ItemGroup]**](ItemGroup.md) |  | 
**breakable_powerup_loot_params** | [**BreakablePowerupLootParams**](BreakablePowerupLootParams.md) | Loot tables for breakable powerup props (build 6711+). | [optional] 
**color_enemy** | [**Color**](Color.md) | Build 6711+. | [optional] 
**color_friend** | [**Color**](Color.md) | Build 6711+. | [optional] 
**color_team1** | [**Color**](Color.md) | Build 6711+. | [optional] 
**color_team2** | [**Color**](Color.md) | Build 6711+. | [optional] 
**corrupted_item_images** | [**CorruptedItemImages**](CorruptedItemImages.md) | Shop art for corrupted items (build 6711+). | [optional] 
**corrupted_penalties** | [**List[CorruptedPenalty]**](CorruptedPenalty.md) | Penalties that can be rolled onto corrupted items (build 6711+). | [optional] 
**damage_flash** | [**DamageFlash**](DamageFlash.md) |  | 
**enemy_objectives_and_zipline_color** | [**Color**](Color.md) |  | [optional] 
**enemy_objectives_color** | [**Color**](Color.md) |  | [optional] 
**enemy_zipline_color** | [**Color**](Color.md) |  | [optional] 
**glitch_settings** | [**GlitchSettings**](GlitchSettings.md) |  | 
**hero_kill_gold_share_frac** | **List[float]** |  | 
**item_corruption_price_per_tier** | **List[int]** | Extra cost of corrupting an item, by item tier (build 6711+). | [optional] 
**item_price_per_tier** | **List[int]** |  | 
**lane_info** | [**List[LaneInfo]**](LaneInfo.md) |  | 
**map_districts** | [**List[MapDistrict]**](MapDistrict.md) | District / building labels shown on the map (build 6711+). | [optional] 
**mini_map_offsets** | [**List[MiniMapOffsets]**](MiniMapOffsets.md) |  | 
**minimap_team_combine_color** | [**Color**](Color.md) |  | [optional] 
**minimap_team_rebels_color** | [**Color**](Color.md) |  | [optional] 
**neutral_camp_respawn_timer_show_distance** | **float** | Distance within which a neutral camp&#39;s respawn timer is shown (build 6711+). | [optional] 
**new_player_metrics** | [**List[NewPlayerMetrics]**](NewPlayerMetrics.md) |  | 
**objective_params** | [**ObjectiveParams**](ObjectiveParams.md) |  | 
**rejuv_params** | [**RejuvParams**](RejuvParams.md) |  | 
**spirit_groups** | [**List[ItemGroup]**](ItemGroup.md) |  | 
**street_brawl** | [**StreetBrawl**](StreetBrawl.md) |  | [optional] 
**targeting_spring_strength** | **List[float]** |  | 
**trooper_kill_gold_share_frac** | **List[float]** |  | 
**weapon_groups** | [**List[ItemGroup]**](ItemGroup.md) |  | 

## Example

```python
from deadlock_api_client.models.generic_data import GenericData

# TODO update the JSON string below
json = "{}"
# create an instance of GenericData from a JSON string
generic_data_instance = GenericData.from_json(json)
# print the JSON string representation of the object
print(GenericData.to_json())

# convert the object into a dict
generic_data_dict = generic_data_instance.to_dict()
# create an instance of GenericData from a dict
generic_data_from_dict = GenericData.from_dict(generic_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


