# PlayerPerformanceCurvePoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assists_avg** | **number** | Average assists at this time point | [default to undefined]
**assists_std** | **number** | Standard deviation of assists at this time point | [default to undefined]
**deaths_avg** | **number** | Average deaths at this time point | [default to undefined]
**deaths_std** | **number** | Standard deviation of deaths at this time point | [default to undefined]
**game_time** | **number** | The time point of the data. If &#x60;resolution&#x60; (default 10) is &gt; 0, this is a percentage (0, 10, ..., 100). If &#x60;resolution&#x60; is 0, this is the match time in seconds. | [default to undefined]
**gold_ability_assassinate_avg** | **number** | Average souls earned from the Assassinate ability at this time point | [default to undefined]
**gold_ability_assassinate_std** | **number** | Standard deviation of &#x60;gold_ability_assassinate_avg&#x60; at this time point | [default to undefined]
**gold_assists_avg** | **number** | Average souls earned from assists at this time point (part of &#x60;gold_player_avg&#x60;) | [default to undefined]
**gold_assists_std** | **number** | Standard deviation of &#x60;gold_assists_avg&#x60; at this time point | [default to undefined]
**gold_boss_avg** | **number** | Average souls earned from objectives at this time point | [default to undefined]
**gold_boss_orb_avg** | **number** | Average souls earned from secured objective orbs at this time point | [default to undefined]
**gold_boss_orb_std** | **number** | Standard deviation of &#x60;gold_boss_orb_avg&#x60; at this time point | [default to undefined]
**gold_boss_std** | **number** | Standard deviation of &#x60;gold_boss_avg&#x60; at this time point | [default to undefined]
**gold_breakable_avg** | **number** | Average souls earned from breakables (crates, statues) at this time point | [default to undefined]
**gold_breakable_std** | **number** | Standard deviation of &#x60;gold_breakable_avg&#x60; at this time point | [default to undefined]
**gold_death_loss_avg** | **number** | Average souls lost on death at this time point | [default to undefined]
**gold_death_loss_std** | **number** | Standard deviation of &#x60;gold_death_loss_avg&#x60; at this time point | [default to undefined]
**gold_denied_avg** | **number** | Average souls denied to enemies at this time point | [default to undefined]
**gold_denied_std** | **number** | Standard deviation of &#x60;gold_denied_avg&#x60; at this time point | [default to undefined]
**gold_item_cultist_sacrifice_avg** | **number** | Average souls earned from the Cultist Sacrifice item at this time point | [default to undefined]
**gold_item_cultist_sacrifice_std** | **number** | Standard deviation of &#x60;gold_item_cultist_sacrifice_avg&#x60; at this time point | [default to undefined]
**gold_item_goose_egg_avg** | **number** | Average souls earned from the Golden Goose Egg item at this time point | [default to undefined]
**gold_item_goose_egg_std** | **number** | Standard deviation of &#x60;gold_item_goose_egg_avg&#x60; at this time point | [default to undefined]
**gold_item_trophy_collector_avg** | **number** | Average souls earned from the Trophy Collector item at this time point | [default to undefined]
**gold_item_trophy_collector_std** | **number** | Standard deviation of &#x60;gold_item_trophy_collector_avg&#x60; at this time point | [default to undefined]
**gold_lane_creep_avg** | **number** | Average souls earned from lane creeps at this time point | [default to undefined]
**gold_lane_creep_orbs_avg** | **number** | Average souls earned from secured lane-creep orbs at this time point | [default to undefined]
**gold_lane_creep_orbs_std** | **number** | Standard deviation of &#x60;gold_lane_creep_orbs_avg&#x60; at this time point | [default to undefined]
**gold_lane_creep_std** | **number** | Standard deviation of &#x60;gold_lane_creep_avg&#x60; at this time point | [default to undefined]
**gold_neutral_creep_avg** | **number** | Average souls earned from neutral (jungle) creeps at this time point | [default to undefined]
**gold_neutral_creep_orbs_avg** | **number** | Average souls earned from secured neutral-creep orbs at this time point | [default to undefined]
**gold_neutral_creep_orbs_std** | **number** | Standard deviation of &#x60;gold_neutral_creep_orbs_avg&#x60; at this time point | [default to undefined]
**gold_neutral_creep_std** | **number** | Standard deviation of &#x60;gold_neutral_creep_avg&#x60; at this time point | [default to undefined]
**gold_player_avg** | **number** | Average souls earned from hero kills at this time point, including assist souls (see &#x60;gold_assists_avg&#x60;) | [default to undefined]
**gold_player_orbs_avg** | **number** | Average souls earned from secured hero-kill orbs at this time point | [default to undefined]
**gold_player_orbs_std** | **number** | Standard deviation of &#x60;gold_player_orbs_avg&#x60; at this time point | [default to undefined]
**gold_player_std** | **number** | Standard deviation of &#x60;gold_player_avg&#x60; at this time point | [default to undefined]
**gold_team_bonus_avg** | **number** | Average souls earned from the team bonus at this time point | [default to undefined]
**gold_team_bonus_std** | **number** | Standard deviation of &#x60;gold_team_bonus_avg&#x60; at this time point | [default to undefined]
**gold_treasure_avg** | **number** | Average souls earned from the urn at this time point | [default to undefined]
**gold_treasure_std** | **number** | Standard deviation of &#x60;gold_treasure_avg&#x60; at this time point | [default to undefined]
**kills_avg** | **number** | Average kills at this time point | [default to undefined]
**kills_std** | **number** | Standard deviation of kills at this time point | [default to undefined]
**net_worth_avg** | **number** | Average net worth at this time point | [default to undefined]
**net_worth_std** | **number** | Standard deviation of net worth at this time point | [default to undefined]
**permanent_buffs_avg** | **number** | Average permanent buff (power-up) pickups collected up to this time point. Only matches since build 6712 (2026-09-29) record pickup times, so only players with at least one timed permanent pickup count; &#x60;null&#x60; when there are none. | [optional] [default to undefined]
**permanent_buffs_std** | **number** | Standard deviation of &#x60;permanent_buffs_avg&#x60; at this time point; &#x60;null&#x60; when there are no players with timed permanent pickups. | [optional] [default to undefined]

## Example

```typescript
import { PlayerPerformanceCurvePoint } from 'deadlock_api_client';

const instance: PlayerPerformanceCurvePoint = {
    assists_avg,
    assists_std,
    deaths_avg,
    deaths_std,
    game_time,
    gold_ability_assassinate_avg,
    gold_ability_assassinate_std,
    gold_assists_avg,
    gold_assists_std,
    gold_boss_avg,
    gold_boss_orb_avg,
    gold_boss_orb_std,
    gold_boss_std,
    gold_breakable_avg,
    gold_breakable_std,
    gold_death_loss_avg,
    gold_death_loss_std,
    gold_denied_avg,
    gold_denied_std,
    gold_item_cultist_sacrifice_avg,
    gold_item_cultist_sacrifice_std,
    gold_item_goose_egg_avg,
    gold_item_goose_egg_std,
    gold_item_trophy_collector_avg,
    gold_item_trophy_collector_std,
    gold_lane_creep_avg,
    gold_lane_creep_orbs_avg,
    gold_lane_creep_orbs_std,
    gold_lane_creep_std,
    gold_neutral_creep_avg,
    gold_neutral_creep_orbs_avg,
    gold_neutral_creep_orbs_std,
    gold_neutral_creep_std,
    gold_player_avg,
    gold_player_orbs_avg,
    gold_player_orbs_std,
    gold_player_std,
    gold_team_bonus_avg,
    gold_team_bonus_std,
    gold_treasure_avg,
    gold_treasure_std,
    kills_avg,
    kills_std,
    net_worth_avg,
    net_worth_std,
    permanent_buffs_avg,
    permanent_buffs_std,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
