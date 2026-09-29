# MiscEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**break_on_dodge_touch** | Option<**bool**> |  | [optional]
**buff_type_graph_color** | Option<[**models::Color**](Color.md)> | Permanent pickups: color used for the buff in the stat graph. | [optional]
**buff_type_loc_string** | Option<**String**> | Permanent pickups: localization token of the stat the buff raises. | [optional]
**buff_type_value_unit** | Option<**String**> | Permanent pickups: unit of the buff value (e.g. `Percent`, `Meters`). | [optional]
**class_name** | **String** |  | 
**collision_radius** | Option<**f64**> |  | [optional]
**color** | Option<[**models::Color**](Color.md)> |  | [optional]
**damaged_by_abilities** | Option<**bool**> |  | [optional]
**damaged_by_bullets** | Option<**bool**> |  | [optional]
**damaged_by_melee** | Option<**bool**> |  | [optional]
**damaged_by_slide** | Option<**bool**> |  | [optional]
**expiration_duration** | Option<[**models::CurveOrFloat**](CurveOrFloat.md)> |  | [optional]
**gold_amount** | Option<**f64**> |  | [optional]
**gold_per_minute_amount** | Option<**f64**> |  | [optional]
**health** | Option<**i64**> |  | [optional]
**heavy_melee_hit_count** | Option<**i64**> |  | [optional]
**heavy_melee_only** | Option<**bool**> |  | [optional]
**id** | **u32** |  | 
**initial_spawn_delay_in_seconds** | Option<**i64**> |  | [optional]
**initial_spawn_delay_seconds** | Option<**i64**> | Duplicate of `initial_spawn_delay_in_seconds` for shape parity. | [optional]
**initial_spawn_time** | Option<**f64**> |  | [optional]
**is_mantleable** | Option<**bool**> |  | [optional]
**lifetime** | Option<**f64**> |  | [optional]
**loot_list_deck_size** | Option<**i64**> |  | [optional]
**m_vec_pickups_lv2** | Option<[**Vec<models::Pickup>**](Pickup.md)> |  | [optional]
**m_vec_pickups_lv3** | Option<[**Vec<models::Pickup>**](Pickup.md)> |  | [optional]
**match_time_mins_for_level2_pickups** | Option<**i64**> |  | [optional]
**match_time_mins_for_level3_pickups** | Option<**i64**> |  | [optional]
**modifier** | Option<[**models::SubclassModifierDefinition**](SubclassModifierDefinition.md)> |  | [optional]
**orb_spawn_delay_max** | Option<**f64**> |  | [optional]
**orb_spawn_delay_min** | Option<**f64**> |  | [optional]
**pickup_chances** | Option<**std::collections::HashMap<String, f64>**> | Pickup name to relative weight (build 6711+); replaces the `primary_pickups` / `m_vecPickups_lv*` lists. | [optional]
**pickup_radius** | Option<[**models::CurveOrFloat**](CurveOrFloat.md)> |  | [optional]
**powerup_drop_chance** | Option<**f64**> | Drop chance (percent) for build 6711+; replaces `primary_drop_chance`. | [optional]
**primary_drop_chance** | Option<**f64**> | Pre-6711 builds only; see `powerup_drop_chance`. | [optional]
**primary_pickups** | Option<[**Vec<models::Pickup>**](Pickup.md)> |  | [optional]
**render_after_death** | Option<**bool**> |  | [optional]
**respawn_time** | Option<**f64**> |  | [optional]
**roll_type** | Option<**String**> | Known values for `m_eRollType`. Unknown values pass through unchanged so a newly-introduced roll type doesn't 500. Known values: `ECitadelRandomRoll_BreakablePowerupPickup`, `ECitadelRandomRoll_BreakableGoldPickup`. | [optional]
**show_on_minimap** | Option<**bool**> |  | [optional]
**solid_after_death** | Option<**bool**> |  | [optional]
**spawn_interval** | Option<**f64**> |  | [optional]
**spawn_interval_in_seconds** | Option<**i64**> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


