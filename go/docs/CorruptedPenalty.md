# CorruptedPenalty

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Effects** | [**[]CorruptedPenaltyEffect**](CorruptedPenaltyEffect.md) |  | 
**Name** | **string** |  | 
**RollWeight** | Pointer to **NullableFloat64** |  | [optional] 

## Methods

### NewCorruptedPenalty

`func NewCorruptedPenalty(effects []CorruptedPenaltyEffect, name string, ) *CorruptedPenalty`

NewCorruptedPenalty instantiates a new CorruptedPenalty object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCorruptedPenaltyWithDefaults

`func NewCorruptedPenaltyWithDefaults() *CorruptedPenalty`

NewCorruptedPenaltyWithDefaults instantiates a new CorruptedPenalty object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEffects

`func (o *CorruptedPenalty) GetEffects() []CorruptedPenaltyEffect`

GetEffects returns the Effects field if non-nil, zero value otherwise.

### GetEffectsOk

`func (o *CorruptedPenalty) GetEffectsOk() (*[]CorruptedPenaltyEffect, bool)`

GetEffectsOk returns a tuple with the Effects field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEffects

`func (o *CorruptedPenalty) SetEffects(v []CorruptedPenaltyEffect)`

SetEffects sets Effects field to given value.


### GetName

`func (o *CorruptedPenalty) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CorruptedPenalty) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CorruptedPenalty) SetName(v string)`

SetName sets Name field to given value.


### GetRollWeight

`func (o *CorruptedPenalty) GetRollWeight() float64`

GetRollWeight returns the RollWeight field if non-nil, zero value otherwise.

### GetRollWeightOk

`func (o *CorruptedPenalty) GetRollWeightOk() (*float64, bool)`

GetRollWeightOk returns a tuple with the RollWeight field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRollWeight

`func (o *CorruptedPenalty) SetRollWeight(v float64)`

SetRollWeight sets RollWeight field to given value.

### HasRollWeight

`func (o *CorruptedPenalty) HasRollWeight() bool`

HasRollWeight returns a boolean if a field has been set.

### SetRollWeightNil

`func (o *CorruptedPenalty) SetRollWeightNil(b bool)`

 SetRollWeightNil sets the value for RollWeight to be an explicit nil

### UnsetRollWeight
`func (o *CorruptedPenalty) UnsetRollWeight()`

UnsetRollWeight ensures that no value is present for RollWeight, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


