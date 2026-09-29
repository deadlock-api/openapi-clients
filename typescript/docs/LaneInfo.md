# LaneInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | [**Color**](Color.md) | Absent for unused lane slots (build 6711+). | [optional] [default to undefined]
**css_class** | **string** |  | [optional] [default to undefined]
**is_enemy_lane** | **boolean** |  | [default to undefined]
**lane_name** | **string** | Localized lane name. Unused lane slots are named &#x60;Unused&#x60;. | [default to undefined]
**minimap_color** | [**Color**](Color.md) | Build 6711+. | [optional] [default to undefined]
**minimap_zipline_color_override** | [**Color**](Color.md) | Only present up to build 6701. | [optional] [default to undefined]
**objective_color** | [**Color**](Color.md) | Only present up to build 6701. | [optional] [default to undefined]

## Example

```typescript
import { LaneInfo } from 'deadlock_api_client';

const instance: LaneInfo = {
    color,
    css_class,
    is_enemy_lane,
    lane_name,
    minimap_color,
    minimap_zipline_color_override,
    objective_color,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
