# Hero


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_players_only** | **boolean** | &#x60;m_bAssignedPlayersOnly&#x60; was removed in build 6711; always &#x60;false&#x60; since. | [default to undefined]
**class_name** | **string** |  | [default to undefined]
**colors** | [**HeroColors**](HeroColors.md) |  | [default to undefined]
**complexity** | **number** |  | [default to undefined]
**cost_bonuses** | **{ [key: string]: Array&lt;HashMapItemSlotTypeVecMapModCostBonusValueInner&gt;; }** |  | [optional] [default to undefined]
**description** | [**HeroDescription**](HeroDescription.md) |  | [default to undefined]
**development_state** | [**HeroDevelopmentState**](HeroDevelopmentState.md) | Hero development state (&#x60;m_eHeroDevelopmentState&#x60;, build 6711+). &#x60;null&#x60; on older builds and on heroes that don\&#39;t declare one. | [optional] [default to undefined]
**disabled** | **boolean** |  | [default to undefined]
**gender** | **string** | Hero gender (&#x60;m_strHeroGender&#x60;, build 6711+), e.g. &#x60;male&#x60; / &#x60;female&#x60;. | [optional] [default to undefined]
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
**player_selectable** | **boolean** | Read from &#x60;m_bPlayerSelectable&#x60; on older builds; since build 6711 it is derived as &#x60;development_state &#x3D;&#x3D; release&#x60;. | [default to undefined]
**popular_items** | [**HeroPopularItems**](HeroPopularItems.md) | Valve\&#39;s generated item pick / win rates per game phase (&#x60;m_PopularItems&#x60;, build 6711+). &#x60;null&#x60; when the hero has no data. | [optional] [default to undefined]
**prerelease_only** | **boolean** | Read from &#x60;m_bPrereleaseOnly&#x60; on older builds; since build 6711 it is derived as &#x60;development_state &#x3D;&#x3D; pre_release&#x60;. | [optional] [default to undefined]
**purchase_bonuses** | **{ [key: string]: Array&lt;HashMapItemSlotTypeVecPurchaseBonusValueInner&gt;; }** | Deprecated: &#x60;m_mapPurchaseBonuses&#x60; was removed in build 6711, so this is always empty for newer builds. | [default to undefined]
**scaling_stats** | [**{ [key: string]: HashMapStringScalingStatValue; }**](HashMapStringScalingStatValue.md) |  | [default to undefined]
**search_name** | **string** | Localized search name (&#x60;m_strHeroSearchName&#x60;, build 6711+). | [optional] [default to undefined]
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
    development_state,
    disabled,
    gender,
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
    popular_items,
    prerelease_only,
    purchase_bonuses,
    scaling_stats,
    search_name,
    shop_stat_display,
    skin,
    standard_level_up_upgrades,
    starting_stats,
    stats_display,
    tags,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
