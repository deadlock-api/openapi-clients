# assets-deadlock-api-client.model.UpgradeV2Input

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
**properties** | [**Map<String, UpgradePropertyV2Input>**](UpgradePropertyV2Input.md) |  | [optional] [default to const {}]
**weaponInfo** | [**RawItemWeaponInfoV2Input**](RawItemWeaponInfoV2Input.md) |  | [optional] 
**type** | **String** |  | [optional] [default to 'upgrade']
**shopImage** | **String** |  | [optional] 
**shopImageWebp** | **String** |  | [optional] 
**shopImageSmall** | **String** |  | [optional] 
**shopImageSmallWebp** | **String** |  | [optional] 
**itemSlotType** | [**ItemSlotTypeV2**](ItemSlotTypeV2.md) |  | 
**itemTier** | [**ItemTierV2**](ItemTierV2.md) |  | 
**disabled** | **bool** |  | [optional] 
**description** | [**UpgradeDescriptionV2**](UpgradeDescriptionV2.md) |  | [optional] 
**activation** | [**RawAbilityActivationV2**](RawAbilityActivationV2.md) |  | 
**imbue** | [**RawAbilityImbueV2**](RawAbilityImbueV2.md) |  | [optional] 
**componentItems** | **List<String>** |  | [optional] [default to const []]
**tooltipSections** | [**List<UpgradeTooltipSectionV2Input>**](UpgradeTooltipSectionV2Input.md) |  | [optional] [default to const []]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


