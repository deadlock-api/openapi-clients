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
**rank_interval** | **int** | Ranked interval the match counted for, which sets the scale of the flat progress. See &lt;https://api.deadlock-api.com/v1/assets/ranked-seasons&gt;. &#x60;null&#x60; for matches before 2026-11-05 19:00 UTC, which are all interval 1. | [optional]
**start_time** | **int** | Match start time as a unix timestamp. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
