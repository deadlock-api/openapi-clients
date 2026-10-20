# AnalyticsAbilityOrderTreeNode

One node of the ability order tree: the players whose upgrade order starts with `abilities`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abilities** | **Array&lt;number&gt;** | The order prefix: one entry per ability point spent, unlocks included. Its parent node is the prefix one entry shorter. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [default to undefined]
**avg_upgrade_time_s** | **number** | Average game time (in seconds) at which the last upgrade in &#x60;abilities&#x60; was bought. | [default to undefined]
**losses** | **number** |  | [default to undefined]
**matches** | **number** |  | [default to undefined]
**players** | **number** | Distinct players, counted exactly. | [default to undefined]
**total_assists** | **number** |  | [default to undefined]
**total_deaths** | **number** |  | [default to undefined]
**total_kills** | **number** |  | [default to undefined]
**wins** | **number** |  | [default to undefined]

## Example

```typescript
import { AnalyticsAbilityOrderTreeNode } from 'deadlock_api_client';

const instance: AnalyticsAbilityOrderTreeNode = {
    abilities,
    avg_upgrade_time_s,
    losses,
    matches,
    players,
    total_assists,
    total_deaths,
    total_kills,
    wins,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
