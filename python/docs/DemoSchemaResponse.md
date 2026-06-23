# DemoSchemaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**demo_url** | **str** |  | 
**match_id** | **int** |  | 
**tables** | [**List[TableSchemaResponse]**](TableSchemaResponse.md) |  | 

## Example

```python
from deadlock_api_client.models.demo_schema_response import DemoSchemaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DemoSchemaResponse from a JSON string
demo_schema_response_instance = DemoSchemaResponse.from_json(json)
# print the JSON string representation of the object
print(DemoSchemaResponse.to_json())

# convert the object into a dict
demo_schema_response_dict = demo_schema_response_instance.to_dict()
# create an instance of DemoSchemaResponse from a dict
demo_schema_response_from_dict = DemoSchemaResponse.from_dict(demo_schema_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


