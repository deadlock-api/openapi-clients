# WeaponV2Output


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
**properties** | [**{ [key: string]: ItemPropertyV2Output; }**](ItemPropertyV2Output.md) |  | [optional] [default to undefined]
**weapon_info** | [**RawWeaponInfoV2Output**](RawWeaponInfoV2Output.md) |  | [optional] [default to undefined]
**type** | **string** |  | [optional] [default to TypeEnum_Weapon]

## Example

```typescript
import { WeaponV2Output } from 'assets-deadlock-api-client';

const instance: WeaponV2Output = {
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
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
