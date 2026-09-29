# CorruptedTooltipBackers

Corrupted item tooltip backers, one per item slot type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spirit** | [**ImagePair**](ImagePair.md) |  | 
**vitality** | [**ImagePair**](ImagePair.md) |  | 
**weapon** | [**ImagePair**](ImagePair.md) |  | 

## Example

```python
from deadlock_api_client.models.corrupted_tooltip_backers import CorruptedTooltipBackers

# TODO update the JSON string below
json = "{}"
# create an instance of CorruptedTooltipBackers from a JSON string
corrupted_tooltip_backers_instance = CorruptedTooltipBackers.from_json(json)
# print the JSON string representation of the object
print(CorruptedTooltipBackers.to_json())

# convert the object into a dict
corrupted_tooltip_backers_dict = corrupted_tooltip_backers_instance.to_dict()
# create an instance of CorruptedTooltipBackers from a dict
corrupted_tooltip_backers_from_dict = CorruptedTooltipBackers.from_dict(corrupted_tooltip_backers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


