# MiscV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **string** |  | [default to undefined]
**color** | [**ColorV1**](ColorV1.md) |  | [optional] [default to undefined]
**initial_spawn_time** | **number** |  | [optional] [default to undefined]
**respawn_time** | **number** |  | [optional] [default to undefined]
**spawn_interval** | **number** |  | [optional] [default to undefined]
**initial_spawn_delay_in_seconds** | **number** |  | [optional] [default to undefined]
**spawn_interval_in_seconds** | **number** |  | [optional] [default to undefined]
**match_time_mins_for_level2_pickups** | **number** |  | [optional] [default to undefined]
**match_time_mins_for_level3_pickups** | **number** |  | [optional] [default to undefined]
**loot_list_deck_size** | **number** |  | [optional] [default to undefined]
**initial_spawn_delay_seconds** | **number** |  | [optional] [default to undefined]
**health** | **number** |  | [optional] [default to undefined]
**break_on_dodge_touch** | **boolean** |  | [optional] [default to undefined]
**solid_after_death** | **boolean** |  | [optional] [default to undefined]
**render_after_death** | **boolean** |  | [optional] [default to undefined]
**damaged_by_abilities** | **boolean** |  | [optional] [default to undefined]
**damaged_by_melee** | **boolean** |  | [optional] [default to undefined]
**damaged_by_bullets** | **boolean** |  | [optional] [default to undefined]
**is_mantleable** | **boolean** |  | [optional] [default to undefined]
**primary_drop_chance** | **number** |  | [optional] [default to undefined]
**primary_pickups** | [**Array&lt;PickupDefinition&gt;**](PickupDefinition.md) |  | [optional] [default to undefined]
**m_vecPickups_lv2** | [**Array&lt;PickupDefinition&gt;**](PickupDefinition.md) |  | [optional] [default to undefined]
**m_vecPickups_lv3** | [**Array&lt;PickupDefinition&gt;**](PickupDefinition.md) |  | [optional] [default to undefined]
**roll_type** | **string** |  | [optional] [default to undefined]
**gold_amount** | **number** |  | [optional] [default to undefined]
**gold_per_minute_amount** | **number** |  | [optional] [default to undefined]
**modifier** | [**SubclassModifierDefinition**](SubclassModifierDefinition.md) |  | [optional] [default to undefined]
**pickup_radius** | [**PickupRadius**](PickupRadius.md) |  | [optional] [default to undefined]
**expiration_duration** | [**ExpirationDuration**](ExpirationDuration.md) |  | [optional] [default to undefined]
**show_on_minimap** | **boolean** |  | [optional] [default to undefined]
**orb_spawn_delay_min** | **number** |  | [optional] [default to undefined]
**orb_spawn_delay_max** | **number** |  | [optional] [default to undefined]
**lifetime** | **number** |  | [optional] [default to undefined]
**collision_radius** | **number** |  | [optional] [default to undefined]
**id** | **number** |  | [readonly] [default to undefined]

## Example

```typescript
import { MiscV2 } from 'assets_deadlock_api_client';

const instance: MiscV2 = {
    class_name,
    color,
    initial_spawn_time,
    respawn_time,
    spawn_interval,
    initial_spawn_delay_in_seconds,
    spawn_interval_in_seconds,
    match_time_mins_for_level2_pickups,
    match_time_mins_for_level3_pickups,
    loot_list_deck_size,
    initial_spawn_delay_seconds,
    health,
    break_on_dodge_touch,
    solid_after_death,
    render_after_death,
    damaged_by_abilities,
    damaged_by_melee,
    damaged_by_bullets,
    is_mantleable,
    primary_drop_chance,
    primary_pickups,
    m_vecPickups_lv2,
    m_vecPickups_lv3,
    roll_type,
    gold_amount,
    gold_per_minute_amount,
    modifier,
    pickup_radius,
    expiration_duration,
    show_on_minimap,
    orb_spawn_delay_min,
    orb_spawn_delay_max,
    lifetime,
    collision_radius,
    id,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
