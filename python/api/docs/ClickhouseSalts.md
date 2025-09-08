# ClickhouseSalts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** |  | [optional] 
**match_id** | **int** |  | 
**metadata_salt** | **int** |  | [optional] 
**replay_salt** | **int** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from deadlock-api-client.models.clickhouse_salts import ClickhouseSalts

# TODO update the JSON string below
json = "{}"
# create an instance of ClickhouseSalts from a JSON string
clickhouse_salts_instance = ClickhouseSalts.from_json(json)
# print the JSON string representation of the object
print(ClickhouseSalts.to_json())

# convert the object into a dict
clickhouse_salts_dict = clickhouse_salts_instance.to_dict()
# create an instance of ClickhouseSalts from a dict
clickhouse_salts_from_dict = ClickhouseSalts.from_dict(clickhouse_salts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


