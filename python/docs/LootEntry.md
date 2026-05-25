# LootEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | **str** |  | 

## Example

```python
from deadlock_api_client.models.loot_entry import LootEntry

# TODO update the JSON string below
json = "{}"
# create an instance of LootEntry from a JSON string
loot_entry_instance = LootEntry.from_json(json)
# print the JSON string representation of the object
print(LootEntry.to_json())

# convert the object into a dict
loot_entry_dict = loot_entry_instance.to_dict()
# create an instance of LootEntry from a dict
loot_entry_from_dict = LootEntry.from_dict(loot_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


