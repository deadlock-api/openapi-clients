# MiscV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClassName** | **string** |  | 
**Color** | Pointer to [**NullableColor**](Color.md) |  | [optional] 
**InitialSpawnTime** | Pointer to **NullableFloat32** |  | [optional] 
**RespawnTime** | Pointer to **NullableFloat32** |  | [optional] 
**SpawnInterval** | Pointer to **NullableFloat32** |  | [optional] 
**InitialSpawnDelayInSeconds** | Pointer to **NullableInt32** |  | [optional] 
**SpawnIntervalInSeconds** | Pointer to **NullableInt32** |  | [optional] 
**MatchTimeMinsForLevel2Pickups** | Pointer to **NullableInt32** |  | [optional] 
**MatchTimeMinsForLevel3Pickups** | Pointer to **NullableInt32** |  | [optional] 
**LootListDeckSize** | Pointer to **NullableInt32** |  | [optional] 
**InitialSpawnDelaySeconds** | Pointer to **NullableInt32** |  | [optional] 
**Health** | Pointer to **NullableInt32** |  | [optional] 
**BreakOnDodgeTouch** | Pointer to **NullableBool** |  | [optional] 
**SolidAfterDeath** | Pointer to **NullableBool** |  | [optional] 
**RenderAfterDeath** | Pointer to **NullableBool** |  | [optional] 
**DamagedByAbilities** | Pointer to **NullableBool** |  | [optional] 
**DamagedByMelee** | Pointer to **NullableBool** |  | [optional] 
**DamagedByBullets** | Pointer to **NullableBool** |  | [optional] 
**IsMantleable** | Pointer to **NullableBool** |  | [optional] 
**PrimaryDropChance** | Pointer to **NullableFloat32** |  | [optional] 
**PrimaryPickups** | Pointer to [**[]PickupDefinition**](PickupDefinition.md) |  | [optional] 
**MVecPickupsLv2** | Pointer to [**[]PickupDefinition**](PickupDefinition.md) |  | [optional] 
**MVecPickupsLv3** | Pointer to [**[]PickupDefinition**](PickupDefinition.md) |  | [optional] 
**RollType** | Pointer to **NullableString** |  | [optional] 
**GoldAmount** | Pointer to **NullableFloat32** |  | [optional] 
**GoldPerMinuteAmount** | Pointer to **NullableFloat32** |  | [optional] 
**Modifier** | Pointer to [**NullableSubclassModifierDefinition**](SubclassModifierDefinition.md) |  | [optional] 
**PickupRadius** | Pointer to **NullableFloat32** |  | [optional] 
**ExpirationDuration** | Pointer to **NullableFloat32** |  | [optional] 
**ShowOnMinimap** | Pointer to **NullableBool** |  | [optional] 
**OrbSpawnDelayMin** | Pointer to **NullableFloat32** |  | [optional] 
**OrbSpawnDelayMax** | Pointer to **NullableFloat32** |  | [optional] 
**Lifetime** | Pointer to **NullableFloat32** |  | [optional] 
**CollisionRadius** | Pointer to **NullableFloat32** |  | [optional] 
**Id** | **int32** |  | [readonly] 

## Methods

### NewMiscV2

`func NewMiscV2(className string, id int32, ) *MiscV2`

NewMiscV2 instantiates a new MiscV2 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMiscV2WithDefaults

`func NewMiscV2WithDefaults() *MiscV2`

NewMiscV2WithDefaults instantiates a new MiscV2 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClassName

`func (o *MiscV2) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *MiscV2) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *MiscV2) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetColor

`func (o *MiscV2) GetColor() Color`

GetColor returns the Color field if non-nil, zero value otherwise.

### GetColorOk

`func (o *MiscV2) GetColorOk() (*Color, bool)`

GetColorOk returns a tuple with the Color field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColor

`func (o *MiscV2) SetColor(v Color)`

SetColor sets Color field to given value.

### HasColor

`func (o *MiscV2) HasColor() bool`

HasColor returns a boolean if a field has been set.

### SetColorNil

`func (o *MiscV2) SetColorNil(b bool)`

 SetColorNil sets the value for Color to be an explicit nil

### UnsetColor
`func (o *MiscV2) UnsetColor()`

UnsetColor ensures that no value is present for Color, not even an explicit nil
### GetInitialSpawnTime

`func (o *MiscV2) GetInitialSpawnTime() float32`

GetInitialSpawnTime returns the InitialSpawnTime field if non-nil, zero value otherwise.

### GetInitialSpawnTimeOk

`func (o *MiscV2) GetInitialSpawnTimeOk() (*float32, bool)`

GetInitialSpawnTimeOk returns a tuple with the InitialSpawnTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInitialSpawnTime

`func (o *MiscV2) SetInitialSpawnTime(v float32)`

SetInitialSpawnTime sets InitialSpawnTime field to given value.

### HasInitialSpawnTime

`func (o *MiscV2) HasInitialSpawnTime() bool`

HasInitialSpawnTime returns a boolean if a field has been set.

### SetInitialSpawnTimeNil

`func (o *MiscV2) SetInitialSpawnTimeNil(b bool)`

 SetInitialSpawnTimeNil sets the value for InitialSpawnTime to be an explicit nil

### UnsetInitialSpawnTime
`func (o *MiscV2) UnsetInitialSpawnTime()`

UnsetInitialSpawnTime ensures that no value is present for InitialSpawnTime, not even an explicit nil
### GetRespawnTime

`func (o *MiscV2) GetRespawnTime() float32`

GetRespawnTime returns the RespawnTime field if non-nil, zero value otherwise.

### GetRespawnTimeOk

`func (o *MiscV2) GetRespawnTimeOk() (*float32, bool)`

GetRespawnTimeOk returns a tuple with the RespawnTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRespawnTime

`func (o *MiscV2) SetRespawnTime(v float32)`

SetRespawnTime sets RespawnTime field to given value.

### HasRespawnTime

`func (o *MiscV2) HasRespawnTime() bool`

HasRespawnTime returns a boolean if a field has been set.

### SetRespawnTimeNil

`func (o *MiscV2) SetRespawnTimeNil(b bool)`

 SetRespawnTimeNil sets the value for RespawnTime to be an explicit nil

### UnsetRespawnTime
`func (o *MiscV2) UnsetRespawnTime()`

UnsetRespawnTime ensures that no value is present for RespawnTime, not even an explicit nil
### GetSpawnInterval

`func (o *MiscV2) GetSpawnInterval() float32`

GetSpawnInterval returns the SpawnInterval field if non-nil, zero value otherwise.

### GetSpawnIntervalOk

`func (o *MiscV2) GetSpawnIntervalOk() (*float32, bool)`

GetSpawnIntervalOk returns a tuple with the SpawnInterval field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpawnInterval

`func (o *MiscV2) SetSpawnInterval(v float32)`

SetSpawnInterval sets SpawnInterval field to given value.

### HasSpawnInterval

`func (o *MiscV2) HasSpawnInterval() bool`

HasSpawnInterval returns a boolean if a field has been set.

### SetSpawnIntervalNil

`func (o *MiscV2) SetSpawnIntervalNil(b bool)`

 SetSpawnIntervalNil sets the value for SpawnInterval to be an explicit nil

### UnsetSpawnInterval
`func (o *MiscV2) UnsetSpawnInterval()`

UnsetSpawnInterval ensures that no value is present for SpawnInterval, not even an explicit nil
### GetInitialSpawnDelayInSeconds

`func (o *MiscV2) GetInitialSpawnDelayInSeconds() int32`

GetInitialSpawnDelayInSeconds returns the InitialSpawnDelayInSeconds field if non-nil, zero value otherwise.

### GetInitialSpawnDelayInSecondsOk

`func (o *MiscV2) GetInitialSpawnDelayInSecondsOk() (*int32, bool)`

GetInitialSpawnDelayInSecondsOk returns a tuple with the InitialSpawnDelayInSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInitialSpawnDelayInSeconds

`func (o *MiscV2) SetInitialSpawnDelayInSeconds(v int32)`

SetInitialSpawnDelayInSeconds sets InitialSpawnDelayInSeconds field to given value.

### HasInitialSpawnDelayInSeconds

`func (o *MiscV2) HasInitialSpawnDelayInSeconds() bool`

HasInitialSpawnDelayInSeconds returns a boolean if a field has been set.

### SetInitialSpawnDelayInSecondsNil

`func (o *MiscV2) SetInitialSpawnDelayInSecondsNil(b bool)`

 SetInitialSpawnDelayInSecondsNil sets the value for InitialSpawnDelayInSeconds to be an explicit nil

### UnsetInitialSpawnDelayInSeconds
`func (o *MiscV2) UnsetInitialSpawnDelayInSeconds()`

UnsetInitialSpawnDelayInSeconds ensures that no value is present for InitialSpawnDelayInSeconds, not even an explicit nil
### GetSpawnIntervalInSeconds

`func (o *MiscV2) GetSpawnIntervalInSeconds() int32`

GetSpawnIntervalInSeconds returns the SpawnIntervalInSeconds field if non-nil, zero value otherwise.

### GetSpawnIntervalInSecondsOk

`func (o *MiscV2) GetSpawnIntervalInSecondsOk() (*int32, bool)`

GetSpawnIntervalInSecondsOk returns a tuple with the SpawnIntervalInSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpawnIntervalInSeconds

`func (o *MiscV2) SetSpawnIntervalInSeconds(v int32)`

SetSpawnIntervalInSeconds sets SpawnIntervalInSeconds field to given value.

### HasSpawnIntervalInSeconds

`func (o *MiscV2) HasSpawnIntervalInSeconds() bool`

HasSpawnIntervalInSeconds returns a boolean if a field has been set.

### SetSpawnIntervalInSecondsNil

`func (o *MiscV2) SetSpawnIntervalInSecondsNil(b bool)`

 SetSpawnIntervalInSecondsNil sets the value for SpawnIntervalInSeconds to be an explicit nil

### UnsetSpawnIntervalInSeconds
`func (o *MiscV2) UnsetSpawnIntervalInSeconds()`

UnsetSpawnIntervalInSeconds ensures that no value is present for SpawnIntervalInSeconds, not even an explicit nil
### GetMatchTimeMinsForLevel2Pickups

`func (o *MiscV2) GetMatchTimeMinsForLevel2Pickups() int32`

GetMatchTimeMinsForLevel2Pickups returns the MatchTimeMinsForLevel2Pickups field if non-nil, zero value otherwise.

### GetMatchTimeMinsForLevel2PickupsOk

`func (o *MiscV2) GetMatchTimeMinsForLevel2PickupsOk() (*int32, bool)`

GetMatchTimeMinsForLevel2PickupsOk returns a tuple with the MatchTimeMinsForLevel2Pickups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchTimeMinsForLevel2Pickups

`func (o *MiscV2) SetMatchTimeMinsForLevel2Pickups(v int32)`

SetMatchTimeMinsForLevel2Pickups sets MatchTimeMinsForLevel2Pickups field to given value.

### HasMatchTimeMinsForLevel2Pickups

`func (o *MiscV2) HasMatchTimeMinsForLevel2Pickups() bool`

HasMatchTimeMinsForLevel2Pickups returns a boolean if a field has been set.

### SetMatchTimeMinsForLevel2PickupsNil

`func (o *MiscV2) SetMatchTimeMinsForLevel2PickupsNil(b bool)`

 SetMatchTimeMinsForLevel2PickupsNil sets the value for MatchTimeMinsForLevel2Pickups to be an explicit nil

### UnsetMatchTimeMinsForLevel2Pickups
`func (o *MiscV2) UnsetMatchTimeMinsForLevel2Pickups()`

UnsetMatchTimeMinsForLevel2Pickups ensures that no value is present for MatchTimeMinsForLevel2Pickups, not even an explicit nil
### GetMatchTimeMinsForLevel3Pickups

`func (o *MiscV2) GetMatchTimeMinsForLevel3Pickups() int32`

GetMatchTimeMinsForLevel3Pickups returns the MatchTimeMinsForLevel3Pickups field if non-nil, zero value otherwise.

### GetMatchTimeMinsForLevel3PickupsOk

`func (o *MiscV2) GetMatchTimeMinsForLevel3PickupsOk() (*int32, bool)`

GetMatchTimeMinsForLevel3PickupsOk returns a tuple with the MatchTimeMinsForLevel3Pickups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchTimeMinsForLevel3Pickups

`func (o *MiscV2) SetMatchTimeMinsForLevel3Pickups(v int32)`

SetMatchTimeMinsForLevel3Pickups sets MatchTimeMinsForLevel3Pickups field to given value.

### HasMatchTimeMinsForLevel3Pickups

`func (o *MiscV2) HasMatchTimeMinsForLevel3Pickups() bool`

HasMatchTimeMinsForLevel3Pickups returns a boolean if a field has been set.

### SetMatchTimeMinsForLevel3PickupsNil

`func (o *MiscV2) SetMatchTimeMinsForLevel3PickupsNil(b bool)`

 SetMatchTimeMinsForLevel3PickupsNil sets the value for MatchTimeMinsForLevel3Pickups to be an explicit nil

### UnsetMatchTimeMinsForLevel3Pickups
`func (o *MiscV2) UnsetMatchTimeMinsForLevel3Pickups()`

UnsetMatchTimeMinsForLevel3Pickups ensures that no value is present for MatchTimeMinsForLevel3Pickups, not even an explicit nil
### GetLootListDeckSize

`func (o *MiscV2) GetLootListDeckSize() int32`

GetLootListDeckSize returns the LootListDeckSize field if non-nil, zero value otherwise.

### GetLootListDeckSizeOk

`func (o *MiscV2) GetLootListDeckSizeOk() (*int32, bool)`

GetLootListDeckSizeOk returns a tuple with the LootListDeckSize field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLootListDeckSize

`func (o *MiscV2) SetLootListDeckSize(v int32)`

SetLootListDeckSize sets LootListDeckSize field to given value.

### HasLootListDeckSize

`func (o *MiscV2) HasLootListDeckSize() bool`

HasLootListDeckSize returns a boolean if a field has been set.

### SetLootListDeckSizeNil

`func (o *MiscV2) SetLootListDeckSizeNil(b bool)`

 SetLootListDeckSizeNil sets the value for LootListDeckSize to be an explicit nil

### UnsetLootListDeckSize
`func (o *MiscV2) UnsetLootListDeckSize()`

UnsetLootListDeckSize ensures that no value is present for LootListDeckSize, not even an explicit nil
### GetInitialSpawnDelaySeconds

`func (o *MiscV2) GetInitialSpawnDelaySeconds() int32`

GetInitialSpawnDelaySeconds returns the InitialSpawnDelaySeconds field if non-nil, zero value otherwise.

### GetInitialSpawnDelaySecondsOk

`func (o *MiscV2) GetInitialSpawnDelaySecondsOk() (*int32, bool)`

GetInitialSpawnDelaySecondsOk returns a tuple with the InitialSpawnDelaySeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInitialSpawnDelaySeconds

`func (o *MiscV2) SetInitialSpawnDelaySeconds(v int32)`

SetInitialSpawnDelaySeconds sets InitialSpawnDelaySeconds field to given value.

### HasInitialSpawnDelaySeconds

`func (o *MiscV2) HasInitialSpawnDelaySeconds() bool`

HasInitialSpawnDelaySeconds returns a boolean if a field has been set.

### SetInitialSpawnDelaySecondsNil

`func (o *MiscV2) SetInitialSpawnDelaySecondsNil(b bool)`

 SetInitialSpawnDelaySecondsNil sets the value for InitialSpawnDelaySeconds to be an explicit nil

### UnsetInitialSpawnDelaySeconds
`func (o *MiscV2) UnsetInitialSpawnDelaySeconds()`

UnsetInitialSpawnDelaySeconds ensures that no value is present for InitialSpawnDelaySeconds, not even an explicit nil
### GetHealth

`func (o *MiscV2) GetHealth() int32`

GetHealth returns the Health field if non-nil, zero value otherwise.

### GetHealthOk

`func (o *MiscV2) GetHealthOk() (*int32, bool)`

GetHealthOk returns a tuple with the Health field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHealth

`func (o *MiscV2) SetHealth(v int32)`

SetHealth sets Health field to given value.

### HasHealth

`func (o *MiscV2) HasHealth() bool`

HasHealth returns a boolean if a field has been set.

### SetHealthNil

`func (o *MiscV2) SetHealthNil(b bool)`

 SetHealthNil sets the value for Health to be an explicit nil

### UnsetHealth
`func (o *MiscV2) UnsetHealth()`

UnsetHealth ensures that no value is present for Health, not even an explicit nil
### GetBreakOnDodgeTouch

`func (o *MiscV2) GetBreakOnDodgeTouch() bool`

GetBreakOnDodgeTouch returns the BreakOnDodgeTouch field if non-nil, zero value otherwise.

### GetBreakOnDodgeTouchOk

`func (o *MiscV2) GetBreakOnDodgeTouchOk() (*bool, bool)`

GetBreakOnDodgeTouchOk returns a tuple with the BreakOnDodgeTouch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBreakOnDodgeTouch

`func (o *MiscV2) SetBreakOnDodgeTouch(v bool)`

SetBreakOnDodgeTouch sets BreakOnDodgeTouch field to given value.

### HasBreakOnDodgeTouch

`func (o *MiscV2) HasBreakOnDodgeTouch() bool`

HasBreakOnDodgeTouch returns a boolean if a field has been set.

### SetBreakOnDodgeTouchNil

`func (o *MiscV2) SetBreakOnDodgeTouchNil(b bool)`

 SetBreakOnDodgeTouchNil sets the value for BreakOnDodgeTouch to be an explicit nil

### UnsetBreakOnDodgeTouch
`func (o *MiscV2) UnsetBreakOnDodgeTouch()`

UnsetBreakOnDodgeTouch ensures that no value is present for BreakOnDodgeTouch, not even an explicit nil
### GetSolidAfterDeath

`func (o *MiscV2) GetSolidAfterDeath() bool`

GetSolidAfterDeath returns the SolidAfterDeath field if non-nil, zero value otherwise.

### GetSolidAfterDeathOk

`func (o *MiscV2) GetSolidAfterDeathOk() (*bool, bool)`

GetSolidAfterDeathOk returns a tuple with the SolidAfterDeath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSolidAfterDeath

`func (o *MiscV2) SetSolidAfterDeath(v bool)`

SetSolidAfterDeath sets SolidAfterDeath field to given value.

### HasSolidAfterDeath

`func (o *MiscV2) HasSolidAfterDeath() bool`

HasSolidAfterDeath returns a boolean if a field has been set.

### SetSolidAfterDeathNil

`func (o *MiscV2) SetSolidAfterDeathNil(b bool)`

 SetSolidAfterDeathNil sets the value for SolidAfterDeath to be an explicit nil

### UnsetSolidAfterDeath
`func (o *MiscV2) UnsetSolidAfterDeath()`

UnsetSolidAfterDeath ensures that no value is present for SolidAfterDeath, not even an explicit nil
### GetRenderAfterDeath

`func (o *MiscV2) GetRenderAfterDeath() bool`

GetRenderAfterDeath returns the RenderAfterDeath field if non-nil, zero value otherwise.

### GetRenderAfterDeathOk

`func (o *MiscV2) GetRenderAfterDeathOk() (*bool, bool)`

GetRenderAfterDeathOk returns a tuple with the RenderAfterDeath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRenderAfterDeath

`func (o *MiscV2) SetRenderAfterDeath(v bool)`

SetRenderAfterDeath sets RenderAfterDeath field to given value.

### HasRenderAfterDeath

`func (o *MiscV2) HasRenderAfterDeath() bool`

HasRenderAfterDeath returns a boolean if a field has been set.

### SetRenderAfterDeathNil

`func (o *MiscV2) SetRenderAfterDeathNil(b bool)`

 SetRenderAfterDeathNil sets the value for RenderAfterDeath to be an explicit nil

### UnsetRenderAfterDeath
`func (o *MiscV2) UnsetRenderAfterDeath()`

UnsetRenderAfterDeath ensures that no value is present for RenderAfterDeath, not even an explicit nil
### GetDamagedByAbilities

`func (o *MiscV2) GetDamagedByAbilities() bool`

GetDamagedByAbilities returns the DamagedByAbilities field if non-nil, zero value otherwise.

### GetDamagedByAbilitiesOk

`func (o *MiscV2) GetDamagedByAbilitiesOk() (*bool, bool)`

GetDamagedByAbilitiesOk returns a tuple with the DamagedByAbilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamagedByAbilities

`func (o *MiscV2) SetDamagedByAbilities(v bool)`

SetDamagedByAbilities sets DamagedByAbilities field to given value.

### HasDamagedByAbilities

`func (o *MiscV2) HasDamagedByAbilities() bool`

HasDamagedByAbilities returns a boolean if a field has been set.

### SetDamagedByAbilitiesNil

`func (o *MiscV2) SetDamagedByAbilitiesNil(b bool)`

 SetDamagedByAbilitiesNil sets the value for DamagedByAbilities to be an explicit nil

### UnsetDamagedByAbilities
`func (o *MiscV2) UnsetDamagedByAbilities()`

UnsetDamagedByAbilities ensures that no value is present for DamagedByAbilities, not even an explicit nil
### GetDamagedByMelee

`func (o *MiscV2) GetDamagedByMelee() bool`

GetDamagedByMelee returns the DamagedByMelee field if non-nil, zero value otherwise.

### GetDamagedByMeleeOk

`func (o *MiscV2) GetDamagedByMeleeOk() (*bool, bool)`

GetDamagedByMeleeOk returns a tuple with the DamagedByMelee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamagedByMelee

`func (o *MiscV2) SetDamagedByMelee(v bool)`

SetDamagedByMelee sets DamagedByMelee field to given value.

### HasDamagedByMelee

`func (o *MiscV2) HasDamagedByMelee() bool`

HasDamagedByMelee returns a boolean if a field has been set.

### SetDamagedByMeleeNil

`func (o *MiscV2) SetDamagedByMeleeNil(b bool)`

 SetDamagedByMeleeNil sets the value for DamagedByMelee to be an explicit nil

### UnsetDamagedByMelee
`func (o *MiscV2) UnsetDamagedByMelee()`

UnsetDamagedByMelee ensures that no value is present for DamagedByMelee, not even an explicit nil
### GetDamagedByBullets

`func (o *MiscV2) GetDamagedByBullets() bool`

GetDamagedByBullets returns the DamagedByBullets field if non-nil, zero value otherwise.

### GetDamagedByBulletsOk

`func (o *MiscV2) GetDamagedByBulletsOk() (*bool, bool)`

GetDamagedByBulletsOk returns a tuple with the DamagedByBullets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamagedByBullets

`func (o *MiscV2) SetDamagedByBullets(v bool)`

SetDamagedByBullets sets DamagedByBullets field to given value.

### HasDamagedByBullets

`func (o *MiscV2) HasDamagedByBullets() bool`

HasDamagedByBullets returns a boolean if a field has been set.

### SetDamagedByBulletsNil

`func (o *MiscV2) SetDamagedByBulletsNil(b bool)`

 SetDamagedByBulletsNil sets the value for DamagedByBullets to be an explicit nil

### UnsetDamagedByBullets
`func (o *MiscV2) UnsetDamagedByBullets()`

UnsetDamagedByBullets ensures that no value is present for DamagedByBullets, not even an explicit nil
### GetIsMantleable

`func (o *MiscV2) GetIsMantleable() bool`

GetIsMantleable returns the IsMantleable field if non-nil, zero value otherwise.

### GetIsMantleableOk

`func (o *MiscV2) GetIsMantleableOk() (*bool, bool)`

GetIsMantleableOk returns a tuple with the IsMantleable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsMantleable

`func (o *MiscV2) SetIsMantleable(v bool)`

SetIsMantleable sets IsMantleable field to given value.

### HasIsMantleable

`func (o *MiscV2) HasIsMantleable() bool`

HasIsMantleable returns a boolean if a field has been set.

### SetIsMantleableNil

`func (o *MiscV2) SetIsMantleableNil(b bool)`

 SetIsMantleableNil sets the value for IsMantleable to be an explicit nil

### UnsetIsMantleable
`func (o *MiscV2) UnsetIsMantleable()`

UnsetIsMantleable ensures that no value is present for IsMantleable, not even an explicit nil
### GetPrimaryDropChance

`func (o *MiscV2) GetPrimaryDropChance() float32`

GetPrimaryDropChance returns the PrimaryDropChance field if non-nil, zero value otherwise.

### GetPrimaryDropChanceOk

`func (o *MiscV2) GetPrimaryDropChanceOk() (*float32, bool)`

GetPrimaryDropChanceOk returns a tuple with the PrimaryDropChance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrimaryDropChance

`func (o *MiscV2) SetPrimaryDropChance(v float32)`

SetPrimaryDropChance sets PrimaryDropChance field to given value.

### HasPrimaryDropChance

`func (o *MiscV2) HasPrimaryDropChance() bool`

HasPrimaryDropChance returns a boolean if a field has been set.

### SetPrimaryDropChanceNil

`func (o *MiscV2) SetPrimaryDropChanceNil(b bool)`

 SetPrimaryDropChanceNil sets the value for PrimaryDropChance to be an explicit nil

### UnsetPrimaryDropChance
`func (o *MiscV2) UnsetPrimaryDropChance()`

UnsetPrimaryDropChance ensures that no value is present for PrimaryDropChance, not even an explicit nil
### GetPrimaryPickups

`func (o *MiscV2) GetPrimaryPickups() []PickupDefinition`

GetPrimaryPickups returns the PrimaryPickups field if non-nil, zero value otherwise.

### GetPrimaryPickupsOk

`func (o *MiscV2) GetPrimaryPickupsOk() (*[]PickupDefinition, bool)`

GetPrimaryPickupsOk returns a tuple with the PrimaryPickups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrimaryPickups

`func (o *MiscV2) SetPrimaryPickups(v []PickupDefinition)`

SetPrimaryPickups sets PrimaryPickups field to given value.

### HasPrimaryPickups

`func (o *MiscV2) HasPrimaryPickups() bool`

HasPrimaryPickups returns a boolean if a field has been set.

### SetPrimaryPickupsNil

`func (o *MiscV2) SetPrimaryPickupsNil(b bool)`

 SetPrimaryPickupsNil sets the value for PrimaryPickups to be an explicit nil

### UnsetPrimaryPickups
`func (o *MiscV2) UnsetPrimaryPickups()`

UnsetPrimaryPickups ensures that no value is present for PrimaryPickups, not even an explicit nil
### GetMVecPickupsLv2

`func (o *MiscV2) GetMVecPickupsLv2() []PickupDefinition`

GetMVecPickupsLv2 returns the MVecPickupsLv2 field if non-nil, zero value otherwise.

### GetMVecPickupsLv2Ok

`func (o *MiscV2) GetMVecPickupsLv2Ok() (*[]PickupDefinition, bool)`

GetMVecPickupsLv2Ok returns a tuple with the MVecPickupsLv2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMVecPickupsLv2

`func (o *MiscV2) SetMVecPickupsLv2(v []PickupDefinition)`

SetMVecPickupsLv2 sets MVecPickupsLv2 field to given value.

### HasMVecPickupsLv2

`func (o *MiscV2) HasMVecPickupsLv2() bool`

HasMVecPickupsLv2 returns a boolean if a field has been set.

### SetMVecPickupsLv2Nil

`func (o *MiscV2) SetMVecPickupsLv2Nil(b bool)`

 SetMVecPickupsLv2Nil sets the value for MVecPickupsLv2 to be an explicit nil

### UnsetMVecPickupsLv2
`func (o *MiscV2) UnsetMVecPickupsLv2()`

UnsetMVecPickupsLv2 ensures that no value is present for MVecPickupsLv2, not even an explicit nil
### GetMVecPickupsLv3

`func (o *MiscV2) GetMVecPickupsLv3() []PickupDefinition`

GetMVecPickupsLv3 returns the MVecPickupsLv3 field if non-nil, zero value otherwise.

### GetMVecPickupsLv3Ok

`func (o *MiscV2) GetMVecPickupsLv3Ok() (*[]PickupDefinition, bool)`

GetMVecPickupsLv3Ok returns a tuple with the MVecPickupsLv3 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMVecPickupsLv3

`func (o *MiscV2) SetMVecPickupsLv3(v []PickupDefinition)`

SetMVecPickupsLv3 sets MVecPickupsLv3 field to given value.

### HasMVecPickupsLv3

`func (o *MiscV2) HasMVecPickupsLv3() bool`

HasMVecPickupsLv3 returns a boolean if a field has been set.

### SetMVecPickupsLv3Nil

`func (o *MiscV2) SetMVecPickupsLv3Nil(b bool)`

 SetMVecPickupsLv3Nil sets the value for MVecPickupsLv3 to be an explicit nil

### UnsetMVecPickupsLv3
`func (o *MiscV2) UnsetMVecPickupsLv3()`

UnsetMVecPickupsLv3 ensures that no value is present for MVecPickupsLv3, not even an explicit nil
### GetRollType

`func (o *MiscV2) GetRollType() string`

GetRollType returns the RollType field if non-nil, zero value otherwise.

### GetRollTypeOk

`func (o *MiscV2) GetRollTypeOk() (*string, bool)`

GetRollTypeOk returns a tuple with the RollType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRollType

`func (o *MiscV2) SetRollType(v string)`

SetRollType sets RollType field to given value.

### HasRollType

`func (o *MiscV2) HasRollType() bool`

HasRollType returns a boolean if a field has been set.

### SetRollTypeNil

`func (o *MiscV2) SetRollTypeNil(b bool)`

 SetRollTypeNil sets the value for RollType to be an explicit nil

### UnsetRollType
`func (o *MiscV2) UnsetRollType()`

UnsetRollType ensures that no value is present for RollType, not even an explicit nil
### GetGoldAmount

`func (o *MiscV2) GetGoldAmount() float32`

GetGoldAmount returns the GoldAmount field if non-nil, zero value otherwise.

### GetGoldAmountOk

`func (o *MiscV2) GetGoldAmountOk() (*float32, bool)`

GetGoldAmountOk returns a tuple with the GoldAmount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldAmount

`func (o *MiscV2) SetGoldAmount(v float32)`

SetGoldAmount sets GoldAmount field to given value.

### HasGoldAmount

`func (o *MiscV2) HasGoldAmount() bool`

HasGoldAmount returns a boolean if a field has been set.

### SetGoldAmountNil

`func (o *MiscV2) SetGoldAmountNil(b bool)`

 SetGoldAmountNil sets the value for GoldAmount to be an explicit nil

### UnsetGoldAmount
`func (o *MiscV2) UnsetGoldAmount()`

UnsetGoldAmount ensures that no value is present for GoldAmount, not even an explicit nil
### GetGoldPerMinuteAmount

`func (o *MiscV2) GetGoldPerMinuteAmount() float32`

GetGoldPerMinuteAmount returns the GoldPerMinuteAmount field if non-nil, zero value otherwise.

### GetGoldPerMinuteAmountOk

`func (o *MiscV2) GetGoldPerMinuteAmountOk() (*float32, bool)`

GetGoldPerMinuteAmountOk returns a tuple with the GoldPerMinuteAmount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldPerMinuteAmount

`func (o *MiscV2) SetGoldPerMinuteAmount(v float32)`

SetGoldPerMinuteAmount sets GoldPerMinuteAmount field to given value.

### HasGoldPerMinuteAmount

`func (o *MiscV2) HasGoldPerMinuteAmount() bool`

HasGoldPerMinuteAmount returns a boolean if a field has been set.

### SetGoldPerMinuteAmountNil

`func (o *MiscV2) SetGoldPerMinuteAmountNil(b bool)`

 SetGoldPerMinuteAmountNil sets the value for GoldPerMinuteAmount to be an explicit nil

### UnsetGoldPerMinuteAmount
`func (o *MiscV2) UnsetGoldPerMinuteAmount()`

UnsetGoldPerMinuteAmount ensures that no value is present for GoldPerMinuteAmount, not even an explicit nil
### GetModifier

`func (o *MiscV2) GetModifier() SubclassModifierDefinition`

GetModifier returns the Modifier field if non-nil, zero value otherwise.

### GetModifierOk

`func (o *MiscV2) GetModifierOk() (*SubclassModifierDefinition, bool)`

GetModifierOk returns a tuple with the Modifier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifier

`func (o *MiscV2) SetModifier(v SubclassModifierDefinition)`

SetModifier sets Modifier field to given value.

### HasModifier

`func (o *MiscV2) HasModifier() bool`

HasModifier returns a boolean if a field has been set.

### SetModifierNil

`func (o *MiscV2) SetModifierNil(b bool)`

 SetModifierNil sets the value for Modifier to be an explicit nil

### UnsetModifier
`func (o *MiscV2) UnsetModifier()`

UnsetModifier ensures that no value is present for Modifier, not even an explicit nil
### GetPickupRadius

`func (o *MiscV2) GetPickupRadius() float32`

GetPickupRadius returns the PickupRadius field if non-nil, zero value otherwise.

### GetPickupRadiusOk

`func (o *MiscV2) GetPickupRadiusOk() (*float32, bool)`

GetPickupRadiusOk returns a tuple with the PickupRadius field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPickupRadius

`func (o *MiscV2) SetPickupRadius(v float32)`

SetPickupRadius sets PickupRadius field to given value.

### HasPickupRadius

`func (o *MiscV2) HasPickupRadius() bool`

HasPickupRadius returns a boolean if a field has been set.

### SetPickupRadiusNil

`func (o *MiscV2) SetPickupRadiusNil(b bool)`

 SetPickupRadiusNil sets the value for PickupRadius to be an explicit nil

### UnsetPickupRadius
`func (o *MiscV2) UnsetPickupRadius()`

UnsetPickupRadius ensures that no value is present for PickupRadius, not even an explicit nil
### GetExpirationDuration

`func (o *MiscV2) GetExpirationDuration() float32`

GetExpirationDuration returns the ExpirationDuration field if non-nil, zero value otherwise.

### GetExpirationDurationOk

`func (o *MiscV2) GetExpirationDurationOk() (*float32, bool)`

GetExpirationDurationOk returns a tuple with the ExpirationDuration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpirationDuration

`func (o *MiscV2) SetExpirationDuration(v float32)`

SetExpirationDuration sets ExpirationDuration field to given value.

### HasExpirationDuration

`func (o *MiscV2) HasExpirationDuration() bool`

HasExpirationDuration returns a boolean if a field has been set.

### SetExpirationDurationNil

`func (o *MiscV2) SetExpirationDurationNil(b bool)`

 SetExpirationDurationNil sets the value for ExpirationDuration to be an explicit nil

### UnsetExpirationDuration
`func (o *MiscV2) UnsetExpirationDuration()`

UnsetExpirationDuration ensures that no value is present for ExpirationDuration, not even an explicit nil
### GetShowOnMinimap

`func (o *MiscV2) GetShowOnMinimap() bool`

GetShowOnMinimap returns the ShowOnMinimap field if non-nil, zero value otherwise.

### GetShowOnMinimapOk

`func (o *MiscV2) GetShowOnMinimapOk() (*bool, bool)`

GetShowOnMinimapOk returns a tuple with the ShowOnMinimap field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShowOnMinimap

`func (o *MiscV2) SetShowOnMinimap(v bool)`

SetShowOnMinimap sets ShowOnMinimap field to given value.

### HasShowOnMinimap

`func (o *MiscV2) HasShowOnMinimap() bool`

HasShowOnMinimap returns a boolean if a field has been set.

### SetShowOnMinimapNil

`func (o *MiscV2) SetShowOnMinimapNil(b bool)`

 SetShowOnMinimapNil sets the value for ShowOnMinimap to be an explicit nil

### UnsetShowOnMinimap
`func (o *MiscV2) UnsetShowOnMinimap()`

UnsetShowOnMinimap ensures that no value is present for ShowOnMinimap, not even an explicit nil
### GetOrbSpawnDelayMin

`func (o *MiscV2) GetOrbSpawnDelayMin() float32`

GetOrbSpawnDelayMin returns the OrbSpawnDelayMin field if non-nil, zero value otherwise.

### GetOrbSpawnDelayMinOk

`func (o *MiscV2) GetOrbSpawnDelayMinOk() (*float32, bool)`

GetOrbSpawnDelayMinOk returns a tuple with the OrbSpawnDelayMin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrbSpawnDelayMin

`func (o *MiscV2) SetOrbSpawnDelayMin(v float32)`

SetOrbSpawnDelayMin sets OrbSpawnDelayMin field to given value.

### HasOrbSpawnDelayMin

`func (o *MiscV2) HasOrbSpawnDelayMin() bool`

HasOrbSpawnDelayMin returns a boolean if a field has been set.

### SetOrbSpawnDelayMinNil

`func (o *MiscV2) SetOrbSpawnDelayMinNil(b bool)`

 SetOrbSpawnDelayMinNil sets the value for OrbSpawnDelayMin to be an explicit nil

### UnsetOrbSpawnDelayMin
`func (o *MiscV2) UnsetOrbSpawnDelayMin()`

UnsetOrbSpawnDelayMin ensures that no value is present for OrbSpawnDelayMin, not even an explicit nil
### GetOrbSpawnDelayMax

`func (o *MiscV2) GetOrbSpawnDelayMax() float32`

GetOrbSpawnDelayMax returns the OrbSpawnDelayMax field if non-nil, zero value otherwise.

### GetOrbSpawnDelayMaxOk

`func (o *MiscV2) GetOrbSpawnDelayMaxOk() (*float32, bool)`

GetOrbSpawnDelayMaxOk returns a tuple with the OrbSpawnDelayMax field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrbSpawnDelayMax

`func (o *MiscV2) SetOrbSpawnDelayMax(v float32)`

SetOrbSpawnDelayMax sets OrbSpawnDelayMax field to given value.

### HasOrbSpawnDelayMax

`func (o *MiscV2) HasOrbSpawnDelayMax() bool`

HasOrbSpawnDelayMax returns a boolean if a field has been set.

### SetOrbSpawnDelayMaxNil

`func (o *MiscV2) SetOrbSpawnDelayMaxNil(b bool)`

 SetOrbSpawnDelayMaxNil sets the value for OrbSpawnDelayMax to be an explicit nil

### UnsetOrbSpawnDelayMax
`func (o *MiscV2) UnsetOrbSpawnDelayMax()`

UnsetOrbSpawnDelayMax ensures that no value is present for OrbSpawnDelayMax, not even an explicit nil
### GetLifetime

`func (o *MiscV2) GetLifetime() float32`

GetLifetime returns the Lifetime field if non-nil, zero value otherwise.

### GetLifetimeOk

`func (o *MiscV2) GetLifetimeOk() (*float32, bool)`

GetLifetimeOk returns a tuple with the Lifetime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLifetime

`func (o *MiscV2) SetLifetime(v float32)`

SetLifetime sets Lifetime field to given value.

### HasLifetime

`func (o *MiscV2) HasLifetime() bool`

HasLifetime returns a boolean if a field has been set.

### SetLifetimeNil

`func (o *MiscV2) SetLifetimeNil(b bool)`

 SetLifetimeNil sets the value for Lifetime to be an explicit nil

### UnsetLifetime
`func (o *MiscV2) UnsetLifetime()`

UnsetLifetime ensures that no value is present for Lifetime, not even an explicit nil
### GetCollisionRadius

`func (o *MiscV2) GetCollisionRadius() float32`

GetCollisionRadius returns the CollisionRadius field if non-nil, zero value otherwise.

### GetCollisionRadiusOk

`func (o *MiscV2) GetCollisionRadiusOk() (*float32, bool)`

GetCollisionRadiusOk returns a tuple with the CollisionRadius field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCollisionRadius

`func (o *MiscV2) SetCollisionRadius(v float32)`

SetCollisionRadius sets CollisionRadius field to given value.

### HasCollisionRadius

`func (o *MiscV2) HasCollisionRadius() bool`

HasCollisionRadius returns a boolean if a field has been set.

### SetCollisionRadiusNil

`func (o *MiscV2) SetCollisionRadiusNil(b bool)`

 SetCollisionRadiusNil sets the value for CollisionRadius to be an explicit nil

### UnsetCollisionRadius
`func (o *MiscV2) UnsetCollisionRadius()`

UnsetCollisionRadius ensures that no value is present for CollisionRadius, not even an explicit nil
### GetId

`func (o *MiscV2) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *MiscV2) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *MiscV2) SetId(v int32)`

SetId sets Id field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


