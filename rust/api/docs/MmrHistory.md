# MmrHistory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **u32** |  | 
**division** | **u32** | Extracted from the rank the division (rank // 10) | 
**division_tier** | **u32** | Extracted from the rank the division tier (rank % 10) | 
**match_id** | **u64** |  | 
**player_score** | **f64** | Player Score is the index for the rank array (internally used for the rank regression) | 
**rank** | **u32** | The Player Rank (tier = first digits, subtier = last digit). See more: <https://assets.deadlock-api.com/v2/ranks> | 
**start_time** | **u32** | Start time of the match | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


