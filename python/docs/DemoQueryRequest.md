# DemoQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | [**OutputFormat**](OutputFormat.md) | Output format of the result artifact. | [optional] 
**match_id** | **int** | Match whose demo to query. | 
**query** | **str** | SQL query to run over the demo&#39;s entity/event tables (see &#x60;/demo/schema&#x60;). | 

## Example

```python
from deadlock_api_client.models.demo_query_request import DemoQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DemoQueryRequest from a JSON string
demo_query_request_instance = DemoQueryRequest.from_json(json)
# print the JSON string representation of the object
print(DemoQueryRequest.to_json())

# convert the object into a dict
demo_query_request_dict = demo_query_request_instance.to_dict()
# create an instance of DemoQueryRequest from a dict
demo_query_request_from_dict = DemoQueryRequest.from_dict(demo_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


