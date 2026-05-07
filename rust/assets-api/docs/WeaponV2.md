# WeaponV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | 
**class_name** | **String** |  | 
**name** | **String** |  | 
**start_trained** | Option<**bool**> |  | [optional]
**image** | Option<**String**> |  | [optional]
**image_webp** | Option<**String**> |  | [optional]
**hero** | Option<**i32**> |  | [optional]
**heroes** | Option<**Vec<i32>**> |  | [optional]
**update_time** | Option<**i32**> |  | [optional]
**properties** | Option<[**std::collections::HashMap<String, models::ItemPropertyV2>**](ItemPropertyV2.md)> |  | [optional]
**weapon_info** | Option<[**models::WeaponInfoV2**](WeaponInfoV2.md)> |  | [optional]
**r#type** | Option<**Type**> |  (enum: weapon) | [optional][default to Weapon]
**crosshair_css_class** | Option<**String**> |  | [optional]
**use_custom_crosshair_settings** | Option<**bool**> |  | [optional]
**custom_crosshair_settings** | Option<[**models::RawCustomCrosshairSettingsV2**](RawCustomCrosshairSettingsV2.md)> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


