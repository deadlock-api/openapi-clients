# IngestStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**active** | **bool** | Whether the ingest tool uploaded a salt for this account within the window that was then verified. | 
**last_upload_at** | **int** | Unix timestamp of the most recent verified upload within the window. | [optional] 
**window_days** | **int** | The window, in days, an upload must fall in to count. | 

## Example

```python
from deadlock_api_client.models.ingest_status_response import IngestStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IngestStatusResponse from a JSON string
ingest_status_response_instance = IngestStatusResponse.from_json(json)
# print the JSON string representation of the object
print(IngestStatusResponse.to_json())

# convert the object into a dict
ingest_status_response_dict = ingest_status_response_instance.to_dict()
# create an instance of IngestStatusResponse from a dict
ingest_status_response_from_dict = IngestStatusResponse.from_dict(ingest_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


