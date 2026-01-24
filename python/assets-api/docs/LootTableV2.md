# LootTableV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[LootTableV2Entry]**](LootTableV2Entry.md) |  | 

## Example

```python
from assets_deadlock_api_client.models.loot_table_v2 import LootTableV2

# TODO update the JSON string below
json = "{}"
# create an instance of LootTableV2 from a JSON string
loot_table_v2_instance = LootTableV2.from_json(json)
# print the JSON string representation of the object
print(LootTableV2.to_json())

# convert the object into a dict
loot_table_v2_dict = loot_table_v2_instance.to_dict()
# create an instance of LootTableV2 from a dict
loot_table_v2_from_dict = LootTableV2.from_dict(loot_table_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


