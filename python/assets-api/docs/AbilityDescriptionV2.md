# AbilityDescriptionV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desc** | **str** |  | [optional] 
**quip** | **str** |  | [optional] 
**t1_desc** | **str** |  | [optional] 
**t2_desc** | **str** |  | [optional] 
**t3_desc** | **str** |  | [optional] 
**active** | **str** |  | [optional] 
**passive** | **str** |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.ability_description_v2 import AbilityDescriptionV2

# TODO update the JSON string below
json = "{}"
# create an instance of AbilityDescriptionV2 from a JSON string
ability_description_v2_instance = AbilityDescriptionV2.from_json(json)
# print the JSON string representation of the object
print(AbilityDescriptionV2.to_json())

# convert the object into a dict
ability_description_v2_dict = ability_description_v2_instance.to_dict()
# create an instance of AbilityDescriptionV2 from a dict
ability_description_v2_from_dict = AbilityDescriptionV2.from_dict(ability_description_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


