# PickupDefinition

Schema for items inside m_vecPrimaryPickups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickup_name** | **str** |  | [optional] 
**pickup_weight** | **float** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.pickup_definition import PickupDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of PickupDefinition from a JSON string
pickup_definition_instance = PickupDefinition.from_json(json)
# print the JSON string representation of the object
print(PickupDefinition.to_json())

# convert the object into a dict
pickup_definition_dict = pickup_definition_instance.to_dict()
# create an instance of PickupDefinition from a dict
pickup_definition_from_dict = PickupDefinition.from_dict(pickup_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


