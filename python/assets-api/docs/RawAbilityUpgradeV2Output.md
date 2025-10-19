# RawAbilityUpgradeV2Output


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_upgrades** | [**List[RawAbilityUpgradePropertyUpgradeV2Output]**](RawAbilityUpgradePropertyUpgradeV2Output.md) |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.raw_ability_upgrade_v2_output import RawAbilityUpgradeV2Output

# TODO update the JSON string below
json = "{}"
# create an instance of RawAbilityUpgradeV2Output from a JSON string
raw_ability_upgrade_v2_output_instance = RawAbilityUpgradeV2Output.from_json(json)
# print the JSON string representation of the object
print(RawAbilityUpgradeV2Output.to_json())

# convert the object into a dict
raw_ability_upgrade_v2_output_dict = raw_ability_upgrade_v2_output_instance.to_dict()
# create an instance of RawAbilityUpgradeV2Output from a dict
raw_ability_upgrade_v2_output_from_dict = RawAbilityUpgradeV2Output.from_dict(raw_ability_upgrade_v2_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


