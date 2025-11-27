# WeaponInfoV2

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
**ReloadSingleBulletsInitialDelay** | Pointer to **NullableFloat32** |  | [optional] 
**ReloadSingleBullets** | Pointer to **NullableBool** |  | [optional] 
**ReloadSingleBulletsAllowCancel** | Pointer to **NullableBool** |  | [optional] 
**BurstShotCount** | Pointer to **NullableInt32** |  | [optional] 
**ClipSize** | Pointer to **NullableInt32** |  | [optional] 
**Spread** | Pointer to **NullableFloat32** |  | [optional] 
**StandingSpread** | Pointer to **NullableFloat32** |  | [optional] 
**LowAmmoIndicatorThreshold** | Pointer to **NullableFloat32** |  | [optional] 
**RecoilSeed** | Pointer to **NullableFloat32** |  | [optional] 
**ReloadDuration** | Pointer to **NullableFloat32** |  | [optional] 
**BulletSpeedCurve** | Pointer to [**NullableRawItemWeaponInfoBulletSpeedCurveV2**](RawItemWeaponInfoBulletSpeedCurveV2.md) |  | [optional] 
**HorizontalRecoil** | Pointer to [**NullableRawWeaponInfoHorizontalRecoilV2**](RawWeaponInfoHorizontalRecoilV2.md) |  | [optional] 
**VerticalRecoil** | Pointer to [**NullableRawWeaponInfoVerticalRecoilV2**](RawWeaponInfoVerticalRecoilV2.md) |  | [optional] 
**ShotsPerSecond** | **NullableFloat32** |  | [readonly] 
**BulletsPerSecond** | **NullableFloat32** |  | [readonly] 
**DamagePerSecond** | **NullableFloat32** |  | [readonly] 
**DamagePerShot** | **NullableFloat32** |  | [readonly] 
**DamagePerMagazine** | **NullableFloat32** |  | [readonly] 

## Methods

### NewWeaponInfoV2

`func NewWeaponInfoV2(shotsPerSecond NullableFloat32, bulletsPerSecond NullableFloat32, damagePerSecond NullableFloat32, damagePerShot NullableFloat32, damagePerMagazine NullableFloat32, ) *WeaponInfoV2`

NewWeaponInfoV2 instantiates a new WeaponInfoV2 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWeaponInfoV2WithDefaults

`func NewWeaponInfoV2WithDefaults() *WeaponInfoV2`

NewWeaponInfoV2WithDefaults instantiates a new WeaponInfoV2 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCanZoom

`func (o *WeaponInfoV2) GetCanZoom() bool`

GetCanZoom returns the CanZoom field if non-nil, zero value otherwise.

### GetCanZoomOk

`func (o *WeaponInfoV2) GetCanZoomOk() (*bool, bool)`

GetCanZoomOk returns a tuple with the CanZoom field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCanZoom

`func (o *WeaponInfoV2) SetCanZoom(v bool)`

SetCanZoom sets CanZoom field to given value.

### HasCanZoom

`func (o *WeaponInfoV2) HasCanZoom() bool`

HasCanZoom returns a boolean if a field has been set.

### SetCanZoomNil

`func (o *WeaponInfoV2) SetCanZoomNil(b bool)`

 SetCanZoomNil sets the value for CanZoom to be an explicit nil

### UnsetCanZoom
`func (o *WeaponInfoV2) UnsetCanZoom()`

UnsetCanZoom ensures that no value is present for CanZoom, not even an explicit nil
### GetBulletDamage

`func (o *WeaponInfoV2) GetBulletDamage() float32`

GetBulletDamage returns the BulletDamage field if non-nil, zero value otherwise.

### GetBulletDamageOk

`func (o *WeaponInfoV2) GetBulletDamageOk() (*float32, bool)`

GetBulletDamageOk returns a tuple with the BulletDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletDamage

`func (o *WeaponInfoV2) SetBulletDamage(v float32)`

SetBulletDamage sets BulletDamage field to given value.

### HasBulletDamage

`func (o *WeaponInfoV2) HasBulletDamage() bool`

HasBulletDamage returns a boolean if a field has been set.

### SetBulletDamageNil

`func (o *WeaponInfoV2) SetBulletDamageNil(b bool)`

 SetBulletDamageNil sets the value for BulletDamage to be an explicit nil

### UnsetBulletDamage
`func (o *WeaponInfoV2) UnsetBulletDamage()`

UnsetBulletDamage ensures that no value is present for BulletDamage, not even an explicit nil
### GetBulletGravityScale

`func (o *WeaponInfoV2) GetBulletGravityScale() float32`

GetBulletGravityScale returns the BulletGravityScale field if non-nil, zero value otherwise.

### GetBulletGravityScaleOk

`func (o *WeaponInfoV2) GetBulletGravityScaleOk() (*float32, bool)`

GetBulletGravityScaleOk returns a tuple with the BulletGravityScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletGravityScale

`func (o *WeaponInfoV2) SetBulletGravityScale(v float32)`

SetBulletGravityScale sets BulletGravityScale field to given value.

### HasBulletGravityScale

`func (o *WeaponInfoV2) HasBulletGravityScale() bool`

HasBulletGravityScale returns a boolean if a field has been set.

### SetBulletGravityScaleNil

`func (o *WeaponInfoV2) SetBulletGravityScaleNil(b bool)`

 SetBulletGravityScaleNil sets the value for BulletGravityScale to be an explicit nil

### UnsetBulletGravityScale
`func (o *WeaponInfoV2) UnsetBulletGravityScale()`

UnsetBulletGravityScale ensures that no value is present for BulletGravityScale, not even an explicit nil
### GetBulletInheritShooterVelocityScale

`func (o *WeaponInfoV2) GetBulletInheritShooterVelocityScale() float32`

GetBulletInheritShooterVelocityScale returns the BulletInheritShooterVelocityScale field if non-nil, zero value otherwise.

### GetBulletInheritShooterVelocityScaleOk

`func (o *WeaponInfoV2) GetBulletInheritShooterVelocityScaleOk() (*float32, bool)`

GetBulletInheritShooterVelocityScaleOk returns a tuple with the BulletInheritShooterVelocityScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletInheritShooterVelocityScale

`func (o *WeaponInfoV2) SetBulletInheritShooterVelocityScale(v float32)`

SetBulletInheritShooterVelocityScale sets BulletInheritShooterVelocityScale field to given value.

### HasBulletInheritShooterVelocityScale

`func (o *WeaponInfoV2) HasBulletInheritShooterVelocityScale() bool`

HasBulletInheritShooterVelocityScale returns a boolean if a field has been set.

### SetBulletInheritShooterVelocityScaleNil

`func (o *WeaponInfoV2) SetBulletInheritShooterVelocityScaleNil(b bool)`

 SetBulletInheritShooterVelocityScaleNil sets the value for BulletInheritShooterVelocityScale to be an explicit nil

### UnsetBulletInheritShooterVelocityScale
`func (o *WeaponInfoV2) UnsetBulletInheritShooterVelocityScale()`

UnsetBulletInheritShooterVelocityScale ensures that no value is present for BulletInheritShooterVelocityScale, not even an explicit nil
### GetBulletLifetime

`func (o *WeaponInfoV2) GetBulletLifetime() float32`

GetBulletLifetime returns the BulletLifetime field if non-nil, zero value otherwise.

### GetBulletLifetimeOk

`func (o *WeaponInfoV2) GetBulletLifetimeOk() (*float32, bool)`

GetBulletLifetimeOk returns a tuple with the BulletLifetime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletLifetime

`func (o *WeaponInfoV2) SetBulletLifetime(v float32)`

SetBulletLifetime sets BulletLifetime field to given value.

### HasBulletLifetime

`func (o *WeaponInfoV2) HasBulletLifetime() bool`

HasBulletLifetime returns a boolean if a field has been set.

### SetBulletLifetimeNil

`func (o *WeaponInfoV2) SetBulletLifetimeNil(b bool)`

 SetBulletLifetimeNil sets the value for BulletLifetime to be an explicit nil

### UnsetBulletLifetime
`func (o *WeaponInfoV2) UnsetBulletLifetime()`

UnsetBulletLifetime ensures that no value is present for BulletLifetime, not even an explicit nil
### GetBulletRadius

`func (o *WeaponInfoV2) GetBulletRadius() float32`

GetBulletRadius returns the BulletRadius field if non-nil, zero value otherwise.

### GetBulletRadiusOk

`func (o *WeaponInfoV2) GetBulletRadiusOk() (*float32, bool)`

GetBulletRadiusOk returns a tuple with the BulletRadius field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletRadius

`func (o *WeaponInfoV2) SetBulletRadius(v float32)`

SetBulletRadius sets BulletRadius field to given value.

### HasBulletRadius

`func (o *WeaponInfoV2) HasBulletRadius() bool`

HasBulletRadius returns a boolean if a field has been set.

### SetBulletRadiusNil

`func (o *WeaponInfoV2) SetBulletRadiusNil(b bool)`

 SetBulletRadiusNil sets the value for BulletRadius to be an explicit nil

### UnsetBulletRadius
`func (o *WeaponInfoV2) UnsetBulletRadius()`

UnsetBulletRadius ensures that no value is present for BulletRadius, not even an explicit nil
### GetBulletRadiusVsWorld

`func (o *WeaponInfoV2) GetBulletRadiusVsWorld() float32`

GetBulletRadiusVsWorld returns the BulletRadiusVsWorld field if non-nil, zero value otherwise.

### GetBulletRadiusVsWorldOk

`func (o *WeaponInfoV2) GetBulletRadiusVsWorldOk() (*float32, bool)`

GetBulletRadiusVsWorldOk returns a tuple with the BulletRadiusVsWorld field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletRadiusVsWorld

`func (o *WeaponInfoV2) SetBulletRadiusVsWorld(v float32)`

SetBulletRadiusVsWorld sets BulletRadiusVsWorld field to given value.

### HasBulletRadiusVsWorld

`func (o *WeaponInfoV2) HasBulletRadiusVsWorld() bool`

HasBulletRadiusVsWorld returns a boolean if a field has been set.

### SetBulletRadiusVsWorldNil

`func (o *WeaponInfoV2) SetBulletRadiusVsWorldNil(b bool)`

 SetBulletRadiusVsWorldNil sets the value for BulletRadiusVsWorld to be an explicit nil

### UnsetBulletRadiusVsWorld
`func (o *WeaponInfoV2) UnsetBulletRadiusVsWorld()`

UnsetBulletRadiusVsWorld ensures that no value is present for BulletRadiusVsWorld, not even an explicit nil
### GetBulletReflectAmount

`func (o *WeaponInfoV2) GetBulletReflectAmount() float32`

GetBulletReflectAmount returns the BulletReflectAmount field if non-nil, zero value otherwise.

### GetBulletReflectAmountOk

`func (o *WeaponInfoV2) GetBulletReflectAmountOk() (*float32, bool)`

GetBulletReflectAmountOk returns a tuple with the BulletReflectAmount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletReflectAmount

`func (o *WeaponInfoV2) SetBulletReflectAmount(v float32)`

SetBulletReflectAmount sets BulletReflectAmount field to given value.

### HasBulletReflectAmount

`func (o *WeaponInfoV2) HasBulletReflectAmount() bool`

HasBulletReflectAmount returns a boolean if a field has been set.

### SetBulletReflectAmountNil

`func (o *WeaponInfoV2) SetBulletReflectAmountNil(b bool)`

 SetBulletReflectAmountNil sets the value for BulletReflectAmount to be an explicit nil

### UnsetBulletReflectAmount
`func (o *WeaponInfoV2) UnsetBulletReflectAmount()`

UnsetBulletReflectAmount ensures that no value is present for BulletReflectAmount, not even an explicit nil
### GetBulletReflectScale

`func (o *WeaponInfoV2) GetBulletReflectScale() float32`

GetBulletReflectScale returns the BulletReflectScale field if non-nil, zero value otherwise.

### GetBulletReflectScaleOk

`func (o *WeaponInfoV2) GetBulletReflectScaleOk() (*float32, bool)`

GetBulletReflectScaleOk returns a tuple with the BulletReflectScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletReflectScale

`func (o *WeaponInfoV2) SetBulletReflectScale(v float32)`

SetBulletReflectScale sets BulletReflectScale field to given value.

### HasBulletReflectScale

`func (o *WeaponInfoV2) HasBulletReflectScale() bool`

HasBulletReflectScale returns a boolean if a field has been set.

### SetBulletReflectScaleNil

`func (o *WeaponInfoV2) SetBulletReflectScaleNil(b bool)`

 SetBulletReflectScaleNil sets the value for BulletReflectScale to be an explicit nil

### UnsetBulletReflectScale
`func (o *WeaponInfoV2) UnsetBulletReflectScale()`

UnsetBulletReflectScale ensures that no value is present for BulletReflectScale, not even an explicit nil
### GetBulletWhizDistance

`func (o *WeaponInfoV2) GetBulletWhizDistance() float32`

GetBulletWhizDistance returns the BulletWhizDistance field if non-nil, zero value otherwise.

### GetBulletWhizDistanceOk

`func (o *WeaponInfoV2) GetBulletWhizDistanceOk() (*float32, bool)`

GetBulletWhizDistanceOk returns a tuple with the BulletWhizDistance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletWhizDistance

`func (o *WeaponInfoV2) SetBulletWhizDistance(v float32)`

SetBulletWhizDistance sets BulletWhizDistance field to given value.

### HasBulletWhizDistance

`func (o *WeaponInfoV2) HasBulletWhizDistance() bool`

HasBulletWhizDistance returns a boolean if a field has been set.

### SetBulletWhizDistanceNil

`func (o *WeaponInfoV2) SetBulletWhizDistanceNil(b bool)`

 SetBulletWhizDistanceNil sets the value for BulletWhizDistance to be an explicit nil

### UnsetBulletWhizDistance
`func (o *WeaponInfoV2) UnsetBulletWhizDistance()`

UnsetBulletWhizDistance ensures that no value is present for BulletWhizDistance, not even an explicit nil
### GetBurstShotCooldown

`func (o *WeaponInfoV2) GetBurstShotCooldown() float32`

GetBurstShotCooldown returns the BurstShotCooldown field if non-nil, zero value otherwise.

### GetBurstShotCooldownOk

`func (o *WeaponInfoV2) GetBurstShotCooldownOk() (*float32, bool)`

GetBurstShotCooldownOk returns a tuple with the BurstShotCooldown field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBurstShotCooldown

`func (o *WeaponInfoV2) SetBurstShotCooldown(v float32)`

SetBurstShotCooldown sets BurstShotCooldown field to given value.

### HasBurstShotCooldown

`func (o *WeaponInfoV2) HasBurstShotCooldown() bool`

HasBurstShotCooldown returns a boolean if a field has been set.

### SetBurstShotCooldownNil

`func (o *WeaponInfoV2) SetBurstShotCooldownNil(b bool)`

 SetBurstShotCooldownNil sets the value for BurstShotCooldown to be an explicit nil

### UnsetBurstShotCooldown
`func (o *WeaponInfoV2) UnsetBurstShotCooldown()`

UnsetBurstShotCooldown ensures that no value is present for BurstShotCooldown, not even an explicit nil
### GetCritBonusAgainstNpcs

`func (o *WeaponInfoV2) GetCritBonusAgainstNpcs() float32`

GetCritBonusAgainstNpcs returns the CritBonusAgainstNpcs field if non-nil, zero value otherwise.

### GetCritBonusAgainstNpcsOk

`func (o *WeaponInfoV2) GetCritBonusAgainstNpcsOk() (*float32, bool)`

GetCritBonusAgainstNpcsOk returns a tuple with the CritBonusAgainstNpcs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCritBonusAgainstNpcs

`func (o *WeaponInfoV2) SetCritBonusAgainstNpcs(v float32)`

SetCritBonusAgainstNpcs sets CritBonusAgainstNpcs field to given value.

### HasCritBonusAgainstNpcs

`func (o *WeaponInfoV2) HasCritBonusAgainstNpcs() bool`

HasCritBonusAgainstNpcs returns a boolean if a field has been set.

### SetCritBonusAgainstNpcsNil

`func (o *WeaponInfoV2) SetCritBonusAgainstNpcsNil(b bool)`

 SetCritBonusAgainstNpcsNil sets the value for CritBonusAgainstNpcs to be an explicit nil

### UnsetCritBonusAgainstNpcs
`func (o *WeaponInfoV2) UnsetCritBonusAgainstNpcs()`

UnsetCritBonusAgainstNpcs ensures that no value is present for CritBonusAgainstNpcs, not even an explicit nil
### GetCritBonusEnd

`func (o *WeaponInfoV2) GetCritBonusEnd() float32`

GetCritBonusEnd returns the CritBonusEnd field if non-nil, zero value otherwise.

### GetCritBonusEndOk

`func (o *WeaponInfoV2) GetCritBonusEndOk() (*float32, bool)`

GetCritBonusEndOk returns a tuple with the CritBonusEnd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCritBonusEnd

`func (o *WeaponInfoV2) SetCritBonusEnd(v float32)`

SetCritBonusEnd sets CritBonusEnd field to given value.

### HasCritBonusEnd

`func (o *WeaponInfoV2) HasCritBonusEnd() bool`

HasCritBonusEnd returns a boolean if a field has been set.

### SetCritBonusEndNil

`func (o *WeaponInfoV2) SetCritBonusEndNil(b bool)`

 SetCritBonusEndNil sets the value for CritBonusEnd to be an explicit nil

### UnsetCritBonusEnd
`func (o *WeaponInfoV2) UnsetCritBonusEnd()`

UnsetCritBonusEnd ensures that no value is present for CritBonusEnd, not even an explicit nil
### GetCritBonusEndRange

`func (o *WeaponInfoV2) GetCritBonusEndRange() float32`

GetCritBonusEndRange returns the CritBonusEndRange field if non-nil, zero value otherwise.

### GetCritBonusEndRangeOk

`func (o *WeaponInfoV2) GetCritBonusEndRangeOk() (*float32, bool)`

GetCritBonusEndRangeOk returns a tuple with the CritBonusEndRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCritBonusEndRange

`func (o *WeaponInfoV2) SetCritBonusEndRange(v float32)`

SetCritBonusEndRange sets CritBonusEndRange field to given value.

### HasCritBonusEndRange

`func (o *WeaponInfoV2) HasCritBonusEndRange() bool`

HasCritBonusEndRange returns a boolean if a field has been set.

### SetCritBonusEndRangeNil

`func (o *WeaponInfoV2) SetCritBonusEndRangeNil(b bool)`

 SetCritBonusEndRangeNil sets the value for CritBonusEndRange to be an explicit nil

### UnsetCritBonusEndRange
`func (o *WeaponInfoV2) UnsetCritBonusEndRange()`

UnsetCritBonusEndRange ensures that no value is present for CritBonusEndRange, not even an explicit nil
### GetCritBonusStart

`func (o *WeaponInfoV2) GetCritBonusStart() float32`

GetCritBonusStart returns the CritBonusStart field if non-nil, zero value otherwise.

### GetCritBonusStartOk

`func (o *WeaponInfoV2) GetCritBonusStartOk() (*float32, bool)`

GetCritBonusStartOk returns a tuple with the CritBonusStart field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCritBonusStart

`func (o *WeaponInfoV2) SetCritBonusStart(v float32)`

SetCritBonusStart sets CritBonusStart field to given value.

### HasCritBonusStart

`func (o *WeaponInfoV2) HasCritBonusStart() bool`

HasCritBonusStart returns a boolean if a field has been set.

### SetCritBonusStartNil

`func (o *WeaponInfoV2) SetCritBonusStartNil(b bool)`

 SetCritBonusStartNil sets the value for CritBonusStart to be an explicit nil

### UnsetCritBonusStart
`func (o *WeaponInfoV2) UnsetCritBonusStart()`

UnsetCritBonusStart ensures that no value is present for CritBonusStart, not even an explicit nil
### GetCritBonusStartRange

`func (o *WeaponInfoV2) GetCritBonusStartRange() float32`

GetCritBonusStartRange returns the CritBonusStartRange field if non-nil, zero value otherwise.

### GetCritBonusStartRangeOk

`func (o *WeaponInfoV2) GetCritBonusStartRangeOk() (*float32, bool)`

GetCritBonusStartRangeOk returns a tuple with the CritBonusStartRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCritBonusStartRange

`func (o *WeaponInfoV2) SetCritBonusStartRange(v float32)`

SetCritBonusStartRange sets CritBonusStartRange field to given value.

### HasCritBonusStartRange

`func (o *WeaponInfoV2) HasCritBonusStartRange() bool`

HasCritBonusStartRange returns a boolean if a field has been set.

### SetCritBonusStartRangeNil

`func (o *WeaponInfoV2) SetCritBonusStartRangeNil(b bool)`

 SetCritBonusStartRangeNil sets the value for CritBonusStartRange to be an explicit nil

### UnsetCritBonusStartRange
`func (o *WeaponInfoV2) UnsetCritBonusStartRange()`

UnsetCritBonusStartRange ensures that no value is present for CritBonusStartRange, not even an explicit nil
### GetCycleTime

`func (o *WeaponInfoV2) GetCycleTime() float32`

GetCycleTime returns the CycleTime field if non-nil, zero value otherwise.

### GetCycleTimeOk

`func (o *WeaponInfoV2) GetCycleTimeOk() (*float32, bool)`

GetCycleTimeOk returns a tuple with the CycleTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCycleTime

`func (o *WeaponInfoV2) SetCycleTime(v float32)`

SetCycleTime sets CycleTime field to given value.

### HasCycleTime

`func (o *WeaponInfoV2) HasCycleTime() bool`

HasCycleTime returns a boolean if a field has been set.

### SetCycleTimeNil

`func (o *WeaponInfoV2) SetCycleTimeNil(b bool)`

 SetCycleTimeNil sets the value for CycleTime to be an explicit nil

### UnsetCycleTime
`func (o *WeaponInfoV2) UnsetCycleTime()`

UnsetCycleTime ensures that no value is present for CycleTime, not even an explicit nil
### GetIntraBurstCycleTime

`func (o *WeaponInfoV2) GetIntraBurstCycleTime() float32`

GetIntraBurstCycleTime returns the IntraBurstCycleTime field if non-nil, zero value otherwise.

### GetIntraBurstCycleTimeOk

`func (o *WeaponInfoV2) GetIntraBurstCycleTimeOk() (*float32, bool)`

GetIntraBurstCycleTimeOk returns a tuple with the IntraBurstCycleTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIntraBurstCycleTime

`func (o *WeaponInfoV2) SetIntraBurstCycleTime(v float32)`

SetIntraBurstCycleTime sets IntraBurstCycleTime field to given value.

### HasIntraBurstCycleTime

`func (o *WeaponInfoV2) HasIntraBurstCycleTime() bool`

HasIntraBurstCycleTime returns a boolean if a field has been set.

### SetIntraBurstCycleTimeNil

`func (o *WeaponInfoV2) SetIntraBurstCycleTimeNil(b bool)`

 SetIntraBurstCycleTimeNil sets the value for IntraBurstCycleTime to be an explicit nil

### UnsetIntraBurstCycleTime
`func (o *WeaponInfoV2) UnsetIntraBurstCycleTime()`

UnsetIntraBurstCycleTime ensures that no value is present for IntraBurstCycleTime, not even an explicit nil
### GetMaxSpinCycleTime

`func (o *WeaponInfoV2) GetMaxSpinCycleTime() float32`

GetMaxSpinCycleTime returns the MaxSpinCycleTime field if non-nil, zero value otherwise.

### GetMaxSpinCycleTimeOk

`func (o *WeaponInfoV2) GetMaxSpinCycleTimeOk() (*float32, bool)`

GetMaxSpinCycleTimeOk returns a tuple with the MaxSpinCycleTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxSpinCycleTime

`func (o *WeaponInfoV2) SetMaxSpinCycleTime(v float32)`

SetMaxSpinCycleTime sets MaxSpinCycleTime field to given value.

### HasMaxSpinCycleTime

`func (o *WeaponInfoV2) HasMaxSpinCycleTime() bool`

HasMaxSpinCycleTime returns a boolean if a field has been set.

### SetMaxSpinCycleTimeNil

`func (o *WeaponInfoV2) SetMaxSpinCycleTimeNil(b bool)`

 SetMaxSpinCycleTimeNil sets the value for MaxSpinCycleTime to be an explicit nil

### UnsetMaxSpinCycleTime
`func (o *WeaponInfoV2) UnsetMaxSpinCycleTime()`

UnsetMaxSpinCycleTime ensures that no value is present for MaxSpinCycleTime, not even an explicit nil
### GetDamageFalloffBias

`func (o *WeaponInfoV2) GetDamageFalloffBias() float32`

GetDamageFalloffBias returns the DamageFalloffBias field if non-nil, zero value otherwise.

### GetDamageFalloffBiasOk

`func (o *WeaponInfoV2) GetDamageFalloffBiasOk() (*float32, bool)`

GetDamageFalloffBiasOk returns a tuple with the DamageFalloffBias field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamageFalloffBias

`func (o *WeaponInfoV2) SetDamageFalloffBias(v float32)`

SetDamageFalloffBias sets DamageFalloffBias field to given value.

### HasDamageFalloffBias

`func (o *WeaponInfoV2) HasDamageFalloffBias() bool`

HasDamageFalloffBias returns a boolean if a field has been set.

### SetDamageFalloffBiasNil

`func (o *WeaponInfoV2) SetDamageFalloffBiasNil(b bool)`

 SetDamageFalloffBiasNil sets the value for DamageFalloffBias to be an explicit nil

### UnsetDamageFalloffBias
`func (o *WeaponInfoV2) UnsetDamageFalloffBias()`

UnsetDamageFalloffBias ensures that no value is present for DamageFalloffBias, not even an explicit nil
### GetDamageFalloffEndRange

`func (o *WeaponInfoV2) GetDamageFalloffEndRange() float32`

GetDamageFalloffEndRange returns the DamageFalloffEndRange field if non-nil, zero value otherwise.

### GetDamageFalloffEndRangeOk

`func (o *WeaponInfoV2) GetDamageFalloffEndRangeOk() (*float32, bool)`

GetDamageFalloffEndRangeOk returns a tuple with the DamageFalloffEndRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamageFalloffEndRange

`func (o *WeaponInfoV2) SetDamageFalloffEndRange(v float32)`

SetDamageFalloffEndRange sets DamageFalloffEndRange field to given value.

### HasDamageFalloffEndRange

`func (o *WeaponInfoV2) HasDamageFalloffEndRange() bool`

HasDamageFalloffEndRange returns a boolean if a field has been set.

### SetDamageFalloffEndRangeNil

`func (o *WeaponInfoV2) SetDamageFalloffEndRangeNil(b bool)`

 SetDamageFalloffEndRangeNil sets the value for DamageFalloffEndRange to be an explicit nil

### UnsetDamageFalloffEndRange
`func (o *WeaponInfoV2) UnsetDamageFalloffEndRange()`

UnsetDamageFalloffEndRange ensures that no value is present for DamageFalloffEndRange, not even an explicit nil
### GetDamageFalloffEndScale

`func (o *WeaponInfoV2) GetDamageFalloffEndScale() float32`

GetDamageFalloffEndScale returns the DamageFalloffEndScale field if non-nil, zero value otherwise.

### GetDamageFalloffEndScaleOk

`func (o *WeaponInfoV2) GetDamageFalloffEndScaleOk() (*float32, bool)`

GetDamageFalloffEndScaleOk returns a tuple with the DamageFalloffEndScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamageFalloffEndScale

`func (o *WeaponInfoV2) SetDamageFalloffEndScale(v float32)`

SetDamageFalloffEndScale sets DamageFalloffEndScale field to given value.

### HasDamageFalloffEndScale

`func (o *WeaponInfoV2) HasDamageFalloffEndScale() bool`

HasDamageFalloffEndScale returns a boolean if a field has been set.

### SetDamageFalloffEndScaleNil

`func (o *WeaponInfoV2) SetDamageFalloffEndScaleNil(b bool)`

 SetDamageFalloffEndScaleNil sets the value for DamageFalloffEndScale to be an explicit nil

### UnsetDamageFalloffEndScale
`func (o *WeaponInfoV2) UnsetDamageFalloffEndScale()`

UnsetDamageFalloffEndScale ensures that no value is present for DamageFalloffEndScale, not even an explicit nil
### GetDamageFalloffStartRange

`func (o *WeaponInfoV2) GetDamageFalloffStartRange() float32`

GetDamageFalloffStartRange returns the DamageFalloffStartRange field if non-nil, zero value otherwise.

### GetDamageFalloffStartRangeOk

`func (o *WeaponInfoV2) GetDamageFalloffStartRangeOk() (*float32, bool)`

GetDamageFalloffStartRangeOk returns a tuple with the DamageFalloffStartRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamageFalloffStartRange

`func (o *WeaponInfoV2) SetDamageFalloffStartRange(v float32)`

SetDamageFalloffStartRange sets DamageFalloffStartRange field to given value.

### HasDamageFalloffStartRange

`func (o *WeaponInfoV2) HasDamageFalloffStartRange() bool`

HasDamageFalloffStartRange returns a boolean if a field has been set.

### SetDamageFalloffStartRangeNil

`func (o *WeaponInfoV2) SetDamageFalloffStartRangeNil(b bool)`

 SetDamageFalloffStartRangeNil sets the value for DamageFalloffStartRange to be an explicit nil

### UnsetDamageFalloffStartRange
`func (o *WeaponInfoV2) UnsetDamageFalloffStartRange()`

UnsetDamageFalloffStartRange ensures that no value is present for DamageFalloffStartRange, not even an explicit nil
### GetDamageFalloffStartScale

`func (o *WeaponInfoV2) GetDamageFalloffStartScale() float32`

GetDamageFalloffStartScale returns the DamageFalloffStartScale field if non-nil, zero value otherwise.

### GetDamageFalloffStartScaleOk

`func (o *WeaponInfoV2) GetDamageFalloffStartScaleOk() (*float32, bool)`

GetDamageFalloffStartScaleOk returns a tuple with the DamageFalloffStartScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamageFalloffStartScale

`func (o *WeaponInfoV2) SetDamageFalloffStartScale(v float32)`

SetDamageFalloffStartScale sets DamageFalloffStartScale field to given value.

### HasDamageFalloffStartScale

`func (o *WeaponInfoV2) HasDamageFalloffStartScale() bool`

HasDamageFalloffStartScale returns a boolean if a field has been set.

### SetDamageFalloffStartScaleNil

`func (o *WeaponInfoV2) SetDamageFalloffStartScaleNil(b bool)`

 SetDamageFalloffStartScaleNil sets the value for DamageFalloffStartScale to be an explicit nil

### UnsetDamageFalloffStartScale
`func (o *WeaponInfoV2) UnsetDamageFalloffStartScale()`

UnsetDamageFalloffStartScale ensures that no value is present for DamageFalloffStartScale, not even an explicit nil
### GetHorizontalPunch

`func (o *WeaponInfoV2) GetHorizontalPunch() float32`

GetHorizontalPunch returns the HorizontalPunch field if non-nil, zero value otherwise.

### GetHorizontalPunchOk

`func (o *WeaponInfoV2) GetHorizontalPunchOk() (*float32, bool)`

GetHorizontalPunchOk returns a tuple with the HorizontalPunch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHorizontalPunch

`func (o *WeaponInfoV2) SetHorizontalPunch(v float32)`

SetHorizontalPunch sets HorizontalPunch field to given value.

### HasHorizontalPunch

`func (o *WeaponInfoV2) HasHorizontalPunch() bool`

HasHorizontalPunch returns a boolean if a field has been set.

### SetHorizontalPunchNil

`func (o *WeaponInfoV2) SetHorizontalPunchNil(b bool)`

 SetHorizontalPunchNil sets the value for HorizontalPunch to be an explicit nil

### UnsetHorizontalPunch
`func (o *WeaponInfoV2) UnsetHorizontalPunch()`

UnsetHorizontalPunch ensures that no value is present for HorizontalPunch, not even an explicit nil
### GetRange

`func (o *WeaponInfoV2) GetRange() float32`

GetRange returns the Range field if non-nil, zero value otherwise.

### GetRangeOk

`func (o *WeaponInfoV2) GetRangeOk() (*float32, bool)`

GetRangeOk returns a tuple with the Range field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRange

`func (o *WeaponInfoV2) SetRange(v float32)`

SetRange sets Range field to given value.

### HasRange

`func (o *WeaponInfoV2) HasRange() bool`

HasRange returns a boolean if a field has been set.

### SetRangeNil

`func (o *WeaponInfoV2) SetRangeNil(b bool)`

 SetRangeNil sets the value for Range to be an explicit nil

### UnsetRange
`func (o *WeaponInfoV2) UnsetRange()`

UnsetRange ensures that no value is present for Range, not even an explicit nil
### GetRecoilRecoveryDelayFactor

`func (o *WeaponInfoV2) GetRecoilRecoveryDelayFactor() float32`

GetRecoilRecoveryDelayFactor returns the RecoilRecoveryDelayFactor field if non-nil, zero value otherwise.

### GetRecoilRecoveryDelayFactorOk

`func (o *WeaponInfoV2) GetRecoilRecoveryDelayFactorOk() (*float32, bool)`

GetRecoilRecoveryDelayFactorOk returns a tuple with the RecoilRecoveryDelayFactor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecoilRecoveryDelayFactor

`func (o *WeaponInfoV2) SetRecoilRecoveryDelayFactor(v float32)`

SetRecoilRecoveryDelayFactor sets RecoilRecoveryDelayFactor field to given value.

### HasRecoilRecoveryDelayFactor

`func (o *WeaponInfoV2) HasRecoilRecoveryDelayFactor() bool`

HasRecoilRecoveryDelayFactor returns a boolean if a field has been set.

### SetRecoilRecoveryDelayFactorNil

`func (o *WeaponInfoV2) SetRecoilRecoveryDelayFactorNil(b bool)`

 SetRecoilRecoveryDelayFactorNil sets the value for RecoilRecoveryDelayFactor to be an explicit nil

### UnsetRecoilRecoveryDelayFactor
`func (o *WeaponInfoV2) UnsetRecoilRecoveryDelayFactor()`

UnsetRecoilRecoveryDelayFactor ensures that no value is present for RecoilRecoveryDelayFactor, not even an explicit nil
### GetRecoilRecoverySpeed

`func (o *WeaponInfoV2) GetRecoilRecoverySpeed() float32`

GetRecoilRecoverySpeed returns the RecoilRecoverySpeed field if non-nil, zero value otherwise.

### GetRecoilRecoverySpeedOk

`func (o *WeaponInfoV2) GetRecoilRecoverySpeedOk() (*float32, bool)`

GetRecoilRecoverySpeedOk returns a tuple with the RecoilRecoverySpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecoilRecoverySpeed

`func (o *WeaponInfoV2) SetRecoilRecoverySpeed(v float32)`

SetRecoilRecoverySpeed sets RecoilRecoverySpeed field to given value.

### HasRecoilRecoverySpeed

`func (o *WeaponInfoV2) HasRecoilRecoverySpeed() bool`

HasRecoilRecoverySpeed returns a boolean if a field has been set.

### SetRecoilRecoverySpeedNil

`func (o *WeaponInfoV2) SetRecoilRecoverySpeedNil(b bool)`

 SetRecoilRecoverySpeedNil sets the value for RecoilRecoverySpeed to be an explicit nil

### UnsetRecoilRecoverySpeed
`func (o *WeaponInfoV2) UnsetRecoilRecoverySpeed()`

UnsetRecoilRecoverySpeed ensures that no value is present for RecoilRecoverySpeed, not even an explicit nil
### GetRecoilShotIndexRecoveryTimeFactor

`func (o *WeaponInfoV2) GetRecoilShotIndexRecoveryTimeFactor() float32`

GetRecoilShotIndexRecoveryTimeFactor returns the RecoilShotIndexRecoveryTimeFactor field if non-nil, zero value otherwise.

### GetRecoilShotIndexRecoveryTimeFactorOk

`func (o *WeaponInfoV2) GetRecoilShotIndexRecoveryTimeFactorOk() (*float32, bool)`

GetRecoilShotIndexRecoveryTimeFactorOk returns a tuple with the RecoilShotIndexRecoveryTimeFactor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecoilShotIndexRecoveryTimeFactor

`func (o *WeaponInfoV2) SetRecoilShotIndexRecoveryTimeFactor(v float32)`

SetRecoilShotIndexRecoveryTimeFactor sets RecoilShotIndexRecoveryTimeFactor field to given value.

### HasRecoilShotIndexRecoveryTimeFactor

`func (o *WeaponInfoV2) HasRecoilShotIndexRecoveryTimeFactor() bool`

HasRecoilShotIndexRecoveryTimeFactor returns a boolean if a field has been set.

### SetRecoilShotIndexRecoveryTimeFactorNil

`func (o *WeaponInfoV2) SetRecoilShotIndexRecoveryTimeFactorNil(b bool)`

 SetRecoilShotIndexRecoveryTimeFactorNil sets the value for RecoilShotIndexRecoveryTimeFactor to be an explicit nil

### UnsetRecoilShotIndexRecoveryTimeFactor
`func (o *WeaponInfoV2) UnsetRecoilShotIndexRecoveryTimeFactor()`

UnsetRecoilShotIndexRecoveryTimeFactor ensures that no value is present for RecoilShotIndexRecoveryTimeFactor, not even an explicit nil
### GetRecoilSpeed

`func (o *WeaponInfoV2) GetRecoilSpeed() float32`

GetRecoilSpeed returns the RecoilSpeed field if non-nil, zero value otherwise.

### GetRecoilSpeedOk

`func (o *WeaponInfoV2) GetRecoilSpeedOk() (*float32, bool)`

GetRecoilSpeedOk returns a tuple with the RecoilSpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecoilSpeed

`func (o *WeaponInfoV2) SetRecoilSpeed(v float32)`

SetRecoilSpeed sets RecoilSpeed field to given value.

### HasRecoilSpeed

`func (o *WeaponInfoV2) HasRecoilSpeed() bool`

HasRecoilSpeed returns a boolean if a field has been set.

### SetRecoilSpeedNil

`func (o *WeaponInfoV2) SetRecoilSpeedNil(b bool)`

 SetRecoilSpeedNil sets the value for RecoilSpeed to be an explicit nil

### UnsetRecoilSpeed
`func (o *WeaponInfoV2) UnsetRecoilSpeed()`

UnsetRecoilSpeed ensures that no value is present for RecoilSpeed, not even an explicit nil
### GetReloadMoveSpeed

`func (o *WeaponInfoV2) GetReloadMoveSpeed() float32`

GetReloadMoveSpeed returns the ReloadMoveSpeed field if non-nil, zero value otherwise.

### GetReloadMoveSpeedOk

`func (o *WeaponInfoV2) GetReloadMoveSpeedOk() (*float32, bool)`

GetReloadMoveSpeedOk returns a tuple with the ReloadMoveSpeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReloadMoveSpeed

`func (o *WeaponInfoV2) SetReloadMoveSpeed(v float32)`

SetReloadMoveSpeed sets ReloadMoveSpeed field to given value.

### HasReloadMoveSpeed

`func (o *WeaponInfoV2) HasReloadMoveSpeed() bool`

HasReloadMoveSpeed returns a boolean if a field has been set.

### SetReloadMoveSpeedNil

`func (o *WeaponInfoV2) SetReloadMoveSpeedNil(b bool)`

 SetReloadMoveSpeedNil sets the value for ReloadMoveSpeed to be an explicit nil

### UnsetReloadMoveSpeed
`func (o *WeaponInfoV2) UnsetReloadMoveSpeed()`

UnsetReloadMoveSpeed ensures that no value is present for ReloadMoveSpeed, not even an explicit nil
### GetScatterYawScale

`func (o *WeaponInfoV2) GetScatterYawScale() float32`

GetScatterYawScale returns the ScatterYawScale field if non-nil, zero value otherwise.

### GetScatterYawScaleOk

`func (o *WeaponInfoV2) GetScatterYawScaleOk() (*float32, bool)`

GetScatterYawScaleOk returns a tuple with the ScatterYawScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScatterYawScale

`func (o *WeaponInfoV2) SetScatterYawScale(v float32)`

SetScatterYawScale sets ScatterYawScale field to given value.

### HasScatterYawScale

`func (o *WeaponInfoV2) HasScatterYawScale() bool`

HasScatterYawScale returns a boolean if a field has been set.

### SetScatterYawScaleNil

`func (o *WeaponInfoV2) SetScatterYawScaleNil(b bool)`

 SetScatterYawScaleNil sets the value for ScatterYawScale to be an explicit nil

### UnsetScatterYawScale
`func (o *WeaponInfoV2) UnsetScatterYawScale()`

UnsetScatterYawScale ensures that no value is present for ScatterYawScale, not even an explicit nil
### GetAimingShotSpreadPenalty

`func (o *WeaponInfoV2) GetAimingShotSpreadPenalty() AimingShotSpreadPenalty`

GetAimingShotSpreadPenalty returns the AimingShotSpreadPenalty field if non-nil, zero value otherwise.

### GetAimingShotSpreadPenaltyOk

`func (o *WeaponInfoV2) GetAimingShotSpreadPenaltyOk() (*AimingShotSpreadPenalty, bool)`

GetAimingShotSpreadPenaltyOk returns a tuple with the AimingShotSpreadPenalty field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAimingShotSpreadPenalty

`func (o *WeaponInfoV2) SetAimingShotSpreadPenalty(v AimingShotSpreadPenalty)`

SetAimingShotSpreadPenalty sets AimingShotSpreadPenalty field to given value.

### HasAimingShotSpreadPenalty

`func (o *WeaponInfoV2) HasAimingShotSpreadPenalty() bool`

HasAimingShotSpreadPenalty returns a boolean if a field has been set.

### SetAimingShotSpreadPenaltyNil

`func (o *WeaponInfoV2) SetAimingShotSpreadPenaltyNil(b bool)`

 SetAimingShotSpreadPenaltyNil sets the value for AimingShotSpreadPenalty to be an explicit nil

### UnsetAimingShotSpreadPenalty
`func (o *WeaponInfoV2) UnsetAimingShotSpreadPenalty()`

UnsetAimingShotSpreadPenalty ensures that no value is present for AimingShotSpreadPenalty, not even an explicit nil
### GetStandingShotSpreadPenalty

`func (o *WeaponInfoV2) GetStandingShotSpreadPenalty() StandingShotSpreadPenalty`

GetStandingShotSpreadPenalty returns the StandingShotSpreadPenalty field if non-nil, zero value otherwise.

### GetStandingShotSpreadPenaltyOk

`func (o *WeaponInfoV2) GetStandingShotSpreadPenaltyOk() (*StandingShotSpreadPenalty, bool)`

GetStandingShotSpreadPenaltyOk returns a tuple with the StandingShotSpreadPenalty field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStandingShotSpreadPenalty

`func (o *WeaponInfoV2) SetStandingShotSpreadPenalty(v StandingShotSpreadPenalty)`

SetStandingShotSpreadPenalty sets StandingShotSpreadPenalty field to given value.

### HasStandingShotSpreadPenalty

`func (o *WeaponInfoV2) HasStandingShotSpreadPenalty() bool`

HasStandingShotSpreadPenalty returns a boolean if a field has been set.

### SetStandingShotSpreadPenaltyNil

`func (o *WeaponInfoV2) SetStandingShotSpreadPenaltyNil(b bool)`

 SetStandingShotSpreadPenaltyNil sets the value for StandingShotSpreadPenalty to be an explicit nil

### UnsetStandingShotSpreadPenalty
`func (o *WeaponInfoV2) UnsetStandingShotSpreadPenalty()`

UnsetStandingShotSpreadPenalty ensures that no value is present for StandingShotSpreadPenalty, not even an explicit nil
### GetShootMoveSpeedPercent

`func (o *WeaponInfoV2) GetShootMoveSpeedPercent() float32`

GetShootMoveSpeedPercent returns the ShootMoveSpeedPercent field if non-nil, zero value otherwise.

### GetShootMoveSpeedPercentOk

`func (o *WeaponInfoV2) GetShootMoveSpeedPercentOk() (*float32, bool)`

GetShootMoveSpeedPercentOk returns a tuple with the ShootMoveSpeedPercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShootMoveSpeedPercent

`func (o *WeaponInfoV2) SetShootMoveSpeedPercent(v float32)`

SetShootMoveSpeedPercent sets ShootMoveSpeedPercent field to given value.

### HasShootMoveSpeedPercent

`func (o *WeaponInfoV2) HasShootMoveSpeedPercent() bool`

HasShootMoveSpeedPercent returns a boolean if a field has been set.

### SetShootMoveSpeedPercentNil

`func (o *WeaponInfoV2) SetShootMoveSpeedPercentNil(b bool)`

 SetShootMoveSpeedPercentNil sets the value for ShootMoveSpeedPercent to be an explicit nil

### UnsetShootMoveSpeedPercent
`func (o *WeaponInfoV2) UnsetShootMoveSpeedPercent()`

UnsetShootMoveSpeedPercent ensures that no value is present for ShootMoveSpeedPercent, not even an explicit nil
### GetShootSpreadPenaltyDecay

`func (o *WeaponInfoV2) GetShootSpreadPenaltyDecay() float32`

GetShootSpreadPenaltyDecay returns the ShootSpreadPenaltyDecay field if non-nil, zero value otherwise.

### GetShootSpreadPenaltyDecayOk

`func (o *WeaponInfoV2) GetShootSpreadPenaltyDecayOk() (*float32, bool)`

GetShootSpreadPenaltyDecayOk returns a tuple with the ShootSpreadPenaltyDecay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShootSpreadPenaltyDecay

`func (o *WeaponInfoV2) SetShootSpreadPenaltyDecay(v float32)`

SetShootSpreadPenaltyDecay sets ShootSpreadPenaltyDecay field to given value.

### HasShootSpreadPenaltyDecay

`func (o *WeaponInfoV2) HasShootSpreadPenaltyDecay() bool`

HasShootSpreadPenaltyDecay returns a boolean if a field has been set.

### SetShootSpreadPenaltyDecayNil

`func (o *WeaponInfoV2) SetShootSpreadPenaltyDecayNil(b bool)`

 SetShootSpreadPenaltyDecayNil sets the value for ShootSpreadPenaltyDecay to be an explicit nil

### UnsetShootSpreadPenaltyDecay
`func (o *WeaponInfoV2) UnsetShootSpreadPenaltyDecay()`

UnsetShootSpreadPenaltyDecay ensures that no value is present for ShootSpreadPenaltyDecay, not even an explicit nil
### GetShootSpreadPenaltyDecayDelay

`func (o *WeaponInfoV2) GetShootSpreadPenaltyDecayDelay() float32`

GetShootSpreadPenaltyDecayDelay returns the ShootSpreadPenaltyDecayDelay field if non-nil, zero value otherwise.

### GetShootSpreadPenaltyDecayDelayOk

`func (o *WeaponInfoV2) GetShootSpreadPenaltyDecayDelayOk() (*float32, bool)`

GetShootSpreadPenaltyDecayDelayOk returns a tuple with the ShootSpreadPenaltyDecayDelay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShootSpreadPenaltyDecayDelay

`func (o *WeaponInfoV2) SetShootSpreadPenaltyDecayDelay(v float32)`

SetShootSpreadPenaltyDecayDelay sets ShootSpreadPenaltyDecayDelay field to given value.

### HasShootSpreadPenaltyDecayDelay

`func (o *WeaponInfoV2) HasShootSpreadPenaltyDecayDelay() bool`

HasShootSpreadPenaltyDecayDelay returns a boolean if a field has been set.

### SetShootSpreadPenaltyDecayDelayNil

`func (o *WeaponInfoV2) SetShootSpreadPenaltyDecayDelayNil(b bool)`

 SetShootSpreadPenaltyDecayDelayNil sets the value for ShootSpreadPenaltyDecayDelay to be an explicit nil

### UnsetShootSpreadPenaltyDecayDelay
`func (o *WeaponInfoV2) UnsetShootSpreadPenaltyDecayDelay()`

UnsetShootSpreadPenaltyDecayDelay ensures that no value is present for ShootSpreadPenaltyDecayDelay, not even an explicit nil
### GetShootSpreadPenaltyPerShot

`func (o *WeaponInfoV2) GetShootSpreadPenaltyPerShot() float32`

GetShootSpreadPenaltyPerShot returns the ShootSpreadPenaltyPerShot field if non-nil, zero value otherwise.

### GetShootSpreadPenaltyPerShotOk

`func (o *WeaponInfoV2) GetShootSpreadPenaltyPerShotOk() (*float32, bool)`

GetShootSpreadPenaltyPerShotOk returns a tuple with the ShootSpreadPenaltyPerShot field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShootSpreadPenaltyPerShot

`func (o *WeaponInfoV2) SetShootSpreadPenaltyPerShot(v float32)`

SetShootSpreadPenaltyPerShot sets ShootSpreadPenaltyPerShot field to given value.

### HasShootSpreadPenaltyPerShot

`func (o *WeaponInfoV2) HasShootSpreadPenaltyPerShot() bool`

HasShootSpreadPenaltyPerShot returns a boolean if a field has been set.

### SetShootSpreadPenaltyPerShotNil

`func (o *WeaponInfoV2) SetShootSpreadPenaltyPerShotNil(b bool)`

 SetShootSpreadPenaltyPerShotNil sets the value for ShootSpreadPenaltyPerShot to be an explicit nil

### UnsetShootSpreadPenaltyPerShot
`func (o *WeaponInfoV2) UnsetShootSpreadPenaltyPerShot()`

UnsetShootSpreadPenaltyPerShot ensures that no value is present for ShootSpreadPenaltyPerShot, not even an explicit nil
### GetShootingUpSpreadPenalty

`func (o *WeaponInfoV2) GetShootingUpSpreadPenalty() float32`

GetShootingUpSpreadPenalty returns the ShootingUpSpreadPenalty field if non-nil, zero value otherwise.

### GetShootingUpSpreadPenaltyOk

`func (o *WeaponInfoV2) GetShootingUpSpreadPenaltyOk() (*float32, bool)`

GetShootingUpSpreadPenaltyOk returns a tuple with the ShootingUpSpreadPenalty field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShootingUpSpreadPenalty

`func (o *WeaponInfoV2) SetShootingUpSpreadPenalty(v float32)`

SetShootingUpSpreadPenalty sets ShootingUpSpreadPenalty field to given value.

### HasShootingUpSpreadPenalty

`func (o *WeaponInfoV2) HasShootingUpSpreadPenalty() bool`

HasShootingUpSpreadPenalty returns a boolean if a field has been set.

### SetShootingUpSpreadPenaltyNil

`func (o *WeaponInfoV2) SetShootingUpSpreadPenaltyNil(b bool)`

 SetShootingUpSpreadPenaltyNil sets the value for ShootingUpSpreadPenalty to be an explicit nil

### UnsetShootingUpSpreadPenalty
`func (o *WeaponInfoV2) UnsetShootingUpSpreadPenalty()`

UnsetShootingUpSpreadPenalty ensures that no value is present for ShootingUpSpreadPenalty, not even an explicit nil
### GetVerticalPunch

`func (o *WeaponInfoV2) GetVerticalPunch() float32`

GetVerticalPunch returns the VerticalPunch field if non-nil, zero value otherwise.

### GetVerticalPunchOk

`func (o *WeaponInfoV2) GetVerticalPunchOk() (*float32, bool)`

GetVerticalPunchOk returns a tuple with the VerticalPunch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerticalPunch

`func (o *WeaponInfoV2) SetVerticalPunch(v float32)`

SetVerticalPunch sets VerticalPunch field to given value.

### HasVerticalPunch

`func (o *WeaponInfoV2) HasVerticalPunch() bool`

HasVerticalPunch returns a boolean if a field has been set.

### SetVerticalPunchNil

`func (o *WeaponInfoV2) SetVerticalPunchNil(b bool)`

 SetVerticalPunchNil sets the value for VerticalPunch to be an explicit nil

### UnsetVerticalPunch
`func (o *WeaponInfoV2) UnsetVerticalPunch()`

UnsetVerticalPunch ensures that no value is present for VerticalPunch, not even an explicit nil
### GetZoomFov

`func (o *WeaponInfoV2) GetZoomFov() float32`

GetZoomFov returns the ZoomFov field if non-nil, zero value otherwise.

### GetZoomFovOk

`func (o *WeaponInfoV2) GetZoomFovOk() (*float32, bool)`

GetZoomFovOk returns a tuple with the ZoomFov field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetZoomFov

`func (o *WeaponInfoV2) SetZoomFov(v float32)`

SetZoomFov sets ZoomFov field to given value.

### HasZoomFov

`func (o *WeaponInfoV2) HasZoomFov() bool`

HasZoomFov returns a boolean if a field has been set.

### SetZoomFovNil

`func (o *WeaponInfoV2) SetZoomFovNil(b bool)`

 SetZoomFovNil sets the value for ZoomFov to be an explicit nil

### UnsetZoomFov
`func (o *WeaponInfoV2) UnsetZoomFov()`

UnsetZoomFov ensures that no value is present for ZoomFov, not even an explicit nil
### GetZoomMoveSpeedPercent

`func (o *WeaponInfoV2) GetZoomMoveSpeedPercent() float32`

GetZoomMoveSpeedPercent returns the ZoomMoveSpeedPercent field if non-nil, zero value otherwise.

### GetZoomMoveSpeedPercentOk

`func (o *WeaponInfoV2) GetZoomMoveSpeedPercentOk() (*float32, bool)`

GetZoomMoveSpeedPercentOk returns a tuple with the ZoomMoveSpeedPercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetZoomMoveSpeedPercent

`func (o *WeaponInfoV2) SetZoomMoveSpeedPercent(v float32)`

SetZoomMoveSpeedPercent sets ZoomMoveSpeedPercent field to given value.

### HasZoomMoveSpeedPercent

`func (o *WeaponInfoV2) HasZoomMoveSpeedPercent() bool`

HasZoomMoveSpeedPercent returns a boolean if a field has been set.

### SetZoomMoveSpeedPercentNil

`func (o *WeaponInfoV2) SetZoomMoveSpeedPercentNil(b bool)`

 SetZoomMoveSpeedPercentNil sets the value for ZoomMoveSpeedPercent to be an explicit nil

### UnsetZoomMoveSpeedPercent
`func (o *WeaponInfoV2) UnsetZoomMoveSpeedPercent()`

UnsetZoomMoveSpeedPercent ensures that no value is present for ZoomMoveSpeedPercent, not even an explicit nil
### GetBullets

`func (o *WeaponInfoV2) GetBullets() int32`

GetBullets returns the Bullets field if non-nil, zero value otherwise.

### GetBulletsOk

`func (o *WeaponInfoV2) GetBulletsOk() (*int32, bool)`

GetBulletsOk returns a tuple with the Bullets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBullets

`func (o *WeaponInfoV2) SetBullets(v int32)`

SetBullets sets Bullets field to given value.

### HasBullets

`func (o *WeaponInfoV2) HasBullets() bool`

HasBullets returns a boolean if a field has been set.

### SetBulletsNil

`func (o *WeaponInfoV2) SetBulletsNil(b bool)`

 SetBulletsNil sets the value for Bullets to be an explicit nil

### UnsetBullets
`func (o *WeaponInfoV2) UnsetBullets()`

UnsetBullets ensures that no value is present for Bullets, not even an explicit nil
### GetReloadSingleBulletsInitialDelay

`func (o *WeaponInfoV2) GetReloadSingleBulletsInitialDelay() float32`

GetReloadSingleBulletsInitialDelay returns the ReloadSingleBulletsInitialDelay field if non-nil, zero value otherwise.

### GetReloadSingleBulletsInitialDelayOk

`func (o *WeaponInfoV2) GetReloadSingleBulletsInitialDelayOk() (*float32, bool)`

GetReloadSingleBulletsInitialDelayOk returns a tuple with the ReloadSingleBulletsInitialDelay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReloadSingleBulletsInitialDelay

`func (o *WeaponInfoV2) SetReloadSingleBulletsInitialDelay(v float32)`

SetReloadSingleBulletsInitialDelay sets ReloadSingleBulletsInitialDelay field to given value.

### HasReloadSingleBulletsInitialDelay

`func (o *WeaponInfoV2) HasReloadSingleBulletsInitialDelay() bool`

HasReloadSingleBulletsInitialDelay returns a boolean if a field has been set.

### SetReloadSingleBulletsInitialDelayNil

`func (o *WeaponInfoV2) SetReloadSingleBulletsInitialDelayNil(b bool)`

 SetReloadSingleBulletsInitialDelayNil sets the value for ReloadSingleBulletsInitialDelay to be an explicit nil

### UnsetReloadSingleBulletsInitialDelay
`func (o *WeaponInfoV2) UnsetReloadSingleBulletsInitialDelay()`

UnsetReloadSingleBulletsInitialDelay ensures that no value is present for ReloadSingleBulletsInitialDelay, not even an explicit nil
### GetReloadSingleBullets

`func (o *WeaponInfoV2) GetReloadSingleBullets() bool`

GetReloadSingleBullets returns the ReloadSingleBullets field if non-nil, zero value otherwise.

### GetReloadSingleBulletsOk

`func (o *WeaponInfoV2) GetReloadSingleBulletsOk() (*bool, bool)`

GetReloadSingleBulletsOk returns a tuple with the ReloadSingleBullets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReloadSingleBullets

`func (o *WeaponInfoV2) SetReloadSingleBullets(v bool)`

SetReloadSingleBullets sets ReloadSingleBullets field to given value.

### HasReloadSingleBullets

`func (o *WeaponInfoV2) HasReloadSingleBullets() bool`

HasReloadSingleBullets returns a boolean if a field has been set.

### SetReloadSingleBulletsNil

`func (o *WeaponInfoV2) SetReloadSingleBulletsNil(b bool)`

 SetReloadSingleBulletsNil sets the value for ReloadSingleBullets to be an explicit nil

### UnsetReloadSingleBullets
`func (o *WeaponInfoV2) UnsetReloadSingleBullets()`

UnsetReloadSingleBullets ensures that no value is present for ReloadSingleBullets, not even an explicit nil
### GetReloadSingleBulletsAllowCancel

`func (o *WeaponInfoV2) GetReloadSingleBulletsAllowCancel() bool`

GetReloadSingleBulletsAllowCancel returns the ReloadSingleBulletsAllowCancel field if non-nil, zero value otherwise.

### GetReloadSingleBulletsAllowCancelOk

`func (o *WeaponInfoV2) GetReloadSingleBulletsAllowCancelOk() (*bool, bool)`

GetReloadSingleBulletsAllowCancelOk returns a tuple with the ReloadSingleBulletsAllowCancel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReloadSingleBulletsAllowCancel

`func (o *WeaponInfoV2) SetReloadSingleBulletsAllowCancel(v bool)`

SetReloadSingleBulletsAllowCancel sets ReloadSingleBulletsAllowCancel field to given value.

### HasReloadSingleBulletsAllowCancel

`func (o *WeaponInfoV2) HasReloadSingleBulletsAllowCancel() bool`

HasReloadSingleBulletsAllowCancel returns a boolean if a field has been set.

### SetReloadSingleBulletsAllowCancelNil

`func (o *WeaponInfoV2) SetReloadSingleBulletsAllowCancelNil(b bool)`

 SetReloadSingleBulletsAllowCancelNil sets the value for ReloadSingleBulletsAllowCancel to be an explicit nil

### UnsetReloadSingleBulletsAllowCancel
`func (o *WeaponInfoV2) UnsetReloadSingleBulletsAllowCancel()`

UnsetReloadSingleBulletsAllowCancel ensures that no value is present for ReloadSingleBulletsAllowCancel, not even an explicit nil
### GetBurstShotCount

`func (o *WeaponInfoV2) GetBurstShotCount() int32`

GetBurstShotCount returns the BurstShotCount field if non-nil, zero value otherwise.

### GetBurstShotCountOk

`func (o *WeaponInfoV2) GetBurstShotCountOk() (*int32, bool)`

GetBurstShotCountOk returns a tuple with the BurstShotCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBurstShotCount

`func (o *WeaponInfoV2) SetBurstShotCount(v int32)`

SetBurstShotCount sets BurstShotCount field to given value.

### HasBurstShotCount

`func (o *WeaponInfoV2) HasBurstShotCount() bool`

HasBurstShotCount returns a boolean if a field has been set.

### SetBurstShotCountNil

`func (o *WeaponInfoV2) SetBurstShotCountNil(b bool)`

 SetBurstShotCountNil sets the value for BurstShotCount to be an explicit nil

### UnsetBurstShotCount
`func (o *WeaponInfoV2) UnsetBurstShotCount()`

UnsetBurstShotCount ensures that no value is present for BurstShotCount, not even an explicit nil
### GetClipSize

`func (o *WeaponInfoV2) GetClipSize() int32`

GetClipSize returns the ClipSize field if non-nil, zero value otherwise.

### GetClipSizeOk

`func (o *WeaponInfoV2) GetClipSizeOk() (*int32, bool)`

GetClipSizeOk returns a tuple with the ClipSize field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClipSize

`func (o *WeaponInfoV2) SetClipSize(v int32)`

SetClipSize sets ClipSize field to given value.

### HasClipSize

`func (o *WeaponInfoV2) HasClipSize() bool`

HasClipSize returns a boolean if a field has been set.

### SetClipSizeNil

`func (o *WeaponInfoV2) SetClipSizeNil(b bool)`

 SetClipSizeNil sets the value for ClipSize to be an explicit nil

### UnsetClipSize
`func (o *WeaponInfoV2) UnsetClipSize()`

UnsetClipSize ensures that no value is present for ClipSize, not even an explicit nil
### GetSpread

`func (o *WeaponInfoV2) GetSpread() float32`

GetSpread returns the Spread field if non-nil, zero value otherwise.

### GetSpreadOk

`func (o *WeaponInfoV2) GetSpreadOk() (*float32, bool)`

GetSpreadOk returns a tuple with the Spread field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpread

`func (o *WeaponInfoV2) SetSpread(v float32)`

SetSpread sets Spread field to given value.

### HasSpread

`func (o *WeaponInfoV2) HasSpread() bool`

HasSpread returns a boolean if a field has been set.

### SetSpreadNil

`func (o *WeaponInfoV2) SetSpreadNil(b bool)`

 SetSpreadNil sets the value for Spread to be an explicit nil

### UnsetSpread
`func (o *WeaponInfoV2) UnsetSpread()`

UnsetSpread ensures that no value is present for Spread, not even an explicit nil
### GetStandingSpread

`func (o *WeaponInfoV2) GetStandingSpread() float32`

GetStandingSpread returns the StandingSpread field if non-nil, zero value otherwise.

### GetStandingSpreadOk

`func (o *WeaponInfoV2) GetStandingSpreadOk() (*float32, bool)`

GetStandingSpreadOk returns a tuple with the StandingSpread field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStandingSpread

`func (o *WeaponInfoV2) SetStandingSpread(v float32)`

SetStandingSpread sets StandingSpread field to given value.

### HasStandingSpread

`func (o *WeaponInfoV2) HasStandingSpread() bool`

HasStandingSpread returns a boolean if a field has been set.

### SetStandingSpreadNil

`func (o *WeaponInfoV2) SetStandingSpreadNil(b bool)`

 SetStandingSpreadNil sets the value for StandingSpread to be an explicit nil

### UnsetStandingSpread
`func (o *WeaponInfoV2) UnsetStandingSpread()`

UnsetStandingSpread ensures that no value is present for StandingSpread, not even an explicit nil
### GetLowAmmoIndicatorThreshold

`func (o *WeaponInfoV2) GetLowAmmoIndicatorThreshold() float32`

GetLowAmmoIndicatorThreshold returns the LowAmmoIndicatorThreshold field if non-nil, zero value otherwise.

### GetLowAmmoIndicatorThresholdOk

`func (o *WeaponInfoV2) GetLowAmmoIndicatorThresholdOk() (*float32, bool)`

GetLowAmmoIndicatorThresholdOk returns a tuple with the LowAmmoIndicatorThreshold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLowAmmoIndicatorThreshold

`func (o *WeaponInfoV2) SetLowAmmoIndicatorThreshold(v float32)`

SetLowAmmoIndicatorThreshold sets LowAmmoIndicatorThreshold field to given value.

### HasLowAmmoIndicatorThreshold

`func (o *WeaponInfoV2) HasLowAmmoIndicatorThreshold() bool`

HasLowAmmoIndicatorThreshold returns a boolean if a field has been set.

### SetLowAmmoIndicatorThresholdNil

`func (o *WeaponInfoV2) SetLowAmmoIndicatorThresholdNil(b bool)`

 SetLowAmmoIndicatorThresholdNil sets the value for LowAmmoIndicatorThreshold to be an explicit nil

### UnsetLowAmmoIndicatorThreshold
`func (o *WeaponInfoV2) UnsetLowAmmoIndicatorThreshold()`

UnsetLowAmmoIndicatorThreshold ensures that no value is present for LowAmmoIndicatorThreshold, not even an explicit nil
### GetRecoilSeed

`func (o *WeaponInfoV2) GetRecoilSeed() float32`

GetRecoilSeed returns the RecoilSeed field if non-nil, zero value otherwise.

### GetRecoilSeedOk

`func (o *WeaponInfoV2) GetRecoilSeedOk() (*float32, bool)`

GetRecoilSeedOk returns a tuple with the RecoilSeed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecoilSeed

`func (o *WeaponInfoV2) SetRecoilSeed(v float32)`

SetRecoilSeed sets RecoilSeed field to given value.

### HasRecoilSeed

`func (o *WeaponInfoV2) HasRecoilSeed() bool`

HasRecoilSeed returns a boolean if a field has been set.

### SetRecoilSeedNil

`func (o *WeaponInfoV2) SetRecoilSeedNil(b bool)`

 SetRecoilSeedNil sets the value for RecoilSeed to be an explicit nil

### UnsetRecoilSeed
`func (o *WeaponInfoV2) UnsetRecoilSeed()`

UnsetRecoilSeed ensures that no value is present for RecoilSeed, not even an explicit nil
### GetReloadDuration

`func (o *WeaponInfoV2) GetReloadDuration() float32`

GetReloadDuration returns the ReloadDuration field if non-nil, zero value otherwise.

### GetReloadDurationOk

`func (o *WeaponInfoV2) GetReloadDurationOk() (*float32, bool)`

GetReloadDurationOk returns a tuple with the ReloadDuration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReloadDuration

`func (o *WeaponInfoV2) SetReloadDuration(v float32)`

SetReloadDuration sets ReloadDuration field to given value.

### HasReloadDuration

`func (o *WeaponInfoV2) HasReloadDuration() bool`

HasReloadDuration returns a boolean if a field has been set.

### SetReloadDurationNil

`func (o *WeaponInfoV2) SetReloadDurationNil(b bool)`

 SetReloadDurationNil sets the value for ReloadDuration to be an explicit nil

### UnsetReloadDuration
`func (o *WeaponInfoV2) UnsetReloadDuration()`

UnsetReloadDuration ensures that no value is present for ReloadDuration, not even an explicit nil
### GetBulletSpeedCurve

`func (o *WeaponInfoV2) GetBulletSpeedCurve() RawItemWeaponInfoBulletSpeedCurveV2`

GetBulletSpeedCurve returns the BulletSpeedCurve field if non-nil, zero value otherwise.

### GetBulletSpeedCurveOk

`func (o *WeaponInfoV2) GetBulletSpeedCurveOk() (*RawItemWeaponInfoBulletSpeedCurveV2, bool)`

GetBulletSpeedCurveOk returns a tuple with the BulletSpeedCurve field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletSpeedCurve

`func (o *WeaponInfoV2) SetBulletSpeedCurve(v RawItemWeaponInfoBulletSpeedCurveV2)`

SetBulletSpeedCurve sets BulletSpeedCurve field to given value.

### HasBulletSpeedCurve

`func (o *WeaponInfoV2) HasBulletSpeedCurve() bool`

HasBulletSpeedCurve returns a boolean if a field has been set.

### SetBulletSpeedCurveNil

`func (o *WeaponInfoV2) SetBulletSpeedCurveNil(b bool)`

 SetBulletSpeedCurveNil sets the value for BulletSpeedCurve to be an explicit nil

### UnsetBulletSpeedCurve
`func (o *WeaponInfoV2) UnsetBulletSpeedCurve()`

UnsetBulletSpeedCurve ensures that no value is present for BulletSpeedCurve, not even an explicit nil
### GetHorizontalRecoil

`func (o *WeaponInfoV2) GetHorizontalRecoil() RawWeaponInfoHorizontalRecoilV2`

GetHorizontalRecoil returns the HorizontalRecoil field if non-nil, zero value otherwise.

### GetHorizontalRecoilOk

`func (o *WeaponInfoV2) GetHorizontalRecoilOk() (*RawWeaponInfoHorizontalRecoilV2, bool)`

GetHorizontalRecoilOk returns a tuple with the HorizontalRecoil field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHorizontalRecoil

`func (o *WeaponInfoV2) SetHorizontalRecoil(v RawWeaponInfoHorizontalRecoilV2)`

SetHorizontalRecoil sets HorizontalRecoil field to given value.

### HasHorizontalRecoil

`func (o *WeaponInfoV2) HasHorizontalRecoil() bool`

HasHorizontalRecoil returns a boolean if a field has been set.

### SetHorizontalRecoilNil

`func (o *WeaponInfoV2) SetHorizontalRecoilNil(b bool)`

 SetHorizontalRecoilNil sets the value for HorizontalRecoil to be an explicit nil

### UnsetHorizontalRecoil
`func (o *WeaponInfoV2) UnsetHorizontalRecoil()`

UnsetHorizontalRecoil ensures that no value is present for HorizontalRecoil, not even an explicit nil
### GetVerticalRecoil

`func (o *WeaponInfoV2) GetVerticalRecoil() RawWeaponInfoVerticalRecoilV2`

GetVerticalRecoil returns the VerticalRecoil field if non-nil, zero value otherwise.

### GetVerticalRecoilOk

`func (o *WeaponInfoV2) GetVerticalRecoilOk() (*RawWeaponInfoVerticalRecoilV2, bool)`

GetVerticalRecoilOk returns a tuple with the VerticalRecoil field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerticalRecoil

`func (o *WeaponInfoV2) SetVerticalRecoil(v RawWeaponInfoVerticalRecoilV2)`

SetVerticalRecoil sets VerticalRecoil field to given value.

### HasVerticalRecoil

`func (o *WeaponInfoV2) HasVerticalRecoil() bool`

HasVerticalRecoil returns a boolean if a field has been set.

### SetVerticalRecoilNil

`func (o *WeaponInfoV2) SetVerticalRecoilNil(b bool)`

 SetVerticalRecoilNil sets the value for VerticalRecoil to be an explicit nil

### UnsetVerticalRecoil
`func (o *WeaponInfoV2) UnsetVerticalRecoil()`

UnsetVerticalRecoil ensures that no value is present for VerticalRecoil, not even an explicit nil
### GetShotsPerSecond

`func (o *WeaponInfoV2) GetShotsPerSecond() float32`

GetShotsPerSecond returns the ShotsPerSecond field if non-nil, zero value otherwise.

### GetShotsPerSecondOk

`func (o *WeaponInfoV2) GetShotsPerSecondOk() (*float32, bool)`

GetShotsPerSecondOk returns a tuple with the ShotsPerSecond field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShotsPerSecond

`func (o *WeaponInfoV2) SetShotsPerSecond(v float32)`

SetShotsPerSecond sets ShotsPerSecond field to given value.


### SetShotsPerSecondNil

`func (o *WeaponInfoV2) SetShotsPerSecondNil(b bool)`

 SetShotsPerSecondNil sets the value for ShotsPerSecond to be an explicit nil

### UnsetShotsPerSecond
`func (o *WeaponInfoV2) UnsetShotsPerSecond()`

UnsetShotsPerSecond ensures that no value is present for ShotsPerSecond, not even an explicit nil
### GetBulletsPerSecond

`func (o *WeaponInfoV2) GetBulletsPerSecond() float32`

GetBulletsPerSecond returns the BulletsPerSecond field if non-nil, zero value otherwise.

### GetBulletsPerSecondOk

`func (o *WeaponInfoV2) GetBulletsPerSecondOk() (*float32, bool)`

GetBulletsPerSecondOk returns a tuple with the BulletsPerSecond field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletsPerSecond

`func (o *WeaponInfoV2) SetBulletsPerSecond(v float32)`

SetBulletsPerSecond sets BulletsPerSecond field to given value.


### SetBulletsPerSecondNil

`func (o *WeaponInfoV2) SetBulletsPerSecondNil(b bool)`

 SetBulletsPerSecondNil sets the value for BulletsPerSecond to be an explicit nil

### UnsetBulletsPerSecond
`func (o *WeaponInfoV2) UnsetBulletsPerSecond()`

UnsetBulletsPerSecond ensures that no value is present for BulletsPerSecond, not even an explicit nil
### GetDamagePerSecond

`func (o *WeaponInfoV2) GetDamagePerSecond() float32`

GetDamagePerSecond returns the DamagePerSecond field if non-nil, zero value otherwise.

### GetDamagePerSecondOk

`func (o *WeaponInfoV2) GetDamagePerSecondOk() (*float32, bool)`

GetDamagePerSecondOk returns a tuple with the DamagePerSecond field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamagePerSecond

`func (o *WeaponInfoV2) SetDamagePerSecond(v float32)`

SetDamagePerSecond sets DamagePerSecond field to given value.


### SetDamagePerSecondNil

`func (o *WeaponInfoV2) SetDamagePerSecondNil(b bool)`

 SetDamagePerSecondNil sets the value for DamagePerSecond to be an explicit nil

### UnsetDamagePerSecond
`func (o *WeaponInfoV2) UnsetDamagePerSecond()`

UnsetDamagePerSecond ensures that no value is present for DamagePerSecond, not even an explicit nil
### GetDamagePerShot

`func (o *WeaponInfoV2) GetDamagePerShot() float32`

GetDamagePerShot returns the DamagePerShot field if non-nil, zero value otherwise.

### GetDamagePerShotOk

`func (o *WeaponInfoV2) GetDamagePerShotOk() (*float32, bool)`

GetDamagePerShotOk returns a tuple with the DamagePerShot field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamagePerShot

`func (o *WeaponInfoV2) SetDamagePerShot(v float32)`

SetDamagePerShot sets DamagePerShot field to given value.


### SetDamagePerShotNil

`func (o *WeaponInfoV2) SetDamagePerShotNil(b bool)`

 SetDamagePerShotNil sets the value for DamagePerShot to be an explicit nil

### UnsetDamagePerShot
`func (o *WeaponInfoV2) UnsetDamagePerShot()`

UnsetDamagePerShot ensures that no value is present for DamagePerShot, not even an explicit nil
### GetDamagePerMagazine

`func (o *WeaponInfoV2) GetDamagePerMagazine() float32`

GetDamagePerMagazine returns the DamagePerMagazine field if non-nil, zero value otherwise.

### GetDamagePerMagazineOk

`func (o *WeaponInfoV2) GetDamagePerMagazineOk() (*float32, bool)`

GetDamagePerMagazineOk returns a tuple with the DamagePerMagazine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamagePerMagazine

`func (o *WeaponInfoV2) SetDamagePerMagazine(v float32)`

SetDamagePerMagazine sets DamagePerMagazine field to given value.


### SetDamagePerMagazineNil

`func (o *WeaponInfoV2) SetDamagePerMagazineNil(b bool)`

 SetDamagePerMagazineNil sets the value for DamagePerMagazine to be an explicit nil

### UnsetDamagePerMagazine
`func (o *WeaponInfoV2) UnsetDamagePerMagazine()`

UnsetDamagePerMagazine ensures that no value is present for DamagePerMagazine, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


