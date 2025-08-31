# CreateCustomResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_secret** | **str** | If a callback url is provided, this is the secret that should be used to verify the callback. The secret is a base64 encoded random string. To verify it you should compare it with the X-Callback-Secret header. If no callback url is provided, this will be None. | [optional] 
**party_code** | **str** |  | 
**party_id** | **str** |  | 

## Example

```python
from openapi_client.models.create_custom_response import CreateCustomResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomResponse from a JSON string
create_custom_response_instance = CreateCustomResponse.from_json(json)
# print the JSON string representation of the object
print(CreateCustomResponse.to_json())

# convert the object into a dict
create_custom_response_dict = create_custom_response_instance.to_dict()
# create an instance of CreateCustomResponse from a dict
create_custom_response_from_dict = CreateCustomResponse.from_dict(create_custom_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


