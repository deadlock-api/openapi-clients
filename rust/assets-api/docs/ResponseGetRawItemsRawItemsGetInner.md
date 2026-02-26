# ResponseGetRawItemsRawItemsGetInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **String** |  | 
**start_trained** | Option<**bool**> |  | [optional]
**image** | Option<**String**> |  | [optional]
**update_time** | Option<**i32**> |  | [optional]
**properties** | Option<[**std::collections::HashMap<String, models::RawItemPropertyV2>**](RawItemPropertyV2.md)> |  | [optional]
**weapon_info** | Option<[**models::RawItemWeaponInfoV2**](RawItemWeaponInfoV2.md)> |  | [optional]
**css_class** | Option<**String**> |  | [optional]
**r#type** | Option<**Type**> |  (enum: ability, weapon, upgrade) | [optional][default to Ability]
**behaviour_bits** | Option<**String**> |  | [optional]
**upgrades** | [**Vec<models::RawAbilityUpgradeV2>**](RawAbilityUpgradeV2.md) |  | 
**ability_type** | Option<[**models::AbilityTypeV2**](AbilityTypeV2.md)> |  | [optional]
**boss_damage_scale** | Option<**f64**> |  | [optional]
**dependant_abilities** | Option<**Vec<String>**> |  | [optional]
**video** | Option<**String**> |  | [optional]
**tooltip_details** | Option<[**models::RawAbilityV2TooltipDetails**](RawAbilityV2TooltipDetails.md)> |  | [optional]
**shop_image** | Option<**String**> |  | [optional]
**shop_image_small** | Option<**String**> |  | [optional]
**item_slot_type** | [**models::ItemSlotTypeV2**](ItemSlotTypeV2.md) |  | 
**item_tier** | [**models::ItemTierV2**](ItemTierV2.md) |  | 
**disabled** | Option<**bool**> |  | [optional]
**activation** | Option<[**models::RawAbilityActivationV2**](RawAbilityActivationV2.md)> |  | [optional]
**imbue** | Option<[**models::RawAbilityImbueV2**](RawAbilityImbueV2.md)> |  | [optional]
**component_items** | Option<**Vec<String>**> |  | [optional]
**tooltip_sections** | Option<[**Vec<models::RawUpgradeTooltipSectionV2>**](RawUpgradeTooltipSectionV2.md)> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


