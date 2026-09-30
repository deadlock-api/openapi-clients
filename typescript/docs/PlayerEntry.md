# PlayerEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **number** |  | [default to undefined]
**badge** | **number** | &#x60;rank&#x60; and &#x60;peak_rank&#x60; sorts only: the rank badge the progress in &#x60;value&#x60; falls in, &#x60;0&#x60; when the player has no ranked match in range. Omitted for every other sort. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional] [default to undefined]
**badge_progress** | **number** | &#x60;rank&#x60; and &#x60;peak_rank&#x60; sorts only: progress points into &#x60;badge&#x60;. A subrank spans 1000 points, the sixth of a tier 2000. &#x60;null&#x60; in Eternus, whose subranks are percentile cuts rather than point spans, and when the player has no ranked match in range. | [optional] [default to undefined]
**matches** | **number** |  | [default to undefined]
**rank** | **number** |  | [default to undefined]
**value** | **number** |  | [default to undefined]

## Example

```typescript
import { PlayerEntry } from 'deadlock_api_client';

const instance: PlayerEntry = {
    account_id,
    badge,
    badge_progress,
    matches,
    rank,
    value,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
