# RankedSeason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calibration_matches** | **int** |  | 
**class_name** | **str** |  | 
**intervals** | [**List[SeasonInterval]**](SeasonInterval.md) |  | 
**min_hero_unlocks** | **int** |  | 
**min_hero_wins** | **int** |  | 
**min_wins** | **int** |  | 
**name** | **str** |  | 
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


