# # UpgradeV2Output

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  |
**class_name** | **string** |  |
**name** | **string** |  |
**start_trained** | **bool** |  | [optional]
**image** | **string** |  | [optional]
**image_webp** | **string** |  | [optional]
**hero** | **int** |  | [optional]
**heroes** | **int[]** |  | [optional]
**update_time** | **int** |  | [optional]
**properties** | [**array<string,\OpenAPI\Client\Model\UpgradePropertyV2Output>**](UpgradePropertyV2Output.md) |  | [optional]
**weapon_info** | [**\OpenAPI\Client\Model\RawItemWeaponInfoV2Output**](RawItemWeaponInfoV2Output.md) |  | [optional]
**type** | **string** |  | [optional] [default to 'upgrade']
**shop_image** | **string** |  | [optional]
**shop_image_webp** | **string** |  | [optional]
**shop_image_small** | **string** |  | [optional]
**shop_image_small_webp** | **string** |  | [optional]
**item_slot_type** | [**\OpenAPI\Client\Model\ItemSlotTypeV2**](ItemSlotTypeV2.md) |  |
**item_tier** | [**\OpenAPI\Client\Model\ItemTierV2**](ItemTierV2.md) |  |
**disabled** | **bool** |  | [optional]
**description** | [**\OpenAPI\Client\Model\UpgradeDescriptionV2**](UpgradeDescriptionV2.md) |  | [optional]
**activation** | [**\OpenAPI\Client\Model\RawAbilityActivationV2**](RawAbilityActivationV2.md) |  |
**imbue** | [**\OpenAPI\Client\Model\RawAbilityImbueV2**](RawAbilityImbueV2.md) |  | [optional]
**component_items** | **string[]** |  | [optional]
**tooltip_sections** | [**\OpenAPI\Client\Model\UpgradeTooltipSectionV2Output[]**](UpgradeTooltipSectionV2Output.md) |  | [optional]
**is_active_item** | **bool** |  | [readonly]
**shopable** | **bool** |  | [readonly]
**cost** | **int** |  | [readonly]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
