# Hero


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_players_only** | **boolean** |  | [default to undefined]
**class_name** | **string** |  | [default to undefined]
**colors** | [**HeroColors**](HeroColors.md) |  | [default to undefined]
**complexity** | **number** |  | [default to undefined]
**cost_bonuses** | **{ [key: string]: Array&lt;HashMapItemSlotTypeVecMapModCostBonusValueInner&gt;; }** |  | [optional] [default to undefined]
**description** | [**HeroDescription**](HeroDescription.md) |  | [default to undefined]
**disabled** | **boolean** |  | [default to undefined]
**gun_tag** | **string** |  | [optional] [default to undefined]
**hero_stats_ui** | [**HeroStatsUI**](HeroStatsUI.md) |  | [default to undefined]
**hero_type** | [**HeroType**](HeroType.md) |  | [optional] [default to undefined]
**hideout_rich_presence** | **string** |  | [optional] [default to undefined]
**id** | **number** |  | [default to undefined]
**images** | [**HeroImages**](HeroImages.md) |  | [default to undefined]
**in_development** | **boolean** |  | [default to undefined]
**item_draft_bucketing** | [**{ [key: string]: HashMapStringOptionDraftBucketingValue; }**](HashMapStringOptionDraftBucketingValue.md) |  | [optional] [default to undefined]
**item_draft_weights** | **{ [key: string]: number; }** |  | [optional] [default to undefined]
**item_slot_info** | [**{ [key: string]: HashMapItemSlotTypeItemSlotInfoValue; }**](HashMapItemSlotTypeItemSlotInfoValue.md) |  | [default to undefined]
**items** | **{ [key: string]: string; }** |  | [default to undefined]
**level_info** | [**{ [key: string]: HashMapStringLevelInfoValue; }**](HashMapStringLevelInfoValue.md) |  | [default to undefined]
**limited_testing** | **boolean** |  | [default to undefined]
**name** | **string** |  | [default to undefined]
**needs_testing** | **boolean** |  | [default to undefined]
**physics** | [**HeroPhysics**](HeroPhysics.md) |  | [default to undefined]
**player_selectable** | **boolean** |  | [default to undefined]
**prerelease_only** | **boolean** |  | [optional] [default to undefined]
**purchase_bonuses** | **{ [key: string]: Array&lt;HashMapItemSlotTypeVecPurchaseBonusValueInner&gt;; }** |  | [default to undefined]
**scaling_stats** | [**{ [key: string]: HashMapStringScalingStatValue; }**](HashMapStringScalingStatValue.md) |  | [default to undefined]
**shop_stat_display** | [**ShopStatDisplay**](ShopStatDisplay.md) |  | [default to undefined]
**skin** | **number** |  | [default to undefined]
**standard_level_up_upgrades** | **{ [key: string]: number; }** |  | [default to undefined]
**starting_stats** | [**StartingStats**](StartingStats.md) |  | [default to undefined]
**stats_display** | [**StatsDisplay**](StatsDisplay.md) |  | [default to undefined]
**tags** | **Array&lt;string&gt;** | Always emitted (empty if the hero declares no &#x60;m_vecHeroTags&#x60;). | [default to undefined]

## Example

```typescript
import { Hero } from 'deadlock_api_client';

const instance: Hero = {
    assigned_players_only,
    class_name,
    colors,
    complexity,
    cost_bonuses,
    description,
    disabled,
    gun_tag,
    hero_stats_ui,
    hero_type,
    hideout_rich_presence,
    id,
    images,
    in_development,
    item_draft_bucketing,
    item_draft_weights,
    item_slot_info,
    items,
    level_info,
    limited_testing,
    name,
    needs_testing,
    physics,
    player_selectable,
    prerelease_only,
    purchase_bonuses,
    scaling_stats,
    shop_stat_display,
    skin,
    standard_level_up_upgrades,
    starting_stats,
    stats_display,
    tags,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
