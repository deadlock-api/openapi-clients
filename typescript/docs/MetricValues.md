# MetricValues

One metric\'s distribution over single matches. Every value is `null` (NaN) when no matching match has the metric, e.g. `first_permanent_buff_time_s` for matches before build 6712.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg** | **number** |  | [default to undefined]
**percentile1** | **number** |  | [default to undefined]
**percentile10** | **number** |  | [default to undefined]
**percentile25** | **number** |  | [default to undefined]
**percentile5** | **number** |  | [default to undefined]
**percentile50** | **number** |  | [default to undefined]
**percentile75** | **number** |  | [default to undefined]
**percentile90** | **number** |  | [default to undefined]
**percentile95** | **number** |  | [default to undefined]
**percentile99** | **number** |  | [default to undefined]
**std** | **number** |  | [default to undefined]

## Example

```typescript
import { MetricValues } from 'deadlock_api_client';

const instance: MetricValues = {
    avg,
    percentile1,
    percentile10,
    percentile25,
    percentile5,
    percentile50,
    percentile75,
    percentile90,
    percentile95,
    percentile99,
    std,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
