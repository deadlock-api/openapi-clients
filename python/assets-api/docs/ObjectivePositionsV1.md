# ObjectivePositionsV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team0_core** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | 
**team1_core** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | 
**team0_titan** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | 
**team1_titan** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | 
**team0_tier2_1** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | 
**team0_tier2_2** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | [optional] 
**team0_tier2_3** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | 
**team0_tier2_4** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | 
**team1_tier2_1** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | 
**team1_tier2_2** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | [optional] 
**team1_tier2_3** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | 
**team1_tier2_4** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | 
**team0_tier1_1** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | 
**team0_tier1_2** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | [optional] 
**team0_tier1_3** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | 
**team0_tier1_4** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | 
**team1_tier1_1** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | 
**team1_tier1_2** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | [optional] 
**team1_tier1_3** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | 
**team1_tier1_4** | [**ObjectivePositionV1**](ObjectivePositionV1.md) |  | 

## Example

```python
from assets-deadlock-api-client.models.objective_positions_v1 import ObjectivePositionsV1

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectivePositionsV1 from a JSON string
objective_positions_v1_instance = ObjectivePositionsV1.from_json(json)
# print the JSON string representation of the object
print(ObjectivePositionsV1.to_json())

# convert the object into a dict
objective_positions_v1_dict = objective_positions_v1_instance.to_dict()
# create an instance of ObjectivePositionsV1 from a dict
objective_positions_v1_from_dict = ObjectivePositionsV1.from_dict(objective_positions_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


