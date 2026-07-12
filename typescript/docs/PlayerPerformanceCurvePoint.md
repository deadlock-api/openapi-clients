# PlayerPerformanceCurvePoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assists_avg** | **number** | Average assists at this time point | [default to undefined]
**assists_std** | **number** | Standard deviation of assists at this time point | [default to undefined]
**deaths_avg** | **number** | Average deaths at this time point | [default to undefined]
**deaths_std** | **number** | Standard deviation of deaths at this time point | [default to undefined]
**game_time** | **number** | The time point of the data. If &#x60;resolution&#x60; (default 10) is &gt; 0, this is a percentage (0, 10, ..., 100). If &#x60;resolution&#x60; is 0, this is the match time in seconds. | [default to undefined]
**gold_boss_avg** | **number** | Average souls earned from objectives at this time point | [default to undefined]
**gold_boss_orb_avg** | **number** | Average souls earned from secured objective orbs at this time point | [default to undefined]
**gold_death_loss_avg** | **number** | Average souls lost on death at this time point | [default to undefined]
**gold_denied_avg** | **number** | Average souls denied to enemies at this time point | [default to undefined]
**gold_lane_creep_avg** | **number** | Average souls earned from lane creeps at this time point | [default to undefined]
**gold_lane_creep_orbs_avg** | **number** | Average souls earned from secured lane-creep orbs at this time point | [default to undefined]
**gold_neutral_creep_avg** | **number** | Average souls earned from neutral (jungle) creeps at this time point | [default to undefined]
**gold_neutral_creep_orbs_avg** | **number** | Average souls earned from secured neutral-creep orbs at this time point | [default to undefined]
**gold_player_avg** | **number** | Average souls earned from hero kills at this time point | [default to undefined]
**gold_player_orbs_avg** | **number** | Average souls earned from secured hero-kill orbs at this time point | [default to undefined]
**gold_treasure_avg** | **number** | Average souls earned from the urn at this time point | [default to undefined]
**kills_avg** | **number** | Average kills at this time point | [default to undefined]
**kills_std** | **number** | Standard deviation of kills at this time point | [default to undefined]
**net_worth_avg** | **number** | Average net worth at this time point | [default to undefined]
**net_worth_std** | **number** | Standard deviation of net worth at this time point | [default to undefined]

## Example

```typescript
import { PlayerPerformanceCurvePoint } from 'deadlock_api_client';

const instance: PlayerPerformanceCurvePoint = {
    assists_avg,
    assists_std,
    deaths_avg,
    deaths_std,
    game_time,
    gold_boss_avg,
    gold_boss_orb_avg,
    gold_death_loss_avg,
    gold_denied_avg,
    gold_lane_creep_avg,
    gold_lane_creep_orbs_avg,
    gold_neutral_creep_avg,
    gold_neutral_creep_orbs_avg,
    gold_player_avg,
    gold_player_orbs_avg,
    gold_treasure_avg,
    kills_avg,
    kills_std,
    net_worth_avg,
    net_worth_std,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
