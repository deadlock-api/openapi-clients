# ResponseGetItemV2ItemsIdOrClassNameGet


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
**properties** | [**{ [key: string]: UpgradePropertyV2; }**](UpgradePropertyV2.md) |  | [optional] [default to undefined]
**weapon_info** | [**RawItemWeaponInfoV2**](RawItemWeaponInfoV2.md) |  | [optional] [default to undefined]
**type** | **string** |  | [optional] [default to TypeEnum_Ability]
**grant_ammo_on_cast** | **boolean** |  | [optional] [default to undefined]
**behaviours** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**description** | [**UpgradeDescriptionV2**](UpgradeDescriptionV2.md) |  | [default to undefined]
**tooltip_details** | [**AbilityTooltipDetailsV2**](AbilityTooltipDetailsV2.md) |  | [optional] [default to undefined]
**upgrades** | [**Array&lt;RawAbilityUpgradeV2&gt;**](RawAbilityUpgradeV2.md) |  | [optional] [default to undefined]
**ability_type** | [**AbilityTypeV2**](AbilityTypeV2.md) |  | [optional] [default to undefined]
**boss_damage_scale** | **number** |  | [optional] [default to undefined]
**dependant_abilities** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**videos** | [**AbilityVideosV2**](AbilityVideosV2.md) |  | [optional] [default to undefined]
**dependent_abilities** | [**{ [key: string]: AbilityV2DependentAbilitiesValue; }**](AbilityV2DependentAbilitiesValue.md) |  | [optional] [default to undefined]
**shop_image** | **string** |  | [optional] [default to undefined]
**shop_image_webp** | **string** |  | [optional] [default to undefined]
**shop_image_small** | **string** |  | [optional] [default to undefined]
**shop_image_small_webp** | **string** |  | [optional] [default to undefined]
**item_slot_type** | [**ItemSlotTypeV2**](ItemSlotTypeV2.md) |  | [default to undefined]
**item_tier** | [**ItemTierV2**](ItemTierV2.md) |  | [default to undefined]
**disabled** | **boolean** |  | [optional] [default to undefined]
**activation** | [**RawAbilityActivationV2**](RawAbilityActivationV2.md) |  | [default to undefined]
**imbue** | [**RawAbilityImbueV2**](RawAbilityImbueV2.md) |  | [optional] [default to undefined]
**component_items** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**tooltip_sections** | [**Array&lt;UpgradeTooltipSectionV2&gt;**](UpgradeTooltipSectionV2.md) |  | [optional] [default to undefined]
**is_active_item** | **boolean** |  | [readonly] [default to undefined]
**shopable** | **boolean** |  | [readonly] [default to undefined]
**cost** | **number** |  | [readonly] [default to undefined]

## Example

```typescript
import { ResponseGetItemV2ItemsIdOrClassNameGet } from 'assets_deadlock_api_client';

const instance: ResponseGetItemV2ItemsIdOrClassNameGet = {
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
    grant_ammo_on_cast,
    behaviours,
    description,
    tooltip_details,
    upgrades,
    ability_type,
    boss_damage_scale,
    dependant_abilities,
    videos,
    dependent_abilities,
    shop_image,
    shop_image_webp,
    shop_image_small,
    shop_image_small_webp,
    item_slot_type,
    item_tier,
    disabled,
    activation,
    imbue,
    component_items,
    tooltip_sections,
    is_active_item,
    shopable,
    cost,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
