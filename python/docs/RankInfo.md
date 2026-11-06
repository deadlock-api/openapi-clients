# RankInfo

One `m_vecRankInfo` entry of the game file (build 6857+), as listed there.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge_shields** | **int** | Losses a player at a badge&#39;s first subrank with 0 rank points can take before dropping a badge (rank loss protection shields). | [optional] 
**rank_end** | **int** | Rank badge (tier * 10 + subrank) the entry stops at: it covers the ranks below it. In Beta Season 2, 91 (Phantom I) gives every rank below Phantom shields and Phantom and up none. | [optional] 
**sub_rank_shields** | **int** | Losses a player can take before dropping a subrank (rank loss protection shields). | [optional] 
**sub_rank_xp** | **List[int]** | Rank points needed per subrank step, the last one being the step to the next badge (Beta Season 2: 1000 between subranks, 1500 from the final subrank). | [optional] 

## Example

```python
from deadlock_api_client.models.rank_info import RankInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RankInfo from a JSON string
rank_info_instance = RankInfo.from_json(json)
# print the JSON string representation of the object
print(RankInfo.to_json())

# convert the object into a dict
rank_info_dict = rank_info_instance.to_dict()
# create an instance of RankInfo from a dict
rank_info_from_dict = RankInfo.from_dict(rank_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


