# WeaponV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [default to undefined]
**class_name** | **string** |  | [default to undefined]
**name** | **string** |  | [default to undefined]
**start_trained** | **boolean** |  | [optional] [default to undefined]
**image** | **string** |  | [optional] [default to undefined]
**image_webp** | **string** |  | [optional] [default to undefined]
**hero** | **number** |  | [optional] [default to undefined]
**heroes** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**update_time** | **number** |  | [optional] [default to undefined]
**properties** | [**{ [key: string]: ItemPropertyV2; }**](ItemPropertyV2.md) |  | [optional] [default to undefined]
**weapon_info** | [**WeaponInfoV2**](WeaponInfoV2.md) |  | [optional] [default to undefined]
**type** | **string** |  | [optional] [default to TypeEnum_Weapon]
**crosshair_css_class** | **string** |  | [optional] [default to undefined]
**use_custom_crosshair_settings** | **boolean** |  | [optional] [default to undefined]
**custom_crosshair_settings** | [**RawCustomCrosshairSettingsV2**](RawCustomCrosshairSettingsV2.md) |  | [optional] [default to undefined]

## Example

```typescript
import { WeaponV2 } from 'assets_deadlock_api_client';

const instance: WeaponV2 = {
    id,
    class_name,
    name,
    start_trained,
    image,
    image_webp,
    hero,
    heroes,
    update_time,
    properties,
    weapon_info,
    type,
    crosshair_css_class,
    use_custom_crosshair_settings,
    custom_crosshair_settings,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
