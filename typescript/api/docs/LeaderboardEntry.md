# LeaderboardEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **string** | The account name of the player. | [optional] [default to undefined]
**badge_level** | **number** | The badge level of the player. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] [default to undefined]
**possible_account_ids** | **Array&lt;number&gt;** | The possible account IDs of the player. **CAVEAT: This is not always correct, as Steam account names are not unique.** | [optional] [default to undefined]
**rank** | **number** | The rank of the player. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] [default to undefined]
**ranked_rank** | **number** | The ranked rank of the player. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] [default to undefined]
**ranked_subrank** | **number** | The ranked subrank of the player. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] [default to undefined]
**top_hero_ids** | **Array&lt;number&gt;** | The top hero IDs of the player. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] [default to undefined]

## Example

```typescript
import { LeaderboardEntry } from 'deadlock-api-client';

const instance: LeaderboardEntry = {
    account_name,
    badge_level,
    possible_account_ids,
    rank,
    ranked_rank,
    ranked_subrank,
    top_hero_ids,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
