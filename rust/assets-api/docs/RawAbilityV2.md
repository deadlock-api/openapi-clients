# RawAbilityV2

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
**r#type** | Option<**Type**> |  (enum: ability) | [optional][default to Ability]
**behaviour_bits** | Option<**String**> |  | [optional]
**upgrades** | [**Vec<models::RawAbilityUpgradeV2>**](RawAbilityUpgradeV2.md) |  | 
**ability_type** | Option<[**models::AbilityTypeV2**](AbilityTypeV2.md)> |  | [optional]
**boss_damage_scale** | Option<**f64**> |  | [optional]
**dependant_abilities** | Option<**Vec<String>**> |  | [optional]
**video** | Option<**String**> |  | [optional]
**tooltip_details** | Option<[**models::RawAbilityV2TooltipDetails**](RawAbilityV2TooltipDetails.md)> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


