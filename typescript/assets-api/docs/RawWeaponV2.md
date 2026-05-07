# RawWeaponV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **string** |  | [default to undefined]
**start_trained** | **boolean** |  | [optional] [default to undefined]
**image** | **string** |  | [optional] [default to undefined]
**update_time** | **number** |  | [optional] [default to undefined]
**properties** | [**{ [key: string]: RawItemPropertyV2; }**](RawItemPropertyV2.md) |  | [optional] [default to undefined]
**weapon_info** | [**RawWeaponInfoV2**](RawWeaponInfoV2.md) |  | [optional] [default to undefined]
**css_class** | **string** |  | [optional] [default to undefined]
**type** | **string** |  | [optional] [default to TypeEnum_Weapon]
**crosshair_css_class** | **string** |  | [optional] [default to undefined]
**use_custom_crosshair_settings** | **boolean** |  | [optional] [default to undefined]
**custom_crosshair_settings** | [**RawCustomCrosshairSettingsV2**](RawCustomCrosshairSettingsV2.md) |  | [optional] [default to undefined]

## Example

```typescript
import { RawWeaponV2 } from 'assets_deadlock_api_client';

const instance: RawWeaponV2 = {
    class_name,
    start_trained,
    image,
    update_time,
    properties,
    weapon_info,
    css_class,
    type,
    crosshair_css_class,
    use_custom_crosshair_settings,
    custom_crosshair_settings,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
