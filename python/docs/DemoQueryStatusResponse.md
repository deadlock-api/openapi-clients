# DemoQueryStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Failure reason, once &#x60;failed&#x60;. | [optional] 
**estimated_wait_seconds** | **int** | Rough seconds until the result is ready, while &#x60;queued&#x60; or &#x60;running&#x60;. | [optional] 
**format** | [**OutputFormat**](OutputFormat.md) |  | 
**job_id** | **str** |  | 
**match_id** | **int** |  | 
**result_url** | **str** | Public URL of the result artifact, once &#x60;done&#x60;. | [optional] 
**status** | [**JobStatus**](JobStatus.md) |  | 

## Example

```python
from deadlock_api_client.models.demo_query_status_response import DemoQueryStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DemoQueryStatusResponse from a JSON string
demo_query_status_response_instance = DemoQueryStatusResponse.from_json(json)
# print the JSON string representation of the object
print(DemoQueryStatusResponse.to_json())

# convert the object into a dict
demo_query_status_response_dict = demo_query_status_response_instance.to_dict()
# create an instance of DemoQueryStatusResponse from a dict
demo_query_status_response_from_dict = DemoQueryStatusResponse.from_dict(demo_query_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


