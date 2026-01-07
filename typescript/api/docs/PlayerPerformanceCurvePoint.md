# PlayerPerformanceCurvePoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assists_avg** | **number** | Average assists at this timestamp | [default to undefined]
**assists_std** | **number** | Standard deviation of assists at this timestamp | [default to undefined]
**deaths_avg** | **number** | Average deaths at this timestamp | [default to undefined]
**deaths_std** | **number** | Standard deviation of deaths at this timestamp | [default to undefined]
**kills_avg** | **number** | Average kills at this timestamp | [default to undefined]
**kills_std** | **number** | Standard deviation of kills at this timestamp | [default to undefined]
**net_worth_avg** | **number** | Average net worth at this timestamp | [default to undefined]
**net_worth_std** | **number** | Standard deviation of net worth at this timestamp | [default to undefined]
**relative_timestamp** | **number** | Percentage interval of match duration (0%, 5%, 10%, ..., 100%) | [default to undefined]

## Example

```typescript
import { PlayerPerformanceCurvePoint } from 'deadlock_api_client';

const instance: PlayerPerformanceCurvePoint = {
    assists_avg,
    assists_std,
    deaths_avg,
    deaths_std,
    kills_avg,
    kills_std,
    net_worth_avg,
    net_worth_std,
    relative_timestamp,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
