# ClickhouseMatchInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_badge_team0** | **int** | See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**average_badge_team1** | **int** | See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**duration_s** | **int** |  | 
**match_id** | **int** |  | 
**match_mode** | **int** |  | 
**start_time** | **int** |  | 

## Example

```python
from openapi_client.models.clickhouse_match_info import ClickhouseMatchInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClickhouseMatchInfo from a JSON string
clickhouse_match_info_instance = ClickhouseMatchInfo.from_json(json)
# print the JSON string representation of the object
print(ClickhouseMatchInfo.to_json())

# convert the object into a dict
clickhouse_match_info_dict = clickhouse_match_info_instance.to_dict()
# create an instance of ClickhouseMatchInfo from a dict
clickhouse_match_info_from_dict = ClickhouseMatchInfo.from_dict(clickhouse_match_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


