# ScriptValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modifier_value** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.script_values import ScriptValues

# TODO update the JSON string below
json = "{}"
# create an instance of ScriptValues from a JSON string
script_values_instance = ScriptValues.from_json(json)
# print the JSON string representation of the object
print(ScriptValues.to_json())

# convert the object into a dict
script_values_dict = script_values_instance.to_dict()
# create an instance of ScriptValues from a dict
script_values_from_dict = ScriptValues.from_dict(script_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


