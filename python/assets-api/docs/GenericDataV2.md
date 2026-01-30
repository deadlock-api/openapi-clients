# GenericDataV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**damage_flash** | [**DamageFlashV2**](DamageFlashV2.md) |  | 
**glitch_settings** | [**GlitchSettingsV2**](GlitchSettingsV2.md) |  | 
**lane_info** | [**List[LaneInfoV2]**](LaneInfoV2.md) |  | 
**new_player_metrics** | [**List[NewPlayerMetricsV2]**](NewPlayerMetricsV2.md) |  | 
**minimap_team_rebels_color** | [**ColorV1**](ColorV1.md) |  | [optional] 
**minimap_team_combine_color** | [**ColorV1**](ColorV1.md) |  | [optional] 
**enemy_objectives_and_zipline_color** | [**ColorV1**](ColorV1.md) |  | [optional] 
**enemy_objectives_color** | [**ColorV1**](ColorV1.md) |  | [optional] 
**enemy_zipline_color** | [**ColorV1**](ColorV1.md) |  | [optional] 
**item_price_per_tier** | **List[int]** |  | 
**trooper_kill_gold_share_frac** | **List[float]** |  | 
**hero_kill_gold_share_frac** | **List[float]** |  | 
**aim_spring_strength** | **List[float]** |  | 
**targeting_spring_strength** | **List[float]** |  | 
**objective_params** | [**ObjectiveParams**](ObjectiveParams.md) |  | 
**rejuv_params** | [**RejuvParams**](RejuvParams.md) |  | 
**mini_map_offsets** | [**List[MiniMapOffsets]**](MiniMapOffsets.md) |  | 
**weapon_groups** | [**List[ItemGroup]**](ItemGroup.md) |  | 
**armor_groups** | [**List[ItemGroup]**](ItemGroup.md) |  | 
**spirit_groups** | [**List[ItemGroup]**](ItemGroup.md) |  | 
**street_brawl** | [**StreetBrawl**](StreetBrawl.md) |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.generic_data_v2 import GenericDataV2

# TODO update the JSON string below
json = "{}"
# create an instance of GenericDataV2 from a JSON string
generic_data_v2_instance = GenericDataV2.from_json(json)
# print the JSON string representation of the object
print(GenericDataV2.to_json())

# convert the object into a dict
generic_data_v2_dict = generic_data_v2_instance.to_dict()
# create an instance of GenericDataV2 from a dict
generic_data_v2_from_dict = GenericDataV2.from_dict(generic_data_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


