# MiscEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**break_on_dodge_touch** | **bool** |  | [optional] 
**class_name** | **str** |  | 
**collision_radius** | **float** |  | [optional] 
**color** | [**Color**](Color.md) |  | [optional] 
**damaged_by_abilities** | **bool** |  | [optional] 
**damaged_by_bullets** | **bool** |  | [optional] 
**damaged_by_melee** | **bool** |  | [optional] 
**expiration_duration** | [**CurveOrFloat**](CurveOrFloat.md) |  | [optional] 
**gold_amount** | **float** |  | [optional] 
**gold_per_minute_amount** | **float** |  | [optional] 
**health** | **int** |  | [optional] 
**id** | **int** |  | 
**initial_spawn_delay_in_seconds** | **int** |  | [optional] 
**initial_spawn_delay_seconds** | **int** | Duplicate of &#x60;initial_spawn_delay_in_seconds&#x60; for shape parity. | [optional] 
**initial_spawn_time** | **float** |  | [optional] 
**is_mantleable** | **bool** |  | [optional] 
**lifetime** | **float** |  | [optional] 
**loot_list_deck_size** | **int** |  | [optional] 
**m_vec_pickups_lv2** | [**List[Pickup]**](Pickup.md) |  | [optional] 
**m_vec_pickups_lv3** | [**List[Pickup]**](Pickup.md) |  | [optional] 
**match_time_mins_for_level2_pickups** | **int** |  | [optional] 
**match_time_mins_for_level3_pickups** | **int** |  | [optional] 
**modifier** | [**SubclassModifierDefinition**](SubclassModifierDefinition.md) |  | [optional] 
**orb_spawn_delay_max** | **float** |  | [optional] 
**orb_spawn_delay_min** | **float** |  | [optional] 
**pickup_radius** | [**CurveOrFloat**](CurveOrFloat.md) |  | [optional] 
**primary_drop_chance** | **float** |  | [optional] 
**primary_pickups** | [**List[Pickup]**](Pickup.md) |  | [optional] 
**render_after_death** | **bool** |  | [optional] 
**respawn_time** | **float** |  | [optional] 
**roll_type** | **str** | Known values for &#x60;m_eRollType&#x60;. Unknown values pass through unchanged so a newly-introduced roll type doesn&#39;t 500. Known values: &#x60;ECitadelRandomRoll_BreakablePowerupPickup&#x60;, &#x60;ECitadelRandomRoll_BreakableGoldPickup&#x60;. | [optional] 
**show_on_minimap** | **bool** |  | [optional] 
**solid_after_death** | **bool** |  | [optional] 
**spawn_interval** | **float** |  | [optional] 
**spawn_interval_in_seconds** | **int** |  | [optional] 

## Example

```python
from deadlock_api_client.models.misc_entity import MiscEntity

# TODO update the JSON string below
json = "{}"
# create an instance of MiscEntity from a JSON string
misc_entity_instance = MiscEntity.from_json(json)
# print the JSON string representation of the object
print(MiscEntity.to_json())

# convert the object into a dict
misc_entity_dict = misc_entity_instance.to_dict()
# create an instance of MiscEntity from a dict
misc_entity_from_dict = MiscEntity.from_dict(misc_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


