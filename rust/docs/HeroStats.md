# HeroStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **u32** |  | 
**accuracy** | **f64** |  | 
**assists** | **u64** |  | 
**assists_per_min** | **f64** |  | 
**avg_first_permanent_buff_time_s** | Option<**f64**> | Average game time (seconds) of the first permanent buff pickup, over matches with pickup timings (build 6712+, at least one permanent pickup), `null` without any. | [optional]
**creeps_per_min** | **f64** |  | 
**crit_shot_rate** | **f64** |  | 
**damage_mitigated_per_min** | **f64** |  | 
**damage_per_min** | **f64** |  | 
**damage_per_soul** | **f64** |  | 
**damage_taken_per_min** | **f64** |  | 
**damage_taken_per_soul** | **f64** |  | 
**deaths** | **u64** |  | 
**deaths_per_min** | **f64** |  | 
**denies_per_match** | **f64** |  | 
**denies_per_min** | **f64** |  | 
**ending_level** | **f64** |  | 
**hero_id** | **u32** | See more: <https://api.deadlock-api.com/v1/assets/heroes> | 
**kills** | **u64** |  | 
**kills_per_min** | **f64** |  | 
**last_hits_per_min** | **f64** |  | 
**last_played** | **u32** |  | 
**matches** | **Vec<u64>** |  | 
**matches_played** | **u64** |  | 
**mvp_rank_counts** | **Vec<u64>** | Matches by the MVP rank Valve awarded the player: index 0 is rank 1 (MVP), index 1 is rank 2, index 2 is rank 3. Only the top three players of a match get a rank. | 
**mvp_rated_matches** | **u64** | Matches played since Valve started reporting MVP ranks (2026-01-06). Divide `mvp_rank_counts` by this, not by `matches_played`, when the time range reaches further back. | 
**networth_per_min** | **f64** |  | 
**obj_damage_per_min** | **f64** |  | 
**obj_damage_per_soul** | **f64** |  | 
**permanent_buff_matches** | **u64** | Matches that carry buff pickup counts. Only matches ingested since build 6712 (late September 2026) have them here, so divide by this rather than `matches_played`. | 
**permanent_buffs** | **u64** | Permanent buff (power-up) pickups over the `permanent_buff_matches` matches. Buff types: <https://api.deadlock-api.com/v1/assets/misc-entities> | 
**permanent_buffs_per_min** | Option<**f64**> | Permanent buff pickups per minute over the `permanent_buff_matches` matches, `null` without any. | [optional]
**time_played** | **u64** |  | 
**total_boss_damage** | **u64** |  | 
**total_creep_damage** | **u64** |  | 
**total_neutral_damage** | **u64** |  | 
**total_player_damage** | **u64** |  | 
**total_player_damage_taken** | **u64** |  | 
**wins** | **u64** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


