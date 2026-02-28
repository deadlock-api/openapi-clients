# RawAbilityV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **string** |  | [default to undefined]
**start_trained** | **boolean** |  | [optional] [default to undefined]
**image** | **string** |  | [optional] [default to undefined]
**update_time** | **number** |  | [optional] [default to undefined]
**properties** | [**{ [key: string]: RawItemPropertyV2; }**](RawItemPropertyV2.md) |  | [optional] [default to undefined]
**weapon_info** | [**RawItemWeaponInfoV2**](RawItemWeaponInfoV2.md) |  | [optional] [default to undefined]
**css_class** | **string** |  | [optional] [default to undefined]
**type** | **string** |  | [optional] [default to TypeEnum_Ability]
**grant_ammo_on_cast** | **boolean** |  | [optional] [default to undefined]
**behaviour_bits** | **string** |  | [optional] [default to undefined]
**upgrades** | [**Array&lt;RawAbilityUpgradeV2&gt;**](RawAbilityUpgradeV2.md) |  | [default to undefined]
**ability_type** | [**AbilityTypeV2**](AbilityTypeV2.md) |  | [optional] [default to undefined]
**boss_damage_scale** | **number** |  | [optional] [default to undefined]
**dependant_abilities** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**video** | **string** |  | [optional] [default to undefined]
**tooltip_details** | [**RawAbilityV2TooltipDetails**](RawAbilityV2TooltipDetails.md) |  | [optional] [default to undefined]
**dependent_abilities** | [**{ [key: string]: AbilityV2DependentAbilitiesValue; }**](AbilityV2DependentAbilitiesValue.md) |  | [optional] [default to undefined]

## Example

```typescript
import { RawAbilityV2 } from 'assets_deadlock_api_client';

const instance: RawAbilityV2 = {
    class_name,
    start_trained,
    image,
    update_time,
    properties,
    weapon_info,
    css_class,
    type,
    grant_ammo_on_cast,
    behaviour_bits,
    upgrades,
    ability_type,
    boss_damage_scale,
    dependant_abilities,
    video,
    tooltip_details,
    dependent_abilities,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
