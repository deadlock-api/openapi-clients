# FlashData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brightness** | **number** |  | [optional] [default to undefined]
**brightness_in_light_sensitivity_mode** | **number** |  | [optional] [default to undefined]
**color** | [**Color**](Color.md) | Flat flash color. From build 6711 on it is derived from the first &#x60;color_gradient&#x60; stop. | [default to undefined]
**color_gradient** | [**Array&lt;ColorGradientStop&gt;**](ColorGradientStop.md) | Color gradient over the flash\&#39;s lifetime (build 6711+). | [optional] [default to undefined]
**coverage** | **number** | Only present up to build 6701. | [optional] [default to undefined]
**duration** | **number** |  | [default to undefined]
**hardness** | **number** | Only present up to build 6701. | [optional] [default to undefined]

## Example

```typescript
import { FlashData } from 'deadlock_api_client';

const instance: FlashData = {
    brightness,
    brightness_in_light_sensitivity_mode,
    color,
    color_gradient,
    coverage,
    duration,
    hardness,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
