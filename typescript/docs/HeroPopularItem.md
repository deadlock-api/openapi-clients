# HeroPopularItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **string** |  | [default to undefined]
**item_id** | **number** | Item id, derived from &#x60;class_name&#x60; like &#x60;/v2/items&#x60; ids. | [default to undefined]
**pick_pct** | **number** | Pick rate in percent (0-100). | [default to undefined]
**winrate_pct** | **number** | Win rate in percent (0-100). | [default to undefined]

## Example

```typescript
import { HeroPopularItem } from 'deadlock_api_client';

const instance: HeroPopularItem = {
    class_name,
    item_id,
    pick_pct,
    winrate_pct,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
