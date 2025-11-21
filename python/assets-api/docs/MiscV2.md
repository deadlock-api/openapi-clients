# MiscV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **str** |  | 
**color** | [**ColorV1**](ColorV1.md) |  | [optional] 
**initial_spawn_time** | **float** |  | [optional] 
**respawn_time** | **float** |  | [optional] 
**spawn_interval** | **float** |  | [optional] 
**initial_spawn_delay_in_seconds** | **int** |  | [optional] 
**spawn_interval_in_seconds** | **int** |  | [optional] 
**match_time_mins_for_level2_pickups** | **int** |  | [optional] 
**match_time_mins_for_level3_pickups** | **int** |  | [optional] 
**loot_list_deck_size** | **int** |  | [optional] 
**initial_spawn_delay_seconds** | **int** |  | [optional] 
**health** | **int** |  | [optional] 
**break_on_dodge_touch** | **bool** |  | [optional] 
**solid_after_death** | **bool** |  | [optional] 
**render_after_death** | **bool** |  | [optional] 
**damaged_by_abilities** | **bool** |  | [optional] 
**damaged_by_melee** | **bool** |  | [optional] 
**damaged_by_bullets** | **bool** |  | [optional] 
**is_mantleable** | **bool** |  | [optional] 
**primary_drop_chance** | **float** |  | [optional] 
**primary_pickups** | [**List[PickupDefinition]**](PickupDefinition.md) |  | [optional] 
**m_vec_pickups_lv2** | [**List[PickupDefinition]**](PickupDefinition.md) |  | [optional] 
**m_vec_pickups_lv3** | [**List[PickupDefinition]**](PickupDefinition.md) |  | [optional] 
**roll_type** | **str** |  | [optional] 
**gold_amount** | **float** |  | [optional] 
**gold_per_minute_amount** | **float** |  | [optional] 
**modifier** | [**SubclassModifierDefinition**](SubclassModifierDefinition.md) |  | [optional] 
**pickup_radius** | **float** |  | [optional] 
**expiration_duration** | **float** |  | [optional] 
**show_on_minimap** | **bool** |  | [optional] 
**orb_spawn_delay_min** | **float** |  | [optional] 
**orb_spawn_delay_max** | **float** |  | [optional] 
**lifetime** | **float** |  | [optional] 
**collision_radius** | **float** |  | [optional] 
**id** | **int** |  | [readonly] 

## Example

```python
from assets_deadlock_api_client.models.misc_v2 import MiscV2

# TODO update the JSON string below
json = "{}"
# create an instance of MiscV2 from a JSON string
misc_v2_instance = MiscV2.from_json(json)
# print the JSON string representation of the object
print(MiscV2.to_json())

# convert the object into a dict
misc_v2_dict = misc_v2_instance.to_dict()
# create an instance of MiscV2 from a dict
misc_v2_from_dict = MiscV2.from_dict(misc_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


