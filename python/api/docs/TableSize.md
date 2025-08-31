# TableSize


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_compressed_bytes** | **int** | Compressed size of the table in bytes. | [optional] 
**data_uncompressed_bytes** | **int** | Uncompressed size of the table in bytes. | [optional] 
**is_view** | **bool** | Whether the table is a view. | 
**rows** | **int** | Number of rows in the table. | [optional] 

## Example

```python
from openapi_client.models.table_size import TableSize

# TODO update the JSON string below
json = "{}"
# create an instance of TableSize from a JSON string
table_size_instance = TableSize.from_json(json)
# print the JSON string representation of the object
print(TableSize.to_json())

# convert the object into a dict
table_size_dict = table_size_instance.to_dict()
# create an instance of TableSize from a dict
table_size_from_dict = TableSize.from_dict(table_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


