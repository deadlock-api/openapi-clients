# RankDistributionEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge** | **number** | Rank badge, &#x60;tier * 10 + subrank&#x60;. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [default to undefined]
**players** | **number** | Number of players whose rank at the end of their latest ranked match in the filtered range is this badge. | [default to undefined]
**rank** | **number** | Rank tier. | [default to undefined]
**subrank** | **number** | Sub-rank within the tier. | [default to undefined]

## Example

```typescript
import { RankDistributionEntry } from 'deadlock_api_client';

const instance: RankDistributionEntry = {
    badge,
    players,
    rank,
    subrank,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
