
# Item

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **className** | **kotlin.String** |  |  |
| **description** | [**UpgradeDescription**](UpgradeDescription.md) |  |  |
| **id** | **kotlin.Int** |  |  |
| **name** | **kotlin.String** |  |  |
| **type** | [**ItemType**](ItemType.md) |  |  |
| **activation** | [**AbilityActivation**](AbilityActivation.md) |  |  |
| **isActiveItem** | **kotlin.Boolean** |  |  |
| **itemSlotType** | [**ItemSlotType**](ItemSlotType.md) |  |  |
| **itemTier** | **kotlin.Int** |  |  |
| **shopable** | **kotlin.Boolean** |  |  |
| **abilityType** | [**AbilityType**](AbilityType.md) |  |  [optional] |
| **behaviours** | **kotlin.collections.List&lt;kotlin.String&gt;** |  |  [optional] |
| **bossDamageScale** | **kotlin.Double** |  |  [optional] |
| **dependantAbilities** | **kotlin.collections.List&lt;kotlin.String&gt;** |  |  [optional] |
| **dependentAbilities** | [**kotlin.collections.Map&lt;kotlin.String, DependantAbilities&gt;**](DependantAbilities.md) |  |  [optional] |
| **grantAmmoOnCast** | **kotlin.Boolean** |  |  [optional] |
| **hero** | **kotlin.Int** |  |  [optional] |
| **heroes** | **kotlin.collections.List&lt;kotlin.Int&gt;** |  |  [optional] |
| **image** | **kotlin.String** |  |  [optional] |
| **imageWebp** | **kotlin.String** |  |  [optional] |
| **properties** | [**kotlin.collections.Map&lt;kotlin.String, UpgradeProperty&gt;**](UpgradeProperty.md) |  |  [optional] |
| **startTrained** | **kotlin.Boolean** |  |  [optional] |
| **tooltipDetails** | [**AbilityTooltipDetails**](AbilityTooltipDetails.md) |  |  [optional] |
| **updateTime** | **kotlin.Long** |  |  [optional] |
| **upgrades** | [**kotlin.collections.List&lt;RawAbilityUpgrade&gt;**](RawAbilityUpgrade.md) |  |  [optional] |
| **videos** | [**AbilityVideos**](AbilityVideos.md) |  |  [optional] |
| **weaponInfo** | [**RawItemWeaponInfoInner**](RawItemWeaponInfoInner.md) |  |  [optional] |
| **crosshairCssClass** | **kotlin.String** |  |  [optional] |
| **customCrosshairSettings** | [**RawCustomCrosshairSettings**](RawCustomCrosshairSettings.md) |  |  [optional] |
| **useCustomCrosshairSettings** | **kotlin.Boolean** |  |  [optional] |
| **componentItems** | **kotlin.collections.List&lt;kotlin.String&gt;** |  |  [optional] |
| **corruptedInfo** | [**CorruptedItemInfo**](CorruptedItemInfo.md) | Present on upgrades the Broker can corrupt (build 6711+). |  [optional] |
| **cost** | **kotlin.Int** |  |  [optional] |
| **disableItemTarget** | **kotlin.String** |  |  [optional] |
| **disabled** | **kotlin.Boolean** |  |  [optional] |
| **disabledShopFilters** | **kotlin.collections.List&lt;kotlin.String&gt;** | Shop filters (&#x60;snake_case&#x60; &#x60;EShopFilter*&#x60; names) this item is hidden from even though its stats would match them. |  [optional] |
| **imbue** | [**AbilityImbue**](AbilityImbue.md) |  |  [optional] |
| **shopFilters** | **kotlin.collections.List&lt;kotlin.String&gt;** | Extra shop filters (&#x60;snake_case&#x60; &#x60;EShopFilter*&#x60; names, e.g. &#x60;status_grounded&#x60;) this item shows up under, beyond those derived from its stats. |  [optional] |
| **shopImage** | **kotlin.String** |  |  [optional] |
| **shopImageSmall** | **kotlin.String** |  |  [optional] |
| **shopImageSmallWebp** | **kotlin.String** |  |  [optional] |
| **shopImageWebp** | **kotlin.String** |  |  [optional] |
| **shopVersion** | **kotlin.Long** |  |  [optional] |
| **tooltipSections** | [**kotlin.collections.List&lt;UpgradeTooltipSection&gt;**](UpgradeTooltipSection.md) |  |  [optional] |



