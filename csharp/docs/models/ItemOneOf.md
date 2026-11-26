# DeadlockApiClient.Model.ItemOneOf

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClassName** | **string** |  | 
**Description** | [**AbilityDescription**](AbilityDescription.md) |  | 
**Id** | **long** |  | 
**Name** | **string** |  | 
**Type** | **string** |  | 
**AbilityType** | **AbilityType** |  | [optional] 
**Behaviours** | **List&lt;string&gt;** |  | [optional] 
**BossDamageScale** | **double** |  | [optional] 
**DependantAbilities** | **List&lt;string&gt;** |  | [optional] 
**DependentAbilities** | [**Dictionary&lt;string, DependantAbilities&gt;**](DependantAbilities.md) | Abilities this one depends on. Entries whose ability has no data are left out. | [optional] 
**GrantAmmoOnCast** | **bool** |  | [optional] 
**Hero** | **long** |  | [optional] 
**Heroes** | **List&lt;long&gt;** |  | [optional] 
**Image** | **string** |  | [optional] 
**ImageWebp** | **string** |  | [optional] 
**Properties** | [**Dictionary&lt;string, ItemProperty&gt;**](ItemProperty.md) |  | [optional] 
**StartTrained** | **bool** |  | [optional] 
**TooltipDetails** | [**AbilityTooltipDetails**](AbilityTooltipDetails.md) |  | [optional] 
**UpdateTime** | **long** |  | [optional] 
**Upgrades** | [**List&lt;RawAbilityUpgrade&gt;**](RawAbilityUpgrade.md) |  | [optional] 
**Videos** | [**AbilityVideos**](AbilityVideos.md) |  | [optional] 
**WeaponInfo** | [**RawItemWeaponInfoInner**](RawItemWeaponInfoInner.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

