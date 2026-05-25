# Accolade


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **str** |  | 
**description** | **str** |  | 
**enabled_game_modes** | **List[str]** |  | [optional] 
**flavor_name** | **str** |  | 
**id** | **int** |  | 
**threshold_type** | **str** |  | 
**tracked_stat_name** | **str** |  | 

## Example

```python
from deadlock_api_client.models.accolade import Accolade

# TODO update the JSON string below
json = "{}"
# create an instance of Accolade from a JSON string
accolade_instance = Accolade.from_json(json)
# print the JSON string representation of the object
print(Accolade.to_json())

# convert the object into a dict
accolade_dict = accolade_instance.to_dict()
# create an instance of Accolade from a dict
accolade_from_dict = Accolade.from_dict(accolade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


