# SubclassObjectiveRegenSubclass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**out_of_combat_health_regen** | **float** |  | [optional] 
**out_of_combat_regen_delay** | **float** |  | [optional] 

## Example

```python
from deadlock_api_client.models.subclass_objective_regen_subclass import SubclassObjectiveRegenSubclass

# TODO update the JSON string below
json = "{}"
# create an instance of SubclassObjectiveRegenSubclass from a JSON string
subclass_objective_regen_subclass_instance = SubclassObjectiveRegenSubclass.from_json(json)
# print the JSON string representation of the object
print(SubclassObjectiveRegenSubclass.to_json())

# convert the object into a dict
subclass_objective_regen_subclass_dict = subclass_objective_regen_subclass_instance.to_dict()
# create an instance of SubclassObjectiveRegenSubclass from a dict
subclass_objective_regen_subclass_from_dict = SubclassObjectiveRegenSubclass.from_dict(subclass_objective_regen_subclass_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


