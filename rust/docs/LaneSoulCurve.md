# LaneSoulCurve

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_lane** | **u32** | The lane the matchup was played in, or `0` when `assigned_lane` was grouped away. See the `lane_info` array of <https://api.deadlock-api.com/v1/assets/generic-data>. | 
**enemy_hero_ids** | **Vec<u32>** | The ascending hero id pair they laned against, or empty when grouped away. | 
**hero_ids** | **Vec<u32>** | The ascending hero id pair that shared the lane, or empty when grouped away. See more: <https://api.deadlock-api.com/v1/assets/heroes> | 
**matches_played** | **u64** | Lane matchups behind the row, counted at its *first* sample. This is what `min_matches` and `max_matches` filter on, so it does not move when the requested time range changes; read `sample_matches` for what any individual point rests on. | 
**net_worth_diff** | **Vec<f64>** | Mean souls the duo is ahead by at the matching entry of `sample_times_s`. Negative means behind. Same length as `sample_times_s`. | 
**net_worth_diff_std** | **Vec<f64>** | Population standard deviation of the lead across the counted matchups, at the matching entry of `sample_times_s`. Same length as `sample_times_s`.  Spread between individual games, not uncertainty about the mean: it stays wide however many matchups are counted, because lane outcomes genuinely differ that much. | 
**sample_matches** | **Vec<u64>** | How many lane matchups were still running at the matching entry of `sample_times_s`. Falls off towards the end of the curve as shorter matches drop out. | 
**sample_times_s** | **Vec<u32>** | Seconds into the match each entry of the curves was sampled at, ascending. | 
**stats** | [**std::collections::HashMap<String, models::LaneStatCurve>**](LaneStatCurve.md) | A curve per stat named in `stats`. Empty unless the parameter was set. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


