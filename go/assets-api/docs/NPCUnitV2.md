# NPCUnitV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClassName** | **string** |  | 
**WeaponInfo** | Pointer to [**NullableRawWeaponInfoV2**](RawWeaponInfoV2.md) |  | [optional] 
**MaxHealth** | Pointer to **NullableInt32** |  | [optional] 
**SightRangePlayers** | Pointer to **NullableFloat32** |  | [optional] 
**SightRangeNpcs** | Pointer to **NullableFloat32** |  | [optional] 
**GoldReward** | Pointer to **NullableFloat32** |  | [optional] 
**GoldRewardBonusPercentPerMinute** | Pointer to **NullableFloat32** |  | [optional] 
**MFlPlayerDamageResistPct** | Pointer to **NullableFloat32** |  | [optional] 
**TrooperDamageResistPct** | Pointer to **NullableFloat32** |  | [optional] 
**T1BossDamageResistPct** | Pointer to **NullableFloat32** |  | [optional] 
**T2BossDamageResistPct** | Pointer to **NullableFloat32** |  | [optional] 
**T3BossDamageResistPct** | Pointer to **NullableFloat32** |  | [optional] 
**BarrackGuardianDamageResistPct** | Pointer to **NullableFloat32** |  | [optional] 
**NearDeathDuration** | Pointer to **NullableFloat32** |  | [optional] 
**WalkSpeed** | Pointer to **NullableFloat32** |  | [optional] 
**RunSpeed** | Pointer to **NullableFloat32** |  | [optional] 
**Acceleration** | Pointer to **NullableFloat32** |  | [optional] 
**MeleeDamage** | Pointer to **NullableFloat32** |  | [optional] 
**MeleeAttemptRange** | Pointer to **NullableFloat32** |  | [optional] 
**MeleeHitRange** | Pointer to **NullableFloat32** |  | [optional] 
**MeleeDuration** | Pointer to **NullableFloat32** |  | [optional] 
**AttackT1BossMaxRange** | Pointer to **NullableFloat32** |  | [optional] 
**AttackT3BossMaxRange** | Pointer to **NullableFloat32** |  | [optional] 
**AttackT3BossPhase2MaxRange** | Pointer to **NullableFloat32** |  | [optional] 
**AttackTrooperMaxRange** | Pointer to **NullableFloat32** |  | [optional] 
**T1BossDps** | Pointer to **NullableFloat32** |  | [optional] 
**T1BossDpsbaseResist** | Pointer to **NullableFloat32** |  | [optional] 
**T1BossDpsmaxResist** | Pointer to **NullableFloat32** |  | [optional] 
**T1BossDpsmaxResistTimeInSeconds** | Pointer to **NullableFloat32** |  | [optional] 
**T2BossDps** | Pointer to **NullableFloat32** |  | [optional] 
**T2BossDpsbaseResist** | Pointer to **NullableFloat32** |  | [optional] 
**T2BossDpsmaxResist** | Pointer to **NullableFloat32** |  | [optional] 
**T2BossDpsmaxResistTimeInSeconds** | Pointer to **NullableFloat32** |  | [optional] 
**T3BossDps** | Pointer to **NullableFloat32** |  | [optional] 
**GeneratorBossDps** | Pointer to **NullableFloat32** |  | [optional] 
**BarrackBossDps** | Pointer to **NullableFloat32** |  | [optional] 
**PlayerDps** | Pointer to **NullableFloat32** |  | [optional] 
**TrooperDps** | Pointer to **NullableFloat32** |  | [optional] 
**HealthBarColorFriend** | Pointer to [**NullableHealthBarColorFriend**](HealthBarColorFriend.md) |  | [optional] 
**HealthBarColorEnemy** | Pointer to [**NullableHealthBarColorEnemy**](HealthBarColorEnemy.md) |  | [optional] 
**HealthBarColorTeam1** | Pointer to [**NullableHealthBarColorTeam1**](HealthBarColorTeam1.md) |  | [optional] 
**HealthBarColorTeam2** | Pointer to [**NullableHealthBarColorTeam2**](HealthBarColorTeam2.md) |  | [optional] 
**HealthBarColorTeamNeutral** | Pointer to [**NullableHealthBarColorTeamNeutral**](HealthBarColorTeamNeutral.md) |  | [optional] 
**GlowColorFriend** | Pointer to [**NullableGlowColorFriend**](GlowColorFriend.md) |  | [optional] 
**GlowColorEnemy** | Pointer to [**NullableGlowColorEnemy**](GlowColorEnemy.md) |  | [optional] 
**GlowColorTeam1** | Pointer to [**NullableGlowColorTeam1**](GlowColorTeam1.md) |  | [optional] 
**GlowColorTeam2** | Pointer to [**NullableGlowColorTeam2**](GlowColorTeam2.md) |  | [optional] 
**GlowColorTeamNeutral** | Pointer to [**NullableGlowColorTeamNeutral**](GlowColorTeamNeutral.md) |  | [optional] 
**Id** | **int64** |  | [readonly] 

## Methods

### NewNPCUnitV2

`func NewNPCUnitV2(className string, id int64, ) *NPCUnitV2`

NewNPCUnitV2 instantiates a new NPCUnitV2 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNPCUnitV2WithDefaults

`func NewNPCUnitV2WithDefaults() *NPCUnitV2`

NewNPCUnitV2WithDefaults instantiates a new NPCUnitV2 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClassName

`func (o *NPCUnitV2) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *NPCUnitV2) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *NPCUnitV2) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetWeaponInfo

`func (o *NPCUnitV2) GetWeaponInfo() RawWeaponInfoV2`

GetWeaponInfo returns the WeaponInfo field if non-nil, zero value otherwise.

### GetWeaponInfoOk

`func (o *NPCUnitV2) GetWeaponInfoOk() (*RawWeaponInfoV2, bool)`

GetWeaponInfoOk returns a tuple with the WeaponInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponInfo

`func (o *NPCUnitV2) SetWeaponInfo(v RawWeaponInfoV2)`

SetWeaponInfo sets WeaponInfo field to given value.

### HasWeaponInfo

`func (o *NPCUnitV2) HasWeaponInfo() bool`

HasWeaponInfo returns a boolean if a field has been set.

### SetWeaponInfoNil

`func (o *NPCUnitV2) SetWeaponInfoNil(b bool)`

 SetWeaponInfoNil sets the value for WeaponInfo to be an explicit nil

### UnsetWeaponInfo
`func (o *NPCUnitV2) UnsetWeaponInfo()`

UnsetWeaponInfo ensures that no value is present for WeaponInfo, not even an explicit nil
### GetMaxHealth

`func (o *NPCUnitV2) GetMaxHealth() int32`

GetMaxHealth returns the MaxHealth field if non-nil, zero value otherwise.

### GetMaxHealthOk

`func (o *NPCUnitV2) GetMaxHealthOk() (*int32, bool)`

GetMaxHealthOk returns a tuple with the MaxHealth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxHealth

`func (o *NPCUnitV2) SetMaxHealth(v int32)`

SetMaxHealth sets MaxHealth field to given value.

### HasMaxHealth

`func (o *NPCUnitV2) HasMaxHealth() bool`

HasMaxHealth returns a boolean if a field has been set.

### SetMaxHealthNil

`func (o *NPCUnitV2) SetMaxHealthNil(b bool)`

 SetMaxHealthNil sets the value for MaxHealth to be an explicit nil

### UnsetMaxHealth
`func (o *NPCUnitV2) UnsetMaxHealth()`

UnsetMaxHealth ensures that no value is present for MaxHealth, not even an explicit nil
### GetSightRangePlayers

`func (o *NPCUnitV2) GetSightRangePlayers() float32`

GetSightRangePlayers returns the SightRangePlayers field if non-nil, zero value otherwise.

### GetSightRangePlayersOk

`func (o *NPCUnitV2) GetSightRangePlayersOk() (*float32, bool)`

GetSightRangePlayersOk returns a tuple with the SightRangePlayers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSightRangePlayers

`func (o *NPCUnitV2) SetSightRangePlayers(v float32)`

SetSightRangePlayers sets SightRangePlayers field to given value.

### HasSightRangePlayers

`func (o *NPCUnitV2) HasSightRangePlayers() bool`

HasSightRangePlayers returns a boolean if a field has been set.

### SetSightRangePlayersNil

`func (o *NPCUnitV2) SetSightRangePlayersNil(b bool)`

 SetSightRangePlayersNil sets the value for SightRangePlayers to be an explicit nil

### UnsetSightRangePlayers
`func (o *NPCUnitV2) UnsetSightRangePlayers()`

UnsetSightRangePlayers ensures that no value is present for SightRangePlayers, not even an explicit nil
### GetSightRangeNpcs

`func (o *NPCUnitV2) GetSightRangeNpcs() float32`

GetSightRangeNpcs returns the SightRangeNpcs field if non-nil, zero value otherwise.

### GetSightRangeNpcsOk

`func (o *NPCUnitV2) GetSightRangeNpcsOk() (*float32, bool)`

GetSightRangeNpcsOk returns a tuple with the SightRangeNpcs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSightRangeNpcs

`func (o *NPCUnitV2) SetSightRangeNpcs(v float32)`

SetSightRangeNpcs sets SightRangeNpcs field to given value.

### HasSightRangeNpcs

`func (o *NPCUnitV2) HasSightRangeNpcs() bool`

HasSightRangeNpcs returns a boolean if a field has been set.

### SetSightRangeNpcsNil

`func (o *NPCUnitV2) SetSightRangeNpcsNil(b bool)`

 SetSightRangeNpcsNil sets the value for SightRangeNpcs to be an explicit nil

### UnsetSightRangeNpcs
`func (o *NPCUnitV2) UnsetSightRangeNpcs()`

UnsetSightRangeNpcs ensures that no value is present for SightRangeNpcs, not even an explicit nil
### GetGoldReward

`func (o *NPCUnitV2) GetGoldReward() float32`

GetGoldReward returns the GoldReward field if non-nil, zero value otherwise.

### GetGoldRewardOk

`func (o *NPCUnitV2) GetGoldRewardOk() (*float32, bool)`

GetGoldRewardOk returns a tuple with the GoldReward field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldReward

`func (o *NPCUnitV2) SetGoldReward(v float32)`

SetGoldReward sets GoldReward field to given value.

### HasGoldReward

`func (o *NPCUnitV2) HasGoldReward() bool`

HasGoldReward returns a boolean if a field has been set.

### SetGoldRewardNil

`func (o *NPCUnitV2) SetGoldRewardNil(b bool)`

 SetGoldRewardNil sets the value for GoldReward to be an explicit nil

### UnsetGoldReward
`func (o *NPCUnitV2) UnsetGoldReward()`

UnsetGoldReward ensures that no value is present for GoldReward, not even an explicit nil
### GetGoldRewardBonusPercentPerMinute

`func (o *NPCUnitV2) GetGoldRewardBonusPercentPerMinute() float32`

GetGoldRewardBonusPercentPerMinute returns the GoldRewardBonusPercentPerMinute field if non-nil, zero value otherwise.

### GetGoldRewardBonusPercentPerMinuteOk

`func (o *NPCUnitV2) GetGoldRewardBonusPercentPerMinuteOk() (*float32, bool)`

GetGoldRewardBonusPercentPerMinuteOk returns a tuple with the GoldRewardBonusPercentPerMinute field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldRewardBonusPercentPerMinute

`func (o *NPCUnitV2) SetGoldRewardBonusPercentPerMinute(v float32)`

SetGoldRewardBonusPercentPerMinute sets GoldRewardBonusPercentPerMinute field to given value.

### HasGoldRewardBonusPercentPerMinute

`func (o *NPCUnitV2) HasGoldRewardBonusPercentPerMinute() bool`

HasGoldRewardBonusPercentPerMinute returns a boolean if a field has been set.

### SetGoldRewardBonusPercentPerMinuteNil

`func (o *NPCUnitV2) SetGoldRewardBonusPercentPerMinuteNil(b bool)`

 SetGoldRewardBonusPercentPerMinuteNil sets the value for GoldRewardBonusPercentPerMinute to be an explicit nil

### UnsetGoldRewardBonusPercentPerMinute
`func (o *NPCUnitV2) UnsetGoldRewardBonusPercentPerMinute()`

UnsetGoldRewardBonusPercentPerMinute ensures that no value is present for GoldRewardBonusPercentPerMinute, not even an explicit nil
### GetMFlPlayerDamageResistPct

`func (o *NPCUnitV2) GetMFlPlayerDamageResistPct() float32`

GetMFlPlayerDamageResistPct returns the MFlPlayerDamageResistPct field if non-nil, zero value otherwise.

### GetMFlPlayerDamageResistPctOk

`func (o *NPCUnitV2) GetMFlPlayerDamageResistPctOk() (*float32, bool)`

GetMFlPlayerDamageResistPctOk returns a tuple with the MFlPlayerDamageResistPct field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlPlayerDamageResistPct

`func (o *NPCUnitV2) SetMFlPlayerDamageResistPct(v float32)`

SetMFlPlayerDamageResistPct sets MFlPlayerDamageResistPct field to given value.

### HasMFlPlayerDamageResistPct

`func (o *NPCUnitV2) HasMFlPlayerDamageResistPct() bool`

HasMFlPlayerDamageResistPct returns a boolean if a field has been set.

### SetMFlPlayerDamageResistPctNil

`func (o *NPCUnitV2) SetMFlPlayerDamageResistPctNil(b bool)`

 SetMFlPlayerDamageResistPctNil sets the value for MFlPlayerDamageResistPct to be an explicit nil

### UnsetMFlPlayerDamageResistPct
`func (o *NPCUnitV2) UnsetMFlPlayerDamageResistPct()`

UnsetMFlPlayerDamageResistPct ensures that no value is present for MFlPlayerDamageResistPct, not even an explicit nil
### GetTrooperDamageResistPct

`func (o *NPCUnitV2) GetTrooperDamageResistPct() float32`

GetTrooperDamageResistPct returns the TrooperDamageResistPct field if non-nil, zero value otherwise.

### GetTrooperDamageResistPctOk

`func (o *NPCUnitV2) GetTrooperDamageResistPctOk() (*float32, bool)`

GetTrooperDamageResistPctOk returns a tuple with the TrooperDamageResistPct field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrooperDamageResistPct

`func (o *NPCUnitV2) SetTrooperDamageResistPct(v float32)`

SetTrooperDamageResistPct sets TrooperDamageResistPct field to given value.

### HasTrooperDamageResistPct

`func (o *NPCUnitV2) HasTrooperDamageResistPct() bool`

HasTrooperDamageResistPct returns a boolean if a field has been set.

### SetTrooperDamageResistPctNil

`func (o *NPCUnitV2) SetTrooperDamageResistPctNil(b bool)`

 SetTrooperDamageResistPctNil sets the value for TrooperDamageResistPct to be an explicit nil

### UnsetTrooperDamageResistPct
`func (o *NPCUnitV2) UnsetTrooperDamageResistPct()`

UnsetTrooperDamageResistPct ensures that no value is present for TrooperDamageResistPct, not even an explicit nil
### GetT1BossDamageResistPct

`func (o *NPCUnitV2) GetT1BossDamageResistPct() float32`

GetT1BossDamageResistPct returns the T1BossDamageResistPct field if non-nil, zero value otherwise.

### GetT1BossDamageResistPctOk

`func (o *NPCUnitV2) GetT1BossDamageResistPctOk() (*float32, bool)`

GetT1BossDamageResistPctOk returns a tuple with the T1BossDamageResistPct field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT1BossDamageResistPct

`func (o *NPCUnitV2) SetT1BossDamageResistPct(v float32)`

SetT1BossDamageResistPct sets T1BossDamageResistPct field to given value.

### HasT1BossDamageResistPct

`func (o *NPCUnitV2) HasT1BossDamageResistPct() bool`

HasT1BossDamageResistPct returns a boolean if a field has been set.

### SetT1BossDamageResistPctNil

`func (o *NPCUnitV2) SetT1BossDamageResistPctNil(b bool)`

 SetT1BossDamageResistPctNil sets the value for T1BossDamageResistPct to be an explicit nil

### UnsetT1BossDamageResistPct
`func (o *NPCUnitV2) UnsetT1BossDamageResistPct()`

UnsetT1BossDamageResistPct ensures that no value is present for T1BossDamageResistPct, not even an explicit nil
### GetT2BossDamageResistPct

`func (o *NPCUnitV2) GetT2BossDamageResistPct() float32`

GetT2BossDamageResistPct returns the T2BossDamageResistPct field if non-nil, zero value otherwise.

### GetT2BossDamageResistPctOk

`func (o *NPCUnitV2) GetT2BossDamageResistPctOk() (*float32, bool)`

GetT2BossDamageResistPctOk returns a tuple with the T2BossDamageResistPct field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT2BossDamageResistPct

`func (o *NPCUnitV2) SetT2BossDamageResistPct(v float32)`

SetT2BossDamageResistPct sets T2BossDamageResistPct field to given value.

### HasT2BossDamageResistPct

`func (o *NPCUnitV2) HasT2BossDamageResistPct() bool`

HasT2BossDamageResistPct returns a boolean if a field has been set.

### SetT2BossDamageResistPctNil

`func (o *NPCUnitV2) SetT2BossDamageResistPctNil(b bool)`

 SetT2BossDamageResistPctNil sets the value for T2BossDamageResistPct to be an explicit nil

### UnsetT2BossDamageResistPct
`func (o *NPCUnitV2) UnsetT2BossDamageResistPct()`

UnsetT2BossDamageResistPct ensures that no value is present for T2BossDamageResistPct, not even an explicit nil
### GetT3BossDamageResistPct

`func (o *NPCUnitV2) GetT3BossDamageResistPct() float32`

GetT3BossDamageResistPct returns the T3BossDamageResistPct field if non-nil, zero value otherwise.

### GetT3BossDamageResistPctOk

`func (o *NPCUnitV2) GetT3BossDamageResistPctOk() (*float32, bool)`

GetT3BossDamageResistPctOk returns a tuple with the T3BossDamageResistPct field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT3BossDamageResistPct

`func (o *NPCUnitV2) SetT3BossDamageResistPct(v float32)`

SetT3BossDamageResistPct sets T3BossDamageResistPct field to given value.

### HasT3BossDamageResistPct

`func (o *NPCUnitV2) HasT3BossDamageResistPct() bool`

HasT3BossDamageResistPct returns a boolean if a field has been set.

### SetT3BossDamageResistPctNil

`func (o *NPCUnitV2) SetT3BossDamageResistPctNil(b bool)`

 SetT3BossDamageResistPctNil sets the value for T3BossDamageResistPct to be an explicit nil

### UnsetT3BossDamageResistPct
`func (o *NPCUnitV2) UnsetT3BossDamageResistPct()`

UnsetT3BossDamageResistPct ensures that no value is present for T3BossDamageResistPct, not even an explicit nil
### GetBarrackGuardianDamageResistPct

`func (o *NPCUnitV2) GetBarrackGuardianDamageResistPct() float32`

GetBarrackGuardianDamageResistPct returns the BarrackGuardianDamageResistPct field if non-nil, zero value otherwise.

### GetBarrackGuardianDamageResistPctOk

`func (o *NPCUnitV2) GetBarrackGuardianDamageResistPctOk() (*float32, bool)`

GetBarrackGuardianDamageResistPctOk returns a tuple with the BarrackGuardianDamageResistPct field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBarrackGuardianDamageResistPct

`func (o *NPCUnitV2) SetBarrackGuardianDamageResistPct(v float32)`

SetBarrackGuardianDamageResistPct sets BarrackGuardianDamageResistPct field to given value.

### HasBarrackGuardianDamageResistPct

`func (o *NPCUnitV2) HasBarrackGuardianDamageResistPct() bool`

HasBarrackGuardianDamageResistPct returns a boolean if a field has been set.

### SetBarrackGuardianDamageResistPctNil

`func (o *NPCUnitV2) SetBarrackGuardianDamageResistPctNil(b bool)`

 SetBarrackGuardianDamageResistPctNil sets the value for BarrackGuardianDamageResistPct to be an explicit nil

### UnsetBarrackGuardianDamageResistPct
`func (o *NPCUnitV2) UnsetBarrackGuardianDamageResistPct()`

UnsetBarrackGuardianDamageResistPct ensures that no value is present for BarrackGuardianDamageResistPct, not even an explicit nil
### GetNearDeathDuration

`func (o *NPCUnitV2) GetNearDeathDuration() float32`

GetNearDeathDuration returns the NearDeathDuration field if non-nil, zero value otherwise.

### GetNearDeathDurationOk

`func (o *NPCUnitV2) GetNearDeathDurationOk() (*float32, bool)`

GetNearDeathDurationOk returns a tuple with the NearDeathDuration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNearDeathDuration

`func (o *NPCUnitV2) SetNearDeathDuration(v float32)`

SetNearDeathDuration sets NearDeathDuration field to given value.

### HasNearDeathDuration

`func (o *NPCUnitV2) HasNearDeathDuration() bool`

HasNearDeathDuration returns a boolean if a field has been set.

### SetNearDeathDurationNil

`func (o *NPCUnitV2) SetNearDeathDurationNil(b bool)`

 SetNearDeathDurationNil sets the value for NearDeathDuration to be an explicit nil

### UnsetNearDeathDuration
`func (o *NPCUnitV2) UnsetNearDeathDuration()`

UnsetNearDeathDuration ensures that no value is present for NearDeathDuration, not even an explicit nil
### GetWalkSpeed

`func (o *NPCUnitV2) GetWalkSpeed() float32`

GetWalkSpeed returns the WalkSpeed field if non-nil, zero value otherwise.

### GetWalkSpeedOk

`func (o *NPCUnitV2) GetWalkSpeedOk() (*float32, bool)`

GetWalkSpeedOk returns a tuple with the WalkSpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWalkSpeed

`func (o *NPCUnitV2) SetWalkSpeed(v float32)`

SetWalkSpeed sets WalkSpeed field to given value.

### HasWalkSpeed

`func (o *NPCUnitV2) HasWalkSpeed() bool`

HasWalkSpeed returns a boolean if a field has been set.

### SetWalkSpeedNil

`func (o *NPCUnitV2) SetWalkSpeedNil(b bool)`

 SetWalkSpeedNil sets the value for WalkSpeed to be an explicit nil

### UnsetWalkSpeed
`func (o *NPCUnitV2) UnsetWalkSpeed()`

UnsetWalkSpeed ensures that no value is present for WalkSpeed, not even an explicit nil
### GetRunSpeed

`func (o *NPCUnitV2) GetRunSpeed() float32`

GetRunSpeed returns the RunSpeed field if non-nil, zero value otherwise.

### GetRunSpeedOk

`func (o *NPCUnitV2) GetRunSpeedOk() (*float32, bool)`

GetRunSpeedOk returns a tuple with the RunSpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRunSpeed

`func (o *NPCUnitV2) SetRunSpeed(v float32)`

SetRunSpeed sets RunSpeed field to given value.

### HasRunSpeed

`func (o *NPCUnitV2) HasRunSpeed() bool`

HasRunSpeed returns a boolean if a field has been set.

### SetRunSpeedNil

`func (o *NPCUnitV2) SetRunSpeedNil(b bool)`

 SetRunSpeedNil sets the value for RunSpeed to be an explicit nil

### UnsetRunSpeed
`func (o *NPCUnitV2) UnsetRunSpeed()`

UnsetRunSpeed ensures that no value is present for RunSpeed, not even an explicit nil
### GetAcceleration

`func (o *NPCUnitV2) GetAcceleration() float32`

GetAcceleration returns the Acceleration field if non-nil, zero value otherwise.

### GetAccelerationOk

`func (o *NPCUnitV2) GetAccelerationOk() (*float32, bool)`

GetAccelerationOk returns a tuple with the Acceleration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAcceleration

`func (o *NPCUnitV2) SetAcceleration(v float32)`

SetAcceleration sets Acceleration field to given value.

### HasAcceleration

`func (o *NPCUnitV2) HasAcceleration() bool`

HasAcceleration returns a boolean if a field has been set.

### SetAccelerationNil

`func (o *NPCUnitV2) SetAccelerationNil(b bool)`

 SetAccelerationNil sets the value for Acceleration to be an explicit nil

### UnsetAcceleration
`func (o *NPCUnitV2) UnsetAcceleration()`

UnsetAcceleration ensures that no value is present for Acceleration, not even an explicit nil
### GetMeleeDamage

`func (o *NPCUnitV2) GetMeleeDamage() float32`

GetMeleeDamage returns the MeleeDamage field if non-nil, zero value otherwise.

### GetMeleeDamageOk

`func (o *NPCUnitV2) GetMeleeDamageOk() (*float32, bool)`

GetMeleeDamageOk returns a tuple with the MeleeDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeleeDamage

`func (o *NPCUnitV2) SetMeleeDamage(v float32)`

SetMeleeDamage sets MeleeDamage field to given value.

### HasMeleeDamage

`func (o *NPCUnitV2) HasMeleeDamage() bool`

HasMeleeDamage returns a boolean if a field has been set.

### SetMeleeDamageNil

`func (o *NPCUnitV2) SetMeleeDamageNil(b bool)`

 SetMeleeDamageNil sets the value for MeleeDamage to be an explicit nil

### UnsetMeleeDamage
`func (o *NPCUnitV2) UnsetMeleeDamage()`

UnsetMeleeDamage ensures that no value is present for MeleeDamage, not even an explicit nil
### GetMeleeAttemptRange

`func (o *NPCUnitV2) GetMeleeAttemptRange() float32`

GetMeleeAttemptRange returns the MeleeAttemptRange field if non-nil, zero value otherwise.

### GetMeleeAttemptRangeOk

`func (o *NPCUnitV2) GetMeleeAttemptRangeOk() (*float32, bool)`

GetMeleeAttemptRangeOk returns a tuple with the MeleeAttemptRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeleeAttemptRange

`func (o *NPCUnitV2) SetMeleeAttemptRange(v float32)`

SetMeleeAttemptRange sets MeleeAttemptRange field to given value.

### HasMeleeAttemptRange

`func (o *NPCUnitV2) HasMeleeAttemptRange() bool`

HasMeleeAttemptRange returns a boolean if a field has been set.

### SetMeleeAttemptRangeNil

`func (o *NPCUnitV2) SetMeleeAttemptRangeNil(b bool)`

 SetMeleeAttemptRangeNil sets the value for MeleeAttemptRange to be an explicit nil

### UnsetMeleeAttemptRange
`func (o *NPCUnitV2) UnsetMeleeAttemptRange()`

UnsetMeleeAttemptRange ensures that no value is present for MeleeAttemptRange, not even an explicit nil
### GetMeleeHitRange

`func (o *NPCUnitV2) GetMeleeHitRange() float32`

GetMeleeHitRange returns the MeleeHitRange field if non-nil, zero value otherwise.

### GetMeleeHitRangeOk

`func (o *NPCUnitV2) GetMeleeHitRangeOk() (*float32, bool)`

GetMeleeHitRangeOk returns a tuple with the MeleeHitRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeleeHitRange

`func (o *NPCUnitV2) SetMeleeHitRange(v float32)`

SetMeleeHitRange sets MeleeHitRange field to given value.

### HasMeleeHitRange

`func (o *NPCUnitV2) HasMeleeHitRange() bool`

HasMeleeHitRange returns a boolean if a field has been set.

### SetMeleeHitRangeNil

`func (o *NPCUnitV2) SetMeleeHitRangeNil(b bool)`

 SetMeleeHitRangeNil sets the value for MeleeHitRange to be an explicit nil

### UnsetMeleeHitRange
`func (o *NPCUnitV2) UnsetMeleeHitRange()`

UnsetMeleeHitRange ensures that no value is present for MeleeHitRange, not even an explicit nil
### GetMeleeDuration

`func (o *NPCUnitV2) GetMeleeDuration() float32`

GetMeleeDuration returns the MeleeDuration field if non-nil, zero value otherwise.

### GetMeleeDurationOk

`func (o *NPCUnitV2) GetMeleeDurationOk() (*float32, bool)`

GetMeleeDurationOk returns a tuple with the MeleeDuration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeleeDuration

`func (o *NPCUnitV2) SetMeleeDuration(v float32)`

SetMeleeDuration sets MeleeDuration field to given value.

### HasMeleeDuration

`func (o *NPCUnitV2) HasMeleeDuration() bool`

HasMeleeDuration returns a boolean if a field has been set.

### SetMeleeDurationNil

`func (o *NPCUnitV2) SetMeleeDurationNil(b bool)`

 SetMeleeDurationNil sets the value for MeleeDuration to be an explicit nil

### UnsetMeleeDuration
`func (o *NPCUnitV2) UnsetMeleeDuration()`

UnsetMeleeDuration ensures that no value is present for MeleeDuration, not even an explicit nil
### GetAttackT1BossMaxRange

`func (o *NPCUnitV2) GetAttackT1BossMaxRange() float32`

GetAttackT1BossMaxRange returns the AttackT1BossMaxRange field if non-nil, zero value otherwise.

### GetAttackT1BossMaxRangeOk

`func (o *NPCUnitV2) GetAttackT1BossMaxRangeOk() (*float32, bool)`

GetAttackT1BossMaxRangeOk returns a tuple with the AttackT1BossMaxRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttackT1BossMaxRange

`func (o *NPCUnitV2) SetAttackT1BossMaxRange(v float32)`

SetAttackT1BossMaxRange sets AttackT1BossMaxRange field to given value.

### HasAttackT1BossMaxRange

`func (o *NPCUnitV2) HasAttackT1BossMaxRange() bool`

HasAttackT1BossMaxRange returns a boolean if a field has been set.

### SetAttackT1BossMaxRangeNil

`func (o *NPCUnitV2) SetAttackT1BossMaxRangeNil(b bool)`

 SetAttackT1BossMaxRangeNil sets the value for AttackT1BossMaxRange to be an explicit nil

### UnsetAttackT1BossMaxRange
`func (o *NPCUnitV2) UnsetAttackT1BossMaxRange()`

UnsetAttackT1BossMaxRange ensures that no value is present for AttackT1BossMaxRange, not even an explicit nil
### GetAttackT3BossMaxRange

`func (o *NPCUnitV2) GetAttackT3BossMaxRange() float32`

GetAttackT3BossMaxRange returns the AttackT3BossMaxRange field if non-nil, zero value otherwise.

### GetAttackT3BossMaxRangeOk

`func (o *NPCUnitV2) GetAttackT3BossMaxRangeOk() (*float32, bool)`

GetAttackT3BossMaxRangeOk returns a tuple with the AttackT3BossMaxRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttackT3BossMaxRange

`func (o *NPCUnitV2) SetAttackT3BossMaxRange(v float32)`

SetAttackT3BossMaxRange sets AttackT3BossMaxRange field to given value.

### HasAttackT3BossMaxRange

`func (o *NPCUnitV2) HasAttackT3BossMaxRange() bool`

HasAttackT3BossMaxRange returns a boolean if a field has been set.

### SetAttackT3BossMaxRangeNil

`func (o *NPCUnitV2) SetAttackT3BossMaxRangeNil(b bool)`

 SetAttackT3BossMaxRangeNil sets the value for AttackT3BossMaxRange to be an explicit nil

### UnsetAttackT3BossMaxRange
`func (o *NPCUnitV2) UnsetAttackT3BossMaxRange()`

UnsetAttackT3BossMaxRange ensures that no value is present for AttackT3BossMaxRange, not even an explicit nil
### GetAttackT3BossPhase2MaxRange

`func (o *NPCUnitV2) GetAttackT3BossPhase2MaxRange() float32`

GetAttackT3BossPhase2MaxRange returns the AttackT3BossPhase2MaxRange field if non-nil, zero value otherwise.

### GetAttackT3BossPhase2MaxRangeOk

`func (o *NPCUnitV2) GetAttackT3BossPhase2MaxRangeOk() (*float32, bool)`

GetAttackT3BossPhase2MaxRangeOk returns a tuple with the AttackT3BossPhase2MaxRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttackT3BossPhase2MaxRange

`func (o *NPCUnitV2) SetAttackT3BossPhase2MaxRange(v float32)`

SetAttackT3BossPhase2MaxRange sets AttackT3BossPhase2MaxRange field to given value.

### HasAttackT3BossPhase2MaxRange

`func (o *NPCUnitV2) HasAttackT3BossPhase2MaxRange() bool`

HasAttackT3BossPhase2MaxRange returns a boolean if a field has been set.

### SetAttackT3BossPhase2MaxRangeNil

`func (o *NPCUnitV2) SetAttackT3BossPhase2MaxRangeNil(b bool)`

 SetAttackT3BossPhase2MaxRangeNil sets the value for AttackT3BossPhase2MaxRange to be an explicit nil

### UnsetAttackT3BossPhase2MaxRange
`func (o *NPCUnitV2) UnsetAttackT3BossPhase2MaxRange()`

UnsetAttackT3BossPhase2MaxRange ensures that no value is present for AttackT3BossPhase2MaxRange, not even an explicit nil
### GetAttackTrooperMaxRange

`func (o *NPCUnitV2) GetAttackTrooperMaxRange() float32`

GetAttackTrooperMaxRange returns the AttackTrooperMaxRange field if non-nil, zero value otherwise.

### GetAttackTrooperMaxRangeOk

`func (o *NPCUnitV2) GetAttackTrooperMaxRangeOk() (*float32, bool)`

GetAttackTrooperMaxRangeOk returns a tuple with the AttackTrooperMaxRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttackTrooperMaxRange

`func (o *NPCUnitV2) SetAttackTrooperMaxRange(v float32)`

SetAttackTrooperMaxRange sets AttackTrooperMaxRange field to given value.

### HasAttackTrooperMaxRange

`func (o *NPCUnitV2) HasAttackTrooperMaxRange() bool`

HasAttackTrooperMaxRange returns a boolean if a field has been set.

### SetAttackTrooperMaxRangeNil

`func (o *NPCUnitV2) SetAttackTrooperMaxRangeNil(b bool)`

 SetAttackTrooperMaxRangeNil sets the value for AttackTrooperMaxRange to be an explicit nil

### UnsetAttackTrooperMaxRange
`func (o *NPCUnitV2) UnsetAttackTrooperMaxRange()`

UnsetAttackTrooperMaxRange ensures that no value is present for AttackTrooperMaxRange, not even an explicit nil
### GetT1BossDps

`func (o *NPCUnitV2) GetT1BossDps() float32`

GetT1BossDps returns the T1BossDps field if non-nil, zero value otherwise.

### GetT1BossDpsOk

`func (o *NPCUnitV2) GetT1BossDpsOk() (*float32, bool)`

GetT1BossDpsOk returns a tuple with the T1BossDps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT1BossDps

`func (o *NPCUnitV2) SetT1BossDps(v float32)`

SetT1BossDps sets T1BossDps field to given value.

### HasT1BossDps

`func (o *NPCUnitV2) HasT1BossDps() bool`

HasT1BossDps returns a boolean if a field has been set.

### SetT1BossDpsNil

`func (o *NPCUnitV2) SetT1BossDpsNil(b bool)`

 SetT1BossDpsNil sets the value for T1BossDps to be an explicit nil

### UnsetT1BossDps
`func (o *NPCUnitV2) UnsetT1BossDps()`

UnsetT1BossDps ensures that no value is present for T1BossDps, not even an explicit nil
### GetT1BossDpsbaseResist

`func (o *NPCUnitV2) GetT1BossDpsbaseResist() float32`

GetT1BossDpsbaseResist returns the T1BossDpsbaseResist field if non-nil, zero value otherwise.

### GetT1BossDpsbaseResistOk

`func (o *NPCUnitV2) GetT1BossDpsbaseResistOk() (*float32, bool)`

GetT1BossDpsbaseResistOk returns a tuple with the T1BossDpsbaseResist field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT1BossDpsbaseResist

`func (o *NPCUnitV2) SetT1BossDpsbaseResist(v float32)`

SetT1BossDpsbaseResist sets T1BossDpsbaseResist field to given value.

### HasT1BossDpsbaseResist

`func (o *NPCUnitV2) HasT1BossDpsbaseResist() bool`

HasT1BossDpsbaseResist returns a boolean if a field has been set.

### SetT1BossDpsbaseResistNil

`func (o *NPCUnitV2) SetT1BossDpsbaseResistNil(b bool)`

 SetT1BossDpsbaseResistNil sets the value for T1BossDpsbaseResist to be an explicit nil

### UnsetT1BossDpsbaseResist
`func (o *NPCUnitV2) UnsetT1BossDpsbaseResist()`

UnsetT1BossDpsbaseResist ensures that no value is present for T1BossDpsbaseResist, not even an explicit nil
### GetT1BossDpsmaxResist

`func (o *NPCUnitV2) GetT1BossDpsmaxResist() float32`

GetT1BossDpsmaxResist returns the T1BossDpsmaxResist field if non-nil, zero value otherwise.

### GetT1BossDpsmaxResistOk

`func (o *NPCUnitV2) GetT1BossDpsmaxResistOk() (*float32, bool)`

GetT1BossDpsmaxResistOk returns a tuple with the T1BossDpsmaxResist field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT1BossDpsmaxResist

`func (o *NPCUnitV2) SetT1BossDpsmaxResist(v float32)`

SetT1BossDpsmaxResist sets T1BossDpsmaxResist field to given value.

### HasT1BossDpsmaxResist

`func (o *NPCUnitV2) HasT1BossDpsmaxResist() bool`

HasT1BossDpsmaxResist returns a boolean if a field has been set.

### SetT1BossDpsmaxResistNil

`func (o *NPCUnitV2) SetT1BossDpsmaxResistNil(b bool)`

 SetT1BossDpsmaxResistNil sets the value for T1BossDpsmaxResist to be an explicit nil

### UnsetT1BossDpsmaxResist
`func (o *NPCUnitV2) UnsetT1BossDpsmaxResist()`

UnsetT1BossDpsmaxResist ensures that no value is present for T1BossDpsmaxResist, not even an explicit nil
### GetT1BossDpsmaxResistTimeInSeconds

`func (o *NPCUnitV2) GetT1BossDpsmaxResistTimeInSeconds() float32`

GetT1BossDpsmaxResistTimeInSeconds returns the T1BossDpsmaxResistTimeInSeconds field if non-nil, zero value otherwise.

### GetT1BossDpsmaxResistTimeInSecondsOk

`func (o *NPCUnitV2) GetT1BossDpsmaxResistTimeInSecondsOk() (*float32, bool)`

GetT1BossDpsmaxResistTimeInSecondsOk returns a tuple with the T1BossDpsmaxResistTimeInSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT1BossDpsmaxResistTimeInSeconds

`func (o *NPCUnitV2) SetT1BossDpsmaxResistTimeInSeconds(v float32)`

SetT1BossDpsmaxResistTimeInSeconds sets T1BossDpsmaxResistTimeInSeconds field to given value.

### HasT1BossDpsmaxResistTimeInSeconds

`func (o *NPCUnitV2) HasT1BossDpsmaxResistTimeInSeconds() bool`

HasT1BossDpsmaxResistTimeInSeconds returns a boolean if a field has been set.

### SetT1BossDpsmaxResistTimeInSecondsNil

`func (o *NPCUnitV2) SetT1BossDpsmaxResistTimeInSecondsNil(b bool)`

 SetT1BossDpsmaxResistTimeInSecondsNil sets the value for T1BossDpsmaxResistTimeInSeconds to be an explicit nil

### UnsetT1BossDpsmaxResistTimeInSeconds
`func (o *NPCUnitV2) UnsetT1BossDpsmaxResistTimeInSeconds()`

UnsetT1BossDpsmaxResistTimeInSeconds ensures that no value is present for T1BossDpsmaxResistTimeInSeconds, not even an explicit nil
### GetT2BossDps

`func (o *NPCUnitV2) GetT2BossDps() float32`

GetT2BossDps returns the T2BossDps field if non-nil, zero value otherwise.

### GetT2BossDpsOk

`func (o *NPCUnitV2) GetT2BossDpsOk() (*float32, bool)`

GetT2BossDpsOk returns a tuple with the T2BossDps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT2BossDps

`func (o *NPCUnitV2) SetT2BossDps(v float32)`

SetT2BossDps sets T2BossDps field to given value.

### HasT2BossDps

`func (o *NPCUnitV2) HasT2BossDps() bool`

HasT2BossDps returns a boolean if a field has been set.

### SetT2BossDpsNil

`func (o *NPCUnitV2) SetT2BossDpsNil(b bool)`

 SetT2BossDpsNil sets the value for T2BossDps to be an explicit nil

### UnsetT2BossDps
`func (o *NPCUnitV2) UnsetT2BossDps()`

UnsetT2BossDps ensures that no value is present for T2BossDps, not even an explicit nil
### GetT2BossDpsbaseResist

`func (o *NPCUnitV2) GetT2BossDpsbaseResist() float32`

GetT2BossDpsbaseResist returns the T2BossDpsbaseResist field if non-nil, zero value otherwise.

### GetT2BossDpsbaseResistOk

`func (o *NPCUnitV2) GetT2BossDpsbaseResistOk() (*float32, bool)`

GetT2BossDpsbaseResistOk returns a tuple with the T2BossDpsbaseResist field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT2BossDpsbaseResist

`func (o *NPCUnitV2) SetT2BossDpsbaseResist(v float32)`

SetT2BossDpsbaseResist sets T2BossDpsbaseResist field to given value.

### HasT2BossDpsbaseResist

`func (o *NPCUnitV2) HasT2BossDpsbaseResist() bool`

HasT2BossDpsbaseResist returns a boolean if a field has been set.

### SetT2BossDpsbaseResistNil

`func (o *NPCUnitV2) SetT2BossDpsbaseResistNil(b bool)`

 SetT2BossDpsbaseResistNil sets the value for T2BossDpsbaseResist to be an explicit nil

### UnsetT2BossDpsbaseResist
`func (o *NPCUnitV2) UnsetT2BossDpsbaseResist()`

UnsetT2BossDpsbaseResist ensures that no value is present for T2BossDpsbaseResist, not even an explicit nil
### GetT2BossDpsmaxResist

`func (o *NPCUnitV2) GetT2BossDpsmaxResist() float32`

GetT2BossDpsmaxResist returns the T2BossDpsmaxResist field if non-nil, zero value otherwise.

### GetT2BossDpsmaxResistOk

`func (o *NPCUnitV2) GetT2BossDpsmaxResistOk() (*float32, bool)`

GetT2BossDpsmaxResistOk returns a tuple with the T2BossDpsmaxResist field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT2BossDpsmaxResist

`func (o *NPCUnitV2) SetT2BossDpsmaxResist(v float32)`

SetT2BossDpsmaxResist sets T2BossDpsmaxResist field to given value.

### HasT2BossDpsmaxResist

`func (o *NPCUnitV2) HasT2BossDpsmaxResist() bool`

HasT2BossDpsmaxResist returns a boolean if a field has been set.

### SetT2BossDpsmaxResistNil

`func (o *NPCUnitV2) SetT2BossDpsmaxResistNil(b bool)`

 SetT2BossDpsmaxResistNil sets the value for T2BossDpsmaxResist to be an explicit nil

### UnsetT2BossDpsmaxResist
`func (o *NPCUnitV2) UnsetT2BossDpsmaxResist()`

UnsetT2BossDpsmaxResist ensures that no value is present for T2BossDpsmaxResist, not even an explicit nil
### GetT2BossDpsmaxResistTimeInSeconds

`func (o *NPCUnitV2) GetT2BossDpsmaxResistTimeInSeconds() float32`

GetT2BossDpsmaxResistTimeInSeconds returns the T2BossDpsmaxResistTimeInSeconds field if non-nil, zero value otherwise.

### GetT2BossDpsmaxResistTimeInSecondsOk

`func (o *NPCUnitV2) GetT2BossDpsmaxResistTimeInSecondsOk() (*float32, bool)`

GetT2BossDpsmaxResistTimeInSecondsOk returns a tuple with the T2BossDpsmaxResistTimeInSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT2BossDpsmaxResistTimeInSeconds

`func (o *NPCUnitV2) SetT2BossDpsmaxResistTimeInSeconds(v float32)`

SetT2BossDpsmaxResistTimeInSeconds sets T2BossDpsmaxResistTimeInSeconds field to given value.

### HasT2BossDpsmaxResistTimeInSeconds

`func (o *NPCUnitV2) HasT2BossDpsmaxResistTimeInSeconds() bool`

HasT2BossDpsmaxResistTimeInSeconds returns a boolean if a field has been set.

### SetT2BossDpsmaxResistTimeInSecondsNil

`func (o *NPCUnitV2) SetT2BossDpsmaxResistTimeInSecondsNil(b bool)`

 SetT2BossDpsmaxResistTimeInSecondsNil sets the value for T2BossDpsmaxResistTimeInSeconds to be an explicit nil

### UnsetT2BossDpsmaxResistTimeInSeconds
`func (o *NPCUnitV2) UnsetT2BossDpsmaxResistTimeInSeconds()`

UnsetT2BossDpsmaxResistTimeInSeconds ensures that no value is present for T2BossDpsmaxResistTimeInSeconds, not even an explicit nil
### GetT3BossDps

`func (o *NPCUnitV2) GetT3BossDps() float32`

GetT3BossDps returns the T3BossDps field if non-nil, zero value otherwise.

### GetT3BossDpsOk

`func (o *NPCUnitV2) GetT3BossDpsOk() (*float32, bool)`

GetT3BossDpsOk returns a tuple with the T3BossDps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetT3BossDps

`func (o *NPCUnitV2) SetT3BossDps(v float32)`

SetT3BossDps sets T3BossDps field to given value.

### HasT3BossDps

`func (o *NPCUnitV2) HasT3BossDps() bool`

HasT3BossDps returns a boolean if a field has been set.

### SetT3BossDpsNil

`func (o *NPCUnitV2) SetT3BossDpsNil(b bool)`

 SetT3BossDpsNil sets the value for T3BossDps to be an explicit nil

### UnsetT3BossDps
`func (o *NPCUnitV2) UnsetT3BossDps()`

UnsetT3BossDps ensures that no value is present for T3BossDps, not even an explicit nil
### GetGeneratorBossDps

`func (o *NPCUnitV2) GetGeneratorBossDps() float32`

GetGeneratorBossDps returns the GeneratorBossDps field if non-nil, zero value otherwise.

### GetGeneratorBossDpsOk

`func (o *NPCUnitV2) GetGeneratorBossDpsOk() (*float32, bool)`

GetGeneratorBossDpsOk returns a tuple with the GeneratorBossDps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGeneratorBossDps

`func (o *NPCUnitV2) SetGeneratorBossDps(v float32)`

SetGeneratorBossDps sets GeneratorBossDps field to given value.

### HasGeneratorBossDps

`func (o *NPCUnitV2) HasGeneratorBossDps() bool`

HasGeneratorBossDps returns a boolean if a field has been set.

### SetGeneratorBossDpsNil

`func (o *NPCUnitV2) SetGeneratorBossDpsNil(b bool)`

 SetGeneratorBossDpsNil sets the value for GeneratorBossDps to be an explicit nil

### UnsetGeneratorBossDps
`func (o *NPCUnitV2) UnsetGeneratorBossDps()`

UnsetGeneratorBossDps ensures that no value is present for GeneratorBossDps, not even an explicit nil
### GetBarrackBossDps

`func (o *NPCUnitV2) GetBarrackBossDps() float32`

GetBarrackBossDps returns the BarrackBossDps field if non-nil, zero value otherwise.

### GetBarrackBossDpsOk

`func (o *NPCUnitV2) GetBarrackBossDpsOk() (*float32, bool)`

GetBarrackBossDpsOk returns a tuple with the BarrackBossDps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBarrackBossDps

`func (o *NPCUnitV2) SetBarrackBossDps(v float32)`

SetBarrackBossDps sets BarrackBossDps field to given value.

### HasBarrackBossDps

`func (o *NPCUnitV2) HasBarrackBossDps() bool`

HasBarrackBossDps returns a boolean if a field has been set.

### SetBarrackBossDpsNil

`func (o *NPCUnitV2) SetBarrackBossDpsNil(b bool)`

 SetBarrackBossDpsNil sets the value for BarrackBossDps to be an explicit nil

### UnsetBarrackBossDps
`func (o *NPCUnitV2) UnsetBarrackBossDps()`

UnsetBarrackBossDps ensures that no value is present for BarrackBossDps, not even an explicit nil
### GetPlayerDps

`func (o *NPCUnitV2) GetPlayerDps() float32`

GetPlayerDps returns the PlayerDps field if non-nil, zero value otherwise.

### GetPlayerDpsOk

`func (o *NPCUnitV2) GetPlayerDpsOk() (*float32, bool)`

GetPlayerDpsOk returns a tuple with the PlayerDps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerDps

`func (o *NPCUnitV2) SetPlayerDps(v float32)`

SetPlayerDps sets PlayerDps field to given value.

### HasPlayerDps

`func (o *NPCUnitV2) HasPlayerDps() bool`

HasPlayerDps returns a boolean if a field has been set.

### SetPlayerDpsNil

`func (o *NPCUnitV2) SetPlayerDpsNil(b bool)`

 SetPlayerDpsNil sets the value for PlayerDps to be an explicit nil

### UnsetPlayerDps
`func (o *NPCUnitV2) UnsetPlayerDps()`

UnsetPlayerDps ensures that no value is present for PlayerDps, not even an explicit nil
### GetTrooperDps

`func (o *NPCUnitV2) GetTrooperDps() float32`

GetTrooperDps returns the TrooperDps field if non-nil, zero value otherwise.

### GetTrooperDpsOk

`func (o *NPCUnitV2) GetTrooperDpsOk() (*float32, bool)`

GetTrooperDpsOk returns a tuple with the TrooperDps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrooperDps

`func (o *NPCUnitV2) SetTrooperDps(v float32)`

SetTrooperDps sets TrooperDps field to given value.

### HasTrooperDps

`func (o *NPCUnitV2) HasTrooperDps() bool`

HasTrooperDps returns a boolean if a field has been set.

### SetTrooperDpsNil

`func (o *NPCUnitV2) SetTrooperDpsNil(b bool)`

 SetTrooperDpsNil sets the value for TrooperDps to be an explicit nil

### UnsetTrooperDps
`func (o *NPCUnitV2) UnsetTrooperDps()`

UnsetTrooperDps ensures that no value is present for TrooperDps, not even an explicit nil
### GetHealthBarColorFriend

`func (o *NPCUnitV2) GetHealthBarColorFriend() HealthBarColorFriend`

GetHealthBarColorFriend returns the HealthBarColorFriend field if non-nil, zero value otherwise.

### GetHealthBarColorFriendOk

`func (o *NPCUnitV2) GetHealthBarColorFriendOk() (*HealthBarColorFriend, bool)`

GetHealthBarColorFriendOk returns a tuple with the HealthBarColorFriend field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHealthBarColorFriend

`func (o *NPCUnitV2) SetHealthBarColorFriend(v HealthBarColorFriend)`

SetHealthBarColorFriend sets HealthBarColorFriend field to given value.

### HasHealthBarColorFriend

`func (o *NPCUnitV2) HasHealthBarColorFriend() bool`

HasHealthBarColorFriend returns a boolean if a field has been set.

### SetHealthBarColorFriendNil

`func (o *NPCUnitV2) SetHealthBarColorFriendNil(b bool)`

 SetHealthBarColorFriendNil sets the value for HealthBarColorFriend to be an explicit nil

### UnsetHealthBarColorFriend
`func (o *NPCUnitV2) UnsetHealthBarColorFriend()`

UnsetHealthBarColorFriend ensures that no value is present for HealthBarColorFriend, not even an explicit nil
### GetHealthBarColorEnemy

`func (o *NPCUnitV2) GetHealthBarColorEnemy() HealthBarColorEnemy`

GetHealthBarColorEnemy returns the HealthBarColorEnemy field if non-nil, zero value otherwise.

### GetHealthBarColorEnemyOk

`func (o *NPCUnitV2) GetHealthBarColorEnemyOk() (*HealthBarColorEnemy, bool)`

GetHealthBarColorEnemyOk returns a tuple with the HealthBarColorEnemy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHealthBarColorEnemy

`func (o *NPCUnitV2) SetHealthBarColorEnemy(v HealthBarColorEnemy)`

SetHealthBarColorEnemy sets HealthBarColorEnemy field to given value.

### HasHealthBarColorEnemy

`func (o *NPCUnitV2) HasHealthBarColorEnemy() bool`

HasHealthBarColorEnemy returns a boolean if a field has been set.

### SetHealthBarColorEnemyNil

`func (o *NPCUnitV2) SetHealthBarColorEnemyNil(b bool)`

 SetHealthBarColorEnemyNil sets the value for HealthBarColorEnemy to be an explicit nil

### UnsetHealthBarColorEnemy
`func (o *NPCUnitV2) UnsetHealthBarColorEnemy()`

UnsetHealthBarColorEnemy ensures that no value is present for HealthBarColorEnemy, not even an explicit nil
### GetHealthBarColorTeam1

`func (o *NPCUnitV2) GetHealthBarColorTeam1() HealthBarColorTeam1`

GetHealthBarColorTeam1 returns the HealthBarColorTeam1 field if non-nil, zero value otherwise.

### GetHealthBarColorTeam1Ok

`func (o *NPCUnitV2) GetHealthBarColorTeam1Ok() (*HealthBarColorTeam1, bool)`

GetHealthBarColorTeam1Ok returns a tuple with the HealthBarColorTeam1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHealthBarColorTeam1

`func (o *NPCUnitV2) SetHealthBarColorTeam1(v HealthBarColorTeam1)`

SetHealthBarColorTeam1 sets HealthBarColorTeam1 field to given value.

### HasHealthBarColorTeam1

`func (o *NPCUnitV2) HasHealthBarColorTeam1() bool`

HasHealthBarColorTeam1 returns a boolean if a field has been set.

### SetHealthBarColorTeam1Nil

`func (o *NPCUnitV2) SetHealthBarColorTeam1Nil(b bool)`

 SetHealthBarColorTeam1Nil sets the value for HealthBarColorTeam1 to be an explicit nil

### UnsetHealthBarColorTeam1
`func (o *NPCUnitV2) UnsetHealthBarColorTeam1()`

UnsetHealthBarColorTeam1 ensures that no value is present for HealthBarColorTeam1, not even an explicit nil
### GetHealthBarColorTeam2

`func (o *NPCUnitV2) GetHealthBarColorTeam2() HealthBarColorTeam2`

GetHealthBarColorTeam2 returns the HealthBarColorTeam2 field if non-nil, zero value otherwise.

### GetHealthBarColorTeam2Ok

`func (o *NPCUnitV2) GetHealthBarColorTeam2Ok() (*HealthBarColorTeam2, bool)`

GetHealthBarColorTeam2Ok returns a tuple with the HealthBarColorTeam2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHealthBarColorTeam2

`func (o *NPCUnitV2) SetHealthBarColorTeam2(v HealthBarColorTeam2)`

SetHealthBarColorTeam2 sets HealthBarColorTeam2 field to given value.

### HasHealthBarColorTeam2

`func (o *NPCUnitV2) HasHealthBarColorTeam2() bool`

HasHealthBarColorTeam2 returns a boolean if a field has been set.

### SetHealthBarColorTeam2Nil

`func (o *NPCUnitV2) SetHealthBarColorTeam2Nil(b bool)`

 SetHealthBarColorTeam2Nil sets the value for HealthBarColorTeam2 to be an explicit nil

### UnsetHealthBarColorTeam2
`func (o *NPCUnitV2) UnsetHealthBarColorTeam2()`

UnsetHealthBarColorTeam2 ensures that no value is present for HealthBarColorTeam2, not even an explicit nil
### GetHealthBarColorTeamNeutral

`func (o *NPCUnitV2) GetHealthBarColorTeamNeutral() HealthBarColorTeamNeutral`

GetHealthBarColorTeamNeutral returns the HealthBarColorTeamNeutral field if non-nil, zero value otherwise.

### GetHealthBarColorTeamNeutralOk

`func (o *NPCUnitV2) GetHealthBarColorTeamNeutralOk() (*HealthBarColorTeamNeutral, bool)`

GetHealthBarColorTeamNeutralOk returns a tuple with the HealthBarColorTeamNeutral field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHealthBarColorTeamNeutral

`func (o *NPCUnitV2) SetHealthBarColorTeamNeutral(v HealthBarColorTeamNeutral)`

SetHealthBarColorTeamNeutral sets HealthBarColorTeamNeutral field to given value.

### HasHealthBarColorTeamNeutral

`func (o *NPCUnitV2) HasHealthBarColorTeamNeutral() bool`

HasHealthBarColorTeamNeutral returns a boolean if a field has been set.

### SetHealthBarColorTeamNeutralNil

`func (o *NPCUnitV2) SetHealthBarColorTeamNeutralNil(b bool)`

 SetHealthBarColorTeamNeutralNil sets the value for HealthBarColorTeamNeutral to be an explicit nil

### UnsetHealthBarColorTeamNeutral
`func (o *NPCUnitV2) UnsetHealthBarColorTeamNeutral()`

UnsetHealthBarColorTeamNeutral ensures that no value is present for HealthBarColorTeamNeutral, not even an explicit nil
### GetGlowColorFriend

`func (o *NPCUnitV2) GetGlowColorFriend() GlowColorFriend`

GetGlowColorFriend returns the GlowColorFriend field if non-nil, zero value otherwise.

### GetGlowColorFriendOk

`func (o *NPCUnitV2) GetGlowColorFriendOk() (*GlowColorFriend, bool)`

GetGlowColorFriendOk returns a tuple with the GlowColorFriend field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGlowColorFriend

`func (o *NPCUnitV2) SetGlowColorFriend(v GlowColorFriend)`

SetGlowColorFriend sets GlowColorFriend field to given value.

### HasGlowColorFriend

`func (o *NPCUnitV2) HasGlowColorFriend() bool`

HasGlowColorFriend returns a boolean if a field has been set.

### SetGlowColorFriendNil

`func (o *NPCUnitV2) SetGlowColorFriendNil(b bool)`

 SetGlowColorFriendNil sets the value for GlowColorFriend to be an explicit nil

### UnsetGlowColorFriend
`func (o *NPCUnitV2) UnsetGlowColorFriend()`

UnsetGlowColorFriend ensures that no value is present for GlowColorFriend, not even an explicit nil
### GetGlowColorEnemy

`func (o *NPCUnitV2) GetGlowColorEnemy() GlowColorEnemy`

GetGlowColorEnemy returns the GlowColorEnemy field if non-nil, zero value otherwise.

### GetGlowColorEnemyOk

`func (o *NPCUnitV2) GetGlowColorEnemyOk() (*GlowColorEnemy, bool)`

GetGlowColorEnemyOk returns a tuple with the GlowColorEnemy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGlowColorEnemy

`func (o *NPCUnitV2) SetGlowColorEnemy(v GlowColorEnemy)`

SetGlowColorEnemy sets GlowColorEnemy field to given value.

### HasGlowColorEnemy

`func (o *NPCUnitV2) HasGlowColorEnemy() bool`

HasGlowColorEnemy returns a boolean if a field has been set.

### SetGlowColorEnemyNil

`func (o *NPCUnitV2) SetGlowColorEnemyNil(b bool)`

 SetGlowColorEnemyNil sets the value for GlowColorEnemy to be an explicit nil

### UnsetGlowColorEnemy
`func (o *NPCUnitV2) UnsetGlowColorEnemy()`

UnsetGlowColorEnemy ensures that no value is present for GlowColorEnemy, not even an explicit nil
### GetGlowColorTeam1

`func (o *NPCUnitV2) GetGlowColorTeam1() GlowColorTeam1`

GetGlowColorTeam1 returns the GlowColorTeam1 field if non-nil, zero value otherwise.

### GetGlowColorTeam1Ok

`func (o *NPCUnitV2) GetGlowColorTeam1Ok() (*GlowColorTeam1, bool)`

GetGlowColorTeam1Ok returns a tuple with the GlowColorTeam1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGlowColorTeam1

`func (o *NPCUnitV2) SetGlowColorTeam1(v GlowColorTeam1)`

SetGlowColorTeam1 sets GlowColorTeam1 field to given value.

### HasGlowColorTeam1

`func (o *NPCUnitV2) HasGlowColorTeam1() bool`

HasGlowColorTeam1 returns a boolean if a field has been set.

### SetGlowColorTeam1Nil

`func (o *NPCUnitV2) SetGlowColorTeam1Nil(b bool)`

 SetGlowColorTeam1Nil sets the value for GlowColorTeam1 to be an explicit nil

### UnsetGlowColorTeam1
`func (o *NPCUnitV2) UnsetGlowColorTeam1()`

UnsetGlowColorTeam1 ensures that no value is present for GlowColorTeam1, not even an explicit nil
### GetGlowColorTeam2

`func (o *NPCUnitV2) GetGlowColorTeam2() GlowColorTeam2`

GetGlowColorTeam2 returns the GlowColorTeam2 field if non-nil, zero value otherwise.

### GetGlowColorTeam2Ok

`func (o *NPCUnitV2) GetGlowColorTeam2Ok() (*GlowColorTeam2, bool)`

GetGlowColorTeam2Ok returns a tuple with the GlowColorTeam2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGlowColorTeam2

`func (o *NPCUnitV2) SetGlowColorTeam2(v GlowColorTeam2)`

SetGlowColorTeam2 sets GlowColorTeam2 field to given value.

### HasGlowColorTeam2

`func (o *NPCUnitV2) HasGlowColorTeam2() bool`

HasGlowColorTeam2 returns a boolean if a field has been set.

### SetGlowColorTeam2Nil

`func (o *NPCUnitV2) SetGlowColorTeam2Nil(b bool)`

 SetGlowColorTeam2Nil sets the value for GlowColorTeam2 to be an explicit nil

### UnsetGlowColorTeam2
`func (o *NPCUnitV2) UnsetGlowColorTeam2()`

UnsetGlowColorTeam2 ensures that no value is present for GlowColorTeam2, not even an explicit nil
### GetGlowColorTeamNeutral

`func (o *NPCUnitV2) GetGlowColorTeamNeutral() GlowColorTeamNeutral`

GetGlowColorTeamNeutral returns the GlowColorTeamNeutral field if non-nil, zero value otherwise.

### GetGlowColorTeamNeutralOk

`func (o *NPCUnitV2) GetGlowColorTeamNeutralOk() (*GlowColorTeamNeutral, bool)`

GetGlowColorTeamNeutralOk returns a tuple with the GlowColorTeamNeutral field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGlowColorTeamNeutral

`func (o *NPCUnitV2) SetGlowColorTeamNeutral(v GlowColorTeamNeutral)`

SetGlowColorTeamNeutral sets GlowColorTeamNeutral field to given value.

### HasGlowColorTeamNeutral

`func (o *NPCUnitV2) HasGlowColorTeamNeutral() bool`

HasGlowColorTeamNeutral returns a boolean if a field has been set.

### SetGlowColorTeamNeutralNil

`func (o *NPCUnitV2) SetGlowColorTeamNeutralNil(b bool)`

 SetGlowColorTeamNeutralNil sets the value for GlowColorTeamNeutral to be an explicit nil

### UnsetGlowColorTeamNeutral
`func (o *NPCUnitV2) UnsetGlowColorTeamNeutral()`

UnsetGlowColorTeamNeutral ensures that no value is present for GlowColorTeamNeutral, not even an explicit nil
### GetId

`func (o *NPCUnitV2) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *NPCUnitV2) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *NPCUnitV2) SetId(v int64)`

SetId sets Id field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


