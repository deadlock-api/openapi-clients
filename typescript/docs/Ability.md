# Ability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ability_type** | [**AbilityType**](AbilityType.md) |  | [optional] [default to undefined]
**behaviours** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**boss_damage_scale** | **number** |  | [optional] [default to undefined]
**class_name** | **string** |  | [default to undefined]
**dependant_abilities** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**dependent_abilities** | [**{ [key: string]: DependantAbilities; }**](DependantAbilities.md) |  | [optional] [default to undefined]
**description** | [**AbilityDescription**](AbilityDescription.md) |  | [default to undefined]
**grant_ammo_on_cast** | **boolean** |  | [optional] [default to undefined]
**hero** | **number** |  | [optional] [default to undefined]
**heroes** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**id** | **number** |  | [default to undefined]
**image** | **string** |  | [optional] [default to undefined]
**image_webp** | **string** |  | [optional] [default to undefined]
**name** | **string** |  | [default to undefined]
**properties** | [**{ [key: string]: ItemProperty; }**](ItemProperty.md) |  | [optional] [default to undefined]
**start_trained** | **boolean** |  | [optional] [default to undefined]
**tooltip_details** | [**AbilityTooltipDetails**](AbilityTooltipDetails.md) |  | [optional] [default to undefined]
**type** | [**ItemType**](ItemType.md) |  | [default to undefined]
**update_time** | **number** |  | [optional] [default to undefined]
**upgrades** | [**Array&lt;RawAbilityUpgrade&gt;**](RawAbilityUpgrade.md) |  | [optional] [default to undefined]
**videos** | [**AbilityVideos**](AbilityVideos.md) |  | [optional] [default to undefined]
**weapon_info** | [**RawItemWeaponInfoInner**](RawItemWeaponInfoInner.md) |  | [optional] [default to undefined]

## Example

```typescript
import { Ability } from 'deadlock_api_client';

const instance: Ability = {
    ability_type,
    behaviours,
    boss_damage_scale,
    class_name,
    dependant_abilities,
    dependent_abilities,
    description,
    grant_ammo_on_cast,
    hero,
    heroes,
    id,
    image,
    image_webp,
    name,
    properties,
    start_trained,
    tooltip_details,
    type,
    update_time,
    upgrades,
    videos,
    weapon_info,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
