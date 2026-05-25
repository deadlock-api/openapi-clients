# GenericData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aim_spring_strength** | **List[float]** |  | 
**armor_groups** | [**List[ItemGroup]**](ItemGroup.md) |  | 
**damage_flash** | [**DamageFlash**](DamageFlash.md) |  | 
**enemy_objectives_and_zipline_color** | [**Color**](Color.md) |  | [optional] 
**enemy_objectives_color** | [**Color**](Color.md) |  | [optional] 
**enemy_zipline_color** | [**Color**](Color.md) |  | [optional] 
**glitch_settings** | [**GlitchSettings**](GlitchSettings.md) |  | 
**hero_kill_gold_share_frac** | **List[float]** |  | 
**item_price_per_tier** | **List[int]** |  | 
**lane_info** | [**List[LaneInfo]**](LaneInfo.md) |  | 
**mini_map_offsets** | [**List[MiniMapOffsets]**](MiniMapOffsets.md) |  | 
**minimap_team_combine_color** | [**Color**](Color.md) |  | [optional] 
**minimap_team_rebels_color** | [**Color**](Color.md) |  | [optional] 
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


