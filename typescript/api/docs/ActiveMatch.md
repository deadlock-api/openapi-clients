# ActiveMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compat_version** | **number** |  | [optional] [default to undefined]
**duration_s** | **number** |  | [optional] [default to undefined]
**game_mode** | **number** |  | [optional] [default to undefined]
**game_mode_parsed** | [**ActiveMatchGameMode**](ActiveMatchGameMode.md) |  | [optional] [default to undefined]
**game_mode_version** | **number** |  | [optional] [default to undefined]
**lobby_id** | **number** |  | [optional] [default to undefined]
**match_id** | **number** |  | [optional] [default to undefined]
**match_mode** | **number** |  | [optional] [default to undefined]
**match_mode_parsed** | [**ActiveMatchMode**](ActiveMatchMode.md) |  | [optional] [default to undefined]
**match_score** | **number** |  | [optional] [default to undefined]
**net_worth_team_0** | **number** |  | [optional] [default to undefined]
**net_worth_team_1** | **number** |  | [optional] [default to undefined]
**objectives_mask_team0** | **number** |  | [optional] [default to undefined]
**objectives_mask_team1** | **number** |  | [optional] [default to undefined]
**open_spectator_slots** | **number** |  | [optional] [default to undefined]
**players** | [**Array&lt;ActiveMatchPlayer&gt;**](ActiveMatchPlayer.md) |  | [default to undefined]
**region_mode** | **number** |  | [optional] [default to undefined]
**region_mode_parsed** | [**ActiveMatchRegionMode**](ActiveMatchRegionMode.md) |  | [optional] [default to undefined]
**spectators** | **number** |  | [optional] [default to undefined]
**start_time** | **number** |  | [optional] [default to undefined]
**winning_team** | **number** |  | [optional] [default to undefined]
**winning_team_parsed** | [**ActiveMatchTeam**](ActiveMatchTeam.md) |  | [optional] [default to undefined]

## Example

```typescript
import { ActiveMatch } from 'deadlock-api-client';

const instance: ActiveMatch = {
    compat_version,
    duration_s,
    game_mode,
    game_mode_parsed,
    game_mode_version,
    lobby_id,
    match_id,
    match_mode,
    match_mode_parsed,
    match_score,
    net_worth_team_0,
    net_worth_team_1,
    objectives_mask_team0,
    objectives_mask_team1,
    open_spectator_slots,
    players,
    region_mode,
    region_mode_parsed,
    spectators,
    start_time,
    winning_team,
    winning_team_parsed,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
