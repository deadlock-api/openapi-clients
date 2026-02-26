# RawHeroV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | 
**class_name** | **String** |  | 
**item_draft_weights** | Option<**std::collections::HashMap<String, f64>**> |  | [optional]
**player_selectable** | **bool** |  | 
**disabled** | **bool** |  | 
**in_development** | **bool** |  | 
**needs_testing** | **bool** |  | 
**assigned_players_only** | **bool** |  | 
**available_in_hero_labs** | Option<**bool**> |  | [optional]
**prerelease_only** | Option<**bool**> |  | [optional]
**limited_testing** | **bool** |  | 
**complexity** | **i32** |  | 
**skin** | **i32** |  | 
**starting_stats** | [**models::RawHeroStartingStatsV2**](RawHeroStartingStatsV2.md) |  | 
**icon_hero_card** | Option<**String**> |  | [optional]
**icon_image_small** | Option<**String**> |  | [optional]
**minimap_image** | Option<**String**> |  | [optional]
**name_image** | Option<**String**> |  | [optional]
**hero_card_critical** | Option<**String**> |  | [optional]
**hero_card_gloat** | Option<**String**> |  | [optional]
**top_bar_vertical_image** | Option<**String**> |  | [optional]
**tags** | Option<**Vec<String>**> |  | [optional]
**gun_tag** | Option<**String**> |  | [optional]
**hideout_rich_presence** | Option<**String**> |  | [optional]
**hero_type** | Option<[**models::HeroTypeV2**](HeroTypeV2.md)> |  | [optional]
**shop_stat_display** | [**models::RawHeroShopStatDisplayV2**](RawHeroShopStatDisplayV2.md) |  | 
**cost_bonuses** | [**std::collections::HashMap<String, Vec<models::RawHeroMapModCostBonusesV2>>**](Vec.md) |  | 
**color_ui** | **Vec<serde_json::Value>** |  | 
**collision_height** | Option<**f64**> |  | [optional]
**collision_radius** | Option<**f64**> |  | [optional]
**footstep_sound_travel_distance_meters** | Option<**f64**> |  | [optional]
**stealth_speed_meters_per_second** | **f64** |  | 
**step_height** | Option<**f64**> |  | [optional]
**step_sound_time** | Option<**f64**> |  | [optional]
**step_sound_time_sprinting** | Option<**f64**> |  | [optional]
**stats_display** | [**models::RawHeroStatsDisplayV2**](RawHeroStatsDisplayV2.md) |  | 
**hero_stats_ui** | [**models::RawHeroStatsUiv2**](RawHeroStatsUIV2.md) |  | 
**items** | **std::collections::HashMap<String, String>** |  | 
**item_slot_info** | [**std::collections::HashMap<String, models::RawHeroItemSlotInfoValueV2>**](RawHeroItemSlotInfoValueV2.md) |  | 
**level_info** | [**std::collections::HashMap<String, models::RawHeroLevelInfoV2>**](RawHeroLevelInfoV2.md) |  | 
**purchase_bonuses** | Option<[**std::collections::HashMap<String, Vec<models::RawHeroPurchaseBonusV2>>**](Vec.md)> |  | [optional]
**scaling_stats** | [**std::collections::HashMap<String, models::RawHeroScalingStatV2>**](RawHeroScalingStatV2.md) |  | 
**standard_level_up_upgrades** | **std::collections::HashMap<String, f64>** |  | 
**background_image** | Option<**String**> |  | [readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


