# RawHeroStartingStatsV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MaxMoveSpeed** | **float32** |  | 
**SprintSpeed** | **float32** |  | 
**CrouchSpeed** | **float32** |  | 
**MoveAcceleration** | **float32** |  | 
**LightMeleeDamage** | **float32** |  | 
**HeavyMeleeDamage** | **int32** |  | 
**MaxHealth** | **int32** |  | 
**WeaponPower** | **int32** |  | 
**ReloadSpeed** | **int32** |  | 
**WeaponPowerScale** | **int32** |  | 
**ProcBuildUpRateScale** | **int32** |  | 
**Stamina** | **int32** |  | 
**BaseHealthRegen** | **float32** |  | 
**StaminaRegenPerSecond** | **float32** |  | 
**AbilityResourceMax** | **int32** |  | 
**AbilityResourceRegenPerSecond** | **int32** |  | 
**CritDamageReceivedScale** | **float32** |  | 
**TechDuration** | **int32** |  | 
**TechArmorDamageReduction** | Pointer to **NullableFloat32** |  | [optional] 
**TechRange** | **int32** |  | 
**BulletArmorDamageReduction** | Pointer to **NullableFloat32** |  | [optional] 

## Methods

### NewRawHeroStartingStatsV2

`func NewRawHeroStartingStatsV2(maxMoveSpeed float32, sprintSpeed float32, crouchSpeed float32, moveAcceleration float32, lightMeleeDamage float32, heavyMeleeDamage int32, maxHealth int32, weaponPower int32, reloadSpeed int32, weaponPowerScale int32, procBuildUpRateScale int32, stamina int32, baseHealthRegen float32, staminaRegenPerSecond float32, abilityResourceMax int32, abilityResourceRegenPerSecond int32, critDamageReceivedScale float32, techDuration int32, techRange int32, ) *RawHeroStartingStatsV2`

NewRawHeroStartingStatsV2 instantiates a new RawHeroStartingStatsV2 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRawHeroStartingStatsV2WithDefaults

`func NewRawHeroStartingStatsV2WithDefaults() *RawHeroStartingStatsV2`

NewRawHeroStartingStatsV2WithDefaults instantiates a new RawHeroStartingStatsV2 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMaxMoveSpeed

`func (o *RawHeroStartingStatsV2) GetMaxMoveSpeed() float32`

GetMaxMoveSpeed returns the MaxMoveSpeed field if non-nil, zero value otherwise.

### GetMaxMoveSpeedOk

`func (o *RawHeroStartingStatsV2) GetMaxMoveSpeedOk() (*float32, bool)`

GetMaxMoveSpeedOk returns a tuple with the MaxMoveSpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxMoveSpeed

`func (o *RawHeroStartingStatsV2) SetMaxMoveSpeed(v float32)`

SetMaxMoveSpeed sets MaxMoveSpeed field to given value.


### GetSprintSpeed

`func (o *RawHeroStartingStatsV2) GetSprintSpeed() float32`

GetSprintSpeed returns the SprintSpeed field if non-nil, zero value otherwise.

### GetSprintSpeedOk

`func (o *RawHeroStartingStatsV2) GetSprintSpeedOk() (*float32, bool)`

GetSprintSpeedOk returns a tuple with the SprintSpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSprintSpeed

`func (o *RawHeroStartingStatsV2) SetSprintSpeed(v float32)`

SetSprintSpeed sets SprintSpeed field to given value.


### GetCrouchSpeed

`func (o *RawHeroStartingStatsV2) GetCrouchSpeed() float32`

GetCrouchSpeed returns the CrouchSpeed field if non-nil, zero value otherwise.

### GetCrouchSpeedOk

`func (o *RawHeroStartingStatsV2) GetCrouchSpeedOk() (*float32, bool)`

GetCrouchSpeedOk returns a tuple with the CrouchSpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrouchSpeed

`func (o *RawHeroStartingStatsV2) SetCrouchSpeed(v float32)`

SetCrouchSpeed sets CrouchSpeed field to given value.


### GetMoveAcceleration

`func (o *RawHeroStartingStatsV2) GetMoveAcceleration() float32`

GetMoveAcceleration returns the MoveAcceleration field if non-nil, zero value otherwise.

### GetMoveAccelerationOk

`func (o *RawHeroStartingStatsV2) GetMoveAccelerationOk() (*float32, bool)`

GetMoveAccelerationOk returns a tuple with the MoveAcceleration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMoveAcceleration

`func (o *RawHeroStartingStatsV2) SetMoveAcceleration(v float32)`

SetMoveAcceleration sets MoveAcceleration field to given value.


### GetLightMeleeDamage

`func (o *RawHeroStartingStatsV2) GetLightMeleeDamage() float32`

GetLightMeleeDamage returns the LightMeleeDamage field if non-nil, zero value otherwise.

### GetLightMeleeDamageOk

`func (o *RawHeroStartingStatsV2) GetLightMeleeDamageOk() (*float32, bool)`

GetLightMeleeDamageOk returns a tuple with the LightMeleeDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLightMeleeDamage

`func (o *RawHeroStartingStatsV2) SetLightMeleeDamage(v float32)`

SetLightMeleeDamage sets LightMeleeDamage field to given value.


### GetHeavyMeleeDamage

`func (o *RawHeroStartingStatsV2) GetHeavyMeleeDamage() int32`

GetHeavyMeleeDamage returns the HeavyMeleeDamage field if non-nil, zero value otherwise.

### GetHeavyMeleeDamageOk

`func (o *RawHeroStartingStatsV2) GetHeavyMeleeDamageOk() (*int32, bool)`

GetHeavyMeleeDamageOk returns a tuple with the HeavyMeleeDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeavyMeleeDamage

`func (o *RawHeroStartingStatsV2) SetHeavyMeleeDamage(v int32)`

SetHeavyMeleeDamage sets HeavyMeleeDamage field to given value.


### GetMaxHealth

`func (o *RawHeroStartingStatsV2) GetMaxHealth() int32`

GetMaxHealth returns the MaxHealth field if non-nil, zero value otherwise.

### GetMaxHealthOk

`func (o *RawHeroStartingStatsV2) GetMaxHealthOk() (*int32, bool)`

GetMaxHealthOk returns a tuple with the MaxHealth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxHealth

`func (o *RawHeroStartingStatsV2) SetMaxHealth(v int32)`

SetMaxHealth sets MaxHealth field to given value.


### GetWeaponPower

`func (o *RawHeroStartingStatsV2) GetWeaponPower() int32`

GetWeaponPower returns the WeaponPower field if non-nil, zero value otherwise.

### GetWeaponPowerOk

`func (o *RawHeroStartingStatsV2) GetWeaponPowerOk() (*int32, bool)`

GetWeaponPowerOk returns a tuple with the WeaponPower field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponPower

`func (o *RawHeroStartingStatsV2) SetWeaponPower(v int32)`

SetWeaponPower sets WeaponPower field to given value.


### GetReloadSpeed

`func (o *RawHeroStartingStatsV2) GetReloadSpeed() int32`

GetReloadSpeed returns the ReloadSpeed field if non-nil, zero value otherwise.

### GetReloadSpeedOk

`func (o *RawHeroStartingStatsV2) GetReloadSpeedOk() (*int32, bool)`

GetReloadSpeedOk returns a tuple with the ReloadSpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReloadSpeed

`func (o *RawHeroStartingStatsV2) SetReloadSpeed(v int32)`

SetReloadSpeed sets ReloadSpeed field to given value.


### GetWeaponPowerScale

`func (o *RawHeroStartingStatsV2) GetWeaponPowerScale() int32`

GetWeaponPowerScale returns the WeaponPowerScale field if non-nil, zero value otherwise.

### GetWeaponPowerScaleOk

`func (o *RawHeroStartingStatsV2) GetWeaponPowerScaleOk() (*int32, bool)`

GetWeaponPowerScaleOk returns a tuple with the WeaponPowerScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponPowerScale

`func (o *RawHeroStartingStatsV2) SetWeaponPowerScale(v int32)`

SetWeaponPowerScale sets WeaponPowerScale field to given value.


### GetProcBuildUpRateScale

`func (o *RawHeroStartingStatsV2) GetProcBuildUpRateScale() int32`

GetProcBuildUpRateScale returns the ProcBuildUpRateScale field if non-nil, zero value otherwise.

### GetProcBuildUpRateScaleOk

`func (o *RawHeroStartingStatsV2) GetProcBuildUpRateScaleOk() (*int32, bool)`

GetProcBuildUpRateScaleOk returns a tuple with the ProcBuildUpRateScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProcBuildUpRateScale

`func (o *RawHeroStartingStatsV2) SetProcBuildUpRateScale(v int32)`

SetProcBuildUpRateScale sets ProcBuildUpRateScale field to given value.


### GetStamina

`func (o *RawHeroStartingStatsV2) GetStamina() int32`

GetStamina returns the Stamina field if non-nil, zero value otherwise.

### GetStaminaOk

`func (o *RawHeroStartingStatsV2) GetStaminaOk() (*int32, bool)`

GetStaminaOk returns a tuple with the Stamina field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStamina

`func (o *RawHeroStartingStatsV2) SetStamina(v int32)`

SetStamina sets Stamina field to given value.


### GetBaseHealthRegen

`func (o *RawHeroStartingStatsV2) GetBaseHealthRegen() float32`

GetBaseHealthRegen returns the BaseHealthRegen field if non-nil, zero value otherwise.

### GetBaseHealthRegenOk

`func (o *RawHeroStartingStatsV2) GetBaseHealthRegenOk() (*float32, bool)`

GetBaseHealthRegenOk returns a tuple with the BaseHealthRegen field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaseHealthRegen

`func (o *RawHeroStartingStatsV2) SetBaseHealthRegen(v float32)`

SetBaseHealthRegen sets BaseHealthRegen field to given value.


### GetStaminaRegenPerSecond

`func (o *RawHeroStartingStatsV2) GetStaminaRegenPerSecond() float32`

GetStaminaRegenPerSecond returns the StaminaRegenPerSecond field if non-nil, zero value otherwise.

### GetStaminaRegenPerSecondOk

`func (o *RawHeroStartingStatsV2) GetStaminaRegenPerSecondOk() (*float32, bool)`

GetStaminaRegenPerSecondOk returns a tuple with the StaminaRegenPerSecond field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStaminaRegenPerSecond

`func (o *RawHeroStartingStatsV2) SetStaminaRegenPerSecond(v float32)`

SetStaminaRegenPerSecond sets StaminaRegenPerSecond field to given value.


### GetAbilityResourceMax

`func (o *RawHeroStartingStatsV2) GetAbilityResourceMax() int32`

GetAbilityResourceMax returns the AbilityResourceMax field if non-nil, zero value otherwise.

### GetAbilityResourceMaxOk

`func (o *RawHeroStartingStatsV2) GetAbilityResourceMaxOk() (*int32, bool)`

GetAbilityResourceMaxOk returns a tuple with the AbilityResourceMax field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAbilityResourceMax

`func (o *RawHeroStartingStatsV2) SetAbilityResourceMax(v int32)`

SetAbilityResourceMax sets AbilityResourceMax field to given value.


### GetAbilityResourceRegenPerSecond

`func (o *RawHeroStartingStatsV2) GetAbilityResourceRegenPerSecond() int32`

GetAbilityResourceRegenPerSecond returns the AbilityResourceRegenPerSecond field if non-nil, zero value otherwise.

### GetAbilityResourceRegenPerSecondOk

`func (o *RawHeroStartingStatsV2) GetAbilityResourceRegenPerSecondOk() (*int32, bool)`

GetAbilityResourceRegenPerSecondOk returns a tuple with the AbilityResourceRegenPerSecond field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAbilityResourceRegenPerSecond

`func (o *RawHeroStartingStatsV2) SetAbilityResourceRegenPerSecond(v int32)`

SetAbilityResourceRegenPerSecond sets AbilityResourceRegenPerSecond field to given value.


### GetCritDamageReceivedScale

`func (o *RawHeroStartingStatsV2) GetCritDamageReceivedScale() float32`

GetCritDamageReceivedScale returns the CritDamageReceivedScale field if non-nil, zero value otherwise.

### GetCritDamageReceivedScaleOk

`func (o *RawHeroStartingStatsV2) GetCritDamageReceivedScaleOk() (*float32, bool)`

GetCritDamageReceivedScaleOk returns a tuple with the CritDamageReceivedScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCritDamageReceivedScale

`func (o *RawHeroStartingStatsV2) SetCritDamageReceivedScale(v float32)`

SetCritDamageReceivedScale sets CritDamageReceivedScale field to given value.


### GetTechDuration

`func (o *RawHeroStartingStatsV2) GetTechDuration() int32`

GetTechDuration returns the TechDuration field if non-nil, zero value otherwise.

### GetTechDurationOk

`func (o *RawHeroStartingStatsV2) GetTechDurationOk() (*int32, bool)`

GetTechDurationOk returns a tuple with the TechDuration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTechDuration

`func (o *RawHeroStartingStatsV2) SetTechDuration(v int32)`

SetTechDuration sets TechDuration field to given value.


### GetTechArmorDamageReduction

`func (o *RawHeroStartingStatsV2) GetTechArmorDamageReduction() float32`

GetTechArmorDamageReduction returns the TechArmorDamageReduction field if non-nil, zero value otherwise.

### GetTechArmorDamageReductionOk

`func (o *RawHeroStartingStatsV2) GetTechArmorDamageReductionOk() (*float32, bool)`

GetTechArmorDamageReductionOk returns a tuple with the TechArmorDamageReduction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTechArmorDamageReduction

`func (o *RawHeroStartingStatsV2) SetTechArmorDamageReduction(v float32)`

SetTechArmorDamageReduction sets TechArmorDamageReduction field to given value.

### HasTechArmorDamageReduction

`func (o *RawHeroStartingStatsV2) HasTechArmorDamageReduction() bool`

HasTechArmorDamageReduction returns a boolean if a field has been set.

### SetTechArmorDamageReductionNil

`func (o *RawHeroStartingStatsV2) SetTechArmorDamageReductionNil(b bool)`

 SetTechArmorDamageReductionNil sets the value for TechArmorDamageReduction to be an explicit nil

### UnsetTechArmorDamageReduction
`func (o *RawHeroStartingStatsV2) UnsetTechArmorDamageReduction()`

UnsetTechArmorDamageReduction ensures that no value is present for TechArmorDamageReduction, not even an explicit nil
### GetTechRange

`func (o *RawHeroStartingStatsV2) GetTechRange() int32`

GetTechRange returns the TechRange field if non-nil, zero value otherwise.

### GetTechRangeOk

`func (o *RawHeroStartingStatsV2) GetTechRangeOk() (*int32, bool)`

GetTechRangeOk returns a tuple with the TechRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTechRange

`func (o *RawHeroStartingStatsV2) SetTechRange(v int32)`

SetTechRange sets TechRange field to given value.


### GetBulletArmorDamageReduction

`func (o *RawHeroStartingStatsV2) GetBulletArmorDamageReduction() float32`

GetBulletArmorDamageReduction returns the BulletArmorDamageReduction field if non-nil, zero value otherwise.

### GetBulletArmorDamageReductionOk

`func (o *RawHeroStartingStatsV2) GetBulletArmorDamageReductionOk() (*float32, bool)`

GetBulletArmorDamageReductionOk returns a tuple with the BulletArmorDamageReduction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletArmorDamageReduction

`func (o *RawHeroStartingStatsV2) SetBulletArmorDamageReduction(v float32)`

SetBulletArmorDamageReduction sets BulletArmorDamageReduction field to given value.

### HasBulletArmorDamageReduction

`func (o *RawHeroStartingStatsV2) HasBulletArmorDamageReduction() bool`

HasBulletArmorDamageReduction returns a boolean if a field has been set.

### SetBulletArmorDamageReductionNil

`func (o *RawHeroStartingStatsV2) SetBulletArmorDamageReductionNil(b bool)`

 SetBulletArmorDamageReductionNil sets the value for BulletArmorDamageReduction to be an explicit nil

### UnsetBulletArmorDamageReduction
`func (o *RawHeroStartingStatsV2) UnsetBulletArmorDamageReduction()`

UnsetBulletArmorDamageReduction ensures that no value is present for BulletArmorDamageReduction, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


