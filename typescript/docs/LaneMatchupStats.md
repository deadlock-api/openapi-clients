# LaneMatchupStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_lane** | **number** | The lane the matchup was played in. See the &#x60;lane_info&#x60; array of &lt;https://api.deadlock-api.com/v1/assets/generic-data&gt;. | [default to undefined]
**enemy_hero_ids** | **Array&lt;number&gt;** | The ascending hero id pair they laned against. | [default to undefined]
**hero_ids** | **Array&lt;number&gt;** | The ascending hero id pair that shared the lane. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [default to undefined]
**matches_played** | **number** | The total number of lane matchups between &#x60;hero_ids&#x60; and &#x60;enemy_hero_ids&#x60; in this lane. | [default to undefined]
**net_worth_diff_9min** | **number** | Mean souls the duo is ahead by 9 minutes in, against that duo. Negative means behind. &#x60;0&#x60; when no counted matchup had net-worth samples for all four players. | [default to undefined]
**net_worth_matches** | **number** | How many of &#x60;matches_played&#x60; carried net-worth samples for all four players. | [default to undefined]
**wins** | **number** | The number of matches &#x60;hero_ids&#x60; won against &#x60;enemy_hero_ids&#x60; in this lane. | [default to undefined]

## Example

```typescript
import { LaneMatchupStats } from 'deadlock_api_client';

const instance: LaneMatchupStats = {
    assigned_lane,
    enemy_hero_ids,
    hero_ids,
    matches_played,
    net_worth_diff_9min,
    net_worth_matches,
    wins,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
