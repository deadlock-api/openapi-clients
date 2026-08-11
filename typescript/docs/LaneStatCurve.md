# LaneStatCurve

One requested stat\'s curve. All four arrays line up with `sample_times_s`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diff** | **Array&lt;number&gt;** | Mean of the duo\&#39;s combined value minus the enemy duo\&#39;s. Negative means behind. | [default to undefined]
**diff_std** | **Array&lt;number&gt;** | Population standard deviation of &#x60;diff&#x60; across the counted matchups. | [default to undefined]
**value** | **Array&lt;number&gt;** | Mean of the duo\&#39;s combined value, summed over its two players. | [default to undefined]
**value_std** | **Array&lt;number&gt;** | Population standard deviation of &#x60;value&#x60; across the counted matchups. | [default to undefined]

## Example

```typescript
import { LaneStatCurve } from 'deadlock_api_client';

const instance: LaneStatCurve = {
    diff,
    diff_std,
    value,
    value_std,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
