# HeroStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **number** |  | [default to undefined]
**accuracy** | **number** |  | [default to undefined]
**assists** | **number** |  | [default to undefined]
**assists_per_min** | **number** |  | [default to undefined]
**avg_first_permanent_buff_time_s** | **number** | Average game time (seconds) of the first permanent buff pickup, over matches with pickup timings (build 6712+, at least one permanent pickup), &#x60;null&#x60; without any. | [optional] [default to undefined]
**creeps_per_min** | **number** |  | [default to undefined]
**crit_shot_rate** | **number** |  | [default to undefined]
**damage_mitigated_per_min** | **number** |  | [default to undefined]
**damage_per_min** | **number** |  | [default to undefined]
**damage_per_soul** | **number** |  | [default to undefined]
**damage_taken_per_min** | **number** |  | [default to undefined]
**damage_taken_per_soul** | **number** |  | [default to undefined]
**deaths** | **number** |  | [default to undefined]
**deaths_per_min** | **number** |  | [default to undefined]
**denies_per_match** | **number** |  | [default to undefined]
**denies_per_min** | **number** |  | [default to undefined]
**ending_level** | **number** |  | [default to undefined]
**hero_id** | **number** | See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [default to undefined]
**kills** | **number** |  | [default to undefined]
**kills_per_min** | **number** |  | [default to undefined]
**last_hits_per_min** | **number** |  | [default to undefined]
**last_played** | **number** |  | [default to undefined]
**matches** | **Array&lt;number&gt;** |  | [default to undefined]
**matches_played** | **number** |  | [default to undefined]
**mvp_rank_counts** | **Array&lt;number&gt;** | Matches by the MVP rank Valve awarded the player: index 0 is rank 1 (MVP), index 1 is rank 2, index 2 is rank 3. Only the top three players of a match get a rank. | [default to undefined]
**mvp_rated_matches** | **number** | Matches played since Valve started reporting MVP ranks (2026-01-06). Divide &#x60;mvp_rank_counts&#x60; by this, not by &#x60;matches_played&#x60;, when the time range reaches further back. | [default to undefined]
**networth_per_min** | **number** |  | [default to undefined]
**obj_damage_per_min** | **number** |  | [default to undefined]
**obj_damage_per_soul** | **number** |  | [default to undefined]
**permanent_buff_matches** | **number** | Matches that carry buff pickup counts. Only matches ingested since build 6712 (late September 2026) have them here, so divide by this rather than &#x60;matches_played&#x60;. | [default to undefined]
**permanent_buffs** | **number** | Permanent buff (power-up) pickups over the &#x60;permanent_buff_matches&#x60; matches. Buff types: &lt;https://api.deadlock-api.com/v1/assets/misc-entities&gt; | [default to undefined]
**permanent_buffs_per_min** | **number** | Permanent buff pickups per minute over the &#x60;permanent_buff_matches&#x60; matches, &#x60;null&#x60; without any. | [optional] [default to undefined]
**time_played** | **number** |  | [default to undefined]
**total_boss_damage** | **number** |  | [default to undefined]
**total_creep_damage** | **number** |  | [default to undefined]
**total_neutral_damage** | **number** |  | [default to undefined]
**total_player_damage** | **number** |  | [default to undefined]
**total_player_damage_taken** | **number** |  | [default to undefined]
**wins** | **number** |  | [default to undefined]

## Example

```typescript
import { HeroStats } from 'deadlock_api_client';

const instance: HeroStats = {
    account_id,
    accuracy,
    assists,
    assists_per_min,
    avg_first_permanent_buff_time_s,
    creeps_per_min,
    crit_shot_rate,
    damage_mitigated_per_min,
    damage_per_min,
    damage_per_soul,
    damage_taken_per_min,
    damage_taken_per_soul,
    deaths,
    deaths_per_min,
    denies_per_match,
    denies_per_min,
    ending_level,
    hero_id,
    kills,
    kills_per_min,
    last_hits_per_min,
    last_played,
    matches,
    matches_played,
    mvp_rank_counts,
    mvp_rated_matches,
    networth_per_min,
    obj_damage_per_min,
    obj_damage_per_soul,
    permanent_buff_matches,
    permanent_buffs,
    permanent_buffs_per_min,
    time_played,
    total_boss_damage,
    total_creep_damage,
    total_neutral_damage,
    total_player_damage,
    total_player_damage_taken,
    wins,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
