# GenericDataV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**damage_flash** | [**DamageFlashV2**](DamageFlashV2.md) |  | [default to undefined]
**glitch_settings** | [**GlitchSettingsV2**](GlitchSettingsV2.md) |  | [default to undefined]
**lane_info** | [**Array&lt;LaneInfoV2&gt;**](LaneInfoV2.md) |  | [default to undefined]
**new_player_metrics** | [**Array&lt;NewPlayerMetricsV2&gt;**](NewPlayerMetricsV2.md) |  | [default to undefined]
**minimap_team_rebels_color** | [**ColorV1**](ColorV1.md) |  | [optional] [default to undefined]
**minimap_team_combine_color** | [**ColorV1**](ColorV1.md) |  | [optional] [default to undefined]
**enemy_objectives_and_zipline_color** | [**ColorV1**](ColorV1.md) |  | [optional] [default to undefined]
**enemy_objectives_color** | [**ColorV1**](ColorV1.md) |  | [optional] [default to undefined]
**enemy_zipline_color** | [**ColorV1**](ColorV1.md) |  | [optional] [default to undefined]
**item_price_per_tier** | **Array&lt;number&gt;** |  | [default to undefined]
**trooper_kill_gold_share_frac** | **Array&lt;number&gt;** |  | [default to undefined]
**hero_kill_gold_share_frac** | **Array&lt;number&gt;** |  | [default to undefined]
**aim_spring_strength** | **Array&lt;number&gt;** |  | [default to undefined]
**targeting_spring_strength** | **Array&lt;number&gt;** |  | [default to undefined]
**objective_params** | [**ObjectiveParams**](ObjectiveParams.md) |  | [default to undefined]
**rejuv_params** | [**RejuvParams**](RejuvParams.md) |  | [default to undefined]
**mini_map_offsets** | [**Array&lt;MiniMapOffsets&gt;**](MiniMapOffsets.md) |  | [default to undefined]
**weapon_groups** | [**Array&lt;ItemGroup&gt;**](ItemGroup.md) |  | [default to undefined]
**armor_groups** | [**Array&lt;ItemGroup&gt;**](ItemGroup.md) |  | [default to undefined]
**spirit_groups** | [**Array&lt;ItemGroup&gt;**](ItemGroup.md) |  | [default to undefined]
**street_brawl** | [**StreetBrawl**](StreetBrawl.md) |  | [optional] [default to undefined]

## Example

```typescript
import { GenericDataV2 } from 'assets_deadlock_api_client';

const instance: GenericDataV2 = {
    damage_flash,
    glitch_settings,
    lane_info,
    new_player_metrics,
    minimap_team_rebels_color,
    minimap_team_combine_color,
    enemy_objectives_and_zipline_color,
    enemy_objectives_color,
    enemy_zipline_color,
    item_price_per_tier,
    trooper_kill_gold_share_frac,
    hero_kill_gold_share_frac,
    aim_spring_strength,
    targeting_spring_strength,
    objective_params,
    rejuv_params,
    mini_map_offsets,
    weapon_groups,
    armor_groups,
    spirit_groups,
    street_brawl,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
