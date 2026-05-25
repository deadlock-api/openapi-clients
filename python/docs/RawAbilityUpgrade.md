# RawAbilityUpgrade


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_upgrades** | [**List[RawAbilityUpgradePropertyUpgrade]**](RawAbilityUpgradePropertyUpgrade.md) |  | [optional] 

## Example

```python
from deadlock_api_client.models.raw_ability_upgrade import RawAbilityUpgrade

# TODO update the JSON string below
json = "{}"
# create an instance of RawAbilityUpgrade from a JSON string
raw_ability_upgrade_instance = RawAbilityUpgrade.from_json(json)
# print the JSON string representation of the object
print(RawAbilityUpgrade.to_json())

# convert the object into a dict
raw_ability_upgrade_dict = raw_ability_upgrade_instance.to_dict()
# create an instance of RawAbilityUpgrade from a dict
raw_ability_upgrade_from_dict = RawAbilityUpgrade.from_dict(raw_ability_upgrade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


