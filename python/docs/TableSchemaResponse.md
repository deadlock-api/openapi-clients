# TableSchemaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[ColumnSchema]**](ColumnSchema.md) |  | 
**kind** | **str** | &#x60;entity&#x60; for tables discovered from the demo&#39;s send-tables, &#x60;event&#x60; for the event tables common to every demo. | 
**name** | **str** |  | 

## Example

```python
from deadlock_api_client.models.table_schema_response import TableSchemaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableSchemaResponse from a JSON string
table_schema_response_instance = TableSchemaResponse.from_json(json)
# print the JSON string representation of the object
print(TableSchemaResponse.to_json())

# convert the object into a dict
table_schema_response_dict = table_schema_response_instance.to_dict()
# create an instance of TableSchemaResponse from a dict
table_schema_response_from_dict = TableSchemaResponse.from_dict(table_schema_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


