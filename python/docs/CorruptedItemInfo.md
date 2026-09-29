# CorruptedItemInfo

Broker (\"City Never Sleeps\", build 6711+) corruption data of an upgrade.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_penalties** | **List[str]** | Names of corrupted penalty definitions (&#x60;generic_data&#x60;) that can never roll on this item. | 
**property_upgrades** | [**List[RawAbilityUpgradePropertyUpgrade]**](RawAbilityUpgradePropertyUpgrade.md) | Property bonuses the corrupted variant gains. | 

## Example

```python
from deadlock_api_client.models.corrupted_item_info import CorruptedItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CorruptedItemInfo from a JSON string
corrupted_item_info_instance = CorruptedItemInfo.from_json(json)
# print the JSON string representation of the object
print(CorruptedItemInfo.to_json())

# convert the object into a dict
corrupted_item_info_dict = corrupted_item_info_instance.to_dict()
# create an instance of CorruptedItemInfo from a dict
corrupted_item_info_from_dict = CorruptedItemInfo.from_dict(corrupted_item_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


