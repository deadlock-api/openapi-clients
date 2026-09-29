# HeroPopularItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**early_game** | [**Array&lt;HeroPopularItem&gt;**](HeroPopularItem.md) |  | [default to undefined]
**late_game** | [**Array&lt;HeroPopularItem&gt;**](HeroPopularItem.md) |  | [default to undefined]
**mid_game** | [**Array&lt;HeroPopularItem&gt;**](HeroPopularItem.md) |  | [default to undefined]
**timestamp** | **number** | Unix timestamp (seconds) at which Valve generated the data. | [optional] [default to undefined]

## Example

```typescript
import { HeroPopularItems } from 'deadlock_api_client';

const instance: HeroPopularItems = {
    early_game,
    late_game,
    mid_game,
    timestamp,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
