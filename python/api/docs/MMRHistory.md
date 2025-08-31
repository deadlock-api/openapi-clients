# MMRHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**division** | **int** | Extracted from the rank the division (rank // 10) | 
**division_tier** | **int** | Extracted from the rank the division tier (rank % 10) | 
**match_id** | **int** |  | 
**player_score** | **float** | Player Score is the index for the rank array (internally used for the rank regression) | 
**rank** | **int** | The Player Rank. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
**start_time** | **int** | Start time of the match | 

## Example

```python
from openapi_client.models.mmr_history import MMRHistory

# TODO update the JSON string below
json = "{}"
# create an instance of MMRHistory from a JSON string
mmr_history_instance = MMRHistory.from_json(json)
# print the JSON string representation of the object
print(MMRHistory.to_json())

# convert the object into a dict
mmr_history_dict = mmr_history_instance.to_dict()
# create an instance of MMRHistory from a dict
mmr_history_from_dict = MMRHistory.from_dict(mmr_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


