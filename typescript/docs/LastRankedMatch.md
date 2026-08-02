# LastRankedMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_id** | **number** |  | [default to undefined]
**player_rank_consumed_demotion_protection** | **boolean** | Whether the match used up one of the player\&#39;s demotion protection games. | [optional] [default to undefined]
**player_rank_desired_progress_change** | **number** | Progress change the match was supposed to award, before demotion protection is applied. | [optional] [default to undefined]
**player_rank_final_flat_progress** | **number** | Rank progress the player ended the match with. | [optional] [default to undefined]
**player_rank_initial_calibration_games** | **number** | Remaining placement games at the start of the match. | [optional] [default to undefined]
**player_rank_initial_demotion_protection_games** | **number** | Remaining demotion protection games at the start of the match. | [optional] [default to undefined]
**player_rank_initial_display_rank** | **number** | Rank badge the player entered the match with, &#x60;tier * 10 + subrank&#x60;. | [default to undefined]
**player_rank_initial_flat_progress** | **number** | Rank progress the player entered the match with. | [optional] [default to undefined]
**player_rank_initial_win_streak** | **number** | Win streak the player entered the match with. | [optional] [default to undefined]
**start_time** | **number** | Match start time as a unix timestamp. | [default to undefined]

## Example

```typescript
import { LastRankedMatch } from 'deadlock_api_client';

const instance: LastRankedMatch = {
    match_id,
    player_rank_consumed_demotion_protection,
    player_rank_desired_progress_change,
    player_rank_final_flat_progress,
    player_rank_initial_calibration_games,
    player_rank_initial_demotion_protection_games,
    player_rank_initial_display_rank,
    player_rank_initial_flat_progress,
    player_rank_initial_win_streak,
    start_time,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
