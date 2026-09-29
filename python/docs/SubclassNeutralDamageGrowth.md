# SubclassNeutralDamageGrowth

Serializes back as `{\"subclass\": ...}` to preserve the KV3 wrapper shape in JSON output.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subclass** | [**SubclassNeutralDamageGrowthSubclass**](SubclassNeutralDamageGrowthSubclass.md) |  | 

## Example

```python
from deadlock_api_client.models.subclass_neutral_damage_growth import SubclassNeutralDamageGrowth

# TODO update the JSON string below
json = "{}"
# create an instance of SubclassNeutralDamageGrowth from a JSON string
subclass_neutral_damage_growth_instance = SubclassNeutralDamageGrowth.from_json(json)
# print the JSON string representation of the object
print(SubclassNeutralDamageGrowth.to_json())

# convert the object into a dict
subclass_neutral_damage_growth_dict = subclass_neutral_damage_growth_instance.to_dict()
# create an instance of SubclassNeutralDamageGrowth from a dict
subclass_neutral_damage_growth_from_dict = SubclassNeutralDamageGrowth.from_dict(subclass_neutral_damage_growth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


