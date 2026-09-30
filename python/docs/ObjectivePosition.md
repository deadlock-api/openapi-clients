# ObjectivePosition

The top-left corner of an objective marker on the minimap, as fractions of its width/height (like a CSS `margin-left`/`margin-top`). The marker is a `Core` (30% x 8%) for the cores and an `Icon` (10% x 10%) otherwise, so its centre is this position plus half that size. Unlike `neutral_camps`, whose `left_relative`/`top_relative` are the point itself. Before build 6711 these are the HUD's schematic layout; from 6711 on they are real map positions.

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


