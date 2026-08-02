# LastRankedMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_id** | **int** |  | 
**player_rank_consumed_demotion_protection** | **bool** | Whether the match used up one of the player&#39;s demotion protection games. | [optional] 
**player_rank_desired_progress_change** | **int** | Progress change the match was supposed to award, before demotion protection is applied. | [optional] 
**player_rank_final_flat_progress** | **int** | Rank progress the player ended the match with. | [optional] 
**player_rank_initial_calibration_games** | **int** | Remaining placement games at the start of the match. | [optional] 
**player_rank_initial_demotion_protection_games** | **int** | Remaining demotion protection games at the start of the match. | [optional] 
**player_rank_initial_display_rank** | **int** | Rank badge the player entered the match with, &#x60;tier * 10 + subrank&#x60;. | 
**player_rank_initial_flat_progress** | **int** | Rank progress the player entered the match with. | [optional] 
**player_rank_initial_win_streak** | **int** | Win streak the player entered the match with. | [optional] 
**start_time** | **int** | Match start time as a unix timestamp. | 

## Example

```python
from deadlock_api_client.models.last_ranked_match import LastRankedMatch

# TODO update the JSON string below
json = "{}"
# create an instance of LastRankedMatch from a JSON string
last_ranked_match_instance = LastRankedMatch.from_json(json)
# print the JSON string representation of the object
print(LastRankedMatch.to_json())

# convert the object into a dict
last_ranked_match_dict = last_ranked_match_instance.to_dict()
# create an instance of LastRankedMatch from a dict
last_ranked_match_from_dict = LastRankedMatch.from_dict(last_ranked_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


