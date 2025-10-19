# RawWeaponInfoV2Input

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MBCanZoom** | Pointer to **NullableBool** |  | [optional] 
**MFlBulletDamage** | Pointer to **NullableFloat32** |  | [optional] 
**MFlBulletGravityScale** | Pointer to **NullableFloat32** |  | [optional] 
**MFlBulletInheritShooterVelocityScale** | Pointer to **NullableFloat32** |  | [optional] 
**MFlBulletLifetime** | Pointer to **NullableFloat32** |  | [optional] 
**MFlBulletRadius** | Pointer to **NullableFloat32** |  | [optional] 
**MFlBulletRadiusVsWorld** | Pointer to **NullableFloat32** |  | [optional] 
**MFlBulletReflectAmount** | Pointer to **NullableFloat32** |  | [optional] 
**MFlBulletReflectScale** | Pointer to **NullableFloat32** |  | [optional] 
**MFlBulletWhizDistance** | Pointer to **NullableFloat32** |  | [optional] 
**MFlBurstShotCooldown** | Pointer to **NullableFloat32** |  | [optional] 
**MFlCritBonusAgainstNpcs** | Pointer to **NullableFloat32** |  | [optional] 
**MFlCritBonusEnd** | Pointer to **NullableFloat32** |  | [optional] 
**MFlCritBonusEndRange** | Pointer to **NullableFloat32** |  | [optional] 
**MFlCritBonusStart** | Pointer to **NullableFloat32** |  | [optional] 
**MFlCritBonusStartRange** | Pointer to **NullableFloat32** |  | [optional] 
**MFlCycleTime** | Pointer to **NullableFloat32** |  | [optional] 
**MFlIntraBurstCycleTime** | Pointer to **NullableFloat32** |  | [optional] 
**MFlMaxSpinCycleTime** | Pointer to **NullableFloat32** |  | [optional] 
**MFlDamageFalloffBias** | Pointer to **NullableFloat32** |  | [optional] 
**MFlDamageFalloffEndRange** | Pointer to **NullableFloat32** |  | [optional] 
**MFlDamageFalloffEndScale** | Pointer to **NullableFloat32** |  | [optional] 
**MFlDamageFalloffStartRange** | Pointer to **NullableFloat32** |  | [optional] 
**MFlDamageFalloffStartScale** | Pointer to **NullableFloat32** |  | [optional] 
**MFlHorizontalPunch** | Pointer to **NullableFloat32** |  | [optional] 
**MFlRange** | Pointer to **NullableFloat32** |  | [optional] 
**MFlRecoilRecoveryDelayFactor** | Pointer to **NullableFloat32** |  | [optional] 
**MFlRecoilRecoverySpeed** | Pointer to **NullableFloat32** |  | [optional] 
**MFlRecoilShotIndexRecoveryTimeFactor** | Pointer to **NullableFloat32** |  | [optional] 
**MFlRecoilSpeed** | Pointer to **NullableFloat32** |  | [optional] 
**MFlReloadMoveSpeed** | Pointer to **NullableFloat32** |  | [optional] 
**MFlScatterYawScale** | Pointer to **NullableFloat32** |  | [optional] 
**MAimingShootSpreadPenalty** | Pointer to [**NullableMAimingshootspreadpenalty**](MAimingshootspreadpenalty.md) |  | [optional] 
**MStandingShootSpreadPenalty** | Pointer to [**NullableMStandingshootspreadpenalty**](MStandingshootspreadpenalty.md) |  | [optional] 
**MFlShootMoveSpeedPercent** | Pointer to **NullableFloat32** |  | [optional] 
**MFlShootSpreadPenaltyDecay** | Pointer to **NullableFloat32** |  | [optional] 
**MFlShootSpreadPenaltyDecayDelay** | Pointer to **NullableFloat32** |  | [optional] 
**MFlShootSpreadPenaltyPerShot** | Pointer to **NullableFloat32** |  | [optional] 
**MFlShootingUpSpreadPenalty** | Pointer to **NullableFloat32** |  | [optional] 
**MFlVerticalPunch** | Pointer to **NullableFloat32** |  | [optional] 
**MFlZoomFov** | Pointer to **NullableFloat32** |  | [optional] 
**MFlZoomMoveSpeedPercent** | Pointer to **NullableFloat32** |  | [optional] 
**MIBullets** | Pointer to **NullableInt32** |  | [optional] 
**MIBurstShotCount** | Pointer to **NullableInt32** |  | [optional] 
**MIClipSize** | Pointer to **NullableInt32** |  | [optional] 
**MFlSpread** | Pointer to **NullableFloat32** |  | [optional] 
**MFlStandingSpread** | Pointer to **NullableFloat32** |  | [optional] 
**MFlLowAmmoIndicatorThreshold** | Pointer to **NullableFloat32** |  | [optional] 
**MFlRecoilSeed** | Pointer to **NullableFloat32** |  | [optional] 
**MFlReloadDuration** | Pointer to **NullableFloat32** |  | [optional] 
**MBulletSpeedCurve** | Pointer to [**NullableRawItemWeaponInfoBulletSpeedCurveV2Input**](RawItemWeaponInfoBulletSpeedCurveV2Input.md) |  | [optional] 
**MHorizontalRecoil** | Pointer to [**NullableRawWeaponInfoHorizontalRecoilV2Input**](RawWeaponInfoHorizontalRecoilV2Input.md) |  | [optional] 
**MVerticalRecoil** | Pointer to [**NullableRawWeaponInfoVerticalRecoilV2Input**](RawWeaponInfoVerticalRecoilV2Input.md) |  | [optional] 

## Methods

### NewRawWeaponInfoV2Input

`func NewRawWeaponInfoV2Input() *RawWeaponInfoV2Input`

NewRawWeaponInfoV2Input instantiates a new RawWeaponInfoV2Input object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRawWeaponInfoV2InputWithDefaults

`func NewRawWeaponInfoV2InputWithDefaults() *RawWeaponInfoV2Input`

NewRawWeaponInfoV2InputWithDefaults instantiates a new RawWeaponInfoV2Input object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMBCanZoom

`func (o *RawWeaponInfoV2Input) GetMBCanZoom() bool`

GetMBCanZoom returns the MBCanZoom field if non-nil, zero value otherwise.

### GetMBCanZoomOk

`func (o *RawWeaponInfoV2Input) GetMBCanZoomOk() (*bool, bool)`

GetMBCanZoomOk returns a tuple with the MBCanZoom field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMBCanZoom

`func (o *RawWeaponInfoV2Input) SetMBCanZoom(v bool)`

SetMBCanZoom sets MBCanZoom field to given value.

### HasMBCanZoom

`func (o *RawWeaponInfoV2Input) HasMBCanZoom() bool`

HasMBCanZoom returns a boolean if a field has been set.

### SetMBCanZoomNil

`func (o *RawWeaponInfoV2Input) SetMBCanZoomNil(b bool)`

 SetMBCanZoomNil sets the value for MBCanZoom to be an explicit nil

### UnsetMBCanZoom
`func (o *RawWeaponInfoV2Input) UnsetMBCanZoom()`

UnsetMBCanZoom ensures that no value is present for MBCanZoom, not even an explicit nil
### GetMFlBulletDamage

`func (o *RawWeaponInfoV2Input) GetMFlBulletDamage() float32`

GetMFlBulletDamage returns the MFlBulletDamage field if non-nil, zero value otherwise.

### GetMFlBulletDamageOk

`func (o *RawWeaponInfoV2Input) GetMFlBulletDamageOk() (*float32, bool)`

GetMFlBulletDamageOk returns a tuple with the MFlBulletDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlBulletDamage

`func (o *RawWeaponInfoV2Input) SetMFlBulletDamage(v float32)`

SetMFlBulletDamage sets MFlBulletDamage field to given value.

### HasMFlBulletDamage

`func (o *RawWeaponInfoV2Input) HasMFlBulletDamage() bool`

HasMFlBulletDamage returns a boolean if a field has been set.

### SetMFlBulletDamageNil

`func (o *RawWeaponInfoV2Input) SetMFlBulletDamageNil(b bool)`

 SetMFlBulletDamageNil sets the value for MFlBulletDamage to be an explicit nil

### UnsetMFlBulletDamage
`func (o *RawWeaponInfoV2Input) UnsetMFlBulletDamage()`

UnsetMFlBulletDamage ensures that no value is present for MFlBulletDamage, not even an explicit nil
### GetMFlBulletGravityScale

`func (o *RawWeaponInfoV2Input) GetMFlBulletGravityScale() float32`

GetMFlBulletGravityScale returns the MFlBulletGravityScale field if non-nil, zero value otherwise.

### GetMFlBulletGravityScaleOk

`func (o *RawWeaponInfoV2Input) GetMFlBulletGravityScaleOk() (*float32, bool)`

GetMFlBulletGravityScaleOk returns a tuple with the MFlBulletGravityScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlBulletGravityScale

`func (o *RawWeaponInfoV2Input) SetMFlBulletGravityScale(v float32)`

SetMFlBulletGravityScale sets MFlBulletGravityScale field to given value.

### HasMFlBulletGravityScale

`func (o *RawWeaponInfoV2Input) HasMFlBulletGravityScale() bool`

HasMFlBulletGravityScale returns a boolean if a field has been set.

### SetMFlBulletGravityScaleNil

`func (o *RawWeaponInfoV2Input) SetMFlBulletGravityScaleNil(b bool)`

 SetMFlBulletGravityScaleNil sets the value for MFlBulletGravityScale to be an explicit nil

### UnsetMFlBulletGravityScale
`func (o *RawWeaponInfoV2Input) UnsetMFlBulletGravityScale()`

UnsetMFlBulletGravityScale ensures that no value is present for MFlBulletGravityScale, not even an explicit nil
### GetMFlBulletInheritShooterVelocityScale

`func (o *RawWeaponInfoV2Input) GetMFlBulletInheritShooterVelocityScale() float32`

GetMFlBulletInheritShooterVelocityScale returns the MFlBulletInheritShooterVelocityScale field if non-nil, zero value otherwise.

### GetMFlBulletInheritShooterVelocityScaleOk

`func (o *RawWeaponInfoV2Input) GetMFlBulletInheritShooterVelocityScaleOk() (*float32, bool)`

GetMFlBulletInheritShooterVelocityScaleOk returns a tuple with the MFlBulletInheritShooterVelocityScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlBulletInheritShooterVelocityScale

`func (o *RawWeaponInfoV2Input) SetMFlBulletInheritShooterVelocityScale(v float32)`

SetMFlBulletInheritShooterVelocityScale sets MFlBulletInheritShooterVelocityScale field to given value.

### HasMFlBulletInheritShooterVelocityScale

`func (o *RawWeaponInfoV2Input) HasMFlBulletInheritShooterVelocityScale() bool`

HasMFlBulletInheritShooterVelocityScale returns a boolean if a field has been set.

### SetMFlBulletInheritShooterVelocityScaleNil

`func (o *RawWeaponInfoV2Input) SetMFlBulletInheritShooterVelocityScaleNil(b bool)`

 SetMFlBulletInheritShooterVelocityScaleNil sets the value for MFlBulletInheritShooterVelocityScale to be an explicit nil

### UnsetMFlBulletInheritShooterVelocityScale
`func (o *RawWeaponInfoV2Input) UnsetMFlBulletInheritShooterVelocityScale()`

UnsetMFlBulletInheritShooterVelocityScale ensures that no value is present for MFlBulletInheritShooterVelocityScale, not even an explicit nil
### GetMFlBulletLifetime

`func (o *RawWeaponInfoV2Input) GetMFlBulletLifetime() float32`

GetMFlBulletLifetime returns the MFlBulletLifetime field if non-nil, zero value otherwise.

### GetMFlBulletLifetimeOk

`func (o *RawWeaponInfoV2Input) GetMFlBulletLifetimeOk() (*float32, bool)`

GetMFlBulletLifetimeOk returns a tuple with the MFlBulletLifetime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlBulletLifetime

`func (o *RawWeaponInfoV2Input) SetMFlBulletLifetime(v float32)`

SetMFlBulletLifetime sets MFlBulletLifetime field to given value.

### HasMFlBulletLifetime

`func (o *RawWeaponInfoV2Input) HasMFlBulletLifetime() bool`

HasMFlBulletLifetime returns a boolean if a field has been set.

### SetMFlBulletLifetimeNil

`func (o *RawWeaponInfoV2Input) SetMFlBulletLifetimeNil(b bool)`

 SetMFlBulletLifetimeNil sets the value for MFlBulletLifetime to be an explicit nil

### UnsetMFlBulletLifetime
`func (o *RawWeaponInfoV2Input) UnsetMFlBulletLifetime()`

UnsetMFlBulletLifetime ensures that no value is present for MFlBulletLifetime, not even an explicit nil
### GetMFlBulletRadius

`func (o *RawWeaponInfoV2Input) GetMFlBulletRadius() float32`

GetMFlBulletRadius returns the MFlBulletRadius field if non-nil, zero value otherwise.

### GetMFlBulletRadiusOk

`func (o *RawWeaponInfoV2Input) GetMFlBulletRadiusOk() (*float32, bool)`

GetMFlBulletRadiusOk returns a tuple with the MFlBulletRadius field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlBulletRadius

`func (o *RawWeaponInfoV2Input) SetMFlBulletRadius(v float32)`

SetMFlBulletRadius sets MFlBulletRadius field to given value.

### HasMFlBulletRadius

`func (o *RawWeaponInfoV2Input) HasMFlBulletRadius() bool`

HasMFlBulletRadius returns a boolean if a field has been set.

### SetMFlBulletRadiusNil

`func (o *RawWeaponInfoV2Input) SetMFlBulletRadiusNil(b bool)`

 SetMFlBulletRadiusNil sets the value for MFlBulletRadius to be an explicit nil

### UnsetMFlBulletRadius
`func (o *RawWeaponInfoV2Input) UnsetMFlBulletRadius()`

UnsetMFlBulletRadius ensures that no value is present for MFlBulletRadius, not even an explicit nil
### GetMFlBulletRadiusVsWorld

`func (o *RawWeaponInfoV2Input) GetMFlBulletRadiusVsWorld() float32`

GetMFlBulletRadiusVsWorld returns the MFlBulletRadiusVsWorld field if non-nil, zero value otherwise.

### GetMFlBulletRadiusVsWorldOk

`func (o *RawWeaponInfoV2Input) GetMFlBulletRadiusVsWorldOk() (*float32, bool)`

GetMFlBulletRadiusVsWorldOk returns a tuple with the MFlBulletRadiusVsWorld field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlBulletRadiusVsWorld

`func (o *RawWeaponInfoV2Input) SetMFlBulletRadiusVsWorld(v float32)`

SetMFlBulletRadiusVsWorld sets MFlBulletRadiusVsWorld field to given value.

### HasMFlBulletRadiusVsWorld

`func (o *RawWeaponInfoV2Input) HasMFlBulletRadiusVsWorld() bool`

HasMFlBulletRadiusVsWorld returns a boolean if a field has been set.

### SetMFlBulletRadiusVsWorldNil

`func (o *RawWeaponInfoV2Input) SetMFlBulletRadiusVsWorldNil(b bool)`

 SetMFlBulletRadiusVsWorldNil sets the value for MFlBulletRadiusVsWorld to be an explicit nil

### UnsetMFlBulletRadiusVsWorld
`func (o *RawWeaponInfoV2Input) UnsetMFlBulletRadiusVsWorld()`

UnsetMFlBulletRadiusVsWorld ensures that no value is present for MFlBulletRadiusVsWorld, not even an explicit nil
### GetMFlBulletReflectAmount

`func (o *RawWeaponInfoV2Input) GetMFlBulletReflectAmount() float32`

GetMFlBulletReflectAmount returns the MFlBulletReflectAmount field if non-nil, zero value otherwise.

### GetMFlBulletReflectAmountOk

`func (o *RawWeaponInfoV2Input) GetMFlBulletReflectAmountOk() (*float32, bool)`

GetMFlBulletReflectAmountOk returns a tuple with the MFlBulletReflectAmount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlBulletReflectAmount

`func (o *RawWeaponInfoV2Input) SetMFlBulletReflectAmount(v float32)`

SetMFlBulletReflectAmount sets MFlBulletReflectAmount field to given value.

### HasMFlBulletReflectAmount

`func (o *RawWeaponInfoV2Input) HasMFlBulletReflectAmount() bool`

HasMFlBulletReflectAmount returns a boolean if a field has been set.

### SetMFlBulletReflectAmountNil

`func (o *RawWeaponInfoV2Input) SetMFlBulletReflectAmountNil(b bool)`

 SetMFlBulletReflectAmountNil sets the value for MFlBulletReflectAmount to be an explicit nil

### UnsetMFlBulletReflectAmount
`func (o *RawWeaponInfoV2Input) UnsetMFlBulletReflectAmount()`

UnsetMFlBulletReflectAmount ensures that no value is present for MFlBulletReflectAmount, not even an explicit nil
### GetMFlBulletReflectScale

`func (o *RawWeaponInfoV2Input) GetMFlBulletReflectScale() float32`

GetMFlBulletReflectScale returns the MFlBulletReflectScale field if non-nil, zero value otherwise.

### GetMFlBulletReflectScaleOk

`func (o *RawWeaponInfoV2Input) GetMFlBulletReflectScaleOk() (*float32, bool)`

GetMFlBulletReflectScaleOk returns a tuple with the MFlBulletReflectScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlBulletReflectScale

`func (o *RawWeaponInfoV2Input) SetMFlBulletReflectScale(v float32)`

SetMFlBulletReflectScale sets MFlBulletReflectScale field to given value.

### HasMFlBulletReflectScale

`func (o *RawWeaponInfoV2Input) HasMFlBulletReflectScale() bool`

HasMFlBulletReflectScale returns a boolean if a field has been set.

### SetMFlBulletReflectScaleNil

`func (o *RawWeaponInfoV2Input) SetMFlBulletReflectScaleNil(b bool)`

 SetMFlBulletReflectScaleNil sets the value for MFlBulletReflectScale to be an explicit nil

### UnsetMFlBulletReflectScale
`func (o *RawWeaponInfoV2Input) UnsetMFlBulletReflectScale()`

UnsetMFlBulletReflectScale ensures that no value is present for MFlBulletReflectScale, not even an explicit nil
### GetMFlBulletWhizDistance

`func (o *RawWeaponInfoV2Input) GetMFlBulletWhizDistance() float32`

GetMFlBulletWhizDistance returns the MFlBulletWhizDistance field if non-nil, zero value otherwise.

### GetMFlBulletWhizDistanceOk

`func (o *RawWeaponInfoV2Input) GetMFlBulletWhizDistanceOk() (*float32, bool)`

GetMFlBulletWhizDistanceOk returns a tuple with the MFlBulletWhizDistance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlBulletWhizDistance

`func (o *RawWeaponInfoV2Input) SetMFlBulletWhizDistance(v float32)`

SetMFlBulletWhizDistance sets MFlBulletWhizDistance field to given value.

### HasMFlBulletWhizDistance

`func (o *RawWeaponInfoV2Input) HasMFlBulletWhizDistance() bool`

HasMFlBulletWhizDistance returns a boolean if a field has been set.

### SetMFlBulletWhizDistanceNil

`func (o *RawWeaponInfoV2Input) SetMFlBulletWhizDistanceNil(b bool)`

 SetMFlBulletWhizDistanceNil sets the value for MFlBulletWhizDistance to be an explicit nil

### UnsetMFlBulletWhizDistance
`func (o *RawWeaponInfoV2Input) UnsetMFlBulletWhizDistance()`

UnsetMFlBulletWhizDistance ensures that no value is present for MFlBulletWhizDistance, not even an explicit nil
### GetMFlBurstShotCooldown

`func (o *RawWeaponInfoV2Input) GetMFlBurstShotCooldown() float32`

GetMFlBurstShotCooldown returns the MFlBurstShotCooldown field if non-nil, zero value otherwise.

### GetMFlBurstShotCooldownOk

`func (o *RawWeaponInfoV2Input) GetMFlBurstShotCooldownOk() (*float32, bool)`

GetMFlBurstShotCooldownOk returns a tuple with the MFlBurstShotCooldown field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlBurstShotCooldown

`func (o *RawWeaponInfoV2Input) SetMFlBurstShotCooldown(v float32)`

SetMFlBurstShotCooldown sets MFlBurstShotCooldown field to given value.

### HasMFlBurstShotCooldown

`func (o *RawWeaponInfoV2Input) HasMFlBurstShotCooldown() bool`

HasMFlBurstShotCooldown returns a boolean if a field has been set.

### SetMFlBurstShotCooldownNil

`func (o *RawWeaponInfoV2Input) SetMFlBurstShotCooldownNil(b bool)`

 SetMFlBurstShotCooldownNil sets the value for MFlBurstShotCooldown to be an explicit nil

### UnsetMFlBurstShotCooldown
`func (o *RawWeaponInfoV2Input) UnsetMFlBurstShotCooldown()`

UnsetMFlBurstShotCooldown ensures that no value is present for MFlBurstShotCooldown, not even an explicit nil
### GetMFlCritBonusAgainstNpcs

`func (o *RawWeaponInfoV2Input) GetMFlCritBonusAgainstNpcs() float32`

GetMFlCritBonusAgainstNpcs returns the MFlCritBonusAgainstNpcs field if non-nil, zero value otherwise.

### GetMFlCritBonusAgainstNpcsOk

`func (o *RawWeaponInfoV2Input) GetMFlCritBonusAgainstNpcsOk() (*float32, bool)`

GetMFlCritBonusAgainstNpcsOk returns a tuple with the MFlCritBonusAgainstNpcs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlCritBonusAgainstNpcs

`func (o *RawWeaponInfoV2Input) SetMFlCritBonusAgainstNpcs(v float32)`

SetMFlCritBonusAgainstNpcs sets MFlCritBonusAgainstNpcs field to given value.

### HasMFlCritBonusAgainstNpcs

`func (o *RawWeaponInfoV2Input) HasMFlCritBonusAgainstNpcs() bool`

HasMFlCritBonusAgainstNpcs returns a boolean if a field has been set.

### SetMFlCritBonusAgainstNpcsNil

`func (o *RawWeaponInfoV2Input) SetMFlCritBonusAgainstNpcsNil(b bool)`

 SetMFlCritBonusAgainstNpcsNil sets the value for MFlCritBonusAgainstNpcs to be an explicit nil

### UnsetMFlCritBonusAgainstNpcs
`func (o *RawWeaponInfoV2Input) UnsetMFlCritBonusAgainstNpcs()`

UnsetMFlCritBonusAgainstNpcs ensures that no value is present for MFlCritBonusAgainstNpcs, not even an explicit nil
### GetMFlCritBonusEnd

`func (o *RawWeaponInfoV2Input) GetMFlCritBonusEnd() float32`

GetMFlCritBonusEnd returns the MFlCritBonusEnd field if non-nil, zero value otherwise.

### GetMFlCritBonusEndOk

`func (o *RawWeaponInfoV2Input) GetMFlCritBonusEndOk() (*float32, bool)`

GetMFlCritBonusEndOk returns a tuple with the MFlCritBonusEnd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlCritBonusEnd

`func (o *RawWeaponInfoV2Input) SetMFlCritBonusEnd(v float32)`

SetMFlCritBonusEnd sets MFlCritBonusEnd field to given value.

### HasMFlCritBonusEnd

`func (o *RawWeaponInfoV2Input) HasMFlCritBonusEnd() bool`

HasMFlCritBonusEnd returns a boolean if a field has been set.

### SetMFlCritBonusEndNil

`func (o *RawWeaponInfoV2Input) SetMFlCritBonusEndNil(b bool)`

 SetMFlCritBonusEndNil sets the value for MFlCritBonusEnd to be an explicit nil

### UnsetMFlCritBonusEnd
`func (o *RawWeaponInfoV2Input) UnsetMFlCritBonusEnd()`

UnsetMFlCritBonusEnd ensures that no value is present for MFlCritBonusEnd, not even an explicit nil
### GetMFlCritBonusEndRange

`func (o *RawWeaponInfoV2Input) GetMFlCritBonusEndRange() float32`

GetMFlCritBonusEndRange returns the MFlCritBonusEndRange field if non-nil, zero value otherwise.

### GetMFlCritBonusEndRangeOk

`func (o *RawWeaponInfoV2Input) GetMFlCritBonusEndRangeOk() (*float32, bool)`

GetMFlCritBonusEndRangeOk returns a tuple with the MFlCritBonusEndRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlCritBonusEndRange

`func (o *RawWeaponInfoV2Input) SetMFlCritBonusEndRange(v float32)`

SetMFlCritBonusEndRange sets MFlCritBonusEndRange field to given value.

### HasMFlCritBonusEndRange

`func (o *RawWeaponInfoV2Input) HasMFlCritBonusEndRange() bool`

HasMFlCritBonusEndRange returns a boolean if a field has been set.

### SetMFlCritBonusEndRangeNil

`func (o *RawWeaponInfoV2Input) SetMFlCritBonusEndRangeNil(b bool)`

 SetMFlCritBonusEndRangeNil sets the value for MFlCritBonusEndRange to be an explicit nil

### UnsetMFlCritBonusEndRange
`func (o *RawWeaponInfoV2Input) UnsetMFlCritBonusEndRange()`

UnsetMFlCritBonusEndRange ensures that no value is present for MFlCritBonusEndRange, not even an explicit nil
### GetMFlCritBonusStart

`func (o *RawWeaponInfoV2Input) GetMFlCritBonusStart() float32`

GetMFlCritBonusStart returns the MFlCritBonusStart field if non-nil, zero value otherwise.

### GetMFlCritBonusStartOk

`func (o *RawWeaponInfoV2Input) GetMFlCritBonusStartOk() (*float32, bool)`

GetMFlCritBonusStartOk returns a tuple with the MFlCritBonusStart field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlCritBonusStart

`func (o *RawWeaponInfoV2Input) SetMFlCritBonusStart(v float32)`

SetMFlCritBonusStart sets MFlCritBonusStart field to given value.

### HasMFlCritBonusStart

`func (o *RawWeaponInfoV2Input) HasMFlCritBonusStart() bool`

HasMFlCritBonusStart returns a boolean if a field has been set.

### SetMFlCritBonusStartNil

`func (o *RawWeaponInfoV2Input) SetMFlCritBonusStartNil(b bool)`

 SetMFlCritBonusStartNil sets the value for MFlCritBonusStart to be an explicit nil

### UnsetMFlCritBonusStart
`func (o *RawWeaponInfoV2Input) UnsetMFlCritBonusStart()`

UnsetMFlCritBonusStart ensures that no value is present for MFlCritBonusStart, not even an explicit nil
### GetMFlCritBonusStartRange

`func (o *RawWeaponInfoV2Input) GetMFlCritBonusStartRange() float32`

GetMFlCritBonusStartRange returns the MFlCritBonusStartRange field if non-nil, zero value otherwise.

### GetMFlCritBonusStartRangeOk

`func (o *RawWeaponInfoV2Input) GetMFlCritBonusStartRangeOk() (*float32, bool)`

GetMFlCritBonusStartRangeOk returns a tuple with the MFlCritBonusStartRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlCritBonusStartRange

`func (o *RawWeaponInfoV2Input) SetMFlCritBonusStartRange(v float32)`

SetMFlCritBonusStartRange sets MFlCritBonusStartRange field to given value.

### HasMFlCritBonusStartRange

`func (o *RawWeaponInfoV2Input) HasMFlCritBonusStartRange() bool`

HasMFlCritBonusStartRange returns a boolean if a field has been set.

### SetMFlCritBonusStartRangeNil

`func (o *RawWeaponInfoV2Input) SetMFlCritBonusStartRangeNil(b bool)`

 SetMFlCritBonusStartRangeNil sets the value for MFlCritBonusStartRange to be an explicit nil

### UnsetMFlCritBonusStartRange
`func (o *RawWeaponInfoV2Input) UnsetMFlCritBonusStartRange()`

UnsetMFlCritBonusStartRange ensures that no value is present for MFlCritBonusStartRange, not even an explicit nil
### GetMFlCycleTime

`func (o *RawWeaponInfoV2Input) GetMFlCycleTime() float32`

GetMFlCycleTime returns the MFlCycleTime field if non-nil, zero value otherwise.

### GetMFlCycleTimeOk

`func (o *RawWeaponInfoV2Input) GetMFlCycleTimeOk() (*float32, bool)`

GetMFlCycleTimeOk returns a tuple with the MFlCycleTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlCycleTime

`func (o *RawWeaponInfoV2Input) SetMFlCycleTime(v float32)`

SetMFlCycleTime sets MFlCycleTime field to given value.

### HasMFlCycleTime

`func (o *RawWeaponInfoV2Input) HasMFlCycleTime() bool`

HasMFlCycleTime returns a boolean if a field has been set.

### SetMFlCycleTimeNil

`func (o *RawWeaponInfoV2Input) SetMFlCycleTimeNil(b bool)`

 SetMFlCycleTimeNil sets the value for MFlCycleTime to be an explicit nil

### UnsetMFlCycleTime
`func (o *RawWeaponInfoV2Input) UnsetMFlCycleTime()`

UnsetMFlCycleTime ensures that no value is present for MFlCycleTime, not even an explicit nil
### GetMFlIntraBurstCycleTime

`func (o *RawWeaponInfoV2Input) GetMFlIntraBurstCycleTime() float32`

GetMFlIntraBurstCycleTime returns the MFlIntraBurstCycleTime field if non-nil, zero value otherwise.

### GetMFlIntraBurstCycleTimeOk

`func (o *RawWeaponInfoV2Input) GetMFlIntraBurstCycleTimeOk() (*float32, bool)`

GetMFlIntraBurstCycleTimeOk returns a tuple with the MFlIntraBurstCycleTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlIntraBurstCycleTime

`func (o *RawWeaponInfoV2Input) SetMFlIntraBurstCycleTime(v float32)`

SetMFlIntraBurstCycleTime sets MFlIntraBurstCycleTime field to given value.

### HasMFlIntraBurstCycleTime

`func (o *RawWeaponInfoV2Input) HasMFlIntraBurstCycleTime() bool`

HasMFlIntraBurstCycleTime returns a boolean if a field has been set.

### SetMFlIntraBurstCycleTimeNil

`func (o *RawWeaponInfoV2Input) SetMFlIntraBurstCycleTimeNil(b bool)`

 SetMFlIntraBurstCycleTimeNil sets the value for MFlIntraBurstCycleTime to be an explicit nil

### UnsetMFlIntraBurstCycleTime
`func (o *RawWeaponInfoV2Input) UnsetMFlIntraBurstCycleTime()`

UnsetMFlIntraBurstCycleTime ensures that no value is present for MFlIntraBurstCycleTime, not even an explicit nil
### GetMFlMaxSpinCycleTime

`func (o *RawWeaponInfoV2Input) GetMFlMaxSpinCycleTime() float32`

GetMFlMaxSpinCycleTime returns the MFlMaxSpinCycleTime field if non-nil, zero value otherwise.

### GetMFlMaxSpinCycleTimeOk

`func (o *RawWeaponInfoV2Input) GetMFlMaxSpinCycleTimeOk() (*float32, bool)`

GetMFlMaxSpinCycleTimeOk returns a tuple with the MFlMaxSpinCycleTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlMaxSpinCycleTime

`func (o *RawWeaponInfoV2Input) SetMFlMaxSpinCycleTime(v float32)`

SetMFlMaxSpinCycleTime sets MFlMaxSpinCycleTime field to given value.

### HasMFlMaxSpinCycleTime

`func (o *RawWeaponInfoV2Input) HasMFlMaxSpinCycleTime() bool`

HasMFlMaxSpinCycleTime returns a boolean if a field has been set.

### SetMFlMaxSpinCycleTimeNil

`func (o *RawWeaponInfoV2Input) SetMFlMaxSpinCycleTimeNil(b bool)`

 SetMFlMaxSpinCycleTimeNil sets the value for MFlMaxSpinCycleTime to be an explicit nil

### UnsetMFlMaxSpinCycleTime
`func (o *RawWeaponInfoV2Input) UnsetMFlMaxSpinCycleTime()`

UnsetMFlMaxSpinCycleTime ensures that no value is present for MFlMaxSpinCycleTime, not even an explicit nil
### GetMFlDamageFalloffBias

`func (o *RawWeaponInfoV2Input) GetMFlDamageFalloffBias() float32`

GetMFlDamageFalloffBias returns the MFlDamageFalloffBias field if non-nil, zero value otherwise.

### GetMFlDamageFalloffBiasOk

`func (o *RawWeaponInfoV2Input) GetMFlDamageFalloffBiasOk() (*float32, bool)`

GetMFlDamageFalloffBiasOk returns a tuple with the MFlDamageFalloffBias field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlDamageFalloffBias

`func (o *RawWeaponInfoV2Input) SetMFlDamageFalloffBias(v float32)`

SetMFlDamageFalloffBias sets MFlDamageFalloffBias field to given value.

### HasMFlDamageFalloffBias

`func (o *RawWeaponInfoV2Input) HasMFlDamageFalloffBias() bool`

HasMFlDamageFalloffBias returns a boolean if a field has been set.

### SetMFlDamageFalloffBiasNil

`func (o *RawWeaponInfoV2Input) SetMFlDamageFalloffBiasNil(b bool)`

 SetMFlDamageFalloffBiasNil sets the value for MFlDamageFalloffBias to be an explicit nil

### UnsetMFlDamageFalloffBias
`func (o *RawWeaponInfoV2Input) UnsetMFlDamageFalloffBias()`

UnsetMFlDamageFalloffBias ensures that no value is present for MFlDamageFalloffBias, not even an explicit nil
### GetMFlDamageFalloffEndRange

`func (o *RawWeaponInfoV2Input) GetMFlDamageFalloffEndRange() float32`

GetMFlDamageFalloffEndRange returns the MFlDamageFalloffEndRange field if non-nil, zero value otherwise.

### GetMFlDamageFalloffEndRangeOk

`func (o *RawWeaponInfoV2Input) GetMFlDamageFalloffEndRangeOk() (*float32, bool)`

GetMFlDamageFalloffEndRangeOk returns a tuple with the MFlDamageFalloffEndRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlDamageFalloffEndRange

`func (o *RawWeaponInfoV2Input) SetMFlDamageFalloffEndRange(v float32)`

SetMFlDamageFalloffEndRange sets MFlDamageFalloffEndRange field to given value.

### HasMFlDamageFalloffEndRange

`func (o *RawWeaponInfoV2Input) HasMFlDamageFalloffEndRange() bool`

HasMFlDamageFalloffEndRange returns a boolean if a field has been set.

### SetMFlDamageFalloffEndRangeNil

`func (o *RawWeaponInfoV2Input) SetMFlDamageFalloffEndRangeNil(b bool)`

 SetMFlDamageFalloffEndRangeNil sets the value for MFlDamageFalloffEndRange to be an explicit nil

### UnsetMFlDamageFalloffEndRange
`func (o *RawWeaponInfoV2Input) UnsetMFlDamageFalloffEndRange()`

UnsetMFlDamageFalloffEndRange ensures that no value is present for MFlDamageFalloffEndRange, not even an explicit nil
### GetMFlDamageFalloffEndScale

`func (o *RawWeaponInfoV2Input) GetMFlDamageFalloffEndScale() float32`

GetMFlDamageFalloffEndScale returns the MFlDamageFalloffEndScale field if non-nil, zero value otherwise.

### GetMFlDamageFalloffEndScaleOk

`func (o *RawWeaponInfoV2Input) GetMFlDamageFalloffEndScaleOk() (*float32, bool)`

GetMFlDamageFalloffEndScaleOk returns a tuple with the MFlDamageFalloffEndScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlDamageFalloffEndScale

`func (o *RawWeaponInfoV2Input) SetMFlDamageFalloffEndScale(v float32)`

SetMFlDamageFalloffEndScale sets MFlDamageFalloffEndScale field to given value.

### HasMFlDamageFalloffEndScale

`func (o *RawWeaponInfoV2Input) HasMFlDamageFalloffEndScale() bool`

HasMFlDamageFalloffEndScale returns a boolean if a field has been set.

### SetMFlDamageFalloffEndScaleNil

`func (o *RawWeaponInfoV2Input) SetMFlDamageFalloffEndScaleNil(b bool)`

 SetMFlDamageFalloffEndScaleNil sets the value for MFlDamageFalloffEndScale to be an explicit nil

### UnsetMFlDamageFalloffEndScale
`func (o *RawWeaponInfoV2Input) UnsetMFlDamageFalloffEndScale()`

UnsetMFlDamageFalloffEndScale ensures that no value is present for MFlDamageFalloffEndScale, not even an explicit nil
### GetMFlDamageFalloffStartRange

`func (o *RawWeaponInfoV2Input) GetMFlDamageFalloffStartRange() float32`

GetMFlDamageFalloffStartRange returns the MFlDamageFalloffStartRange field if non-nil, zero value otherwise.

### GetMFlDamageFalloffStartRangeOk

`func (o *RawWeaponInfoV2Input) GetMFlDamageFalloffStartRangeOk() (*float32, bool)`

GetMFlDamageFalloffStartRangeOk returns a tuple with the MFlDamageFalloffStartRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlDamageFalloffStartRange

`func (o *RawWeaponInfoV2Input) SetMFlDamageFalloffStartRange(v float32)`

SetMFlDamageFalloffStartRange sets MFlDamageFalloffStartRange field to given value.

### HasMFlDamageFalloffStartRange

`func (o *RawWeaponInfoV2Input) HasMFlDamageFalloffStartRange() bool`

HasMFlDamageFalloffStartRange returns a boolean if a field has been set.

### SetMFlDamageFalloffStartRangeNil

`func (o *RawWeaponInfoV2Input) SetMFlDamageFalloffStartRangeNil(b bool)`

 SetMFlDamageFalloffStartRangeNil sets the value for MFlDamageFalloffStartRange to be an explicit nil

### UnsetMFlDamageFalloffStartRange
`func (o *RawWeaponInfoV2Input) UnsetMFlDamageFalloffStartRange()`

UnsetMFlDamageFalloffStartRange ensures that no value is present for MFlDamageFalloffStartRange, not even an explicit nil
### GetMFlDamageFalloffStartScale

`func (o *RawWeaponInfoV2Input) GetMFlDamageFalloffStartScale() float32`

GetMFlDamageFalloffStartScale returns the MFlDamageFalloffStartScale field if non-nil, zero value otherwise.

### GetMFlDamageFalloffStartScaleOk

`func (o *RawWeaponInfoV2Input) GetMFlDamageFalloffStartScaleOk() (*float32, bool)`

GetMFlDamageFalloffStartScaleOk returns a tuple with the MFlDamageFalloffStartScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlDamageFalloffStartScale

`func (o *RawWeaponInfoV2Input) SetMFlDamageFalloffStartScale(v float32)`

SetMFlDamageFalloffStartScale sets MFlDamageFalloffStartScale field to given value.

### HasMFlDamageFalloffStartScale

`func (o *RawWeaponInfoV2Input) HasMFlDamageFalloffStartScale() bool`

HasMFlDamageFalloffStartScale returns a boolean if a field has been set.

### SetMFlDamageFalloffStartScaleNil

`func (o *RawWeaponInfoV2Input) SetMFlDamageFalloffStartScaleNil(b bool)`

 SetMFlDamageFalloffStartScaleNil sets the value for MFlDamageFalloffStartScale to be an explicit nil

### UnsetMFlDamageFalloffStartScale
`func (o *RawWeaponInfoV2Input) UnsetMFlDamageFalloffStartScale()`

UnsetMFlDamageFalloffStartScale ensures that no value is present for MFlDamageFalloffStartScale, not even an explicit nil
### GetMFlHorizontalPunch

`func (o *RawWeaponInfoV2Input) GetMFlHorizontalPunch() float32`

GetMFlHorizontalPunch returns the MFlHorizontalPunch field if non-nil, zero value otherwise.

### GetMFlHorizontalPunchOk

`func (o *RawWeaponInfoV2Input) GetMFlHorizontalPunchOk() (*float32, bool)`

GetMFlHorizontalPunchOk returns a tuple with the MFlHorizontalPunch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlHorizontalPunch

`func (o *RawWeaponInfoV2Input) SetMFlHorizontalPunch(v float32)`

SetMFlHorizontalPunch sets MFlHorizontalPunch field to given value.

### HasMFlHorizontalPunch

`func (o *RawWeaponInfoV2Input) HasMFlHorizontalPunch() bool`

HasMFlHorizontalPunch returns a boolean if a field has been set.

### SetMFlHorizontalPunchNil

`func (o *RawWeaponInfoV2Input) SetMFlHorizontalPunchNil(b bool)`

 SetMFlHorizontalPunchNil sets the value for MFlHorizontalPunch to be an explicit nil

### UnsetMFlHorizontalPunch
`func (o *RawWeaponInfoV2Input) UnsetMFlHorizontalPunch()`

UnsetMFlHorizontalPunch ensures that no value is present for MFlHorizontalPunch, not even an explicit nil
### GetMFlRange

`func (o *RawWeaponInfoV2Input) GetMFlRange() float32`

GetMFlRange returns the MFlRange field if non-nil, zero value otherwise.

### GetMFlRangeOk

`func (o *RawWeaponInfoV2Input) GetMFlRangeOk() (*float32, bool)`

GetMFlRangeOk returns a tuple with the MFlRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlRange

`func (o *RawWeaponInfoV2Input) SetMFlRange(v float32)`

SetMFlRange sets MFlRange field to given value.

### HasMFlRange

`func (o *RawWeaponInfoV2Input) HasMFlRange() bool`

HasMFlRange returns a boolean if a field has been set.

### SetMFlRangeNil

`func (o *RawWeaponInfoV2Input) SetMFlRangeNil(b bool)`

 SetMFlRangeNil sets the value for MFlRange to be an explicit nil

### UnsetMFlRange
`func (o *RawWeaponInfoV2Input) UnsetMFlRange()`

UnsetMFlRange ensures that no value is present for MFlRange, not even an explicit nil
### GetMFlRecoilRecoveryDelayFactor

`func (o *RawWeaponInfoV2Input) GetMFlRecoilRecoveryDelayFactor() float32`

GetMFlRecoilRecoveryDelayFactor returns the MFlRecoilRecoveryDelayFactor field if non-nil, zero value otherwise.

### GetMFlRecoilRecoveryDelayFactorOk

`func (o *RawWeaponInfoV2Input) GetMFlRecoilRecoveryDelayFactorOk() (*float32, bool)`

GetMFlRecoilRecoveryDelayFactorOk returns a tuple with the MFlRecoilRecoveryDelayFactor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlRecoilRecoveryDelayFactor

`func (o *RawWeaponInfoV2Input) SetMFlRecoilRecoveryDelayFactor(v float32)`

SetMFlRecoilRecoveryDelayFactor sets MFlRecoilRecoveryDelayFactor field to given value.

### HasMFlRecoilRecoveryDelayFactor

`func (o *RawWeaponInfoV2Input) HasMFlRecoilRecoveryDelayFactor() bool`

HasMFlRecoilRecoveryDelayFactor returns a boolean if a field has been set.

### SetMFlRecoilRecoveryDelayFactorNil

`func (o *RawWeaponInfoV2Input) SetMFlRecoilRecoveryDelayFactorNil(b bool)`

 SetMFlRecoilRecoveryDelayFactorNil sets the value for MFlRecoilRecoveryDelayFactor to be an explicit nil

### UnsetMFlRecoilRecoveryDelayFactor
`func (o *RawWeaponInfoV2Input) UnsetMFlRecoilRecoveryDelayFactor()`

UnsetMFlRecoilRecoveryDelayFactor ensures that no value is present for MFlRecoilRecoveryDelayFactor, not even an explicit nil
### GetMFlRecoilRecoverySpeed

`func (o *RawWeaponInfoV2Input) GetMFlRecoilRecoverySpeed() float32`

GetMFlRecoilRecoverySpeed returns the MFlRecoilRecoverySpeed field if non-nil, zero value otherwise.

### GetMFlRecoilRecoverySpeedOk

`func (o *RawWeaponInfoV2Input) GetMFlRecoilRecoverySpeedOk() (*float32, bool)`

GetMFlRecoilRecoverySpeedOk returns a tuple with the MFlRecoilRecoverySpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlRecoilRecoverySpeed

`func (o *RawWeaponInfoV2Input) SetMFlRecoilRecoverySpeed(v float32)`

SetMFlRecoilRecoverySpeed sets MFlRecoilRecoverySpeed field to given value.

### HasMFlRecoilRecoverySpeed

`func (o *RawWeaponInfoV2Input) HasMFlRecoilRecoverySpeed() bool`

HasMFlRecoilRecoverySpeed returns a boolean if a field has been set.

### SetMFlRecoilRecoverySpeedNil

`func (o *RawWeaponInfoV2Input) SetMFlRecoilRecoverySpeedNil(b bool)`

 SetMFlRecoilRecoverySpeedNil sets the value for MFlRecoilRecoverySpeed to be an explicit nil

### UnsetMFlRecoilRecoverySpeed
`func (o *RawWeaponInfoV2Input) UnsetMFlRecoilRecoverySpeed()`

UnsetMFlRecoilRecoverySpeed ensures that no value is present for MFlRecoilRecoverySpeed, not even an explicit nil
### GetMFlRecoilShotIndexRecoveryTimeFactor

`func (o *RawWeaponInfoV2Input) GetMFlRecoilShotIndexRecoveryTimeFactor() float32`

GetMFlRecoilShotIndexRecoveryTimeFactor returns the MFlRecoilShotIndexRecoveryTimeFactor field if non-nil, zero value otherwise.

### GetMFlRecoilShotIndexRecoveryTimeFactorOk

`func (o *RawWeaponInfoV2Input) GetMFlRecoilShotIndexRecoveryTimeFactorOk() (*float32, bool)`

GetMFlRecoilShotIndexRecoveryTimeFactorOk returns a tuple with the MFlRecoilShotIndexRecoveryTimeFactor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlRecoilShotIndexRecoveryTimeFactor

`func (o *RawWeaponInfoV2Input) SetMFlRecoilShotIndexRecoveryTimeFactor(v float32)`

SetMFlRecoilShotIndexRecoveryTimeFactor sets MFlRecoilShotIndexRecoveryTimeFactor field to given value.

### HasMFlRecoilShotIndexRecoveryTimeFactor

`func (o *RawWeaponInfoV2Input) HasMFlRecoilShotIndexRecoveryTimeFactor() bool`

HasMFlRecoilShotIndexRecoveryTimeFactor returns a boolean if a field has been set.

### SetMFlRecoilShotIndexRecoveryTimeFactorNil

`func (o *RawWeaponInfoV2Input) SetMFlRecoilShotIndexRecoveryTimeFactorNil(b bool)`

 SetMFlRecoilShotIndexRecoveryTimeFactorNil sets the value for MFlRecoilShotIndexRecoveryTimeFactor to be an explicit nil

### UnsetMFlRecoilShotIndexRecoveryTimeFactor
`func (o *RawWeaponInfoV2Input) UnsetMFlRecoilShotIndexRecoveryTimeFactor()`

UnsetMFlRecoilShotIndexRecoveryTimeFactor ensures that no value is present for MFlRecoilShotIndexRecoveryTimeFactor, not even an explicit nil
### GetMFlRecoilSpeed

`func (o *RawWeaponInfoV2Input) GetMFlRecoilSpeed() float32`

GetMFlRecoilSpeed returns the MFlRecoilSpeed field if non-nil, zero value otherwise.

### GetMFlRecoilSpeedOk

`func (o *RawWeaponInfoV2Input) GetMFlRecoilSpeedOk() (*float32, bool)`

GetMFlRecoilSpeedOk returns a tuple with the MFlRecoilSpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlRecoilSpeed

`func (o *RawWeaponInfoV2Input) SetMFlRecoilSpeed(v float32)`

SetMFlRecoilSpeed sets MFlRecoilSpeed field to given value.

### HasMFlRecoilSpeed

`func (o *RawWeaponInfoV2Input) HasMFlRecoilSpeed() bool`

HasMFlRecoilSpeed returns a boolean if a field has been set.

### SetMFlRecoilSpeedNil

`func (o *RawWeaponInfoV2Input) SetMFlRecoilSpeedNil(b bool)`

 SetMFlRecoilSpeedNil sets the value for MFlRecoilSpeed to be an explicit nil

### UnsetMFlRecoilSpeed
`func (o *RawWeaponInfoV2Input) UnsetMFlRecoilSpeed()`

UnsetMFlRecoilSpeed ensures that no value is present for MFlRecoilSpeed, not even an explicit nil
### GetMFlReloadMoveSpeed

`func (o *RawWeaponInfoV2Input) GetMFlReloadMoveSpeed() float32`

GetMFlReloadMoveSpeed returns the MFlReloadMoveSpeed field if non-nil, zero value otherwise.

### GetMFlReloadMoveSpeedOk

`func (o *RawWeaponInfoV2Input) GetMFlReloadMoveSpeedOk() (*float32, bool)`

GetMFlReloadMoveSpeedOk returns a tuple with the MFlReloadMoveSpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlReloadMoveSpeed

`func (o *RawWeaponInfoV2Input) SetMFlReloadMoveSpeed(v float32)`

SetMFlReloadMoveSpeed sets MFlReloadMoveSpeed field to given value.

### HasMFlReloadMoveSpeed

`func (o *RawWeaponInfoV2Input) HasMFlReloadMoveSpeed() bool`

HasMFlReloadMoveSpeed returns a boolean if a field has been set.

### SetMFlReloadMoveSpeedNil

`func (o *RawWeaponInfoV2Input) SetMFlReloadMoveSpeedNil(b bool)`

 SetMFlReloadMoveSpeedNil sets the value for MFlReloadMoveSpeed to be an explicit nil

### UnsetMFlReloadMoveSpeed
`func (o *RawWeaponInfoV2Input) UnsetMFlReloadMoveSpeed()`

UnsetMFlReloadMoveSpeed ensures that no value is present for MFlReloadMoveSpeed, not even an explicit nil
### GetMFlScatterYawScale

`func (o *RawWeaponInfoV2Input) GetMFlScatterYawScale() float32`

GetMFlScatterYawScale returns the MFlScatterYawScale field if non-nil, zero value otherwise.

### GetMFlScatterYawScaleOk

`func (o *RawWeaponInfoV2Input) GetMFlScatterYawScaleOk() (*float32, bool)`

GetMFlScatterYawScaleOk returns a tuple with the MFlScatterYawScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlScatterYawScale

`func (o *RawWeaponInfoV2Input) SetMFlScatterYawScale(v float32)`

SetMFlScatterYawScale sets MFlScatterYawScale field to given value.

### HasMFlScatterYawScale

`func (o *RawWeaponInfoV2Input) HasMFlScatterYawScale() bool`

HasMFlScatterYawScale returns a boolean if a field has been set.

### SetMFlScatterYawScaleNil

`func (o *RawWeaponInfoV2Input) SetMFlScatterYawScaleNil(b bool)`

 SetMFlScatterYawScaleNil sets the value for MFlScatterYawScale to be an explicit nil

### UnsetMFlScatterYawScale
`func (o *RawWeaponInfoV2Input) UnsetMFlScatterYawScale()`

UnsetMFlScatterYawScale ensures that no value is present for MFlScatterYawScale, not even an explicit nil
### GetMAimingShootSpreadPenalty

`func (o *RawWeaponInfoV2Input) GetMAimingShootSpreadPenalty() MAimingshootspreadpenalty`

GetMAimingShootSpreadPenalty returns the MAimingShootSpreadPenalty field if non-nil, zero value otherwise.

### GetMAimingShootSpreadPenaltyOk

`func (o *RawWeaponInfoV2Input) GetMAimingShootSpreadPenaltyOk() (*MAimingshootspreadpenalty, bool)`

GetMAimingShootSpreadPenaltyOk returns a tuple with the MAimingShootSpreadPenalty field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMAimingShootSpreadPenalty

`func (o *RawWeaponInfoV2Input) SetMAimingShootSpreadPenalty(v MAimingshootspreadpenalty)`

SetMAimingShootSpreadPenalty sets MAimingShootSpreadPenalty field to given value.

### HasMAimingShootSpreadPenalty

`func (o *RawWeaponInfoV2Input) HasMAimingShootSpreadPenalty() bool`

HasMAimingShootSpreadPenalty returns a boolean if a field has been set.

### SetMAimingShootSpreadPenaltyNil

`func (o *RawWeaponInfoV2Input) SetMAimingShootSpreadPenaltyNil(b bool)`

 SetMAimingShootSpreadPenaltyNil sets the value for MAimingShootSpreadPenalty to be an explicit nil

### UnsetMAimingShootSpreadPenalty
`func (o *RawWeaponInfoV2Input) UnsetMAimingShootSpreadPenalty()`

UnsetMAimingShootSpreadPenalty ensures that no value is present for MAimingShootSpreadPenalty, not even an explicit nil
### GetMStandingShootSpreadPenalty

`func (o *RawWeaponInfoV2Input) GetMStandingShootSpreadPenalty() MStandingshootspreadpenalty`

GetMStandingShootSpreadPenalty returns the MStandingShootSpreadPenalty field if non-nil, zero value otherwise.

### GetMStandingShootSpreadPenaltyOk

`func (o *RawWeaponInfoV2Input) GetMStandingShootSpreadPenaltyOk() (*MStandingshootspreadpenalty, bool)`

GetMStandingShootSpreadPenaltyOk returns a tuple with the MStandingShootSpreadPenalty field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMStandingShootSpreadPenalty

`func (o *RawWeaponInfoV2Input) SetMStandingShootSpreadPenalty(v MStandingshootspreadpenalty)`

SetMStandingShootSpreadPenalty sets MStandingShootSpreadPenalty field to given value.

### HasMStandingShootSpreadPenalty

`func (o *RawWeaponInfoV2Input) HasMStandingShootSpreadPenalty() bool`

HasMStandingShootSpreadPenalty returns a boolean if a field has been set.

### SetMStandingShootSpreadPenaltyNil

`func (o *RawWeaponInfoV2Input) SetMStandingShootSpreadPenaltyNil(b bool)`

 SetMStandingShootSpreadPenaltyNil sets the value for MStandingShootSpreadPenalty to be an explicit nil

### UnsetMStandingShootSpreadPenalty
`func (o *RawWeaponInfoV2Input) UnsetMStandingShootSpreadPenalty()`

UnsetMStandingShootSpreadPenalty ensures that no value is present for MStandingShootSpreadPenalty, not even an explicit nil
### GetMFlShootMoveSpeedPercent

`func (o *RawWeaponInfoV2Input) GetMFlShootMoveSpeedPercent() float32`

GetMFlShootMoveSpeedPercent returns the MFlShootMoveSpeedPercent field if non-nil, zero value otherwise.

### GetMFlShootMoveSpeedPercentOk

`func (o *RawWeaponInfoV2Input) GetMFlShootMoveSpeedPercentOk() (*float32, bool)`

GetMFlShootMoveSpeedPercentOk returns a tuple with the MFlShootMoveSpeedPercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlShootMoveSpeedPercent

`func (o *RawWeaponInfoV2Input) SetMFlShootMoveSpeedPercent(v float32)`

SetMFlShootMoveSpeedPercent sets MFlShootMoveSpeedPercent field to given value.

### HasMFlShootMoveSpeedPercent

`func (o *RawWeaponInfoV2Input) HasMFlShootMoveSpeedPercent() bool`

HasMFlShootMoveSpeedPercent returns a boolean if a field has been set.

### SetMFlShootMoveSpeedPercentNil

`func (o *RawWeaponInfoV2Input) SetMFlShootMoveSpeedPercentNil(b bool)`

 SetMFlShootMoveSpeedPercentNil sets the value for MFlShootMoveSpeedPercent to be an explicit nil

### UnsetMFlShootMoveSpeedPercent
`func (o *RawWeaponInfoV2Input) UnsetMFlShootMoveSpeedPercent()`

UnsetMFlShootMoveSpeedPercent ensures that no value is present for MFlShootMoveSpeedPercent, not even an explicit nil
### GetMFlShootSpreadPenaltyDecay

`func (o *RawWeaponInfoV2Input) GetMFlShootSpreadPenaltyDecay() float32`

GetMFlShootSpreadPenaltyDecay returns the MFlShootSpreadPenaltyDecay field if non-nil, zero value otherwise.

### GetMFlShootSpreadPenaltyDecayOk

`func (o *RawWeaponInfoV2Input) GetMFlShootSpreadPenaltyDecayOk() (*float32, bool)`

GetMFlShootSpreadPenaltyDecayOk returns a tuple with the MFlShootSpreadPenaltyDecay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlShootSpreadPenaltyDecay

`func (o *RawWeaponInfoV2Input) SetMFlShootSpreadPenaltyDecay(v float32)`

SetMFlShootSpreadPenaltyDecay sets MFlShootSpreadPenaltyDecay field to given value.

### HasMFlShootSpreadPenaltyDecay

`func (o *RawWeaponInfoV2Input) HasMFlShootSpreadPenaltyDecay() bool`

HasMFlShootSpreadPenaltyDecay returns a boolean if a field has been set.

### SetMFlShootSpreadPenaltyDecayNil

`func (o *RawWeaponInfoV2Input) SetMFlShootSpreadPenaltyDecayNil(b bool)`

 SetMFlShootSpreadPenaltyDecayNil sets the value for MFlShootSpreadPenaltyDecay to be an explicit nil

### UnsetMFlShootSpreadPenaltyDecay
`func (o *RawWeaponInfoV2Input) UnsetMFlShootSpreadPenaltyDecay()`

UnsetMFlShootSpreadPenaltyDecay ensures that no value is present for MFlShootSpreadPenaltyDecay, not even an explicit nil
### GetMFlShootSpreadPenaltyDecayDelay

`func (o *RawWeaponInfoV2Input) GetMFlShootSpreadPenaltyDecayDelay() float32`

GetMFlShootSpreadPenaltyDecayDelay returns the MFlShootSpreadPenaltyDecayDelay field if non-nil, zero value otherwise.

### GetMFlShootSpreadPenaltyDecayDelayOk

`func (o *RawWeaponInfoV2Input) GetMFlShootSpreadPenaltyDecayDelayOk() (*float32, bool)`

GetMFlShootSpreadPenaltyDecayDelayOk returns a tuple with the MFlShootSpreadPenaltyDecayDelay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlShootSpreadPenaltyDecayDelay

`func (o *RawWeaponInfoV2Input) SetMFlShootSpreadPenaltyDecayDelay(v float32)`

SetMFlShootSpreadPenaltyDecayDelay sets MFlShootSpreadPenaltyDecayDelay field to given value.

### HasMFlShootSpreadPenaltyDecayDelay

`func (o *RawWeaponInfoV2Input) HasMFlShootSpreadPenaltyDecayDelay() bool`

HasMFlShootSpreadPenaltyDecayDelay returns a boolean if a field has been set.

### SetMFlShootSpreadPenaltyDecayDelayNil

`func (o *RawWeaponInfoV2Input) SetMFlShootSpreadPenaltyDecayDelayNil(b bool)`

 SetMFlShootSpreadPenaltyDecayDelayNil sets the value for MFlShootSpreadPenaltyDecayDelay to be an explicit nil

### UnsetMFlShootSpreadPenaltyDecayDelay
`func (o *RawWeaponInfoV2Input) UnsetMFlShootSpreadPenaltyDecayDelay()`

UnsetMFlShootSpreadPenaltyDecayDelay ensures that no value is present for MFlShootSpreadPenaltyDecayDelay, not even an explicit nil
### GetMFlShootSpreadPenaltyPerShot

`func (o *RawWeaponInfoV2Input) GetMFlShootSpreadPenaltyPerShot() float32`

GetMFlShootSpreadPenaltyPerShot returns the MFlShootSpreadPenaltyPerShot field if non-nil, zero value otherwise.

### GetMFlShootSpreadPenaltyPerShotOk

`func (o *RawWeaponInfoV2Input) GetMFlShootSpreadPenaltyPerShotOk() (*float32, bool)`

GetMFlShootSpreadPenaltyPerShotOk returns a tuple with the MFlShootSpreadPenaltyPerShot field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlShootSpreadPenaltyPerShot

`func (o *RawWeaponInfoV2Input) SetMFlShootSpreadPenaltyPerShot(v float32)`

SetMFlShootSpreadPenaltyPerShot sets MFlShootSpreadPenaltyPerShot field to given value.

### HasMFlShootSpreadPenaltyPerShot

`func (o *RawWeaponInfoV2Input) HasMFlShootSpreadPenaltyPerShot() bool`

HasMFlShootSpreadPenaltyPerShot returns a boolean if a field has been set.

### SetMFlShootSpreadPenaltyPerShotNil

`func (o *RawWeaponInfoV2Input) SetMFlShootSpreadPenaltyPerShotNil(b bool)`

 SetMFlShootSpreadPenaltyPerShotNil sets the value for MFlShootSpreadPenaltyPerShot to be an explicit nil

### UnsetMFlShootSpreadPenaltyPerShot
`func (o *RawWeaponInfoV2Input) UnsetMFlShootSpreadPenaltyPerShot()`

UnsetMFlShootSpreadPenaltyPerShot ensures that no value is present for MFlShootSpreadPenaltyPerShot, not even an explicit nil
### GetMFlShootingUpSpreadPenalty

`func (o *RawWeaponInfoV2Input) GetMFlShootingUpSpreadPenalty() float32`

GetMFlShootingUpSpreadPenalty returns the MFlShootingUpSpreadPenalty field if non-nil, zero value otherwise.

### GetMFlShootingUpSpreadPenaltyOk

`func (o *RawWeaponInfoV2Input) GetMFlShootingUpSpreadPenaltyOk() (*float32, bool)`

GetMFlShootingUpSpreadPenaltyOk returns a tuple with the MFlShootingUpSpreadPenalty field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlShootingUpSpreadPenalty

`func (o *RawWeaponInfoV2Input) SetMFlShootingUpSpreadPenalty(v float32)`

SetMFlShootingUpSpreadPenalty sets MFlShootingUpSpreadPenalty field to given value.

### HasMFlShootingUpSpreadPenalty

`func (o *RawWeaponInfoV2Input) HasMFlShootingUpSpreadPenalty() bool`

HasMFlShootingUpSpreadPenalty returns a boolean if a field has been set.

### SetMFlShootingUpSpreadPenaltyNil

`func (o *RawWeaponInfoV2Input) SetMFlShootingUpSpreadPenaltyNil(b bool)`

 SetMFlShootingUpSpreadPenaltyNil sets the value for MFlShootingUpSpreadPenalty to be an explicit nil

### UnsetMFlShootingUpSpreadPenalty
`func (o *RawWeaponInfoV2Input) UnsetMFlShootingUpSpreadPenalty()`

UnsetMFlShootingUpSpreadPenalty ensures that no value is present for MFlShootingUpSpreadPenalty, not even an explicit nil
### GetMFlVerticalPunch

`func (o *RawWeaponInfoV2Input) GetMFlVerticalPunch() float32`

GetMFlVerticalPunch returns the MFlVerticalPunch field if non-nil, zero value otherwise.

### GetMFlVerticalPunchOk

`func (o *RawWeaponInfoV2Input) GetMFlVerticalPunchOk() (*float32, bool)`

GetMFlVerticalPunchOk returns a tuple with the MFlVerticalPunch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlVerticalPunch

`func (o *RawWeaponInfoV2Input) SetMFlVerticalPunch(v float32)`

SetMFlVerticalPunch sets MFlVerticalPunch field to given value.

### HasMFlVerticalPunch

`func (o *RawWeaponInfoV2Input) HasMFlVerticalPunch() bool`

HasMFlVerticalPunch returns a boolean if a field has been set.

### SetMFlVerticalPunchNil

`func (o *RawWeaponInfoV2Input) SetMFlVerticalPunchNil(b bool)`

 SetMFlVerticalPunchNil sets the value for MFlVerticalPunch to be an explicit nil

### UnsetMFlVerticalPunch
`func (o *RawWeaponInfoV2Input) UnsetMFlVerticalPunch()`

UnsetMFlVerticalPunch ensures that no value is present for MFlVerticalPunch, not even an explicit nil
### GetMFlZoomFov

`func (o *RawWeaponInfoV2Input) GetMFlZoomFov() float32`

GetMFlZoomFov returns the MFlZoomFov field if non-nil, zero value otherwise.

### GetMFlZoomFovOk

`func (o *RawWeaponInfoV2Input) GetMFlZoomFovOk() (*float32, bool)`

GetMFlZoomFovOk returns a tuple with the MFlZoomFov field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlZoomFov

`func (o *RawWeaponInfoV2Input) SetMFlZoomFov(v float32)`

SetMFlZoomFov sets MFlZoomFov field to given value.

### HasMFlZoomFov

`func (o *RawWeaponInfoV2Input) HasMFlZoomFov() bool`

HasMFlZoomFov returns a boolean if a field has been set.

### SetMFlZoomFovNil

`func (o *RawWeaponInfoV2Input) SetMFlZoomFovNil(b bool)`

 SetMFlZoomFovNil sets the value for MFlZoomFov to be an explicit nil

### UnsetMFlZoomFov
`func (o *RawWeaponInfoV2Input) UnsetMFlZoomFov()`

UnsetMFlZoomFov ensures that no value is present for MFlZoomFov, not even an explicit nil
### GetMFlZoomMoveSpeedPercent

`func (o *RawWeaponInfoV2Input) GetMFlZoomMoveSpeedPercent() float32`

GetMFlZoomMoveSpeedPercent returns the MFlZoomMoveSpeedPercent field if non-nil, zero value otherwise.

### GetMFlZoomMoveSpeedPercentOk

`func (o *RawWeaponInfoV2Input) GetMFlZoomMoveSpeedPercentOk() (*float32, bool)`

GetMFlZoomMoveSpeedPercentOk returns a tuple with the MFlZoomMoveSpeedPercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlZoomMoveSpeedPercent

`func (o *RawWeaponInfoV2Input) SetMFlZoomMoveSpeedPercent(v float32)`

SetMFlZoomMoveSpeedPercent sets MFlZoomMoveSpeedPercent field to given value.

### HasMFlZoomMoveSpeedPercent

`func (o *RawWeaponInfoV2Input) HasMFlZoomMoveSpeedPercent() bool`

HasMFlZoomMoveSpeedPercent returns a boolean if a field has been set.

### SetMFlZoomMoveSpeedPercentNil

`func (o *RawWeaponInfoV2Input) SetMFlZoomMoveSpeedPercentNil(b bool)`

 SetMFlZoomMoveSpeedPercentNil sets the value for MFlZoomMoveSpeedPercent to be an explicit nil

### UnsetMFlZoomMoveSpeedPercent
`func (o *RawWeaponInfoV2Input) UnsetMFlZoomMoveSpeedPercent()`

UnsetMFlZoomMoveSpeedPercent ensures that no value is present for MFlZoomMoveSpeedPercent, not even an explicit nil
### GetMIBullets

`func (o *RawWeaponInfoV2Input) GetMIBullets() int32`

GetMIBullets returns the MIBullets field if non-nil, zero value otherwise.

### GetMIBulletsOk

`func (o *RawWeaponInfoV2Input) GetMIBulletsOk() (*int32, bool)`

GetMIBulletsOk returns a tuple with the MIBullets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMIBullets

`func (o *RawWeaponInfoV2Input) SetMIBullets(v int32)`

SetMIBullets sets MIBullets field to given value.

### HasMIBullets

`func (o *RawWeaponInfoV2Input) HasMIBullets() bool`

HasMIBullets returns a boolean if a field has been set.

### SetMIBulletsNil

`func (o *RawWeaponInfoV2Input) SetMIBulletsNil(b bool)`

 SetMIBulletsNil sets the value for MIBullets to be an explicit nil

### UnsetMIBullets
`func (o *RawWeaponInfoV2Input) UnsetMIBullets()`

UnsetMIBullets ensures that no value is present for MIBullets, not even an explicit nil
### GetMIBurstShotCount

`func (o *RawWeaponInfoV2Input) GetMIBurstShotCount() int32`

GetMIBurstShotCount returns the MIBurstShotCount field if non-nil, zero value otherwise.

### GetMIBurstShotCountOk

`func (o *RawWeaponInfoV2Input) GetMIBurstShotCountOk() (*int32, bool)`

GetMIBurstShotCountOk returns a tuple with the MIBurstShotCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMIBurstShotCount

`func (o *RawWeaponInfoV2Input) SetMIBurstShotCount(v int32)`

SetMIBurstShotCount sets MIBurstShotCount field to given value.

### HasMIBurstShotCount

`func (o *RawWeaponInfoV2Input) HasMIBurstShotCount() bool`

HasMIBurstShotCount returns a boolean if a field has been set.

### SetMIBurstShotCountNil

`func (o *RawWeaponInfoV2Input) SetMIBurstShotCountNil(b bool)`

 SetMIBurstShotCountNil sets the value for MIBurstShotCount to be an explicit nil

### UnsetMIBurstShotCount
`func (o *RawWeaponInfoV2Input) UnsetMIBurstShotCount()`

UnsetMIBurstShotCount ensures that no value is present for MIBurstShotCount, not even an explicit nil
### GetMIClipSize

`func (o *RawWeaponInfoV2Input) GetMIClipSize() int32`

GetMIClipSize returns the MIClipSize field if non-nil, zero value otherwise.

### GetMIClipSizeOk

`func (o *RawWeaponInfoV2Input) GetMIClipSizeOk() (*int32, bool)`

GetMIClipSizeOk returns a tuple with the MIClipSize field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMIClipSize

`func (o *RawWeaponInfoV2Input) SetMIClipSize(v int32)`

SetMIClipSize sets MIClipSize field to given value.

### HasMIClipSize

`func (o *RawWeaponInfoV2Input) HasMIClipSize() bool`

HasMIClipSize returns a boolean if a field has been set.

### SetMIClipSizeNil

`func (o *RawWeaponInfoV2Input) SetMIClipSizeNil(b bool)`

 SetMIClipSizeNil sets the value for MIClipSize to be an explicit nil

### UnsetMIClipSize
`func (o *RawWeaponInfoV2Input) UnsetMIClipSize()`

UnsetMIClipSize ensures that no value is present for MIClipSize, not even an explicit nil
### GetMFlSpread

`func (o *RawWeaponInfoV2Input) GetMFlSpread() float32`

GetMFlSpread returns the MFlSpread field if non-nil, zero value otherwise.

### GetMFlSpreadOk

`func (o *RawWeaponInfoV2Input) GetMFlSpreadOk() (*float32, bool)`

GetMFlSpreadOk returns a tuple with the MFlSpread field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlSpread

`func (o *RawWeaponInfoV2Input) SetMFlSpread(v float32)`

SetMFlSpread sets MFlSpread field to given value.

### HasMFlSpread

`func (o *RawWeaponInfoV2Input) HasMFlSpread() bool`

HasMFlSpread returns a boolean if a field has been set.

### SetMFlSpreadNil

`func (o *RawWeaponInfoV2Input) SetMFlSpreadNil(b bool)`

 SetMFlSpreadNil sets the value for MFlSpread to be an explicit nil

### UnsetMFlSpread
`func (o *RawWeaponInfoV2Input) UnsetMFlSpread()`

UnsetMFlSpread ensures that no value is present for MFlSpread, not even an explicit nil
### GetMFlStandingSpread

`func (o *RawWeaponInfoV2Input) GetMFlStandingSpread() float32`

GetMFlStandingSpread returns the MFlStandingSpread field if non-nil, zero value otherwise.

### GetMFlStandingSpreadOk

`func (o *RawWeaponInfoV2Input) GetMFlStandingSpreadOk() (*float32, bool)`

GetMFlStandingSpreadOk returns a tuple with the MFlStandingSpread field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlStandingSpread

`func (o *RawWeaponInfoV2Input) SetMFlStandingSpread(v float32)`

SetMFlStandingSpread sets MFlStandingSpread field to given value.

### HasMFlStandingSpread

`func (o *RawWeaponInfoV2Input) HasMFlStandingSpread() bool`

HasMFlStandingSpread returns a boolean if a field has been set.

### SetMFlStandingSpreadNil

`func (o *RawWeaponInfoV2Input) SetMFlStandingSpreadNil(b bool)`

 SetMFlStandingSpreadNil sets the value for MFlStandingSpread to be an explicit nil

### UnsetMFlStandingSpread
`func (o *RawWeaponInfoV2Input) UnsetMFlStandingSpread()`

UnsetMFlStandingSpread ensures that no value is present for MFlStandingSpread, not even an explicit nil
### GetMFlLowAmmoIndicatorThreshold

`func (o *RawWeaponInfoV2Input) GetMFlLowAmmoIndicatorThreshold() float32`

GetMFlLowAmmoIndicatorThreshold returns the MFlLowAmmoIndicatorThreshold field if non-nil, zero value otherwise.

### GetMFlLowAmmoIndicatorThresholdOk

`func (o *RawWeaponInfoV2Input) GetMFlLowAmmoIndicatorThresholdOk() (*float32, bool)`

GetMFlLowAmmoIndicatorThresholdOk returns a tuple with the MFlLowAmmoIndicatorThreshold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlLowAmmoIndicatorThreshold

`func (o *RawWeaponInfoV2Input) SetMFlLowAmmoIndicatorThreshold(v float32)`

SetMFlLowAmmoIndicatorThreshold sets MFlLowAmmoIndicatorThreshold field to given value.

### HasMFlLowAmmoIndicatorThreshold

`func (o *RawWeaponInfoV2Input) HasMFlLowAmmoIndicatorThreshold() bool`

HasMFlLowAmmoIndicatorThreshold returns a boolean if a field has been set.

### SetMFlLowAmmoIndicatorThresholdNil

`func (o *RawWeaponInfoV2Input) SetMFlLowAmmoIndicatorThresholdNil(b bool)`

 SetMFlLowAmmoIndicatorThresholdNil sets the value for MFlLowAmmoIndicatorThreshold to be an explicit nil

### UnsetMFlLowAmmoIndicatorThreshold
`func (o *RawWeaponInfoV2Input) UnsetMFlLowAmmoIndicatorThreshold()`

UnsetMFlLowAmmoIndicatorThreshold ensures that no value is present for MFlLowAmmoIndicatorThreshold, not even an explicit nil
### GetMFlRecoilSeed

`func (o *RawWeaponInfoV2Input) GetMFlRecoilSeed() float32`

GetMFlRecoilSeed returns the MFlRecoilSeed field if non-nil, zero value otherwise.

### GetMFlRecoilSeedOk

`func (o *RawWeaponInfoV2Input) GetMFlRecoilSeedOk() (*float32, bool)`

GetMFlRecoilSeedOk returns a tuple with the MFlRecoilSeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlRecoilSeed

`func (o *RawWeaponInfoV2Input) SetMFlRecoilSeed(v float32)`

SetMFlRecoilSeed sets MFlRecoilSeed field to given value.

### HasMFlRecoilSeed

`func (o *RawWeaponInfoV2Input) HasMFlRecoilSeed() bool`

HasMFlRecoilSeed returns a boolean if a field has been set.

### SetMFlRecoilSeedNil

`func (o *RawWeaponInfoV2Input) SetMFlRecoilSeedNil(b bool)`

 SetMFlRecoilSeedNil sets the value for MFlRecoilSeed to be an explicit nil

### UnsetMFlRecoilSeed
`func (o *RawWeaponInfoV2Input) UnsetMFlRecoilSeed()`

UnsetMFlRecoilSeed ensures that no value is present for MFlRecoilSeed, not even an explicit nil
### GetMFlReloadDuration

`func (o *RawWeaponInfoV2Input) GetMFlReloadDuration() float32`

GetMFlReloadDuration returns the MFlReloadDuration field if non-nil, zero value otherwise.

### GetMFlReloadDurationOk

`func (o *RawWeaponInfoV2Input) GetMFlReloadDurationOk() (*float32, bool)`

GetMFlReloadDurationOk returns a tuple with the MFlReloadDuration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMFlReloadDuration

`func (o *RawWeaponInfoV2Input) SetMFlReloadDuration(v float32)`

SetMFlReloadDuration sets MFlReloadDuration field to given value.

### HasMFlReloadDuration

`func (o *RawWeaponInfoV2Input) HasMFlReloadDuration() bool`

HasMFlReloadDuration returns a boolean if a field has been set.

### SetMFlReloadDurationNil

`func (o *RawWeaponInfoV2Input) SetMFlReloadDurationNil(b bool)`

 SetMFlReloadDurationNil sets the value for MFlReloadDuration to be an explicit nil

### UnsetMFlReloadDuration
`func (o *RawWeaponInfoV2Input) UnsetMFlReloadDuration()`

UnsetMFlReloadDuration ensures that no value is present for MFlReloadDuration, not even an explicit nil
### GetMBulletSpeedCurve

`func (o *RawWeaponInfoV2Input) GetMBulletSpeedCurve() RawItemWeaponInfoBulletSpeedCurveV2Input`

GetMBulletSpeedCurve returns the MBulletSpeedCurve field if non-nil, zero value otherwise.

### GetMBulletSpeedCurveOk

`func (o *RawWeaponInfoV2Input) GetMBulletSpeedCurveOk() (*RawItemWeaponInfoBulletSpeedCurveV2Input, bool)`

GetMBulletSpeedCurveOk returns a tuple with the MBulletSpeedCurve field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMBulletSpeedCurve

`func (o *RawWeaponInfoV2Input) SetMBulletSpeedCurve(v RawItemWeaponInfoBulletSpeedCurveV2Input)`

SetMBulletSpeedCurve sets MBulletSpeedCurve field to given value.

### HasMBulletSpeedCurve

`func (o *RawWeaponInfoV2Input) HasMBulletSpeedCurve() bool`

HasMBulletSpeedCurve returns a boolean if a field has been set.

### SetMBulletSpeedCurveNil

`func (o *RawWeaponInfoV2Input) SetMBulletSpeedCurveNil(b bool)`

 SetMBulletSpeedCurveNil sets the value for MBulletSpeedCurve to be an explicit nil

### UnsetMBulletSpeedCurve
`func (o *RawWeaponInfoV2Input) UnsetMBulletSpeedCurve()`

UnsetMBulletSpeedCurve ensures that no value is present for MBulletSpeedCurve, not even an explicit nil
### GetMHorizontalRecoil

`func (o *RawWeaponInfoV2Input) GetMHorizontalRecoil() RawWeaponInfoHorizontalRecoilV2Input`

GetMHorizontalRecoil returns the MHorizontalRecoil field if non-nil, zero value otherwise.

### GetMHorizontalRecoilOk

`func (o *RawWeaponInfoV2Input) GetMHorizontalRecoilOk() (*RawWeaponInfoHorizontalRecoilV2Input, bool)`

GetMHorizontalRecoilOk returns a tuple with the MHorizontalRecoil field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMHorizontalRecoil

`func (o *RawWeaponInfoV2Input) SetMHorizontalRecoil(v RawWeaponInfoHorizontalRecoilV2Input)`

SetMHorizontalRecoil sets MHorizontalRecoil field to given value.

### HasMHorizontalRecoil

`func (o *RawWeaponInfoV2Input) HasMHorizontalRecoil() bool`

HasMHorizontalRecoil returns a boolean if a field has been set.

### SetMHorizontalRecoilNil

`func (o *RawWeaponInfoV2Input) SetMHorizontalRecoilNil(b bool)`

 SetMHorizontalRecoilNil sets the value for MHorizontalRecoil to be an explicit nil

### UnsetMHorizontalRecoil
`func (o *RawWeaponInfoV2Input) UnsetMHorizontalRecoil()`

UnsetMHorizontalRecoil ensures that no value is present for MHorizontalRecoil, not even an explicit nil
### GetMVerticalRecoil

`func (o *RawWeaponInfoV2Input) GetMVerticalRecoil() RawWeaponInfoVerticalRecoilV2Input`

GetMVerticalRecoil returns the MVerticalRecoil field if non-nil, zero value otherwise.

### GetMVerticalRecoilOk

`func (o *RawWeaponInfoV2Input) GetMVerticalRecoilOk() (*RawWeaponInfoVerticalRecoilV2Input, bool)`

GetMVerticalRecoilOk returns a tuple with the MVerticalRecoil field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMVerticalRecoil

`func (o *RawWeaponInfoV2Input) SetMVerticalRecoil(v RawWeaponInfoVerticalRecoilV2Input)`

SetMVerticalRecoil sets MVerticalRecoil field to given value.

### HasMVerticalRecoil

`func (o *RawWeaponInfoV2Input) HasMVerticalRecoil() bool`

HasMVerticalRecoil returns a boolean if a field has been set.

### SetMVerticalRecoilNil

`func (o *RawWeaponInfoV2Input) SetMVerticalRecoilNil(b bool)`

 SetMVerticalRecoilNil sets the value for MVerticalRecoil to be an explicit nil

### UnsetMVerticalRecoil
`func (o *RawWeaponInfoV2Input) UnsetMVerticalRecoil()`

UnsetMVerticalRecoil ensures that no value is present for MVerticalRecoil, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


