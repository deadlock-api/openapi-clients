# Item


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ability_type** | [**AbilityType**](AbilityType.md) |  | [optional] [default to undefined]
**behaviours** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**boss_damage_scale** | **number** |  | [optional] [default to undefined]
**class_name** | **string** |  | [default to undefined]
**dependant_abilities** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**dependent_abilities** | [**{ [key: string]: DependantAbilities; }**](DependantAbilities.md) |  | [optional] [default to undefined]
**description** | [**UpgradeDescription**](UpgradeDescription.md) |  | [default to undefined]
**grant_ammo_on_cast** | **boolean** |  | [optional] [default to undefined]
**hero** | **number** |  | [optional] [default to undefined]
**heroes** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**id** | **number** |  | [default to undefined]
**image** | **string** |  | [optional] [default to undefined]
**image_webp** | **string** |  | [optional] [default to undefined]
**name** | **string** |  | [default to undefined]
**properties** | [**{ [key: string]: UpgradeProperty; }**](UpgradeProperty.md) |  | [optional] [default to undefined]
**start_trained** | **boolean** |  | [optional] [default to undefined]
**tooltip_details** | [**AbilityTooltipDetails**](AbilityTooltipDetails.md) |  | [optional] [default to undefined]
**type** | [**ItemType**](ItemType.md) |  | [default to undefined]
**update_time** | **number** |  | [optional] [default to undefined]
**upgrades** | [**Array&lt;RawAbilityUpgrade&gt;**](RawAbilityUpgrade.md) |  | [optional] [default to undefined]
**videos** | [**AbilityVideos**](AbilityVideos.md) |  | [optional] [default to undefined]
**weapon_info** | [**RawItemWeaponInfoInner**](RawItemWeaponInfoInner.md) |  | [optional] [default to undefined]
**crosshair_css_class** | **string** |  | [optional] [default to undefined]
**custom_crosshair_settings** | [**RawCustomCrosshairSettings**](RawCustomCrosshairSettings.md) |  | [optional] [default to undefined]
**use_custom_crosshair_settings** | **boolean** |  | [optional] [default to undefined]
**activation** | [**AbilityActivation**](AbilityActivation.md) |  | [default to undefined]
**component_items** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**corrupted_info** | [**CorruptedItemInfo**](CorruptedItemInfo.md) | Present on upgrades the Broker can corrupt (build 6711+). | [optional] [default to undefined]
**cost** | **number** |  | [optional] [default to undefined]
**disable_item_target** | **string** |  | [optional] [default to undefined]
**disabled** | **boolean** |  | [optional] [default to undefined]
**disabled_shop_filters** | **Array&lt;string&gt;** | Shop filters (&#x60;snake_case&#x60; &#x60;EShopFilter*&#x60; names) this item is hidden from even though its stats would match them. | [optional] [default to undefined]
**imbue** | [**AbilityImbue**](AbilityImbue.md) |  | [optional] [default to undefined]
**is_active_item** | **boolean** |  | [default to undefined]
**item_slot_type** | [**ItemSlotType**](ItemSlotType.md) |  | [default to undefined]
**item_tier** | **number** |  | [default to undefined]
**shop_filters** | **Array&lt;string&gt;** | Extra shop filters (&#x60;snake_case&#x60; &#x60;EShopFilter*&#x60; names, e.g. &#x60;status_grounded&#x60;) this item shows up under, beyond those derived from its stats. | [optional] [default to undefined]
**shop_image** | **string** |  | [optional] [default to undefined]
**shop_image_small** | **string** |  | [optional] [default to undefined]
**shop_image_small_webp** | **string** |  | [optional] [default to undefined]
**shop_image_webp** | **string** |  | [optional] [default to undefined]
**shop_version** | **number** |  | [optional] [default to undefined]
**shopable** | **boolean** |  | [default to undefined]
**tooltip_sections** | [**Array&lt;UpgradeTooltipSection&gt;**](UpgradeTooltipSection.md) |  | [optional] [default to undefined]

## Example

```typescript
import { Item } from 'deadlock_api_client';

const instance: Item = {
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
    crosshair_css_class,
    custom_crosshair_settings,
    use_custom_crosshair_settings,
    activation,
    component_items,
    corrupted_info,
    cost,
    disable_item_target,
    disabled,
    disabled_shop_filters,
    imbue,
    is_active_item,
    item_slot_type,
    item_tier,
    shop_filters,
    shop_image,
    shop_image_small,
    shop_image_small_webp,
    shop_image_webp,
    shop_version,
    shopable,
    tooltip_sections,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
