# AbilityDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **str** |  | [optional] 
**desc** | **str** |  | [optional] 
**passive** | **str** |  | [optional] 
**quip** | **str** |  | [optional] 
**t1_desc** | **str** |  | [optional] 
**t2_desc** | **str** |  | [optional] 
**t3_desc** | **str** |  | [optional] 

## Example

```python
from deadlock_api_client.models.ability_description import AbilityDescription

# TODO update the JSON string below
json = "{}"
# create an instance of AbilityDescription from a JSON string
ability_description_instance = AbilityDescription.from_json(json)
# print the JSON string representation of the object
print(AbilityDescription.to_json())

# convert the object into a dict
ability_description_dict = ability_description_instance.to_dict()
# create an instance of AbilityDescription from a dict
ability_description_from_dict = AbilityDescription.from_dict(ability_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


