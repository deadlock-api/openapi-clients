# TeamModels

Published pose GLBs (see `NpcUnit::models`) of a per-team model pair.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amber** | **Dict[str, str]** |  | [optional] 
**sapphire** | **Dict[str, str]** |  | [optional] 

## Example

```python
from deadlock_api_client.models.team_models import TeamModels

# TODO update the JSON string below
json = "{}"
# create an instance of TeamModels from a JSON string
team_models_instance = TeamModels.from_json(json)
# print the JSON string representation of the object
print(TeamModels.to_json())

# convert the object into a dict
team_models_dict = team_models_instance.to_dict()
# create an instance of TeamModels from a dict
team_models_from_dict = TeamModels.from_dict(team_models_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


