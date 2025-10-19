# RawWeaponInfoV2Output

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CanZoom** | Pointer to **NullableBool** |  | [optional] 
**BulletDamage** | Pointer to **NullableFloat32** |  | [optional] 
**BulletGravityScale** | Pointer to **NullableFloat32** |  | [optional] 
**BulletInheritShooterVelocityScale** | Pointer to **NullableFloat32** |  | [optional] 
**BulletLifetime** | Pointer to **NullableFloat32** |  | [optional] 
**BulletRadius** | Pointer to **NullableFloat32** |  | [optional] 
**BulletRadiusVsWorld** | Pointer to **NullableFloat32** |  | [optional] 
**BulletReflectAmount** | Pointer to **NullableFloat32** |  | [optional] 
**BulletReflectScale** | Pointer to **NullableFloat32** |  | [optional] 
**BulletWhizDistance** | Pointer to **NullableFloat32** |  | [optional] 
**BurstShotCooldown** | Pointer to **NullableFloat32** |  | [optional] 
**CritBonusAgainstNpcs** | Pointer to **NullableFloat32** |  | [optional] 
**CritBonusEnd** | Pointer to **NullableFloat32** |  | [optional] 
**CritBonusEndRange** | Pointer to **NullableFloat32** |  | [optional] 
**CritBonusStart** | Pointer to **NullableFloat32** |  | [optional] 
**CritBonusStartRange** | Pointer to **NullableFloat32** |  | [optional] 
**CycleTime** | Pointer to **NullableFloat32** |  | [optional] 
**IntraBurstCycleTime** | Pointer to **NullableFloat32** |  | [optional] 
**MaxSpinCycleTime** | Pointer to **NullableFloat32** |  | [optional] 
**DamageFalloffBias** | Pointer to **NullableFloat32** |  | [optional] 
**DamageFalloffEndRange** | Pointer to **NullableFloat32** |  | [optional] 
**DamageFalloffEndScale** | Pointer to **NullableFloat32** |  | [optional] 
**DamageFalloffStartRange** | Pointer to **NullableFloat32** |  | [optional] 
**DamageFalloffStartScale** | Pointer to **NullableFloat32** |  | [optional] 
**HorizontalPunch** | Pointer to **NullableFloat32** |  | [optional] 
**Range** | Pointer to **NullableFloat32** |  | [optional] 
**RecoilRecoveryDelayFactor** | Pointer to **NullableFloat32** |  | [optional] 
**RecoilRecoverySpeed** | Pointer to **NullableFloat32** |  | [optional] 
**RecoilShotIndexRecoveryTimeFactor** | Pointer to **NullableFloat32** |  | [optional] 
**RecoilSpeed** | Pointer to **NullableFloat32** |  | [optional] 
**ReloadMoveSpeed** | Pointer to **NullableFloat32** |  | [optional] 
**ScatterYawScale** | Pointer to **NullableFloat32** |  | [optional] 
**AimingShotSpreadPenalty** | Pointer to [**NullableAimingShotSpreadPenalty**](AimingShotSpreadPenalty.md) |  | [optional] 
**StandingShotSpreadPenalty** | Pointer to [**NullableStandingShotSpreadPenalty**](StandingShotSpreadPenalty.md) |  | [optional] 
**ShootMoveSpeedPercent** | Pointer to **NullableFloat32** |  | [optional] 
**ShootSpreadPenaltyDecay** | Pointer to **NullableFloat32** |  | [optional] 
**ShootSpreadPenaltyDecayDelay** | Pointer to **NullableFloat32** |  | [optional] 
**ShootSpreadPenaltyPerShot** | Pointer to **NullableFloat32** |  | [optional] 
**ShootingUpSpreadPenalty** | Pointer to **NullableFloat32** |  | [optional] 
**VerticalPunch** | Pointer to **NullableFloat32** |  | [optional] 
**ZoomFov** | Pointer to **NullableFloat32** |  | [optional] 
**ZoomMoveSpeedPercent** | Pointer to **NullableFloat32** |  | [optional] 
**Bullets** | Pointer to **NullableInt32** |  | [optional] 
**BurstShotCount** | Pointer to **NullableInt32** |  | [optional] 
**ClipSize** | Pointer to **NullableInt32** |  | [optional] 
**Spread** | Pointer to **NullableFloat32** |  | [optional] 
**StandingSpread** | Pointer to **NullableFloat32** |  | [optional] 
**LowAmmoIndicatorThreshold** | Pointer to **NullableFloat32** |  | [optional] 
**RecoilSeed** | Pointer to **NullableFloat32** |  | [optional] 
**ReloadDuration** | Pointer to **NullableFloat32** |  | [optional] 
**BulletSpeedCurve** | Pointer to [**NullableRawItemWeaponInfoBulletSpeedCurveV2Output**](RawItemWeaponInfoBulletSpeedCurveV2Output.md) |  | [optional] 
**HorizontalRecoil** | Pointer to [**NullableRawWeaponInfoHorizontalRecoilV2Output**](RawWeaponInfoHorizontalRecoilV2Output.md) |  | [optional] 
**VerticalRecoil** | Pointer to [**NullableRawWeaponInfoVerticalRecoilV2Output**](RawWeaponInfoVerticalRecoilV2Output.md) |  | [optional] 

## Methods

### NewRawWeaponInfoV2Output

`func NewRawWeaponInfoV2Output() *RawWeaponInfoV2Output`

NewRawWeaponInfoV2Output instantiates a new RawWeaponInfoV2Output object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRawWeaponInfoV2OutputWithDefaults

`func NewRawWeaponInfoV2OutputWithDefaults() *RawWeaponInfoV2Output`

NewRawWeaponInfoV2OutputWithDefaults instantiates a new RawWeaponInfoV2Output object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCanZoom

`func (o *RawWeaponInfoV2Output) GetCanZoom() bool`

GetCanZoom returns the CanZoom field if non-nil, zero value otherwise.

### GetCanZoomOk

`func (o *RawWeaponInfoV2Output) GetCanZoomOk() (*bool, bool)`

GetCanZoomOk returns a tuple with the CanZoom field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCanZoom

`func (o *RawWeaponInfoV2Output) SetCanZoom(v bool)`

SetCanZoom sets CanZoom field to given value.

### HasCanZoom

`func (o *RawWeaponInfoV2Output) HasCanZoom() bool`

HasCanZoom returns a boolean if a field has been set.

### SetCanZoomNil

`func (o *RawWeaponInfoV2Output) SetCanZoomNil(b bool)`

 SetCanZoomNil sets the value for CanZoom to be an explicit nil

### UnsetCanZoom
`func (o *RawWeaponInfoV2Output) UnsetCanZoom()`

UnsetCanZoom ensures that no value is present for CanZoom, not even an explicit nil
### GetBulletDamage

`func (o *RawWeaponInfoV2Output) GetBulletDamage() float32`

GetBulletDamage returns the BulletDamage field if non-nil, zero value otherwise.

### GetBulletDamageOk

`func (o *RawWeaponInfoV2Output) GetBulletDamageOk() (*float32, bool)`

GetBulletDamageOk returns a tuple with the BulletDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletDamage

`func (o *RawWeaponInfoV2Output) SetBulletDamage(v float32)`

SetBulletDamage sets BulletDamage field to given value.

### HasBulletDamage

`func (o *RawWeaponInfoV2Output) HasBulletDamage() bool`

HasBulletDamage returns a boolean if a field has been set.

### SetBulletDamageNil

`func (o *RawWeaponInfoV2Output) SetBulletDamageNil(b bool)`

 SetBulletDamageNil sets the value for BulletDamage to be an explicit nil

### UnsetBulletDamage
`func (o *RawWeaponInfoV2Output) UnsetBulletDamage()`

UnsetBulletDamage ensures that no value is present for BulletDamage, not even an explicit nil
### GetBulletGravityScale

`func (o *RawWeaponInfoV2Output) GetBulletGravityScale() float32`

GetBulletGravityScale returns the BulletGravityScale field if non-nil, zero value otherwise.

### GetBulletGravityScaleOk

`func (o *RawWeaponInfoV2Output) GetBulletGravityScaleOk() (*float32, bool)`

GetBulletGravityScaleOk returns a tuple with the BulletGravityScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletGravityScale

`func (o *RawWeaponInfoV2Output) SetBulletGravityScale(v float32)`

SetBulletGravityScale sets BulletGravityScale field to given value.

### HasBulletGravityScale

`func (o *RawWeaponInfoV2Output) HasBulletGravityScale() bool`

HasBulletGravityScale returns a boolean if a field has been set.

### SetBulletGravityScaleNil

`func (o *RawWeaponInfoV2Output) SetBulletGravityScaleNil(b bool)`

 SetBulletGravityScaleNil sets the value for BulletGravityScale to be an explicit nil

### UnsetBulletGravityScale
`func (o *RawWeaponInfoV2Output) UnsetBulletGravityScale()`

UnsetBulletGravityScale ensures that no value is present for BulletGravityScale, not even an explicit nil
### GetBulletInheritShooterVelocityScale

`func (o *RawWeaponInfoV2Output) GetBulletInheritShooterVelocityScale() float32`

GetBulletInheritShooterVelocityScale returns the BulletInheritShooterVelocityScale field if non-nil, zero value otherwise.

### GetBulletInheritShooterVelocityScaleOk

`func (o *RawWeaponInfoV2Output) GetBulletInheritShooterVelocityScaleOk() (*float32, bool)`

GetBulletInheritShooterVelocityScaleOk returns a tuple with the BulletInheritShooterVelocityScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletInheritShooterVelocityScale

`func (o *RawWeaponInfoV2Output) SetBulletInheritShooterVelocityScale(v float32)`

SetBulletInheritShooterVelocityScale sets BulletInheritShooterVelocityScale field to given value.

### HasBulletInheritShooterVelocityScale

`func (o *RawWeaponInfoV2Output) HasBulletInheritShooterVelocityScale() bool`

HasBulletInheritShooterVelocityScale returns a boolean if a field has been set.

### SetBulletInheritShooterVelocityScaleNil

`func (o *RawWeaponInfoV2Output) SetBulletInheritShooterVelocityScaleNil(b bool)`

 SetBulletInheritShooterVelocityScaleNil sets the value for BulletInheritShooterVelocityScale to be an explicit nil

### UnsetBulletInheritShooterVelocityScale
`func (o *RawWeaponInfoV2Output) UnsetBulletInheritShooterVelocityScale()`

UnsetBulletInheritShooterVelocityScale ensures that no value is present for BulletInheritShooterVelocityScale, not even an explicit nil
### GetBulletLifetime

`func (o *RawWeaponInfoV2Output) GetBulletLifetime() float32`

GetBulletLifetime returns the BulletLifetime field if non-nil, zero value otherwise.

### GetBulletLifetimeOk

`func (o *RawWeaponInfoV2Output) GetBulletLifetimeOk() (*float32, bool)`

GetBulletLifetimeOk returns a tuple with the BulletLifetime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletLifetime

`func (o *RawWeaponInfoV2Output) SetBulletLifetime(v float32)`

SetBulletLifetime sets BulletLifetime field to given value.

### HasBulletLifetime

`func (o *RawWeaponInfoV2Output) HasBulletLifetime() bool`

HasBulletLifetime returns a boolean if a field has been set.

### SetBulletLifetimeNil

`func (o *RawWeaponInfoV2Output) SetBulletLifetimeNil(b bool)`

 SetBulletLifetimeNil sets the value for BulletLifetime to be an explicit nil

### UnsetBulletLifetime
`func (o *RawWeaponInfoV2Output) UnsetBulletLifetime()`

UnsetBulletLifetime ensures that no value is present for BulletLifetime, not even an explicit nil
### GetBulletRadius

`func (o *RawWeaponInfoV2Output) GetBulletRadius() float32`

GetBulletRadius returns the BulletRadius field if non-nil, zero value otherwise.

### GetBulletRadiusOk

`func (o *RawWeaponInfoV2Output) GetBulletRadiusOk() (*float32, bool)`

GetBulletRadiusOk returns a tuple with the BulletRadius field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletRadius

`func (o *RawWeaponInfoV2Output) SetBulletRadius(v float32)`

SetBulletRadius sets BulletRadius field to given value.

### HasBulletRadius

`func (o *RawWeaponInfoV2Output) HasBulletRadius() bool`

HasBulletRadius returns a boolean if a field has been set.

### SetBulletRadiusNil

`func (o *RawWeaponInfoV2Output) SetBulletRadiusNil(b bool)`

 SetBulletRadiusNil sets the value for BulletRadius to be an explicit nil

### UnsetBulletRadius
`func (o *RawWeaponInfoV2Output) UnsetBulletRadius()`

UnsetBulletRadius ensures that no value is present for BulletRadius, not even an explicit nil
### GetBulletRadiusVsWorld

`func (o *RawWeaponInfoV2Output) GetBulletRadiusVsWorld() float32`

GetBulletRadiusVsWorld returns the BulletRadiusVsWorld field if non-nil, zero value otherwise.

### GetBulletRadiusVsWorldOk

`func (o *RawWeaponInfoV2Output) GetBulletRadiusVsWorldOk() (*float32, bool)`

GetBulletRadiusVsWorldOk returns a tuple with the BulletRadiusVsWorld field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletRadiusVsWorld

`func (o *RawWeaponInfoV2Output) SetBulletRadiusVsWorld(v float32)`

SetBulletRadiusVsWorld sets BulletRadiusVsWorld field to given value.

### HasBulletRadiusVsWorld

`func (o *RawWeaponInfoV2Output) HasBulletRadiusVsWorld() bool`

HasBulletRadiusVsWorld returns a boolean if a field has been set.

### SetBulletRadiusVsWorldNil

`func (o *RawWeaponInfoV2Output) SetBulletRadiusVsWorldNil(b bool)`

 SetBulletRadiusVsWorldNil sets the value for BulletRadiusVsWorld to be an explicit nil

### UnsetBulletRadiusVsWorld
`func (o *RawWeaponInfoV2Output) UnsetBulletRadiusVsWorld()`

UnsetBulletRadiusVsWorld ensures that no value is present for BulletRadiusVsWorld, not even an explicit nil
### GetBulletReflectAmount

`func (o *RawWeaponInfoV2Output) GetBulletReflectAmount() float32`

GetBulletReflectAmount returns the BulletReflectAmount field if non-nil, zero value otherwise.

### GetBulletReflectAmountOk

`func (o *RawWeaponInfoV2Output) GetBulletReflectAmountOk() (*float32, bool)`

GetBulletReflectAmountOk returns a tuple with the BulletReflectAmount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletReflectAmount

`func (o *RawWeaponInfoV2Output) SetBulletReflectAmount(v float32)`

SetBulletReflectAmount sets BulletReflectAmount field to given value.

### HasBulletReflectAmount

`func (o *RawWeaponInfoV2Output) HasBulletReflectAmount() bool`

HasBulletReflectAmount returns a boolean if a field has been set.

### SetBulletReflectAmountNil

`func (o *RawWeaponInfoV2Output) SetBulletReflectAmountNil(b bool)`

 SetBulletReflectAmountNil sets the value for BulletReflectAmount to be an explicit nil

### UnsetBulletReflectAmount
`func (o *RawWeaponInfoV2Output) UnsetBulletReflectAmount()`

UnsetBulletReflectAmount ensures that no value is present for BulletReflectAmount, not even an explicit nil
### GetBulletReflectScale

`func (o *RawWeaponInfoV2Output) GetBulletReflectScale() float32`

GetBulletReflectScale returns the BulletReflectScale field if non-nil, zero value otherwise.

### GetBulletReflectScaleOk

`func (o *RawWeaponInfoV2Output) GetBulletReflectScaleOk() (*float32, bool)`

GetBulletReflectScaleOk returns a tuple with the BulletReflectScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletReflectScale

`func (o *RawWeaponInfoV2Output) SetBulletReflectScale(v float32)`

SetBulletReflectScale sets BulletReflectScale field to given value.

### HasBulletReflectScale

`func (o *RawWeaponInfoV2Output) HasBulletReflectScale() bool`

HasBulletReflectScale returns a boolean if a field has been set.

### SetBulletReflectScaleNil

`func (o *RawWeaponInfoV2Output) SetBulletReflectScaleNil(b bool)`

 SetBulletReflectScaleNil sets the value for BulletReflectScale to be an explicit nil

### UnsetBulletReflectScale
`func (o *RawWeaponInfoV2Output) UnsetBulletReflectScale()`

UnsetBulletReflectScale ensures that no value is present for BulletReflectScale, not even an explicit nil
### GetBulletWhizDistance

`func (o *RawWeaponInfoV2Output) GetBulletWhizDistance() float32`

GetBulletWhizDistance returns the BulletWhizDistance field if non-nil, zero value otherwise.

### GetBulletWhizDistanceOk

`func (o *RawWeaponInfoV2Output) GetBulletWhizDistanceOk() (*float32, bool)`

GetBulletWhizDistanceOk returns a tuple with the BulletWhizDistance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletWhizDistance

`func (o *RawWeaponInfoV2Output) SetBulletWhizDistance(v float32)`

SetBulletWhizDistance sets BulletWhizDistance field to given value.

### HasBulletWhizDistance

`func (o *RawWeaponInfoV2Output) HasBulletWhizDistance() bool`

HasBulletWhizDistance returns a boolean if a field has been set.

### SetBulletWhizDistanceNil

`func (o *RawWeaponInfoV2Output) SetBulletWhizDistanceNil(b bool)`

 SetBulletWhizDistanceNil sets the value for BulletWhizDistance to be an explicit nil

### UnsetBulletWhizDistance
`func (o *RawWeaponInfoV2Output) UnsetBulletWhizDistance()`

UnsetBulletWhizDistance ensures that no value is present for BulletWhizDistance, not even an explicit nil
### GetBurstShotCooldown

`func (o *RawWeaponInfoV2Output) GetBurstShotCooldown() float32`

GetBurstShotCooldown returns the BurstShotCooldown field if non-nil, zero value otherwise.

### GetBurstShotCooldownOk

`func (o *RawWeaponInfoV2Output) GetBurstShotCooldownOk() (*float32, bool)`

GetBurstShotCooldownOk returns a tuple with the BurstShotCooldown field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBurstShotCooldown

`func (o *RawWeaponInfoV2Output) SetBurstShotCooldown(v float32)`

SetBurstShotCooldown sets BurstShotCooldown field to given value.

### HasBurstShotCooldown

`func (o *RawWeaponInfoV2Output) HasBurstShotCooldown() bool`

HasBurstShotCooldown returns a boolean if a field has been set.

### SetBurstShotCooldownNil

`func (o *RawWeaponInfoV2Output) SetBurstShotCooldownNil(b bool)`

 SetBurstShotCooldownNil sets the value for BurstShotCooldown to be an explicit nil

### UnsetBurstShotCooldown
`func (o *RawWeaponInfoV2Output) UnsetBurstShotCooldown()`

UnsetBurstShotCooldown ensures that no value is present for BurstShotCooldown, not even an explicit nil
### GetCritBonusAgainstNpcs

`func (o *RawWeaponInfoV2Output) GetCritBonusAgainstNpcs() float32`

GetCritBonusAgainstNpcs returns the CritBonusAgainstNpcs field if non-nil, zero value otherwise.

### GetCritBonusAgainstNpcsOk

`func (o *RawWeaponInfoV2Output) GetCritBonusAgainstNpcsOk() (*float32, bool)`

GetCritBonusAgainstNpcsOk returns a tuple with the CritBonusAgainstNpcs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCritBonusAgainstNpcs

`func (o *RawWeaponInfoV2Output) SetCritBonusAgainstNpcs(v float32)`

SetCritBonusAgainstNpcs sets CritBonusAgainstNpcs field to given value.

### HasCritBonusAgainstNpcs

`func (o *RawWeaponInfoV2Output) HasCritBonusAgainstNpcs() bool`

HasCritBonusAgainstNpcs returns a boolean if a field has been set.

### SetCritBonusAgainstNpcsNil

`func (o *RawWeaponInfoV2Output) SetCritBonusAgainstNpcsNil(b bool)`

 SetCritBonusAgainstNpcsNil sets the value for CritBonusAgainstNpcs to be an explicit nil

### UnsetCritBonusAgainstNpcs
`func (o *RawWeaponInfoV2Output) UnsetCritBonusAgainstNpcs()`

UnsetCritBonusAgainstNpcs ensures that no value is present for CritBonusAgainstNpcs, not even an explicit nil
### GetCritBonusEnd

`func (o *RawWeaponInfoV2Output) GetCritBonusEnd() float32`

GetCritBonusEnd returns the CritBonusEnd field if non-nil, zero value otherwise.

### GetCritBonusEndOk

`func (o *RawWeaponInfoV2Output) GetCritBonusEndOk() (*float32, bool)`

GetCritBonusEndOk returns a tuple with the CritBonusEnd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCritBonusEnd

`func (o *RawWeaponInfoV2Output) SetCritBonusEnd(v float32)`

SetCritBonusEnd sets CritBonusEnd field to given value.

### HasCritBonusEnd

`func (o *RawWeaponInfoV2Output) HasCritBonusEnd() bool`

HasCritBonusEnd returns a boolean if a field has been set.

### SetCritBonusEndNil

`func (o *RawWeaponInfoV2Output) SetCritBonusEndNil(b bool)`

 SetCritBonusEndNil sets the value for CritBonusEnd to be an explicit nil

### UnsetCritBonusEnd
`func (o *RawWeaponInfoV2Output) UnsetCritBonusEnd()`

UnsetCritBonusEnd ensures that no value is present for CritBonusEnd, not even an explicit nil
### GetCritBonusEndRange

`func (o *RawWeaponInfoV2Output) GetCritBonusEndRange() float32`

GetCritBonusEndRange returns the CritBonusEndRange field if non-nil, zero value otherwise.

### GetCritBonusEndRangeOk

`func (o *RawWeaponInfoV2Output) GetCritBonusEndRangeOk() (*float32, bool)`

GetCritBonusEndRangeOk returns a tuple with the CritBonusEndRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCritBonusEndRange

`func (o *RawWeaponInfoV2Output) SetCritBonusEndRange(v float32)`

SetCritBonusEndRange sets CritBonusEndRange field to given value.

### HasCritBonusEndRange

`func (o *RawWeaponInfoV2Output) HasCritBonusEndRange() bool`

HasCritBonusEndRange returns a boolean if a field has been set.

### SetCritBonusEndRangeNil

`func (o *RawWeaponInfoV2Output) SetCritBonusEndRangeNil(b bool)`

 SetCritBonusEndRangeNil sets the value for CritBonusEndRange to be an explicit nil

### UnsetCritBonusEndRange
`func (o *RawWeaponInfoV2Output) UnsetCritBonusEndRange()`

UnsetCritBonusEndRange ensures that no value is present for CritBonusEndRange, not even an explicit nil
### GetCritBonusStart

`func (o *RawWeaponInfoV2Output) GetCritBonusStart() float32`

GetCritBonusStart returns the CritBonusStart field if non-nil, zero value otherwise.

### GetCritBonusStartOk

`func (o *RawWeaponInfoV2Output) GetCritBonusStartOk() (*float32, bool)`

GetCritBonusStartOk returns a tuple with the CritBonusStart field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCritBonusStart

`func (o *RawWeaponInfoV2Output) SetCritBonusStart(v float32)`

SetCritBonusStart sets CritBonusStart field to given value.

### HasCritBonusStart

`func (o *RawWeaponInfoV2Output) HasCritBonusStart() bool`

HasCritBonusStart returns a boolean if a field has been set.

### SetCritBonusStartNil

`func (o *RawWeaponInfoV2Output) SetCritBonusStartNil(b bool)`

 SetCritBonusStartNil sets the value for CritBonusStart to be an explicit nil

### UnsetCritBonusStart
`func (o *RawWeaponInfoV2Output) UnsetCritBonusStart()`

UnsetCritBonusStart ensures that no value is present for CritBonusStart, not even an explicit nil
### GetCritBonusStartRange

`func (o *RawWeaponInfoV2Output) GetCritBonusStartRange() float32`

GetCritBonusStartRange returns the CritBonusStartRange field if non-nil, zero value otherwise.

### GetCritBonusStartRangeOk

`func (o *RawWeaponInfoV2Output) GetCritBonusStartRangeOk() (*float32, bool)`

GetCritBonusStartRangeOk returns a tuple with the CritBonusStartRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCritBonusStartRange

`func (o *RawWeaponInfoV2Output) SetCritBonusStartRange(v float32)`

SetCritBonusStartRange sets CritBonusStartRange field to given value.

### HasCritBonusStartRange

`func (o *RawWeaponInfoV2Output) HasCritBonusStartRange() bool`

HasCritBonusStartRange returns a boolean if a field has been set.

### SetCritBonusStartRangeNil

`func (o *RawWeaponInfoV2Output) SetCritBonusStartRangeNil(b bool)`

 SetCritBonusStartRangeNil sets the value for CritBonusStartRange to be an explicit nil

### UnsetCritBonusStartRange
`func (o *RawWeaponInfoV2Output) UnsetCritBonusStartRange()`

UnsetCritBonusStartRange ensures that no value is present for CritBonusStartRange, not even an explicit nil
### GetCycleTime

`func (o *RawWeaponInfoV2Output) GetCycleTime() float32`

GetCycleTime returns the CycleTime field if non-nil, zero value otherwise.

### GetCycleTimeOk

`func (o *RawWeaponInfoV2Output) GetCycleTimeOk() (*float32, bool)`

GetCycleTimeOk returns a tuple with the CycleTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCycleTime

`func (o *RawWeaponInfoV2Output) SetCycleTime(v float32)`

SetCycleTime sets CycleTime field to given value.

### HasCycleTime

`func (o *RawWeaponInfoV2Output) HasCycleTime() bool`

HasCycleTime returns a boolean if a field has been set.

### SetCycleTimeNil

`func (o *RawWeaponInfoV2Output) SetCycleTimeNil(b bool)`

 SetCycleTimeNil sets the value for CycleTime to be an explicit nil

### UnsetCycleTime
`func (o *RawWeaponInfoV2Output) UnsetCycleTime()`

UnsetCycleTime ensures that no value is present for CycleTime, not even an explicit nil
### GetIntraBurstCycleTime

`func (o *RawWeaponInfoV2Output) GetIntraBurstCycleTime() float32`

GetIntraBurstCycleTime returns the IntraBurstCycleTime field if non-nil, zero value otherwise.

### GetIntraBurstCycleTimeOk

`func (o *RawWeaponInfoV2Output) GetIntraBurstCycleTimeOk() (*float32, bool)`

GetIntraBurstCycleTimeOk returns a tuple with the IntraBurstCycleTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIntraBurstCycleTime

`func (o *RawWeaponInfoV2Output) SetIntraBurstCycleTime(v float32)`

SetIntraBurstCycleTime sets IntraBurstCycleTime field to given value.

### HasIntraBurstCycleTime

`func (o *RawWeaponInfoV2Output) HasIntraBurstCycleTime() bool`

HasIntraBurstCycleTime returns a boolean if a field has been set.

### SetIntraBurstCycleTimeNil

`func (o *RawWeaponInfoV2Output) SetIntraBurstCycleTimeNil(b bool)`

 SetIntraBurstCycleTimeNil sets the value for IntraBurstCycleTime to be an explicit nil

### UnsetIntraBurstCycleTime
`func (o *RawWeaponInfoV2Output) UnsetIntraBurstCycleTime()`

UnsetIntraBurstCycleTime ensures that no value is present for IntraBurstCycleTime, not even an explicit nil
### GetMaxSpinCycleTime

`func (o *RawWeaponInfoV2Output) GetMaxSpinCycleTime() float32`

GetMaxSpinCycleTime returns the MaxSpinCycleTime field if non-nil, zero value otherwise.

### GetMaxSpinCycleTimeOk

`func (o *RawWeaponInfoV2Output) GetMaxSpinCycleTimeOk() (*float32, bool)`

GetMaxSpinCycleTimeOk returns a tuple with the MaxSpinCycleTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxSpinCycleTime

`func (o *RawWeaponInfoV2Output) SetMaxSpinCycleTime(v float32)`

SetMaxSpinCycleTime sets MaxSpinCycleTime field to given value.

### HasMaxSpinCycleTime

`func (o *RawWeaponInfoV2Output) HasMaxSpinCycleTime() bool`

HasMaxSpinCycleTime returns a boolean if a field has been set.

### SetMaxSpinCycleTimeNil

`func (o *RawWeaponInfoV2Output) SetMaxSpinCycleTimeNil(b bool)`

 SetMaxSpinCycleTimeNil sets the value for MaxSpinCycleTime to be an explicit nil

### UnsetMaxSpinCycleTime
`func (o *RawWeaponInfoV2Output) UnsetMaxSpinCycleTime()`

UnsetMaxSpinCycleTime ensures that no value is present for MaxSpinCycleTime, not even an explicit nil
### GetDamageFalloffBias

`func (o *RawWeaponInfoV2Output) GetDamageFalloffBias() float32`

GetDamageFalloffBias returns the DamageFalloffBias field if non-nil, zero value otherwise.

### GetDamageFalloffBiasOk

`func (o *RawWeaponInfoV2Output) GetDamageFalloffBiasOk() (*float32, bool)`

GetDamageFalloffBiasOk returns a tuple with the DamageFalloffBias field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamageFalloffBias

`func (o *RawWeaponInfoV2Output) SetDamageFalloffBias(v float32)`

SetDamageFalloffBias sets DamageFalloffBias field to given value.

### HasDamageFalloffBias

`func (o *RawWeaponInfoV2Output) HasDamageFalloffBias() bool`

HasDamageFalloffBias returns a boolean if a field has been set.

### SetDamageFalloffBiasNil

`func (o *RawWeaponInfoV2Output) SetDamageFalloffBiasNil(b bool)`

 SetDamageFalloffBiasNil sets the value for DamageFalloffBias to be an explicit nil

### UnsetDamageFalloffBias
`func (o *RawWeaponInfoV2Output) UnsetDamageFalloffBias()`

UnsetDamageFalloffBias ensures that no value is present for DamageFalloffBias, not even an explicit nil
### GetDamageFalloffEndRange

`func (o *RawWeaponInfoV2Output) GetDamageFalloffEndRange() float32`

GetDamageFalloffEndRange returns the DamageFalloffEndRange field if non-nil, zero value otherwise.

### GetDamageFalloffEndRangeOk

`func (o *RawWeaponInfoV2Output) GetDamageFalloffEndRangeOk() (*float32, bool)`

GetDamageFalloffEndRangeOk returns a tuple with the DamageFalloffEndRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamageFalloffEndRange

`func (o *RawWeaponInfoV2Output) SetDamageFalloffEndRange(v float32)`

SetDamageFalloffEndRange sets DamageFalloffEndRange field to given value.

### HasDamageFalloffEndRange

`func (o *RawWeaponInfoV2Output) HasDamageFalloffEndRange() bool`

HasDamageFalloffEndRange returns a boolean if a field has been set.

### SetDamageFalloffEndRangeNil

`func (o *RawWeaponInfoV2Output) SetDamageFalloffEndRangeNil(b bool)`

 SetDamageFalloffEndRangeNil sets the value for DamageFalloffEndRange to be an explicit nil

### UnsetDamageFalloffEndRange
`func (o *RawWeaponInfoV2Output) UnsetDamageFalloffEndRange()`

UnsetDamageFalloffEndRange ensures that no value is present for DamageFalloffEndRange, not even an explicit nil
### GetDamageFalloffEndScale

`func (o *RawWeaponInfoV2Output) GetDamageFalloffEndScale() float32`

GetDamageFalloffEndScale returns the DamageFalloffEndScale field if non-nil, zero value otherwise.

### GetDamageFalloffEndScaleOk

`func (o *RawWeaponInfoV2Output) GetDamageFalloffEndScaleOk() (*float32, bool)`

GetDamageFalloffEndScaleOk returns a tuple with the DamageFalloffEndScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamageFalloffEndScale

`func (o *RawWeaponInfoV2Output) SetDamageFalloffEndScale(v float32)`

SetDamageFalloffEndScale sets DamageFalloffEndScale field to given value.

### HasDamageFalloffEndScale

`func (o *RawWeaponInfoV2Output) HasDamageFalloffEndScale() bool`

HasDamageFalloffEndScale returns a boolean if a field has been set.

### SetDamageFalloffEndScaleNil

`func (o *RawWeaponInfoV2Output) SetDamageFalloffEndScaleNil(b bool)`

 SetDamageFalloffEndScaleNil sets the value for DamageFalloffEndScale to be an explicit nil

### UnsetDamageFalloffEndScale
`func (o *RawWeaponInfoV2Output) UnsetDamageFalloffEndScale()`

UnsetDamageFalloffEndScale ensures that no value is present for DamageFalloffEndScale, not even an explicit nil
### GetDamageFalloffStartRange

`func (o *RawWeaponInfoV2Output) GetDamageFalloffStartRange() float32`

GetDamageFalloffStartRange returns the DamageFalloffStartRange field if non-nil, zero value otherwise.

### GetDamageFalloffStartRangeOk

`func (o *RawWeaponInfoV2Output) GetDamageFalloffStartRangeOk() (*float32, bool)`

GetDamageFalloffStartRangeOk returns a tuple with the DamageFalloffStartRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamageFalloffStartRange

`func (o *RawWeaponInfoV2Output) SetDamageFalloffStartRange(v float32)`

SetDamageFalloffStartRange sets DamageFalloffStartRange field to given value.

### HasDamageFalloffStartRange

`func (o *RawWeaponInfoV2Output) HasDamageFalloffStartRange() bool`

HasDamageFalloffStartRange returns a boolean if a field has been set.

### SetDamageFalloffStartRangeNil

`func (o *RawWeaponInfoV2Output) SetDamageFalloffStartRangeNil(b bool)`

 SetDamageFalloffStartRangeNil sets the value for DamageFalloffStartRange to be an explicit nil

### UnsetDamageFalloffStartRange
`func (o *RawWeaponInfoV2Output) UnsetDamageFalloffStartRange()`

UnsetDamageFalloffStartRange ensures that no value is present for DamageFalloffStartRange, not even an explicit nil
### GetDamageFalloffStartScale

`func (o *RawWeaponInfoV2Output) GetDamageFalloffStartScale() float32`

GetDamageFalloffStartScale returns the DamageFalloffStartScale field if non-nil, zero value otherwise.

### GetDamageFalloffStartScaleOk

`func (o *RawWeaponInfoV2Output) GetDamageFalloffStartScaleOk() (*float32, bool)`

GetDamageFalloffStartScaleOk returns a tuple with the DamageFalloffStartScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamageFalloffStartScale

`func (o *RawWeaponInfoV2Output) SetDamageFalloffStartScale(v float32)`

SetDamageFalloffStartScale sets DamageFalloffStartScale field to given value.

### HasDamageFalloffStartScale

`func (o *RawWeaponInfoV2Output) HasDamageFalloffStartScale() bool`

HasDamageFalloffStartScale returns a boolean if a field has been set.

### SetDamageFalloffStartScaleNil

`func (o *RawWeaponInfoV2Output) SetDamageFalloffStartScaleNil(b bool)`

 SetDamageFalloffStartScaleNil sets the value for DamageFalloffStartScale to be an explicit nil

### UnsetDamageFalloffStartScale
`func (o *RawWeaponInfoV2Output) UnsetDamageFalloffStartScale()`

UnsetDamageFalloffStartScale ensures that no value is present for DamageFalloffStartScale, not even an explicit nil
### GetHorizontalPunch

`func (o *RawWeaponInfoV2Output) GetHorizontalPunch() float32`

GetHorizontalPunch returns the HorizontalPunch field if non-nil, zero value otherwise.

### GetHorizontalPunchOk

`func (o *RawWeaponInfoV2Output) GetHorizontalPunchOk() (*float32, bool)`

GetHorizontalPunchOk returns a tuple with the HorizontalPunch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHorizontalPunch

`func (o *RawWeaponInfoV2Output) SetHorizontalPunch(v float32)`

SetHorizontalPunch sets HorizontalPunch field to given value.

### HasHorizontalPunch

`func (o *RawWeaponInfoV2Output) HasHorizontalPunch() bool`

HasHorizontalPunch returns a boolean if a field has been set.

### SetHorizontalPunchNil

`func (o *RawWeaponInfoV2Output) SetHorizontalPunchNil(b bool)`

 SetHorizontalPunchNil sets the value for HorizontalPunch to be an explicit nil

### UnsetHorizontalPunch
`func (o *RawWeaponInfoV2Output) UnsetHorizontalPunch()`

UnsetHorizontalPunch ensures that no value is present for HorizontalPunch, not even an explicit nil
### GetRange

`func (o *RawWeaponInfoV2Output) GetRange() float32`

GetRange returns the Range field if non-nil, zero value otherwise.

### GetRangeOk

`func (o *RawWeaponInfoV2Output) GetRangeOk() (*float32, bool)`

GetRangeOk returns a tuple with the Range field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRange

`func (o *RawWeaponInfoV2Output) SetRange(v float32)`

SetRange sets Range field to given value.

### HasRange

`func (o *RawWeaponInfoV2Output) HasRange() bool`

HasRange returns a boolean if a field has been set.

### SetRangeNil

`func (o *RawWeaponInfoV2Output) SetRangeNil(b bool)`

 SetRangeNil sets the value for Range to be an explicit nil

### UnsetRange
`func (o *RawWeaponInfoV2Output) UnsetRange()`

UnsetRange ensures that no value is present for Range, not even an explicit nil
### GetRecoilRecoveryDelayFactor

`func (o *RawWeaponInfoV2Output) GetRecoilRecoveryDelayFactor() float32`

GetRecoilRecoveryDelayFactor returns the RecoilRecoveryDelayFactor field if non-nil, zero value otherwise.

### GetRecoilRecoveryDelayFactorOk

`func (o *RawWeaponInfoV2Output) GetRecoilRecoveryDelayFactorOk() (*float32, bool)`

GetRecoilRecoveryDelayFactorOk returns a tuple with the RecoilRecoveryDelayFactor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecoilRecoveryDelayFactor

`func (o *RawWeaponInfoV2Output) SetRecoilRecoveryDelayFactor(v float32)`

SetRecoilRecoveryDelayFactor sets RecoilRecoveryDelayFactor field to given value.

### HasRecoilRecoveryDelayFactor

`func (o *RawWeaponInfoV2Output) HasRecoilRecoveryDelayFactor() bool`

HasRecoilRecoveryDelayFactor returns a boolean if a field has been set.

### SetRecoilRecoveryDelayFactorNil

`func (o *RawWeaponInfoV2Output) SetRecoilRecoveryDelayFactorNil(b bool)`

 SetRecoilRecoveryDelayFactorNil sets the value for RecoilRecoveryDelayFactor to be an explicit nil

### UnsetRecoilRecoveryDelayFactor
`func (o *RawWeaponInfoV2Output) UnsetRecoilRecoveryDelayFactor()`

UnsetRecoilRecoveryDelayFactor ensures that no value is present for RecoilRecoveryDelayFactor, not even an explicit nil
### GetRecoilRecoverySpeed

`func (o *RawWeaponInfoV2Output) GetRecoilRecoverySpeed() float32`

GetRecoilRecoverySpeed returns the RecoilRecoverySpeed field if non-nil, zero value otherwise.

### GetRecoilRecoverySpeedOk

`func (o *RawWeaponInfoV2Output) GetRecoilRecoverySpeedOk() (*float32, bool)`

GetRecoilRecoverySpeedOk returns a tuple with the RecoilRecoverySpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecoilRecoverySpeed

`func (o *RawWeaponInfoV2Output) SetRecoilRecoverySpeed(v float32)`

SetRecoilRecoverySpeed sets RecoilRecoverySpeed field to given value.

### HasRecoilRecoverySpeed

`func (o *RawWeaponInfoV2Output) HasRecoilRecoverySpeed() bool`

HasRecoilRecoverySpeed returns a boolean if a field has been set.

### SetRecoilRecoverySpeedNil

`func (o *RawWeaponInfoV2Output) SetRecoilRecoverySpeedNil(b bool)`

 SetRecoilRecoverySpeedNil sets the value for RecoilRecoverySpeed to be an explicit nil

### UnsetRecoilRecoverySpeed
`func (o *RawWeaponInfoV2Output) UnsetRecoilRecoverySpeed()`

UnsetRecoilRecoverySpeed ensures that no value is present for RecoilRecoverySpeed, not even an explicit nil
### GetRecoilShotIndexRecoveryTimeFactor

`func (o *RawWeaponInfoV2Output) GetRecoilShotIndexRecoveryTimeFactor() float32`

GetRecoilShotIndexRecoveryTimeFactor returns the RecoilShotIndexRecoveryTimeFactor field if non-nil, zero value otherwise.

### GetRecoilShotIndexRecoveryTimeFactorOk

`func (o *RawWeaponInfoV2Output) GetRecoilShotIndexRecoveryTimeFactorOk() (*float32, bool)`

GetRecoilShotIndexRecoveryTimeFactorOk returns a tuple with the RecoilShotIndexRecoveryTimeFactor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecoilShotIndexRecoveryTimeFactor

`func (o *RawWeaponInfoV2Output) SetRecoilShotIndexRecoveryTimeFactor(v float32)`

SetRecoilShotIndexRecoveryTimeFactor sets RecoilShotIndexRecoveryTimeFactor field to given value.

### HasRecoilShotIndexRecoveryTimeFactor

`func (o *RawWeaponInfoV2Output) HasRecoilShotIndexRecoveryTimeFactor() bool`

HasRecoilShotIndexRecoveryTimeFactor returns a boolean if a field has been set.

### SetRecoilShotIndexRecoveryTimeFactorNil

`func (o *RawWeaponInfoV2Output) SetRecoilShotIndexRecoveryTimeFactorNil(b bool)`

 SetRecoilShotIndexRecoveryTimeFactorNil sets the value for RecoilShotIndexRecoveryTimeFactor to be an explicit nil

### UnsetRecoilShotIndexRecoveryTimeFactor
`func (o *RawWeaponInfoV2Output) UnsetRecoilShotIndexRecoveryTimeFactor()`

UnsetRecoilShotIndexRecoveryTimeFactor ensures that no value is present for RecoilShotIndexRecoveryTimeFactor, not even an explicit nil
### GetRecoilSpeed

`func (o *RawWeaponInfoV2Output) GetRecoilSpeed() float32`

GetRecoilSpeed returns the RecoilSpeed field if non-nil, zero value otherwise.

### GetRecoilSpeedOk

`func (o *RawWeaponInfoV2Output) GetRecoilSpeedOk() (*float32, bool)`

GetRecoilSpeedOk returns a tuple with the RecoilSpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecoilSpeed

`func (o *RawWeaponInfoV2Output) SetRecoilSpeed(v float32)`

SetRecoilSpeed sets RecoilSpeed field to given value.

### HasRecoilSpeed

`func (o *RawWeaponInfoV2Output) HasRecoilSpeed() bool`

HasRecoilSpeed returns a boolean if a field has been set.

### SetRecoilSpeedNil

`func (o *RawWeaponInfoV2Output) SetRecoilSpeedNil(b bool)`

 SetRecoilSpeedNil sets the value for RecoilSpeed to be an explicit nil

### UnsetRecoilSpeed
`func (o *RawWeaponInfoV2Output) UnsetRecoilSpeed()`

UnsetRecoilSpeed ensures that no value is present for RecoilSpeed, not even an explicit nil
### GetReloadMoveSpeed

`func (o *RawWeaponInfoV2Output) GetReloadMoveSpeed() float32`

GetReloadMoveSpeed returns the ReloadMoveSpeed field if non-nil, zero value otherwise.

### GetReloadMoveSpeedOk

`func (o *RawWeaponInfoV2Output) GetReloadMoveSpeedOk() (*float32, bool)`

GetReloadMoveSpeedOk returns a tuple with the ReloadMoveSpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReloadMoveSpeed

`func (o *RawWeaponInfoV2Output) SetReloadMoveSpeed(v float32)`

SetReloadMoveSpeed sets ReloadMoveSpeed field to given value.

### HasReloadMoveSpeed

`func (o *RawWeaponInfoV2Output) HasReloadMoveSpeed() bool`

HasReloadMoveSpeed returns a boolean if a field has been set.

### SetReloadMoveSpeedNil

`func (o *RawWeaponInfoV2Output) SetReloadMoveSpeedNil(b bool)`

 SetReloadMoveSpeedNil sets the value for ReloadMoveSpeed to be an explicit nil

### UnsetReloadMoveSpeed
`func (o *RawWeaponInfoV2Output) UnsetReloadMoveSpeed()`

UnsetReloadMoveSpeed ensures that no value is present for ReloadMoveSpeed, not even an explicit nil
### GetScatterYawScale

`func (o *RawWeaponInfoV2Output) GetScatterYawScale() float32`

GetScatterYawScale returns the ScatterYawScale field if non-nil, zero value otherwise.

### GetScatterYawScaleOk

`func (o *RawWeaponInfoV2Output) GetScatterYawScaleOk() (*float32, bool)`

GetScatterYawScaleOk returns a tuple with the ScatterYawScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScatterYawScale

`func (o *RawWeaponInfoV2Output) SetScatterYawScale(v float32)`

SetScatterYawScale sets ScatterYawScale field to given value.

### HasScatterYawScale

`func (o *RawWeaponInfoV2Output) HasScatterYawScale() bool`

HasScatterYawScale returns a boolean if a field has been set.

### SetScatterYawScaleNil

`func (o *RawWeaponInfoV2Output) SetScatterYawScaleNil(b bool)`

 SetScatterYawScaleNil sets the value for ScatterYawScale to be an explicit nil

### UnsetScatterYawScale
`func (o *RawWeaponInfoV2Output) UnsetScatterYawScale()`

UnsetScatterYawScale ensures that no value is present for ScatterYawScale, not even an explicit nil
### GetAimingShotSpreadPenalty

`func (o *RawWeaponInfoV2Output) GetAimingShotSpreadPenalty() AimingShotSpreadPenalty`

GetAimingShotSpreadPenalty returns the AimingShotSpreadPenalty field if non-nil, zero value otherwise.

### GetAimingShotSpreadPenaltyOk

`func (o *RawWeaponInfoV2Output) GetAimingShotSpreadPenaltyOk() (*AimingShotSpreadPenalty, bool)`

GetAimingShotSpreadPenaltyOk returns a tuple with the AimingShotSpreadPenalty field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAimingShotSpreadPenalty

`func (o *RawWeaponInfoV2Output) SetAimingShotSpreadPenalty(v AimingShotSpreadPenalty)`

SetAimingShotSpreadPenalty sets AimingShotSpreadPenalty field to given value.

### HasAimingShotSpreadPenalty

`func (o *RawWeaponInfoV2Output) HasAimingShotSpreadPenalty() bool`

HasAimingShotSpreadPenalty returns a boolean if a field has been set.

### SetAimingShotSpreadPenaltyNil

`func (o *RawWeaponInfoV2Output) SetAimingShotSpreadPenaltyNil(b bool)`

 SetAimingShotSpreadPenaltyNil sets the value for AimingShotSpreadPenalty to be an explicit nil

### UnsetAimingShotSpreadPenalty
`func (o *RawWeaponInfoV2Output) UnsetAimingShotSpreadPenalty()`

UnsetAimingShotSpreadPenalty ensures that no value is present for AimingShotSpreadPenalty, not even an explicit nil
### GetStandingShotSpreadPenalty

`func (o *RawWeaponInfoV2Output) GetStandingShotSpreadPenalty() StandingShotSpreadPenalty`

GetStandingShotSpreadPenalty returns the StandingShotSpreadPenalty field if non-nil, zero value otherwise.

### GetStandingShotSpreadPenaltyOk

`func (o *RawWeaponInfoV2Output) GetStandingShotSpreadPenaltyOk() (*StandingShotSpreadPenalty, bool)`

GetStandingShotSpreadPenaltyOk returns a tuple with the StandingShotSpreadPenalty field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStandingShotSpreadPenalty

`func (o *RawWeaponInfoV2Output) SetStandingShotSpreadPenalty(v StandingShotSpreadPenalty)`

SetStandingShotSpreadPenalty sets StandingShotSpreadPenalty field to given value.

### HasStandingShotSpreadPenalty

`func (o *RawWeaponInfoV2Output) HasStandingShotSpreadPenalty() bool`

HasStandingShotSpreadPenalty returns a boolean if a field has been set.

### SetStandingShotSpreadPenaltyNil

`func (o *RawWeaponInfoV2Output) SetStandingShotSpreadPenaltyNil(b bool)`

 SetStandingShotSpreadPenaltyNil sets the value for StandingShotSpreadPenalty to be an explicit nil

### UnsetStandingShotSpreadPenalty
`func (o *RawWeaponInfoV2Output) UnsetStandingShotSpreadPenalty()`

UnsetStandingShotSpreadPenalty ensures that no value is present for StandingShotSpreadPenalty, not even an explicit nil
### GetShootMoveSpeedPercent

`func (o *RawWeaponInfoV2Output) GetShootMoveSpeedPercent() float32`

GetShootMoveSpeedPercent returns the ShootMoveSpeedPercent field if non-nil, zero value otherwise.

### GetShootMoveSpeedPercentOk

`func (o *RawWeaponInfoV2Output) GetShootMoveSpeedPercentOk() (*float32, bool)`

GetShootMoveSpeedPercentOk returns a tuple with the ShootMoveSpeedPercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShootMoveSpeedPercent

`func (o *RawWeaponInfoV2Output) SetShootMoveSpeedPercent(v float32)`

SetShootMoveSpeedPercent sets ShootMoveSpeedPercent field to given value.

### HasShootMoveSpeedPercent

`func (o *RawWeaponInfoV2Output) HasShootMoveSpeedPercent() bool`

HasShootMoveSpeedPercent returns a boolean if a field has been set.

### SetShootMoveSpeedPercentNil

`func (o *RawWeaponInfoV2Output) SetShootMoveSpeedPercentNil(b bool)`

 SetShootMoveSpeedPercentNil sets the value for ShootMoveSpeedPercent to be an explicit nil

### UnsetShootMoveSpeedPercent
`func (o *RawWeaponInfoV2Output) UnsetShootMoveSpeedPercent()`

UnsetShootMoveSpeedPercent ensures that no value is present for ShootMoveSpeedPercent, not even an explicit nil
### GetShootSpreadPenaltyDecay

`func (o *RawWeaponInfoV2Output) GetShootSpreadPenaltyDecay() float32`

GetShootSpreadPenaltyDecay returns the ShootSpreadPenaltyDecay field if non-nil, zero value otherwise.

### GetShootSpreadPenaltyDecayOk

`func (o *RawWeaponInfoV2Output) GetShootSpreadPenaltyDecayOk() (*float32, bool)`

GetShootSpreadPenaltyDecayOk returns a tuple with the ShootSpreadPenaltyDecay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShootSpreadPenaltyDecay

`func (o *RawWeaponInfoV2Output) SetShootSpreadPenaltyDecay(v float32)`

SetShootSpreadPenaltyDecay sets ShootSpreadPenaltyDecay field to given value.

### HasShootSpreadPenaltyDecay

`func (o *RawWeaponInfoV2Output) HasShootSpreadPenaltyDecay() bool`

HasShootSpreadPenaltyDecay returns a boolean if a field has been set.

### SetShootSpreadPenaltyDecayNil

`func (o *RawWeaponInfoV2Output) SetShootSpreadPenaltyDecayNil(b bool)`

 SetShootSpreadPenaltyDecayNil sets the value for ShootSpreadPenaltyDecay to be an explicit nil

### UnsetShootSpreadPenaltyDecay
`func (o *RawWeaponInfoV2Output) UnsetShootSpreadPenaltyDecay()`

UnsetShootSpreadPenaltyDecay ensures that no value is present for ShootSpreadPenaltyDecay, not even an explicit nil
### GetShootSpreadPenaltyDecayDelay

`func (o *RawWeaponInfoV2Output) GetShootSpreadPenaltyDecayDelay() float32`

GetShootSpreadPenaltyDecayDelay returns the ShootSpreadPenaltyDecayDelay field if non-nil, zero value otherwise.

### GetShootSpreadPenaltyDecayDelayOk

`func (o *RawWeaponInfoV2Output) GetShootSpreadPenaltyDecayDelayOk() (*float32, bool)`

GetShootSpreadPenaltyDecayDelayOk returns a tuple with the ShootSpreadPenaltyDecayDelay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShootSpreadPenaltyDecayDelay

`func (o *RawWeaponInfoV2Output) SetShootSpreadPenaltyDecayDelay(v float32)`

SetShootSpreadPenaltyDecayDelay sets ShootSpreadPenaltyDecayDelay field to given value.

### HasShootSpreadPenaltyDecayDelay

`func (o *RawWeaponInfoV2Output) HasShootSpreadPenaltyDecayDelay() bool`

HasShootSpreadPenaltyDecayDelay returns a boolean if a field has been set.

### SetShootSpreadPenaltyDecayDelayNil

`func (o *RawWeaponInfoV2Output) SetShootSpreadPenaltyDecayDelayNil(b bool)`

 SetShootSpreadPenaltyDecayDelayNil sets the value for ShootSpreadPenaltyDecayDelay to be an explicit nil

### UnsetShootSpreadPenaltyDecayDelay
`func (o *RawWeaponInfoV2Output) UnsetShootSpreadPenaltyDecayDelay()`

UnsetShootSpreadPenaltyDecayDelay ensures that no value is present for ShootSpreadPenaltyDecayDelay, not even an explicit nil
### GetShootSpreadPenaltyPerShot

`func (o *RawWeaponInfoV2Output) GetShootSpreadPenaltyPerShot() float32`

GetShootSpreadPenaltyPerShot returns the ShootSpreadPenaltyPerShot field if non-nil, zero value otherwise.

### GetShootSpreadPenaltyPerShotOk

`func (o *RawWeaponInfoV2Output) GetShootSpreadPenaltyPerShotOk() (*float32, bool)`

GetShootSpreadPenaltyPerShotOk returns a tuple with the ShootSpreadPenaltyPerShot field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShootSpreadPenaltyPerShot

`func (o *RawWeaponInfoV2Output) SetShootSpreadPenaltyPerShot(v float32)`

SetShootSpreadPenaltyPerShot sets ShootSpreadPenaltyPerShot field to given value.

### HasShootSpreadPenaltyPerShot

`func (o *RawWeaponInfoV2Output) HasShootSpreadPenaltyPerShot() bool`

HasShootSpreadPenaltyPerShot returns a boolean if a field has been set.

### SetShootSpreadPenaltyPerShotNil

`func (o *RawWeaponInfoV2Output) SetShootSpreadPenaltyPerShotNil(b bool)`

 SetShootSpreadPenaltyPerShotNil sets the value for ShootSpreadPenaltyPerShot to be an explicit nil

### UnsetShootSpreadPenaltyPerShot
`func (o *RawWeaponInfoV2Output) UnsetShootSpreadPenaltyPerShot()`

UnsetShootSpreadPenaltyPerShot ensures that no value is present for ShootSpreadPenaltyPerShot, not even an explicit nil
### GetShootingUpSpreadPenalty

`func (o *RawWeaponInfoV2Output) GetShootingUpSpreadPenalty() float32`

GetShootingUpSpreadPenalty returns the ShootingUpSpreadPenalty field if non-nil, zero value otherwise.

### GetShootingUpSpreadPenaltyOk

`func (o *RawWeaponInfoV2Output) GetShootingUpSpreadPenaltyOk() (*float32, bool)`

GetShootingUpSpreadPenaltyOk returns a tuple with the ShootingUpSpreadPenalty field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShootingUpSpreadPenalty

`func (o *RawWeaponInfoV2Output) SetShootingUpSpreadPenalty(v float32)`

SetShootingUpSpreadPenalty sets ShootingUpSpreadPenalty field to given value.

### HasShootingUpSpreadPenalty

`func (o *RawWeaponInfoV2Output) HasShootingUpSpreadPenalty() bool`

HasShootingUpSpreadPenalty returns a boolean if a field has been set.

### SetShootingUpSpreadPenaltyNil

`func (o *RawWeaponInfoV2Output) SetShootingUpSpreadPenaltyNil(b bool)`

 SetShootingUpSpreadPenaltyNil sets the value for ShootingUpSpreadPenalty to be an explicit nil

### UnsetShootingUpSpreadPenalty
`func (o *RawWeaponInfoV2Output) UnsetShootingUpSpreadPenalty()`

UnsetShootingUpSpreadPenalty ensures that no value is present for ShootingUpSpreadPenalty, not even an explicit nil
### GetVerticalPunch

`func (o *RawWeaponInfoV2Output) GetVerticalPunch() float32`

GetVerticalPunch returns the VerticalPunch field if non-nil, zero value otherwise.

### GetVerticalPunchOk

`func (o *RawWeaponInfoV2Output) GetVerticalPunchOk() (*float32, bool)`

GetVerticalPunchOk returns a tuple with the VerticalPunch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerticalPunch

`func (o *RawWeaponInfoV2Output) SetVerticalPunch(v float32)`

SetVerticalPunch sets VerticalPunch field to given value.

### HasVerticalPunch

`func (o *RawWeaponInfoV2Output) HasVerticalPunch() bool`

HasVerticalPunch returns a boolean if a field has been set.

### SetVerticalPunchNil

`func (o *RawWeaponInfoV2Output) SetVerticalPunchNil(b bool)`

 SetVerticalPunchNil sets the value for VerticalPunch to be an explicit nil

### UnsetVerticalPunch
`func (o *RawWeaponInfoV2Output) UnsetVerticalPunch()`

UnsetVerticalPunch ensures that no value is present for VerticalPunch, not even an explicit nil
### GetZoomFov

`func (o *RawWeaponInfoV2Output) GetZoomFov() float32`

GetZoomFov returns the ZoomFov field if non-nil, zero value otherwise.

### GetZoomFovOk

`func (o *RawWeaponInfoV2Output) GetZoomFovOk() (*float32, bool)`

GetZoomFovOk returns a tuple with the ZoomFov field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetZoomFov

`func (o *RawWeaponInfoV2Output) SetZoomFov(v float32)`

SetZoomFov sets ZoomFov field to given value.

### HasZoomFov

`func (o *RawWeaponInfoV2Output) HasZoomFov() bool`

HasZoomFov returns a boolean if a field has been set.

### SetZoomFovNil

`func (o *RawWeaponInfoV2Output) SetZoomFovNil(b bool)`

 SetZoomFovNil sets the value for ZoomFov to be an explicit nil

### UnsetZoomFov
`func (o *RawWeaponInfoV2Output) UnsetZoomFov()`

UnsetZoomFov ensures that no value is present for ZoomFov, not even an explicit nil
### GetZoomMoveSpeedPercent

`func (o *RawWeaponInfoV2Output) GetZoomMoveSpeedPercent() float32`

GetZoomMoveSpeedPercent returns the ZoomMoveSpeedPercent field if non-nil, zero value otherwise.

### GetZoomMoveSpeedPercentOk

`func (o *RawWeaponInfoV2Output) GetZoomMoveSpeedPercentOk() (*float32, bool)`

GetZoomMoveSpeedPercentOk returns a tuple with the ZoomMoveSpeedPercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetZoomMoveSpeedPercent

`func (o *RawWeaponInfoV2Output) SetZoomMoveSpeedPercent(v float32)`

SetZoomMoveSpeedPercent sets ZoomMoveSpeedPercent field to given value.

### HasZoomMoveSpeedPercent

`func (o *RawWeaponInfoV2Output) HasZoomMoveSpeedPercent() bool`

HasZoomMoveSpeedPercent returns a boolean if a field has been set.

### SetZoomMoveSpeedPercentNil

`func (o *RawWeaponInfoV2Output) SetZoomMoveSpeedPercentNil(b bool)`

 SetZoomMoveSpeedPercentNil sets the value for ZoomMoveSpeedPercent to be an explicit nil

### UnsetZoomMoveSpeedPercent
`func (o *RawWeaponInfoV2Output) UnsetZoomMoveSpeedPercent()`

UnsetZoomMoveSpeedPercent ensures that no value is present for ZoomMoveSpeedPercent, not even an explicit nil
### GetBullets

`func (o *RawWeaponInfoV2Output) GetBullets() int32`

GetBullets returns the Bullets field if non-nil, zero value otherwise.

### GetBulletsOk

`func (o *RawWeaponInfoV2Output) GetBulletsOk() (*int32, bool)`

GetBulletsOk returns a tuple with the Bullets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBullets

`func (o *RawWeaponInfoV2Output) SetBullets(v int32)`

SetBullets sets Bullets field to given value.

### HasBullets

`func (o *RawWeaponInfoV2Output) HasBullets() bool`

HasBullets returns a boolean if a field has been set.

### SetBulletsNil

`func (o *RawWeaponInfoV2Output) SetBulletsNil(b bool)`

 SetBulletsNil sets the value for Bullets to be an explicit nil

### UnsetBullets
`func (o *RawWeaponInfoV2Output) UnsetBullets()`

UnsetBullets ensures that no value is present for Bullets, not even an explicit nil
### GetBurstShotCount

`func (o *RawWeaponInfoV2Output) GetBurstShotCount() int32`

GetBurstShotCount returns the BurstShotCount field if non-nil, zero value otherwise.

### GetBurstShotCountOk

`func (o *RawWeaponInfoV2Output) GetBurstShotCountOk() (*int32, bool)`

GetBurstShotCountOk returns a tuple with the BurstShotCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBurstShotCount

`func (o *RawWeaponInfoV2Output) SetBurstShotCount(v int32)`

SetBurstShotCount sets BurstShotCount field to given value.

### HasBurstShotCount

`func (o *RawWeaponInfoV2Output) HasBurstShotCount() bool`

HasBurstShotCount returns a boolean if a field has been set.

### SetBurstShotCountNil

`func (o *RawWeaponInfoV2Output) SetBurstShotCountNil(b bool)`

 SetBurstShotCountNil sets the value for BurstShotCount to be an explicit nil

### UnsetBurstShotCount
`func (o *RawWeaponInfoV2Output) UnsetBurstShotCount()`

UnsetBurstShotCount ensures that no value is present for BurstShotCount, not even an explicit nil
### GetClipSize

`func (o *RawWeaponInfoV2Output) GetClipSize() int32`

GetClipSize returns the ClipSize field if non-nil, zero value otherwise.

### GetClipSizeOk

`func (o *RawWeaponInfoV2Output) GetClipSizeOk() (*int32, bool)`

GetClipSizeOk returns a tuple with the ClipSize field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClipSize

`func (o *RawWeaponInfoV2Output) SetClipSize(v int32)`

SetClipSize sets ClipSize field to given value.

### HasClipSize

`func (o *RawWeaponInfoV2Output) HasClipSize() bool`

HasClipSize returns a boolean if a field has been set.

### SetClipSizeNil

`func (o *RawWeaponInfoV2Output) SetClipSizeNil(b bool)`

 SetClipSizeNil sets the value for ClipSize to be an explicit nil

### UnsetClipSize
`func (o *RawWeaponInfoV2Output) UnsetClipSize()`

UnsetClipSize ensures that no value is present for ClipSize, not even an explicit nil
### GetSpread

`func (o *RawWeaponInfoV2Output) GetSpread() float32`

GetSpread returns the Spread field if non-nil, zero value otherwise.

### GetSpreadOk

`func (o *RawWeaponInfoV2Output) GetSpreadOk() (*float32, bool)`

GetSpreadOk returns a tuple with the Spread field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpread

`func (o *RawWeaponInfoV2Output) SetSpread(v float32)`

SetSpread sets Spread field to given value.

### HasSpread

`func (o *RawWeaponInfoV2Output) HasSpread() bool`

HasSpread returns a boolean if a field has been set.

### SetSpreadNil

`func (o *RawWeaponInfoV2Output) SetSpreadNil(b bool)`

 SetSpreadNil sets the value for Spread to be an explicit nil

### UnsetSpread
`func (o *RawWeaponInfoV2Output) UnsetSpread()`

UnsetSpread ensures that no value is present for Spread, not even an explicit nil
### GetStandingSpread

`func (o *RawWeaponInfoV2Output) GetStandingSpread() float32`

GetStandingSpread returns the StandingSpread field if non-nil, zero value otherwise.

### GetStandingSpreadOk

`func (o *RawWeaponInfoV2Output) GetStandingSpreadOk() (*float32, bool)`

GetStandingSpreadOk returns a tuple with the StandingSpread field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStandingSpread

`func (o *RawWeaponInfoV2Output) SetStandingSpread(v float32)`

SetStandingSpread sets StandingSpread field to given value.

### HasStandingSpread

`func (o *RawWeaponInfoV2Output) HasStandingSpread() bool`

HasStandingSpread returns a boolean if a field has been set.

### SetStandingSpreadNil

`func (o *RawWeaponInfoV2Output) SetStandingSpreadNil(b bool)`

 SetStandingSpreadNil sets the value for StandingSpread to be an explicit nil

### UnsetStandingSpread
`func (o *RawWeaponInfoV2Output) UnsetStandingSpread()`

UnsetStandingSpread ensures that no value is present for StandingSpread, not even an explicit nil
### GetLowAmmoIndicatorThreshold

`func (o *RawWeaponInfoV2Output) GetLowAmmoIndicatorThreshold() float32`

GetLowAmmoIndicatorThreshold returns the LowAmmoIndicatorThreshold field if non-nil, zero value otherwise.

### GetLowAmmoIndicatorThresholdOk

`func (o *RawWeaponInfoV2Output) GetLowAmmoIndicatorThresholdOk() (*float32, bool)`

GetLowAmmoIndicatorThresholdOk returns a tuple with the LowAmmoIndicatorThreshold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLowAmmoIndicatorThreshold

`func (o *RawWeaponInfoV2Output) SetLowAmmoIndicatorThreshold(v float32)`

SetLowAmmoIndicatorThreshold sets LowAmmoIndicatorThreshold field to given value.

### HasLowAmmoIndicatorThreshold

`func (o *RawWeaponInfoV2Output) HasLowAmmoIndicatorThreshold() bool`

HasLowAmmoIndicatorThreshold returns a boolean if a field has been set.

### SetLowAmmoIndicatorThresholdNil

`func (o *RawWeaponInfoV2Output) SetLowAmmoIndicatorThresholdNil(b bool)`

 SetLowAmmoIndicatorThresholdNil sets the value for LowAmmoIndicatorThreshold to be an explicit nil

### UnsetLowAmmoIndicatorThreshold
`func (o *RawWeaponInfoV2Output) UnsetLowAmmoIndicatorThreshold()`

UnsetLowAmmoIndicatorThreshold ensures that no value is present for LowAmmoIndicatorThreshold, not even an explicit nil
### GetRecoilSeed

`func (o *RawWeaponInfoV2Output) GetRecoilSeed() float32`

GetRecoilSeed returns the RecoilSeed field if non-nil, zero value otherwise.

### GetRecoilSeedOk

`func (o *RawWeaponInfoV2Output) GetRecoilSeedOk() (*float32, bool)`

GetRecoilSeedOk returns a tuple with the RecoilSeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecoilSeed

`func (o *RawWeaponInfoV2Output) SetRecoilSeed(v float32)`

SetRecoilSeed sets RecoilSeed field to given value.

### HasRecoilSeed

`func (o *RawWeaponInfoV2Output) HasRecoilSeed() bool`

HasRecoilSeed returns a boolean if a field has been set.

### SetRecoilSeedNil

`func (o *RawWeaponInfoV2Output) SetRecoilSeedNil(b bool)`

 SetRecoilSeedNil sets the value for RecoilSeed to be an explicit nil

### UnsetRecoilSeed
`func (o *RawWeaponInfoV2Output) UnsetRecoilSeed()`

UnsetRecoilSeed ensures that no value is present for RecoilSeed, not even an explicit nil
### GetReloadDuration

`func (o *RawWeaponInfoV2Output) GetReloadDuration() float32`

GetReloadDuration returns the ReloadDuration field if non-nil, zero value otherwise.

### GetReloadDurationOk

`func (o *RawWeaponInfoV2Output) GetReloadDurationOk() (*float32, bool)`

GetReloadDurationOk returns a tuple with the ReloadDuration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReloadDuration

`func (o *RawWeaponInfoV2Output) SetReloadDuration(v float32)`

SetReloadDuration sets ReloadDuration field to given value.

### HasReloadDuration

`func (o *RawWeaponInfoV2Output) HasReloadDuration() bool`

HasReloadDuration returns a boolean if a field has been set.

### SetReloadDurationNil

`func (o *RawWeaponInfoV2Output) SetReloadDurationNil(b bool)`

 SetReloadDurationNil sets the value for ReloadDuration to be an explicit nil

### UnsetReloadDuration
`func (o *RawWeaponInfoV2Output) UnsetReloadDuration()`

UnsetReloadDuration ensures that no value is present for ReloadDuration, not even an explicit nil
### GetBulletSpeedCurve

`func (o *RawWeaponInfoV2Output) GetBulletSpeedCurve() RawItemWeaponInfoBulletSpeedCurveV2Output`

GetBulletSpeedCurve returns the BulletSpeedCurve field if non-nil, zero value otherwise.

### GetBulletSpeedCurveOk

`func (o *RawWeaponInfoV2Output) GetBulletSpeedCurveOk() (*RawItemWeaponInfoBulletSpeedCurveV2Output, bool)`

GetBulletSpeedCurveOk returns a tuple with the BulletSpeedCurve field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletSpeedCurve

`func (o *RawWeaponInfoV2Output) SetBulletSpeedCurve(v RawItemWeaponInfoBulletSpeedCurveV2Output)`

SetBulletSpeedCurve sets BulletSpeedCurve field to given value.

### HasBulletSpeedCurve

`func (o *RawWeaponInfoV2Output) HasBulletSpeedCurve() bool`

HasBulletSpeedCurve returns a boolean if a field has been set.

### SetBulletSpeedCurveNil

`func (o *RawWeaponInfoV2Output) SetBulletSpeedCurveNil(b bool)`

 SetBulletSpeedCurveNil sets the value for BulletSpeedCurve to be an explicit nil

### UnsetBulletSpeedCurve
`func (o *RawWeaponInfoV2Output) UnsetBulletSpeedCurve()`

UnsetBulletSpeedCurve ensures that no value is present for BulletSpeedCurve, not even an explicit nil
### GetHorizontalRecoil

`func (o *RawWeaponInfoV2Output) GetHorizontalRecoil() RawWeaponInfoHorizontalRecoilV2Output`

GetHorizontalRecoil returns the HorizontalRecoil field if non-nil, zero value otherwise.

### GetHorizontalRecoilOk

`func (o *RawWeaponInfoV2Output) GetHorizontalRecoilOk() (*RawWeaponInfoHorizontalRecoilV2Output, bool)`

GetHorizontalRecoilOk returns a tuple with the HorizontalRecoil field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHorizontalRecoil

`func (o *RawWeaponInfoV2Output) SetHorizontalRecoil(v RawWeaponInfoHorizontalRecoilV2Output)`

SetHorizontalRecoil sets HorizontalRecoil field to given value.

### HasHorizontalRecoil

`func (o *RawWeaponInfoV2Output) HasHorizontalRecoil() bool`

HasHorizontalRecoil returns a boolean if a field has been set.

### SetHorizontalRecoilNil

`func (o *RawWeaponInfoV2Output) SetHorizontalRecoilNil(b bool)`

 SetHorizontalRecoilNil sets the value for HorizontalRecoil to be an explicit nil

### UnsetHorizontalRecoil
`func (o *RawWeaponInfoV2Output) UnsetHorizontalRecoil()`

UnsetHorizontalRecoil ensures that no value is present for HorizontalRecoil, not even an explicit nil
### GetVerticalRecoil

`func (o *RawWeaponInfoV2Output) GetVerticalRecoil() RawWeaponInfoVerticalRecoilV2Output`

GetVerticalRecoil returns the VerticalRecoil field if non-nil, zero value otherwise.

### GetVerticalRecoilOk

`func (o *RawWeaponInfoV2Output) GetVerticalRecoilOk() (*RawWeaponInfoVerticalRecoilV2Output, bool)`

GetVerticalRecoilOk returns a tuple with the VerticalRecoil field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerticalRecoil

`func (o *RawWeaponInfoV2Output) SetVerticalRecoil(v RawWeaponInfoVerticalRecoilV2Output)`

SetVerticalRecoil sets VerticalRecoil field to given value.

### HasVerticalRecoil

`func (o *RawWeaponInfoV2Output) HasVerticalRecoil() bool`

HasVerticalRecoil returns a boolean if a field has been set.

### SetVerticalRecoilNil

`func (o *RawWeaponInfoV2Output) SetVerticalRecoilNil(b bool)`

 SetVerticalRecoilNil sets the value for VerticalRecoil to be an explicit nil

### UnsetVerticalRecoil
`func (o *RawWeaponInfoV2Output) UnsetVerticalRecoil()`

UnsetVerticalRecoil ensures that no value is present for VerticalRecoil, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


