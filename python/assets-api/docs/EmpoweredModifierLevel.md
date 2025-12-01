# EmpoweredModifierLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_health** | **int** |  | [optional] 
**transition_duration** | **float** |  | [optional] 
**model_scale** | **float** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.empowered_modifier_level import EmpoweredModifierLevel

# TODO update the JSON string below
json = "{}"
# create an instance of EmpoweredModifierLevel from a JSON string
empowered_modifier_level_instance = EmpoweredModifierLevel.from_json(json)
# print the JSON string representation of the object
print(EmpoweredModifierLevel.to_json())

# convert the object into a dict
empowered_modifier_level_dict = empowered_modifier_level_instance.to_dict()
# create an instance of EmpoweredModifierLevel from a dict
empowered_modifier_level_from_dict = EmpoweredModifierLevel.from_dict(empowered_modifier_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


