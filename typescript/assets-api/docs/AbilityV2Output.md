# AbilityV2Output


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [default to undefined]
**class_name** | **string** |  | [default to undefined]
**name** | **string** |  | [default to undefined]
**start_trained** | **boolean** |  | [optional] [default to undefined]
**image** | **string** |  | [optional] [default to undefined]
**image_webp** | **string** |  | [optional] [default to undefined]
**hero** | **number** |  | [optional] [default to undefined]
**heroes** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**update_time** | **number** |  | [optional] [default to undefined]
**properties** | [**{ [key: string]: ItemPropertyV2Output; }**](ItemPropertyV2Output.md) |  | [optional] [default to undefined]
**weapon_info** | [**RawItemWeaponInfoV2Output**](RawItemWeaponInfoV2Output.md) |  | [optional] [default to undefined]
**type** | **string** |  | [optional] [default to TypeEnum_Ability]
**behaviours** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**description** | [**AbilityDescriptionV2**](AbilityDescriptionV2.md) |  | [default to undefined]
**tooltip_details** | [**AbilityTooltipDetailsV2Output**](AbilityTooltipDetailsV2Output.md) |  | [optional] [default to undefined]
**upgrades** | [**Array&lt;RawAbilityUpgradeV2Output&gt;**](RawAbilityUpgradeV2Output.md) |  | [optional] [default to undefined]
**ability_type** | [**AbilityTypeV2**](AbilityTypeV2.md) |  | [optional] [default to undefined]
**boss_damage_scale** | **number** |  | [optional] [default to undefined]
**dependant_abilities** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**videos** | [**AbilityVideosV2**](AbilityVideosV2.md) |  | [optional] [default to undefined]

## Example

```typescript
import { AbilityV2Output } from 'assets-deadlock-api-client';

const instance: AbilityV2Output = {
    id,
    class_name,
    name,
    start_trained,
    image,
    image_webp,
    hero,
    heroes,
    update_time,
    properties,
    weapon_info,
    type,
    behaviours,
    description,
    tooltip_details,
    upgrades,
    ability_type,
    boss_damage_scale,
    dependant_abilities,
    videos,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
