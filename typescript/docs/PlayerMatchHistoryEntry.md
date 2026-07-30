# PlayerMatchHistoryEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abandoned_time_s** | **number** |  | [optional] [default to undefined]
**account_id** | **number** |  | [default to undefined]
**brawl_avg_round_time_s** | **number** |  | [optional] [default to undefined]
**brawl_score_team0** | **number** |  | [optional] [default to undefined]
**brawl_score_team1** | **number** |  | [optional] [default to undefined]
**denies** | **number** |  | [default to undefined]
**game_mode** | **number** |  | [default to undefined]
**hero_id** | **number** | See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [default to undefined]
**hero_level** | **number** |  | [default to undefined]
**last_hits** | **number** |  | [default to undefined]
**match_duration_s** | **number** |  | [default to undefined]
**match_id** | **number** |  | [default to undefined]
**match_mode** | **number** |  | [default to undefined]
**match_result** | **number** |  | [default to undefined]
**net_worth** | **number** |  | [default to undefined]
**objectives_mask_team0** | **number** |  | [default to undefined]
**objectives_mask_team1** | **number** |  | [default to undefined]
**player_assists** | **number** |  | [default to undefined]
**player_deaths** | **number** |  | [default to undefined]
**player_kills** | **number** |  | [default to undefined]
**player_match_outcome** | **number** | How the match was scored for the player: 0 &#x3D; invalid, 1 &#x3D; win, 2 &#x3D; loss, 3 &#x3D; penalized, 4 &#x3D; penalized party, 5 &#x3D; not scored. | [default to undefined]
**player_team** | **number** |  | [default to undefined]
**ranked_calibration_match** | **number** | Non-zero if this match counted towards the player\&#39;s ranked calibration. | [optional] [default to undefined]
**ranked_delta** | **number** | The ranked progress change the player got from this match. | [optional] [default to undefined]
**ranked_display_badge** | **number** | The ranked badge shown for the player after the match (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional] [default to undefined]
**ranked_used_demotion_protection** | **boolean** | Whether the player\&#39;s demotion protection absorbed a loss in this match. | [optional] [default to undefined]
**start_time** | **number** |  | [default to undefined]
**team_abandoned** | **boolean** |  | [optional] [default to undefined]

## Example

```typescript
import { PlayerMatchHistoryEntry } from 'deadlock_api_client';

const instance: PlayerMatchHistoryEntry = {
    abandoned_time_s,
    account_id,
    brawl_avg_round_time_s,
    brawl_score_team0,
    brawl_score_team1,
    denies,
    game_mode,
    hero_id,
    hero_level,
    last_hits,
    match_duration_s,
    match_id,
    match_mode,
    match_result,
    net_worth,
    objectives_mask_team0,
    objectives_mask_team1,
    player_assists,
    player_deaths,
    player_kills,
    player_match_outcome,
    player_team,
    ranked_calibration_match,
    ranked_delta,
    ranked_display_badge,
    ranked_used_demotion_protection,
    start_time,
    team_abandoned,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
