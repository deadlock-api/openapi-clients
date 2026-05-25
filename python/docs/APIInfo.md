# APIInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fetched_matches_per_day** | **int** | The number of matches fetched in the last 24 hours. | [optional] 
**table_sizes** | [**Dict[str, TableSize]**](TableSize.md) | The sizes of all tables in the database. | [optional] 
**user_ingested_matches_last24h** | **int** | The number of matches ingested in the last 24 hours. | [optional] 

## Example

```python
from deadlock_api_client.models.api_info import APIInfo

# TODO update the JSON string below
json = "{}"
# create an instance of APIInfo from a JSON string
api_info_instance = APIInfo.from_json(json)
# print the JSON string representation of the object
print(APIInfo.to_json())

# convert the object into a dict
api_info_dict = api_info_instance.to_dict()
# create an instance of APIInfo from a dict
api_info_from_dict = APIInfo.from_dict(api_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


