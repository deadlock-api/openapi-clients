
# UpgradeV2Output

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **id** | **kotlin.Int** |  |  |
| **className** | **kotlin.String** |  |  |
| **name** | **kotlin.String** |  |  |
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
| **properties** | [**kotlin.collections.Map&lt;kotlin.String, UpgradePropertyV2Output&gt;**](UpgradePropertyV2Output.md) |  |  [optional] |
| **weaponInfo** | [**RawItemWeaponInfoV2Output**](RawItemWeaponInfoV2Output.md) |  |  [optional] |
| **type** | [**inline**](#Type) |  |  [optional] |
| **shopImage** | **kotlin.String** |  |  [optional] |
| **shopImageWebp** | **kotlin.String** |  |  [optional] |
| **shopImageSmall** | **kotlin.String** |  |  [optional] |
| **shopImageSmallWebp** | **kotlin.String** |  |  [optional] |
| **disabled** | **kotlin.Boolean** |  |  [optional] |
| **description** | [**UpgradeDescriptionV2**](UpgradeDescriptionV2.md) |  |  [optional] |
| **imbue** | [**RawAbilityImbueV2**](RawAbilityImbueV2.md) |  |  [optional] |
| **componentItems** | **kotlin.collections.List&lt;kotlin.String&gt;** |  |  [optional] |
| **tooltipSections** | [**kotlin.collections.List&lt;UpgradeTooltipSectionV2Output&gt;**](UpgradeTooltipSectionV2Output.md) |  |  [optional] |


<a id="Type"></a>
## Enum: type
| Name | Value |
| ---- | ----- |
| type | upgrade |



