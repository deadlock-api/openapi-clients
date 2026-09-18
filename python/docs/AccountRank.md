# AccountRank


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge** | **int** | Rank badge, &#x60;tier * 10 + subrank&#x60;, including the progress the last ranked match awarded. Eternus subranks are percentile-based and refreshed daily by Valve, so within Eternus this is the badge the player entered their latest ranked match with. &#x60;0&#x60; when no recent ranked match reports a rank. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | 
**last_match** | [**LastRankedMatch**](LastRankedMatch.md) | Rank metadata of the ranked match the badge was read from. &#x60;null&#x60; when none of the player&#39;s recent ranked matches reports a rank. | [optional] 
**rank** | **int** | Rank tier, &#x60;0&#x60; when unknown. | 
**subrank** | **int** | Sub-rank within the tier, &#x60;0&#x60; when unknown. | 
**account_id** | **int** | The players &#x60;SteamID3&#x60; | 

## Example

```python
from deadlock_api_client.models.account_rank import AccountRank

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRank from a JSON string
account_rank_instance = AccountRank.from_json(json)
# print the JSON string representation of the object
print(AccountRank.to_json())

# convert the object into a dict
account_rank_dict = account_rank_instance.to_dict()
# create an instance of AccountRank from a dict
account_rank_from_dict = AccountRank.from_dict(account_rank_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


