# PlayerMatchHistoryEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abandoned_time_s** | Option<**u32**> |  | [optional]
**account_id** | **u32** |  | 
**brawl_avg_round_time_s** | Option<**u32**> |  | [optional]
**brawl_score_team0** | Option<**u32**> |  | [optional]
**brawl_score_team1** | Option<**u32**> |  | [optional]
**denies** | **u32** |  | 
**game_mode** | **i32** |  | 
**hero_id** | **u32** | See more: <https://api.deadlock-api.com/v1/assets/heroes> | 
**hero_level** | **u32** |  | 
**last_hits** | **u32** |  | 
**match_duration_s** | **u32** |  | 
**match_id** | **u64** |  | 
**match_mode** | **i32** |  | 
**match_result** | **u32** |  | 
**net_worth** | **u32** |  | 
**objectives_mask_team0** | **u32** |  | 
**objectives_mask_team1** | **u32** |  | 
**player_assists** | **u32** |  | 
**player_deaths** | **u32** |  | 
**player_kills** | **u32** |  | 
**player_match_outcome** | **i32** | How the match was scored for the player: 0 = invalid, 1 = win, 2 = loss, 3 = penalized, 4 = penalized party, 5 = not scored. | 
**player_team** | **i32** |  | 
**ranked_calibration_match** | Option<**u32**> | Non-zero if this match counted towards the player's ranked calibration. | [optional]
**ranked_delta** | Option<**i32**> | The ranked progress change the player got from this match. | [optional]
**ranked_display_badge** | Option<**u32**> | The ranked badge shown for the player after the match (tier = first digits, subtier = last digit). See more: <https://api.deadlock-api.com/v1/assets/ranks> | [optional]
**ranked_used_demotion_protection** | Option<**bool**> | Whether the player's demotion protection absorbed a loss in this match. | [optional]
**start_time** | **u32** |  | 
**team_abandoned** | Option<**bool**> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


