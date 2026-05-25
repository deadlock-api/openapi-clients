# Accolade

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClassName** | **string** |  | 
**Description** | **string** |  | 
**EnabledGameModes** | Pointer to **[]string** |  | [optional] 
**FlavorName** | **string** |  | 
**Id** | **int32** |  | 
**ThresholdType** | **string** |  | 
**TrackedStatName** | **string** |  | 

## Methods

### NewAccolade

`func NewAccolade(className string, description string, flavorName string, id int32, thresholdType string, trackedStatName string, ) *Accolade`

NewAccolade instantiates a new Accolade object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAccoladeWithDefaults

`func NewAccoladeWithDefaults() *Accolade`

NewAccoladeWithDefaults instantiates a new Accolade object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClassName

`func (o *Accolade) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *Accolade) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *Accolade) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetDescription

`func (o *Accolade) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Accolade) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Accolade) SetDescription(v string)`

SetDescription sets Description field to given value.


### GetEnabledGameModes

`func (o *Accolade) GetEnabledGameModes() []string`

GetEnabledGameModes returns the EnabledGameModes field if non-nil, zero value otherwise.

### GetEnabledGameModesOk

`func (o *Accolade) GetEnabledGameModesOk() (*[]string, bool)`

GetEnabledGameModesOk returns a tuple with the EnabledGameModes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabledGameModes

`func (o *Accolade) SetEnabledGameModes(v []string)`

SetEnabledGameModes sets EnabledGameModes field to given value.

### HasEnabledGameModes

`func (o *Accolade) HasEnabledGameModes() bool`

HasEnabledGameModes returns a boolean if a field has been set.

### SetEnabledGameModesNil

`func (o *Accolade) SetEnabledGameModesNil(b bool)`

 SetEnabledGameModesNil sets the value for EnabledGameModes to be an explicit nil

### UnsetEnabledGameModes
`func (o *Accolade) UnsetEnabledGameModes()`

UnsetEnabledGameModes ensures that no value is present for EnabledGameModes, not even an explicit nil
### GetFlavorName

`func (o *Accolade) GetFlavorName() string`

GetFlavorName returns the FlavorName field if non-nil, zero value otherwise.

### GetFlavorNameOk

`func (o *Accolade) GetFlavorNameOk() (*string, bool)`

GetFlavorNameOk returns a tuple with the FlavorName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlavorName

`func (o *Accolade) SetFlavorName(v string)`

SetFlavorName sets FlavorName field to given value.


### GetId

`func (o *Accolade) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Accolade) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Accolade) SetId(v int32)`

SetId sets Id field to given value.


### GetThresholdType

`func (o *Accolade) GetThresholdType() string`

GetThresholdType returns the ThresholdType field if non-nil, zero value otherwise.

### GetThresholdTypeOk

`func (o *Accolade) GetThresholdTypeOk() (*string, bool)`

GetThresholdTypeOk returns a tuple with the ThresholdType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThresholdType

`func (o *Accolade) SetThresholdType(v string)`

SetThresholdType sets ThresholdType field to given value.


### GetTrackedStatName

`func (o *Accolade) GetTrackedStatName() string`

GetTrackedStatName returns the TrackedStatName field if non-nil, zero value otherwise.

### GetTrackedStatNameOk

`func (o *Accolade) GetTrackedStatNameOk() (*string, bool)`

GetTrackedStatNameOk returns a tuple with the TrackedStatName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackedStatName

`func (o *Accolade) SetTrackedStatName(v string)`

SetTrackedStatName sets TrackedStatName field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


