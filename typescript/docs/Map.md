# ModelMap

The `/v1/assets/map` response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**images** | [**MapImages**](MapImages.md) |  | [default to undefined]
**objective_positions** | [**{ [key: string]: ObjectivePosition; }**](ObjectivePosition.md) |  | [default to undefined]
**radius** | **number** |  | [default to undefined]
**zipline_paths** | [**Array&lt;ZiplanePath&gt;**](ZiplanePath.md) |  | [default to undefined]

## Example

```typescript
import { ModelMap } from 'deadlock_api_client';

const instance: ModelMap = {
    images,
    objective_positions,
    radius,
    zipline_paths,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
