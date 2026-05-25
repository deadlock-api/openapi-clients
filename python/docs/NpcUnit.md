# NpcUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceleration** | **float** |  | [optional] 
**attack_t1_boss_max_range** | **float** |  | [optional] 
**attack_t3_boss_max_range** | **float** |  | [optional] 
**attack_t3_boss_phase2_max_range** | **float** |  | [optional] 
**attack_trooper_max_range** | **float** |  | [optional] 
**backdoor_bullet_resist_modifier** | [**SubclassBulletResistModifier**](SubclassBulletResistModifier.md) |  | [optional] 
**barrack_boss_dps** | **float** |  | [optional] 
**barrack_guardian_damage_resist_pct** | **float** |  | [optional] 
**bound_abilities** | **Dict[str, str]** |  | [optional] 
**class_name** | **str** |  | 
**empowered_modifier_level1** | [**SubclassEmpoweredModifierLevel**](SubclassEmpoweredModifierLevel.md) |  | [optional] 
**empowered_modifier_level2** | [**SubclassEmpoweredModifierLevel**](SubclassEmpoweredModifierLevel.md) |  | [optional] 
**enemy_trooper_damage_reduction** | [**SubclassTrooperDamageReduction**](SubclassTrooperDamageReduction.md) |  | [optional] 
**enemy_trooper_protection_range** | **float** |  | [optional] 
**generator_boss_dps** | **float** |  | [optional] 
**gold_reward** | **float** |  | [optional] 
**gold_reward_bonus_percent_per_minute** | **float** |  | [optional] 
**health_bar_color_enemy** | [**Color**](Color.md) |  | [optional] 
**health_bar_color_friend** | [**Color**](Color.md) |  | [optional] 
**health_bar_color_team1** | [**Color**](Color.md) |  | [optional] 
**health_bar_color_team2** | [**Color**](Color.md) |  | [optional] 
**health_bar_color_team_neutral** | [**Color**](Color.md) |  | [optional] 
**id** | **int** |  | 
**intrinsic_modifiers** | [**List[SubclassIntrinsicModifiers]**](SubclassIntrinsicModifiers.md) |  | [optional] 
**laser_dps_max_health** | **float** |  | [optional] 
**laser_dps_to_players** | **float** |  | [optional] 
**max_health** | **int** |  | [optional] 
**max_health_final** | **int** |  | [optional] 
**max_health_generator** | **int** |  | [optional] 
**melee_attempt_range** | **float** |  | [optional] 
**melee_damage** | **float** |  | [optional] 
**melee_duration** | **float** |  | [optional] 
**melee_hit_range** | **float** |  | [optional] 
**near_death_duration** | **float** |  | [optional] 
**no_shield_laser_dps_to_players** | **float** |  | [optional] 
**objective_health_growth_phase1** | [**SubclassObjectiveHealthGrowthPhase**](SubclassObjectiveHealthGrowthPhase.md) |  | [optional] 
**objective_health_growth_phase2** | [**SubclassObjectiveHealthGrowthPhase**](SubclassObjectiveHealthGrowthPhase.md) |  | [optional] 
**objective_regen** | [**SubclassObjectiveRegen**](SubclassObjectiveRegen.md) |  | [optional] 
**phase2_health** | **int** |  | [optional] 
**player_damage_resist_pct** | **float** |  | [optional] 
**player_dps** | **float** |  | [optional] 
**ranged_armor_modifier** | [**SubclassRangedArmorModifier**](SubclassRangedArmorModifier.md) |  | [optional] 
**run_speed** | **float** |  | [optional] 
**sight_range_npcs** | **float** |  | [optional] 
**sight_range_players** | **float** |  | [optional] 
**spawn_breakables_on_death** | **bool** |  | [optional] 
**stomp_damage** | **float** |  | [optional] 
**stomp_damage_max_health_percent** | **float** |  | [optional] 
**stomp_impact_radius** | **float** |  | [optional] 
**stun_duration** | **float** |  | [optional] 
**t1_boss_damage_resist_pct** | **float** |  | [optional] 
**t1_boss_dps** | **float** |  | [optional] 
**t1_boss_dpsbase_resist** | **float** |  | [optional] 
**t1_boss_dpsmax_resist** | **float** |  | [optional] 
**t1_boss_dpsmax_resist_time_in_seconds** | **float** |  | [optional] 
**t2_boss_damage_resist_pct** | **float** |  | [optional] 
**t2_boss_dps** | **float** |  | [optional] 
**t2_boss_dpsbase_resist** | **float** |  | [optional] 
**t2_boss_dpsmax_resist** | **float** |  | [optional] 
**t2_boss_dpsmax_resist_time_in_seconds** | **float** |  | [optional] 
**t3_boss_damage_resist_pct** | **float** |  | [optional] 
**t3_boss_dps** | **float** |  | [optional] 
**trooper_damage_resist_pct** | **float** |  | [optional] 
**trooper_dps** | **float** |  | [optional] 
**walk_speed** | **float** |  | [optional] 
**weapon_info** | [**WeaponInfo**](WeaponInfo.md) |  | [optional] 

## Example

```python
from deadlock_api_client.models.npc_unit import NpcUnit

# TODO update the JSON string below
json = "{}"
# create an instance of NpcUnit from a JSON string
npc_unit_instance = NpcUnit.from_json(json)
# print the JSON string representation of the object
print(NpcUnit.to_json())

# convert the object into a dict
npc_unit_dict = npc_unit_instance.to_dict()
# create an instance of NpcUnit from a dict
npc_unit_from_dict = NpcUnit.from_dict(npc_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


