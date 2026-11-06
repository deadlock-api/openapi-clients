# PlayerEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**badge** | **int** | &#x60;rank&#x60; and &#x60;peak_rank&#x60; sorts only: the rank badge the progress in &#x60;value&#x60; falls in, &#x60;0&#x60; when the player has no ranked match in range. Omitted for every other sort. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional] 
**badge_progress** | **int** | &#x60;rank&#x60; and &#x60;peak_rank&#x60; sorts only: progress points into &#x60;badge&#x60;, out of &#x60;badge_progress_max&#x60;. In Eternus, whose subranks are percentile cuts rather than point spans, the points past the start of Eternus. &#x60;null&#x60; when the player has no ranked match in range. | [optional] 
**badge_progress_max** | **int** | &#x60;rank&#x60; and &#x60;peak_rank&#x60; sorts only: the points the subrank of &#x60;badge&#x60; spans in that match&#39;s season (&#x60;sub_rank_xp&#x60; in &lt;https://api.deadlock-api.com/v1/assets/ranked-seasons&gt;). &#x60;null&#x60; in Eternus and when the player has no ranked match in range. | [optional] 
**matches** | **int** |  | 
**rank** | **int** |  | 
**value** | **float** |  | 

## Example

```python
from deadlock_api_client.models.player_entry import PlayerEntry

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerEntry from a JSON string
player_entry_instance = PlayerEntry.from_json(json)
# print the JSON string representation of the object
print(PlayerEntry.to_json())

# convert the object into a dict
player_entry_dict = player_entry_instance.to_dict()
# create an instance of PlayerEntry from a dict
player_entry_from_dict = PlayerEntry.from_dict(player_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


