# SubclassRangedArmorModifier

Serializes back as `{\"subclass\": ...}` to preserve the KV3 wrapper shape in JSON output.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subclass** | [**SubclassRangedArmorModifierSubclass**](SubclassRangedArmorModifierSubclass.md) |  | 

## Example

```python
from deadlock_api_client.models.subclass_ranged_armor_modifier import SubclassRangedArmorModifier

# TODO update the JSON string below
json = "{}"
# create an instance of SubclassRangedArmorModifier from a JSON string
subclass_ranged_armor_modifier_instance = SubclassRangedArmorModifier.from_json(json)
# print the JSON string representation of the object
print(SubclassRangedArmorModifier.to_json())

# convert the object into a dict
subclass_ranged_armor_modifier_dict = subclass_ranged_armor_modifier_instance.to_dict()
# create an instance of SubclassRangedArmorModifier from a dict
subclass_ranged_armor_modifier_from_dict = SubclassRangedArmorModifier.from_dict(subclass_ranged_armor_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


