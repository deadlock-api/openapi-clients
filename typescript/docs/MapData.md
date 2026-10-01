# MapData

The `/v1/assets/map` response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**MapEntities**](MapEntities.md) | Interactable map entities; only for builds whose assets were built with the map entity extraction. | [optional] [default to undefined]
**images** | [**MapImages**](MapImages.md) |  | [default to undefined]
**neutral_camps** | [**Array&lt;NeutralCamp&gt;**](NeutralCamp.md) | Neutral camps (build 6711+). | [optional] [default to undefined]
**objective_positions** | [**{ [key: string]: ObjectivePosition; }**](ObjectivePosition.md) |  | [default to undefined]
**radius** | **number** |  | [default to undefined]
**zipline_paths** | [**Array&lt;ZiplanePath&gt;**](ZiplanePath.md) |  | [default to undefined]

## Example

```typescript
import { MapData } from 'deadlock_api_client';

const instance: MapData = {
    entities,
    images,
    neutral_camps,
    objective_positions,
    radius,
    zipline_paths,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
