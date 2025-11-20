# MapV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**radius** | **number** | The radius of the map. | [optional] [default to 10752]
**images** | [**MapImagesV1**](MapImagesV1.md) | The images of the map. | [default to undefined]
**objective_positions** | [**ObjectivePositionsV1**](ObjectivePositionsV1.md) |  | [readonly] [default to undefined]
**zipline_paths** | [**Array&lt;ZiplanePathV1&gt;**](ZiplanePathV1.md) | The ziplane paths of the map. Each path is a list of P0, P1, and P2 points, describing the cubic spline. | [default to undefined]

## Example

```typescript
import { MapV1 } from 'assets_deadlock_api_client';

const instance: MapV1 = {
    radius,
    images,
    objective_positions,
    zipline_paths,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
