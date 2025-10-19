# assets-deadlock-api-client.model.AbilityV2Input

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
**properties** | [**Map<String, ItemPropertyV2Input>**](ItemPropertyV2Input.md) |  | [optional] [default to const {}]
**weaponInfo** | [**RawItemWeaponInfoV2Input**](RawItemWeaponInfoV2Input.md) |  | [optional] 
**type** | **String** |  | [optional] [default to 'ability']
**behaviours** | **List<String>** |  | [optional] [default to const []]
**description** | [**AbilityDescriptionV2**](AbilityDescriptionV2.md) |  | 
**tooltipDetails** | [**AbilityTooltipDetailsV2Input**](AbilityTooltipDetailsV2Input.md) |  | [optional] 
**upgrades** | [**List<RawAbilityUpgradeV2Input>**](RawAbilityUpgradeV2Input.md) |  | [optional] [default to const []]
**abilityType** | [**AbilityTypeV2**](AbilityTypeV2.md) |  | [optional] 
**bossDamageScale** | **num** |  | [optional] 
**dependantAbilities** | **List<String>** |  | [optional] [default to const []]
**videos** | [**AbilityVideosV2**](AbilityVideosV2.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


