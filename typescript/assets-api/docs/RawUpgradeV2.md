# RawUpgradeV2


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
**type** | **string** |  | [optional] [default to TypeEnum_Upgrade]
**shop_image** | **string** |  | [optional] [default to undefined]
**shop_image_small** | **string** |  | [optional] [default to undefined]
**item_slot_type** | [**ItemSlotTypeV2**](ItemSlotTypeV2.md) |  | [default to undefined]
**item_tier** | [**ItemTierV2**](ItemTierV2.md) |  | [default to undefined]
**disabled** | **boolean** |  | [optional] [default to undefined]
**activation** | [**RawAbilityActivationV2**](RawAbilityActivationV2.md) |  | [optional] [default to undefined]
**imbue** | [**RawAbilityImbueV2**](RawAbilityImbueV2.md) |  | [optional] [default to undefined]
**component_items** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**tooltip_sections** | [**Array&lt;RawUpgradeTooltipSectionV2&gt;**](RawUpgradeTooltipSectionV2.md) |  | [optional] [default to undefined]
**upgrades** | [**Array&lt;RawAbilityUpgradeV2&gt;**](RawAbilityUpgradeV2.md) |  | [optional] [default to undefined]

## Example

```typescript
import { RawUpgradeV2 } from 'assets_deadlock_api_client';

const instance: RawUpgradeV2 = {
    class_name,
    start_trained,
    image,
    update_time,
    properties,
    weapon_info,
    css_class,
    type,
    shop_image,
    shop_image_small,
    item_slot_type,
    item_tier,
    disabled,
    activation,
    imbue,
    component_items,
    tooltip_sections,
    upgrades,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
