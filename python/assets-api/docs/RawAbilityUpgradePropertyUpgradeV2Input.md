# RawAbilityUpgradePropertyUpgradeV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_str_property_name** | **str** |  | 
**m_str_bonus** | [**MStrbonus**](MStrbonus.md) |  | 
**m_e_scale_stat_filter** | **str** |  | [optional] 
**m_e_upgrade_type** | **str** |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.raw_ability_upgrade_property_upgrade_v2_input import RawAbilityUpgradePropertyUpgradeV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of RawAbilityUpgradePropertyUpgradeV2Input from a JSON string
raw_ability_upgrade_property_upgrade_v2_input_instance = RawAbilityUpgradePropertyUpgradeV2Input.from_json(json)
# print the JSON string representation of the object
print(RawAbilityUpgradePropertyUpgradeV2Input.to_json())

# convert the object into a dict
raw_ability_upgrade_property_upgrade_v2_input_dict = raw_ability_upgrade_property_upgrade_v2_input_instance.to_dict()
# create an instance of RawAbilityUpgradePropertyUpgradeV2Input from a dict
raw_ability_upgrade_property_upgrade_v2_input_from_dict = RawAbilityUpgradePropertyUpgradeV2Input.from_dict(raw_ability_upgrade_property_upgrade_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


