# AccoladeV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClassName** | **string** |  | 
**Id** | **int32** |  | 
**TrackedStatName** | [**TrackedStatName**](TrackedStatName.md) |  | 
**FlavorName** | **string** |  | 
**Description** | **string** |  | 
**ThresholdType** | [**ThresholdType**](ThresholdType.md) |  | 
**EnabledGameModes** | Pointer to [**[]GameMode**](GameMode.md) |  | [optional] 

## Methods

### NewAccoladeV2

`func NewAccoladeV2(className string, id int32, trackedStatName TrackedStatName, flavorName string, description string, thresholdType ThresholdType, ) *AccoladeV2`

NewAccoladeV2 instantiates a new AccoladeV2 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAccoladeV2WithDefaults

`func NewAccoladeV2WithDefaults() *AccoladeV2`

NewAccoladeV2WithDefaults instantiates a new AccoladeV2 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClassName

`func (o *AccoladeV2) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *AccoladeV2) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *AccoladeV2) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetId

`func (o *AccoladeV2) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *AccoladeV2) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *AccoladeV2) SetId(v int32)`

SetId sets Id field to given value.


### GetTrackedStatName

`func (o *AccoladeV2) GetTrackedStatName() TrackedStatName`

GetTrackedStatName returns the TrackedStatName field if non-nil, zero value otherwise.

### GetTrackedStatNameOk

`func (o *AccoladeV2) GetTrackedStatNameOk() (*TrackedStatName, bool)`

GetTrackedStatNameOk returns a tuple with the TrackedStatName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackedStatName

`func (o *AccoladeV2) SetTrackedStatName(v TrackedStatName)`

SetTrackedStatName sets TrackedStatName field to given value.


### GetFlavorName

`func (o *AccoladeV2) GetFlavorName() string`

GetFlavorName returns the FlavorName field if non-nil, zero value otherwise.

### GetFlavorNameOk

`func (o *AccoladeV2) GetFlavorNameOk() (*string, bool)`

GetFlavorNameOk returns a tuple with the FlavorName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlavorName

`func (o *AccoladeV2) SetFlavorName(v string)`

SetFlavorName sets FlavorName field to given value.


### GetDescription

`func (o *AccoladeV2) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *AccoladeV2) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *AccoladeV2) SetDescription(v string)`

SetDescription sets Description field to given value.


### GetThresholdType

`func (o *AccoladeV2) GetThresholdType() ThresholdType`

GetThresholdType returns the ThresholdType field if non-nil, zero value otherwise.

### GetThresholdTypeOk

`func (o *AccoladeV2) GetThresholdTypeOk() (*ThresholdType, bool)`

GetThresholdTypeOk returns a tuple with the ThresholdType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThresholdType

`func (o *AccoladeV2) SetThresholdType(v ThresholdType)`

SetThresholdType sets ThresholdType field to given value.


### GetEnabledGameModes

`func (o *AccoladeV2) GetEnabledGameModes() []GameMode`

GetEnabledGameModes returns the EnabledGameModes field if non-nil, zero value otherwise.

### GetEnabledGameModesOk

`func (o *AccoladeV2) GetEnabledGameModesOk() (*[]GameMode, bool)`

GetEnabledGameModesOk returns a tuple with the EnabledGameModes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabledGameModes

`func (o *AccoladeV2) SetEnabledGameModes(v []GameMode)`

SetEnabledGameModes sets EnabledGameModes field to given value.

### HasEnabledGameModes

`func (o *AccoladeV2) HasEnabledGameModes() bool`

HasEnabledGameModes returns a boolean if a field has been set.

### SetEnabledGameModesNil

`func (o *AccoladeV2) SetEnabledGameModesNil(b bool)`

 SetEnabledGameModesNil sets the value for EnabledGameModes to be an explicit nil

### UnsetEnabledGameModes
`func (o *AccoladeV2) UnsetEnabledGameModes()`

UnsetEnabledGameModes ensures that no value is present for EnabledGameModes, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


