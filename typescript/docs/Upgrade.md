# Upgrade


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation** | [**AbilityActivation**](AbilityActivation.md) |  | [default to undefined]
**class_name** | **string** |  | [default to undefined]
**component_items** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**cost** | **number** |  | [optional] [default to undefined]
**description** | [**UpgradeDescription**](UpgradeDescription.md) |  | [optional] [default to undefined]
**disabled** | **boolean** |  | [optional] [default to undefined]
**hero** | **number** |  | [optional] [default to undefined]
**heroes** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**id** | **number** |  | [default to undefined]
**image** | **string** |  | [optional] [default to undefined]
**image_webp** | **string** |  | [optional] [default to undefined]
**imbue** | [**AbilityImbue**](AbilityImbue.md) |  | [optional] [default to undefined]
**is_active_item** | **boolean** |  | [default to undefined]
**item_slot_type** | [**ItemSlotType**](ItemSlotType.md) |  | [default to undefined]
**item_tier** | **number** |  | [default to undefined]
**name** | **string** |  | [default to undefined]
**properties** | [**{ [key: string]: UpgradeProperty; }**](UpgradeProperty.md) |  | [optional] [default to undefined]
**shop_image** | **string** |  | [optional] [default to undefined]
**shop_image_small** | **string** |  | [optional] [default to undefined]
**shop_image_small_webp** | **string** |  | [optional] [default to undefined]
**shop_image_webp** | **string** |  | [optional] [default to undefined]
**shopable** | **boolean** |  | [default to undefined]
**start_trained** | **boolean** |  | [optional] [default to undefined]
**tooltip_sections** | [**Array&lt;UpgradeTooltipSection&gt;**](UpgradeTooltipSection.md) |  | [optional] [default to undefined]
**type** | [**ItemType**](ItemType.md) |  | [default to undefined]
**update_time** | **number** |  | [optional] [default to undefined]
**upgrades** | [**Array&lt;RawAbilityUpgrade&gt;**](RawAbilityUpgrade.md) |  | [optional] [default to undefined]
**weapon_info** | [**RawItemWeaponInfoInner**](RawItemWeaponInfoInner.md) |  | [optional] [default to undefined]

## Example

```typescript
import { Upgrade } from 'deadlock_api_client';

const instance: Upgrade = {
    activation,
    class_name,
    component_items,
    cost,
    description,
    disabled,
    hero,
    heroes,
    id,
    image,
    image_webp,
    imbue,
    is_active_item,
    item_slot_type,
    item_tier,
    name,
    properties,
    shop_image,
    shop_image_small,
    shop_image_small_webp,
    shop_image_webp,
    shopable,
    start_trained,
    tooltip_sections,
    type,
    update_time,
    upgrades,
    weapon_info,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
