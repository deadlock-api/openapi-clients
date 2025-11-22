# ObjectiveParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gold_per_orb** | **int** |  | 
**near_player_split_pct** | **float** |  | 
**tier1_gold_kill** | **int** |  | 
**tier1_gold_orbs** | **int** |  | 
**tier2_gold_kill** | **int** |  | 
**tier2_gold_orbs** | **int** |  | 
**base_guardians_gold_kill** | **int** |  | 
**base_guardians_gold_orbs** | **int** |  | 
**shrines_gold_kill** | **int** |  | 
**shrines_gold_orbs** | **int** |  | 
**patron_phase1_gold_kill** | **int** |  | 
**patron_phase1_gold_orbs** | **int** |  | 

## Example

```python
from assets_deadlock_api_client.models.objective_params import ObjectiveParams

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectiveParams from a JSON string
objective_params_instance = ObjectiveParams.from_json(json)
# print the JSON string representation of the object
print(ObjectiveParams.to_json())

# convert the object into a dict
objective_params_dict = objective_params_instance.to_dict()
# create an instance of ObjectiveParams from a dict
objective_params_from_dict = ObjectiveParams.from_dict(objective_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


