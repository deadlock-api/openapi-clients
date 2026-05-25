# LootTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[LootEntry]**](LootEntry.md) |  | 

## Example

```python
from deadlock_api_client.models.loot_table import LootTable

# TODO update the JSON string below
json = "{}"
# create an instance of LootTable from a JSON string
loot_table_instance = LootTable.from_json(json)
# print the JSON string representation of the object
print(LootTable.to_json())

# convert the object into a dict
loot_table_dict = loot_table_instance.to_dict()
# create an instance of LootTable from a dict
loot_table_from_dict = LootTable.from_dict(loot_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


