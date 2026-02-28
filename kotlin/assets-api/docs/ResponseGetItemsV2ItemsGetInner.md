
# ResponseGetItemsV2ItemsGetInner

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **id** | **kotlin.Int** |  |  |
| **className** | **kotlin.String** |  |  |
| **name** | **kotlin.String** |  |  |
| **description** | [**UpgradeDescriptionV2**](UpgradeDescriptionV2.md) |  |  |
| **itemSlotType** | [**ItemSlotTypeV2**](ItemSlotTypeV2.md) |  |  |
| **itemTier** | [**ItemTierV2**](ItemTierV2.md) |  |  |
| **activation** | [**RawAbilityActivationV2**](RawAbilityActivationV2.md) |  |  |
| **isActiveItem** | **kotlin.Boolean** |  |  [readonly] |
| **shopable** | **kotlin.Boolean** |  |  [readonly] |
| **cost** | **kotlin.Int** |  |  [readonly] |
| **startTrained** | **kotlin.Boolean** |  |  [optional] |
| **image** | **kotlin.String** |  |  [optional] |
| **imageWebp** | **kotlin.String** |  |  [optional] |
| **hero** | **kotlin.Int** |  |  [optional] |
| **heroes** | **kotlin.collections.List&lt;kotlin.Int&gt;** |  |  [optional] |
| **updateTime** | **kotlin.Int** |  |  [optional] |
| **properties** | [**kotlin.collections.Map&lt;kotlin.String, UpgradePropertyV2&gt;**](UpgradePropertyV2.md) |  |  [optional] |
| **weaponInfo** | [**RawItemWeaponInfoV2**](RawItemWeaponInfoV2.md) |  |  [optional] |
| **type** | [**inline**](#Type) |  |  [optional] |
| **grantAmmoOnCast** | **kotlin.Boolean** |  |  [optional] |
| **behaviours** | **kotlin.collections.List&lt;kotlin.String&gt;** |  |  [optional] |
| **tooltipDetails** | [**AbilityTooltipDetailsV2**](AbilityTooltipDetailsV2.md) |  |  [optional] |
| **upgrades** | [**kotlin.collections.List&lt;RawAbilityUpgradeV2&gt;**](RawAbilityUpgradeV2.md) |  |  [optional] |
| **abilityType** | [**AbilityTypeV2**](AbilityTypeV2.md) |  |  [optional] |
| **bossDamageScale** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **dependantAbilities** | **kotlin.collections.List&lt;kotlin.String&gt;** |  |  [optional] |
| **videos** | [**AbilityVideosV2**](AbilityVideosV2.md) |  |  [optional] |
| **dependentAbilities** | [**kotlin.collections.Map&lt;kotlin.String, AbilityV2DependentAbilitiesValue&gt;**](AbilityV2DependentAbilitiesValue.md) |  |  [optional] |
| **shopImage** | **kotlin.String** |  |  [optional] |
| **shopImageWebp** | **kotlin.String** |  |  [optional] |
| **shopImageSmall** | **kotlin.String** |  |  [optional] |
| **shopImageSmallWebp** | **kotlin.String** |  |  [optional] |
| **disabled** | **kotlin.Boolean** |  |  [optional] |
| **imbue** | [**RawAbilityImbueV2**](RawAbilityImbueV2.md) |  |  [optional] |
| **componentItems** | **kotlin.collections.List&lt;kotlin.String&gt;** |  |  [optional] |
| **tooltipSections** | [**kotlin.collections.List&lt;UpgradeTooltipSectionV2&gt;**](UpgradeTooltipSectionV2.md) |  |  [optional] |


<a id="Type"></a>
## Enum: type
| Name | Value |
| ---- | ----- |
| type | ability, weapon, upgrade |



