# MMRHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **number** |  | [default to undefined]
**division** | **number** | Extracted from the rank the division (rank // 10) | [default to undefined]
**division_tier** | **number** | Extracted from the rank the division tier (rank % 10) | [default to undefined]
**match_id** | **number** |  | [default to undefined]
**player_score** | **number** | Contiguous index of the rank (1-66), derived from &#x60;rank&#x60; | [default to undefined]
**rank** | **number** | The Player Rank (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [default to undefined]
**start_time** | **number** | Start time of the match | [default to undefined]

## Example

```typescript
import { MMRHistory } from 'deadlock_api_client';

const instance: MMRHistory = {
    account_id,
    division,
    division_tier,
    match_id,
    player_score,
    rank,
    start_time,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
