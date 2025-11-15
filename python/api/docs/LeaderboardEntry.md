# LeaderboardEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** | The account name of the player. | [optional] 
**badge_level** | **int** | The badge level of the player (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**possible_account_ids** | **List[int]** | The possible account IDs of the player. **CAVEAT: This is not always correct, as Steam account names are not unique.** | [optional] 
**rank** | **int** | The rank of the player (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**ranked_rank** | **int** | The ranked rank of the player. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**ranked_subrank** | **int** | The ranked subrank of the player. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**top_hero_ids** | **List[int]** | The top hero IDs of the player. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] 

## Example

```python
from deadlock-api-client.models.leaderboard_entry import LeaderboardEntry

# TODO update the JSON string below
json = "{}"
# create an instance of LeaderboardEntry from a JSON string
leaderboard_entry_instance = LeaderboardEntry.from_json(json)
# print the JSON string representation of the object
print(LeaderboardEntry.to_json())

# convert the object into a dict
leaderboard_entry_dict = leaderboard_entry_instance.to_dict()
# create an instance of LeaderboardEntry from a dict
leaderboard_entry_from_dict = LeaderboardEntry.from_dict(leaderboard_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


