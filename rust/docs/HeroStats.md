# HeroStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **u32** |  | 
**accuracy** | **f64** |  | 
**assists** | **u64** |  | 
**assists_per_min** | **f64** |  | 
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
**time_played** | **u64** |  | 
**total_boss_damage** | **u64** |  | 
**total_creep_damage** | **u64** |  | 
**total_neutral_damage** | **u64** |  | 
**total_player_damage** | **u64** |  | 
**total_player_damage_taken** | **u64** |  | 
**wins** | **u64** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


