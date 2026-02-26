# RawHeroV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [default to undefined]
**class_name** | **string** |  | [default to undefined]
**item_draft_weights** | **{ [key: string]: number; }** |  | [optional] [default to undefined]
**player_selectable** | **boolean** |  | [default to undefined]
**disabled** | **boolean** |  | [default to undefined]
**in_development** | **boolean** |  | [default to undefined]
**needs_testing** | **boolean** |  | [default to undefined]
**assigned_players_only** | **boolean** |  | [default to undefined]
**available_in_hero_labs** | **boolean** |  | [optional] [default to undefined]
**prerelease_only** | **boolean** |  | [optional] [default to undefined]
**limited_testing** | **boolean** |  | [default to undefined]
**complexity** | **number** |  | [default to undefined]
**skin** | **number** |  | [default to undefined]
**starting_stats** | [**RawHeroStartingStatsV2**](RawHeroStartingStatsV2.md) |  | [default to undefined]
**icon_hero_card** | **string** |  | [optional] [default to undefined]
**icon_image_small** | **string** |  | [optional] [default to undefined]
**minimap_image** | **string** |  | [optional] [default to undefined]
**name_image** | **string** |  | [optional] [default to undefined]
**hero_card_critical** | **string** |  | [optional] [default to undefined]
**hero_card_gloat** | **string** |  | [optional] [default to undefined]
**top_bar_vertical_image** | **string** |  | [optional] [default to undefined]
**tags** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**gun_tag** | **string** |  | [optional] [default to undefined]
**hideout_rich_presence** | **string** |  | [optional] [default to undefined]
**hero_type** | [**HeroTypeV2**](HeroTypeV2.md) |  | [optional] [default to undefined]
**shop_stat_display** | [**RawHeroShopStatDisplayV2**](RawHeroShopStatDisplayV2.md) |  | [default to undefined]
**cost_bonuses** | **{ [key: string]: Array&lt;RawHeroMapModCostBonusesV2&gt;; }** |  | [default to undefined]
**color_ui** | **Array&lt;any&gt;** |  | [default to undefined]
**collision_height** | **number** |  | [optional] [default to undefined]
**collision_radius** | **number** |  | [optional] [default to undefined]
**footstep_sound_travel_distance_meters** | **number** |  | [optional] [default to undefined]
**stealth_speed_meters_per_second** | **number** |  | [default to undefined]
**step_height** | **number** |  | [optional] [default to undefined]
**step_sound_time** | **number** |  | [optional] [default to undefined]
**step_sound_time_sprinting** | **number** |  | [optional] [default to undefined]
**stats_display** | [**RawHeroStatsDisplayV2**](RawHeroStatsDisplayV2.md) |  | [default to undefined]
**hero_stats_ui** | [**RawHeroStatsUIV2**](RawHeroStatsUIV2.md) |  | [default to undefined]
**items** | **{ [key: string]: string; }** |  | [default to undefined]
**item_slot_info** | [**{ [key: string]: RawHeroItemSlotInfoValueV2; }**](RawHeroItemSlotInfoValueV2.md) |  | [default to undefined]
**level_info** | [**{ [key: string]: RawHeroLevelInfoV2; }**](RawHeroLevelInfoV2.md) |  | [default to undefined]
**purchase_bonuses** | **{ [key: string]: Array&lt;RawHeroPurchaseBonusV2&gt;; }** |  | [optional] [default to undefined]
**scaling_stats** | [**{ [key: string]: RawHeroScalingStatV2; }**](RawHeroScalingStatV2.md) |  | [default to undefined]
**standard_level_up_upgrades** | **{ [key: string]: number; }** |  | [default to undefined]
**background_image** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { RawHeroV2 } from 'assets_deadlock_api_client';

const instance: RawHeroV2 = {
    id,
    class_name,
    item_draft_weights,
    player_selectable,
    disabled,
    in_development,
    needs_testing,
    assigned_players_only,
    available_in_hero_labs,
    prerelease_only,
    limited_testing,
    complexity,
    skin,
    starting_stats,
    icon_hero_card,
    icon_image_small,
    minimap_image,
    name_image,
    hero_card_critical,
    hero_card_gloat,
    top_bar_vertical_image,
    tags,
    gun_tag,
    hideout_rich_presence,
    hero_type,
    shop_stat_display,
    cost_bonuses,
    color_ui,
    collision_height,
    collision_radius,
    footstep_sound_travel_distance_meters,
    stealth_speed_meters_per_second,
    step_height,
    step_sound_time,
    step_sound_time_sprinting,
    stats_display,
    hero_stats_ui,
    items,
    item_slot_info,
    level_info,
    purchase_bonuses,
    scaling_stats,
    standard_level_up_upgrades,
    background_image,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
