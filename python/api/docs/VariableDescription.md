# VariableDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**VariableCategory**](VariableCategory.md) | The category of the variable. | 
**default_label** | **str** | The default label for the variable. | [optional] 
**description** | **str** | The description of the variable. | 
**extra_args** | **List[str]** | Extra arguments that can be passed to the variable. | 
**name** | **str** | The name of the variable. | 

## Example

```python
from deadlock_api_client.models.variable_description import VariableDescription

# TODO update the JSON string below
json = "{}"
# create an instance of VariableDescription from a JSON string
variable_description_instance = VariableDescription.from_json(json)
# print the JSON string representation of the object
print(VariableDescription.to_json())

# convert the object into a dict
variable_description_dict = variable_description_instance.to_dict()
# create an instance of VariableDescription from a dict
variable_description_from_dict = VariableDescription.from_dict(variable_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


