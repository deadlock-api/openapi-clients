# Hero

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_players_only** | **bool** |  |
**class_name** | **string** |  |
**colors** | [**\OpenAPI\Client\Model\HeroColors**](HeroColors.md) |  |
**complexity** | **int** |  |
**cost_bonuses** | **array<string,\OpenAPI\Client\Model\HashMapItemSlotTypeVecMapModCostBonusValueInner[]>** |  | [optional]
**description** | [**\OpenAPI\Client\Model\HeroDescription**](HeroDescription.md) |  |
**disabled** | **bool** |  |
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
**player_selectable** | **bool** |  |
**prerelease_only** | **bool** |  | [optional]
**purchase_bonuses** | **array<string,\OpenAPI\Client\Model\HashMapItemSlotTypeVecPurchaseBonusValueInner[]>** |  |
**scaling_stats** | [**array<string,\OpenAPI\Client\Model\HashMapStringScalingStatValue>**](HashMapStringScalingStatValue.md) |  |
**shop_stat_display** | [**\OpenAPI\Client\Model\ShopStatDisplay**](ShopStatDisplay.md) |  |
**skin** | **int** |  |
**standard_level_up_upgrades** | **array<string,float>** |  |
**starting_stats** | [**\OpenAPI\Client\Model\StartingStats**](StartingStats.md) |  |
**stats_display** | [**\OpenAPI\Client\Model\StatsDisplay**](StatsDisplay.md) |  |
**tags** | **string[]** | Always emitted (empty if the hero declares no &#x60;m_vecHeroTags&#x60;). |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
