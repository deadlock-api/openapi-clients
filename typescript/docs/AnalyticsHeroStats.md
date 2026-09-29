# AnalyticsHeroStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **number** |  | [default to undefined]
**hero_id** | **number** | See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [default to undefined]
**losses** | **number** |  | [default to undefined]
**matches** | **number** |  | [default to undefined]
**matches_per_bucket** | **number** |  | [default to undefined]
**permanent_buff_matches** | **number** | Matches that carry buff pickup counts. Equals &#x60;matches&#x60;, except on account-scoped queries (&#x60;account_ids&#x60; without item or ability filters): those read a per-account table that only has buff counts for matches ingested since build 6712 (late September 2026). | [default to undefined]
**permanent_buff_timing_matches** | **number** | Matches with pickup timings. Only matches since build 6712 (2026-09-29) record pickup times, and only players with at least one permanent pickup count here. | [default to undefined]
**total_assists** | **number** |  | [default to undefined]
**total_boss_damage** | **number** |  | [default to undefined]
**total_creep_damage** | **number** |  | [default to undefined]
**total_deaths** | **number** |  | [default to undefined]
**total_denies** | **number** |  | [default to undefined]
**total_first_permanent_buff_time_s** | **number** | Sum of the game time (seconds) of each player\&#39;s first permanent buff pickup, over the &#x60;permanent_buff_timing_matches&#x60; matches. Average: &#x60;total_first_permanent_buff_time_s / permanent_buff_timing_matches&#x60;. | [default to undefined]
**total_kills** | **number** |  | [default to undefined]
**total_last_hits** | **number** |  | [default to undefined]
**total_max_health** | **number** |  | [default to undefined]
**total_net_worth** | **number** |  | [default to undefined]
**total_neutral_damage** | **number** |  | [default to undefined]
**total_permanent_buffs** | **number** | Sum of permanent buff (power-up) pickups over the &#x60;permanent_buff_matches&#x60; matches. Average per match: &#x60;total_permanent_buffs / permanent_buff_matches&#x60;. Buff types: &lt;https://api.deadlock-api.com/v1/assets/misc-entities&gt; | [default to undefined]
**total_player_damage** | **number** |  | [default to undefined]
**total_player_damage_taken** | **number** |  | [default to undefined]
**total_shots_hit** | **number** |  | [default to undefined]
**total_shots_missed** | **number** |  | [default to undefined]
**wins** | **number** |  | [default to undefined]

## Example

```typescript
import { AnalyticsHeroStats } from 'deadlock_api_client';

const instance: AnalyticsHeroStats = {
    bucket,
    hero_id,
    losses,
    matches,
    matches_per_bucket,
    permanent_buff_matches,
    permanent_buff_timing_matches,
    total_assists,
    total_boss_damage,
    total_creep_damage,
    total_deaths,
    total_denies,
    total_first_permanent_buff_time_s,
    total_kills,
    total_last_hits,
    total_max_health,
    total_net_worth,
    total_neutral_damage,
    total_permanent_buffs,
    total_player_damage,
    total_player_damage_taken,
    total_shots_hit,
    total_shots_missed,
    wins,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
