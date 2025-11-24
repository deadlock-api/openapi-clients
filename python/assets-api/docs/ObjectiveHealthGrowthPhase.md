# ObjectiveHealthGrowthPhase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**growth_per_minute** | **int** |  | [optional] 
**tick_rate** | **float** |  | [optional] 
**growth_start_time_in_minutes** | **int** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.objective_health_growth_phase import ObjectiveHealthGrowthPhase

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectiveHealthGrowthPhase from a JSON string
objective_health_growth_phase_instance = ObjectiveHealthGrowthPhase.from_json(json)
# print the JSON string representation of the object
print(ObjectiveHealthGrowthPhase.to_json())

# convert the object into a dict
objective_health_growth_phase_dict = objective_health_growth_phase_instance.to_dict()
# create an instance of ObjectiveHealthGrowthPhase from a dict
objective_health_growth_phase_from_dict = ObjectiveHealthGrowthPhase.from_dict(objective_health_growth_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


