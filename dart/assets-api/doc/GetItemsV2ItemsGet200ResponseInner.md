# assets-deadlock-api-client.model.GetItemsV2ItemsGet200ResponseInner

## Load the model package
```dart
import 'package:assets-deadlock-api-client/api.dart';
```

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**className** | **String** |  | 
**name** | **String** |  | 
**startTrained** | **bool** |  | [optional] 
**image** | **String** |  | [optional] 
**imageWebp** | **String** |  | [optional] 
**hero** | **int** |  | [optional] 
**heroes** | **List<int>** |  | [optional] [default to const []]
**updateTime** | **int** |  | [optional] 
**properties** | [**Map<String, UpgradePropertyV2>**](UpgradePropertyV2.md) |  | [optional] [default to const {}]
**weaponInfo** | [**RawItemWeaponInfoV2**](RawItemWeaponInfoV2.md) |  | [optional] 
**type** | **String** |  | [optional] [default to 'ability']
**behaviours** | **List<String>** |  | [optional] [default to const []]
**description** | [**UpgradeDescriptionV2**](UpgradeDescriptionV2.md) |  | 
**tooltipDetails** | [**AbilityTooltipDetailsV2**](AbilityTooltipDetailsV2.md) |  | [optional] 
**upgrades** | [**List<RawAbilityUpgradeV2>**](RawAbilityUpgradeV2.md) |  | [optional] [default to const []]
**abilityType** | [**AbilityTypeV2**](AbilityTypeV2.md) |  | [optional] 
**bossDamageScale** | **num** |  | [optional] 
**dependantAbilities** | **List<String>** |  | [optional] [default to const []]
**videos** | [**AbilityVideosV2**](AbilityVideosV2.md) |  | [optional] 
**shopImage** | **String** |  | [optional] 
**shopImageWebp** | **String** |  | [optional] 
**shopImageSmall** | **String** |  | [optional] 
**shopImageSmallWebp** | **String** |  | [optional] 
**itemSlotType** | [**ItemSlotTypeV2**](ItemSlotTypeV2.md) |  | 
**itemTier** | [**ItemTierV2**](ItemTierV2.md) |  | 
**disabled** | **bool** |  | [optional] 
**activation** | [**RawAbilityActivationV2**](RawAbilityActivationV2.md) |  | 
**imbue** | [**RawAbilityImbueV2**](RawAbilityImbueV2.md) |  | [optional] 
**componentItems** | **List<String>** |  | [optional] [default to const []]
**tooltipSections** | [**List<UpgradeTooltipSectionV2>**](UpgradeTooltipSectionV2.md) |  | [optional] [default to const []]
**isActiveItem** | **bool** |  | [readonly] 
**shopable** | **bool** |  | [readonly] 
**cost** | **int** |  | [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


