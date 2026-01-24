# StreetBrawl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**respawn_times** | **List[int]** |  | 
**gold_per_round** | **List[int]** |  | 
**apper_round** | **List[int]** |  | 
**item_draft_rerolls_per_round** | **List[int]** |  | 
**round_length_minutes** | **List[int]** |  | 
**round_length_minutes_urgent** | **List[float]** |  | 
**overtime_respawn_time_increase** | **List[float]** |  | 
**overtime_respawn_time_increase_urgent** | **List[float]** |  | 
**overtime_trooper_health_scale** | **List[float]** |  | 
**overtime_trooper_damage_scale** | **List[float]** |  | 
**buy_time** | **List[int]** |  | 
**pre_buy_time** | **List[float]** |  | 
**score_to_win** | **int** |  | 
**scoring_time** | **float** |  | 
**lane_number** | **int** |  | 
**objective_max_health** | **List[int]** |  | 
**tier2_bonus_health** | **int** |  | 
**comeback_bonus_health** | **int** |  | 
**comeback_bonus_health_critical** | **int** |  | 
**trooper_spawn_timer** | **List[float]** |  | 
**trooper_spawn_before_round_start_timer** | **float** |  | 
**zip_boost_cooldown_on_start** | **float** |  | 
**buy_time_grace_period** | **float** |  | 
**tier1_max_resist_time** | **float** |  | 
**tier2_max_resist_time** | **float** |  | 
**ultimate_unlock_round** | **int** |  | 
**item_draft_rounds_per_game_round** | [**List[ItemDraftRoundPerGameRound]**](ItemDraftRoundPerGameRound.md) |  | 
**outline_color_friend** | **List[int]** |  | [optional] 
**outline_color_enemy** | **List[int]** |  | [optional] 
**outline_color_team1** | **List[int]** |  | [optional] 
**outline_color_team2** | **List[int]** |  | [optional] 
**outline_color_neutral** | **List[int]** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.street_brawl import StreetBrawl

# TODO update the JSON string below
json = "{}"
# create an instance of StreetBrawl from a JSON string
street_brawl_instance = StreetBrawl.from_json(json)
# print the JSON string representation of the object
print(StreetBrawl.to_json())

# convert the object into a dict
street_brawl_dict = street_brawl_instance.to_dict()
# create an instance of StreetBrawl from a dict
street_brawl_from_dict = StreetBrawl.from_dict(street_brawl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


