# SpreadPenalty

Source data emits spread penalties as either a list of floats or a string (sometimes a comma-separated list, sometimes a literal label).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from deadlock_api_client.models.spread_penalty import SpreadPenalty

# TODO update the JSON string below
json = "{}"
# create an instance of SpreadPenalty from a JSON string
spread_penalty_instance = SpreadPenalty.from_json(json)
# print the JSON string representation of the object
print(SpreadPenalty.to_json())

# convert the object into a dict
spread_penalty_dict = spread_penalty_instance.to_dict()
# create an instance of SpreadPenalty from a dict
spread_penalty_from_dict = SpreadPenalty.from_dict(spread_penalty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


