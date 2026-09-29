# CorruptedPenalty

A penalty that can be rolled onto a corrupted item (build 6711+).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effects** | [**List[CorruptedPenaltyEffect]**](CorruptedPenaltyEffect.md) |  | 
**name** | **str** |  | 
**roll_weight** | **float** |  | [optional] 

## Example

```python
from deadlock_api_client.models.corrupted_penalty import CorruptedPenalty

# TODO update the JSON string below
json = "{}"
# create an instance of CorruptedPenalty from a JSON string
corrupted_penalty_instance = CorruptedPenalty.from_json(json)
# print the JSON string representation of the object
print(CorruptedPenalty.to_json())

# convert the object into a dict
corrupted_penalty_dict = corrupted_penalty_instance.to_dict()
# create an instance of CorruptedPenalty from a dict
corrupted_penalty_from_dict = CorruptedPenalty.from_dict(corrupted_penalty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


