# Settings

Crosshair convars. Anything not given keeps the game\'s default.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color_b** | **number** |  | [optional] [default to 255]
**color_g** | **number** |  | [optional] [default to 255]
**color_r** | **number** |  | [optional] [default to 255]
**dot_opacity** | **number** | 0 to 1. | [optional] [default to 0.7]
**dot_outline_border** | **number** |  | [optional] [default to 2]
**dot_outline_gap** | **number** |  | [optional] [default to 0]
**dot_outline_opacity** | **number** | 0 to 1. | [optional] [default to 0.7]
**dot_size** | **number** |  | [optional] [default to 4]
**outline_color_b** | **number** |  | [optional] [default to 0]
**outline_color_g** | **number** |  | [optional] [default to 0]
**outline_color_r** | **number** |  | [optional] [default to 0]
**pip_gap** | **number** |  | [optional] [default to 4]
**pip_gap_static** | **boolean** | Keep the pips at a fixed distance instead of spreading them with weapon spread. | [optional] [default to false]
**pip_height** | **number** |  | [optional] [default to 16]
**pip_opacity** | **number** | 0 to 1. | [optional] [default to 0.5]
**pip_outline_border** | **number** |  | [optional] [default to 1]
**pip_outline_gap** | **number** |  | [optional] [default to 0]
**pip_outline_opacity** | **number** | 0 to 1. | [optional] [default to 0.7]
**pip_width** | **number** |  | [optional] [default to 2]
**themed** | **boolean** | Use the hero\&#39;s own crosshair instead of these settings. | [optional] [default to false]

## Example

```typescript
import { Settings } from 'deadlock_api_client';

const instance: Settings = {
    color_b,
    color_g,
    color_r,
    dot_opacity,
    dot_outline_border,
    dot_outline_gap,
    dot_outline_opacity,
    dot_size,
    outline_color_b,
    outline_color_g,
    outline_color_r,
    pip_gap,
    pip_gap_static,
    pip_height,
    pip_opacity,
    pip_outline_border,
    pip_outline_gap,
    pip_outline_opacity,
    pip_width,
    themed,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
