# LaneMatchupStat

One requested stat, read at `sample_time_s` and averaged over the matchups that reached it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diff** | **number** | Mean of the duo\&#39;s combined value minus the enemy duo\&#39;s. Negative means behind. | [default to undefined]
**diff_std** | **number** | Population standard deviation of &#x60;diff&#x60; across the counted matchups. | [default to undefined]
**value** | **number** | Mean of the duo\&#39;s combined value, summed over its two players. | [default to undefined]
**value_std** | **number** | Population standard deviation of &#x60;value&#x60; across the counted matchups. | [default to undefined]

## Example

```typescript
import { LaneMatchupStat } from 'deadlock_api_client';

const instance: LaneMatchupStat = {
    diff,
    diff_std,
    value,
    value_std,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
