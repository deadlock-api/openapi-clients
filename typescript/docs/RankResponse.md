# RankResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge** | **number** | Rank badge, &#x60;tier * 10 + subrank&#x60;. &#x60;0&#x60; when no recent ranked match reports a rank. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [default to undefined]
**rank** | **number** | Rank tier, &#x60;0&#x60; when unknown. | [default to undefined]
**subrank** | **number** | Sub-rank within the tier, &#x60;0&#x60; when unknown. | [default to undefined]

## Example

```typescript
import { RankResponse } from 'deadlock_api_client';

const instance: RankResponse = {
    badge,
    rank,
    subrank,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
