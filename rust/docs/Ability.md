# Ability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ability_type** | Option<[**models::AbilityType**](AbilityType.md)> |  | [optional]
**behaviours** | Option<**Vec<String>**> |  | [optional]
**boss_damage_scale** | Option<**f64**> |  | [optional]
**class_name** | **String** |  | 
**dependant_abilities** | Option<**Vec<String>**> |  | [optional]
**dependent_abilities** | Option<[**std::collections::HashMap<String, models::DependantAbilities>**](DependantAbilities.md)> |  | [optional]
**description** | [**models::AbilityDescription**](AbilityDescription.md) |  | 
**grant_ammo_on_cast** | Option<**bool**> |  | [optional]
**hero** | Option<**u32**> |  | [optional]
**heroes** | Option<**Vec<u32>**> |  | [optional]
**id** | **u32** |  | 
**image** | Option<**String**> |  | [optional]
**image_webp** | Option<**String**> |  | [optional]
**name** | **String** |  | 
**properties** | Option<[**std::collections::HashMap<String, models::ItemProperty>**](ItemProperty.md)> |  | [optional]
**start_trained** | Option<**bool**> |  | [optional]
**tooltip_details** | Option<[**models::AbilityTooltipDetails**](AbilityTooltipDetails.md)> |  | [optional]
**r#type** | [**models::ItemType**](ItemType.md) |  | 
**update_time** | Option<**i64**> |  | [optional]
**upgrades** | Option<[**Vec<models::RawAbilityUpgrade>**](RawAbilityUpgrade.md)> |  | [optional]
**videos** | Option<[**models::AbilityVideos**](AbilityVideos.md)> |  | [optional]
**weapon_info** | Option<[**models::RawItemWeaponInfoInner**](RawItemWeaponInfoInner.md)> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


