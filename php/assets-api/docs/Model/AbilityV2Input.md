# # AbilityV2Input

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
**properties** | [**array<string,\OpenAPI\Client\Model\ItemPropertyV2Input>**](ItemPropertyV2Input.md) |  | [optional]
**weapon_info** | [**\OpenAPI\Client\Model\RawItemWeaponInfoV2Input**](RawItemWeaponInfoV2Input.md) |  | [optional]
**type** | **string** |  | [optional] [default to 'ability']
**behaviours** | **string[]** |  | [optional]
**description** | [**\OpenAPI\Client\Model\AbilityDescriptionV2**](AbilityDescriptionV2.md) |  |
**tooltip_details** | [**\OpenAPI\Client\Model\AbilityTooltipDetailsV2Input**](AbilityTooltipDetailsV2Input.md) |  | [optional]
**upgrades** | [**\OpenAPI\Client\Model\RawAbilityUpgradeV2Input[]**](RawAbilityUpgradeV2Input.md) |  | [optional]
**ability_type** | [**\OpenAPI\Client\Model\AbilityTypeV2**](AbilityTypeV2.md) |  | [optional]
**boss_damage_scale** | **float** |  | [optional]
**dependant_abilities** | **string[]** |  | [optional]
**videos** | [**\OpenAPI\Client\Model\AbilityVideosV2**](AbilityVideosV2.md) |  | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
