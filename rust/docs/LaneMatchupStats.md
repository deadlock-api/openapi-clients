# LaneMatchupStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_lane** | **u32** | The lane the matchup was played in. See the `lane_info` array of <https://api.deadlock-api.com/v1/assets/generic-data>. | 
**enemy_hero_ids** | **Vec<u32>** | The ascending hero id pair they laned against. | 
**hero_ids** | **Vec<u32>** | The ascending hero id pair that shared the lane. See more: <https://api.deadlock-api.com/v1/assets/heroes> | 
**matches_played** | **u64** | The total number of lane matchups between `hero_ids` and `enemy_hero_ids` in this lane. | 
**net_worth_diff_9min** | **f64** | Mean souls the duo is ahead by 9 minutes in, against that duo. Negative means behind. `0` when no counted matchup had net-worth samples for all four players. | 
**net_worth_matches** | **u64** | How many of `matches_played` carried net-worth samples for all four players. | 
**wins** | **u64** | The number of matches `hero_ids` won against `enemy_hero_ids` in this lane. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


