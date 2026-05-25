# HeroPhysics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CollisionHeight** | Pointer to **NullableFloat64** |  | [optional] 
**CollisionRadius** | Pointer to **NullableFloat64** |  | [optional] 
**FootstepSoundTravelDistanceMeters** | Pointer to **NullableFloat64** |  | [optional] 
**StealthSpeedMetersPerSecond** | **float64** |  | 
**StepHeight** | Pointer to **NullableFloat64** |  | [optional] 
**StepSoundTime** | Pointer to **NullableFloat64** |  | [optional] 
**StepSoundTimeSprinting** | Pointer to **NullableFloat64** |  | [optional] 

## Methods

### NewHeroPhysics

`func NewHeroPhysics(stealthSpeedMetersPerSecond float64, ) *HeroPhysics`

NewHeroPhysics instantiates a new HeroPhysics object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHeroPhysicsWithDefaults

`func NewHeroPhysicsWithDefaults() *HeroPhysics`

NewHeroPhysicsWithDefaults instantiates a new HeroPhysics object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCollisionHeight

`func (o *HeroPhysics) GetCollisionHeight() float64`

GetCollisionHeight returns the CollisionHeight field if non-nil, zero value otherwise.

### GetCollisionHeightOk

`func (o *HeroPhysics) GetCollisionHeightOk() (*float64, bool)`

GetCollisionHeightOk returns a tuple with the CollisionHeight field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCollisionHeight

`func (o *HeroPhysics) SetCollisionHeight(v float64)`

SetCollisionHeight sets CollisionHeight field to given value.

### HasCollisionHeight

`func (o *HeroPhysics) HasCollisionHeight() bool`

HasCollisionHeight returns a boolean if a field has been set.

### SetCollisionHeightNil

`func (o *HeroPhysics) SetCollisionHeightNil(b bool)`

 SetCollisionHeightNil sets the value for CollisionHeight to be an explicit nil

### UnsetCollisionHeight
`func (o *HeroPhysics) UnsetCollisionHeight()`

UnsetCollisionHeight ensures that no value is present for CollisionHeight, not even an explicit nil
### GetCollisionRadius

`func (o *HeroPhysics) GetCollisionRadius() float64`

GetCollisionRadius returns the CollisionRadius field if non-nil, zero value otherwise.

### GetCollisionRadiusOk

`func (o *HeroPhysics) GetCollisionRadiusOk() (*float64, bool)`

GetCollisionRadiusOk returns a tuple with the CollisionRadius field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCollisionRadius

`func (o *HeroPhysics) SetCollisionRadius(v float64)`

SetCollisionRadius sets CollisionRadius field to given value.

### HasCollisionRadius

`func (o *HeroPhysics) HasCollisionRadius() bool`

HasCollisionRadius returns a boolean if a field has been set.

### SetCollisionRadiusNil

`func (o *HeroPhysics) SetCollisionRadiusNil(b bool)`

 SetCollisionRadiusNil sets the value for CollisionRadius to be an explicit nil

### UnsetCollisionRadius
`func (o *HeroPhysics) UnsetCollisionRadius()`

UnsetCollisionRadius ensures that no value is present for CollisionRadius, not even an explicit nil
### GetFootstepSoundTravelDistanceMeters

`func (o *HeroPhysics) GetFootstepSoundTravelDistanceMeters() float64`

GetFootstepSoundTravelDistanceMeters returns the FootstepSoundTravelDistanceMeters field if non-nil, zero value otherwise.

### GetFootstepSoundTravelDistanceMetersOk

`func (o *HeroPhysics) GetFootstepSoundTravelDistanceMetersOk() (*float64, bool)`

GetFootstepSoundTravelDistanceMetersOk returns a tuple with the FootstepSoundTravelDistanceMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFootstepSoundTravelDistanceMeters

`func (o *HeroPhysics) SetFootstepSoundTravelDistanceMeters(v float64)`

SetFootstepSoundTravelDistanceMeters sets FootstepSoundTravelDistanceMeters field to given value.

### HasFootstepSoundTravelDistanceMeters

`func (o *HeroPhysics) HasFootstepSoundTravelDistanceMeters() bool`

HasFootstepSoundTravelDistanceMeters returns a boolean if a field has been set.

### SetFootstepSoundTravelDistanceMetersNil

`func (o *HeroPhysics) SetFootstepSoundTravelDistanceMetersNil(b bool)`

 SetFootstepSoundTravelDistanceMetersNil sets the value for FootstepSoundTravelDistanceMeters to be an explicit nil

### UnsetFootstepSoundTravelDistanceMeters
`func (o *HeroPhysics) UnsetFootstepSoundTravelDistanceMeters()`

UnsetFootstepSoundTravelDistanceMeters ensures that no value is present for FootstepSoundTravelDistanceMeters, not even an explicit nil
### GetStealthSpeedMetersPerSecond

`func (o *HeroPhysics) GetStealthSpeedMetersPerSecond() float64`

GetStealthSpeedMetersPerSecond returns the StealthSpeedMetersPerSecond field if non-nil, zero value otherwise.

### GetStealthSpeedMetersPerSecondOk

`func (o *HeroPhysics) GetStealthSpeedMetersPerSecondOk() (*float64, bool)`

GetStealthSpeedMetersPerSecondOk returns a tuple with the StealthSpeedMetersPerSecond field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStealthSpeedMetersPerSecond

`func (o *HeroPhysics) SetStealthSpeedMetersPerSecond(v float64)`

SetStealthSpeedMetersPerSecond sets StealthSpeedMetersPerSecond field to given value.


### GetStepHeight

`func (o *HeroPhysics) GetStepHeight() float64`

GetStepHeight returns the StepHeight field if non-nil, zero value otherwise.

### GetStepHeightOk

`func (o *HeroPhysics) GetStepHeightOk() (*float64, bool)`

GetStepHeightOk returns a tuple with the StepHeight field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepHeight

`func (o *HeroPhysics) SetStepHeight(v float64)`

SetStepHeight sets StepHeight field to given value.

### HasStepHeight

`func (o *HeroPhysics) HasStepHeight() bool`

HasStepHeight returns a boolean if a field has been set.

### SetStepHeightNil

`func (o *HeroPhysics) SetStepHeightNil(b bool)`

 SetStepHeightNil sets the value for StepHeight to be an explicit nil

### UnsetStepHeight
`func (o *HeroPhysics) UnsetStepHeight()`

UnsetStepHeight ensures that no value is present for StepHeight, not even an explicit nil
### GetStepSoundTime

`func (o *HeroPhysics) GetStepSoundTime() float64`

GetStepSoundTime returns the StepSoundTime field if non-nil, zero value otherwise.

### GetStepSoundTimeOk

`func (o *HeroPhysics) GetStepSoundTimeOk() (*float64, bool)`

GetStepSoundTimeOk returns a tuple with the StepSoundTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepSoundTime

`func (o *HeroPhysics) SetStepSoundTime(v float64)`

SetStepSoundTime sets StepSoundTime field to given value.

### HasStepSoundTime

`func (o *HeroPhysics) HasStepSoundTime() bool`

HasStepSoundTime returns a boolean if a field has been set.

### SetStepSoundTimeNil

`func (o *HeroPhysics) SetStepSoundTimeNil(b bool)`

 SetStepSoundTimeNil sets the value for StepSoundTime to be an explicit nil

### UnsetStepSoundTime
`func (o *HeroPhysics) UnsetStepSoundTime()`

UnsetStepSoundTime ensures that no value is present for StepSoundTime, not even an explicit nil
### GetStepSoundTimeSprinting

`func (o *HeroPhysics) GetStepSoundTimeSprinting() float64`

GetStepSoundTimeSprinting returns the StepSoundTimeSprinting field if non-nil, zero value otherwise.

### GetStepSoundTimeSprintingOk

`func (o *HeroPhysics) GetStepSoundTimeSprintingOk() (*float64, bool)`

GetStepSoundTimeSprintingOk returns a tuple with the StepSoundTimeSprinting field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepSoundTimeSprinting

`func (o *HeroPhysics) SetStepSoundTimeSprinting(v float64)`

SetStepSoundTimeSprinting sets StepSoundTimeSprinting field to given value.

### HasStepSoundTimeSprinting

`func (o *HeroPhysics) HasStepSoundTimeSprinting() bool`

HasStepSoundTimeSprinting returns a boolean if a field has been set.

### SetStepSoundTimeSprintingNil

`func (o *HeroPhysics) SetStepSoundTimeSprintingNil(b bool)`

 SetStepSoundTimeSprintingNil sets the value for StepSoundTimeSprinting to be an explicit nil

### UnsetStepSoundTimeSprinting
`func (o *HeroPhysics) UnsetStepSoundTimeSprinting()`

UnsetStepSoundTimeSprinting ensures that no value is present for StepSoundTimeSprinting, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


