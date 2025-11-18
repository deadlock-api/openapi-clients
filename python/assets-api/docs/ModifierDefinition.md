# ModifierDefinition

Schema for the m_sModifer block (note the typo in the source key 'Modifer').

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **str** |  | [optional] 
**subclass_name** | **str** |  | [optional] 
**duration** | **float** |  | [optional] 
**time_min** | **float** |  | [optional] 
**time_max** | **float** |  | [optional] 
**debuff_type** | **str** |  | [optional] 
**always_show_in_ui** | **List[str]** |  | [optional] 
**modifier_values** | [**List[ModifierValue]**](ModifierValue.md) |  | [optional] 
**script_values** | [**List[ModifierValue]**](ModifierValue.md) |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.modifier_definition import ModifierDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierDefinition from a JSON string
modifier_definition_instance = ModifierDefinition.from_json(json)
# print the JSON string representation of the object
print(ModifierDefinition.to_json())

# convert the object into a dict
modifier_definition_dict = modifier_definition_instance.to_dict()
# create an instance of ModifierDefinition from a dict
modifier_definition_from_dict = ModifierDefinition.from_dict(modifier_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


