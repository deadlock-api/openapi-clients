# PlayerCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **number** |  | [default to undefined]
**ranked_badge_level** | **number** | See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] [default to undefined]
**ranked_rank** | **number** | See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] [default to undefined]
**ranked_subrank** | **number** | See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] [default to undefined]
**slots** | [**Array&lt;PlayerCardSlot&gt;**](PlayerCardSlot.md) |  | [default to undefined]

## Example

```typescript
import { PlayerCard } from 'deadlock_api_client';

const instance: PlayerCard = {
    account_id,
    ranked_badge_level,
    ranked_rank,
    ranked_subrank,
    slots,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
