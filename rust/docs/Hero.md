# Hero

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_players_only** | **bool** |  | 
**class_name** | **String** |  | 
**colors** | [**models::HeroColors**](HeroColors.md) |  | 
**complexity** | **i64** |  | 
**cost_bonuses** | Option<[**std::collections::HashMap<String, Vec<models::HashMapItemSlotTypeVecMapModCostBonusValueInner>>**](Vec.md)> |  | [optional]
**description** | [**models::HeroDescription**](HeroDescription.md) |  | 
**disabled** | **bool** |  | 
**gun_tag** | Option<**String**> |  | [optional]
**hero_stats_ui** | [**models::HeroStatsUi**](HeroStatsUI.md) |  | 
**hero_type** | Option<[**models::HeroType**](HeroType.md)> |  | [optional]
**hideout_rich_presence** | Option<**String**> |  | [optional]
**id** | **u32** |  | 
**images** | [**models::HeroImages**](HeroImages.md) |  | 
**in_development** | **bool** |  | 
**item_draft_bucketing** | Option<[**std::collections::HashMap<String, models::HashMapStringOptionDraftBucketingValue>**](HashMapStringOptionDraftBucketingValue.md)> |  | [optional]
**item_draft_weights** | Option<**std::collections::HashMap<String, f64>**> |  | [optional]
**item_slot_info** | [**std::collections::HashMap<String, models::HashMapItemSlotTypeItemSlotInfoValue>**](HashMapItemSlotTypeItemSlotInfoValue.md) |  | 
**items** | **std::collections::HashMap<String, String>** |  | 
**level_info** | [**std::collections::HashMap<String, models::HashMapStringLevelInfoValue>**](HashMapStringLevelInfoValue.md) |  | 
**limited_testing** | **bool** |  | 
**name** | **String** |  | 
**needs_testing** | **bool** |  | 
**physics** | [**models::HeroPhysics**](HeroPhysics.md) |  | 
**player_selectable** | **bool** |  | 
**prerelease_only** | Option<**bool**> |  | [optional]
**purchase_bonuses** | [**std::collections::HashMap<String, Vec<models::HashMapItemSlotTypeVecPurchaseBonusValueInner>>**](Vec.md) |  | 
**scaling_stats** | [**std::collections::HashMap<String, models::HashMapStringScalingStatValue>**](HashMapStringScalingStatValue.md) |  | 
**shop_stat_display** | [**models::ShopStatDisplay**](ShopStatDisplay.md) |  | 
**skin** | **i64** |  | 
**standard_level_up_upgrades** | **std::collections::HashMap<String, f64>** |  | 
**starting_stats** | [**models::StartingStats**](StartingStats.md) |  | 
**stats_display** | [**models::StatsDisplay**](StatsDisplay.md) |  | 
**tags** | **Vec<String>** | Always emitted (empty if the hero declares no `m_vecHeroTags`). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


