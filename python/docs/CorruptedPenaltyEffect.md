# CorruptedPenaltyEffect


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonus_per_tier** | **List[float]** | Penalty value indexed by item tier (same indexing as &#x60;item_price_per_tier&#x60;; tiers that can&#39;t be corrupted are &#x60;0&#x60;), in display units: distances are meters (source suffix &#x60;m&#x60; stripped), matching &#x60;postfix&#x60;. | 
**css_class** | **str** |  | [optional] 
**display** | **bool** | &#x60;false&#x60; for effects the game applies but doesn&#39;t list in tooltips. | 
**display_type** | **str** |  | [optional] 
**label** | **str** | Localized stat label (from &#x60;loc_token_override&#x60;). | [optional] 
**loc_token_override** | **str** |  | [optional] 
**modifier_value** | **str** | Modifier the penalty applies, e.g. &#x60;MODIFIER_VALUE_COOLDOWN_REDUCTION_PERCENTAGE&#x60;. | 
**postfix** | **str** | Localized unit suffix, e.g. &#x60;%&#x60; or &#x60; m&#x60;. | [optional] 

## Example

```python
from deadlock_api_client.models.corrupted_penalty_effect import CorruptedPenaltyEffect

# TODO update the JSON string below
json = "{}"
# create an instance of CorruptedPenaltyEffect from a JSON string
corrupted_penalty_effect_instance = CorruptedPenaltyEffect.from_json(json)
# print the JSON string representation of the object
print(CorruptedPenaltyEffect.to_json())

# convert the object into a dict
corrupted_penalty_effect_dict = corrupted_penalty_effect_instance.to_dict()
# create an instance of CorruptedPenaltyEffect from a dict
corrupted_penalty_effect_from_dict = CorruptedPenaltyEffect.from_dict(corrupted_penalty_effect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


