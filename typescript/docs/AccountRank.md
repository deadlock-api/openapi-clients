# AccountRank


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge** | **number** | Rank badge, &#x60;tier * 10 + subrank&#x60;, including the progress the last ranked match awarded. Eternus subranks are percentile-based and refreshed daily by Valve, so within Eternus this is the badge the player entered their latest ranked match with. &#x60;0&#x60; when no recent ranked match reports a rank. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [default to undefined]
**last_match** | [**LastRankedMatch**](LastRankedMatch.md) | Rank metadata of the ranked match the badge was read from. &#x60;null&#x60; when none of the player\&#39;s recent ranked matches reports a rank. | [optional] [default to undefined]
**rank** | **number** | Rank tier, &#x60;0&#x60; when unknown. | [default to undefined]
**subrank** | **number** | Sub-rank within the tier, &#x60;0&#x60; when unknown. | [default to undefined]
**account_id** | **number** | The players &#x60;SteamID3&#x60; | [default to undefined]

## Example

```typescript
import { AccountRank } from 'deadlock_api_client';

const instance: AccountRank = {
    badge,
    last_match,
    rank,
    subrank,
    account_id,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
