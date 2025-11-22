# PickupRadius


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **float** |  | [optional] 
**per_minute_after_start** | **float** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.pickup_radius import PickupRadius

# TODO update the JSON string below
json = "{}"
# create an instance of PickupRadius from a JSON string
pickup_radius_instance = PickupRadius.from_json(json)
# print the JSON string representation of the object
print(PickupRadius.to_json())

# convert the object into a dict
pickup_radius_dict = pickup_radius_instance.to_dict()
# create an instance of PickupRadius from a dict
pickup_radius_from_dict = PickupRadius.from_dict(pickup_radius_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


