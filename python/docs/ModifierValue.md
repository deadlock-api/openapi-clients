# ModifierValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
**value_max** | **float** |  | [optional] 
**value_min** | **float** |  | [optional] 
**value_type** | **str** |  | [optional] 

## Example

```python
from deadlock_api_client.models.modifier_value import ModifierValue

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


