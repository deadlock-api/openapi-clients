# ObjectiveRegen


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**out_of_combat_health_regen** | **int** |  | [optional] 
**out_of_combat_regen_delay** | **float** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.objective_regen import ObjectiveRegen

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectiveRegen from a JSON string
objective_regen_instance = ObjectiveRegen.from_json(json)
# print the JSON string representation of the object
print(ObjectiveRegen.to_json())

# convert the object into a dict
objective_regen_dict = objective_regen_instance.to_dict()
# create an instance of ObjectiveRegen from a dict
objective_regen_from_dict = ObjectiveRegen.from_dict(objective_regen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


