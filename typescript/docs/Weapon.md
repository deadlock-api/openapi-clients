# Weapon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **string** |  | [default to undefined]
**crosshair_css_class** | **string** |  | [optional] [default to undefined]
**custom_crosshair_settings** | [**RawCustomCrosshairSettings**](RawCustomCrosshairSettings.md) |  | [optional] [default to undefined]
**hero** | **number** |  | [optional] [default to undefined]
**heroes** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**id** | **number** |  | [default to undefined]
**image** | **string** |  | [optional] [default to undefined]
**image_webp** | **string** |  | [optional] [default to undefined]
**name** | **string** |  | [default to undefined]
**properties** | [**{ [key: string]: ItemProperty; }**](ItemProperty.md) |  | [optional] [default to undefined]
**start_trained** | **boolean** |  | [optional] [default to undefined]
**type** | [**ItemType**](ItemType.md) |  | [default to undefined]
**update_time** | **number** |  | [optional] [default to undefined]
**use_custom_crosshair_settings** | **boolean** |  | [optional] [default to undefined]
**weapon_info** | [**WeaponInfo**](WeaponInfo.md) |  | [optional] [default to undefined]

## Example

```typescript
import { Weapon } from 'deadlock_api_client';

const instance: Weapon = {
    class_name,
    crosshair_css_class,
    custom_crosshair_settings,
    hero,
    heroes,
    id,
    image,
    image_webp,
    name,
    properties,
    start_trained,
    type,
    update_time,
    use_custom_crosshair_settings,
    weapon_info,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
