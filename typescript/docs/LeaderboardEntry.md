# LeaderboardEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **string** | The account name of the player. | [optional] [default to undefined]
**possible_account_ids** | **Array&lt;number&gt;** | The possible account IDs of the player. **CAVEAT: This is not always correct, as Steam account names are not unique.** | [default to undefined]
**rank** | **number** | The player\&#39;s place on the leaderboard, starting at 1. Players can share a place, and the following places are then skipped (1, 2, 2, 4). Not a rank badge. | [optional] [default to undefined]
**top_hero_ids** | **Array&lt;number&gt;** | The top hero IDs of the player, as the game sends them. Since 2026-07-31 the game leaves them empty for about half of the entries. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [default to undefined]

## Example

```typescript
import { LeaderboardEntry } from 'deadlock_api_client';

const instance: LeaderboardEntry = {
    account_name,
    possible_account_ids,
    rank,
    top_hero_ids,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
