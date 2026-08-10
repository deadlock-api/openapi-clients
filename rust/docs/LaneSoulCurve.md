# LaneSoulCurve

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_lane** | **u32** | The lane the matchup was played in. See the `lane_info` array of <https://api.deadlock-api.com/v1/assets/generic-data>. | 
**enemy_hero_ids** | **Vec<u32>** | The ascending hero id pair they laned against. | 
**hero_ids** | **Vec<u32>** | The ascending hero id pair that shared the lane. See more: <https://api.deadlock-api.com/v1/assets/heroes> | 
**matches_played** | **u64** | Lane matchups behind the curve, counted at its *least* covered sample. A match that ended before 900s still contributes to the earlier points, so the earlier points rest on at least this many matchups and never fewer. | 
**net_worth_diff** | **Vec<f64>** | Mean souls the duo is ahead by at the matching entry of `sample_times_s`. Negative means behind. Same length as `sample_times_s`. | 
**net_worth_diff_std** | **Vec<f64>** | Population standard deviation of the lead across the counted matchups, at the matching entry of `sample_times_s`. Same length as `sample_times_s`.  Spread between individual games, not uncertainty about the mean: it stays wide however many matchups are counted, because lane outcomes genuinely differ that much. | 
**sample_times_s** | **Vec<u32>** | Seconds into the match each entry of `net_worth_diff` was sampled at, ascending. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


