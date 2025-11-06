# assets-deadlock-api-client.model.HeroV2

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
**description** | [**HeroDescriptionV2**](HeroDescriptionV2.md) |  | 
**recommendedUpgrades** | **List<String>** |  | [optional] [default to const []]
**recommendedAbilityOrder** | **List<String>** |  | [optional] [default to const []]
**playerSelectable** | **bool** |  | 
**disabled** | **bool** |  | 
**inDevelopment** | **bool** |  | 
**needsTesting** | **bool** |  | 
**assignedPlayersOnly** | **bool** |  | 
**tags** | **List<String>** |  | [optional] [default to const []]
**gunTag** | **String** |  | [optional] 
**hideoutRichPresence** | **String** |  | [optional] 
**heroType** | [**HeroTypeV2**](HeroTypeV2.md) |  | [optional] 
**prereleaseOnly** | **bool** |  | [optional] 
**limitedTesting** | **bool** |  | 
**complexity** | **int** |  | 
**skin** | **int** |  | 
**images** | [**HeroImagesV2**](HeroImagesV2.md) |  | 
**items** | **Map<String, String>** |  | [default to const {}]
**startingStats** | [**HeroStartingStatsV2**](HeroStartingStatsV2.md) |  | 
**itemSlotInfo** | [**Map<String, RawHeroItemSlotInfoValueV2>**](RawHeroItemSlotInfoValueV2.md) |  | [default to const {}]
**physics** | [**HeroPhysicsV2**](HeroPhysicsV2.md) |  | 
**colors** | [**HeroColorsV2**](HeroColorsV2.md) |  | 
**shopStatDisplay** | [**HeroShopStatDisplayV2**](HeroShopStatDisplayV2.md) |  | 
**costBonuses** | [**Map<String, List<RawHeroMapModCostBonusesV2>>**](List.md) |  | [optional] [default to const {}]
**statsDisplay** | [**RawHeroStatsDisplayV2**](RawHeroStatsDisplayV2.md) |  | 
**heroStatsUi** | [**RawHeroStatsUIV2**](RawHeroStatsUIV2.md) |  | 
**levelInfo** | [**Map<String, HeroLevelInfoV2>**](HeroLevelInfoV2.md) |  | [default to const {}]
**scalingStats** | [**Map<String, RawHeroScalingStatV2>**](RawHeroScalingStatV2.md) |  | [default to const {}]
**purchaseBonuses** | [**Map<String, List<RawHeroPurchaseBonusV2>>**](List.md) |  | [default to const {}]
**standardLevelUpUpgrades** | **Map<String, num>** |  | [default to const {}]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


