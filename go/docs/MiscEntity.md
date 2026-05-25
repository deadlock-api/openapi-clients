# MiscEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BreakOnDodgeTouch** | Pointer to **NullableBool** |  | [optional] 
**ClassName** | **string** |  | 
**CollisionRadius** | Pointer to **NullableFloat64** |  | [optional] 
**Color** | Pointer to [**NullableColor**](Color.md) |  | [optional] 
**DamagedByAbilities** | Pointer to **NullableBool** |  | [optional] 
**DamagedByBullets** | Pointer to **NullableBool** |  | [optional] 
**DamagedByMelee** | Pointer to **NullableBool** |  | [optional] 
**ExpirationDuration** | Pointer to [**NullableCurveOrFloat**](CurveOrFloat.md) |  | [optional] 
**GoldAmount** | Pointer to **NullableFloat64** |  | [optional] 
**GoldPerMinuteAmount** | Pointer to **NullableFloat64** |  | [optional] 
**Health** | Pointer to **NullableInt64** |  | [optional] 
**Id** | **int32** |  | 
**InitialSpawnDelayInSeconds** | Pointer to **NullableInt64** |  | [optional] 
**InitialSpawnDelaySeconds** | Pointer to **NullableInt64** | Duplicate of &#x60;initial_spawn_delay_in_seconds&#x60; for shape parity. | [optional] 
**InitialSpawnTime** | Pointer to **NullableFloat64** |  | [optional] 
**IsMantleable** | Pointer to **NullableBool** |  | [optional] 
**Lifetime** | Pointer to **NullableFloat64** |  | [optional] 
**LootListDeckSize** | Pointer to **NullableInt64** |  | [optional] 
**MVecPickupsLv2** | Pointer to [**[]Pickup**](Pickup.md) |  | [optional] 
**MVecPickupsLv3** | Pointer to [**[]Pickup**](Pickup.md) |  | [optional] 
**MatchTimeMinsForLevel2Pickups** | Pointer to **NullableInt64** |  | [optional] 
**MatchTimeMinsForLevel3Pickups** | Pointer to **NullableInt64** |  | [optional] 
**Modifier** | Pointer to [**NullableSubclassModifierDefinition**](SubclassModifierDefinition.md) |  | [optional] 
**OrbSpawnDelayMax** | Pointer to **NullableFloat64** |  | [optional] 
**OrbSpawnDelayMin** | Pointer to **NullableFloat64** |  | [optional] 
**PickupRadius** | Pointer to [**NullableCurveOrFloat**](CurveOrFloat.md) |  | [optional] 
**PrimaryDropChance** | Pointer to **NullableFloat64** |  | [optional] 
**PrimaryPickups** | Pointer to [**[]Pickup**](Pickup.md) |  | [optional] 
**RenderAfterDeath** | Pointer to **NullableBool** |  | [optional] 
**RespawnTime** | Pointer to **NullableFloat64** |  | [optional] 
**RollType** | Pointer to [**NullableRollType**](RollType.md) |  | [optional] 
**ShowOnMinimap** | Pointer to **NullableBool** |  | [optional] 
**SolidAfterDeath** | Pointer to **NullableBool** |  | [optional] 
**SpawnInterval** | Pointer to **NullableFloat64** |  | [optional] 
**SpawnIntervalInSeconds** | Pointer to **NullableInt64** |  | [optional] 

## Methods

### NewMiscEntity

`func NewMiscEntity(className string, id int32, ) *MiscEntity`

NewMiscEntity instantiates a new MiscEntity object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMiscEntityWithDefaults

`func NewMiscEntityWithDefaults() *MiscEntity`

NewMiscEntityWithDefaults instantiates a new MiscEntity object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBreakOnDodgeTouch

`func (o *MiscEntity) GetBreakOnDodgeTouch() bool`

GetBreakOnDodgeTouch returns the BreakOnDodgeTouch field if non-nil, zero value otherwise.

### GetBreakOnDodgeTouchOk

`func (o *MiscEntity) GetBreakOnDodgeTouchOk() (*bool, bool)`

GetBreakOnDodgeTouchOk returns a tuple with the BreakOnDodgeTouch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBreakOnDodgeTouch

`func (o *MiscEntity) SetBreakOnDodgeTouch(v bool)`

SetBreakOnDodgeTouch sets BreakOnDodgeTouch field to given value.

### HasBreakOnDodgeTouch

`func (o *MiscEntity) HasBreakOnDodgeTouch() bool`

HasBreakOnDodgeTouch returns a boolean if a field has been set.

### SetBreakOnDodgeTouchNil

`func (o *MiscEntity) SetBreakOnDodgeTouchNil(b bool)`

 SetBreakOnDodgeTouchNil sets the value for BreakOnDodgeTouch to be an explicit nil

### UnsetBreakOnDodgeTouch
`func (o *MiscEntity) UnsetBreakOnDodgeTouch()`

UnsetBreakOnDodgeTouch ensures that no value is present for BreakOnDodgeTouch, not even an explicit nil
### GetClassName

`func (o *MiscEntity) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *MiscEntity) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *MiscEntity) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetCollisionRadius

`func (o *MiscEntity) GetCollisionRadius() float64`

GetCollisionRadius returns the CollisionRadius field if non-nil, zero value otherwise.

### GetCollisionRadiusOk

`func (o *MiscEntity) GetCollisionRadiusOk() (*float64, bool)`

GetCollisionRadiusOk returns a tuple with the CollisionRadius field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCollisionRadius

`func (o *MiscEntity) SetCollisionRadius(v float64)`

SetCollisionRadius sets CollisionRadius field to given value.

### HasCollisionRadius

`func (o *MiscEntity) HasCollisionRadius() bool`

HasCollisionRadius returns a boolean if a field has been set.

### SetCollisionRadiusNil

`func (o *MiscEntity) SetCollisionRadiusNil(b bool)`

 SetCollisionRadiusNil sets the value for CollisionRadius to be an explicit nil

### UnsetCollisionRadius
`func (o *MiscEntity) UnsetCollisionRadius()`

UnsetCollisionRadius ensures that no value is present for CollisionRadius, not even an explicit nil
### GetColor

`func (o *MiscEntity) GetColor() Color`

GetColor returns the Color field if non-nil, zero value otherwise.

### GetColorOk

`func (o *MiscEntity) GetColorOk() (*Color, bool)`

GetColorOk returns a tuple with the Color field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColor

`func (o *MiscEntity) SetColor(v Color)`

SetColor sets Color field to given value.

### HasColor

`func (o *MiscEntity) HasColor() bool`

HasColor returns a boolean if a field has been set.

### SetColorNil

`func (o *MiscEntity) SetColorNil(b bool)`

 SetColorNil sets the value for Color to be an explicit nil

### UnsetColor
`func (o *MiscEntity) UnsetColor()`

UnsetColor ensures that no value is present for Color, not even an explicit nil
### GetDamagedByAbilities

`func (o *MiscEntity) GetDamagedByAbilities() bool`

GetDamagedByAbilities returns the DamagedByAbilities field if non-nil, zero value otherwise.

### GetDamagedByAbilitiesOk

`func (o *MiscEntity) GetDamagedByAbilitiesOk() (*bool, bool)`

GetDamagedByAbilitiesOk returns a tuple with the DamagedByAbilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamagedByAbilities

`func (o *MiscEntity) SetDamagedByAbilities(v bool)`

SetDamagedByAbilities sets DamagedByAbilities field to given value.

### HasDamagedByAbilities

`func (o *MiscEntity) HasDamagedByAbilities() bool`

HasDamagedByAbilities returns a boolean if a field has been set.

### SetDamagedByAbilitiesNil

`func (o *MiscEntity) SetDamagedByAbilitiesNil(b bool)`

 SetDamagedByAbilitiesNil sets the value for DamagedByAbilities to be an explicit nil

### UnsetDamagedByAbilities
`func (o *MiscEntity) UnsetDamagedByAbilities()`

UnsetDamagedByAbilities ensures that no value is present for DamagedByAbilities, not even an explicit nil
### GetDamagedByBullets

`func (o *MiscEntity) GetDamagedByBullets() bool`

GetDamagedByBullets returns the DamagedByBullets field if non-nil, zero value otherwise.

### GetDamagedByBulletsOk

`func (o *MiscEntity) GetDamagedByBulletsOk() (*bool, bool)`

GetDamagedByBulletsOk returns a tuple with the DamagedByBullets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamagedByBullets

`func (o *MiscEntity) SetDamagedByBullets(v bool)`

SetDamagedByBullets sets DamagedByBullets field to given value.

### HasDamagedByBullets

`func (o *MiscEntity) HasDamagedByBullets() bool`

HasDamagedByBullets returns a boolean if a field has been set.

### SetDamagedByBulletsNil

`func (o *MiscEntity) SetDamagedByBulletsNil(b bool)`

 SetDamagedByBulletsNil sets the value for DamagedByBullets to be an explicit nil

### UnsetDamagedByBullets
`func (o *MiscEntity) UnsetDamagedByBullets()`

UnsetDamagedByBullets ensures that no value is present for DamagedByBullets, not even an explicit nil
### GetDamagedByMelee

`func (o *MiscEntity) GetDamagedByMelee() bool`

GetDamagedByMelee returns the DamagedByMelee field if non-nil, zero value otherwise.

### GetDamagedByMeleeOk

`func (o *MiscEntity) GetDamagedByMeleeOk() (*bool, bool)`

GetDamagedByMeleeOk returns a tuple with the DamagedByMelee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamagedByMelee

`func (o *MiscEntity) SetDamagedByMelee(v bool)`

SetDamagedByMelee sets DamagedByMelee field to given value.

### HasDamagedByMelee

`func (o *MiscEntity) HasDamagedByMelee() bool`

HasDamagedByMelee returns a boolean if a field has been set.

### SetDamagedByMeleeNil

`func (o *MiscEntity) SetDamagedByMeleeNil(b bool)`

 SetDamagedByMeleeNil sets the value for DamagedByMelee to be an explicit nil

### UnsetDamagedByMelee
`func (o *MiscEntity) UnsetDamagedByMelee()`

UnsetDamagedByMelee ensures that no value is present for DamagedByMelee, not even an explicit nil
### GetExpirationDuration

`func (o *MiscEntity) GetExpirationDuration() CurveOrFloat`

GetExpirationDuration returns the ExpirationDuration field if non-nil, zero value otherwise.

### GetExpirationDurationOk

`func (o *MiscEntity) GetExpirationDurationOk() (*CurveOrFloat, bool)`

GetExpirationDurationOk returns a tuple with the ExpirationDuration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpirationDuration

`func (o *MiscEntity) SetExpirationDuration(v CurveOrFloat)`

SetExpirationDuration sets ExpirationDuration field to given value.

### HasExpirationDuration

`func (o *MiscEntity) HasExpirationDuration() bool`

HasExpirationDuration returns a boolean if a field has been set.

### SetExpirationDurationNil

`func (o *MiscEntity) SetExpirationDurationNil(b bool)`

 SetExpirationDurationNil sets the value for ExpirationDuration to be an explicit nil

### UnsetExpirationDuration
`func (o *MiscEntity) UnsetExpirationDuration()`

UnsetExpirationDuration ensures that no value is present for ExpirationDuration, not even an explicit nil
### GetGoldAmount

`func (o *MiscEntity) GetGoldAmount() float64`

GetGoldAmount returns the GoldAmount field if non-nil, zero value otherwise.

### GetGoldAmountOk

`func (o *MiscEntity) GetGoldAmountOk() (*float64, bool)`

GetGoldAmountOk returns a tuple with the GoldAmount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldAmount

`func (o *MiscEntity) SetGoldAmount(v float64)`

SetGoldAmount sets GoldAmount field to given value.

### HasGoldAmount

`func (o *MiscEntity) HasGoldAmount() bool`

HasGoldAmount returns a boolean if a field has been set.

### SetGoldAmountNil

`func (o *MiscEntity) SetGoldAmountNil(b bool)`

 SetGoldAmountNil sets the value for GoldAmount to be an explicit nil

### UnsetGoldAmount
`func (o *MiscEntity) UnsetGoldAmount()`

UnsetGoldAmount ensures that no value is present for GoldAmount, not even an explicit nil
### GetGoldPerMinuteAmount

`func (o *MiscEntity) GetGoldPerMinuteAmount() float64`

GetGoldPerMinuteAmount returns the GoldPerMinuteAmount field if non-nil, zero value otherwise.

### GetGoldPerMinuteAmountOk

`func (o *MiscEntity) GetGoldPerMinuteAmountOk() (*float64, bool)`

GetGoldPerMinuteAmountOk returns a tuple with the GoldPerMinuteAmount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldPerMinuteAmount

`func (o *MiscEntity) SetGoldPerMinuteAmount(v float64)`

SetGoldPerMinuteAmount sets GoldPerMinuteAmount field to given value.

### HasGoldPerMinuteAmount

`func (o *MiscEntity) HasGoldPerMinuteAmount() bool`

HasGoldPerMinuteAmount returns a boolean if a field has been set.

### SetGoldPerMinuteAmountNil

`func (o *MiscEntity) SetGoldPerMinuteAmountNil(b bool)`

 SetGoldPerMinuteAmountNil sets the value for GoldPerMinuteAmount to be an explicit nil

### UnsetGoldPerMinuteAmount
`func (o *MiscEntity) UnsetGoldPerMinuteAmount()`

UnsetGoldPerMinuteAmount ensures that no value is present for GoldPerMinuteAmount, not even an explicit nil
### GetHealth

`func (o *MiscEntity) GetHealth() int64`

GetHealth returns the Health field if non-nil, zero value otherwise.

### GetHealthOk

`func (o *MiscEntity) GetHealthOk() (*int64, bool)`

GetHealthOk returns a tuple with the Health field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHealth

`func (o *MiscEntity) SetHealth(v int64)`

SetHealth sets Health field to given value.

### HasHealth

`func (o *MiscEntity) HasHealth() bool`

HasHealth returns a boolean if a field has been set.

### SetHealthNil

`func (o *MiscEntity) SetHealthNil(b bool)`

 SetHealthNil sets the value for Health to be an explicit nil

### UnsetHealth
`func (o *MiscEntity) UnsetHealth()`

UnsetHealth ensures that no value is present for Health, not even an explicit nil
### GetId

`func (o *MiscEntity) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *MiscEntity) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *MiscEntity) SetId(v int32)`

SetId sets Id field to given value.


### GetInitialSpawnDelayInSeconds

`func (o *MiscEntity) GetInitialSpawnDelayInSeconds() int64`

GetInitialSpawnDelayInSeconds returns the InitialSpawnDelayInSeconds field if non-nil, zero value otherwise.

### GetInitialSpawnDelayInSecondsOk

`func (o *MiscEntity) GetInitialSpawnDelayInSecondsOk() (*int64, bool)`

GetInitialSpawnDelayInSecondsOk returns a tuple with the InitialSpawnDelayInSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInitialSpawnDelayInSeconds

`func (o *MiscEntity) SetInitialSpawnDelayInSeconds(v int64)`

SetInitialSpawnDelayInSeconds sets InitialSpawnDelayInSeconds field to given value.

### HasInitialSpawnDelayInSeconds

`func (o *MiscEntity) HasInitialSpawnDelayInSeconds() bool`

HasInitialSpawnDelayInSeconds returns a boolean if a field has been set.

### SetInitialSpawnDelayInSecondsNil

`func (o *MiscEntity) SetInitialSpawnDelayInSecondsNil(b bool)`

 SetInitialSpawnDelayInSecondsNil sets the value for InitialSpawnDelayInSeconds to be an explicit nil

### UnsetInitialSpawnDelayInSeconds
`func (o *MiscEntity) UnsetInitialSpawnDelayInSeconds()`

UnsetInitialSpawnDelayInSeconds ensures that no value is present for InitialSpawnDelayInSeconds, not even an explicit nil
### GetInitialSpawnDelaySeconds

`func (o *MiscEntity) GetInitialSpawnDelaySeconds() int64`

GetInitialSpawnDelaySeconds returns the InitialSpawnDelaySeconds field if non-nil, zero value otherwise.

### GetInitialSpawnDelaySecondsOk

`func (o *MiscEntity) GetInitialSpawnDelaySecondsOk() (*int64, bool)`

GetInitialSpawnDelaySecondsOk returns a tuple with the InitialSpawnDelaySeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInitialSpawnDelaySeconds

`func (o *MiscEntity) SetInitialSpawnDelaySeconds(v int64)`

SetInitialSpawnDelaySeconds sets InitialSpawnDelaySeconds field to given value.

### HasInitialSpawnDelaySeconds

`func (o *MiscEntity) HasInitialSpawnDelaySeconds() bool`

HasInitialSpawnDelaySeconds returns a boolean if a field has been set.

### SetInitialSpawnDelaySecondsNil

`func (o *MiscEntity) SetInitialSpawnDelaySecondsNil(b bool)`

 SetInitialSpawnDelaySecondsNil sets the value for InitialSpawnDelaySeconds to be an explicit nil

### UnsetInitialSpawnDelaySeconds
`func (o *MiscEntity) UnsetInitialSpawnDelaySeconds()`

UnsetInitialSpawnDelaySeconds ensures that no value is present for InitialSpawnDelaySeconds, not even an explicit nil
### GetInitialSpawnTime

`func (o *MiscEntity) GetInitialSpawnTime() float64`

GetInitialSpawnTime returns the InitialSpawnTime field if non-nil, zero value otherwise.

### GetInitialSpawnTimeOk

`func (o *MiscEntity) GetInitialSpawnTimeOk() (*float64, bool)`

GetInitialSpawnTimeOk returns a tuple with the InitialSpawnTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInitialSpawnTime

`func (o *MiscEntity) SetInitialSpawnTime(v float64)`

SetInitialSpawnTime sets InitialSpawnTime field to given value.

### HasInitialSpawnTime

`func (o *MiscEntity) HasInitialSpawnTime() bool`

HasInitialSpawnTime returns a boolean if a field has been set.

### SetInitialSpawnTimeNil

`func (o *MiscEntity) SetInitialSpawnTimeNil(b bool)`

 SetInitialSpawnTimeNil sets the value for InitialSpawnTime to be an explicit nil

### UnsetInitialSpawnTime
`func (o *MiscEntity) UnsetInitialSpawnTime()`

UnsetInitialSpawnTime ensures that no value is present for InitialSpawnTime, not even an explicit nil
### GetIsMantleable

`func (o *MiscEntity) GetIsMantleable() bool`

GetIsMantleable returns the IsMantleable field if non-nil, zero value otherwise.

### GetIsMantleableOk

`func (o *MiscEntity) GetIsMantleableOk() (*bool, bool)`

GetIsMantleableOk returns a tuple with the IsMantleable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsMantleable

`func (o *MiscEntity) SetIsMantleable(v bool)`

SetIsMantleable sets IsMantleable field to given value.

### HasIsMantleable

`func (o *MiscEntity) HasIsMantleable() bool`

HasIsMantleable returns a boolean if a field has been set.

### SetIsMantleableNil

`func (o *MiscEntity) SetIsMantleableNil(b bool)`

 SetIsMantleableNil sets the value for IsMantleable to be an explicit nil

### UnsetIsMantleable
`func (o *MiscEntity) UnsetIsMantleable()`

UnsetIsMantleable ensures that no value is present for IsMantleable, not even an explicit nil
### GetLifetime

`func (o *MiscEntity) GetLifetime() float64`

GetLifetime returns the Lifetime field if non-nil, zero value otherwise.

### GetLifetimeOk

`func (o *MiscEntity) GetLifetimeOk() (*float64, bool)`

GetLifetimeOk returns a tuple with the Lifetime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLifetime

`func (o *MiscEntity) SetLifetime(v float64)`

SetLifetime sets Lifetime field to given value.

### HasLifetime

`func (o *MiscEntity) HasLifetime() bool`

HasLifetime returns a boolean if a field has been set.

### SetLifetimeNil

`func (o *MiscEntity) SetLifetimeNil(b bool)`

 SetLifetimeNil sets the value for Lifetime to be an explicit nil

### UnsetLifetime
`func (o *MiscEntity) UnsetLifetime()`

UnsetLifetime ensures that no value is present for Lifetime, not even an explicit nil
### GetLootListDeckSize

`func (o *MiscEntity) GetLootListDeckSize() int64`

GetLootListDeckSize returns the LootListDeckSize field if non-nil, zero value otherwise.

### GetLootListDeckSizeOk

`func (o *MiscEntity) GetLootListDeckSizeOk() (*int64, bool)`

GetLootListDeckSizeOk returns a tuple with the LootListDeckSize field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLootListDeckSize

`func (o *MiscEntity) SetLootListDeckSize(v int64)`

SetLootListDeckSize sets LootListDeckSize field to given value.

### HasLootListDeckSize

`func (o *MiscEntity) HasLootListDeckSize() bool`

HasLootListDeckSize returns a boolean if a field has been set.

### SetLootListDeckSizeNil

`func (o *MiscEntity) SetLootListDeckSizeNil(b bool)`

 SetLootListDeckSizeNil sets the value for LootListDeckSize to be an explicit nil

### UnsetLootListDeckSize
`func (o *MiscEntity) UnsetLootListDeckSize()`

UnsetLootListDeckSize ensures that no value is present for LootListDeckSize, not even an explicit nil
### GetMVecPickupsLv2

`func (o *MiscEntity) GetMVecPickupsLv2() []Pickup`

GetMVecPickupsLv2 returns the MVecPickupsLv2 field if non-nil, zero value otherwise.

### GetMVecPickupsLv2Ok

`func (o *MiscEntity) GetMVecPickupsLv2Ok() (*[]Pickup, bool)`

GetMVecPickupsLv2Ok returns a tuple with the MVecPickupsLv2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMVecPickupsLv2

`func (o *MiscEntity) SetMVecPickupsLv2(v []Pickup)`

SetMVecPickupsLv2 sets MVecPickupsLv2 field to given value.

### HasMVecPickupsLv2

`func (o *MiscEntity) HasMVecPickupsLv2() bool`

HasMVecPickupsLv2 returns a boolean if a field has been set.

### SetMVecPickupsLv2Nil

`func (o *MiscEntity) SetMVecPickupsLv2Nil(b bool)`

 SetMVecPickupsLv2Nil sets the value for MVecPickupsLv2 to be an explicit nil

### UnsetMVecPickupsLv2
`func (o *MiscEntity) UnsetMVecPickupsLv2()`

UnsetMVecPickupsLv2 ensures that no value is present for MVecPickupsLv2, not even an explicit nil
### GetMVecPickupsLv3

`func (o *MiscEntity) GetMVecPickupsLv3() []Pickup`

GetMVecPickupsLv3 returns the MVecPickupsLv3 field if non-nil, zero value otherwise.

### GetMVecPickupsLv3Ok

`func (o *MiscEntity) GetMVecPickupsLv3Ok() (*[]Pickup, bool)`

GetMVecPickupsLv3Ok returns a tuple with the MVecPickupsLv3 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMVecPickupsLv3

`func (o *MiscEntity) SetMVecPickupsLv3(v []Pickup)`

SetMVecPickupsLv3 sets MVecPickupsLv3 field to given value.

### HasMVecPickupsLv3

`func (o *MiscEntity) HasMVecPickupsLv3() bool`

HasMVecPickupsLv3 returns a boolean if a field has been set.

### SetMVecPickupsLv3Nil

`func (o *MiscEntity) SetMVecPickupsLv3Nil(b bool)`

 SetMVecPickupsLv3Nil sets the value for MVecPickupsLv3 to be an explicit nil

### UnsetMVecPickupsLv3
`func (o *MiscEntity) UnsetMVecPickupsLv3()`

UnsetMVecPickupsLv3 ensures that no value is present for MVecPickupsLv3, not even an explicit nil
### GetMatchTimeMinsForLevel2Pickups

`func (o *MiscEntity) GetMatchTimeMinsForLevel2Pickups() int64`

GetMatchTimeMinsForLevel2Pickups returns the MatchTimeMinsForLevel2Pickups field if non-nil, zero value otherwise.

### GetMatchTimeMinsForLevel2PickupsOk

`func (o *MiscEntity) GetMatchTimeMinsForLevel2PickupsOk() (*int64, bool)`

GetMatchTimeMinsForLevel2PickupsOk returns a tuple with the MatchTimeMinsForLevel2Pickups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchTimeMinsForLevel2Pickups

`func (o *MiscEntity) SetMatchTimeMinsForLevel2Pickups(v int64)`

SetMatchTimeMinsForLevel2Pickups sets MatchTimeMinsForLevel2Pickups field to given value.

### HasMatchTimeMinsForLevel2Pickups

`func (o *MiscEntity) HasMatchTimeMinsForLevel2Pickups() bool`

HasMatchTimeMinsForLevel2Pickups returns a boolean if a field has been set.

### SetMatchTimeMinsForLevel2PickupsNil

`func (o *MiscEntity) SetMatchTimeMinsForLevel2PickupsNil(b bool)`

 SetMatchTimeMinsForLevel2PickupsNil sets the value for MatchTimeMinsForLevel2Pickups to be an explicit nil

### UnsetMatchTimeMinsForLevel2Pickups
`func (o *MiscEntity) UnsetMatchTimeMinsForLevel2Pickups()`

UnsetMatchTimeMinsForLevel2Pickups ensures that no value is present for MatchTimeMinsForLevel2Pickups, not even an explicit nil
### GetMatchTimeMinsForLevel3Pickups

`func (o *MiscEntity) GetMatchTimeMinsForLevel3Pickups() int64`

GetMatchTimeMinsForLevel3Pickups returns the MatchTimeMinsForLevel3Pickups field if non-nil, zero value otherwise.

### GetMatchTimeMinsForLevel3PickupsOk

`func (o *MiscEntity) GetMatchTimeMinsForLevel3PickupsOk() (*int64, bool)`

GetMatchTimeMinsForLevel3PickupsOk returns a tuple with the MatchTimeMinsForLevel3Pickups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchTimeMinsForLevel3Pickups

`func (o *MiscEntity) SetMatchTimeMinsForLevel3Pickups(v int64)`

SetMatchTimeMinsForLevel3Pickups sets MatchTimeMinsForLevel3Pickups field to given value.

### HasMatchTimeMinsForLevel3Pickups

`func (o *MiscEntity) HasMatchTimeMinsForLevel3Pickups() bool`

HasMatchTimeMinsForLevel3Pickups returns a boolean if a field has been set.

### SetMatchTimeMinsForLevel3PickupsNil

`func (o *MiscEntity) SetMatchTimeMinsForLevel3PickupsNil(b bool)`

 SetMatchTimeMinsForLevel3PickupsNil sets the value for MatchTimeMinsForLevel3Pickups to be an explicit nil

### UnsetMatchTimeMinsForLevel3Pickups
`func (o *MiscEntity) UnsetMatchTimeMinsForLevel3Pickups()`

UnsetMatchTimeMinsForLevel3Pickups ensures that no value is present for MatchTimeMinsForLevel3Pickups, not even an explicit nil
### GetModifier

`func (o *MiscEntity) GetModifier() SubclassModifierDefinition`

GetModifier returns the Modifier field if non-nil, zero value otherwise.

### GetModifierOk

`func (o *MiscEntity) GetModifierOk() (*SubclassModifierDefinition, bool)`

GetModifierOk returns a tuple with the Modifier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifier

`func (o *MiscEntity) SetModifier(v SubclassModifierDefinition)`

SetModifier sets Modifier field to given value.

### HasModifier

`func (o *MiscEntity) HasModifier() bool`

HasModifier returns a boolean if a field has been set.

### SetModifierNil

`func (o *MiscEntity) SetModifierNil(b bool)`

 SetModifierNil sets the value for Modifier to be an explicit nil

### UnsetModifier
`func (o *MiscEntity) UnsetModifier()`

UnsetModifier ensures that no value is present for Modifier, not even an explicit nil
### GetOrbSpawnDelayMax

`func (o *MiscEntity) GetOrbSpawnDelayMax() float64`

GetOrbSpawnDelayMax returns the OrbSpawnDelayMax field if non-nil, zero value otherwise.

### GetOrbSpawnDelayMaxOk

`func (o *MiscEntity) GetOrbSpawnDelayMaxOk() (*float64, bool)`

GetOrbSpawnDelayMaxOk returns a tuple with the OrbSpawnDelayMax field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrbSpawnDelayMax

`func (o *MiscEntity) SetOrbSpawnDelayMax(v float64)`

SetOrbSpawnDelayMax sets OrbSpawnDelayMax field to given value.

### HasOrbSpawnDelayMax

`func (o *MiscEntity) HasOrbSpawnDelayMax() bool`

HasOrbSpawnDelayMax returns a boolean if a field has been set.

### SetOrbSpawnDelayMaxNil

`func (o *MiscEntity) SetOrbSpawnDelayMaxNil(b bool)`

 SetOrbSpawnDelayMaxNil sets the value for OrbSpawnDelayMax to be an explicit nil

### UnsetOrbSpawnDelayMax
`func (o *MiscEntity) UnsetOrbSpawnDelayMax()`

UnsetOrbSpawnDelayMax ensures that no value is present for OrbSpawnDelayMax, not even an explicit nil
### GetOrbSpawnDelayMin

`func (o *MiscEntity) GetOrbSpawnDelayMin() float64`

GetOrbSpawnDelayMin returns the OrbSpawnDelayMin field if non-nil, zero value otherwise.

### GetOrbSpawnDelayMinOk

`func (o *MiscEntity) GetOrbSpawnDelayMinOk() (*float64, bool)`

GetOrbSpawnDelayMinOk returns a tuple with the OrbSpawnDelayMin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrbSpawnDelayMin

`func (o *MiscEntity) SetOrbSpawnDelayMin(v float64)`

SetOrbSpawnDelayMin sets OrbSpawnDelayMin field to given value.

### HasOrbSpawnDelayMin

`func (o *MiscEntity) HasOrbSpawnDelayMin() bool`

HasOrbSpawnDelayMin returns a boolean if a field has been set.

### SetOrbSpawnDelayMinNil

`func (o *MiscEntity) SetOrbSpawnDelayMinNil(b bool)`

 SetOrbSpawnDelayMinNil sets the value for OrbSpawnDelayMin to be an explicit nil

### UnsetOrbSpawnDelayMin
`func (o *MiscEntity) UnsetOrbSpawnDelayMin()`

UnsetOrbSpawnDelayMin ensures that no value is present for OrbSpawnDelayMin, not even an explicit nil
### GetPickupRadius

`func (o *MiscEntity) GetPickupRadius() CurveOrFloat`

GetPickupRadius returns the PickupRadius field if non-nil, zero value otherwise.

### GetPickupRadiusOk

`func (o *MiscEntity) GetPickupRadiusOk() (*CurveOrFloat, bool)`

GetPickupRadiusOk returns a tuple with the PickupRadius field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPickupRadius

`func (o *MiscEntity) SetPickupRadius(v CurveOrFloat)`

SetPickupRadius sets PickupRadius field to given value.

### HasPickupRadius

`func (o *MiscEntity) HasPickupRadius() bool`

HasPickupRadius returns a boolean if a field has been set.

### SetPickupRadiusNil

`func (o *MiscEntity) SetPickupRadiusNil(b bool)`

 SetPickupRadiusNil sets the value for PickupRadius to be an explicit nil

### UnsetPickupRadius
`func (o *MiscEntity) UnsetPickupRadius()`

UnsetPickupRadius ensures that no value is present for PickupRadius, not even an explicit nil
### GetPrimaryDropChance

`func (o *MiscEntity) GetPrimaryDropChance() float64`

GetPrimaryDropChance returns the PrimaryDropChance field if non-nil, zero value otherwise.

### GetPrimaryDropChanceOk

`func (o *MiscEntity) GetPrimaryDropChanceOk() (*float64, bool)`

GetPrimaryDropChanceOk returns a tuple with the PrimaryDropChance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrimaryDropChance

`func (o *MiscEntity) SetPrimaryDropChance(v float64)`

SetPrimaryDropChance sets PrimaryDropChance field to given value.

### HasPrimaryDropChance

`func (o *MiscEntity) HasPrimaryDropChance() bool`

HasPrimaryDropChance returns a boolean if a field has been set.

### SetPrimaryDropChanceNil

`func (o *MiscEntity) SetPrimaryDropChanceNil(b bool)`

 SetPrimaryDropChanceNil sets the value for PrimaryDropChance to be an explicit nil

### UnsetPrimaryDropChance
`func (o *MiscEntity) UnsetPrimaryDropChance()`

UnsetPrimaryDropChance ensures that no value is present for PrimaryDropChance, not even an explicit nil
### GetPrimaryPickups

`func (o *MiscEntity) GetPrimaryPickups() []Pickup`

GetPrimaryPickups returns the PrimaryPickups field if non-nil, zero value otherwise.

### GetPrimaryPickupsOk

`func (o *MiscEntity) GetPrimaryPickupsOk() (*[]Pickup, bool)`

GetPrimaryPickupsOk returns a tuple with the PrimaryPickups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrimaryPickups

`func (o *MiscEntity) SetPrimaryPickups(v []Pickup)`

SetPrimaryPickups sets PrimaryPickups field to given value.

### HasPrimaryPickups

`func (o *MiscEntity) HasPrimaryPickups() bool`

HasPrimaryPickups returns a boolean if a field has been set.

### SetPrimaryPickupsNil

`func (o *MiscEntity) SetPrimaryPickupsNil(b bool)`

 SetPrimaryPickupsNil sets the value for PrimaryPickups to be an explicit nil

### UnsetPrimaryPickups
`func (o *MiscEntity) UnsetPrimaryPickups()`

UnsetPrimaryPickups ensures that no value is present for PrimaryPickups, not even an explicit nil
### GetRenderAfterDeath

`func (o *MiscEntity) GetRenderAfterDeath() bool`

GetRenderAfterDeath returns the RenderAfterDeath field if non-nil, zero value otherwise.

### GetRenderAfterDeathOk

`func (o *MiscEntity) GetRenderAfterDeathOk() (*bool, bool)`

GetRenderAfterDeathOk returns a tuple with the RenderAfterDeath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRenderAfterDeath

`func (o *MiscEntity) SetRenderAfterDeath(v bool)`

SetRenderAfterDeath sets RenderAfterDeath field to given value.

### HasRenderAfterDeath

`func (o *MiscEntity) HasRenderAfterDeath() bool`

HasRenderAfterDeath returns a boolean if a field has been set.

### SetRenderAfterDeathNil

`func (o *MiscEntity) SetRenderAfterDeathNil(b bool)`

 SetRenderAfterDeathNil sets the value for RenderAfterDeath to be an explicit nil

### UnsetRenderAfterDeath
`func (o *MiscEntity) UnsetRenderAfterDeath()`

UnsetRenderAfterDeath ensures that no value is present for RenderAfterDeath, not even an explicit nil
### GetRespawnTime

`func (o *MiscEntity) GetRespawnTime() float64`

GetRespawnTime returns the RespawnTime field if non-nil, zero value otherwise.

### GetRespawnTimeOk

`func (o *MiscEntity) GetRespawnTimeOk() (*float64, bool)`

GetRespawnTimeOk returns a tuple with the RespawnTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRespawnTime

`func (o *MiscEntity) SetRespawnTime(v float64)`

SetRespawnTime sets RespawnTime field to given value.

### HasRespawnTime

`func (o *MiscEntity) HasRespawnTime() bool`

HasRespawnTime returns a boolean if a field has been set.

### SetRespawnTimeNil

`func (o *MiscEntity) SetRespawnTimeNil(b bool)`

 SetRespawnTimeNil sets the value for RespawnTime to be an explicit nil

### UnsetRespawnTime
`func (o *MiscEntity) UnsetRespawnTime()`

UnsetRespawnTime ensures that no value is present for RespawnTime, not even an explicit nil
### GetRollType

`func (o *MiscEntity) GetRollType() RollType`

GetRollType returns the RollType field if non-nil, zero value otherwise.

### GetRollTypeOk

`func (o *MiscEntity) GetRollTypeOk() (*RollType, bool)`

GetRollTypeOk returns a tuple with the RollType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRollType

`func (o *MiscEntity) SetRollType(v RollType)`

SetRollType sets RollType field to given value.

### HasRollType

`func (o *MiscEntity) HasRollType() bool`

HasRollType returns a boolean if a field has been set.

### SetRollTypeNil

`func (o *MiscEntity) SetRollTypeNil(b bool)`

 SetRollTypeNil sets the value for RollType to be an explicit nil

### UnsetRollType
`func (o *MiscEntity) UnsetRollType()`

UnsetRollType ensures that no value is present for RollType, not even an explicit nil
### GetShowOnMinimap

`func (o *MiscEntity) GetShowOnMinimap() bool`

GetShowOnMinimap returns the ShowOnMinimap field if non-nil, zero value otherwise.

### GetShowOnMinimapOk

`func (o *MiscEntity) GetShowOnMinimapOk() (*bool, bool)`

GetShowOnMinimapOk returns a tuple with the ShowOnMinimap field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShowOnMinimap

`func (o *MiscEntity) SetShowOnMinimap(v bool)`

SetShowOnMinimap sets ShowOnMinimap field to given value.

### HasShowOnMinimap

`func (o *MiscEntity) HasShowOnMinimap() bool`

HasShowOnMinimap returns a boolean if a field has been set.

### SetShowOnMinimapNil

`func (o *MiscEntity) SetShowOnMinimapNil(b bool)`

 SetShowOnMinimapNil sets the value for ShowOnMinimap to be an explicit nil

### UnsetShowOnMinimap
`func (o *MiscEntity) UnsetShowOnMinimap()`

UnsetShowOnMinimap ensures that no value is present for ShowOnMinimap, not even an explicit nil
### GetSolidAfterDeath

`func (o *MiscEntity) GetSolidAfterDeath() bool`

GetSolidAfterDeath returns the SolidAfterDeath field if non-nil, zero value otherwise.

### GetSolidAfterDeathOk

`func (o *MiscEntity) GetSolidAfterDeathOk() (*bool, bool)`

GetSolidAfterDeathOk returns a tuple with the SolidAfterDeath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSolidAfterDeath

`func (o *MiscEntity) SetSolidAfterDeath(v bool)`

SetSolidAfterDeath sets SolidAfterDeath field to given value.

### HasSolidAfterDeath

`func (o *MiscEntity) HasSolidAfterDeath() bool`

HasSolidAfterDeath returns a boolean if a field has been set.

### SetSolidAfterDeathNil

`func (o *MiscEntity) SetSolidAfterDeathNil(b bool)`

 SetSolidAfterDeathNil sets the value for SolidAfterDeath to be an explicit nil

### UnsetSolidAfterDeath
`func (o *MiscEntity) UnsetSolidAfterDeath()`

UnsetSolidAfterDeath ensures that no value is present for SolidAfterDeath, not even an explicit nil
### GetSpawnInterval

`func (o *MiscEntity) GetSpawnInterval() float64`

GetSpawnInterval returns the SpawnInterval field if non-nil, zero value otherwise.

### GetSpawnIntervalOk

`func (o *MiscEntity) GetSpawnIntervalOk() (*float64, bool)`

GetSpawnIntervalOk returns a tuple with the SpawnInterval field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpawnInterval

`func (o *MiscEntity) SetSpawnInterval(v float64)`

SetSpawnInterval sets SpawnInterval field to given value.

### HasSpawnInterval

`func (o *MiscEntity) HasSpawnInterval() bool`

HasSpawnInterval returns a boolean if a field has been set.

### SetSpawnIntervalNil

`func (o *MiscEntity) SetSpawnIntervalNil(b bool)`

 SetSpawnIntervalNil sets the value for SpawnInterval to be an explicit nil

### UnsetSpawnInterval
`func (o *MiscEntity) UnsetSpawnInterval()`

UnsetSpawnInterval ensures that no value is present for SpawnInterval, not even an explicit nil
### GetSpawnIntervalInSeconds

`func (o *MiscEntity) GetSpawnIntervalInSeconds() int64`

GetSpawnIntervalInSeconds returns the SpawnIntervalInSeconds field if non-nil, zero value otherwise.

### GetSpawnIntervalInSecondsOk

`func (o *MiscEntity) GetSpawnIntervalInSecondsOk() (*int64, bool)`

GetSpawnIntervalInSecondsOk returns a tuple with the SpawnIntervalInSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpawnIntervalInSeconds

`func (o *MiscEntity) SetSpawnIntervalInSeconds(v int64)`

SetSpawnIntervalInSeconds sets SpawnIntervalInSeconds field to given value.

### HasSpawnIntervalInSeconds

`func (o *MiscEntity) HasSpawnIntervalInSeconds() bool`

HasSpawnIntervalInSeconds returns a boolean if a field has been set.

### SetSpawnIntervalInSecondsNil

`func (o *MiscEntity) SetSpawnIntervalInSecondsNil(b bool)`

 SetSpawnIntervalInSecondsNil sets the value for SpawnIntervalInSeconds to be an explicit nil

### UnsetSpawnIntervalInSeconds
`func (o *MiscEntity) UnsetSpawnIntervalInSeconds()`

UnsetSpawnIntervalInSeconds ensures that no value is present for SpawnIntervalInSeconds, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


