# MiscEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BreakOnDodgeTouch** | Pointer to **NullableBool** |  | [optional] 
**BuffTypeGraphColor** | Pointer to [**NullableColor**](Color.md) | Permanent pickups: color used for the buff in the stat graph. | [optional] 
**BuffTypeLocString** | Pointer to **NullableString** | Permanent pickups: localization token of the stat the buff raises. | [optional] 
**BuffTypeName** | Pointer to **NullableString** | Permanent pickups: &#x60;buff_type_loc_string&#x60; localized into the requested language (e.g. &#x60;Fire Rate&#x60;). | [optional] 
**BuffTypeValueUnit** | Pointer to **NullableString** | Permanent pickups: unit of the buff value (e.g. &#x60;Percent&#x60;, &#x60;Meters&#x60;). The modifier value itself is in game units (&#x60;Meters&#x60; values are inches, 39.37 per meter). | [optional] 
**ClassName** | **string** |  | 
**CollectionMethod** | Pointer to **NullableString** | How the pickup is collected, e.g. &#x60;Punch&#x60; or &#x60;VacuumTrigger&#x60;. | [optional] 
**CollisionRadius** | Pointer to **NullableFloat64** |  | [optional] 
**Color** | Pointer to [**NullableColor**](Color.md) |  | [optional] 
**DamagedByAbilities** | Pointer to **NullableBool** |  | [optional] 
**DamagedByBullets** | Pointer to **NullableBool** |  | [optional] 
**DamagedByMelee** | Pointer to **NullableBool** |  | [optional] 
**DamagedBySlide** | Pointer to **NullableBool** |  | [optional] 
**ExpirationDuration** | Pointer to [**NullableCurveOrFloat**](CurveOrFloat.md) |  | [optional] 
**GoldAmount** | Pointer to **NullableFloat64** |  | [optional] 
**GoldPerMinuteAmount** | Pointer to **NullableFloat64** |  | [optional] 
**Health** | Pointer to **NullableInt64** |  | [optional] 
**HeavyMeleeHitCount** | Pointer to **NullableInt64** |  | [optional] 
**HeavyMeleeOnly** | Pointer to **NullableBool** |  | [optional] 
**HitsRequired** | Pointer to **NullableInt64** | Punchable pickups: hits needed to collect. | [optional] 
**Id** | **int32** |  | 
**InShopModifier** | Pointer to [**NullableSubclassModifierDefinition**](SubclassModifierDefinition.md) | Corrupted item shop (Broker) trigger: modifier applied while inside. | [optional] 
**InitialSpawnDelayInSeconds** | Pointer to **NullableInt64** |  | [optional] 
**InitialSpawnDelaySeconds** | Pointer to **NullableInt64** | Duplicate of &#x60;initial_spawn_delay_in_seconds&#x60; for shape parity. | [optional] 
**InitialSpawnTime** | Pointer to **NullableFloat64** |  | [optional] 
**IsMantleable** | Pointer to **NullableBool** |  | [optional] 
**IsPermanentPickup** | Pointer to **NullableBool** |  | [optional] 
**Lifetime** | Pointer to **NullableFloat64** |  | [optional] 
**LootListDeckSize** | Pointer to **NullableInt64** |  | [optional] 
**MVecPickupsLv2** | Pointer to [**[]Pickup**](Pickup.md) |  | [optional] 
**MVecPickupsLv3** | Pointer to [**[]Pickup**](Pickup.md) |  | [optional] 
**MatchTimeMinsForLevel2Pickups** | Pointer to **NullableInt64** |  | [optional] 
**MatchTimeMinsForLevel3Pickups** | Pointer to **NullableInt64** |  | [optional] 
**MinimapClass** | Pointer to **NullableString** |  | [optional] 
**Modifier** | Pointer to [**NullableSubclassModifierDefinition**](SubclassModifierDefinition.md) |  | [optional] 
**Name** | Pointer to **NullableString** | &#x60;name_loc_string&#x60; localized into the requested language (e.g. &#x60;+1.5% Fire Rate&#x60;). Gold pickups use an ICU plural pattern (&#x60;{amount, plural, one{Soul} other{Souls}}&#x60;). | [optional] 
**NameLocString** | Pointer to **NullableString** | Localization token of the pickup&#39;s world label. | [optional] 
**OrbSpawnDelayMax** | Pointer to **NullableFloat64** |  | [optional] 
**OrbSpawnDelayMin** | Pointer to **NullableFloat64** |  | [optional] 
**Pickup** | Pointer to **NullableString** | Pickup spawners: class name of the spawned pickup. | [optional] 
**PickupChances** | Pointer to **map[string]float64** | Pickup name to relative weight (build 6711+); replaces the &#x60;primary_pickups&#x60; / &#x60;m_vecPickups_lv*&#x60; lists. | [optional] 
**PickupRadius** | Pointer to [**NullableCurveOrFloat**](CurveOrFloat.md) |  | [optional] 
**PowerupDropChance** | Pointer to **NullableFloat64** | Drop chance (percent) for build 6711+; replaces &#x60;primary_drop_chance&#x60;. | [optional] 
**PrimaryDropChance** | Pointer to **NullableFloat64** | Pre-6711 builds only; see &#x60;powerup_drop_chance&#x60;. | [optional] 
**PrimaryPickups** | Pointer to [**[]Pickup**](Pickup.md) |  | [optional] 
**RegenDuration** | Pointer to **NullableFloat64** | Health pickups: seconds over which the healing is applied to heroes. | [optional] 
**RegenDurationTroopers** | Pointer to **NullableFloat64** | Health pickups: seconds over which the healing is applied to troopers. | [optional] 
**RegenMaxHealthPercent** | Pointer to [**NullableCurveOrFloat**](CurveOrFloat.md) | Health pickups: healing as percent of max health. | [optional] 
**RegenTrooperMulti** | Pointer to **NullableFloat64** | Health pickups: healing multiplier for troopers. | [optional] 
**RenderAfterDeath** | Pointer to **NullableBool** |  | [optional] 
**RespawnTime** | Pointer to **NullableFloat64** |  | [optional] 
**RollType** | Pointer to **NullableString** | Known values for &#x60;m_eRollType&#x60;. Unknown values pass through unchanged so a newly-introduced roll type doesn&#39;t 500. Known values: &#x60;ECitadelRandomRoll_BreakablePowerupPickup&#x60;, &#x60;ECitadelRandomRoll_BreakableGoldPickup&#x60;. | [optional] 
**ShowOnMinimap** | Pointer to **NullableBool** |  | [optional] 
**SinglePickupOverride** | Pointer to **NullableString** | Powerup spawners: class name of the only pickup spawned, overriding &#x60;pickup_chances&#x60;. | [optional] 
**SolidAfterDeath** | Pointer to **NullableBool** |  | [optional] 
**SpawnDelay** | Pointer to **NullableFloat64** | Pickup spawners: delay (seconds) before the first spawn. | [optional] 
**SpawnInterval** | Pointer to **NullableFloat64** |  | [optional] 
**SpawnIntervalInSeconds** | Pointer to **NullableInt64** |  | [optional] 
**SpawnMusicState** | Pointer to **NullableString** | Corrupted item shop (Broker) trigger: music cue played on spawn. | [optional] 

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
### GetBuffTypeGraphColor

`func (o *MiscEntity) GetBuffTypeGraphColor() Color`

GetBuffTypeGraphColor returns the BuffTypeGraphColor field if non-nil, zero value otherwise.

### GetBuffTypeGraphColorOk

`func (o *MiscEntity) GetBuffTypeGraphColorOk() (*Color, bool)`

GetBuffTypeGraphColorOk returns a tuple with the BuffTypeGraphColor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuffTypeGraphColor

`func (o *MiscEntity) SetBuffTypeGraphColor(v Color)`

SetBuffTypeGraphColor sets BuffTypeGraphColor field to given value.

### HasBuffTypeGraphColor

`func (o *MiscEntity) HasBuffTypeGraphColor() bool`

HasBuffTypeGraphColor returns a boolean if a field has been set.

### SetBuffTypeGraphColorNil

`func (o *MiscEntity) SetBuffTypeGraphColorNil(b bool)`

 SetBuffTypeGraphColorNil sets the value for BuffTypeGraphColor to be an explicit nil

### UnsetBuffTypeGraphColor
`func (o *MiscEntity) UnsetBuffTypeGraphColor()`

UnsetBuffTypeGraphColor ensures that no value is present for BuffTypeGraphColor, not even an explicit nil
### GetBuffTypeLocString

`func (o *MiscEntity) GetBuffTypeLocString() string`

GetBuffTypeLocString returns the BuffTypeLocString field if non-nil, zero value otherwise.

### GetBuffTypeLocStringOk

`func (o *MiscEntity) GetBuffTypeLocStringOk() (*string, bool)`

GetBuffTypeLocStringOk returns a tuple with the BuffTypeLocString field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuffTypeLocString

`func (o *MiscEntity) SetBuffTypeLocString(v string)`

SetBuffTypeLocString sets BuffTypeLocString field to given value.

### HasBuffTypeLocString

`func (o *MiscEntity) HasBuffTypeLocString() bool`

HasBuffTypeLocString returns a boolean if a field has been set.

### SetBuffTypeLocStringNil

`func (o *MiscEntity) SetBuffTypeLocStringNil(b bool)`

 SetBuffTypeLocStringNil sets the value for BuffTypeLocString to be an explicit nil

### UnsetBuffTypeLocString
`func (o *MiscEntity) UnsetBuffTypeLocString()`

UnsetBuffTypeLocString ensures that no value is present for BuffTypeLocString, not even an explicit nil
### GetBuffTypeName

`func (o *MiscEntity) GetBuffTypeName() string`

GetBuffTypeName returns the BuffTypeName field if non-nil, zero value otherwise.

### GetBuffTypeNameOk

`func (o *MiscEntity) GetBuffTypeNameOk() (*string, bool)`

GetBuffTypeNameOk returns a tuple with the BuffTypeName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuffTypeName

`func (o *MiscEntity) SetBuffTypeName(v string)`

SetBuffTypeName sets BuffTypeName field to given value.

### HasBuffTypeName

`func (o *MiscEntity) HasBuffTypeName() bool`

HasBuffTypeName returns a boolean if a field has been set.

### SetBuffTypeNameNil

`func (o *MiscEntity) SetBuffTypeNameNil(b bool)`

 SetBuffTypeNameNil sets the value for BuffTypeName to be an explicit nil

### UnsetBuffTypeName
`func (o *MiscEntity) UnsetBuffTypeName()`

UnsetBuffTypeName ensures that no value is present for BuffTypeName, not even an explicit nil
### GetBuffTypeValueUnit

`func (o *MiscEntity) GetBuffTypeValueUnit() string`

GetBuffTypeValueUnit returns the BuffTypeValueUnit field if non-nil, zero value otherwise.

### GetBuffTypeValueUnitOk

`func (o *MiscEntity) GetBuffTypeValueUnitOk() (*string, bool)`

GetBuffTypeValueUnitOk returns a tuple with the BuffTypeValueUnit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuffTypeValueUnit

`func (o *MiscEntity) SetBuffTypeValueUnit(v string)`

SetBuffTypeValueUnit sets BuffTypeValueUnit field to given value.

### HasBuffTypeValueUnit

`func (o *MiscEntity) HasBuffTypeValueUnit() bool`

HasBuffTypeValueUnit returns a boolean if a field has been set.

### SetBuffTypeValueUnitNil

`func (o *MiscEntity) SetBuffTypeValueUnitNil(b bool)`

 SetBuffTypeValueUnitNil sets the value for BuffTypeValueUnit to be an explicit nil

### UnsetBuffTypeValueUnit
`func (o *MiscEntity) UnsetBuffTypeValueUnit()`

UnsetBuffTypeValueUnit ensures that no value is present for BuffTypeValueUnit, not even an explicit nil
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


### GetCollectionMethod

`func (o *MiscEntity) GetCollectionMethod() string`

GetCollectionMethod returns the CollectionMethod field if non-nil, zero value otherwise.

### GetCollectionMethodOk

`func (o *MiscEntity) GetCollectionMethodOk() (*string, bool)`

GetCollectionMethodOk returns a tuple with the CollectionMethod field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCollectionMethod

`func (o *MiscEntity) SetCollectionMethod(v string)`

SetCollectionMethod sets CollectionMethod field to given value.

### HasCollectionMethod

`func (o *MiscEntity) HasCollectionMethod() bool`

HasCollectionMethod returns a boolean if a field has been set.

### SetCollectionMethodNil

`func (o *MiscEntity) SetCollectionMethodNil(b bool)`

 SetCollectionMethodNil sets the value for CollectionMethod to be an explicit nil

### UnsetCollectionMethod
`func (o *MiscEntity) UnsetCollectionMethod()`

UnsetCollectionMethod ensures that no value is present for CollectionMethod, not even an explicit nil
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
### GetDamagedBySlide

`func (o *MiscEntity) GetDamagedBySlide() bool`

GetDamagedBySlide returns the DamagedBySlide field if non-nil, zero value otherwise.

### GetDamagedBySlideOk

`func (o *MiscEntity) GetDamagedBySlideOk() (*bool, bool)`

GetDamagedBySlideOk returns a tuple with the DamagedBySlide field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamagedBySlide

`func (o *MiscEntity) SetDamagedBySlide(v bool)`

SetDamagedBySlide sets DamagedBySlide field to given value.

### HasDamagedBySlide

`func (o *MiscEntity) HasDamagedBySlide() bool`

HasDamagedBySlide returns a boolean if a field has been set.

### SetDamagedBySlideNil

`func (o *MiscEntity) SetDamagedBySlideNil(b bool)`

 SetDamagedBySlideNil sets the value for DamagedBySlide to be an explicit nil

### UnsetDamagedBySlide
`func (o *MiscEntity) UnsetDamagedBySlide()`

UnsetDamagedBySlide ensures that no value is present for DamagedBySlide, not even an explicit nil
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
### GetHeavyMeleeHitCount

`func (o *MiscEntity) GetHeavyMeleeHitCount() int64`

GetHeavyMeleeHitCount returns the HeavyMeleeHitCount field if non-nil, zero value otherwise.

### GetHeavyMeleeHitCountOk

`func (o *MiscEntity) GetHeavyMeleeHitCountOk() (*int64, bool)`

GetHeavyMeleeHitCountOk returns a tuple with the HeavyMeleeHitCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeavyMeleeHitCount

`func (o *MiscEntity) SetHeavyMeleeHitCount(v int64)`

SetHeavyMeleeHitCount sets HeavyMeleeHitCount field to given value.

### HasHeavyMeleeHitCount

`func (o *MiscEntity) HasHeavyMeleeHitCount() bool`

HasHeavyMeleeHitCount returns a boolean if a field has been set.

### SetHeavyMeleeHitCountNil

`func (o *MiscEntity) SetHeavyMeleeHitCountNil(b bool)`

 SetHeavyMeleeHitCountNil sets the value for HeavyMeleeHitCount to be an explicit nil

### UnsetHeavyMeleeHitCount
`func (o *MiscEntity) UnsetHeavyMeleeHitCount()`

UnsetHeavyMeleeHitCount ensures that no value is present for HeavyMeleeHitCount, not even an explicit nil
### GetHeavyMeleeOnly

`func (o *MiscEntity) GetHeavyMeleeOnly() bool`

GetHeavyMeleeOnly returns the HeavyMeleeOnly field if non-nil, zero value otherwise.

### GetHeavyMeleeOnlyOk

`func (o *MiscEntity) GetHeavyMeleeOnlyOk() (*bool, bool)`

GetHeavyMeleeOnlyOk returns a tuple with the HeavyMeleeOnly field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeavyMeleeOnly

`func (o *MiscEntity) SetHeavyMeleeOnly(v bool)`

SetHeavyMeleeOnly sets HeavyMeleeOnly field to given value.

### HasHeavyMeleeOnly

`func (o *MiscEntity) HasHeavyMeleeOnly() bool`

HasHeavyMeleeOnly returns a boolean if a field has been set.

### SetHeavyMeleeOnlyNil

`func (o *MiscEntity) SetHeavyMeleeOnlyNil(b bool)`

 SetHeavyMeleeOnlyNil sets the value for HeavyMeleeOnly to be an explicit nil

### UnsetHeavyMeleeOnly
`func (o *MiscEntity) UnsetHeavyMeleeOnly()`

UnsetHeavyMeleeOnly ensures that no value is present for HeavyMeleeOnly, not even an explicit nil
### GetHitsRequired

`func (o *MiscEntity) GetHitsRequired() int64`

GetHitsRequired returns the HitsRequired field if non-nil, zero value otherwise.

### GetHitsRequiredOk

`func (o *MiscEntity) GetHitsRequiredOk() (*int64, bool)`

GetHitsRequiredOk returns a tuple with the HitsRequired field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHitsRequired

`func (o *MiscEntity) SetHitsRequired(v int64)`

SetHitsRequired sets HitsRequired field to given value.

### HasHitsRequired

`func (o *MiscEntity) HasHitsRequired() bool`

HasHitsRequired returns a boolean if a field has been set.

### SetHitsRequiredNil

`func (o *MiscEntity) SetHitsRequiredNil(b bool)`

 SetHitsRequiredNil sets the value for HitsRequired to be an explicit nil

### UnsetHitsRequired
`func (o *MiscEntity) UnsetHitsRequired()`

UnsetHitsRequired ensures that no value is present for HitsRequired, not even an explicit nil
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


### GetInShopModifier

`func (o *MiscEntity) GetInShopModifier() SubclassModifierDefinition`

GetInShopModifier returns the InShopModifier field if non-nil, zero value otherwise.

### GetInShopModifierOk

`func (o *MiscEntity) GetInShopModifierOk() (*SubclassModifierDefinition, bool)`

GetInShopModifierOk returns a tuple with the InShopModifier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInShopModifier

`func (o *MiscEntity) SetInShopModifier(v SubclassModifierDefinition)`

SetInShopModifier sets InShopModifier field to given value.

### HasInShopModifier

`func (o *MiscEntity) HasInShopModifier() bool`

HasInShopModifier returns a boolean if a field has been set.

### SetInShopModifierNil

`func (o *MiscEntity) SetInShopModifierNil(b bool)`

 SetInShopModifierNil sets the value for InShopModifier to be an explicit nil

### UnsetInShopModifier
`func (o *MiscEntity) UnsetInShopModifier()`

UnsetInShopModifier ensures that no value is present for InShopModifier, not even an explicit nil
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
### GetIsPermanentPickup

`func (o *MiscEntity) GetIsPermanentPickup() bool`

GetIsPermanentPickup returns the IsPermanentPickup field if non-nil, zero value otherwise.

### GetIsPermanentPickupOk

`func (o *MiscEntity) GetIsPermanentPickupOk() (*bool, bool)`

GetIsPermanentPickupOk returns a tuple with the IsPermanentPickup field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsPermanentPickup

`func (o *MiscEntity) SetIsPermanentPickup(v bool)`

SetIsPermanentPickup sets IsPermanentPickup field to given value.

### HasIsPermanentPickup

`func (o *MiscEntity) HasIsPermanentPickup() bool`

HasIsPermanentPickup returns a boolean if a field has been set.

### SetIsPermanentPickupNil

`func (o *MiscEntity) SetIsPermanentPickupNil(b bool)`

 SetIsPermanentPickupNil sets the value for IsPermanentPickup to be an explicit nil

### UnsetIsPermanentPickup
`func (o *MiscEntity) UnsetIsPermanentPickup()`

UnsetIsPermanentPickup ensures that no value is present for IsPermanentPickup, not even an explicit nil
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
### GetMinimapClass

`func (o *MiscEntity) GetMinimapClass() string`

GetMinimapClass returns the MinimapClass field if non-nil, zero value otherwise.

### GetMinimapClassOk

`func (o *MiscEntity) GetMinimapClassOk() (*string, bool)`

GetMinimapClassOk returns a tuple with the MinimapClass field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMinimapClass

`func (o *MiscEntity) SetMinimapClass(v string)`

SetMinimapClass sets MinimapClass field to given value.

### HasMinimapClass

`func (o *MiscEntity) HasMinimapClass() bool`

HasMinimapClass returns a boolean if a field has been set.

### SetMinimapClassNil

`func (o *MiscEntity) SetMinimapClassNil(b bool)`

 SetMinimapClassNil sets the value for MinimapClass to be an explicit nil

### UnsetMinimapClass
`func (o *MiscEntity) UnsetMinimapClass()`

UnsetMinimapClass ensures that no value is present for MinimapClass, not even an explicit nil
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
### GetName

`func (o *MiscEntity) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *MiscEntity) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *MiscEntity) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *MiscEntity) HasName() bool`

HasName returns a boolean if a field has been set.

### SetNameNil

`func (o *MiscEntity) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *MiscEntity) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil
### GetNameLocString

`func (o *MiscEntity) GetNameLocString() string`

GetNameLocString returns the NameLocString field if non-nil, zero value otherwise.

### GetNameLocStringOk

`func (o *MiscEntity) GetNameLocStringOk() (*string, bool)`

GetNameLocStringOk returns a tuple with the NameLocString field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNameLocString

`func (o *MiscEntity) SetNameLocString(v string)`

SetNameLocString sets NameLocString field to given value.

### HasNameLocString

`func (o *MiscEntity) HasNameLocString() bool`

HasNameLocString returns a boolean if a field has been set.

### SetNameLocStringNil

`func (o *MiscEntity) SetNameLocStringNil(b bool)`

 SetNameLocStringNil sets the value for NameLocString to be an explicit nil

### UnsetNameLocString
`func (o *MiscEntity) UnsetNameLocString()`

UnsetNameLocString ensures that no value is present for NameLocString, not even an explicit nil
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
### GetPickup

`func (o *MiscEntity) GetPickup() string`

GetPickup returns the Pickup field if non-nil, zero value otherwise.

### GetPickupOk

`func (o *MiscEntity) GetPickupOk() (*string, bool)`

GetPickupOk returns a tuple with the Pickup field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPickup

`func (o *MiscEntity) SetPickup(v string)`

SetPickup sets Pickup field to given value.

### HasPickup

`func (o *MiscEntity) HasPickup() bool`

HasPickup returns a boolean if a field has been set.

### SetPickupNil

`func (o *MiscEntity) SetPickupNil(b bool)`

 SetPickupNil sets the value for Pickup to be an explicit nil

### UnsetPickup
`func (o *MiscEntity) UnsetPickup()`

UnsetPickup ensures that no value is present for Pickup, not even an explicit nil
### GetPickupChances

`func (o *MiscEntity) GetPickupChances() map[string]float64`

GetPickupChances returns the PickupChances field if non-nil, zero value otherwise.

### GetPickupChancesOk

`func (o *MiscEntity) GetPickupChancesOk() (*map[string]float64, bool)`

GetPickupChancesOk returns a tuple with the PickupChances field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPickupChances

`func (o *MiscEntity) SetPickupChances(v map[string]float64)`

SetPickupChances sets PickupChances field to given value.

### HasPickupChances

`func (o *MiscEntity) HasPickupChances() bool`

HasPickupChances returns a boolean if a field has been set.

### SetPickupChancesNil

`func (o *MiscEntity) SetPickupChancesNil(b bool)`

 SetPickupChancesNil sets the value for PickupChances to be an explicit nil

### UnsetPickupChances
`func (o *MiscEntity) UnsetPickupChances()`

UnsetPickupChances ensures that no value is present for PickupChances, not even an explicit nil
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
### GetPowerupDropChance

`func (o *MiscEntity) GetPowerupDropChance() float64`

GetPowerupDropChance returns the PowerupDropChance field if non-nil, zero value otherwise.

### GetPowerupDropChanceOk

`func (o *MiscEntity) GetPowerupDropChanceOk() (*float64, bool)`

GetPowerupDropChanceOk returns a tuple with the PowerupDropChance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPowerupDropChance

`func (o *MiscEntity) SetPowerupDropChance(v float64)`

SetPowerupDropChance sets PowerupDropChance field to given value.

### HasPowerupDropChance

`func (o *MiscEntity) HasPowerupDropChance() bool`

HasPowerupDropChance returns a boolean if a field has been set.

### SetPowerupDropChanceNil

`func (o *MiscEntity) SetPowerupDropChanceNil(b bool)`

 SetPowerupDropChanceNil sets the value for PowerupDropChance to be an explicit nil

### UnsetPowerupDropChance
`func (o *MiscEntity) UnsetPowerupDropChance()`

UnsetPowerupDropChance ensures that no value is present for PowerupDropChance, not even an explicit nil
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
### GetRegenDuration

`func (o *MiscEntity) GetRegenDuration() float64`

GetRegenDuration returns the RegenDuration field if non-nil, zero value otherwise.

### GetRegenDurationOk

`func (o *MiscEntity) GetRegenDurationOk() (*float64, bool)`

GetRegenDurationOk returns a tuple with the RegenDuration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegenDuration

`func (o *MiscEntity) SetRegenDuration(v float64)`

SetRegenDuration sets RegenDuration field to given value.

### HasRegenDuration

`func (o *MiscEntity) HasRegenDuration() bool`

HasRegenDuration returns a boolean if a field has been set.

### SetRegenDurationNil

`func (o *MiscEntity) SetRegenDurationNil(b bool)`

 SetRegenDurationNil sets the value for RegenDuration to be an explicit nil

### UnsetRegenDuration
`func (o *MiscEntity) UnsetRegenDuration()`

UnsetRegenDuration ensures that no value is present for RegenDuration, not even an explicit nil
### GetRegenDurationTroopers

`func (o *MiscEntity) GetRegenDurationTroopers() float64`

GetRegenDurationTroopers returns the RegenDurationTroopers field if non-nil, zero value otherwise.

### GetRegenDurationTroopersOk

`func (o *MiscEntity) GetRegenDurationTroopersOk() (*float64, bool)`

GetRegenDurationTroopersOk returns a tuple with the RegenDurationTroopers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegenDurationTroopers

`func (o *MiscEntity) SetRegenDurationTroopers(v float64)`

SetRegenDurationTroopers sets RegenDurationTroopers field to given value.

### HasRegenDurationTroopers

`func (o *MiscEntity) HasRegenDurationTroopers() bool`

HasRegenDurationTroopers returns a boolean if a field has been set.

### SetRegenDurationTroopersNil

`func (o *MiscEntity) SetRegenDurationTroopersNil(b bool)`

 SetRegenDurationTroopersNil sets the value for RegenDurationTroopers to be an explicit nil

### UnsetRegenDurationTroopers
`func (o *MiscEntity) UnsetRegenDurationTroopers()`

UnsetRegenDurationTroopers ensures that no value is present for RegenDurationTroopers, not even an explicit nil
### GetRegenMaxHealthPercent

`func (o *MiscEntity) GetRegenMaxHealthPercent() CurveOrFloat`

GetRegenMaxHealthPercent returns the RegenMaxHealthPercent field if non-nil, zero value otherwise.

### GetRegenMaxHealthPercentOk

`func (o *MiscEntity) GetRegenMaxHealthPercentOk() (*CurveOrFloat, bool)`

GetRegenMaxHealthPercentOk returns a tuple with the RegenMaxHealthPercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegenMaxHealthPercent

`func (o *MiscEntity) SetRegenMaxHealthPercent(v CurveOrFloat)`

SetRegenMaxHealthPercent sets RegenMaxHealthPercent field to given value.

### HasRegenMaxHealthPercent

`func (o *MiscEntity) HasRegenMaxHealthPercent() bool`

HasRegenMaxHealthPercent returns a boolean if a field has been set.

### SetRegenMaxHealthPercentNil

`func (o *MiscEntity) SetRegenMaxHealthPercentNil(b bool)`

 SetRegenMaxHealthPercentNil sets the value for RegenMaxHealthPercent to be an explicit nil

### UnsetRegenMaxHealthPercent
`func (o *MiscEntity) UnsetRegenMaxHealthPercent()`

UnsetRegenMaxHealthPercent ensures that no value is present for RegenMaxHealthPercent, not even an explicit nil
### GetRegenTrooperMulti

`func (o *MiscEntity) GetRegenTrooperMulti() float64`

GetRegenTrooperMulti returns the RegenTrooperMulti field if non-nil, zero value otherwise.

### GetRegenTrooperMultiOk

`func (o *MiscEntity) GetRegenTrooperMultiOk() (*float64, bool)`

GetRegenTrooperMultiOk returns a tuple with the RegenTrooperMulti field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegenTrooperMulti

`func (o *MiscEntity) SetRegenTrooperMulti(v float64)`

SetRegenTrooperMulti sets RegenTrooperMulti field to given value.

### HasRegenTrooperMulti

`func (o *MiscEntity) HasRegenTrooperMulti() bool`

HasRegenTrooperMulti returns a boolean if a field has been set.

### SetRegenTrooperMultiNil

`func (o *MiscEntity) SetRegenTrooperMultiNil(b bool)`

 SetRegenTrooperMultiNil sets the value for RegenTrooperMulti to be an explicit nil

### UnsetRegenTrooperMulti
`func (o *MiscEntity) UnsetRegenTrooperMulti()`

UnsetRegenTrooperMulti ensures that no value is present for RegenTrooperMulti, not even an explicit nil
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

`func (o *MiscEntity) GetRollType() string`

GetRollType returns the RollType field if non-nil, zero value otherwise.

### GetRollTypeOk

`func (o *MiscEntity) GetRollTypeOk() (*string, bool)`

GetRollTypeOk returns a tuple with the RollType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRollType

`func (o *MiscEntity) SetRollType(v string)`

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
### GetSinglePickupOverride

`func (o *MiscEntity) GetSinglePickupOverride() string`

GetSinglePickupOverride returns the SinglePickupOverride field if non-nil, zero value otherwise.

### GetSinglePickupOverrideOk

`func (o *MiscEntity) GetSinglePickupOverrideOk() (*string, bool)`

GetSinglePickupOverrideOk returns a tuple with the SinglePickupOverride field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSinglePickupOverride

`func (o *MiscEntity) SetSinglePickupOverride(v string)`

SetSinglePickupOverride sets SinglePickupOverride field to given value.

### HasSinglePickupOverride

`func (o *MiscEntity) HasSinglePickupOverride() bool`

HasSinglePickupOverride returns a boolean if a field has been set.

### SetSinglePickupOverrideNil

`func (o *MiscEntity) SetSinglePickupOverrideNil(b bool)`

 SetSinglePickupOverrideNil sets the value for SinglePickupOverride to be an explicit nil

### UnsetSinglePickupOverride
`func (o *MiscEntity) UnsetSinglePickupOverride()`

UnsetSinglePickupOverride ensures that no value is present for SinglePickupOverride, not even an explicit nil
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
### GetSpawnDelay

`func (o *MiscEntity) GetSpawnDelay() float64`

GetSpawnDelay returns the SpawnDelay field if non-nil, zero value otherwise.

### GetSpawnDelayOk

`func (o *MiscEntity) GetSpawnDelayOk() (*float64, bool)`

GetSpawnDelayOk returns a tuple with the SpawnDelay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpawnDelay

`func (o *MiscEntity) SetSpawnDelay(v float64)`

SetSpawnDelay sets SpawnDelay field to given value.

### HasSpawnDelay

`func (o *MiscEntity) HasSpawnDelay() bool`

HasSpawnDelay returns a boolean if a field has been set.

### SetSpawnDelayNil

`func (o *MiscEntity) SetSpawnDelayNil(b bool)`

 SetSpawnDelayNil sets the value for SpawnDelay to be an explicit nil

### UnsetSpawnDelay
`func (o *MiscEntity) UnsetSpawnDelay()`

UnsetSpawnDelay ensures that no value is present for SpawnDelay, not even an explicit nil
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
### GetSpawnMusicState

`func (o *MiscEntity) GetSpawnMusicState() string`

GetSpawnMusicState returns the SpawnMusicState field if non-nil, zero value otherwise.

### GetSpawnMusicStateOk

`func (o *MiscEntity) GetSpawnMusicStateOk() (*string, bool)`

GetSpawnMusicStateOk returns a tuple with the SpawnMusicState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpawnMusicState

`func (o *MiscEntity) SetSpawnMusicState(v string)`

SetSpawnMusicState sets SpawnMusicState field to given value.

### HasSpawnMusicState

`func (o *MiscEntity) HasSpawnMusicState() bool`

HasSpawnMusicState returns a boolean if a field has been set.

### SetSpawnMusicStateNil

`func (o *MiscEntity) SetSpawnMusicStateNil(b bool)`

 SetSpawnMusicStateNil sets the value for SpawnMusicState to be an explicit nil

### UnsetSpawnMusicState
`func (o *MiscEntity) UnsetSpawnMusicState()`

UnsetSpawnMusicState ensures that no value is present for SpawnMusicState, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


