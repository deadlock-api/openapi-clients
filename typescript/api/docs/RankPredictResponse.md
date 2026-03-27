# RankPredictResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge** | **number** | See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [default to undefined]
**raw_score** | **number** | Raw model output (float index into badge space) | [default to undefined]
**matches_used** | **number** | Number of recent matches used for the prediction | [default to undefined]

## Example

```typescript
import { RankPredictResponse } from 'deadlock_api_client';

const instance: RankPredictResponse = {
    badge,
    raw_score,
    matches_used,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
