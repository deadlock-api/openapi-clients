# AnalyticsBuffStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_first_pickup_time_s** | **number** | Average game time (seconds) of a player\&#39;s first pickup of this buff type, over player-matches with timings, &#x60;null&#x60; without any. | [optional] [default to undefined]
**avg_pickup_time_s** | **number** | Average game time (seconds) of the &#x60;timed_pickups&#x60;, &#x60;null&#x60; without any. | [optional] [default to undefined]
**buff_type** | **string** | Buff type, e.g. &#x60;hp_permanent_pickup_lv2&#x60;. Display names, units and colors: &lt;https://api.deadlock-api.com/v1/assets/misc-entities&gt; (&#x60;buff_type_name&#x60;). | [default to undefined]
**is_permanent** | **boolean** | Whether the buff is permanent. Temporary power-ups never carry pickup timings. | [default to undefined]
**matches** | **number** | Player-matches matching the filters (the same for every buff type). Average pickups per match: &#x60;pickups / matches&#x60;. | [default to undefined]
**matches_with_pickup** | **number** | Player-matches with at least one pickup of this buff type. | [default to undefined]
**pickups** | **number** | Total pickups of this buff type. | [default to undefined]
**timed_matches** | **number** | Player-matches matching the filters that record pickup timings (the same for every buff type): matches since build 6712 (2026-09-29) with at least one timed permanent pickup. Average stat gained per match: &#x60;total_stat_value / timed_matches&#x60;. | [default to undefined]
**timed_pickups** | **number** | Pickups of this buff type with a recorded game time and stat value (build 6712+). | [default to undefined]
**total_stat_value** | **number** | Sum of the stat values granted by the &#x60;timed_pickups&#x60;, in the buff type\&#39;s unit (&#x60;buff_type_value_unit&#x60; in the assets). | [default to undefined]

## Example

```typescript
import { AnalyticsBuffStats } from 'deadlock_api_client';

const instance: AnalyticsBuffStats = {
    avg_first_pickup_time_s,
    avg_pickup_time_s,
    buff_type,
    is_permanent,
    matches,
    matches_with_pickup,
    pickups,
    timed_matches,
    timed_pickups,
    total_stat_value,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
