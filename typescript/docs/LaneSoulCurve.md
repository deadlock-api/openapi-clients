# LaneSoulCurve


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_lane** | **number** | The lane the matchup was played in. See the &#x60;lane_info&#x60; array of &lt;https://api.deadlock-api.com/v1/assets/generic-data&gt;. | [default to undefined]
**enemy_hero_ids** | **Array&lt;number&gt;** | The ascending hero id pair they laned against. | [default to undefined]
**hero_ids** | **Array&lt;number&gt;** | The ascending hero id pair that shared the lane. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [default to undefined]
**matches_played** | **number** | Lane matchups behind the curve, counted at its *least* covered sample. A match that ended before 900s still contributes to the earlier points, so the earlier points rest on at least this many matchups and never fewer. | [default to undefined]
**net_worth_diff** | **Array&lt;number&gt;** | Mean souls the duo is ahead by at the matching entry of &#x60;sample_times_s&#x60;. Negative means behind. Same length as &#x60;sample_times_s&#x60;. | [default to undefined]
**net_worth_diff_std** | **Array&lt;number&gt;** | Population standard deviation of the lead across the counted matchups, at the matching entry of &#x60;sample_times_s&#x60;. Same length as &#x60;sample_times_s&#x60;.  Spread between individual games, not uncertainty about the mean: it stays wide however many matchups are counted, because lane outcomes genuinely differ that much. | [default to undefined]
**sample_times_s** | **Array&lt;number&gt;** | Seconds into the match each entry of &#x60;net_worth_diff&#x60; was sampled at, ascending. | [default to undefined]

## Example

```typescript
import { LaneSoulCurve } from 'deadlock_api_client';

const instance: LaneSoulCurve = {
    assigned_lane,
    enemy_hero_ids,
    hero_ids,
    matches_played,
    net_worth_diff,
    net_worth_diff_std,
    sample_times_s,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
