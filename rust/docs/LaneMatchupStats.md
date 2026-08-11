# LaneMatchupStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_lane** | **u32** | The lane the matchup was played in, or `0` when `assigned_lane` was grouped away. See the `lane_info` array of <https://api.deadlock-api.com/v1/assets/generic-data>. | 
**enemy_hero_ids** | **Vec<u32>** | The ascending hero id pair they laned against, or empty when grouped away. | 
**hero_ids** | **Vec<u32>** | The ascending hero id pair that shared the lane, or empty when grouped away. See more: <https://api.deadlock-api.com/v1/assets/heroes> | 
**matches_played** | **u64** | The total number of lane matchups between `hero_ids` and `enemy_hero_ids` in this lane. | 
**net_worth_diff** | **f64** | Mean souls the duo is ahead by at `sample_time_s`, against that duo. Negative means behind. `0` when no counted matchup lasted that long. | 
**sample_matches** | **u64** | How many of `matches_played` lasted to `sample_time_s` with all four players still in. Every reading on this row rests on those matchups only. | 
**sample_time_s** | **u32** | Seconds into the match the stat readings were taken at. Echoes the `sample_time_s` parameter. | 
**stats** | [**std::collections::HashMap<String, models::LaneMatchupStat>**](LaneMatchupStat.md) | A reading per stat named in `stats`. Empty unless the parameter was set. | 
**wins** | **u64** | The number of matches `hero_ids` won against `enemy_hero_ids` in this lane. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


