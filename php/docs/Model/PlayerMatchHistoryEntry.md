# PlayerMatchHistoryEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abandoned_time_s** | **int** |  | [optional]
**account_id** | **int** |  |
**brawl_avg_round_time_s** | **int** |  | [optional]
**brawl_score_team0** | **int** |  | [optional]
**brawl_score_team1** | **int** |  | [optional]
**denies** | **int** |  |
**game_mode** | **int** |  |
**hero_id** | **int** | See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; |
**hero_level** | **int** |  |
**last_hits** | **int** |  |
**match_duration_s** | **int** |  |
**match_id** | **int** |  |
**match_mode** | **int** |  |
**match_result** | **int** |  |
**net_worth** | **int** |  |
**objectives_mask_team0** | **int** |  |
**objectives_mask_team1** | **int** |  |
**player_assists** | **int** |  |
**player_deaths** | **int** |  |
**player_kills** | **int** |  |
**player_match_outcome** | **int** | How the match was scored for the player: 0 &#x3D; invalid, 1 &#x3D; win, 2 &#x3D; loss, 3 &#x3D; penalized, 4 &#x3D; penalized party, 5 &#x3D; not scored. |
**player_team** | **int** |  |
**ranked_calibration_match** | **int** | Non-zero if this match counted towards the player&#39;s ranked calibration. | [optional]
**ranked_delta** | **int** | The ranked progress change the player got from this match. | [optional]
**ranked_display_badge** | **int** | The ranked badge shown for the player after the match (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional]
**ranked_used_demotion_protection** | **bool** | Whether the player&#39;s demotion protection absorbed a loss in this match. | [optional]
**start_time** | **int** |  |
**team_abandoned** | **bool** |  | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
