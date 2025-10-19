
# AbilityV2Input

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
| **properties** | [**kotlin.collections.Map&lt;kotlin.String, ItemPropertyV2Input&gt;**](ItemPropertyV2Input.md) |  |  [optional] |
| **weaponInfo** | [**RawItemWeaponInfoV2Input**](RawItemWeaponInfoV2Input.md) |  |  [optional] |
| **type** | [**inline**](#Type) |  |  [optional] |
| **behaviours** | **kotlin.collections.List&lt;kotlin.String&gt;** |  |  [optional] |
| **tooltipDetails** | [**AbilityTooltipDetailsV2Input**](AbilityTooltipDetailsV2Input.md) |  |  [optional] |
| **upgrades** | [**kotlin.collections.List&lt;RawAbilityUpgradeV2Input&gt;**](RawAbilityUpgradeV2Input.md) |  |  [optional] |
| **abilityType** | [**AbilityTypeV2**](AbilityTypeV2.md) |  |  [optional] |
| **bossDamageScale** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **dependantAbilities** | **kotlin.collections.List&lt;kotlin.String&gt;** |  |  [optional] |
| **videos** | [**AbilityVideosV2**](AbilityVideosV2.md) |  |  [optional] |


<a id="Type"></a>
## Enum: type
| Name | Value |
| ---- | ----- |
| type | ability |



