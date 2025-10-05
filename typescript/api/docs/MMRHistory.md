# MMRHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **number** |  | [default to undefined]
**division** | **number** | Extracted from the rank the division (rank // 10) | [default to undefined]
**division_tier** | **number** | Extracted from the rank the division tier (rank % 10) | [default to undefined]
**match_id** | **number** |  | [default to undefined]
**player_score** | **number** | Player Score is the index for the rank array (internally used for the rank regression) | [default to undefined]
**rank** | **number** | The Player Rank. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [default to undefined]
**start_time** | **number** | Start time of the match | [default to undefined]

## Example

```typescript
import { MMRHistory } from 'deadlock-api-client';

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
