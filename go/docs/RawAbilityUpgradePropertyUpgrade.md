# RawAbilityUpgradePropertyUpgrade

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Bonus** | **string** |  | 
**FixedCorruptedBonus** | Pointer to **NullableBool** | Corrupted item bonuses only (build 6711+). | [optional] 
**Name** | **string** |  | 
**RoundCorruptedBonus** | Pointer to **NullableBool** | Corrupted item bonuses only (build 6711+). | [optional] 
**ScaleStatFilter** | Pointer to **NullableString** |  | [optional] 
**UpgradeType** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewRawAbilityUpgradePropertyUpgrade

`func NewRawAbilityUpgradePropertyUpgrade(bonus string, name string, ) *RawAbilityUpgradePropertyUpgrade`

NewRawAbilityUpgradePropertyUpgrade instantiates a new RawAbilityUpgradePropertyUpgrade object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRawAbilityUpgradePropertyUpgradeWithDefaults

`func NewRawAbilityUpgradePropertyUpgradeWithDefaults() *RawAbilityUpgradePropertyUpgrade`

NewRawAbilityUpgradePropertyUpgradeWithDefaults instantiates a new RawAbilityUpgradePropertyUpgrade object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBonus

`func (o *RawAbilityUpgradePropertyUpgrade) GetBonus() string`

GetBonus returns the Bonus field if non-nil, zero value otherwise.

### GetBonusOk

`func (o *RawAbilityUpgradePropertyUpgrade) GetBonusOk() (*string, bool)`

GetBonusOk returns a tuple with the Bonus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBonus

`func (o *RawAbilityUpgradePropertyUpgrade) SetBonus(v string)`

SetBonus sets Bonus field to given value.


### GetFixedCorruptedBonus

`func (o *RawAbilityUpgradePropertyUpgrade) GetFixedCorruptedBonus() bool`

GetFixedCorruptedBonus returns the FixedCorruptedBonus field if non-nil, zero value otherwise.

### GetFixedCorruptedBonusOk

`func (o *RawAbilityUpgradePropertyUpgrade) GetFixedCorruptedBonusOk() (*bool, bool)`

GetFixedCorruptedBonusOk returns a tuple with the FixedCorruptedBonus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFixedCorruptedBonus

`func (o *RawAbilityUpgradePropertyUpgrade) SetFixedCorruptedBonus(v bool)`

SetFixedCorruptedBonus sets FixedCorruptedBonus field to given value.

### HasFixedCorruptedBonus

`func (o *RawAbilityUpgradePropertyUpgrade) HasFixedCorruptedBonus() bool`

HasFixedCorruptedBonus returns a boolean if a field has been set.

### SetFixedCorruptedBonusNil

`func (o *RawAbilityUpgradePropertyUpgrade) SetFixedCorruptedBonusNil(b bool)`

 SetFixedCorruptedBonusNil sets the value for FixedCorruptedBonus to be an explicit nil

### UnsetFixedCorruptedBonus
`func (o *RawAbilityUpgradePropertyUpgrade) UnsetFixedCorruptedBonus()`

UnsetFixedCorruptedBonus ensures that no value is present for FixedCorruptedBonus, not even an explicit nil
### GetName

`func (o *RawAbilityUpgradePropertyUpgrade) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *RawAbilityUpgradePropertyUpgrade) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *RawAbilityUpgradePropertyUpgrade) SetName(v string)`

SetName sets Name field to given value.


### GetRoundCorruptedBonus

`func (o *RawAbilityUpgradePropertyUpgrade) GetRoundCorruptedBonus() bool`

GetRoundCorruptedBonus returns the RoundCorruptedBonus field if non-nil, zero value otherwise.

### GetRoundCorruptedBonusOk

`func (o *RawAbilityUpgradePropertyUpgrade) GetRoundCorruptedBonusOk() (*bool, bool)`

GetRoundCorruptedBonusOk returns a tuple with the RoundCorruptedBonus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRoundCorruptedBonus

`func (o *RawAbilityUpgradePropertyUpgrade) SetRoundCorruptedBonus(v bool)`

SetRoundCorruptedBonus sets RoundCorruptedBonus field to given value.

### HasRoundCorruptedBonus

`func (o *RawAbilityUpgradePropertyUpgrade) HasRoundCorruptedBonus() bool`

HasRoundCorruptedBonus returns a boolean if a field has been set.

### SetRoundCorruptedBonusNil

`func (o *RawAbilityUpgradePropertyUpgrade) SetRoundCorruptedBonusNil(b bool)`

 SetRoundCorruptedBonusNil sets the value for RoundCorruptedBonus to be an explicit nil

### UnsetRoundCorruptedBonus
`func (o *RawAbilityUpgradePropertyUpgrade) UnsetRoundCorruptedBonus()`

UnsetRoundCorruptedBonus ensures that no value is present for RoundCorruptedBonus, not even an explicit nil
### GetScaleStatFilter

`func (o *RawAbilityUpgradePropertyUpgrade) GetScaleStatFilter() string`

GetScaleStatFilter returns the ScaleStatFilter field if non-nil, zero value otherwise.

### GetScaleStatFilterOk

`func (o *RawAbilityUpgradePropertyUpgrade) GetScaleStatFilterOk() (*string, bool)`

GetScaleStatFilterOk returns a tuple with the ScaleStatFilter field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScaleStatFilter

`func (o *RawAbilityUpgradePropertyUpgrade) SetScaleStatFilter(v string)`

SetScaleStatFilter sets ScaleStatFilter field to given value.

### HasScaleStatFilter

`func (o *RawAbilityUpgradePropertyUpgrade) HasScaleStatFilter() bool`

HasScaleStatFilter returns a boolean if a field has been set.

### SetScaleStatFilterNil

`func (o *RawAbilityUpgradePropertyUpgrade) SetScaleStatFilterNil(b bool)`

 SetScaleStatFilterNil sets the value for ScaleStatFilter to be an explicit nil

### UnsetScaleStatFilter
`func (o *RawAbilityUpgradePropertyUpgrade) UnsetScaleStatFilter()`

UnsetScaleStatFilter ensures that no value is present for ScaleStatFilter, not even an explicit nil
### GetUpgradeType

`func (o *RawAbilityUpgradePropertyUpgrade) GetUpgradeType() string`

GetUpgradeType returns the UpgradeType field if non-nil, zero value otherwise.

### GetUpgradeTypeOk

`func (o *RawAbilityUpgradePropertyUpgrade) GetUpgradeTypeOk() (*string, bool)`

GetUpgradeTypeOk returns a tuple with the UpgradeType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpgradeType

`func (o *RawAbilityUpgradePropertyUpgrade) SetUpgradeType(v string)`

SetUpgradeType sets UpgradeType field to given value.

### HasUpgradeType

`func (o *RawAbilityUpgradePropertyUpgrade) HasUpgradeType() bool`

HasUpgradeType returns a boolean if a field has been set.

### SetUpgradeTypeNil

`func (o *RawAbilityUpgradePropertyUpgrade) SetUpgradeTypeNil(b bool)`

 SetUpgradeTypeNil sets the value for UpgradeType to be an explicit nil

### UnsetUpgradeType
`func (o *RawAbilityUpgradePropertyUpgrade) UnsetUpgradeType()`

UnsetUpgradeType ensures that no value is present for UpgradeType, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


