# LaneSoulCurve

**⚠️ Subject to change:** newly added, fields may change or be removed without notice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_lane** | **number** | The lane the matchup was played in, or &#x60;0&#x60; when &#x60;assigned_lane&#x60; was grouped away. See the &#x60;lane_info&#x60; array of &lt;https://api.deadlock-api.com/v1/assets/generic-data&gt;. | [default to undefined]
**enemy_hero_ids** | **Array&lt;number&gt;** | The ascending hero id pair they laned against, or empty when grouped away. | [default to undefined]
**hero_ids** | **Array&lt;number&gt;** | The ascending hero id pair that shared the lane, or empty when grouped away. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [default to undefined]
**matches_played** | **number** | Lane matchups behind the row, counted at its *first* sample. This is what &#x60;min_matches&#x60; and &#x60;max_matches&#x60; filter on, so it does not move when the requested time range changes; read &#x60;sample_matches&#x60; for what any individual point rests on. | [default to undefined]
**net_worth_diff** | **Array&lt;number&gt;** | Mean souls the duo is ahead by at the matching entry of &#x60;sample_times_s&#x60;. Negative means behind. Same length as &#x60;sample_times_s&#x60;. | [default to undefined]
**net_worth_diff_std** | **Array&lt;number&gt;** | Population standard deviation of the lead across the counted matchups, at the matching entry of &#x60;sample_times_s&#x60;. Same length as &#x60;sample_times_s&#x60;.  Spread between individual games, not uncertainty about the mean: it stays wide however many matchups are counted, because lane outcomes genuinely differ that much. | [default to undefined]
**sample_matches** | **Array&lt;number&gt;** | How many lane matchups were still running at the matching entry of &#x60;sample_times_s&#x60;. Falls off towards the end of the curve as shorter matches drop out. | [default to undefined]
**sample_times_s** | **Array&lt;number&gt;** | Seconds into the match each entry of the curves was sampled at, ascending. | [default to undefined]
**stats** | [**{ [key: string]: LaneStatCurve; }**](LaneStatCurve.md) | A curve per stat named in &#x60;stats&#x60;. Empty unless the parameter was set. | [default to undefined]

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
    sample_matches,
    sample_times_s,
    stats,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
