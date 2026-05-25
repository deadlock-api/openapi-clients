# MiscEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**break_on_dodge_touch** | **boolean** |  | [optional] [default to undefined]
**class_name** | **string** |  | [default to undefined]
**collision_radius** | **number** |  | [optional] [default to undefined]
**color** | [**Color**](Color.md) |  | [optional] [default to undefined]
**damaged_by_abilities** | **boolean** |  | [optional] [default to undefined]
**damaged_by_bullets** | **boolean** |  | [optional] [default to undefined]
**damaged_by_melee** | **boolean** |  | [optional] [default to undefined]
**expiration_duration** | [**CurveOrFloat**](CurveOrFloat.md) |  | [optional] [default to undefined]
**gold_amount** | **number** |  | [optional] [default to undefined]
**gold_per_minute_amount** | **number** |  | [optional] [default to undefined]
**health** | **number** |  | [optional] [default to undefined]
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
**pickup_radius** | [**CurveOrFloat**](CurveOrFloat.md) |  | [optional] [default to undefined]
**primary_drop_chance** | **number** |  | [optional] [default to undefined]
**primary_pickups** | [**Array&lt;Pickup&gt;**](Pickup.md) |  | [optional] [default to undefined]
**render_after_death** | **boolean** |  | [optional] [default to undefined]
**respawn_time** | **number** |  | [optional] [default to undefined]
**roll_type** | [**RollType**](RollType.md) |  | [optional] [default to undefined]
**show_on_minimap** | **boolean** |  | [optional] [default to undefined]
**solid_after_death** | **boolean** |  | [optional] [default to undefined]
**spawn_interval** | **number** |  | [optional] [default to undefined]
**spawn_interval_in_seconds** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { MiscEntity } from 'deadlock_api_client';

const instance: MiscEntity = {
    break_on_dodge_touch,
    class_name,
    collision_radius,
    color,
    damaged_by_abilities,
    damaged_by_bullets,
    damaged_by_melee,
    expiration_duration,
    gold_amount,
    gold_per_minute_amount,
    health,
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
    pickup_radius,
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
