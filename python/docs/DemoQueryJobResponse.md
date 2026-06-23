# DemoQueryJobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Stable id of the job; poll &#x60;/demo/query/{job_id}&#x60; for status and the result URL. | 
**status** | [**JobStatus**](JobStatus.md) |  | 

## Example

```python
from deadlock_api_client.models.demo_query_job_response import DemoQueryJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DemoQueryJobResponse from a JSON string
demo_query_job_response_instance = DemoQueryJobResponse.from_json(json)
# print the JSON string representation of the object
print(DemoQueryJobResponse.to_json())

# convert the object into a dict
demo_query_job_response_dict = demo_query_job_response_instance.to_dict()
# create an instance of DemoQueryJobResponse from a dict
demo_query_job_response_from_dict = DemoQueryJobResponse.from_dict(demo_query_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


