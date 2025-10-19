# HeroV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [default to undefined]
**class_name** | **string** |  | [default to undefined]
**name** | **string** |  | [default to undefined]
**description** | [**HeroDescriptionV2**](HeroDescriptionV2.md) |  | [default to undefined]
**recommended_upgrades** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**recommended_ability_order** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**player_selectable** | **boolean** |  | [default to undefined]
**disabled** | **boolean** |  | [default to undefined]
**in_development** | **boolean** |  | [default to undefined]
**needs_testing** | **boolean** |  | [default to undefined]
**assigned_players_only** | **boolean** |  | [default to undefined]
**tags** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**gun_tag** | **string** |  | [optional] [default to undefined]
**hideout_rich_presence** | **string** |  | [optional] [default to undefined]
**hero_type** | [**HeroTypeV2**](HeroTypeV2.md) |  | [optional] [default to undefined]
**prerelease_only** | **boolean** |  | [optional] [default to undefined]
**limited_testing** | **boolean** |  | [default to undefined]
**complexity** | **number** |  | [default to undefined]
**skin** | **number** |  | [default to undefined]
**images** | [**HeroImagesV2**](HeroImagesV2.md) |  | [default to undefined]
**items** | **{ [key: string]: string; }** |  | [default to undefined]
**starting_stats** | [**HeroStartingStatsV2**](HeroStartingStatsV2.md) |  | [default to undefined]
**item_slot_info** | [**{ [key: string]: RawHeroItemSlotInfoValueV2Output; }**](RawHeroItemSlotInfoValueV2Output.md) |  | [default to undefined]
**physics** | [**HeroPhysicsV2**](HeroPhysicsV2.md) |  | [default to undefined]
**colors** | [**HeroColorsV2**](HeroColorsV2.md) |  | [default to undefined]
**shop_stat_display** | [**HeroShopStatDisplayV2Output**](HeroShopStatDisplayV2Output.md) |  | [default to undefined]
**cost_bonuses** | **{ [key: string]: Array&lt;RawHeroMapModCostBonusesV2Output&gt;; }** |  | [optional] [default to undefined]
**stats_display** | [**RawHeroStatsDisplayV2Output**](RawHeroStatsDisplayV2Output.md) |  | [default to undefined]
**hero_stats_ui** | [**RawHeroStatsUIV2Output**](RawHeroStatsUIV2Output.md) |  | [default to undefined]
**level_info** | [**{ [key: string]: HeroLevelInfoV2Output; }**](HeroLevelInfoV2Output.md) |  | [default to undefined]
**scaling_stats** | [**{ [key: string]: RawHeroScalingStatV2Output; }**](RawHeroScalingStatV2Output.md) |  | [default to undefined]
**purchase_bonuses** | **{ [key: string]: Array&lt;RawHeroPurchaseBonusV2Output&gt;; }** |  | [default to undefined]
**standard_level_up_upgrades** | **{ [key: string]: number; }** |  | [default to undefined]

## Example

```typescript
import { HeroV2 } from 'assets-deadlock-api-client';

const instance: HeroV2 = {
    id,
    class_name,
    name,
    description,
    recommended_upgrades,
    recommended_ability_order,
    player_selectable,
    disabled,
    in_development,
    needs_testing,
    assigned_players_only,
    tags,
    gun_tag,
    hideout_rich_presence,
    hero_type,
    prerelease_only,
    limited_testing,
    complexity,
    skin,
    images,
    items,
    starting_stats,
    item_slot_info,
    physics,
    colors,
    shop_stat_display,
    cost_bonuses,
    stats_display,
    hero_stats_ui,
    level_info,
    scaling_stats,
    purchase_bonuses,
    standard_level_up_upgrades,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
