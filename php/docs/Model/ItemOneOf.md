# ItemOneOf

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ability_type** | [**\OpenAPI\Client\Model\AbilityType**](AbilityType.md) |  | [optional]
**behaviours** | **string[]** |  | [optional]
**boss_damage_scale** | **float** |  | [optional]
**class_name** | **string** |  |
**dependant_abilities** | **string[]** |  | [optional]
**dependent_abilities** | [**array<string,\OpenAPI\Client\Model\DependantAbilities>**](DependantAbilities.md) | Abilities this one depends on. Entries whose ability has no data are left out. | [optional]
**description** | [**\OpenAPI\Client\Model\AbilityDescription**](AbilityDescription.md) |  |
**grant_ammo_on_cast** | **bool** |  | [optional]
**hero** | **int** |  | [optional]
**heroes** | **int[]** |  | [optional]
**id** | **int** |  |
**image** | **string** |  | [optional]
**image_webp** | **string** |  | [optional]
**name** | **string** |  |
**properties** | [**array<string,\OpenAPI\Client\Model\ItemProperty>**](ItemProperty.md) |  | [optional]
**start_trained** | **bool** |  | [optional]
**tooltip_details** | [**\OpenAPI\Client\Model\AbilityTooltipDetails**](AbilityTooltipDetails.md) |  | [optional]
**update_time** | **int** |  | [optional]
**upgrades** | [**\OpenAPI\Client\Model\RawAbilityUpgrade[]**](RawAbilityUpgrade.md) |  | [optional]
**videos** | [**\OpenAPI\Client\Model\AbilityVideos**](AbilityVideos.md) |  | [optional]
**weapon_info** | [**\OpenAPI\Client\Model\RawItemWeaponInfoInner**](RawItemWeaponInfoInner.md) |  | [optional]
**type** | **string** |  |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
