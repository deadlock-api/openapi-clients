# Upgrade

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation** | [**\OpenAPI\Client\Model\AbilityActivation**](AbilityActivation.md) |  |
**class_name** | **string** |  |
**component_items** | **string[]** |  | [optional]
**corrupted_info** | [**\OpenAPI\Client\Model\CorruptedItemInfo**](CorruptedItemInfo.md) | Present on upgrades the Broker can corrupt (build 6711+). | [optional]
**cost** | **int** |  | [optional]
**description** | [**\OpenAPI\Client\Model\UpgradeDescription**](UpgradeDescription.md) |  | [optional]
**disable_item_target** | **string** |  | [optional]
**disabled** | **bool** |  | [optional]
**disabled_shop_filters** | **string[]** | Shop filters (&#x60;snake_case&#x60; &#x60;EShopFilter*&#x60; names) this item is hidden from even though its stats would match them. | [optional]
**hero** | **int** |  | [optional]
**heroes** | **int[]** |  | [optional]
**id** | **int** |  |
**image** | **string** |  | [optional]
**image_webp** | **string** |  | [optional]
**imbue** | [**\OpenAPI\Client\Model\AbilityImbue**](AbilityImbue.md) |  | [optional]
**is_active_item** | **bool** |  |
**item_slot_type** | [**\OpenAPI\Client\Model\ItemSlotType**](ItemSlotType.md) |  |
**item_tier** | **int** |  |
**name** | **string** |  |
**properties** | [**array<string,\OpenAPI\Client\Model\UpgradeProperty>**](UpgradeProperty.md) |  | [optional]
**shop_filters** | **string[]** | Extra shop filters (&#x60;snake_case&#x60; &#x60;EShopFilter*&#x60; names, e.g. &#x60;status_grounded&#x60;) this item shows up under, beyond those derived from its stats. | [optional]
**shop_image** | **string** |  | [optional]
**shop_image_small** | **string** |  | [optional]
**shop_image_small_webp** | **string** |  | [optional]
**shop_image_webp** | **string** |  | [optional]
**shop_version** | **int** |  | [optional]
**shopable** | **bool** |  |
**start_trained** | **bool** |  | [optional]
**tooltip_sections** | [**\OpenAPI\Client\Model\UpgradeTooltipSection[]**](UpgradeTooltipSection.md) |  | [optional]
**type** | [**\OpenAPI\Client\Model\ItemType**](ItemType.md) |  |
**update_time** | **int** |  | [optional]
**upgrades** | [**\OpenAPI\Client\Model\RawAbilityUpgrade[]**](RawAbilityUpgrade.md) |  | [optional]
**weapon_info** | [**\OpenAPI\Client\Model\RawItemWeaponInfoInner**](RawItemWeaponInfoInner.md) |  | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
