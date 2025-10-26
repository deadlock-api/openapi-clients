# DataPrivacyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_id_params** | **Dict[str, str]** |  | 
**steam_id** | **int** |  | 

## Example

```python
from deadlock-api-client.models.data_privacy_request import DataPrivacyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataPrivacyRequest from a JSON string
data_privacy_request_instance = DataPrivacyRequest.from_json(json)
# print the JSON string representation of the object
print(DataPrivacyRequest.to_json())

# convert the object into a dict
data_privacy_request_dict = data_privacy_request_instance.to_dict()
# create an instance of DataPrivacyRequest from a dict
data_privacy_request_from_dict = DataPrivacyRequest.from_dict(data_privacy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


