# MiscEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**break_on_dodge_touch** | **boolean** |  | [optional] [default to undefined]
**buff_type_graph_color** | [**Color**](Color.md) | Permanent pickups: color used for the buff in the stat graph. | [optional] [default to undefined]
**buff_type_loc_string** | **string** | Permanent pickups: localization token of the stat the buff raises. | [optional] [default to undefined]
**buff_type_name** | **string** | Permanent pickups: &#x60;buff_type_loc_string&#x60; localized into the requested language (e.g. &#x60;Fire Rate&#x60;). | [optional] [default to undefined]
**buff_type_value_unit** | **string** | Permanent pickups: unit of the buff value (e.g. &#x60;Percent&#x60;, &#x60;Meters&#x60;). The modifier value itself is in game units (&#x60;Meters&#x60; values are inches, 39.37 per meter). | [optional] [default to undefined]
**class_name** | **string** |  | [default to undefined]
**collection_method** | **string** | How the pickup is collected, e.g. &#x60;Punch&#x60; or &#x60;VacuumTrigger&#x60;. | [optional] [default to undefined]
**collision_radius** | **number** |  | [optional] [default to undefined]
**color** | [**Color**](Color.md) |  | [optional] [default to undefined]
**damaged_by_abilities** | **boolean** |  | [optional] [default to undefined]
**damaged_by_bullets** | **boolean** |  | [optional] [default to undefined]
**damaged_by_melee** | **boolean** |  | [optional] [default to undefined]
**damaged_by_slide** | **boolean** |  | [optional] [default to undefined]
**expiration_duration** | [**CurveOrFloat**](CurveOrFloat.md) |  | [optional] [default to undefined]
**gold_amount** | **number** |  | [optional] [default to undefined]
**gold_per_minute_amount** | **number** |  | [optional] [default to undefined]
**health** | **number** |  | [optional] [default to undefined]
**heavy_melee_hit_count** | **number** |  | [optional] [default to undefined]
**heavy_melee_only** | **boolean** |  | [optional] [default to undefined]
**hits_required** | **number** | Punchable pickups: hits needed to collect. | [optional] [default to undefined]
**id** | **number** |  | [default to undefined]
**in_shop_modifier** | [**SubclassModifierDefinition**](SubclassModifierDefinition.md) | Corrupted item shop (Broker) trigger: modifier applied while inside. | [optional] [default to undefined]
**initial_spawn_delay_in_seconds** | **number** |  | [optional] [default to undefined]
**initial_spawn_delay_seconds** | **number** | Duplicate of &#x60;initial_spawn_delay_in_seconds&#x60; for shape parity. | [optional] [default to undefined]
**initial_spawn_time** | **number** |  | [optional] [default to undefined]
**is_mantleable** | **boolean** |  | [optional] [default to undefined]
**is_permanent_pickup** | **boolean** |  | [optional] [default to undefined]
**lifetime** | **number** |  | [optional] [default to undefined]
**loot_list_deck_size** | **number** |  | [optional] [default to undefined]
**m_vecPickups_lv2** | [**Array&lt;Pickup&gt;**](Pickup.md) |  | [optional] [default to undefined]
**m_vecPickups_lv3** | [**Array&lt;Pickup&gt;**](Pickup.md) |  | [optional] [default to undefined]
**match_time_mins_for_level2_pickups** | **number** |  | [optional] [default to undefined]
**match_time_mins_for_level3_pickups** | **number** |  | [optional] [default to undefined]
**minimap_class** | **string** |  | [optional] [default to undefined]
**modifier** | [**SubclassModifierDefinition**](SubclassModifierDefinition.md) |  | [optional] [default to undefined]
**name** | **string** | &#x60;name_loc_string&#x60; localized into the requested language (e.g. &#x60;+1.5% Fire Rate&#x60;). Gold pickups use an ICU plural pattern (&#x60;{amount, plural, one{Soul} other{Souls}}&#x60;). | [optional] [default to undefined]
**name_loc_string** | **string** | Localization token of the pickup\&#39;s world label. | [optional] [default to undefined]
**orb_spawn_delay_max** | **number** |  | [optional] [default to undefined]
**orb_spawn_delay_min** | **number** |  | [optional] [default to undefined]
**pickup** | **string** | Pickup spawners: class name of the spawned pickup. | [optional] [default to undefined]
**pickup_chances** | **{ [key: string]: number; }** | Pickup name to relative weight (build 6711+); replaces the &#x60;primary_pickups&#x60; / &#x60;m_vecPickups_lv*&#x60; lists. | [optional] [default to undefined]
**pickup_radius** | [**CurveOrFloat**](CurveOrFloat.md) |  | [optional] [default to undefined]
**powerup_drop_chance** | **number** | Drop chance (percent) for build 6711+; replaces &#x60;primary_drop_chance&#x60;. | [optional] [default to undefined]
**primary_drop_chance** | **number** | Pre-6711 builds only; see &#x60;powerup_drop_chance&#x60;. | [optional] [default to undefined]
**primary_pickups** | [**Array&lt;Pickup&gt;**](Pickup.md) |  | [optional] [default to undefined]
**regen_duration** | **number** | Health pickups: seconds over which the healing is applied to heroes. | [optional] [default to undefined]
**regen_duration_troopers** | **number** | Health pickups: seconds over which the healing is applied to troopers. | [optional] [default to undefined]
**regen_max_health_percent** | [**CurveOrFloat**](CurveOrFloat.md) | Health pickups: healing as percent of max health. | [optional] [default to undefined]
**regen_trooper_multi** | **number** | Health pickups: healing multiplier for troopers. | [optional] [default to undefined]
**render_after_death** | **boolean** |  | [optional] [default to undefined]
**respawn_time** | **number** |  | [optional] [default to undefined]
**roll_type** | **string** | Known values for &#x60;m_eRollType&#x60;. Unknown values pass through unchanged so a newly-introduced roll type doesn\&#39;t 500. Known values: &#x60;ECitadelRandomRoll_BreakablePowerupPickup&#x60;, &#x60;ECitadelRandomRoll_BreakableGoldPickup&#x60;. | [optional] [default to undefined]
**show_on_minimap** | **boolean** |  | [optional] [default to undefined]
**single_pickup_override** | **string** | Powerup spawners: class name of the only pickup spawned, overriding &#x60;pickup_chances&#x60;. | [optional] [default to undefined]
**solid_after_death** | **boolean** |  | [optional] [default to undefined]
**spawn_delay** | **number** | Pickup spawners: delay (seconds) before the first spawn. | [optional] [default to undefined]
**spawn_interval** | **number** |  | [optional] [default to undefined]
**spawn_interval_in_seconds** | **number** |  | [optional] [default to undefined]
**spawn_music_state** | **string** | Corrupted item shop (Broker) trigger: music cue played on spawn. | [optional] [default to undefined]

## Example

```typescript
import { MiscEntity } from 'deadlock_api_client';

const instance: MiscEntity = {
    break_on_dodge_touch,
    buff_type_graph_color,
    buff_type_loc_string,
    buff_type_name,
    buff_type_value_unit,
    class_name,
    collection_method,
    collision_radius,
    color,
    damaged_by_abilities,
    damaged_by_bullets,
    damaged_by_melee,
    damaged_by_slide,
    expiration_duration,
    gold_amount,
    gold_per_minute_amount,
    health,
    heavy_melee_hit_count,
    heavy_melee_only,
    hits_required,
    id,
    in_shop_modifier,
    initial_spawn_delay_in_seconds,
    initial_spawn_delay_seconds,
    initial_spawn_time,
    is_mantleable,
    is_permanent_pickup,
    lifetime,
    loot_list_deck_size,
    m_vecPickups_lv2,
    m_vecPickups_lv3,
    match_time_mins_for_level2_pickups,
    match_time_mins_for_level3_pickups,
    minimap_class,
    modifier,
    name,
    name_loc_string,
    orb_spawn_delay_max,
    orb_spawn_delay_min,
    pickup,
    pickup_chances,
    pickup_radius,
    powerup_drop_chance,
    primary_drop_chance,
    primary_pickups,
    regen_duration,
    regen_duration_troopers,
    regen_max_health_percent,
    regen_trooper_multi,
    render_after_death,
    respawn_time,
    roll_type,
    show_on_minimap,
    single_pickup_override,
    solid_after_death,
    spawn_delay,
    spawn_interval,
    spawn_interval_in_seconds,
    spawn_music_state,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
