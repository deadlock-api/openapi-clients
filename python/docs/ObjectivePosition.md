# ObjectivePosition

A position on the minimap, as fractions of its width/height.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_relative** | **float** |  | 
**top_relative** | **float** |  | 

## Example

```python
from deadlock_api_client.models.objective_position import ObjectivePosition

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectivePosition from a JSON string
objective_position_instance = ObjectivePosition.from_json(json)
# print the JSON string representation of the object
print(ObjectivePosition.to_json())

# convert the object into a dict
objective_position_dict = objective_position_instance.to_dict()
# create an instance of ObjectivePosition from a dict
objective_position_from_dict = ObjectivePosition.from_dict(objective_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


