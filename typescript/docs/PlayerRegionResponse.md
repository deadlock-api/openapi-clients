# PlayerRegionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **number** |  | [default to undefined]
**history** | [**Array&lt;PlayerClusterMonth&gt;**](PlayerClusterMonth.md) | Matches per month and server cluster, newest month first. | [default to undefined]
**region** | **string** | The region the player played most matches in during their latest month with a known region. &#x60;null&#x60; if none of their matches has a known region. | [optional] [default to undefined]
**region_month** | **number** | Unix timestamp of the month &#x60;region&#x60; was taken from. | [optional] [default to undefined]

## Example

```typescript
import { PlayerRegionResponse } from 'deadlock_api_client';

const instance: PlayerRegionResponse = {
    account_id,
    history,
    region,
    region_month,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
