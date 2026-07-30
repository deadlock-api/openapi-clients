# LeaderboardEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **string** | The account name of the player. | [optional] [default to undefined]
**possible_account_ids** | **Array&lt;number&gt;** | The possible account IDs of the player. **CAVEAT: This is not always correct, as Steam account names are not unique.** | [optional] [default to undefined]
**rank** | **number** | The rank of the player (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional] [default to undefined]
**top_hero_ids** | **Array&lt;number&gt;** | The top hero IDs of the player. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [optional] [default to undefined]

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
