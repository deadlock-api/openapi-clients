# GenericData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aim_spring_strength** | **Array&lt;number&gt;** |  | [default to undefined]
**armor_groups** | [**Array&lt;ItemGroup&gt;**](ItemGroup.md) |  | [default to undefined]
**breakable_powerup_loot_params** | [**BreakablePowerupLootParams**](BreakablePowerupLootParams.md) | Loot tables for breakable powerup props (build 6711+). | [optional] [default to undefined]
**color_enemy** | [**Color**](Color.md) | Build 6711+. | [optional] [default to undefined]
**color_friend** | [**Color**](Color.md) | Build 6711+. | [optional] [default to undefined]
**color_team1** | [**Color**](Color.md) | Build 6711+. | [optional] [default to undefined]
**color_team2** | [**Color**](Color.md) | Build 6711+. | [optional] [default to undefined]
**corrupted_penalties** | [**Array&lt;CorruptedPenalty&gt;**](CorruptedPenalty.md) | Penalties that can be rolled onto corrupted items (build 6711+). | [optional] [default to undefined]
**damage_flash** | [**DamageFlash**](DamageFlash.md) |  | [default to undefined]
**enemy_objectives_and_zipline_color** | [**Color**](Color.md) |  | [optional] [default to undefined]
**enemy_objectives_color** | [**Color**](Color.md) |  | [optional] [default to undefined]
**enemy_zipline_color** | [**Color**](Color.md) |  | [optional] [default to undefined]
**glitch_settings** | [**GlitchSettings**](GlitchSettings.md) |  | [default to undefined]
**hero_kill_gold_share_frac** | **Array&lt;number&gt;** |  | [default to undefined]
**item_corruption_price_per_tier** | **Array&lt;number&gt;** | Extra cost of corrupting an item, by item tier (build 6711+). | [optional] [default to undefined]
**item_price_per_tier** | **Array&lt;number&gt;** |  | [default to undefined]
**lane_info** | [**Array&lt;LaneInfo&gt;**](LaneInfo.md) |  | [default to undefined]
**map_districts** | [**Array&lt;MapDistrict&gt;**](MapDistrict.md) | District / building labels shown on the map (build 6711+). | [optional] [default to undefined]
**mini_map_offsets** | [**Array&lt;MiniMapOffsets&gt;**](MiniMapOffsets.md) |  | [default to undefined]
**minimap_team_combine_color** | [**Color**](Color.md) |  | [optional] [default to undefined]
**minimap_team_rebels_color** | [**Color**](Color.md) |  | [optional] [default to undefined]
**neutral_camp_respawn_timer_show_distance** | **number** | Distance within which a neutral camp\&#39;s respawn timer is shown (build 6711+). | [optional] [default to undefined]
**new_player_metrics** | [**Array&lt;NewPlayerMetrics&gt;**](NewPlayerMetrics.md) |  | [default to undefined]
**objective_params** | [**ObjectiveParams**](ObjectiveParams.md) |  | [default to undefined]
**rejuv_params** | [**RejuvParams**](RejuvParams.md) |  | [default to undefined]
**spirit_groups** | [**Array&lt;ItemGroup&gt;**](ItemGroup.md) |  | [default to undefined]
**street_brawl** | [**StreetBrawl**](StreetBrawl.md) |  | [optional] [default to undefined]
**targeting_spring_strength** | **Array&lt;number&gt;** |  | [default to undefined]
**trooper_kill_gold_share_frac** | **Array&lt;number&gt;** |  | [default to undefined]
**weapon_groups** | [**Array&lt;ItemGroup&gt;**](ItemGroup.md) |  | [default to undefined]

## Example

```typescript
import { GenericData } from 'deadlock_api_client';

const instance: GenericData = {
    aim_spring_strength,
    armor_groups,
    breakable_powerup_loot_params,
    color_enemy,
    color_friend,
    color_team1,
    color_team2,
    corrupted_penalties,
    damage_flash,
    enemy_objectives_and_zipline_color,
    enemy_objectives_color,
    enemy_zipline_color,
    glitch_settings,
    hero_kill_gold_share_frac,
    item_corruption_price_per_tier,
    item_price_per_tier,
    lane_info,
    map_districts,
    mini_map_offsets,
    minimap_team_combine_color,
    minimap_team_rebels_color,
    neutral_camp_respawn_timer_show_distance,
    new_player_metrics,
    objective_params,
    rejuv_params,
    spirit_groups,
    street_brawl,
    targeting_spring_strength,
    trooper_kill_gold_share_frac,
    weapon_groups,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
