
# AbilityV2

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **id** | **kotlin.Int** |  |  |
| **className** | **kotlin.String** |  |  |
| **name** | **kotlin.String** |  |  |
| **description** | [**AbilityDescriptionV2**](AbilityDescriptionV2.md) |  |  |
| **startTrained** | **kotlin.Boolean** |  |  [optional] |
| **image** | **kotlin.String** |  |  [optional] |
| **imageWebp** | **kotlin.String** |  |  [optional] |
| **hero** | **kotlin.Int** |  |  [optional] |
| **heroes** | **kotlin.collections.List&lt;kotlin.Int&gt;** |  |  [optional] |
| **updateTime** | **kotlin.Int** |  |  [optional] |
| **properties** | [**kotlin.collections.Map&lt;kotlin.String, ItemPropertyV2&gt;**](ItemPropertyV2.md) |  |  [optional] |
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
| **dependentAbilities** | [**kotlin.collections.Map&lt;kotlin.String, DependantAbilities&gt;**](DependantAbilities.md) |  |  [optional] |


<a id="Type"></a>
## Enum: type
| Name | Value |
| ---- | ----- |
| type | ability |



