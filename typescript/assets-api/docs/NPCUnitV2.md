# NPCUnitV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **string** |  | [default to undefined]
**weapon_info** | [**RawWeaponInfoV2**](RawWeaponInfoV2.md) |  | [optional] [default to undefined]
**max_health** | **number** |  | [optional] [default to undefined]
**sight_range_players** | **number** |  | [optional] [default to undefined]
**sight_range_npcs** | **number** |  | [optional] [default to undefined]
**gold_reward** | **number** |  | [optional] [default to undefined]
**gold_reward_bonus_percent_per_minute** | **number** |  | [optional] [default to undefined]
**m_flPlayerDamageResistPct** | **number** |  | [optional] [default to undefined]
**trooper_damage_resist_pct** | **number** |  | [optional] [default to undefined]
**t1_boss_damage_resist_pct** | **number** |  | [optional] [default to undefined]
**t2_boss_damage_resist_pct** | **number** |  | [optional] [default to undefined]
**t3_boss_damage_resist_pct** | **number** |  | [optional] [default to undefined]
**barrack_guardian_damage_resist_pct** | **number** |  | [optional] [default to undefined]
**near_death_duration** | **number** |  | [optional] [default to undefined]
**walk_speed** | **number** |  | [optional] [default to undefined]
**run_speed** | **number** |  | [optional] [default to undefined]
**acceleration** | **number** |  | [optional] [default to undefined]
**melee_damage** | **number** |  | [optional] [default to undefined]
**melee_attempt_range** | **number** |  | [optional] [default to undefined]
**melee_hit_range** | **number** |  | [optional] [default to undefined]
**melee_duration** | **number** |  | [optional] [default to undefined]
**attack_t1_boss_max_range** | **number** |  | [optional] [default to undefined]
**attack_t3_boss_max_range** | **number** |  | [optional] [default to undefined]
**attack_t3_boss_phase2_max_range** | **number** |  | [optional] [default to undefined]
**attack_trooper_max_range** | **number** |  | [optional] [default to undefined]
**t1_boss_dps** | **number** |  | [optional] [default to undefined]
**t1_boss_dpsbase_resist** | **number** |  | [optional] [default to undefined]
**t1_boss_dpsmax_resist** | **number** |  | [optional] [default to undefined]
**t1_boss_dpsmax_resist_time_in_seconds** | **number** |  | [optional] [default to undefined]
**t2_boss_dps** | **number** |  | [optional] [default to undefined]
**t2_boss_dpsbase_resist** | **number** |  | [optional] [default to undefined]
**t2_boss_dpsmax_resist** | **number** |  | [optional] [default to undefined]
**t2_boss_dpsmax_resist_time_in_seconds** | **number** |  | [optional] [default to undefined]
**t3_boss_dps** | **number** |  | [optional] [default to undefined]
**generator_boss_dps** | **number** |  | [optional] [default to undefined]
**barrack_boss_dps** | **number** |  | [optional] [default to undefined]
**player_dps** | **number** |  | [optional] [default to undefined]
**trooper_dps** | **number** |  | [optional] [default to undefined]
**health_bar_color_friend** | [**ColorV1**](ColorV1.md) |  | [optional] [default to undefined]
**health_bar_color_enemy** | [**ColorV1**](ColorV1.md) |  | [optional] [default to undefined]
**health_bar_color_team1** | [**ColorV1**](ColorV1.md) |  | [optional] [default to undefined]
**health_bar_color_team2** | [**ColorV1**](ColorV1.md) |  | [optional] [default to undefined]
**health_bar_color_team_neutral** | [**ColorV1**](ColorV1.md) |  | [optional] [default to undefined]
**glow_color_friend** | [**ColorV1**](ColorV1.md) |  | [optional] [default to undefined]
**glow_color_enemy** | [**ColorV1**](ColorV1.md) |  | [optional] [default to undefined]
**glow_color_team1** | [**ColorV1**](ColorV1.md) |  | [optional] [default to undefined]
**glow_color_team2** | [**ColorV1**](ColorV1.md) |  | [optional] [default to undefined]
**glow_color_team_neutral** | [**ColorV1**](ColorV1.md) |  | [optional] [default to undefined]
**id** | **number** |  | [readonly] [default to undefined]

## Example

```typescript
import { NPCUnitV2 } from 'assets_deadlock_api_client';

const instance: NPCUnitV2 = {
    class_name,
    weapon_info,
    max_health,
    sight_range_players,
    sight_range_npcs,
    gold_reward,
    gold_reward_bonus_percent_per_minute,
    m_flPlayerDamageResistPct,
    trooper_damage_resist_pct,
    t1_boss_damage_resist_pct,
    t2_boss_damage_resist_pct,
    t3_boss_damage_resist_pct,
    barrack_guardian_damage_resist_pct,
    near_death_duration,
    walk_speed,
    run_speed,
    acceleration,
    melee_damage,
    melee_attempt_range,
    melee_hit_range,
    melee_duration,
    attack_t1_boss_max_range,
    attack_t3_boss_max_range,
    attack_t3_boss_phase2_max_range,
    attack_trooper_max_range,
    t1_boss_dps,
    t1_boss_dpsbase_resist,
    t1_boss_dpsmax_resist,
    t1_boss_dpsmax_resist_time_in_seconds,
    t2_boss_dps,
    t2_boss_dpsbase_resist,
    t2_boss_dpsmax_resist,
    t2_boss_dpsmax_resist_time_in_seconds,
    t3_boss_dps,
    generator_boss_dps,
    barrack_boss_dps,
    player_dps,
    trooper_dps,
    health_bar_color_friend,
    health_bar_color_enemy,
    health_bar_color_team1,
    health_bar_color_team2,
    health_bar_color_team_neutral,
    glow_color_friend,
    glow_color_enemy,
    glow_color_team1,
    glow_color_team2,
    glow_color_team_neutral,
    id,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
