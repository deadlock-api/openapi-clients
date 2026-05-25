# StreetBrawl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apper_round** | **Array&lt;number&gt;** |  | [default to undefined]
**buy_time** | **Array&lt;number&gt;** |  | [default to undefined]
**buy_time_grace_period** | **number** |  | [default to undefined]
**comeback_bonus_health** | **number** |  | [default to undefined]
**comeback_bonus_health_critical** | **number** |  | [default to undefined]
**gold_per_round** | **Array&lt;number&gt;** |  | [default to undefined]
**item_draft_rerolls_per_round** | **Array&lt;number&gt;** |  | [default to undefined]
**item_draft_rounds_per_game_round** | [**Array&lt;ItemDraftRoundPerGameRound&gt;**](ItemDraftRoundPerGameRound.md) |  | [default to undefined]
**item_drafts** | [**{ [key: string]: DraftBuckets; }**](DraftBuckets.md) |  | [default to undefined]
**lane_number** | **number** |  | [default to undefined]
**objective_max_health** | **Array&lt;number&gt;** |  | [default to undefined]
**overtime_respawn_time_increase** | **Array&lt;number&gt;** |  | [default to undefined]
**overtime_respawn_time_increase_urgent** | **Array&lt;number&gt;** |  | [default to undefined]
**overtime_trooper_damage_scale** | **Array&lt;number&gt;** |  | [default to undefined]
**overtime_trooper_health_scale** | **Array&lt;number&gt;** |  | [default to undefined]
**pre_buy_time** | **Array&lt;number&gt;** |  | [default to undefined]
**respawn_times** | **Array&lt;number&gt;** |  | [default to undefined]
**round_length_minutes** | **Array&lt;number&gt;** |  | [default to undefined]
**round_length_minutes_urgent** | **Array&lt;number&gt;** |  | [default to undefined]
**score_to_win** | **number** |  | [default to undefined]
**scoring_time** | **number** |  | [default to undefined]
**tier1_max_resist_time** | **number** |  | [default to undefined]
**tier2_bonus_health** | **number** |  | [default to undefined]
**tier2_max_resist_time** | **number** |  | [default to undefined]
**trooper_spawn_before_round_start_timer** | **number** |  | [default to undefined]
**trooper_spawn_timer** | **Array&lt;number&gt;** |  | [default to undefined]
**ultimate_unlock_round** | **number** |  | [default to undefined]
**zip_boost_cooldown_on_start** | **number** |  | [default to undefined]

## Example

```typescript
import { StreetBrawl } from 'deadlock_api_client';

const instance: StreetBrawl = {
    apper_round,
    buy_time,
    buy_time_grace_period,
    comeback_bonus_health,
    comeback_bonus_health_critical,
    gold_per_round,
    item_draft_rerolls_per_round,
    item_draft_rounds_per_game_round,
    item_drafts,
    lane_number,
    objective_max_health,
    overtime_respawn_time_increase,
    overtime_respawn_time_increase_urgent,
    overtime_trooper_damage_scale,
    overtime_trooper_health_scale,
    pre_buy_time,
    respawn_times,
    round_length_minutes,
    round_length_minutes_urgent,
    score_to_win,
    scoring_time,
    tier1_max_resist_time,
    tier2_bonus_health,
    tier2_max_resist_time,
    trooper_spawn_before_round_start_timer,
    trooper_spawn_timer,
    ultimate_unlock_round,
    zip_boost_cooldown_on_start,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
