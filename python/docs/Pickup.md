# Pickup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickup_name** | **str** |  | [optional] 
**pickup_weight** | **float** |  | [optional] 

## Example

```python
from deadlock_api_client.models.pickup import Pickup

# TODO update the JSON string below
json = "{}"
# create an instance of Pickup from a JSON string
pickup_instance = Pickup.from_json(json)
# print the JSON string representation of the object
print(Pickup.to_json())

# convert the object into a dict
pickup_dict = pickup_instance.to_dict()
# create an instance of Pickup from a dict
pickup_from_dict = Pickup.from_dict(pickup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


