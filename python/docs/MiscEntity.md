# MiscEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**break_on_dodge_touch** | **bool** |  | [optional] 
**buff_type_graph_color** | [**Color**](Color.md) | Permanent pickups: color used for the buff in the stat graph. | [optional] 
**buff_type_loc_string** | **str** | Permanent pickups: localization token of the stat the buff raises. | [optional] 
**buff_type_name** | **str** | Permanent pickups: &#x60;buff_type_loc_string&#x60; localized into the requested language (e.g. &#x60;Fire Rate&#x60;). | [optional] 
**buff_type_value_unit** | **str** | Permanent pickups: unit of the buff value (e.g. &#x60;Percent&#x60;, &#x60;Meters&#x60;). The modifier value itself is in game units (&#x60;Meters&#x60; values are inches, 39.37 per meter). | [optional] 
**class_name** | **str** |  | 
**collection_method** | **str** | How the pickup is collected, e.g. &#x60;Punch&#x60; or &#x60;VacuumTrigger&#x60;. | [optional] 
**collision_radius** | **float** |  | [optional] 
**color** | [**Color**](Color.md) |  | [optional] 
**damaged_by_abilities** | **bool** |  | [optional] 
**damaged_by_bullets** | **bool** |  | [optional] 
**damaged_by_melee** | **bool** |  | [optional] 
**damaged_by_slide** | **bool** |  | [optional] 
**expiration_duration** | [**CurveOrFloat**](CurveOrFloat.md) |  | [optional] 
**gold_amount** | **float** |  | [optional] 
**gold_per_minute_amount** | **float** |  | [optional] 
**health** | **int** |  | [optional] 
**heavy_melee_hit_count** | **int** |  | [optional] 
**heavy_melee_only** | **bool** |  | [optional] 
**hits_required** | **int** | Punchable pickups: hits needed to collect. | [optional] 
**id** | **int** |  | 
**in_shop_modifier** | [**SubclassModifierDefinition**](SubclassModifierDefinition.md) | Corrupted item shop (Broker) trigger: modifier applied while inside. | [optional] 
**initial_spawn_delay_in_seconds** | **int** |  | [optional] 
**initial_spawn_delay_seconds** | **int** | Duplicate of &#x60;initial_spawn_delay_in_seconds&#x60; for shape parity. | [optional] 
**initial_spawn_time** | **float** |  | [optional] 
**is_mantleable** | **bool** |  | [optional] 
**is_permanent_pickup** | **bool** |  | [optional] 
**lifetime** | **float** |  | [optional] 
**loot_list_deck_size** | **int** |  | [optional] 
**m_vec_pickups_lv2** | [**List[Pickup]**](Pickup.md) |  | [optional] 
**m_vec_pickups_lv3** | [**List[Pickup]**](Pickup.md) |  | [optional] 
**match_time_mins_for_level2_pickups** | **int** |  | [optional] 
**match_time_mins_for_level3_pickups** | **int** |  | [optional] 
**minimap_class** | **str** |  | [optional] 
**modifier** | [**SubclassModifierDefinition**](SubclassModifierDefinition.md) |  | [optional] 
**name** | **str** | &#x60;name_loc_string&#x60; localized into the requested language (e.g. &#x60;+1.5% Fire Rate&#x60;). Gold pickups use an ICU plural pattern (&#x60;{amount, plural, one{Soul} other{Souls}}&#x60;). | [optional] 
**name_loc_string** | **str** | Localization token of the pickup&#39;s world label. | [optional] 
**orb_spawn_delay_max** | **float** |  | [optional] 
**orb_spawn_delay_min** | **float** |  | [optional] 
**pickup** | **str** | Pickup spawners: class name of the spawned pickup. | [optional] 
**pickup_chances** | **Dict[str, float]** | Pickup name to relative weight (build 6711+); replaces the &#x60;primary_pickups&#x60; / &#x60;m_vecPickups_lv*&#x60; lists. | [optional] 
**pickup_radius** | [**CurveOrFloat**](CurveOrFloat.md) |  | [optional] 
**powerup_drop_chance** | **float** | Drop chance (percent) for build 6711+; replaces &#x60;primary_drop_chance&#x60;. | [optional] 
**primary_drop_chance** | **float** | Pre-6711 builds only; see &#x60;powerup_drop_chance&#x60;. | [optional] 
**primary_pickups** | [**List[Pickup]**](Pickup.md) |  | [optional] 
**regen_duration** | **float** | Health pickups: seconds over which the healing is applied to heroes. | [optional] 
**regen_duration_troopers** | **float** | Health pickups: seconds over which the healing is applied to troopers. | [optional] 
**regen_max_health_percent** | [**CurveOrFloat**](CurveOrFloat.md) | Health pickups: healing as percent of max health. | [optional] 
**regen_trooper_multi** | **float** | Health pickups: healing multiplier for troopers. | [optional] 
**render_after_death** | **bool** |  | [optional] 
**respawn_time** | **float** |  | [optional] 
**roll_type** | **str** | Known values for &#x60;m_eRollType&#x60;. Unknown values pass through unchanged so a newly-introduced roll type doesn&#39;t 500. Known values: &#x60;ECitadelRandomRoll_BreakablePowerupPickup&#x60;, &#x60;ECitadelRandomRoll_BreakableGoldPickup&#x60;. | [optional] 
**show_on_minimap** | **bool** |  | [optional] 
**single_pickup_override** | **str** | Powerup spawners: class name of the only pickup spawned, overriding &#x60;pickup_chances&#x60;. | [optional] 
**solid_after_death** | **bool** |  | [optional] 
**spawn_delay** | **float** | Pickup spawners: delay (seconds) before the first spawn. | [optional] 
**spawn_interval** | **float** |  | [optional] 
**spawn_interval_in_seconds** | **int** |  | [optional] 
**spawn_music_state** | **str** | Corrupted item shop (Broker) trigger: music cue played on spawn. | [optional] 

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


