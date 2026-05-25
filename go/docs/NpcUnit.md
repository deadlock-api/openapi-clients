# NpcUnit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Acceleration** | Pointer to **NullableFloat64** |  | [optional] 
**AttackT1BossMaxRange** | Pointer to **NullableFloat64** |  | [optional] 
**AttackT3BossMaxRange** | Pointer to **NullableFloat64** |  | [optional] 
**AttackT3BossPhase2MaxRange** | Pointer to **NullableFloat64** |  | [optional] 
**AttackTrooperMaxRange** | Pointer to **NullableFloat64** |  | [optional] 
**BackdoorBulletResistModifier** | Pointer to [**NullableSubclassBulletResistModifier**](SubclassBulletResistModifier.md) |  | [optional] 
**BarrackBossDps** | Pointer to **NullableFloat64** |  | [optional] 
**BarrackGuardianDamageResistPct** | Pointer to **NullableFloat64** |  | [optional] 
**BoundAbilities** | Pointer to **map[string]string** |  | [optional] 
**ClassName** | **string** |  | 
**EmpoweredModifierLevel1** | Pointer to [**NullableSubclassEmpoweredModifierLevel**](SubclassEmpoweredModifierLevel.md) |  | [optional] 
**EmpoweredModifierLevel2** | Pointer to [**NullableSubclassEmpoweredModifierLevel**](SubclassEmpoweredModifierLevel.md) |  | [optional] 
**EnemyTrooperDamageReduction** | Pointer to [**NullableSubclassTrooperDamageReduction**](SubclassTrooperDamageReduction.md) |  | [optional] 
**EnemyTrooperProtectionRange** | Pointer to **NullableFloat64** |  | [optional] 
**GeneratorBossDps** | Pointer to **NullableFloat64** |  | [optional] 
**GoldReward** | Pointer to **NullableFloat64** |  | [optional] 
**GoldRewardBonusPercentPerMinute** | Pointer to **NullableFloat64** |  | [optional] 
**HealthBarColorEnemy** | Pointer to [**NullableColor**](Color.md) |  | [optional] 
**HealthBarColorFriend** | Pointer to [**NullableColor**](Color.md) |  | [optional] 
**HealthBarColorTeam1** | Pointer to [**NullableColor**](Color.md) |  | [optional] 
**HealthBarColorTeam2** | Pointer to [**NullableColor**](Color.md) |  | [optional] 
**HealthBarColorTeamNeutral** | Pointer to [**NullableColor**](Color.md) |  | [optional] 
**Id** | **int32** |  | 
**IntrinsicModifiers** | Pointer to [**[]SubclassIntrinsicModifiers**](SubclassIntrinsicModifiers.md) |  | [optional] 
**LaserDpsMaxHealth** | Pointer to **NullableFloat64** |  | [optional] 
**LaserDpsToPlayers** | Pointer to **NullableFloat64** |  | [optional] 
**MaxHealth** | Pointer to **NullableInt64** |  | [optional] 
**MaxHealthFinal** | Pointer to **NullableInt64** |  | [optional] 
**MaxHealthGenerator** | Pointer to **NullableInt64** |  | [optional] 
**MeleeAttemptRange** | Pointer to **NullableFloat64** |  | [optional] 
**MeleeDamage** | Pointer to **NullableFloat64** |  | [optional] 
**MeleeDuration** | Pointer to **NullableFloat64** |  | [optional] 
**MeleeHitRange** | Pointer to **NullableFloat64** |  | [optional] 
**NearDeathDuration** | Pointer to **NullableFloat64** |  | [optional] 
**NoShieldLaserDpsToPlayers** | Pointer to **NullableFloat64** |  | [optional] 
**ObjectiveHealthGrowthPhase1** | Pointer to [**NullableSubclassObjectiveHealthGrowthPhase**](SubclassObjectiveHealthGrowthPhase.md) |  | [optional] 
**ObjectiveHealthGrowthPhase2** | Pointer to [**NullableSubclassObjectiveHealthGrowthPhase**](SubclassObjectiveHealthGrowthPhase.md) |  | [optional] 
**ObjectiveRegen** | Pointer to [**NullableSubclassObjectiveRegen**](SubclassObjectiveRegen.md) |  | [optional] 
**Phase2Health** | Pointer to **NullableInt64** |  | [optional] 
**PlayerDamageResistPct** | Pointer to **NullableFloat64** |  | [optional] 
**PlayerDps** | Pointer to **NullableFloat64** |  | [optional] 
**RangedArmorModifier** | Pointer to [**NullableSubclassRangedArmorModifier**](SubclassRangedArmorModifier.md) |  | [optional] 
**RunSpeed** | Pointer to **NullableFloat64** |  | [optional] 
**SightRangeNpcs** | Pointer to **NullableFloat64** |  | [optional] 
**SightRangePlayers** | Pointer to **NullableFloat64** |  | [optional] 
**SpawnBreakablesOnDeath** | Pointer to **NullableBool** |  | [optional] 
**StompDamage** | Pointer to **NullableFloat64** |  | [optional] 
**StompDamageMaxHealthPercent** | Pointer to **NullableFloat64** |  | [optional] 
**StompImpactRadius** | Pointer to **NullableFloat64** |  | [optional] 
**StunDuration** | Pointer to **NullableFloat64** |  | [optional] 
**T1BossDamageResistPct** | Pointer to **NullableFloat64** |  | [optional] 
**T1BossDps** | Pointer to **NullableFloat64** |  | [optional] 
**T1BossDpsbaseResist** | Pointer to **NullableFloat64** |  | [optional] 
**T1BossDpsmaxResist** | Pointer to **NullableFloat64** |  | [optional] 
**T1BossDpsmaxResistTimeInSeconds** | Pointer to **NullableFloat64** |  | [optional] 
**T2BossDamageResistPct** | Pointer to **NullableFloat64** |  | [optional] 
**T2BossDps** | Pointer to **NullableFloat64** |  | [optional] 
**T2BossDpsbaseResist** | Pointer to **NullableFloat64** |  | [optional] 
**T2BossDpsmaxResist** | Pointer to **NullableFloat64** |  | [optional] 
**T2BossDpsmaxResistTimeInSeconds** | Pointer to **NullableFloat64** |  | [optional] 
**T3BossDamageResistPct** | Pointer to **NullableFloat64** |  | [optional] 
**T3BossDps** | Pointer to **NullableFloat64** |  | [optional] 
**TrooperDamageResistPct** | Pointer to **NullableFloat64** |  | [optional] 
**TrooperDps** | Pointer to **NullableFloat64** |  | [optional] 
**WalkSpeed** | Pointer to **NullableFloat64** |  | [optional] 
**WeaponInfo** | Pointer to [**NullableWeaponInfo**](WeaponInfo.md) |  | [optional] 

## Methods

### NewNpcUnit

`func NewNpcUnit(className string, id int32, ) *NpcUnit`

NewNpcUnit instantiates a new NpcUnit object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNpcUnitWithDefaults

`func NewNpcUnitWithDefaults() *NpcUnit`

NewNpcUnitWithDefaults instantiates a new NpcUnit object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAcceleration

`func (o *NpcUnit) GetAcceleration() float64`

GetAcceleration returns the Acceleration field if non-nil, zero value otherwise.

### GetAccelerationOk

`func (o *NpcUnit) GetAccelerationOk() (*float64, bool)`

GetAccelerationOk returns a tuple with the Acceleration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAcceleration

`func (o *NpcUnit) SetAcceleration(v float64)`

SetAcceleration sets Acceleration field to given value.

### HasAcceleration

`func (o *NpcUnit) HasAcceleration() bool`

HasAcceleration returns a boolean if a field has been set.

### SetAccelerationNil

`func (o *NpcUnit) SetAccelerationNil(b bool)`

 SetAccelerationNil sets the value for Acceleration to be an explicit nil

### UnsetAcceleration
`func (o *NpcUnit) UnsetAcceleration()`

UnsetAcceleration ensures that no value is present for Acceleration, not even an explicit nil
### GetAttackT1BossMaxRange

`func (o *NpcUnit) GetAttackT1BossMaxRange() float64`

GetAttackT1BossMaxRange returns the AttackT1BossMaxRange field if non-nil, zero value otherwise.

### GetAttackT1BossMaxRangeOk

`func (o *NpcUnit) GetAttackT1BossMaxRangeOk() (*float64, bool)`

GetAttackT1BossMaxRangeOk returns a tuple with the AttackT1BossMaxRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttackT1BossMaxRange

`func (o *NpcUnit) SetAttackT1BossMaxRange(v float64)`

SetAttackT1BossMaxRange sets AttackT1BossMaxRange field to given value.

### HasAttackT1BossMaxRange

`func (o *NpcUnit) HasAttackT1BossMaxRange() bool`

HasAttackT1BossMaxRange returns a boolean if a field has been set.

### SetAttackT1BossMaxRangeNil

`func (o *NpcUnit) SetAttackT1BossMaxRangeNil(b bool)`

 SetAttackT1BossMaxRangeNil sets the value for AttackT1BossMaxRange to be an explicit nil

### UnsetAttackT1BossMaxRange
`func (o *NpcUnit) UnsetAttackT1BossMaxRange()`

UnsetAttackT1BossMaxRange ensures that no value is present for AttackT1BossMaxRange, not even an explicit nil
### GetAttackT3BossMaxRange

`func (o *NpcUnit) GetAttackT3BossMaxRange() float64`

GetAttackT3BossMaxRange returns the AttackT3BossMaxRange field if non-nil, zero value otherwise.

### GetAttackT3BossMaxRangeOk

`func (o *NpcUnit) GetAttackT3BossMaxRangeOk() (*float64, bool)`

GetAttackT3BossMaxRangeOk returns a tuple with the AttackT3BossMaxRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttackT3BossMaxRange

`func (o *NpcUnit) SetAttackT3BossMaxRange(v float64)`

SetAttackT3BossMaxRange sets AttackT3BossMaxRange field to given value.

### HasAttackT3BossMaxRange

`func (o *NpcUnit) HasAttackT3BossMaxRange() bool`

HasAttackT3BossMaxRange returns a boolean if a field has been set.

### SetAttackT3BossMaxRangeNil

`func (o *NpcUnit) SetAttackT3BossMaxRangeNil(b bool)`

 SetAttackT3BossMaxRangeNil sets the value for AttackT3BossMaxRange to be an explicit nil

### UnsetAttackT3BossMaxRange
`func (o *NpcUnit) UnsetAttackT3BossMaxRange()`

UnsetAttackT3BossMaxRange ensures that no value is present for AttackT3BossMaxRange, not even an explicit nil
### GetAttackT3BossPhase2MaxRange

`func (o *NpcUnit) GetAttackT3BossPhase2MaxRange() float64`

GetAttackT3BossPhase2MaxRange returns the AttackT3BossPhase2MaxRange field if non-nil, zero value otherwise.

### GetAttackT3BossPhase2MaxRangeOk

`func (o *NpcUnit) GetAttackT3BossPhase2MaxRangeOk() (*float64, bool)`

GetAttackT3BossPhase2MaxRangeOk returns a tuple with the AttackT3BossPhase2MaxRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttackT3BossPhase2MaxRange

`func (o *NpcUnit) SetAttackT3BossPhase2MaxRange(v float64)`

SetAttackT3BossPhase2MaxRange sets AttackT3BossPhase2MaxRange field to given value.

### HasAttackT3BossPhase2MaxRange

`func (o *NpcUnit) HasAttackT3BossPhase2MaxRange() bool`

HasAttackT3BossPhase2MaxRange returns a boolean if a field has been set.

### SetAttackT3BossPhase2MaxRangeNil

`func (o *NpcUnit) SetAttackT3BossPhase2MaxRangeNil(b bool)`

 SetAttackT3BossPhase2MaxRangeNil sets the value for AttackT3BossPhase2MaxRange to be an explicit nil

### UnsetAttackT3BossPhase2MaxRange
`func (o *NpcUnit) UnsetAttackT3BossPhase2MaxRange()`

UnsetAttackT3BossPhase2MaxRange ensures that no value is present for AttackT3BossPhase2MaxRange, not even an explicit nil
### GetAttackTrooperMaxRange

`func (o *NpcUnit) GetAttackTrooperMaxRange() float64`

GetAttackTrooperMaxRange returns the AttackTrooperMaxRange field if non-nil, zero value otherwise.

### GetAttackTrooperMaxRangeOk

`func (o *NpcUnit) GetAttackTrooperMaxRangeOk() (*float64, bool)`

GetAttackTrooperMaxRangeOk returns a tuple with the AttackTrooperMaxRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttackTrooperMaxRange

`func (o *NpcUnit) SetAttackTrooperMaxRange(v float64)`

SetAttackTrooperMaxRange sets AttackTrooperMaxRange field to given value.

### HasAttackTrooperMaxRange

`func (o *NpcUnit) HasAttackTrooperMaxRange() bool`

HasAttackTrooperMaxRange returns a boolean if a field has been set.

### SetAttackTrooperMaxRangeNil

`func (o *NpcUnit) SetAttackTrooperMaxRangeNil(b bool)`

 SetAttackTrooperMaxRangeNil sets the value for AttackTrooperMaxRange to be an explicit nil

### UnsetAttackTrooperMaxRange
`func (o *NpcUnit) UnsetAttackTrooperMaxRange()`

UnsetAttackTrooperMaxRange ensures that no value is present for AttackTrooperMaxRange, not even an explicit nil
### GetBackdoorBulletResistModifier

`func (o *NpcUnit) GetBackdoorBulletResistModifier() SubclassBulletResistModifier`

GetBackdoorBulletResistModifier returns the BackdoorBulletResistModifier field if non-nil, zero value otherwise.

### GetBackdoorBulletResistModifierOk

`func (o *NpcUnit) GetBackdoorBulletResistModifierOk() (*SubclassBulletResistModifier, bool)`

GetBackdoorBulletResistModifierOk returns a tuple with the BackdoorBulletResistModifier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBackdoorBulletResistModifier

`func (o *NpcUnit) SetBackdoorBulletResistModifier(v SubclassBulletResistModifier)`

SetBackdoorBulletResistModifier sets BackdoorBulletResistModifier field to given value.

### HasBackdoorBulletResistModifier

`func (o *NpcUnit) HasBackdoorBulletResistModifier() bool`

HasBackdoorBulletResistModifier returns a boolean if a field has been set.

### SetBackdoorBulletResistModifierNil

`func (o *NpcUnit) SetBackdoorBulletResistModifierNil(b bool)`

 SetBackdoorBulletResistModifierNil sets the value for BackdoorBulletResistModifier to be an explicit nil

### UnsetBackdoorBulletResistModifier
`func (o *NpcUnit) UnsetBackdoorBulletResistModifier()`

UnsetBackdoorBulletResistModifier ensures that no value is present for BackdoorBulletResistModifier, not even an explicit nil
### GetBarrackBossDps

`func (o *NpcUnit) GetBarrackBossDps() float64`

GetBarrackBossDps returns the BarrackBossDps field if non-nil, zero value otherwise.

### GetBarrackBossDpsOk

`func (o *NpcUnit) GetBarrackBossDpsOk() (*float64, bool)`

GetBarrackBossDpsOk returns a tuple with the BarrackBossDps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBarrackBossDps

`func (o *NpcUnit) SetBarrackBossDps(v float64)`

SetBarrackBossDps sets BarrackBossDps field to given value.

### HasBarrackBossDps

`func (o *NpcUnit) HasBarrackBossDps() bool`

HasBarrackBossDps returns a boolean if a field has been set.

### SetBarrackBossDpsNil

`func (o *NpcUnit) SetBarrackBossDpsNil(b bool)`

 SetBarrackBossDpsNil sets the value for BarrackBossDps to be an explicit nil

### UnsetBarrackBossDps
`func (o *NpcUnit) UnsetBarrackBossDps()`

UnsetBarrackBossDps ensures that no value is present for BarrackBossDps, not even an explicit nil
### GetBarrackGuardianDamageResistPct

`func (o *NpcUnit) GetBarrackGuardianDamageResistPct() float64`

GetBarrackGuardianDamageResistPct returns the BarrackGuardianDamageResistPct field if non-nil, zero value otherwise.

### GetBarrackGuardianDamageResistPctOk

`func (o *NpcUnit) GetBarrackGuardianDamageResistPctOk() (*float64, bool)`

GetBarrackGuardianDamageResistPctOk returns a tuple with the BarrackGuardianDamageResistPct field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBarrackGuardianDamageResistPct

`func (o *NpcUnit) SetBarrackGuardianDamageResistPct(v float64)`

SetBarrackGuardianDamageResistPct sets BarrackGuardianDamageResistPct field to given value.

### HasBarrackGuardianDamageResistPct

`func (o *NpcUnit) HasBarrackGuardianDamageResistPct() bool`

HasBarrackGuardianDamageResistPct returns a boolean if a field has been set.

### SetBarrackGuardianDamageResistPctNil

`func (o *NpcUnit) SetBarrackGuardianDamageResistPctNil(b bool)`

 SetBarrackGuardianDamageResistPctNil sets the value for BarrackGuardianDamageResistPct to be an explicit nil

### UnsetBarrackGuardianDamageResistPct
`func (o *NpcUnit) UnsetBarrackGuardianDamageResistPct()`

UnsetBarrackGuardianDamageResistPct ensures that no value is present for BarrackGuardianDamageResistPct, not even an explicit nil
### GetBoundAbilities

`func (o *NpcUnit) GetBoundAbilities() map[string]string`

GetBoundAbilities returns the BoundAbilities field if non-nil, zero value otherwise.

### GetBoundAbilitiesOk

`func (o *NpcUnit) GetBoundAbilitiesOk() (*map[string]string, bool)`

GetBoundAbilitiesOk returns a tuple with the BoundAbilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBoundAbilities

`func (o *NpcUnit) SetBoundAbilities(v map[string]string)`

SetBoundAbilities sets BoundAbilities field to given value.

### HasBoundAbilities

`func (o *NpcUnit) HasBoundAbilities() bool`

HasBoundAbilities returns a boolean if a field has been set.

### GetClassName

`func (o *NpcUnit) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *NpcUnit) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *NpcUnit) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetEmpoweredModifierLevel1

`func (o *NpcUnit) GetEmpoweredModifierLevel1() SubclassEmpoweredModifierLevel`

GetEmpoweredModifierLevel1 returns the EmpoweredModifierLevel1 field if non-nil, zero value otherwise.

### GetEmpoweredModifierLevel1Ok

`func (o *NpcUnit) GetEmpoweredModifierLevel1Ok() (*SubclassEmpoweredModifierLevel, bool)`

GetEmpoweredModifierLevel1Ok returns a tuple with the EmpoweredModifierLevel1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmpoweredModifierLevel1

`func (o *NpcUnit) SetEmpoweredModifierLevel1(v SubclassEmpoweredModifierLevel)`

SetEmpoweredModifierLevel1 sets EmpoweredModifierLevel1 field to given value.

### HasEmpoweredModifierLevel1

`func (o *NpcUnit) HasEmpoweredModifierLevel1() bool`

HasEmpoweredModifierLevel1 returns a boolean if a field has been set.

### SetEmpoweredModifierLevel1Nil

`func (o *NpcUnit) SetEmpoweredModifierLevel1Nil(b bool)`

 SetEmpoweredModifierLevel1Nil sets the value for EmpoweredModifierLevel1 to be an explicit nil

### UnsetEmpoweredModifierLevel1
`func (o *NpcUnit) UnsetEmpoweredModifierLevel1()`

UnsetEmpoweredModifierLevel1 ensures that no value is present for EmpoweredModifierLevel1, not even an explicit nil
### GetEmpoweredModifierLevel2

`func (o *NpcUnit) GetEmpoweredModifierLevel2() SubclassEmpoweredModifierLevel`

GetEmpoweredModifierLevel2 returns the EmpoweredModifierLevel2 field if non-nil, zero value otherwise.

### GetEmpoweredModifierLevel2Ok

`func (o *NpcUnit) GetEmpoweredModifierLevel2Ok() (*SubclassEmpoweredModifierLevel, bool)`

GetEmpoweredModifierLevel2Ok returns a tuple with the EmpoweredModifierLevel2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmpoweredModifierLevel2

`func (o *NpcUnit) SetEmpoweredModifierLevel2(v SubclassEmpoweredModifierLevel)`

SetEmpoweredModifierLevel2 sets EmpoweredModifierLevel2 field to given value.

### HasEmpoweredModifierLevel2

`func (o *NpcUnit) HasEmpoweredModifierLevel2() bool`

HasEmpoweredModifierLevel2 returns a boolean if a field has been set.

### SetEmpoweredModifierLevel2Nil

`func (o *NpcUnit) SetEmpoweredModifierLevel2Nil(b bool)`

 SetEmpoweredModifierLevel2Nil sets the value for EmpoweredModifierLevel2 to be an explicit nil

### UnsetEmpoweredModifierLevel2
`func (o *NpcUnit) UnsetEmpoweredModifierLevel2()`

UnsetEmpoweredModifierLevel2 ensures that no value is present for EmpoweredModifierLevel2, not even an explicit nil
### GetEnemyTrooperDamageReduction

`func (o *NpcUnit) GetEnemyTrooperDamageReduction() SubclassTrooperDamageReduction`

GetEnemyTrooperDamageReduction returns the EnemyTrooperDamageReduction field if non-nil, zero value otherwise.

### GetEnemyTrooperDamageReductionOk

`func (o *NpcUnit) GetEnemyTrooperDamageReductionOk() (*SubclassTrooperDamageReduction, bool)`

GetEnemyTrooperDamageReductionOk returns a tuple with the EnemyTrooperDamageReduction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyTrooperDamageReduction

`func (o *NpcUnit) SetEnemyTrooperDamageReduction(v SubclassTrooperDamageReduction)`

SetEnemyTrooperDamageReduction sets EnemyTrooperDamageReduction field to given value.

### HasEnemyTrooperDamageReduction

`func (o *NpcUnit) HasEnemyTrooperDamageReduction() bool`

HasEnemyTrooperDamageReduction returns a boolean if a field has been set.

### SetEnemyTrooperDamageReductionNil

`func (o *NpcUnit) SetEnemyTrooperDamageReductionNil(b bool)`

 SetEnemyTrooperDamageReductionNil sets the value for EnemyTrooperDamageReduction to be an explicit nil

### UnsetEnemyTrooperDamageReduction
`func (o *NpcUnit) UnsetEnemyTrooperDamageReduction()`

UnsetEnemyTrooperDamageReduction ensures that no value is present for EnemyTrooperDamageReduction, not even an explicit nil
### GetEnemyTrooperProtectionRange

`func (o *NpcUnit) GetEnemyTrooperProtectionRange() float64`

GetEnemyTrooperProtectionRange returns the EnemyTrooperProtectionRange field if non-nil, zero value otherwise.

### GetEnemyTrooperProtectionRangeOk

`func (o *NpcUnit) GetEnemyTrooperProtectionRangeOk() (*float64, bool)`

GetEnemyTrooperProtectionRangeOk returns a tuple with the EnemyTrooperProtectionRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyTrooperProtectionRange

`func (o *NpcUnit) SetEnemyTrooperProtectionRange(v float64)`

SetEnemyTrooperProtectionRange sets EnemyTrooperProtectionRange field to given value.

### HasEnemyTrooperProtectionRange

`func (o *NpcUnit) HasEnemyTrooperProtectionRange() bool`

HasEnemyTrooperProtectionRange returns a boolean if a field has been set.

### SetEnemyTrooperProtectionRangeNil

`func (o *NpcUnit) SetEnemyTrooperProtectionRangeNil(b bool)`

 SetEnemyTrooperProtectionRangeNil sets the value for EnemyTrooperProtectionRange to be an explicit nil

### UnsetEnemyTrooperProtectionRange
`func (o *NpcUnit) UnsetEnemyTrooperProtectionRange()`

UnsetEnemyTrooperProtectionRange ensures that no value is present for EnemyTrooperProtectionRange, not even an explicit nil
### GetGeneratorBossDps

`func (o *NpcUnit) GetGeneratorBossDps() float64`

GetGeneratorBossDps returns the GeneratorBossDps field if non-nil, zero value otherwise.

### GetGeneratorBossDpsOk

`func (o *NpcUnit) GetGeneratorBossDpsOk() (*float64, bool)`

GetGeneratorBossDpsOk returns a tuple with the GeneratorBossDps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGeneratorBossDps

`func (o *NpcUnit) SetGeneratorBossDps(v float64)`

SetGeneratorBossDps sets GeneratorBossDps field to given value.

### HasGeneratorBossDps

`func (o *NpcUnit) HasGeneratorBossDps() bool`

HasGeneratorBossDps returns a boolean if a field has been set.

### SetGeneratorBossDpsNil

`func (o *NpcUnit) SetGeneratorBossDpsNil(b bool)`

 SetGeneratorBossDpsNil sets the value for GeneratorBossDps to be an explicit nil

### UnsetGeneratorBossDps
`func (o *NpcUnit) UnsetGeneratorBossDps()`

UnsetGeneratorBossDps ensures that no value is present for GeneratorBossDps, not even an explicit nil
### GetGoldReward

`func (o *NpcUnit) GetGoldReward() float64`

GetGoldReward returns the GoldReward field if non-nil, zero value otherwise.

### GetGoldRewardOk

`func (o *NpcUnit) GetGoldRewardOk() (*float64, bool)`

GetGoldRewardOk returns a tuple with the GoldReward field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldReward

`func (o *NpcUnit) SetGoldReward(v float64)`

SetGoldReward sets GoldReward field to given value.

### HasGoldReward

`func (o *NpcUnit) HasGoldReward() bool`

HasGoldReward returns a boolean if a field has been set.

### SetGoldRewardNil

`func (o *NpcUnit) SetGoldRewardNil(b bool)`

 SetGoldRewardNil sets the value for GoldReward to be an explicit nil

### UnsetGoldReward
`func (o *NpcUnit) UnsetGoldReward()`

UnsetGoldReward ensures that no value is present for GoldReward, not even an explicit nil
### GetGoldRewardBonusPercentPerMinute

`func (o *NpcUnit) GetGoldRewardBonusPercentPerMinute() float64`

GetGoldRewardBonusPercentPerMinute returns the GoldRewardBonusPercentPerMinute field if non-nil, zero value otherwise.

### GetGoldRewardBonusPercentPerMinuteOk

`func (o *NpcUnit) GetGoldRewardBonusPercentPerMinuteOk() (*float64, bool)`

GetGoldRewardBonusPercentPerMinuteOk returns a tuple with the GoldRewardBonusPercentPerMinute field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldRewardBonusPercentPerMinute

`func (o *NpcUnit) SetGoldRewardBonusPercentPerMinute(v float64)`

SetGoldRewardBonusPercentPerMinute sets GoldRewardBonusPercentPerMinute field to given value.

### HasGoldRewardBonusPercentPerMinute

`func (o *NpcUnit) HasGoldRewardBonusPercentPerMinute() bool`

HasGoldRewardBonusPercentPerMinute returns a boolean if a field has been set.

### SetGoldRewardBonusPercentPerMinuteNil

`func (o *NpcUnit) SetGoldRewardBonusPercentPerMinuteNil(b bool)`

 SetGoldRewardBonusPercentPerMinuteNil sets the value for GoldRewardBonusPercentPerMinute to be an explicit nil

### UnsetGoldRewardBonusPercentPerMinute
`func (o *NpcUnit) UnsetGoldRewardBonusPercentPerMinute()`

UnsetGoldRewardBonusPercentPerMinute ensures that no value is present for GoldRewardBonusPercentPerMinute, not even an explicit nil
### GetHealthBarColorEnemy

`func (o *NpcUnit) GetHealthBarColorEnemy() Color`

GetHealthBarColorEnemy returns the HealthBarColorEnemy field if non-nil, zero value otherwise.

### GetHealthBarColorEnemyOk

`func (o *NpcUnit) GetHealthBarColorEnemyOk() (*Color, bool)`

GetHealthBarColorEnemyOk returns a tuple with the HealthBarColorEnemy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHealthBarColorEnemy

`func (o *NpcUnit) SetHealthBarColorEnemy(v Color)`

SetHealthBarColorEnemy sets HealthBarColorEnemy field to given value.

### HasHealthBarColorEnemy

`func (o *NpcUnit) HasHealthBarColorEnemy() bool`

HasHealthBarColorEnemy returns a boolean if a field has been set.

### SetHealthBarColorEnemyNil

`func (o *NpcUnit) SetHealthBarColorEnemyNil(b bool)`

 SetHealthBarColorEnemyNil sets the value for HealthBarColorEnemy to be an explicit nil

### UnsetHealthBarColorEnemy
`func (o *NpcUnit) UnsetHealthBarColorEnemy()`

UnsetHealthBarColorEnemy ensures that no value is present for HealthBarColorEnemy, not even an explicit nil
### GetHealthBarColorFriend

`func (o *NpcUnit) GetHealthBarColorFriend() Color`

GetHealthBarColorFriend returns the HealthBarColorFriend field if non-nil, zero value otherwise.

### GetHealthBarColorFriendOk

`func (o *NpcUnit) GetHealthBarColorFriendOk() (*Color, bool)`

GetHealthBarColorFriendOk returns a tuple with the HealthBarColorFriend field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHealthBarColorFriend

`func (o *NpcUnit) SetHealthBarColorFriend(v Color)`

SetHealthBarColorFriend sets HealthBarColorFriend field to given value.

### HasHealthBarColorFriend

`func (o *NpcUnit) HasHealthBarColorFriend() bool`

HasHealthBarColorFriend returns a boolean if a field has been set.

### SetHealthBarColorFriendNil

`func (o *NpcUnit) SetHealthBarColorFriendNil(b bool)`

 SetHealthBarColorFriendNil sets the value for HealthBarColorFriend to be an explicit nil

### UnsetHealthBarColorFriend
`func (o *NpcUnit) UnsetHealthBarColorFriend()`

UnsetHealthBarColorFriend ensures that no value is present for HealthBarColorFriend, not even an explicit nil
### GetHealthBarColorTeam1

`func (o *NpcUnit) GetHealthBarColorTeam1() Color`

GetHealthBarColorTeam1 returns the HealthBarColorTeam1 field if non-nil, zero value otherwise.

### GetHealthBarColorTeam1Ok

`func (o *NpcUnit) GetHealthBarColorTeam1Ok() (*Color, bool)`

GetHealthBarColorTeam1Ok returns a tuple with the HealthBarColorTeam1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHealthBarColorTeam1

`func (o *NpcUnit) SetHealthBarColorTeam1(v Color)`

SetHealthBarColorTeam1 sets HealthBarColorTeam1 field to given value.

### HasHealthBarColorTeam1

`func (o *NpcUnit) HasHealthBarColorTeam1() bool`

HasHealthBarColorTeam1 returns a boolean if a field has been set.

### SetHealthBarColorTeam1Nil

`func (o *NpcUnit) SetHealthBarColorTeam1Nil(b bool)`

 SetHealthBarColorTeam1Nil sets the value for HealthBarColorTeam1 to be an explicit nil

### UnsetHealthBarColorTeam1
`func (o *NpcUnit) UnsetHealthBarColorTeam1()`

UnsetHealthBarColorTeam1 ensures that no value is present for HealthBarColorTeam1, not even an explicit nil
### GetHealthBarColorTeam2

`func (o *NpcUnit) GetHealthBarColorTeam2() Color`

GetHealthBarColorTeam2 returns the HealthBarColorTeam2 field if non-nil, zero value otherwise.

### GetHealthBarColorTeam2Ok

`func (o *NpcUnit) GetHealthBarColorTeam2Ok() (*Color, bool)`

GetHealthBarColorTeam2Ok returns a tuple with the HealthBarColorTeam2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHealthBarColorTeam2

`func (o *NpcUnit) SetHealthBarColorTeam2(v Color)`

SetHealthBarColorTeam2 sets HealthBarColorTeam2 field to given value.

### HasHealthBarColorTeam2

`func (o *NpcUnit) HasHealthBarColorTeam2() bool`

HasHealthBarColorTeam2 returns a boolean if a field has been set.

### SetHealthBarColorTeam2Nil

`func (o *NpcUnit) SetHealthBarColorTeam2Nil(b bool)`

 SetHealthBarColorTeam2Nil sets the value for HealthBarColorTeam2 to be an explicit nil

### UnsetHealthBarColorTeam2
`func (o *NpcUnit) UnsetHealthBarColorTeam2()`

UnsetHealthBarColorTeam2 ensures that no value is present for HealthBarColorTeam2, not even an explicit nil
### GetHealthBarColorTeamNeutral

`func (o *NpcUnit) GetHealthBarColorTeamNeutral() Color`

GetHealthBarColorTeamNeutral returns the HealthBarColorTeamNeutral field if non-nil, zero value otherwise.

### GetHealthBarColorTeamNeutralOk

`func (o *NpcUnit) GetHealthBarColorTeamNeutralOk() (*Color, bool)`

GetHealthBarColorTeamNeutralOk returns a tuple with the HealthBarColorTeamNeutral field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHealthBarColorTeamNeutral

`func (o *NpcUnit) SetHealthBarColorTeamNeutral(v Color)`

SetHealthBarColorTeamNeutral sets HealthBarColorTeamNeutral field to given value.

### HasHealthBarColorTeamNeutral

`func (o *NpcUnit) HasHealthBarColorTeamNeutral() bool`

HasHealthBarColorTeamNeutral returns a boolean if a field has been set.

### SetHealthBarColorTeamNeutralNil

`func (o *NpcUnit) SetHealthBarColorTeamNeutralNil(b bool)`

 SetHealthBarColorTeamNeutralNil sets the value for HealthBarColorTeamNeutral to be an explicit nil

### UnsetHealthBarColorTeamNeutral
`func (o *NpcUnit) UnsetHealthBarColorTeamNeutral()`

UnsetHealthBarColorTeamNeutral ensures that no value is present for HealthBarColorTeamNeutral, not even an explicit nil
### GetId

`func (o *NpcUnit) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *NpcUnit) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *NpcUnit) SetId(v int32)`

SetId sets Id field to given value.


### GetIntrinsicModifiers

`func (o *NpcUnit) GetIntrinsicModifiers() []SubclassIntrinsicModifiers`

GetIntrinsicModifiers returns the IntrinsicModifiers field if non-nil, zero value otherwise.

### GetIntrinsicModifiersOk

`func (o *NpcUnit) GetIntrinsicModifiersOk() (*[]SubclassIntrinsicModifiers, bool)`

GetIntrinsicModifiersOk returns a tuple with the IntrinsicModifiers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIntrinsicModifiers

`func (o *NpcUnit) SetIntrinsicModifiers(v []SubclassIntrinsicModifiers)`

SetIntrinsicModifiers sets IntrinsicModifiers field to given value.

### HasIntrinsicModifiers

`func (o *NpcUnit) HasIntrinsicModifiers() bool`

HasIntrinsicModifiers returns a boolean if a field has been set.

### SetIntrinsicModifiersNil

`func (o *NpcUnit) SetIntrinsicModifiersNil(b bool)`

 SetIntrinsicModifiersNil sets the value for IntrinsicModifiers to be an explicit nil

### UnsetIntrinsicModifiers
`func (o *NpcUnit) UnsetIntrinsicModifiers()`

UnsetIntrinsicModifiers ensures that no value is present for IntrinsicModifiers, not even an explicit nil
### GetLaserDpsMaxHealth

`func (o *NpcUnit) GetLaserDpsMaxHealth() float64`

GetLaserDpsMaxHealth returns the LaserDpsMaxHealth field if non-nil, zero value otherwise.

### GetLaserDpsMaxHealthOk

`func (o *NpcUnit) GetLaserDpsMaxHealthOk() (*float64, bool)`

GetLaserDpsMaxHealthOk returns a tuple with the LaserDpsMaxHealth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLaserDpsMaxHealth

`func (o *NpcUnit) SetLaserDpsMaxHealth(v float64)`

SetLaserDpsMaxHealth sets LaserDpsMaxHealth field to given value.

### HasLaserDpsMaxHealth

`func (o *NpcUnit) HasLaserDpsMaxHealth() bool`

HasLaserDpsMaxHealth returns a boolean if a field has been set.

### SetLaserDpsMaxHealthNil

`func (o *NpcUnit) SetLaserDpsMaxHealthNil(b bool)`

 SetLaserDpsMaxHealthNil sets the value for LaserDpsMaxHealth to be an explicit nil

### UnsetLaserDpsMaxHealth
`func (o *NpcUnit) UnsetLaserDpsMaxHealth()`

UnsetLaserDpsMaxHealth ensures that no value is present for LaserDpsMaxHealth, not even an explicit nil
### GetLaserDpsToPlayers

`func (o *NpcUnit) GetLaserDpsToPlayers() float64`

GetLaserDpsToPlayers returns the LaserDpsToPlayers field if non-nil, zero value otherwise.

### GetLaserDpsToPlayersOk

`func (o *NpcUnit) GetLaserDpsToPlayersOk() (*float64, bool)`

GetLaserDpsToPlayersOk returns a tuple with the LaserDpsToPlayers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLaserDpsToPlayers

`func (o *NpcUnit) SetLaserDpsToPlayers(v float64)`

SetLaserDpsToPlayers sets LaserDpsToPlayers field to given value.

### HasLaserDpsToPlayers

`func (o *NpcUnit) HasLaserDpsToPlayers() bool`

HasLaserDpsToPlayers returns a boolean if a field has been set.

### SetLaserDpsToPlayersNil

`func (o *NpcUnit) SetLaserDpsToPlayersNil(b bool)`

 SetLaserDpsToPlayersNil sets the value for LaserDpsToPlayers to be an explicit nil

### UnsetLaserDpsToPlayers
`func (o *NpcUnit) UnsetLaserDpsToPlayers()`

UnsetLaserDpsToPlayers ensures that no value is present for LaserDpsToPlayers, not even an explicit nil
### GetMaxHealth

`func (o *NpcUnit) GetMaxHealth() int64`

GetMaxHealth returns the MaxHealth field if non-nil, zero value otherwise.

### GetMaxHealthOk

`func (o *NpcUnit) GetMaxHealthOk() (*int64, bool)`

GetMaxHealthOk returns a tuple with the MaxHealth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxHealth

`func (o *NpcUnit) SetMaxHealth(v int64)`

SetMaxHealth sets MaxHealth field to given value.

### HasMaxHealth

`func (o *NpcUnit) HasMaxHealth() bool`

HasMaxHealth returns a boolean if a field has been set.

### SetMaxHealthNil

`func (o *NpcUnit) SetMaxHealthNil(b bool)`

 SetMaxHealthNil sets the value for MaxHealth to be an explicit nil

### UnsetMaxHealth
`func (o *NpcUnit) UnsetMaxHealth()`

UnsetMaxHealth ensures that no value is present for MaxHealth, not even an explicit nil
### GetMaxHealthFinal

`func (o *NpcUnit) GetMaxHealthFinal() int64`

GetMaxHealthFinal returns the MaxHealthFinal field if non-nil, zero value otherwise.

### GetMaxHealthFinalOk

`func (o *NpcUnit) GetMaxHealthFinalOk() (*int64, bool)`

GetMaxHealthFinalOk returns a tuple with the MaxHealthFinal field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxHealthFinal

`func (o *NpcUnit) SetMaxHealthFinal(v int64)`

SetMaxHealthFinal sets MaxHealthFinal field to given value.

### HasMaxHealthFinal

`func (o *NpcUnit) HasMaxHealthFinal() bool`

HasMaxHealthFinal returns a boolean if a field has been set.

### SetMaxHealthFinalNil

`func (o *NpcUnit) SetMaxHealthFinalNil(b bool)`

 SetMaxHealthFinalNil sets the value for MaxHealthFinal to be an explicit nil

### UnsetMaxHealthFinal
`func (o *NpcUnit) UnsetMaxHealthFinal()`

UnsetMaxHealthFinal ensures that no value is present for MaxHealthFinal, not even an explicit nil
### GetMaxHealthGenerator

`func (o *NpcUnit) GetMaxHealthGenerator() int64`

GetMaxHealthGenerator returns the MaxHealthGenerator field if non-nil, zero value otherwise.

### GetMaxHealthGeneratorOk

`func (o *NpcUnit) GetMaxHealthGeneratorOk() (*int64, bool)`

GetMaxHealthGeneratorOk returns a tuple with the MaxHealthGenerator field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxHealthGenerator

`func (o *NpcUnit) SetMaxHealthGenerator(v int64)`

SetMaxHealthGenerator sets MaxHealthGenerator field to given value.

### HasMaxHealthGenerator

`func (o *NpcUnit) HasMaxHealthGenerator() bool`

HasMaxHealthGenerator returns a boolean if a field has been set.

### SetMaxHealthGeneratorNil

`func (o *NpcUnit) SetMaxHealthGeneratorNil(b bool)`

 SetMaxHealthGeneratorNil sets the value for MaxHealthGenerator to be an explicit nil

### UnsetMaxHealthGenerator
`func (o *NpcUnit) UnsetMaxHealthGenerator()`

UnsetMaxHealthGenerator ensures that no value is present for MaxHealthGenerator, not even an explicit nil
### GetMeleeAttemptRange

`func (o *NpcUnit) GetMeleeAttemptRange() float64`

GetMeleeAttemptRange returns the MeleeAttemptRange field if non-nil, zero value otherwise.

### GetMeleeAttemptRangeOk

`func (o *NpcUnit) GetMeleeAttemptRangeOk() (*float64, bool)`

GetMeleeAttemptRangeOk returns a tuple with the MeleeAttemptRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeleeAttemptRange

`func (o *NpcUnit) SetMeleeAttemptRange(v float64)`

SetMeleeAttemptRange sets MeleeAttemptRange field to given value.

### HasMeleeAttemptRange

`func (o *NpcUnit) HasMeleeAttemptRange() bool`

HasMeleeAttemptRange returns a boolean if a field has been set.

### SetMeleeAttemptRangeNil

`func (o *NpcUnit) SetMeleeAttemptRangeNil(b bool)`

 SetMeleeAttemptRangeNil sets the value for MeleeAttemptRange to be an explicit nil

### UnsetMeleeAttemptRange
`func (o *NpcUnit) UnsetMeleeAttemptRange()`

UnsetMeleeAttemptRange ensures that no value is present for MeleeAttemptRange, not even an explicit nil
### GetMeleeDamage

`func (o *NpcUnit) GetMeleeDamage() float64`

GetMeleeDamage returns the MeleeDamage field if non-nil, zero value otherwise.

### GetMeleeDamageOk

`func (o *NpcUnit) GetMeleeDamageOk() (*float64, bool)`

GetMeleeDamageOk returns a tuple with the MeleeDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeleeDamage

`func (o *NpcUnit) SetMeleeDamage(v float64)`

SetMeleeDamage sets MeleeDamage field to given value.

### HasMeleeDamage

`func (o *NpcUnit) HasMeleeDamage() bool`

HasMeleeDamage returns a boolean if a field has been set.

### SetMeleeDamageNil

`func (o *NpcUnit) SetMeleeDamageNil(b bool)`

 SetMeleeDamageNil sets the value for MeleeDamage to be an explicit nil

### UnsetMeleeDamage
`func (o *NpcUnit) UnsetMeleeDamage()`

UnsetMeleeDamage ensures that no value is present for MeleeDamage, not even an explicit nil
### GetMeleeDuration

`func (o *NpcUnit) GetMeleeDuration() float64`

GetMeleeDuration returns the MeleeDuration field if non-nil, zero value otherwise.

### GetMeleeDurationOk

`func (o *NpcUnit) GetMeleeDurationOk() (*float64, bool)`

GetMeleeDurationOk returns a tuple with the MeleeDuration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeleeDuration

`func (o *NpcUnit) SetMeleeDuration(v float64)`

SetMeleeDuration sets MeleeDuration field to given value.

### HasMeleeDuration

`func (o *NpcUnit) HasMeleeDuration() bool`

HasMeleeDuration returns a boolean if a field has been set.

### SetMeleeDurationNil

`func (o *NpcUnit) SetMeleeDurationNil(b bool)`

 SetMeleeDurationNil sets the value for MeleeDuration to be an explicit nil

### UnsetMeleeDuration
`func (o *NpcUnit) UnsetMeleeDuration()`

UnsetMeleeDuration ensures that no value is present for MeleeDuration, not even an explicit nil
### GetMeleeHitRange

`func (o *NpcUnit) GetMeleeHitRange() float64`

GetMeleeHitRange returns the MeleeHitRange field if non-nil, zero value otherwise.

### GetMeleeHitRangeOk

`func (o *NpcUnit) GetMeleeHitRangeOk() (*float64, bool)`

GetMeleeHitRangeOk returns a tuple with the MeleeHitRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeleeHitRange

`func (o *NpcUnit) SetMeleeHitRange(v float64)`

SetMeleeHitRange sets MeleeHitRange field to given value.

### HasMeleeHitRange

`func (o *NpcUnit) HasMeleeHitRange() bool`

HasMeleeHitRange returns a boolean if a field has been set.

### SetMeleeHitRangeNil

`func (o *NpcUnit) SetMeleeHitRangeNil(b bool)`

 SetMeleeHitRangeNil sets the value for MeleeHitRange to be an explicit nil

### UnsetMeleeHitRange
`func (o *NpcUnit) UnsetMeleeHitRange()`

UnsetMeleeHitRange ensures that no value is present for MeleeHitRange, not even an explicit nil
### GetNearDeathDuration

`func (o *NpcUnit) GetNearDeathDuration() float64`

GetNearDeathDuration returns the NearDeathDuration field if non-nil, zero value otherwise.

### GetNearDeathDurationOk

`func (o *NpcUnit) GetNearDeathDurationOk() (*float64, bool)`

GetNearDeathDurationOk returns a tuple with the NearDeathDuration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNearDeathDuration

`func (o *NpcUnit) SetNearDeathDuration(v float64)`

SetNearDeathDuration sets NearDeathDuration field to given value.

### HasNearDeathDuration

`func (o *NpcUnit) HasNearDeathDuration() bool`

HasNearDeathDuration returns a boolean if a field has been set.

### SetNearDeathDurationNil

`func (o *NpcUnit) SetNearDeathDurationNil(b bool)`

 SetNearDeathDurationNil sets the value for NearDeathDuration to be an explicit nil

### UnsetNearDeathDuration
`func (o *NpcUnit) UnsetNearDeathDuration()`

UnsetNearDeathDuration ensures that no value is present for NearDeathDuration, not even an explicit nil
### GetNoShieldLaserDpsToPlayers

`func (o *NpcUnit) GetNoShieldLaserDpsToPlayers() float64`

GetNoShieldLaserDpsToPlayers returns the NoShieldLaserDpsToPlayers field if non-nil, zero value otherwise.

### GetNoShieldLaserDpsToPlayersOk

`func (o *NpcUnit) GetNoShieldLaserDpsToPlayersOk() (*float64, bool)`

GetNoShieldLaserDpsToPlayersOk returns a tuple with the NoShieldLaserDpsToPlayers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNoShieldLaserDpsToPlayers

`func (o *NpcUnit) SetNoShieldLaserDpsToPlayers(v float64)`

SetNoShieldLaserDpsToPlayers sets NoShieldLaserDpsToPlayers field to given value.

### HasNoShieldLaserDpsToPlayers

`func (o *NpcUnit) HasNoShieldLaserDpsToPlayers() bool`

HasNoShieldLaserDpsToPlayers returns a boolean if a field has been set.

### SetNoShieldLaserDpsToPlayersNil

`func (o *NpcUnit) SetNoShieldLaserDpsToPlayersNil(b bool)`

 SetNoShieldLaserDpsToPlayersNil sets the value for NoShieldLaserDpsToPlayers to be an explicit nil

### UnsetNoShieldLaserDpsToPlayers
`func (o *NpcUnit) UnsetNoShieldLaserDpsToPlayers()`

UnsetNoShieldLaserDpsToPlayers ensures that no value is present for NoShieldLaserDpsToPlayers, not even an explicit nil
### GetObjectiveHealthGrowthPhase1

`func (o *NpcUnit) GetObjectiveHealthGrowthPhase1() SubclassObjectiveHealthGrowthPhase`

GetObjectiveHealthGrowthPhase1 returns the ObjectiveHealthGrowthPhase1 field if non-nil, zero value otherwise.

### GetObjectiveHealthGrowthPhase1Ok

`func (o *NpcUnit) GetObjectiveHealthGrowthPhase1Ok() (*SubclassObjectiveHealthGrowthPhase, bool)`

GetObjectiveHealthGrowthPhase1Ok returns a tuple with the ObjectiveHealthGrowthPhase1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectiveHealthGrowthPhase1

`func (o *NpcUnit) SetObjectiveHealthGrowthPhase1(v SubclassObjectiveHealthGrowthPhase)`

SetObjectiveHealthGrowthPhase1 sets ObjectiveHealthGrowthPhase1 field to given value.

### HasObjectiveHealthGrowthPhase1

`func (o *NpcUnit) HasObjectiveHealthGrowthPhase1() bool`

HasObjectiveHealthGrowthPhase1 returns a boolean if a field has been set.

### SetObjectiveHealthGrowthPhase1Nil

`func (o *NpcUnit) SetObjectiveHealthGrowthPhase1Nil(b bool)`

 SetObjectiveHealthGrowthPhase1Nil sets the value for ObjectiveHealthGrowthPhase1 to be an explicit nil

### UnsetObjectiveHealthGrowthPhase1
`func (o *NpcUnit) UnsetObjectiveHealthGrowthPhase1()`

UnsetObjectiveHealthGrowthPhase1 ensures that no value is present for ObjectiveHealthGrowthPhase1, not even an explicit nil
### GetObjectiveHealthGrowthPhase2

`func (o *NpcUnit) GetObjectiveHealthGrowthPhase2() SubclassObjectiveHealthGrowthPhase`

GetObjectiveHealthGrowthPhase2 returns the ObjectiveHealthGrowthPhase2 field if non-nil, zero value otherwise.

### GetObjectiveHealthGrowthPhase2Ok

`func (o *NpcUnit) GetObjectiveHealthGrowthPhase2Ok() (*SubclassObjectiveHealthGrowthPhase, bool)`

GetObjectiveHealthGrowthPhase2Ok returns a tuple with the ObjectiveHealthGrowthPhase2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectiveHealthGrowthPhase2

`func (o *NpcUnit) SetObjectiveHealthGrowthPhase2(v SubclassObjectiveHealthGrowthPhase)`

SetObjectiveHealthGrowthPhase2 sets ObjectiveHealthGrowthPhase2 field to given value.

### HasObjectiveHealthGrowthPhase2

`func (o *NpcUnit) HasObjectiveHealthGrowthPhase2() bool`

HasObjectiveHealthGrowthPhase2 returns a boolean if a field has been set.

### SetObjectiveHealthGrowthPhase2Nil

`func (o *NpcUnit) SetObjectiveHealthGrowthPhase2Nil(b bool)`

 SetObjectiveHealthGrowthPhase2Nil sets the value for ObjectiveHealthGrowthPhase2 to be an explicit nil

### UnsetObjectiveHealthGrowthPhase2
`func (o *NpcUnit) UnsetObjectiveHealthGrowthPhase2()`

UnsetObjectiveHealthGrowthPhase2 ensures that no value is present for ObjectiveHealthGrowthPhase2, not even an explicit nil
### GetObjectiveRegen

`func (o *NpcUnit) GetObjectiveRegen() SubclassObjectiveRegen`

GetObjectiveRegen returns the ObjectiveRegen field if non-nil, zero value otherwise.

### GetObjectiveRegenOk

`func (o *NpcUnit) GetObjectiveRegenOk() (*SubclassObjectiveRegen, bool)`

GetObjectiveRegenOk returns a tuple with the ObjectiveRegen field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectiveRegen

`func (o *NpcUnit) SetObjectiveRegen(v SubclassObjectiveRegen)`

SetObjectiveRegen sets ObjectiveRegen field to given value.

### HasObjectiveRegen

`func (o *NpcUnit) HasObjectiveRegen() bool`

HasObjectiveRegen returns a boolean if a field has been set.

### SetObjectiveRegenNil

`func (o *NpcUnit) SetObjectiveRegenNil(b bool)`

 SetObjectiveRegenNil sets the value for ObjectiveRegen to be an explicit nil

### UnsetObjectiveRegen
`func (o *NpcUnit) UnsetObjectiveRegen()`

UnsetObjectiveRegen ensures that no value is present for ObjectiveRegen, not even an explicit nil
### GetPhase2Health

`func (o *NpcUnit) GetPhase2Health() int64`

GetPhase2Health returns the Phase2Health field if non-nil, zero value otherwise.

### GetPhase2HealthOk

`func (o *NpcUnit) GetPhase2HealthOk() (*int64, bool)`

GetPhase2HealthOk returns a tuple with the Phase2Health field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPhase2Health

`func (o *NpcUnit) SetPhase2Health(v int64)`

SetPhase2Health sets Phase2Health field to given value.

### HasPhase2Health

`func (o *NpcUnit) HasPhase2Health() bool`

HasPhase2Health returns a boolean if a field has been set.

### SetPhase2HealthNil

`func (o *NpcUnit) SetPhase2HealthNil(b bool)`

 SetPhase2HealthNil sets the value for Phase2Health to be an explicit nil

### UnsetPhase2Health
`func (o *NpcUnit) UnsetPhase2Health()`

UnsetPhase2Health ensures that no value is present for Phase2Health, not even an explicit nil
### GetPlayerDamageResistPct

`func (o *NpcUnit) GetPlayerDamageResistPct() float64`

GetPlayerDamageResistPct returns the PlayerDamageResistPct field if non-nil, zero value otherwise.

### GetPlayerDamageResistPctOk

`func (o *NpcUnit) GetPlayerDamageResistPctOk() (*float64, bool)`

GetPlayerDamageResistPctOk returns a tuple with the PlayerDamageResistPct field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerDamageResistPct

`func (o *NpcUnit) SetPlayerDamageResistPct(v float64)`

SetPlayerDamageResistPct sets PlayerDamageResistPct field to given value.

### HasPlayerDamageResistPct

`func (o *NpcUnit) HasPlayerDamageResistPct() bool`

HasPlayerDamageResistPct returns a boolean if a field has been set.

### SetPlayerDamageResistPctNil

`func (o *NpcUnit) SetPlayerDamageResistPctNil(b bool)`

 SetPlayerDamageResistPctNil sets the value for PlayerDamageResistPct to be an explicit nil

### UnsetPlayerDamageResistPct
`func (o *NpcUnit) UnsetPlayerDamageResistPct()`

UnsetPlayerDamageResistPct ensures that no value is present for PlayerDamageResistPct, not even an explicit nil
### GetPlayerDps

`func (o *NpcUnit) GetPlayerDps() float64`

GetPlayerDps returns the PlayerDps field if non-nil, zero value otherwise.

### GetPlayerDpsOk

`func (o *NpcUnit) GetPlayerDpsOk() (*float64, bool)`

GetPlayerDpsOk returns a tuple with the PlayerDps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerDps

`func (o *NpcUnit) SetPlayerDps(v float64)`

SetPlayerDps sets PlayerDps field to given value.

### HasPlayerDps

`func (o *NpcUnit) HasPlayerDps() bool`

HasPlayerDps returns a boolean if a field has been set.

### SetPlayerDpsNil

`func (o *NpcUnit) SetPlayerDpsNil(b bool)`

 SetPlayerDpsNil sets the value for PlayerDps to be an explicit nil

### UnsetPlayerDps
`func (o *NpcUnit) UnsetPlayerDps()`

UnsetPlayerDps ensures that no value is present for PlayerDps, not even an explicit nil
### GetRangedArmorModifier

`func (o *NpcUnit) GetRangedArmorModifier() SubclassRangedArmorModifier`

GetRangedArmorModifier returns the RangedArmorModifier field if non-nil, zero value otherwise.

### GetRangedArmorModifierOk

`func (o *NpcUnit) GetRangedArmorModifierOk() (*SubclassRangedArmorModifier, bool)`

GetRangedArmorModifierOk returns a tuple with the RangedArmorModifier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRangedArmorModifier

`func (o *NpcUnit) SetRangedArmorModifier(v SubclassRangedArmorModifier)`

SetRangedArmorModifier sets RangedArmorModifier field to given value.

### HasRangedArmorModifier

`func (o *NpcUnit) HasRangedArmorModifier() bool`

HasRangedArmorModifier returns a boolean if a field has been set.

### SetRangedArmorModifierNil

`func (o *NpcUnit) SetRangedArmorModifierNil(b bool)`

 SetRangedArmorModifierNil sets the value for RangedArmorModifier to be an explicit nil

### UnsetRangedArmorModifier
`func (o *NpcUnit) UnsetRangedArmorModifier()`

UnsetRangedArmorModifier ensures that no value is present for RangedArmorModifier, not even an explicit nil
### GetRunSpeed

`func (o *NpcUnit) GetRunSpeed() float64`

GetRunSpeed returns the RunSpeed field if non-nil, zero value otherwise.

### GetRunSpeedOk

`func (o *NpcUnit) GetRunSpeedOk() (*float64, bool)`

GetRunSpeedOk returns a tuple with the RunSpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRunSpeed

`func (o *NpcUnit) SetRunSpeed(v float64)`

SetRunSpeed sets RunSpeed field to given value.

### HasRunSpeed

`func (o *NpcUnit) HasRunSpeed() bool`

HasRunSpeed returns a boolean if a field has been set.

### SetRunSpeedNil

`func (o *NpcUnit) SetRunSpeedNil(b bool)`

 SetRunSpeedNil sets the value for RunSpeed to be an explicit nil

### UnsetRunSpeed
`func (o *NpcUnit) UnsetRunSpeed()`

UnsetRunSpeed ensures that no value is present for RunSpeed, not even an explicit nil
### GetSightRangeNpcs

`func (o *NpcUnit) GetSightRangeNpcs() float64`

GetSightRangeNpcs returns the SightRangeNpcs field if non-nil, zero value otherwise.

### GetSightRangeNpcsOk

`func (o *NpcUnit) GetSightRangeNpcsOk() (*float64, bool)`

GetSightRangeNpcsOk returns a tuple with the SightRangeNpcs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSightRangeNpcs

`func (o *NpcUnit) SetSightRangeNpcs(v float64)`

SetSightRangeNpcs sets SightRangeNpcs field to given value.

### HasSightRangeNpcs

`func (o *NpcUnit) HasSightRangeNpcs() bool`

HasSightRangeNpcs returns a boolean if a field has been set.

### SetSightRangeNpcsNil

`func (o *NpcUnit) SetSightRangeNpcsNil(b bool)`

 SetSightRangeNpcsNil sets the value for SightRangeNpcs to be an explicit nil

### UnsetSightRangeNpcs
`func (o *NpcUnit) UnsetSightRangeNpcs()`

UnsetSightRangeNpcs ensures that no value is present for SightRangeNpcs, not even an explicit nil
### GetSightRangePlayers

`func (o *NpcUnit) GetSightRangePlayers() float64`

GetSightRangePlayers returns the SightRangePlayers field if non-nil, zero value otherwise.

### GetSightRangePlayersOk

`func (o *NpcUnit) GetSightRangePlayersOk() (*float64, bool)`

GetSightRangePlayersOk returns a tuple with the SightRangePlayers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSightRangePlayers

`func (o *NpcUnit) SetSightRangePlayers(v float64)`

SetSightRangePlayers sets SightRangePlayers field to given value.

### HasSightRangePlayers

`func (o *NpcUnit) HasSightRangePlayers() bool`

HasSightRangePlayers returns a boolean if a field has been set.

### SetSightRangePlayersNil

`func (o *NpcUnit) SetSightRangePlayersNil(b bool)`

 SetSightRangePlayersNil sets the value for SightRangePlayers to be an explicit nil

### UnsetSightRangePlayers
`func (o *NpcUnit) UnsetSightRangePlayers()`

UnsetSightRangePlayers ensures that no value is present for SightRangePlayers, not even an explicit nil
### GetSpawnBreakablesOnDeath

`func (o *NpcUnit) GetSpawnBreakablesOnDeath() bool`

GetSpawnBreakablesOnDeath returns the SpawnBreakablesOnDeath field if non-nil, zero value otherwise.

### GetSpawnBreakablesOnDeathOk

`func (o *NpcUnit) GetSpawnBreakablesOnDeathOk() (*bool, bool)`

GetSpawnBreakablesOnDeathOk returns a tuple with the SpawnBreakablesOnDeath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpawnBreakablesOnDeath

`func (o *NpcUnit) SetSpawnBreakablesOnDeath(v bool)`

SetSpawnBreakablesOnDeath sets SpawnBreakablesOnDeath field to given value.

### HasSpawnBreakablesOnDeath

`func (o *NpcUnit) HasSpawnBreakablesOnDeath() bool`

HasSpawnBreakablesOnDeath returns a boolean if a field has been set.

### SetSpawnBreakablesOnDeathNil

`func (o *NpcUnit) SetSpawnBreakablesOnDeathNil(b bool)`

 SetSpawnBreakablesOnDeathNil sets the value for SpawnBreakablesOnDeath to be an explicit nil

### UnsetSpawnBreakablesOnDeath
`func (o *NpcUnit) UnsetSpawnBreakablesOnDeath()`

UnsetSpawnBreakablesOnDeath ensures that no value is present for SpawnBreakablesOnDeath, not even an explicit nil
### GetStompDamage

`func (o *NpcUnit) GetStompDamage() float64`

GetStompDamage returns the StompDamage field if non-nil, zero value otherwise.

### GetStompDamageOk

`func (o *NpcUnit) GetStompDamageOk() (*float64, bool)`

GetStompDamageOk returns a tuple with the StompDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStompDamage

`func (o *NpcUnit) SetStompDamage(v float64)`

SetStompDamage sets StompDamage field to given value.

### HasStompDamage

`func (o *NpcUnit) HasStompDamage() bool`

HasStompDamage returns a boolean if a field has been set.

### SetStompDamageNil

`func (o *NpcUnit) SetStompDamageNil(b bool)`

 SetStompDamageNil sets the value for StompDamage to be an explicit nil

### UnsetStompDamage
`func (o *NpcUnit) UnsetStompDamage()`

UnsetStompDamage ensures that no value is present for StompDamage, not even an explicit nil
### GetStompDamageMaxHealthPercent

`func (o *NpcUnit) GetStompDamageMaxHealthPercent() float64`

GetStompDamageMaxHealthPercent returns the StompDamageMaxHealthPercent field if non-nil, zero value otherwise.

### GetStompDamageMaxHealthPercentOk

`func (o *NpcUnit) GetStompDamageMaxHealthPercentOk() (*float64, bool)`

GetStompDamageMaxHealthPercentOk returns a tuple with the StompDamageMaxHealthPercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStompDamageMaxHealthPercent

`func (o *NpcUnit) SetStompDamageMaxHealthPercent(v float64)`

SetStompDamageMaxHealthPercent sets StompDamageMaxHealthPercent field to given value.

### HasStompDamageMaxHealthPercent

`func (o *NpcUnit) HasStompDamageMaxHealthPercent() bool`

HasStompDamageMaxHealthPercent returns a boolean if a field has been set.

### SetStompDamageMaxHealthPercentNil

`func (o *NpcUnit) SetStompDamageMaxHealthPercentNil(b bool)`

 SetStompDamageMaxHealthPercentNil sets the value for StompDamageMaxHealthPercent to be an explicit nil

### UnsetStompDamageMaxHealthPercent
`func (o *NpcUnit) UnsetStompDamageMaxHealthPercent()`

UnsetStompDamageMaxHealthPercent ensures that no value is present for StompDamageMaxHealthPercent, not even an explicit nil
### GetStompImpactRadius

`func (o *NpcUnit) GetStompImpactRadius() float64`

GetStompImpactRadius returns the StompImpactRadius field if non-nil, zero value otherwise.

### GetStompImpactRadiusOk

`func (o *NpcUnit) GetStompImpactRadiusOk() (*float64, bool)`

GetStompImpactRadiusOk returns a tuple with the StompImpactRadius field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStompImpactRadius

`func (o *NpcUnit) SetStompImpactRadius(v float64)`

SetStompImpactRadius sets StompImpactRadius field to given value.

### HasStompImpactRadius

`func (o *NpcUnit) HasStompImpactRadius() bool`

HasStompImpactRadius returns a boolean if a field has been set.

### SetStompImpactRadiusNil

`func (o *NpcUnit) SetStompImpactRadiusNil(b bool)`

 SetStompImpactRadiusNil sets the value for StompImpactRadius to be an explicit nil

### UnsetStompImpactRadius
`func (o *NpcUnit) UnsetStompImpactRadius()`

UnsetStompImpactRadius ensures that no value is present for StompImpactRadius, not even an explicit nil
### GetStunDuration

`func (o *NpcUnit) GetStunDuration() float64`

GetStunDuration returns the StunDuration field if non-nil, zero value otherwise.

### GetStunDurationOk

`func (o *NpcUnit) GetStunDurationOk() (*float64, bool)`

GetStunDurationOk returns a tuple with the StunDuration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStunDuration

`func (o *NpcUnit) SetStunDuration(v float64)`

SetStunDuration sets StunDuration field to given value.

### HasStunDuration

`func (o *NpcUnit) HasStunDuration() bool`

HasStunDuration returns a boolean if a field has been set.

### SetStunDurationNil

`func (o *NpcUnit) SetStunDurationNil(b bool)`

 SetStunDurationNil sets the value for StunDuration to be an explicit nil

### UnsetStunDuration
`func (o *NpcUnit) UnsetStunDuration()`

UnsetStunDuration ensures that no value is present for StunDuration, not even an explicit nil
### GetT1BossDamageResistPct

`func (o *NpcUnit) GetT1BossDamageResistPct() float64`

GetT1BossDamageResistPct returns the T1BossDamageResistPct field if non-nil, zero value otherwise.

### GetT1BossDamageResistPctOk

`func (o *NpcUnit) GetT1BossDamageResistPctOk() (*float64, bool)`

GetT1BossDamageResistPctOk returns a tuple with the T1BossDamageResistPct field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT1BossDamageResistPct

`func (o *NpcUnit) SetT1BossDamageResistPct(v float64)`

SetT1BossDamageResistPct sets T1BossDamageResistPct field to given value.

### HasT1BossDamageResistPct

`func (o *NpcUnit) HasT1BossDamageResistPct() bool`

HasT1BossDamageResistPct returns a boolean if a field has been set.

### SetT1BossDamageResistPctNil

`func (o *NpcUnit) SetT1BossDamageResistPctNil(b bool)`

 SetT1BossDamageResistPctNil sets the value for T1BossDamageResistPct to be an explicit nil

### UnsetT1BossDamageResistPct
`func (o *NpcUnit) UnsetT1BossDamageResistPct()`

UnsetT1BossDamageResistPct ensures that no value is present for T1BossDamageResistPct, not even an explicit nil
### GetT1BossDps

`func (o *NpcUnit) GetT1BossDps() float64`

GetT1BossDps returns the T1BossDps field if non-nil, zero value otherwise.

### GetT1BossDpsOk

`func (o *NpcUnit) GetT1BossDpsOk() (*float64, bool)`

GetT1BossDpsOk returns a tuple with the T1BossDps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT1BossDps

`func (o *NpcUnit) SetT1BossDps(v float64)`

SetT1BossDps sets T1BossDps field to given value.

### HasT1BossDps

`func (o *NpcUnit) HasT1BossDps() bool`

HasT1BossDps returns a boolean if a field has been set.

### SetT1BossDpsNil

`func (o *NpcUnit) SetT1BossDpsNil(b bool)`

 SetT1BossDpsNil sets the value for T1BossDps to be an explicit nil

### UnsetT1BossDps
`func (o *NpcUnit) UnsetT1BossDps()`

UnsetT1BossDps ensures that no value is present for T1BossDps, not even an explicit nil
### GetT1BossDpsbaseResist

`func (o *NpcUnit) GetT1BossDpsbaseResist() float64`

GetT1BossDpsbaseResist returns the T1BossDpsbaseResist field if non-nil, zero value otherwise.

### GetT1BossDpsbaseResistOk

`func (o *NpcUnit) GetT1BossDpsbaseResistOk() (*float64, bool)`

GetT1BossDpsbaseResistOk returns a tuple with the T1BossDpsbaseResist field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT1BossDpsbaseResist

`func (o *NpcUnit) SetT1BossDpsbaseResist(v float64)`

SetT1BossDpsbaseResist sets T1BossDpsbaseResist field to given value.

### HasT1BossDpsbaseResist

`func (o *NpcUnit) HasT1BossDpsbaseResist() bool`

HasT1BossDpsbaseResist returns a boolean if a field has been set.

### SetT1BossDpsbaseResistNil

`func (o *NpcUnit) SetT1BossDpsbaseResistNil(b bool)`

 SetT1BossDpsbaseResistNil sets the value for T1BossDpsbaseResist to be an explicit nil

### UnsetT1BossDpsbaseResist
`func (o *NpcUnit) UnsetT1BossDpsbaseResist()`

UnsetT1BossDpsbaseResist ensures that no value is present for T1BossDpsbaseResist, not even an explicit nil
### GetT1BossDpsmaxResist

`func (o *NpcUnit) GetT1BossDpsmaxResist() float64`

GetT1BossDpsmaxResist returns the T1BossDpsmaxResist field if non-nil, zero value otherwise.

### GetT1BossDpsmaxResistOk

`func (o *NpcUnit) GetT1BossDpsmaxResistOk() (*float64, bool)`

GetT1BossDpsmaxResistOk returns a tuple with the T1BossDpsmaxResist field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT1BossDpsmaxResist

`func (o *NpcUnit) SetT1BossDpsmaxResist(v float64)`

SetT1BossDpsmaxResist sets T1BossDpsmaxResist field to given value.

### HasT1BossDpsmaxResist

`func (o *NpcUnit) HasT1BossDpsmaxResist() bool`

HasT1BossDpsmaxResist returns a boolean if a field has been set.

### SetT1BossDpsmaxResistNil

`func (o *NpcUnit) SetT1BossDpsmaxResistNil(b bool)`

 SetT1BossDpsmaxResistNil sets the value for T1BossDpsmaxResist to be an explicit nil

### UnsetT1BossDpsmaxResist
`func (o *NpcUnit) UnsetT1BossDpsmaxResist()`

UnsetT1BossDpsmaxResist ensures that no value is present for T1BossDpsmaxResist, not even an explicit nil
### GetT1BossDpsmaxResistTimeInSeconds

`func (o *NpcUnit) GetT1BossDpsmaxResistTimeInSeconds() float64`

GetT1BossDpsmaxResistTimeInSeconds returns the T1BossDpsmaxResistTimeInSeconds field if non-nil, zero value otherwise.

### GetT1BossDpsmaxResistTimeInSecondsOk

`func (o *NpcUnit) GetT1BossDpsmaxResistTimeInSecondsOk() (*float64, bool)`

GetT1BossDpsmaxResistTimeInSecondsOk returns a tuple with the T1BossDpsmaxResistTimeInSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT1BossDpsmaxResistTimeInSeconds

`func (o *NpcUnit) SetT1BossDpsmaxResistTimeInSeconds(v float64)`

SetT1BossDpsmaxResistTimeInSeconds sets T1BossDpsmaxResistTimeInSeconds field to given value.

### HasT1BossDpsmaxResistTimeInSeconds

`func (o *NpcUnit) HasT1BossDpsmaxResistTimeInSeconds() bool`

HasT1BossDpsmaxResistTimeInSeconds returns a boolean if a field has been set.

### SetT1BossDpsmaxResistTimeInSecondsNil

`func (o *NpcUnit) SetT1BossDpsmaxResistTimeInSecondsNil(b bool)`

 SetT1BossDpsmaxResistTimeInSecondsNil sets the value for T1BossDpsmaxResistTimeInSeconds to be an explicit nil

### UnsetT1BossDpsmaxResistTimeInSeconds
`func (o *NpcUnit) UnsetT1BossDpsmaxResistTimeInSeconds()`

UnsetT1BossDpsmaxResistTimeInSeconds ensures that no value is present for T1BossDpsmaxResistTimeInSeconds, not even an explicit nil
### GetT2BossDamageResistPct

`func (o *NpcUnit) GetT2BossDamageResistPct() float64`

GetT2BossDamageResistPct returns the T2BossDamageResistPct field if non-nil, zero value otherwise.

### GetT2BossDamageResistPctOk

`func (o *NpcUnit) GetT2BossDamageResistPctOk() (*float64, bool)`

GetT2BossDamageResistPctOk returns a tuple with the T2BossDamageResistPct field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT2BossDamageResistPct

`func (o *NpcUnit) SetT2BossDamageResistPct(v float64)`

SetT2BossDamageResistPct sets T2BossDamageResistPct field to given value.

### HasT2BossDamageResistPct

`func (o *NpcUnit) HasT2BossDamageResistPct() bool`

HasT2BossDamageResistPct returns a boolean if a field has been set.

### SetT2BossDamageResistPctNil

`func (o *NpcUnit) SetT2BossDamageResistPctNil(b bool)`

 SetT2BossDamageResistPctNil sets the value for T2BossDamageResistPct to be an explicit nil

### UnsetT2BossDamageResistPct
`func (o *NpcUnit) UnsetT2BossDamageResistPct()`

UnsetT2BossDamageResistPct ensures that no value is present for T2BossDamageResistPct, not even an explicit nil
### GetT2BossDps

`func (o *NpcUnit) GetT2BossDps() float64`

GetT2BossDps returns the T2BossDps field if non-nil, zero value otherwise.

### GetT2BossDpsOk

`func (o *NpcUnit) GetT2BossDpsOk() (*float64, bool)`

GetT2BossDpsOk returns a tuple with the T2BossDps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT2BossDps

`func (o *NpcUnit) SetT2BossDps(v float64)`

SetT2BossDps sets T2BossDps field to given value.

### HasT2BossDps

`func (o *NpcUnit) HasT2BossDps() bool`

HasT2BossDps returns a boolean if a field has been set.

### SetT2BossDpsNil

`func (o *NpcUnit) SetT2BossDpsNil(b bool)`

 SetT2BossDpsNil sets the value for T2BossDps to be an explicit nil

### UnsetT2BossDps
`func (o *NpcUnit) UnsetT2BossDps()`

UnsetT2BossDps ensures that no value is present for T2BossDps, not even an explicit nil
### GetT2BossDpsbaseResist

`func (o *NpcUnit) GetT2BossDpsbaseResist() float64`

GetT2BossDpsbaseResist returns the T2BossDpsbaseResist field if non-nil, zero value otherwise.

### GetT2BossDpsbaseResistOk

`func (o *NpcUnit) GetT2BossDpsbaseResistOk() (*float64, bool)`

GetT2BossDpsbaseResistOk returns a tuple with the T2BossDpsbaseResist field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT2BossDpsbaseResist

`func (o *NpcUnit) SetT2BossDpsbaseResist(v float64)`

SetT2BossDpsbaseResist sets T2BossDpsbaseResist field to given value.

### HasT2BossDpsbaseResist

`func (o *NpcUnit) HasT2BossDpsbaseResist() bool`

HasT2BossDpsbaseResist returns a boolean if a field has been set.

### SetT2BossDpsbaseResistNil

`func (o *NpcUnit) SetT2BossDpsbaseResistNil(b bool)`

 SetT2BossDpsbaseResistNil sets the value for T2BossDpsbaseResist to be an explicit nil

### UnsetT2BossDpsbaseResist
`func (o *NpcUnit) UnsetT2BossDpsbaseResist()`

UnsetT2BossDpsbaseResist ensures that no value is present for T2BossDpsbaseResist, not even an explicit nil
### GetT2BossDpsmaxResist

`func (o *NpcUnit) GetT2BossDpsmaxResist() float64`

GetT2BossDpsmaxResist returns the T2BossDpsmaxResist field if non-nil, zero value otherwise.

### GetT2BossDpsmaxResistOk

`func (o *NpcUnit) GetT2BossDpsmaxResistOk() (*float64, bool)`

GetT2BossDpsmaxResistOk returns a tuple with the T2BossDpsmaxResist field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT2BossDpsmaxResist

`func (o *NpcUnit) SetT2BossDpsmaxResist(v float64)`

SetT2BossDpsmaxResist sets T2BossDpsmaxResist field to given value.

### HasT2BossDpsmaxResist

`func (o *NpcUnit) HasT2BossDpsmaxResist() bool`

HasT2BossDpsmaxResist returns a boolean if a field has been set.

### SetT2BossDpsmaxResistNil

`func (o *NpcUnit) SetT2BossDpsmaxResistNil(b bool)`

 SetT2BossDpsmaxResistNil sets the value for T2BossDpsmaxResist to be an explicit nil

### UnsetT2BossDpsmaxResist
`func (o *NpcUnit) UnsetT2BossDpsmaxResist()`

UnsetT2BossDpsmaxResist ensures that no value is present for T2BossDpsmaxResist, not even an explicit nil
### GetT2BossDpsmaxResistTimeInSeconds

`func (o *NpcUnit) GetT2BossDpsmaxResistTimeInSeconds() float64`

GetT2BossDpsmaxResistTimeInSeconds returns the T2BossDpsmaxResistTimeInSeconds field if non-nil, zero value otherwise.

### GetT2BossDpsmaxResistTimeInSecondsOk

`func (o *NpcUnit) GetT2BossDpsmaxResistTimeInSecondsOk() (*float64, bool)`

GetT2BossDpsmaxResistTimeInSecondsOk returns a tuple with the T2BossDpsmaxResistTimeInSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT2BossDpsmaxResistTimeInSeconds

`func (o *NpcUnit) SetT2BossDpsmaxResistTimeInSeconds(v float64)`

SetT2BossDpsmaxResistTimeInSeconds sets T2BossDpsmaxResistTimeInSeconds field to given value.

### HasT2BossDpsmaxResistTimeInSeconds

`func (o *NpcUnit) HasT2BossDpsmaxResistTimeInSeconds() bool`

HasT2BossDpsmaxResistTimeInSeconds returns a boolean if a field has been set.

### SetT2BossDpsmaxResistTimeInSecondsNil

`func (o *NpcUnit) SetT2BossDpsmaxResistTimeInSecondsNil(b bool)`

 SetT2BossDpsmaxResistTimeInSecondsNil sets the value for T2BossDpsmaxResistTimeInSeconds to be an explicit nil

### UnsetT2BossDpsmaxResistTimeInSeconds
`func (o *NpcUnit) UnsetT2BossDpsmaxResistTimeInSeconds()`

UnsetT2BossDpsmaxResistTimeInSeconds ensures that no value is present for T2BossDpsmaxResistTimeInSeconds, not even an explicit nil
### GetT3BossDamageResistPct

`func (o *NpcUnit) GetT3BossDamageResistPct() float64`

GetT3BossDamageResistPct returns the T3BossDamageResistPct field if non-nil, zero value otherwise.

### GetT3BossDamageResistPctOk

`func (o *NpcUnit) GetT3BossDamageResistPctOk() (*float64, bool)`

GetT3BossDamageResistPctOk returns a tuple with the T3BossDamageResistPct field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT3BossDamageResistPct

`func (o *NpcUnit) SetT3BossDamageResistPct(v float64)`

SetT3BossDamageResistPct sets T3BossDamageResistPct field to given value.

### HasT3BossDamageResistPct

`func (o *NpcUnit) HasT3BossDamageResistPct() bool`

HasT3BossDamageResistPct returns a boolean if a field has been set.

### SetT3BossDamageResistPctNil

`func (o *NpcUnit) SetT3BossDamageResistPctNil(b bool)`

 SetT3BossDamageResistPctNil sets the value for T3BossDamageResistPct to be an explicit nil

### UnsetT3BossDamageResistPct
`func (o *NpcUnit) UnsetT3BossDamageResistPct()`

UnsetT3BossDamageResistPct ensures that no value is present for T3BossDamageResistPct, not even an explicit nil
### GetT3BossDps

`func (o *NpcUnit) GetT3BossDps() float64`

GetT3BossDps returns the T3BossDps field if non-nil, zero value otherwise.

### GetT3BossDpsOk

`func (o *NpcUnit) GetT3BossDpsOk() (*float64, bool)`

GetT3BossDpsOk returns a tuple with the T3BossDps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT3BossDps

`func (o *NpcUnit) SetT3BossDps(v float64)`

SetT3BossDps sets T3BossDps field to given value.

### HasT3BossDps

`func (o *NpcUnit) HasT3BossDps() bool`

HasT3BossDps returns a boolean if a field has been set.

### SetT3BossDpsNil

`func (o *NpcUnit) SetT3BossDpsNil(b bool)`

 SetT3BossDpsNil sets the value for T3BossDps to be an explicit nil

### UnsetT3BossDps
`func (o *NpcUnit) UnsetT3BossDps()`

UnsetT3BossDps ensures that no value is present for T3BossDps, not even an explicit nil
### GetTrooperDamageResistPct

`func (o *NpcUnit) GetTrooperDamageResistPct() float64`

GetTrooperDamageResistPct returns the TrooperDamageResistPct field if non-nil, zero value otherwise.

### GetTrooperDamageResistPctOk

`func (o *NpcUnit) GetTrooperDamageResistPctOk() (*float64, bool)`

GetTrooperDamageResistPctOk returns a tuple with the TrooperDamageResistPct field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrooperDamageResistPct

`func (o *NpcUnit) SetTrooperDamageResistPct(v float64)`

SetTrooperDamageResistPct sets TrooperDamageResistPct field to given value.

### HasTrooperDamageResistPct

`func (o *NpcUnit) HasTrooperDamageResistPct() bool`

HasTrooperDamageResistPct returns a boolean if a field has been set.

### SetTrooperDamageResistPctNil

`func (o *NpcUnit) SetTrooperDamageResistPctNil(b bool)`

 SetTrooperDamageResistPctNil sets the value for TrooperDamageResistPct to be an explicit nil

### UnsetTrooperDamageResistPct
`func (o *NpcUnit) UnsetTrooperDamageResistPct()`

UnsetTrooperDamageResistPct ensures that no value is present for TrooperDamageResistPct, not even an explicit nil
### GetTrooperDps

`func (o *NpcUnit) GetTrooperDps() float64`

GetTrooperDps returns the TrooperDps field if non-nil, zero value otherwise.

### GetTrooperDpsOk

`func (o *NpcUnit) GetTrooperDpsOk() (*float64, bool)`

GetTrooperDpsOk returns a tuple with the TrooperDps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrooperDps

`func (o *NpcUnit) SetTrooperDps(v float64)`

SetTrooperDps sets TrooperDps field to given value.

### HasTrooperDps

`func (o *NpcUnit) HasTrooperDps() bool`

HasTrooperDps returns a boolean if a field has been set.

### SetTrooperDpsNil

`func (o *NpcUnit) SetTrooperDpsNil(b bool)`

 SetTrooperDpsNil sets the value for TrooperDps to be an explicit nil

### UnsetTrooperDps
`func (o *NpcUnit) UnsetTrooperDps()`

UnsetTrooperDps ensures that no value is present for TrooperDps, not even an explicit nil
### GetWalkSpeed

`func (o *NpcUnit) GetWalkSpeed() float64`

GetWalkSpeed returns the WalkSpeed field if non-nil, zero value otherwise.

### GetWalkSpeedOk

`func (o *NpcUnit) GetWalkSpeedOk() (*float64, bool)`

GetWalkSpeedOk returns a tuple with the WalkSpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWalkSpeed

`func (o *NpcUnit) SetWalkSpeed(v float64)`

SetWalkSpeed sets WalkSpeed field to given value.

### HasWalkSpeed

`func (o *NpcUnit) HasWalkSpeed() bool`

HasWalkSpeed returns a boolean if a field has been set.

### SetWalkSpeedNil

`func (o *NpcUnit) SetWalkSpeedNil(b bool)`

 SetWalkSpeedNil sets the value for WalkSpeed to be an explicit nil

### UnsetWalkSpeed
`func (o *NpcUnit) UnsetWalkSpeed()`

UnsetWalkSpeed ensures that no value is present for WalkSpeed, not even an explicit nil
### GetWeaponInfo

`func (o *NpcUnit) GetWeaponInfo() WeaponInfo`

GetWeaponInfo returns the WeaponInfo field if non-nil, zero value otherwise.

### GetWeaponInfoOk

`func (o *NpcUnit) GetWeaponInfoOk() (*WeaponInfo, bool)`

GetWeaponInfoOk returns a tuple with the WeaponInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponInfo

`func (o *NpcUnit) SetWeaponInfo(v WeaponInfo)`

SetWeaponInfo sets WeaponInfo field to given value.

### HasWeaponInfo

`func (o *NpcUnit) HasWeaponInfo() bool`

HasWeaponInfo returns a boolean if a field has been set.

### SetWeaponInfoNil

`func (o *NpcUnit) SetWeaponInfoNil(b bool)`

 SetWeaponInfoNil sets the value for WeaponInfo to be an explicit nil

### UnsetWeaponInfo
`func (o *NpcUnit) UnsetWeaponInfo()`

UnsetWeaponInfo ensures that no value is present for WeaponInfo, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


