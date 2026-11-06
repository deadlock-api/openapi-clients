# RankedSeason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_win_loss_point_grant** | **int** | Base rank points granted per win / taken per loss (build 6701+). | [optional] 
**calibration_matches** | **int** |  | 
**calibration_max_rank** | **int** | Highest rank badge (tier * 10 + subrank) placements put a player at (build 6857+). Valve&#39;s notes for Beta Season 2 (101, Ascendant I) allow up to Ascendant III for strong previous-season performance. | [optional] 
**class_name** | **str** |  | 
**intervals** | [**List[SeasonInterval]**](SeasonInterval.md) |  | 
**min_hero_unlock_points** | **int** | Points a hero needs to count towards &#x60;min_hero_unlocks&#x60;: 2 per win, 1 per loss (build 6857+). | [optional] 
**min_hero_unlocks** | **int** |  | 
**min_hero_wins** | **int** | Wins a hero needs to count towards &#x60;min_hero_unlocks&#x60;. Absent where the season counts hero points instead, see &#x60;min_hero_unlock_points&#x60;. | [optional] 
**min_wins** | **int** |  | 
**name** | **str** |  | 
**rank_info** | [**List[RankInfo]**](RankInfo.md) | Rank progression settings (build 6857+). | [optional] 
**ranked_type** | **str** |  | 
**valid_party_sizes** | **List[int]** |  | 

## Example

```python
from deadlock_api_client.models.ranked_season import RankedSeason

# TODO update the JSON string below
json = "{}"
# create an instance of RankedSeason from a JSON string
ranked_season_instance = RankedSeason.from_json(json)
# print the JSON string representation of the object
print(RankedSeason.to_json())

# convert the object into a dict
ranked_season_dict = ranked_season_instance.to_dict()
# create an instance of RankedSeason from a dict
ranked_season_from_dict = RankedSeason.from_dict(ranked_season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


