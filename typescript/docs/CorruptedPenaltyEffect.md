# CorruptedPenaltyEffect


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonus_per_tier** | **Array&lt;number&gt;** | Penalty value indexed by item tier (same indexing as &#x60;item_price_per_tier&#x60;; tiers that can\&#39;t be corrupted are &#x60;0&#x60;), in display units: distances are meters (source suffix &#x60;m&#x60; stripped), matching &#x60;postfix&#x60;. | [default to undefined]
**css_class** | **string** |  | [optional] [default to undefined]
**display** | **boolean** | &#x60;false&#x60; for effects the game applies but doesn\&#39;t list in tooltips. | [default to undefined]
**display_type** | **string** |  | [optional] [default to undefined]
**label** | **string** | Localized stat label (from &#x60;loc_token_override&#x60;). | [optional] [default to undefined]
**loc_token_override** | **string** |  | [optional] [default to undefined]
**modifier_value** | **string** | Modifier the penalty applies, e.g. &#x60;MODIFIER_VALUE_COOLDOWN_REDUCTION_PERCENTAGE&#x60;. | [default to undefined]
**postfix** | **string** | Localized unit suffix, e.g. &#x60;%&#x60; or &#x60; m&#x60;. | [optional] [default to undefined]

## Example

```typescript
import { CorruptedPenaltyEffect } from 'deadlock_api_client';

const instance: CorruptedPenaltyEffect = {
    bonus_per_tier,
    css_class,
    display,
    display_type,
    label,
    loc_token_override,
    modifier_value,
    postfix,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
