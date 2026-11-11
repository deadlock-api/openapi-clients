# PlayerClusterMonth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **number** | The server cluster the matches were played on. | [default to undefined]
**datacenter** | **string** | Datacenter(s) of the cluster\&#39;s servers, e.g. &#x60;fra2&#x60;; comma-separated if the cluster spans several. &#x60;null&#x60; if the cluster has not been seen in a replay yet. | [optional] [default to undefined]
**matches** | **number** | Number of the player\&#39;s matches on this cluster in this month. | [default to undefined]
**month** | **number** | Unix timestamp of the first day of the month (UTC). | [default to undefined]
**region** | **string** | Region of the cluster\&#39;s servers, e.g. &#x60;eu_west&#x60; or &#x60;us_north_central&#x60;. &#x60;null&#x60; if the cluster has not been seen in a replay yet. | [optional] [default to undefined]

## Example

```typescript
import { PlayerClusterMonth } from 'deadlock_api_client';

const instance: PlayerClusterMonth = {
    cluster_id,
    datacenter,
    matches,
    month,
    region,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
