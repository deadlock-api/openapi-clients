# SubclassModifierDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subclass** | [**ModifierDefinition**](ModifierDefinition.md) |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.subclass_modifier_definition import SubclassModifierDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of SubclassModifierDefinition from a JSON string
subclass_modifier_definition_instance = SubclassModifierDefinition.from_json(json)
# print the JSON string representation of the object
print(SubclassModifierDefinition.to_json())

# convert the object into a dict
subclass_modifier_definition_dict = subclass_modifier_definition_instance.to_dict()
# create an instance of SubclassModifierDefinition from a dict
subclass_modifier_definition_from_dict = SubclassModifierDefinition.from_dict(subclass_modifier_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


