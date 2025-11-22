# ExpirationDuration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **float** |  | [optional] 
**per_minute_after_start** | **float** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.expiration_duration import ExpirationDuration

# TODO update the JSON string below
json = "{}"
# create an instance of ExpirationDuration from a JSON string
expiration_duration_instance = ExpirationDuration.from_json(json)
# print the JSON string representation of the object
print(ExpirationDuration.to_json())

# convert the object into a dict
expiration_duration_dict = expiration_duration_instance.to_dict()
# create an instance of ExpirationDuration from a dict
expiration_duration_from_dict = ExpirationDuration.from_dict(expiration_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


