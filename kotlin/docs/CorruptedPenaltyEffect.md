
# CorruptedPenaltyEffect

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **bonusPerTier** | **kotlin.collections.List&lt;kotlin.Double&gt;** | Penalty value indexed by item tier (same indexing as &#x60;item_price_per_tier&#x60;; tiers that can&#39;t be corrupted are &#x60;0&#x60;), in display units: distances are meters (source suffix &#x60;m&#x60; stripped), matching &#x60;postfix&#x60;. |  |
| **display** | **kotlin.Boolean** | &#x60;false&#x60; for effects the game applies but doesn&#39;t list in tooltips. |  |
| **modifierValue** | **kotlin.String** | Modifier the penalty applies, e.g. &#x60;MODIFIER_VALUE_COOLDOWN_REDUCTION_PERCENTAGE&#x60;. |  |
| **cssClass** | **kotlin.String** |  |  [optional] |
| **displayType** | **kotlin.String** |  |  [optional] |
| **label** | **kotlin.String** | Localized stat label (from &#x60;loc_token_override&#x60;). |  [optional] |
| **locTokenOverride** | **kotlin.String** |  |  [optional] |
| **postfix** | **kotlin.String** | Localized unit suffix, e.g. &#x60;%&#x60; or &#x60; m&#x60;. |  [optional] |



