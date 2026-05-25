# StartingStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AbilityResourceMax** | [**StartingStat**](StartingStat.md) |  | 
**AbilityResourceRegenPerSecond** | [**StartingStat**](StartingStat.md) |  | 
**BaseHealthRegen** | [**StartingStat**](StartingStat.md) |  | 
**BulletArmorDamageReduction** | Pointer to [**NullableStartingStat**](StartingStat.md) |  | [optional] 
**CritDamageReceivedScale** | [**StartingStat**](StartingStat.md) |  | 
**CrouchSpeed** | [**StartingStat**](StartingStat.md) |  | 
**HeavyMeleeDamage** | [**StartingStat**](StartingStat.md) |  | 
**LightMeleeDamage** | [**StartingStat**](StartingStat.md) |  | 
**MaxHealth** | [**StartingStat**](StartingStat.md) |  | 
**MaxMoveSpeed** | [**StartingStat**](StartingStat.md) |  | 
**MoveAcceleration** | [**StartingStat**](StartingStat.md) |  | 
**ProcBuildUpRateScale** | [**StartingStat**](StartingStat.md) |  | 
**ReloadSpeed** | [**StartingStat**](StartingStat.md) |  | 
**SprintSpeed** | [**StartingStat**](StartingStat.md) |  | 
**Stamina** | [**StartingStat**](StartingStat.md) |  | 
**StaminaRegenPerSecond** | [**StartingStat**](StartingStat.md) |  | 
**TechArmorDamageReduction** | Pointer to [**NullableStartingStat**](StartingStat.md) |  | [optional] 
**TechDuration** | [**StartingStat**](StartingStat.md) |  | 
**TechRange** | [**StartingStat**](StartingStat.md) |  | 
**WeaponPower** | [**StartingStat**](StartingStat.md) |  | 
**WeaponPowerScale** | [**StartingStat**](StartingStat.md) |  | 

## Methods

### NewStartingStats

`func NewStartingStats(abilityResourceMax StartingStat, abilityResourceRegenPerSecond StartingStat, baseHealthRegen StartingStat, critDamageReceivedScale StartingStat, crouchSpeed StartingStat, heavyMeleeDamage StartingStat, lightMeleeDamage StartingStat, maxHealth StartingStat, maxMoveSpeed StartingStat, moveAcceleration StartingStat, procBuildUpRateScale StartingStat, reloadSpeed StartingStat, sprintSpeed StartingStat, stamina StartingStat, staminaRegenPerSecond StartingStat, techDuration StartingStat, techRange StartingStat, weaponPower StartingStat, weaponPowerScale StartingStat, ) *StartingStats`

NewStartingStats instantiates a new StartingStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStartingStatsWithDefaults

`func NewStartingStatsWithDefaults() *StartingStats`

NewStartingStatsWithDefaults instantiates a new StartingStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAbilityResourceMax

`func (o *StartingStats) GetAbilityResourceMax() StartingStat`

GetAbilityResourceMax returns the AbilityResourceMax field if non-nil, zero value otherwise.

### GetAbilityResourceMaxOk

`func (o *StartingStats) GetAbilityResourceMaxOk() (*StartingStat, bool)`

GetAbilityResourceMaxOk returns a tuple with the AbilityResourceMax field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAbilityResourceMax

`func (o *StartingStats) SetAbilityResourceMax(v StartingStat)`

SetAbilityResourceMax sets AbilityResourceMax field to given value.


### GetAbilityResourceRegenPerSecond

`func (o *StartingStats) GetAbilityResourceRegenPerSecond() StartingStat`

GetAbilityResourceRegenPerSecond returns the AbilityResourceRegenPerSecond field if non-nil, zero value otherwise.

### GetAbilityResourceRegenPerSecondOk

`func (o *StartingStats) GetAbilityResourceRegenPerSecondOk() (*StartingStat, bool)`

GetAbilityResourceRegenPerSecondOk returns a tuple with the AbilityResourceRegenPerSecond field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAbilityResourceRegenPerSecond

`func (o *StartingStats) SetAbilityResourceRegenPerSecond(v StartingStat)`

SetAbilityResourceRegenPerSecond sets AbilityResourceRegenPerSecond field to given value.


### GetBaseHealthRegen

`func (o *StartingStats) GetBaseHealthRegen() StartingStat`

GetBaseHealthRegen returns the BaseHealthRegen field if non-nil, zero value otherwise.

### GetBaseHealthRegenOk

`func (o *StartingStats) GetBaseHealthRegenOk() (*StartingStat, bool)`

GetBaseHealthRegenOk returns a tuple with the BaseHealthRegen field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaseHealthRegen

`func (o *StartingStats) SetBaseHealthRegen(v StartingStat)`

SetBaseHealthRegen sets BaseHealthRegen field to given value.


### GetBulletArmorDamageReduction

`func (o *StartingStats) GetBulletArmorDamageReduction() StartingStat`

GetBulletArmorDamageReduction returns the BulletArmorDamageReduction field if non-nil, zero value otherwise.

### GetBulletArmorDamageReductionOk

`func (o *StartingStats) GetBulletArmorDamageReductionOk() (*StartingStat, bool)`

GetBulletArmorDamageReductionOk returns a tuple with the BulletArmorDamageReduction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletArmorDamageReduction

`func (o *StartingStats) SetBulletArmorDamageReduction(v StartingStat)`

SetBulletArmorDamageReduction sets BulletArmorDamageReduction field to given value.

### HasBulletArmorDamageReduction

`func (o *StartingStats) HasBulletArmorDamageReduction() bool`

HasBulletArmorDamageReduction returns a boolean if a field has been set.

### SetBulletArmorDamageReductionNil

`func (o *StartingStats) SetBulletArmorDamageReductionNil(b bool)`

 SetBulletArmorDamageReductionNil sets the value for BulletArmorDamageReduction to be an explicit nil

### UnsetBulletArmorDamageReduction
`func (o *StartingStats) UnsetBulletArmorDamageReduction()`

UnsetBulletArmorDamageReduction ensures that no value is present for BulletArmorDamageReduction, not even an explicit nil
### GetCritDamageReceivedScale

`func (o *StartingStats) GetCritDamageReceivedScale() StartingStat`

GetCritDamageReceivedScale returns the CritDamageReceivedScale field if non-nil, zero value otherwise.

### GetCritDamageReceivedScaleOk

`func (o *StartingStats) GetCritDamageReceivedScaleOk() (*StartingStat, bool)`

GetCritDamageReceivedScaleOk returns a tuple with the CritDamageReceivedScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCritDamageReceivedScale

`func (o *StartingStats) SetCritDamageReceivedScale(v StartingStat)`

SetCritDamageReceivedScale sets CritDamageReceivedScale field to given value.


### GetCrouchSpeed

`func (o *StartingStats) GetCrouchSpeed() StartingStat`

GetCrouchSpeed returns the CrouchSpeed field if non-nil, zero value otherwise.

### GetCrouchSpeedOk

`func (o *StartingStats) GetCrouchSpeedOk() (*StartingStat, bool)`

GetCrouchSpeedOk returns a tuple with the CrouchSpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrouchSpeed

`func (o *StartingStats) SetCrouchSpeed(v StartingStat)`

SetCrouchSpeed sets CrouchSpeed field to given value.


### GetHeavyMeleeDamage

`func (o *StartingStats) GetHeavyMeleeDamage() StartingStat`

GetHeavyMeleeDamage returns the HeavyMeleeDamage field if non-nil, zero value otherwise.

### GetHeavyMeleeDamageOk

`func (o *StartingStats) GetHeavyMeleeDamageOk() (*StartingStat, bool)`

GetHeavyMeleeDamageOk returns a tuple with the HeavyMeleeDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeavyMeleeDamage

`func (o *StartingStats) SetHeavyMeleeDamage(v StartingStat)`

SetHeavyMeleeDamage sets HeavyMeleeDamage field to given value.


### GetLightMeleeDamage

`func (o *StartingStats) GetLightMeleeDamage() StartingStat`

GetLightMeleeDamage returns the LightMeleeDamage field if non-nil, zero value otherwise.

### GetLightMeleeDamageOk

`func (o *StartingStats) GetLightMeleeDamageOk() (*StartingStat, bool)`

GetLightMeleeDamageOk returns a tuple with the LightMeleeDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLightMeleeDamage

`func (o *StartingStats) SetLightMeleeDamage(v StartingStat)`

SetLightMeleeDamage sets LightMeleeDamage field to given value.


### GetMaxHealth

`func (o *StartingStats) GetMaxHealth() StartingStat`

GetMaxHealth returns the MaxHealth field if non-nil, zero value otherwise.

### GetMaxHealthOk

`func (o *StartingStats) GetMaxHealthOk() (*StartingStat, bool)`

GetMaxHealthOk returns a tuple with the MaxHealth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxHealth

`func (o *StartingStats) SetMaxHealth(v StartingStat)`

SetMaxHealth sets MaxHealth field to given value.


### GetMaxMoveSpeed

`func (o *StartingStats) GetMaxMoveSpeed() StartingStat`

GetMaxMoveSpeed returns the MaxMoveSpeed field if non-nil, zero value otherwise.

### GetMaxMoveSpeedOk

`func (o *StartingStats) GetMaxMoveSpeedOk() (*StartingStat, bool)`

GetMaxMoveSpeedOk returns a tuple with the MaxMoveSpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxMoveSpeed

`func (o *StartingStats) SetMaxMoveSpeed(v StartingStat)`

SetMaxMoveSpeed sets MaxMoveSpeed field to given value.


### GetMoveAcceleration

`func (o *StartingStats) GetMoveAcceleration() StartingStat`

GetMoveAcceleration returns the MoveAcceleration field if non-nil, zero value otherwise.

### GetMoveAccelerationOk

`func (o *StartingStats) GetMoveAccelerationOk() (*StartingStat, bool)`

GetMoveAccelerationOk returns a tuple with the MoveAcceleration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMoveAcceleration

`func (o *StartingStats) SetMoveAcceleration(v StartingStat)`

SetMoveAcceleration sets MoveAcceleration field to given value.


### GetProcBuildUpRateScale

`func (o *StartingStats) GetProcBuildUpRateScale() StartingStat`

GetProcBuildUpRateScale returns the ProcBuildUpRateScale field if non-nil, zero value otherwise.

### GetProcBuildUpRateScaleOk

`func (o *StartingStats) GetProcBuildUpRateScaleOk() (*StartingStat, bool)`

GetProcBuildUpRateScaleOk returns a tuple with the ProcBuildUpRateScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProcBuildUpRateScale

`func (o *StartingStats) SetProcBuildUpRateScale(v StartingStat)`

SetProcBuildUpRateScale sets ProcBuildUpRateScale field to given value.


### GetReloadSpeed

`func (o *StartingStats) GetReloadSpeed() StartingStat`

GetReloadSpeed returns the ReloadSpeed field if non-nil, zero value otherwise.

### GetReloadSpeedOk

`func (o *StartingStats) GetReloadSpeedOk() (*StartingStat, bool)`

GetReloadSpeedOk returns a tuple with the ReloadSpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReloadSpeed

`func (o *StartingStats) SetReloadSpeed(v StartingStat)`

SetReloadSpeed sets ReloadSpeed field to given value.


### GetSprintSpeed

`func (o *StartingStats) GetSprintSpeed() StartingStat`

GetSprintSpeed returns the SprintSpeed field if non-nil, zero value otherwise.

### GetSprintSpeedOk

`func (o *StartingStats) GetSprintSpeedOk() (*StartingStat, bool)`

GetSprintSpeedOk returns a tuple with the SprintSpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSprintSpeed

`func (o *StartingStats) SetSprintSpeed(v StartingStat)`

SetSprintSpeed sets SprintSpeed field to given value.


### GetStamina

`func (o *StartingStats) GetStamina() StartingStat`

GetStamina returns the Stamina field if non-nil, zero value otherwise.

### GetStaminaOk

`func (o *StartingStats) GetStaminaOk() (*StartingStat, bool)`

GetStaminaOk returns a tuple with the Stamina field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStamina

`func (o *StartingStats) SetStamina(v StartingStat)`

SetStamina sets Stamina field to given value.


### GetStaminaRegenPerSecond

`func (o *StartingStats) GetStaminaRegenPerSecond() StartingStat`

GetStaminaRegenPerSecond returns the StaminaRegenPerSecond field if non-nil, zero value otherwise.

### GetStaminaRegenPerSecondOk

`func (o *StartingStats) GetStaminaRegenPerSecondOk() (*StartingStat, bool)`

GetStaminaRegenPerSecondOk returns a tuple with the StaminaRegenPerSecond field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStaminaRegenPerSecond

`func (o *StartingStats) SetStaminaRegenPerSecond(v StartingStat)`

SetStaminaRegenPerSecond sets StaminaRegenPerSecond field to given value.


### GetTechArmorDamageReduction

`func (o *StartingStats) GetTechArmorDamageReduction() StartingStat`

GetTechArmorDamageReduction returns the TechArmorDamageReduction field if non-nil, zero value otherwise.

### GetTechArmorDamageReductionOk

`func (o *StartingStats) GetTechArmorDamageReductionOk() (*StartingStat, bool)`

GetTechArmorDamageReductionOk returns a tuple with the TechArmorDamageReduction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTechArmorDamageReduction

`func (o *StartingStats) SetTechArmorDamageReduction(v StartingStat)`

SetTechArmorDamageReduction sets TechArmorDamageReduction field to given value.

### HasTechArmorDamageReduction

`func (o *StartingStats) HasTechArmorDamageReduction() bool`

HasTechArmorDamageReduction returns a boolean if a field has been set.

### SetTechArmorDamageReductionNil

`func (o *StartingStats) SetTechArmorDamageReductionNil(b bool)`

 SetTechArmorDamageReductionNil sets the value for TechArmorDamageReduction to be an explicit nil

### UnsetTechArmorDamageReduction
`func (o *StartingStats) UnsetTechArmorDamageReduction()`

UnsetTechArmorDamageReduction ensures that no value is present for TechArmorDamageReduction, not even an explicit nil
### GetTechDuration

`func (o *StartingStats) GetTechDuration() StartingStat`

GetTechDuration returns the TechDuration field if non-nil, zero value otherwise.

### GetTechDurationOk

`func (o *StartingStats) GetTechDurationOk() (*StartingStat, bool)`

GetTechDurationOk returns a tuple with the TechDuration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTechDuration

`func (o *StartingStats) SetTechDuration(v StartingStat)`

SetTechDuration sets TechDuration field to given value.


### GetTechRange

`func (o *StartingStats) GetTechRange() StartingStat`

GetTechRange returns the TechRange field if non-nil, zero value otherwise.

### GetTechRangeOk

`func (o *StartingStats) GetTechRangeOk() (*StartingStat, bool)`

GetTechRangeOk returns a tuple with the TechRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTechRange

`func (o *StartingStats) SetTechRange(v StartingStat)`

SetTechRange sets TechRange field to given value.


### GetWeaponPower

`func (o *StartingStats) GetWeaponPower() StartingStat`

GetWeaponPower returns the WeaponPower field if non-nil, zero value otherwise.

### GetWeaponPowerOk

`func (o *StartingStats) GetWeaponPowerOk() (*StartingStat, bool)`

GetWeaponPowerOk returns a tuple with the WeaponPower field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponPower

`func (o *StartingStats) SetWeaponPower(v StartingStat)`

SetWeaponPower sets WeaponPower field to given value.


### GetWeaponPowerScale

`func (o *StartingStats) GetWeaponPowerScale() StartingStat`

GetWeaponPowerScale returns the WeaponPowerScale field if non-nil, zero value otherwise.

### GetWeaponPowerScaleOk

`func (o *StartingStats) GetWeaponPowerScaleOk() (*StartingStat, bool)`

GetWeaponPowerScaleOk returns a tuple with the WeaponPowerScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponPowerScale

`func (o *StartingStats) SetWeaponPowerScale(v StartingStat)`

SetWeaponPowerScale sets WeaponPowerScale field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


