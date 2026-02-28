# AbilityV2

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
**weapon_info** | Option<[**models::RawItemWeaponInfoV2**](RawItemWeaponInfoV2.md)> |  | [optional]
**r#type** | Option<**Type**> |  (enum: ability) | [optional][default to Ability]
**grant_ammo_on_cast** | Option<**bool**> |  | [optional]
**behaviours** | Option<**Vec<String>**> |  | [optional]
**description** | [**models::AbilityDescriptionV2**](AbilityDescriptionV2.md) |  | 
**tooltip_details** | Option<[**models::AbilityTooltipDetailsV2**](AbilityTooltipDetailsV2.md)> |  | [optional]
**upgrades** | Option<[**Vec<models::RawAbilityUpgradeV2>**](RawAbilityUpgradeV2.md)> |  | [optional]
**ability_type** | Option<[**models::AbilityTypeV2**](AbilityTypeV2.md)> |  | [optional]
**boss_damage_scale** | Option<**f64**> |  | [optional]
**dependant_abilities** | Option<**Vec<String>**> |  | [optional]
**videos** | Option<[**models::AbilityVideosV2**](AbilityVideosV2.md)> |  | [optional]
**dependent_abilities** | Option<[**std::collections::HashMap<String, models::AbilityV2DependentAbilitiesValue>**](AbilityV2DependentAbilitiesValue.md)> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


