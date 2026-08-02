# LastRankedMatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_id** | **u64** |  | 
**player_rank_consumed_demotion_protection** | Option<**bool**> | Whether the match used up one of the player's demotion protection games. | [optional]
**player_rank_desired_progress_change** | Option<**i32**> | Progress change the match was supposed to award, before demotion protection is applied. | [optional]
**player_rank_final_flat_progress** | Option<**u32**> | Rank progress the player ended the match with. | [optional]
**player_rank_initial_calibration_games** | Option<**u32**> | Remaining placement games at the start of the match. | [optional]
**player_rank_initial_demotion_protection_games** | Option<**u32**> | Remaining demotion protection games at the start of the match. | [optional]
**player_rank_initial_display_rank** | **u32** | Rank badge the player entered the match with, `tier * 10 + subrank`. | 
**player_rank_initial_flat_progress** | Option<**u32**> | Rank progress the player entered the match with. | [optional]
**player_rank_initial_win_streak** | Option<**u32**> | Win streak the player entered the match with. | [optional]
**start_time** | **u32** | Match start time as a unix timestamp. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


