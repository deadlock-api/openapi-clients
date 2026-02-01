# AssetsDeadlockApiClient.Model.UpgradeV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int** |  | 
**ClassName** | **string** |  | 
**Name** | **string** |  | 
**ItemSlotType** | **ItemSlotTypeV2** |  | 
**ItemTier** | **ItemTierV2** |  | 
**Activation** | **RawAbilityActivationV2** |  | 
**IsActiveItem** | **bool** |  | [readonly] 
**Shopable** | **bool** |  | [readonly] 
**StartTrained** | **bool** |  | [optional] 
**Image** | **string** |  | [optional] 
**ImageWebp** | **string** |  | [optional] 
**Hero** | **int** |  | [optional] 
**Heroes** | **List&lt;int&gt;** |  | [optional] 
**UpdateTime** | **int** |  | [optional] 
**Properties** | [**Dictionary&lt;string, UpgradePropertyV2&gt;**](UpgradePropertyV2.md) |  | [optional] 
**WeaponInfo** | [**RawItemWeaponInfoV2**](RawItemWeaponInfoV2.md) |  | [optional] 
**Type** | **string** |  | [optional] [default to TypeEnum.Upgrade]
**ShopImage** | **string** |  | [optional] 
**ShopImageWebp** | **string** |  | [optional] 
**ShopImageSmall** | **string** |  | [optional] 
**ShopImageSmallWebp** | **string** |  | [optional] 
**Disabled** | **bool** |  | [optional] 
**Description** | [**UpgradeDescriptionV2**](UpgradeDescriptionV2.md) |  | [optional] 
**Imbue** | **RawAbilityImbueV2** |  | [optional] 
**ComponentItems** | **List&lt;string&gt;** |  | [optional] 
**TooltipSections** | [**List&lt;UpgradeTooltipSectionV2&gt;**](UpgradeTooltipSectionV2.md) |  | [optional] 
**Upgrades** | [**List&lt;RawAbilityUpgradeV2&gt;**](RawAbilityUpgradeV2.md) |  | [optional] 
**Cost** | **int** |  | [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

