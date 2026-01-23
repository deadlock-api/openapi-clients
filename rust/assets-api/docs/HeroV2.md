# HeroV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | 
**class_name** | **String** |  | 
**name** | **String** |  | 
**description** | [**models::HeroDescriptionV2**](HeroDescriptionV2.md) |  | 
**item_draft_weights** | Option<**std::collections::HashMap<String, f64>**> |  | [optional]
**player_selectable** | **bool** |  | 
**disabled** | **bool** |  | 
**in_development** | **bool** |  | 
**needs_testing** | **bool** |  | 
**assigned_players_only** | **bool** |  | 
**tags** | Option<**Vec<String>**> |  | [optional]
**gun_tag** | Option<**String**> |  | [optional]
**hideout_rich_presence** | Option<**String**> |  | [optional]
**hero_type** | Option<[**models::HeroTypeV2**](HeroTypeV2.md)> |  | [optional]
**prerelease_only** | Option<**bool**> |  | [optional]
**limited_testing** | **bool** |  | 
**complexity** | **i32** |  | 
**skin** | **i32** |  | 
**images** | [**models::HeroImagesV2**](HeroImagesV2.md) |  | 
**items** | **std::collections::HashMap<String, String>** |  | 
**starting_stats** | [**models::HeroStartingStatsV2**](HeroStartingStatsV2.md) |  | 
**item_slot_info** | [**std::collections::HashMap<String, models::RawHeroItemSlotInfoValueV2>**](RawHeroItemSlotInfoValueV2.md) |  | 
**physics** | [**models::HeroPhysicsV2**](HeroPhysicsV2.md) |  | 
**colors** | [**models::HeroColorsV2**](HeroColorsV2.md) |  | 
**shop_stat_display** | [**models::HeroShopStatDisplayV2**](HeroShopStatDisplayV2.md) |  | 
**cost_bonuses** | Option<[**std::collections::HashMap<String, Vec<models::RawHeroMapModCostBonusesV2>>**](Vec.md)> |  | [optional]
**stats_display** | [**models::RawHeroStatsDisplayV2**](RawHeroStatsDisplayV2.md) |  | 
**hero_stats_ui** | [**models::RawHeroStatsUiv2**](RawHeroStatsUIV2.md) |  | 
**level_info** | [**std::collections::HashMap<String, models::HeroLevelInfoV2>**](HeroLevelInfoV2.md) |  | 
**scaling_stats** | [**std::collections::HashMap<String, models::RawHeroScalingStatV2>**](RawHeroScalingStatV2.md) |  | 
**purchase_bonuses** | [**std::collections::HashMap<String, Vec<models::RawHeroPurchaseBonusV2>>**](Vec.md) |  | 
**standard_level_up_upgrades** | **std::collections::HashMap<String, f64>** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


