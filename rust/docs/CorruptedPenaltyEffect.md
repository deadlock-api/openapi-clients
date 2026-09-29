# CorruptedPenaltyEffect

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonus_per_tier** | **Vec<f64>** | Penalty value indexed by item tier (same indexing as `item_price_per_tier`; tiers that can't be corrupted are `0`), in display units: distances are meters (source suffix `m` stripped), matching `postfix`. | 
**css_class** | Option<**String**> |  | [optional]
**display** | **bool** | `false` for effects the game applies but doesn't list in tooltips. | 
**display_type** | Option<**String**> |  | [optional]
**label** | Option<**String**> | Localized stat label (from `loc_token_override`). | [optional]
**loc_token_override** | Option<**String**> |  | [optional]
**modifier_value** | **String** | Modifier the penalty applies, e.g. `MODIFIER_VALUE_COOLDOWN_REDUCTION_PERCENTAGE`. | 
**postfix** | Option<**String**> | Localized unit suffix, e.g. `%` or ` m`. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


