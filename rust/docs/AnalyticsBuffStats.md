# AnalyticsBuffStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_first_pickup_time_s** | Option<**f64**> | Average game time (seconds) of a player's first pickup of this buff type, over player-matches with timings, `null` without any. | [optional]
**avg_pickup_time_s** | Option<**f64**> | Average game time (seconds) of the `timed_pickups`, `null` without any. | [optional]
**buff_type** | **String** | Buff type, e.g. `hp_permanent_pickup_lv2`. Display names, units and colors: <https://api.deadlock-api.com/v1/assets/misc-entities> (`buff_type_name`). | 
**is_permanent** | **bool** | Whether the buff is permanent. Temporary power-ups never carry pickup timings. | 
**matches** | **u64** | Player-matches matching the filters (the same for every buff type). Average pickups per match: `pickups / matches`. | 
**matches_with_pickup** | **u64** | Player-matches with at least one pickup of this buff type. | 
**pickups** | **u64** | Total pickups of this buff type. | 
**timed_matches** | **u64** | Player-matches matching the filters that record pickup timings (the same for every buff type): matches since build 6712 (2026-09-29) with at least one timed permanent pickup. Average stat gained per match: `total_stat_value / timed_matches`. | 
**timed_pickups** | **u64** | Pickups of this buff type with a recorded game time and stat value (build 6712+). | 
**total_stat_value** | **f64** | Sum of the stat values granted by the `timed_pickups`, in the buff type's unit (`buff_type_value_unit` in the assets). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


