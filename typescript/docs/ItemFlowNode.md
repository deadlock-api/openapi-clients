# ItemFlowNode

A single item, aggregated within one column of the flow graph.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjusted_win_rate** | **number** | Win rate standardized to the stage\&#39;s net-worth-at-buy distribution, removing the \&quot;richer buyers win more\&quot; confound. See the endpoint description. | [default to undefined]
**avg_net_worth_at_buy** | **number** | Average net worth of buyers at the moment they bought this item (confound visibility). | [default to undefined]
**column** | **number** | The phase column (0-based) the item was bought in. | [default to undefined]
**item_id** | **number** | See more: &lt;https://api.deadlock-api.com/v1/assets/items&gt; | [default to undefined]
**losses** | **number** |  | [default to undefined]
**matches** | **number** |  | [default to undefined]
**players** | **number** |  | [default to undefined]
**total_assists** | **number** |  | [default to undefined]
**total_deaths** | **number** |  | [default to undefined]
**total_kills** | **number** |  | [default to undefined]
**wins** | **number** |  | [default to undefined]

## Example

```typescript
import { ItemFlowNode } from 'deadlock_api_client';

const instance: ItemFlowNode = {
    adjusted_win_rate,
    avg_net_worth_at_buy,
    column,
    item_id,
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
