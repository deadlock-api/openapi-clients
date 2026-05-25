# Upgrade

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation** | [**models::AbilityActivation**](AbilityActivation.md) |  | 
**class_name** | **String** |  | 
**component_items** | Option<**Vec<String>**> |  | [optional]
**cost** | Option<**u32**> |  | [optional]
**description** | Option<[**models::UpgradeDescription**](UpgradeDescription.md)> |  | [optional]
**disabled** | Option<**bool**> |  | [optional]
**hero** | Option<**u32**> |  | [optional]
**heroes** | Option<**Vec<u32>**> |  | [optional]
**id** | **u32** |  | 
**image** | Option<**String**> |  | [optional]
**image_webp** | Option<**String**> |  | [optional]
**imbue** | Option<[**models::AbilityImbue**](AbilityImbue.md)> |  | [optional]
**is_active_item** | **bool** |  | 
**item_slot_type** | [**models::ItemSlotType**](ItemSlotType.md) |  | 
**item_tier** | **u32** |  | 
**name** | **String** |  | 
**properties** | Option<[**std::collections::HashMap<String, models::UpgradeProperty>**](UpgradeProperty.md)> |  | [optional]
**shop_image** | Option<**String**> |  | [optional]
**shop_image_small** | Option<**String**> |  | [optional]
**shop_image_small_webp** | Option<**String**> |  | [optional]
**shop_image_webp** | Option<**String**> |  | [optional]
**shopable** | **bool** |  | 
**start_trained** | Option<**bool**> |  | [optional]
**tooltip_sections** | Option<[**Vec<models::UpgradeTooltipSection>**](UpgradeTooltipSection.md)> |  | [optional]
**r#type** | [**models::ItemType**](ItemType.md) |  | 
**update_time** | Option<**i64**> |  | [optional]
**upgrades** | Option<[**Vec<models::RawAbilityUpgrade>**](RawAbilityUpgrade.md)> |  | [optional]
**weapon_info** | Option<[**models::RawItemWeaponInfoInner**](RawItemWeaponInfoInner.md)> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


