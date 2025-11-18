# ModifierValue

Handles items within m_vecModifierValues and m_vecScriptValues. Captures both fixed values (m_value) and ranged values (m_valueMin/Max).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_type** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**value_min** | **float** |  | [optional] 
**value_max** | **float** |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.modifier_value import ModifierValue

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierValue from a JSON string
modifier_value_instance = ModifierValue.from_json(json)
# print the JSON string representation of the object
print(ModifierValue.to_json())

# convert the object into a dict
modifier_value_dict = modifier_value_instance.to_dict()
# create an instance of ModifierValue from a dict
modifier_value_from_dict = ModifierValue.from_dict(modifier_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


