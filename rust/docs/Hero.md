# Hero

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_players_only** | **bool** | `m_bAssignedPlayersOnly` was removed in build 6711; always `false` since. | 
**class_name** | **String** |  | 
**colors** | [**models::HeroColors**](HeroColors.md) |  | 
**complexity** | **i64** |  | 
**cost_bonuses** | Option<[**std::collections::HashMap<String, Vec<models::HashMapItemSlotTypeVecMapModCostBonusValueInner>>**](Vec.md)> |  | [optional]
**description** | [**models::HeroDescription**](HeroDescription.md) |  | 
**development_state** | Option<[**models::HeroDevelopmentState**](HeroDevelopmentState.md)> | Hero development state (`m_eHeroDevelopmentState`, build 6711+). `null` on older builds and on heroes that don't declare one. | [optional]
**disabled** | **bool** |  | 
**gender** | Option<**String**> | Hero gender (`m_strHeroGender`, build 6711+), e.g. `male` / `female`. | [optional]
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
**player_selectable** | **bool** | Read from `m_bPlayerSelectable` on older builds; since build 6711 it is derived as `development_state == release`. | 
**popular_items** | Option<[**models::HeroPopularItems**](HeroPopularItems.md)> | Valve's generated item pick / win rates per game phase (`m_PopularItems`, build 6711+). `null` when the hero has no data. | [optional]
**prerelease_only** | Option<**bool**> | Read from `m_bPrereleaseOnly` on older builds; since build 6711 it is derived as `development_state == pre_release`. | [optional]
**purchase_bonuses** | [**std::collections::HashMap<String, Vec<models::HashMapItemSlotTypeVecPurchaseBonusValueInner>>**](Vec.md) | Deprecated: `m_mapPurchaseBonuses` was removed in build 6711, so this is always empty for newer builds. | 
**scaling_stats** | [**std::collections::HashMap<String, models::HashMapStringScalingStatValue>**](HashMapStringScalingStatValue.md) |  | 
**search_name** | Option<**String**> | Localized search name (`m_strHeroSearchName`, build 6711+). | [optional]
**shop_stat_display** | [**models::ShopStatDisplay**](ShopStatDisplay.md) |  | 
**skin** | **i64** |  | 
**standard_level_up_upgrades** | **std::collections::HashMap<String, f64>** |  | 
**starting_stats** | [**models::StartingStats**](StartingStats.md) |  | 
**stats_display** | [**models::StatsDisplay**](StatsDisplay.md) |  | 
**tags** | **Vec<String>** | Always emitted (empty if the hero declares no `m_vecHeroTags`). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


