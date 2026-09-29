# Hero

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_players_only** | **bool** | &#x60;m_bAssignedPlayersOnly&#x60; was removed in build 6711; always &#x60;false&#x60; since. |
**class_name** | **string** |  |
**colors** | [**\OpenAPI\Client\Model\HeroColors**](HeroColors.md) |  |
**complexity** | **int** |  |
**cost_bonuses** | **array<string,\OpenAPI\Client\Model\HashMapItemSlotTypeVecMapModCostBonusValueInner[]>** |  | [optional]
**description** | [**\OpenAPI\Client\Model\HeroDescription**](HeroDescription.md) |  |
**development_state** | [**\OpenAPI\Client\Model\HeroDevelopmentState**](HeroDevelopmentState.md) | Hero development state (&#x60;m_eHeroDevelopmentState&#x60;, build 6711+). &#x60;null&#x60; on older builds and on heroes that don&#39;t declare one. | [optional]
**disabled** | **bool** |  |
**gender** | **string** | Hero gender (&#x60;m_strHeroGender&#x60;, build 6711+), e.g. &#x60;male&#x60; / &#x60;female&#x60;. | [optional]
**gun_tag** | **string** |  | [optional]
**hero_stats_ui** | [**\OpenAPI\Client\Model\HeroStatsUI**](HeroStatsUI.md) |  |
**hero_type** | [**\OpenAPI\Client\Model\HeroType**](HeroType.md) |  | [optional]
**hideout_rich_presence** | **string** |  | [optional]
**id** | **int** |  |
**images** | [**\OpenAPI\Client\Model\HeroImages**](HeroImages.md) |  |
**in_development** | **bool** |  |
**item_draft_bucketing** | [**array<string,\OpenAPI\Client\Model\HashMapStringOptionDraftBucketingValue>**](HashMapStringOptionDraftBucketingValue.md) |  | [optional]
**item_draft_weights** | **array<string,float>** |  | [optional]
**item_slot_info** | [**array<string,\OpenAPI\Client\Model\HashMapItemSlotTypeItemSlotInfoValue>**](HashMapItemSlotTypeItemSlotInfoValue.md) |  |
**items** | **array<string,string>** |  |
**level_info** | [**array<string,\OpenAPI\Client\Model\HashMapStringLevelInfoValue>**](HashMapStringLevelInfoValue.md) |  |
**limited_testing** | **bool** |  |
**name** | **string** |  |
**needs_testing** | **bool** |  |
**physics** | [**\OpenAPI\Client\Model\HeroPhysics**](HeroPhysics.md) |  |
**player_selectable** | **bool** | Read from &#x60;m_bPlayerSelectable&#x60; on older builds; since build 6711 it is derived as &#x60;development_state &#x3D;&#x3D; release&#x60;. |
**popular_items** | [**\OpenAPI\Client\Model\HeroPopularItems**](HeroPopularItems.md) | Valve&#39;s generated item pick / win rates per game phase (&#x60;m_PopularItems&#x60;, build 6711+). &#x60;null&#x60; when the hero has no data. | [optional]
**prerelease_only** | **bool** | Read from &#x60;m_bPrereleaseOnly&#x60; on older builds; since build 6711 it is derived as &#x60;development_state &#x3D;&#x3D; pre_release&#x60;. | [optional]
**purchase_bonuses** | **array<string,\OpenAPI\Client\Model\HashMapItemSlotTypeVecPurchaseBonusValueInner[]>** | Deprecated: &#x60;m_mapPurchaseBonuses&#x60; was removed in build 6711, so this is always empty for newer builds. |
**scaling_stats** | [**array<string,\OpenAPI\Client\Model\HashMapStringScalingStatValue>**](HashMapStringScalingStatValue.md) |  |
**search_name** | **string** | Localized search name (&#x60;m_strHeroSearchName&#x60;, build 6711+). | [optional]
**shop_stat_display** | [**\OpenAPI\Client\Model\ShopStatDisplay**](ShopStatDisplay.md) |  |
**skin** | **int** |  |
**standard_level_up_upgrades** | **array<string,float>** |  |
**starting_stats** | [**\OpenAPI\Client\Model\StartingStats**](StartingStats.md) |  |
**stats_display** | [**\OpenAPI\Client\Model\StatsDisplay**](StatsDisplay.md) |  |
**tags** | **string[]** | Always emitted (empty if the hero declares no &#x60;m_vecHeroTags&#x60;). |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
