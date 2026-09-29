# MiscEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**break_on_dodge_touch** | **boolean** |  | [optional] [default to undefined]
**buff_type_graph_color** | [**Color**](Color.md) | Permanent pickups: color used for the buff in the stat graph. | [optional] [default to undefined]
**buff_type_loc_string** | **string** | Permanent pickups: localization token of the stat the buff raises. | [optional] [default to undefined]
**buff_type_value_unit** | **string** | Permanent pickups: unit of the buff value (e.g. &#x60;Percent&#x60;, &#x60;Meters&#x60;). | [optional] [default to undefined]
**class_name** | **string** |  | [default to undefined]
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
**id** | **number** |  | [default to undefined]
**initial_spawn_delay_in_seconds** | **number** |  | [optional] [default to undefined]
**initial_spawn_delay_seconds** | **number** | Duplicate of &#x60;initial_spawn_delay_in_seconds&#x60; for shape parity. | [optional] [default to undefined]
**initial_spawn_time** | **number** |  | [optional] [default to undefined]
**is_mantleable** | **boolean** |  | [optional] [default to undefined]
**lifetime** | **number** |  | [optional] [default to undefined]
**loot_list_deck_size** | **number** |  | [optional] [default to undefined]
**m_vecPickups_lv2** | [**Array&lt;Pickup&gt;**](Pickup.md) |  | [optional] [default to undefined]
**m_vecPickups_lv3** | [**Array&lt;Pickup&gt;**](Pickup.md) |  | [optional] [default to undefined]
**match_time_mins_for_level2_pickups** | **number** |  | [optional] [default to undefined]
**match_time_mins_for_level3_pickups** | **number** |  | [optional] [default to undefined]
**modifier** | [**SubclassModifierDefinition**](SubclassModifierDefinition.md) |  | [optional] [default to undefined]
**orb_spawn_delay_max** | **number** |  | [optional] [default to undefined]
**orb_spawn_delay_min** | **number** |  | [optional] [default to undefined]
**pickup_chances** | **{ [key: string]: number; }** | Pickup name to relative weight (build 6711+); replaces the &#x60;primary_pickups&#x60; / &#x60;m_vecPickups_lv*&#x60; lists. | [optional] [default to undefined]
**pickup_radius** | [**CurveOrFloat**](CurveOrFloat.md) |  | [optional] [default to undefined]
**powerup_drop_chance** | **number** | Drop chance (percent) for build 6711+; replaces &#x60;primary_drop_chance&#x60;. | [optional] [default to undefined]
**primary_drop_chance** | **number** | Pre-6711 builds only; see &#x60;powerup_drop_chance&#x60;. | [optional] [default to undefined]
**primary_pickups** | [**Array&lt;Pickup&gt;**](Pickup.md) |  | [optional] [default to undefined]
**render_after_death** | **boolean** |  | [optional] [default to undefined]
**respawn_time** | **number** |  | [optional] [default to undefined]
**roll_type** | **string** | Known values for &#x60;m_eRollType&#x60;. Unknown values pass through unchanged so a newly-introduced roll type doesn\&#39;t 500. Known values: &#x60;ECitadelRandomRoll_BreakablePowerupPickup&#x60;, &#x60;ECitadelRandomRoll_BreakableGoldPickup&#x60;. | [optional] [default to undefined]
**show_on_minimap** | **boolean** |  | [optional] [default to undefined]
**solid_after_death** | **boolean** |  | [optional] [default to undefined]
**spawn_interval** | **number** |  | [optional] [default to undefined]
**spawn_interval_in_seconds** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { MiscEntity } from 'deadlock_api_client';

const instance: MiscEntity = {
    break_on_dodge_touch,
    buff_type_graph_color,
    buff_type_loc_string,
    buff_type_value_unit,
    class_name,
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
    id,
    initial_spawn_delay_in_seconds,
    initial_spawn_delay_seconds,
    initial_spawn_time,
    is_mantleable,
    lifetime,
    loot_list_deck_size,
    m_vecPickups_lv2,
    m_vecPickups_lv3,
    match_time_mins_for_level2_pickups,
    match_time_mins_for_level3_pickups,
    modifier,
    orb_spawn_delay_max,
    orb_spawn_delay_min,
    pickup_chances,
    pickup_radius,
    powerup_drop_chance,
    primary_drop_chance,
    primary_pickups,
    render_after_death,
    respawn_time,
    roll_type,
    show_on_minimap,
    solid_after_death,
    spawn_interval,
    spawn_interval_in_seconds,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
