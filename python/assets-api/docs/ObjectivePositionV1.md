# ObjectivePositionV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_relative** | **float** | The relative margin left of the map image. | 
**top_relative** | **float** | The relative margin top of the map image. | 

## Example

```python
from assets_deadlock_api_client.models.objective_position_v1 import ObjectivePositionV1

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectivePositionV1 from a JSON string
objective_position_v1_instance = ObjectivePositionV1.from_json(json)
# print the JSON string representation of the object
print(ObjectivePositionV1.to_json())

# convert the object into a dict
objective_position_v1_dict = objective_position_v1_instance.to_dict()
# create an instance of ObjectivePositionV1 from a dict
objective_position_v1_from_dict = ObjectivePositionV1.from_dict(objective_position_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


