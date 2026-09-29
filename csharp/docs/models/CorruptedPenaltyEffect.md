# DeadlockApiClient.Model.CorruptedPenaltyEffect

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BonusPerTier** | **List&lt;double&gt;** | Penalty value indexed by item tier (same indexing as &#x60;item_price_per_tier&#x60;; tiers that can&#39;t be corrupted are &#x60;0&#x60;), in display units: distances are meters (source suffix &#x60;m&#x60; stripped), matching &#x60;postfix&#x60;. | 
**Display** | **bool** | &#x60;false&#x60; for effects the game applies but doesn&#39;t list in tooltips. | 
**ModifierValue** | **string** | Modifier the penalty applies, e.g. &#x60;MODIFIER_VALUE_COOLDOWN_REDUCTION_PERCENTAGE&#x60;. | 
**CssClass** | **string** |  | [optional] 
**DisplayType** | **string** |  | [optional] 
**Label** | **string** | Localized stat label (from &#x60;loc_token_override&#x60;). | [optional] 
**LocTokenOverride** | **string** |  | [optional] 
**Postfix** | **string** | Localized unit suffix, e.g. &#x60;%&#x60; or &#x60; m&#x60;. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

