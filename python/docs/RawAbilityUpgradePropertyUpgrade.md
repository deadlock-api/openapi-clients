# RawAbilityUpgradePropertyUpgrade


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonus** | **str** |  | 
**name** | **str** |  | 
**scale_stat_filter** | **str** |  | [optional] 
**upgrade_type** | **str** |  | [optional] 

## Example

```python
from deadlock_api_client.models.raw_ability_upgrade_property_upgrade import RawAbilityUpgradePropertyUpgrade

# TODO update the JSON string below
json = "{}"
# create an instance of RawAbilityUpgradePropertyUpgrade from a JSON string
raw_ability_upgrade_property_upgrade_instance = RawAbilityUpgradePropertyUpgrade.from_json(json)
# print the JSON string representation of the object
print(RawAbilityUpgradePropertyUpgrade.to_json())

# convert the object into a dict
raw_ability_upgrade_property_upgrade_dict = raw_ability_upgrade_property_upgrade_instance.to_dict()
# create an instance of RawAbilityUpgradePropertyUpgrade from a dict
raw_ability_upgrade_property_upgrade_from_dict = RawAbilityUpgradePropertyUpgrade.from_dict(raw_ability_upgrade_property_upgrade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


