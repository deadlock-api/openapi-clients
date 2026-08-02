# RankResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge** | **int** | Rank badge, &#x60;tier * 10 + subrank&#x60;. &#x60;0&#x60; when no recent ranked match reports a rank. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | 
**last_match** | [**LastRankedMatch**](LastRankedMatch.md) | Rank metadata of the ranked match the badge was read from. &#x60;null&#x60; when none of the player&#39;s recent ranked matches reports a rank. | [optional] 
**rank** | **int** | Rank tier, &#x60;0&#x60; when unknown. | 
**subrank** | **int** | Sub-rank within the tier, &#x60;0&#x60; when unknown. | 

## Example

```python
from deadlock_api_client.models.rank_response import RankResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RankResponse from a JSON string
rank_response_instance = RankResponse.from_json(json)
# print the JSON string representation of the object
print(RankResponse.to_json())

# convert the object into a dict
rank_response_dict = rank_response_instance.to_dict()
# create an instance of RankResponse from a dict
rank_response_from_dict = RankResponse.from_dict(rank_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


