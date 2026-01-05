# NetWorthCurvePoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg** | **number** | Average net worth at this timestamp | [default to undefined]
**percentile1** | **number** | 1st percentile net worth | [default to undefined]
**percentile10** | **number** | 10th percentile net worth | [default to undefined]
**percentile25** | **number** | 25th percentile net worth | [default to undefined]
**percentile5** | **number** | 5th percentile net worth | [default to undefined]
**percentile50** | **number** | 50th percentile net worth | [default to undefined]
**percentile75** | **number** | 75th percentile net worth | [default to undefined]
**percentile90** | **number** | 90th percentile net worth | [default to undefined]
**percentile95** | **number** | 95th percentile net worth | [default to undefined]
**percentile99** | **number** | 99th percentile net worth | [default to undefined]
**relative_timestamp** | **number** | Percentage interval of match duration (0%, 5%, 10%, ..., 100%) | [default to undefined]
**std** | **number** | Standard deviation of net worth at this timestamp | [default to undefined]

## Example

```typescript
import { NetWorthCurvePoint } from 'deadlock_api_client';

const instance: NetWorthCurvePoint = {
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
    relative_timestamp,
    std,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
