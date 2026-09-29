# AnalyticsHeroStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **u32** |  | 
**hero_id** | **u32** | See more: <https://api.deadlock-api.com/v1/assets/heroes> | 
**losses** | **u64** |  | 
**matches** | **u64** |  | 
**matches_per_bucket** | **u64** |  | 
**permanent_buff_matches** | **u64** | Matches that carry buff pickup counts. Equals `matches`, except on account-scoped queries (`account_ids` without item or ability filters): those read a per-account table that only has buff counts for matches ingested since build 6712 (late September 2026). | 
**permanent_buff_timing_matches** | **u64** | Matches with pickup timings. Only matches since build 6712 (2026-09-29) record pickup times, and only players with at least one permanent pickup count here. | 
**total_assists** | **u64** |  | 
**total_boss_damage** | **u64** |  | 
**total_creep_damage** | **u64** |  | 
**total_deaths** | **u64** |  | 
**total_denies** | **u64** |  | 
**total_first_permanent_buff_time_s** | **u64** | Sum of the game time (seconds) of each player's first permanent buff pickup, over the `permanent_buff_timing_matches` matches. Average: `total_first_permanent_buff_time_s / permanent_buff_timing_matches`. | 
**total_kills** | **u64** |  | 
**total_last_hits** | **u64** |  | 
**total_max_health** | **u64** |  | 
**total_net_worth** | **u64** |  | 
**total_neutral_damage** | **u64** |  | 
**total_permanent_buffs** | **u64** | Sum of permanent buff (power-up) pickups over the `permanent_buff_matches` matches. Average per match: `total_permanent_buffs / permanent_buff_matches`. Buff types: <https://api.deadlock-api.com/v1/assets/misc-entities> | 
**total_player_damage** | **u64** |  | 
**total_player_damage_taken** | **u64** |  | 
**total_shots_hit** | **u64** |  | 
**total_shots_missed** | **u64** |  | 
**wins** | **u64** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


