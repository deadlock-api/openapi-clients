# UpgradeV2

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
**properties** | Option<[**std::collections::HashMap<String, models::UpgradePropertyV2>**](UpgradePropertyV2.md)> |  | [optional]
**weapon_info** | Option<[**models::RawItemWeaponInfoV2**](RawItemWeaponInfoV2.md)> |  | [optional]
**r#type** | Option<**String**> |  | [optional][default to Upgrade]
**shop_image** | Option<**String**> |  | [optional]
**shop_image_webp** | Option<**String**> |  | [optional]
**shop_image_small** | Option<**String**> |  | [optional]
**shop_image_small_webp** | Option<**String**> |  | [optional]
**item_slot_type** | [**models::ItemSlotTypeV2**](ItemSlotTypeV2.md) |  | 
**item_tier** | [**models::ItemTierV2**](ItemTierV2.md) |  | 
**disabled** | Option<**bool**> |  | [optional]
**description** | Option<[**models::UpgradeDescriptionV2**](UpgradeDescriptionV2.md)> |  | [optional]
**activation** | [**models::RawAbilityActivationV2**](RawAbilityActivationV2.md) |  | 
**imbue** | Option<[**models::RawAbilityImbueV2**](RawAbilityImbueV2.md)> |  | [optional]
**component_items** | Option<**Vec<String>**> |  | [optional]
**tooltip_sections** | Option<[**Vec<models::UpgradeTooltipSectionV2>**](UpgradeTooltipSectionV2.md)> |  | [optional]
**is_active_item** | **bool** |  | [readonly]
**shopable** | **bool** |  | [readonly]
**cost** | Option<**i32**> |  | [readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


