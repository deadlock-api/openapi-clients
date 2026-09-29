# DeadlockApiClient.Model.Upgrade

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Activation** | **AbilityActivation** |  | 
**ClassName** | **string** |  | 
**Id** | **int** |  | 
**IsActiveItem** | **bool** |  | 
**ItemSlotType** | **ItemSlotType** |  | 
**ItemTier** | **int** |  | 
**Name** | **string** |  | 
**Shopable** | **bool** |  | 
**Type** | **ItemType** |  | 
**ComponentItems** | **List&lt;string&gt;** |  | [optional] 
**CorruptedInfo** | [**CorruptedItemInfo**](CorruptedItemInfo.md) | Present on upgrades the Broker can corrupt (build 6711+). | [optional] 
**Cost** | **int** |  | [optional] 
**Description** | [**UpgradeDescription**](UpgradeDescription.md) |  | [optional] 
**DisableItemTarget** | **string** |  | [optional] 
**Disabled** | **bool** |  | [optional] 
**DisabledShopFilters** | **List&lt;string&gt;** | Shop filters (&#x60;snake_case&#x60; &#x60;EShopFilter*&#x60; names) this item is hidden from even though its stats would match them. | [optional] 
**Hero** | **int** |  | [optional] 
**Heroes** | **List&lt;int&gt;** |  | [optional] 
**Image** | **string** |  | [optional] 
**ImageWebp** | **string** |  | [optional] 
**Imbue** | **AbilityImbue** |  | [optional] 
**Properties** | [**Dictionary&lt;string, UpgradeProperty&gt;**](UpgradeProperty.md) |  | [optional] 
**ShopFilters** | **List&lt;string&gt;** | Extra shop filters (&#x60;snake_case&#x60; &#x60;EShopFilter*&#x60; names, e.g. &#x60;status_grounded&#x60;) this item shows up under, beyond those derived from its stats. | [optional] 
**ShopImage** | **string** |  | [optional] 
**ShopImageSmall** | **string** |  | [optional] 
**ShopImageSmallWebp** | **string** |  | [optional] 
**ShopImageWebp** | **string** |  | [optional] 
**ShopVersion** | **long** |  | [optional] 
**StartTrained** | **bool** |  | [optional] 
**TooltipSections** | [**List&lt;UpgradeTooltipSection&gt;**](UpgradeTooltipSection.md) |  | [optional] 
**UpdateTime** | **long** |  | [optional] 
**Upgrades** | [**List&lt;RawAbilityUpgrade&gt;**](RawAbilityUpgrade.md) |  | [optional] 
**WeaponInfo** | [**RawItemWeaponInfoInner**](RawItemWeaponInfoInner.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

