# ItemStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_buy_time_relative** | **number** | Average buy time as percentage of match duration | [default to undefined]
**avg_buy_time_s** | **number** | Average buy time in seconds (absolute) | [default to undefined]
**avg_sell_time_relative** | **number** | Average sell time as percentage of match duration (for items that were sold) | [default to undefined]
**avg_sell_time_s** | **number** | Average sell time in seconds (absolute, for items that were sold) | [default to undefined]
**bucket** | **number** |  | [default to undefined]
**item_id** | **number** | See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [default to undefined]
**losses** | **number** |  | [default to undefined]
**matches** | **number** |  | [default to undefined]
**players** | **number** |  | [default to undefined]
**wins** | **number** |  | [default to undefined]

## Example

```typescript
import { ItemStats } from 'deadlock_api_client';

const instance: ItemStats = {
    avg_buy_time_relative,
    avg_buy_time_s,
    avg_sell_time_relative,
    avg_sell_time_s,
    bucket,
    item_id,
    losses,
    matches,
    players,
    wins,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
