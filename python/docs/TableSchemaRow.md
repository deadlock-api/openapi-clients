# TableSchemaRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from deadlock_api_client.models.table_schema_row import TableSchemaRow

# TODO update the JSON string below
json = "{}"
# create an instance of TableSchemaRow from a JSON string
table_schema_row_instance = TableSchemaRow.from_json(json)
# print the JSON string representation of the object
print(TableSchemaRow.to_json())

# convert the object into a dict
table_schema_row_dict = table_schema_row_instance.to_dict()
# create an instance of TableSchemaRow from a dict
table_schema_row_from_dict = TableSchemaRow.from_dict(table_schema_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


