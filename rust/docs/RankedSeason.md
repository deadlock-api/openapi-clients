# RankedSeason

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_win_loss_point_grant** | Option<**u32**> | Base rank points granted per win / taken per loss (build 6701+). | [optional]
**calibration_matches** | **u32** |  | 
**calibration_max_rank** | Option<**u32**> | Highest rank badge (tier * 10 + subrank) placements put a player at (build 6857+). Valve's notes for Beta Season 2 (101, Ascendant I) allow up to Ascendant III for strong previous-season performance. | [optional]
**class_name** | **String** |  | 
**intervals** | [**Vec<models::SeasonInterval>**](SeasonInterval.md) |  | 
**min_hero_unlock_points** | Option<**u32**> | Points a hero needs to count towards `min_hero_unlocks`: 2 per win, 1 per loss (build 6857+). | [optional]
**min_hero_unlocks** | **u32** |  | 
**min_hero_wins** | Option<**u32**> | Wins a hero needs to count towards `min_hero_unlocks`. Absent where the season counts hero points instead, see `min_hero_unlock_points`. | [optional]
**min_wins** | **u32** |  | 
**name** | **String** |  | 
**rank_info** | Option<[**Vec<models::RankInfo>**](RankInfo.md)> | Rank progression settings (build 6857+). | [optional]
**ranked_type** | **String** |  | 
**valid_party_sizes** | **Vec<u32>** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


