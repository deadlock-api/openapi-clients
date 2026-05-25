# SubclassModifierDefinitionSubclass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**always_show_in_ui** | **List[str]** |  | [optional] 
**class_name** | **str** |  | [optional] 
**duration** | **float** |  | [optional] 
**modifier_values** | [**List[ModifierValue]**](ModifierValue.md) |  | [optional] 
**script_values** | [**List[ModifierValue]**](ModifierValue.md) |  | [optional] 
**subclass_name** | **str** |  | [optional] 
**time_max** | **float** |  | [optional] 
**time_min** | **float** |  | [optional] 

## Example

```python
from deadlock_api_client.models.subclass_modifier_definition_subclass import SubclassModifierDefinitionSubclass

# TODO update the JSON string below
json = "{}"
# create an instance of SubclassModifierDefinitionSubclass from a JSON string
subclass_modifier_definition_subclass_instance = SubclassModifierDefinitionSubclass.from_json(json)
# print the JSON string representation of the object
print(SubclassModifierDefinitionSubclass.to_json())

# convert the object into a dict
subclass_modifier_definition_subclass_dict = subclass_modifier_definition_subclass_instance.to_dict()
# create an instance of SubclassModifierDefinitionSubclass from a dict
subclass_modifier_definition_subclass_from_dict = SubclassModifierDefinitionSubclass.from_dict(subclass_modifier_definition_subclass_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


