# NpcUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceleration** | **number** |  | [optional] [default to undefined]
**attack_t1_boss_max_range** | **number** |  | [optional] [default to undefined]
**attack_t3_boss_max_range** | **number** |  | [optional] [default to undefined]
**attack_t3_boss_phase2_max_range** | **number** |  | [optional] [default to undefined]
**attack_trooper_max_range** | **number** |  | [optional] [default to undefined]
**backdoor_bullet_resist_modifier** | [**SubclassBulletResistModifier**](SubclassBulletResistModifier.md) |  | [optional] [default to undefined]
**barrack_boss_dps** | **number** |  | [optional] [default to undefined]
**barrack_guardian_damage_resist_pct** | **number** |  | [optional] [default to undefined]
**bound_abilities** | **{ [key: string]: string; }** |  | [optional] [default to undefined]
**class_name** | **string** |  | [default to undefined]
**empowered_modifier_level1** | [**SubclassEmpoweredModifierLevel**](SubclassEmpoweredModifierLevel.md) |  | [optional] [default to undefined]
**empowered_modifier_level2** | [**SubclassEmpoweredModifierLevel**](SubclassEmpoweredModifierLevel.md) |  | [optional] [default to undefined]
**enemy_trooper_damage_reduction** | [**SubclassTrooperDamageReduction**](SubclassTrooperDamageReduction.md) |  | [optional] [default to undefined]
**enemy_trooper_protection_range** | **number** |  | [optional] [default to undefined]
**generator_boss_dps** | **number** |  | [optional] [default to undefined]
**gold_reward** | **number** |  | [optional] [default to undefined]
**gold_reward_bonus_percent_per_minute** | **number** |  | [optional] [default to undefined]
**health_bar_color_enemy** | [**Color**](Color.md) |  | [optional] [default to undefined]
**health_bar_color_friend** | [**Color**](Color.md) |  | [optional] [default to undefined]
**health_bar_color_team1** | [**Color**](Color.md) |  | [optional] [default to undefined]
**health_bar_color_team2** | [**Color**](Color.md) |  | [optional] [default to undefined]
**health_bar_color_team_neutral** | [**Color**](Color.md) |  | [optional] [default to undefined]
**id** | **number** |  | [default to undefined]
**intrinsic_modifiers** | [**Array&lt;SubclassIntrinsicModifiers&gt;**](SubclassIntrinsicModifiers.md) |  | [optional] [default to undefined]
**laser_dps_max_health** | **number** |  | [optional] [default to undefined]
**laser_dps_to_players** | **number** |  | [optional] [default to undefined]
**max_health** | **number** |  | [optional] [default to undefined]
**max_health_final** | **number** |  | [optional] [default to undefined]
**max_health_generator** | **number** |  | [optional] [default to undefined]
**melee_attempt_range** | **number** |  | [optional] [default to undefined]
**melee_damage** | **number** |  | [optional] [default to undefined]
**melee_duration** | **number** |  | [optional] [default to undefined]
**melee_hit_range** | **number** |  | [optional] [default to undefined]
**near_death_duration** | **number** |  | [optional] [default to undefined]
**no_shield_laser_dps_to_players** | **number** |  | [optional] [default to undefined]
**objective_health_growth_phase1** | [**SubclassObjectiveHealthGrowthPhase**](SubclassObjectiveHealthGrowthPhase.md) |  | [optional] [default to undefined]
**objective_health_growth_phase2** | [**SubclassObjectiveHealthGrowthPhase**](SubclassObjectiveHealthGrowthPhase.md) |  | [optional] [default to undefined]
**objective_regen** | [**SubclassObjectiveRegen**](SubclassObjectiveRegen.md) |  | [optional] [default to undefined]
**phase2_health** | **number** |  | [optional] [default to undefined]
**player_damage_resist_pct** | **number** |  | [optional] [default to undefined]
**player_dps** | **number** |  | [optional] [default to undefined]
**ranged_armor_modifier** | [**SubclassRangedArmorModifier**](SubclassRangedArmorModifier.md) |  | [optional] [default to undefined]
**run_speed** | **number** |  | [optional] [default to undefined]
**sight_range_npcs** | **number** |  | [optional] [default to undefined]
**sight_range_players** | **number** |  | [optional] [default to undefined]
**spawn_breakables_on_death** | **boolean** |  | [optional] [default to undefined]
**stomp_damage** | **number** |  | [optional] [default to undefined]
**stomp_damage_max_health_percent** | **number** |  | [optional] [default to undefined]
**stomp_impact_radius** | **number** |  | [optional] [default to undefined]
**stun_duration** | **number** |  | [optional] [default to undefined]
**t1_boss_damage_resist_pct** | **number** |  | [optional] [default to undefined]
**t1_boss_dps** | **number** |  | [optional] [default to undefined]
**t1_boss_dpsbase_resist** | **number** |  | [optional] [default to undefined]
**t1_boss_dpsmax_resist** | **number** |  | [optional] [default to undefined]
**t1_boss_dpsmax_resist_time_in_seconds** | **number** |  | [optional] [default to undefined]
**t2_boss_damage_resist_pct** | **number** |  | [optional] [default to undefined]
**t2_boss_dps** | **number** |  | [optional] [default to undefined]
**t2_boss_dpsbase_resist** | **number** |  | [optional] [default to undefined]
**t2_boss_dpsmax_resist** | **number** |  | [optional] [default to undefined]
**t2_boss_dpsmax_resist_time_in_seconds** | **number** |  | [optional] [default to undefined]
**t3_boss_damage_resist_pct** | **number** |  | [optional] [default to undefined]
**t3_boss_dps** | **number** |  | [optional] [default to undefined]
**trooper_damage_resist_pct** | **number** |  | [optional] [default to undefined]
**trooper_dps** | **number** |  | [optional] [default to undefined]
**walk_speed** | **number** |  | [optional] [default to undefined]
**weapon_info** | [**WeaponInfo**](WeaponInfo.md) |  | [optional] [default to undefined]

## Example

```typescript
import { NpcUnit } from 'deadlock_api_client';

const instance: NpcUnit = {
    acceleration,
    attack_t1_boss_max_range,
    attack_t3_boss_max_range,
    attack_t3_boss_phase2_max_range,
    attack_trooper_max_range,
    backdoor_bullet_resist_modifier,
    barrack_boss_dps,
    barrack_guardian_damage_resist_pct,
    bound_abilities,
    class_name,
    empowered_modifier_level1,
    empowered_modifier_level2,
    enemy_trooper_damage_reduction,
    enemy_trooper_protection_range,
    generator_boss_dps,
    gold_reward,
    gold_reward_bonus_percent_per_minute,
    health_bar_color_enemy,
    health_bar_color_friend,
    health_bar_color_team1,
    health_bar_color_team2,
    health_bar_color_team_neutral,
    id,
    intrinsic_modifiers,
    laser_dps_max_health,
    laser_dps_to_players,
    max_health,
    max_health_final,
    max_health_generator,
    melee_attempt_range,
    melee_damage,
    melee_duration,
    melee_hit_range,
    near_death_duration,
    no_shield_laser_dps_to_players,
    objective_health_growth_phase1,
    objective_health_growth_phase2,
    objective_regen,
    phase2_health,
    player_damage_resist_pct,
    player_dps,
    ranged_armor_modifier,
    run_speed,
    sight_range_npcs,
    sight_range_players,
    spawn_breakables_on_death,
    stomp_damage,
    stomp_damage_max_health_percent,
    stomp_impact_radius,
    stun_duration,
    t1_boss_damage_resist_pct,
    t1_boss_dps,
    t1_boss_dpsbase_resist,
    t1_boss_dpsmax_resist,
    t1_boss_dpsmax_resist_time_in_seconds,
    t2_boss_damage_resist_pct,
    t2_boss_dps,
    t2_boss_dpsbase_resist,
    t2_boss_dpsmax_resist,
    t2_boss_dpsmax_resist_time_in_seconds,
    t3_boss_damage_resist_pct,
    t3_boss_dps,
    trooper_damage_resist_pct,
    trooper_dps,
    walk_speed,
    weapon_info,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
