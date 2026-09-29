# Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ability_type** | [**\OpenAPI\Client\Model\AbilityType**](AbilityType.md) |  | [optional]
**behaviours** | **string[]** |  | [optional]
**boss_damage_scale** | **float** |  | [optional]
**class_name** | **string** |  |
**dependant_abilities** | **string[]** |  | [optional]
**dependent_abilities** | [**array<string,\OpenAPI\Client\Model\DependantAbilities>**](DependantAbilities.md) |  | [optional]
**description** | [**\OpenAPI\Client\Model\UpgradeDescription**](UpgradeDescription.md) |  |
**grant_ammo_on_cast** | **bool** |  | [optional]
**hero** | **int** |  | [optional]
**heroes** | **int[]** |  | [optional]
**id** | **int** |  |
**image** | **string** |  | [optional]
**image_webp** | **string** |  | [optional]
**name** | **string** |  |
**properties** | [**array<string,\OpenAPI\Client\Model\UpgradeProperty>**](UpgradeProperty.md) |  | [optional]
**start_trained** | **bool** |  | [optional]
**tooltip_details** | [**\OpenAPI\Client\Model\AbilityTooltipDetails**](AbilityTooltipDetails.md) |  | [optional]
**type** | [**\OpenAPI\Client\Model\ItemType**](ItemType.md) |  |
**update_time** | **int** |  | [optional]
**upgrades** | [**\OpenAPI\Client\Model\RawAbilityUpgrade[]**](RawAbilityUpgrade.md) |  | [optional]
**videos** | [**\OpenAPI\Client\Model\AbilityVideos**](AbilityVideos.md) |  | [optional]
**weapon_info** | [**\OpenAPI\Client\Model\RawItemWeaponInfoInner**](RawItemWeaponInfoInner.md) |  | [optional]
**crosshair_css_class** | **string** |  | [optional]
**custom_crosshair_settings** | [**\OpenAPI\Client\Model\RawCustomCrosshairSettings**](RawCustomCrosshairSettings.md) |  | [optional]
**use_custom_crosshair_settings** | **bool** |  | [optional]
**activation** | [**\OpenAPI\Client\Model\AbilityActivation**](AbilityActivation.md) |  |
**component_items** | **string[]** |  | [optional]
**corrupted_info** | [**\OpenAPI\Client\Model\CorruptedItemInfo**](CorruptedItemInfo.md) | Present on upgrades the Broker can corrupt (build 6711+). | [optional]
**cost** | **int** |  | [optional]
**disable_item_target** | **string** |  | [optional]
**disabled** | **bool** |  | [optional]
**disabled_shop_filters** | **string[]** | Shop filters (&#x60;snake_case&#x60; &#x60;EShopFilter*&#x60; names) this item is hidden from even though its stats would match them. | [optional]
**imbue** | [**\OpenAPI\Client\Model\AbilityImbue**](AbilityImbue.md) |  | [optional]
**is_active_item** | **bool** |  |
**item_slot_type** | [**\OpenAPI\Client\Model\ItemSlotType**](ItemSlotType.md) |  |
**item_tier** | **int** |  |
**shop_filters** | **string[]** | Extra shop filters (&#x60;snake_case&#x60; &#x60;EShopFilter*&#x60; names, e.g. &#x60;status_grounded&#x60;) this item shows up under, beyond those derived from its stats. | [optional]
**shop_image** | **string** |  | [optional]
**shop_image_small** | **string** |  | [optional]
**shop_image_small_webp** | **string** |  | [optional]
**shop_image_webp** | **string** |  | [optional]
**shop_version** | **int** |  | [optional]
**shopable** | **bool** |  |
**tooltip_sections** | [**\OpenAPI\Client\Model\UpgradeTooltipSection[]**](UpgradeTooltipSection.md) |  | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
