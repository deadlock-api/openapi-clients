# CreateCustomRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CallbackUrl** | Pointer to **NullableString** | If a callback url is provided, we will send a POST request to this url when the match starts. | [optional] 
**CheatsEnabled** | Pointer to **NullableBool** |  | [optional] 
**DisableAutoReady** | Pointer to **NullableBool** | If auto-ready is disabled, the bot will not automatically ready up. You need to call the &#x60;ready&#x60; endpoint to ready up. | [optional] 
**DuplicateHeroesEnabled** | Pointer to **NullableBool** |  | [optional] 
**ExperimentalHeroesEnabled** | Pointer to **NullableBool** |  | [optional] 
**IsPubliclyVisible** | Pointer to **NullableBool** |  | [optional] 
**MinRosterSize** | Pointer to **NullableInt32** |  | [optional] 
**RandomizeLanes** | Pointer to **NullableBool** |  | [optional] 
**RegionMode** | Pointer to [**NullableRegionMode**](RegionMode.md) |  | [optional] 

## Methods

### NewCreateCustomRequest

`func NewCreateCustomRequest() *CreateCustomRequest`

NewCreateCustomRequest instantiates a new CreateCustomRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateCustomRequestWithDefaults

`func NewCreateCustomRequestWithDefaults() *CreateCustomRequest`

NewCreateCustomRequestWithDefaults instantiates a new CreateCustomRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCallbackUrl

`func (o *CreateCustomRequest) GetCallbackUrl() string`

GetCallbackUrl returns the CallbackUrl field if non-nil, zero value otherwise.

### GetCallbackUrlOk

`func (o *CreateCustomRequest) GetCallbackUrlOk() (*string, bool)`

GetCallbackUrlOk returns a tuple with the CallbackUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCallbackUrl

`func (o *CreateCustomRequest) SetCallbackUrl(v string)`

SetCallbackUrl sets CallbackUrl field to given value.

### HasCallbackUrl

`func (o *CreateCustomRequest) HasCallbackUrl() bool`

HasCallbackUrl returns a boolean if a field has been set.

### SetCallbackUrlNil

`func (o *CreateCustomRequest) SetCallbackUrlNil(b bool)`

 SetCallbackUrlNil sets the value for CallbackUrl to be an explicit nil

### UnsetCallbackUrl
`func (o *CreateCustomRequest) UnsetCallbackUrl()`

UnsetCallbackUrl ensures that no value is present for CallbackUrl, not even an explicit nil
### GetCheatsEnabled

`func (o *CreateCustomRequest) GetCheatsEnabled() bool`

GetCheatsEnabled returns the CheatsEnabled field if non-nil, zero value otherwise.

### GetCheatsEnabledOk

`func (o *CreateCustomRequest) GetCheatsEnabledOk() (*bool, bool)`

GetCheatsEnabledOk returns a tuple with the CheatsEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCheatsEnabled

`func (o *CreateCustomRequest) SetCheatsEnabled(v bool)`

SetCheatsEnabled sets CheatsEnabled field to given value.

### HasCheatsEnabled

`func (o *CreateCustomRequest) HasCheatsEnabled() bool`

HasCheatsEnabled returns a boolean if a field has been set.

### SetCheatsEnabledNil

`func (o *CreateCustomRequest) SetCheatsEnabledNil(b bool)`

 SetCheatsEnabledNil sets the value for CheatsEnabled to be an explicit nil

### UnsetCheatsEnabled
`func (o *CreateCustomRequest) UnsetCheatsEnabled()`

UnsetCheatsEnabled ensures that no value is present for CheatsEnabled, not even an explicit nil
### GetDisableAutoReady

`func (o *CreateCustomRequest) GetDisableAutoReady() bool`

GetDisableAutoReady returns the DisableAutoReady field if non-nil, zero value otherwise.

### GetDisableAutoReadyOk

`func (o *CreateCustomRequest) GetDisableAutoReadyOk() (*bool, bool)`

GetDisableAutoReadyOk returns a tuple with the DisableAutoReady field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisableAutoReady

`func (o *CreateCustomRequest) SetDisableAutoReady(v bool)`

SetDisableAutoReady sets DisableAutoReady field to given value.

### HasDisableAutoReady

`func (o *CreateCustomRequest) HasDisableAutoReady() bool`

HasDisableAutoReady returns a boolean if a field has been set.

### SetDisableAutoReadyNil

`func (o *CreateCustomRequest) SetDisableAutoReadyNil(b bool)`

 SetDisableAutoReadyNil sets the value for DisableAutoReady to be an explicit nil

### UnsetDisableAutoReady
`func (o *CreateCustomRequest) UnsetDisableAutoReady()`

UnsetDisableAutoReady ensures that no value is present for DisableAutoReady, not even an explicit nil
### GetDuplicateHeroesEnabled

`func (o *CreateCustomRequest) GetDuplicateHeroesEnabled() bool`

GetDuplicateHeroesEnabled returns the DuplicateHeroesEnabled field if non-nil, zero value otherwise.

### GetDuplicateHeroesEnabledOk

`func (o *CreateCustomRequest) GetDuplicateHeroesEnabledOk() (*bool, bool)`

GetDuplicateHeroesEnabledOk returns a tuple with the DuplicateHeroesEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDuplicateHeroesEnabled

`func (o *CreateCustomRequest) SetDuplicateHeroesEnabled(v bool)`

SetDuplicateHeroesEnabled sets DuplicateHeroesEnabled field to given value.

### HasDuplicateHeroesEnabled

`func (o *CreateCustomRequest) HasDuplicateHeroesEnabled() bool`

HasDuplicateHeroesEnabled returns a boolean if a field has been set.

### SetDuplicateHeroesEnabledNil

`func (o *CreateCustomRequest) SetDuplicateHeroesEnabledNil(b bool)`

 SetDuplicateHeroesEnabledNil sets the value for DuplicateHeroesEnabled to be an explicit nil

### UnsetDuplicateHeroesEnabled
`func (o *CreateCustomRequest) UnsetDuplicateHeroesEnabled()`

UnsetDuplicateHeroesEnabled ensures that no value is present for DuplicateHeroesEnabled, not even an explicit nil
### GetExperimentalHeroesEnabled

`func (o *CreateCustomRequest) GetExperimentalHeroesEnabled() bool`

GetExperimentalHeroesEnabled returns the ExperimentalHeroesEnabled field if non-nil, zero value otherwise.

### GetExperimentalHeroesEnabledOk

`func (o *CreateCustomRequest) GetExperimentalHeroesEnabledOk() (*bool, bool)`

GetExperimentalHeroesEnabledOk returns a tuple with the ExperimentalHeroesEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExperimentalHeroesEnabled

`func (o *CreateCustomRequest) SetExperimentalHeroesEnabled(v bool)`

SetExperimentalHeroesEnabled sets ExperimentalHeroesEnabled field to given value.

### HasExperimentalHeroesEnabled

`func (o *CreateCustomRequest) HasExperimentalHeroesEnabled() bool`

HasExperimentalHeroesEnabled returns a boolean if a field has been set.

### SetExperimentalHeroesEnabledNil

`func (o *CreateCustomRequest) SetExperimentalHeroesEnabledNil(b bool)`

 SetExperimentalHeroesEnabledNil sets the value for ExperimentalHeroesEnabled to be an explicit nil

### UnsetExperimentalHeroesEnabled
`func (o *CreateCustomRequest) UnsetExperimentalHeroesEnabled()`

UnsetExperimentalHeroesEnabled ensures that no value is present for ExperimentalHeroesEnabled, not even an explicit nil
### GetIsPubliclyVisible

`func (o *CreateCustomRequest) GetIsPubliclyVisible() bool`

GetIsPubliclyVisible returns the IsPubliclyVisible field if non-nil, zero value otherwise.

### GetIsPubliclyVisibleOk

`func (o *CreateCustomRequest) GetIsPubliclyVisibleOk() (*bool, bool)`

GetIsPubliclyVisibleOk returns a tuple with the IsPubliclyVisible field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsPubliclyVisible

`func (o *CreateCustomRequest) SetIsPubliclyVisible(v bool)`

SetIsPubliclyVisible sets IsPubliclyVisible field to given value.

### HasIsPubliclyVisible

`func (o *CreateCustomRequest) HasIsPubliclyVisible() bool`

HasIsPubliclyVisible returns a boolean if a field has been set.

### SetIsPubliclyVisibleNil

`func (o *CreateCustomRequest) SetIsPubliclyVisibleNil(b bool)`

 SetIsPubliclyVisibleNil sets the value for IsPubliclyVisible to be an explicit nil

### UnsetIsPubliclyVisible
`func (o *CreateCustomRequest) UnsetIsPubliclyVisible()`

UnsetIsPubliclyVisible ensures that no value is present for IsPubliclyVisible, not even an explicit nil
### GetMinRosterSize

`func (o *CreateCustomRequest) GetMinRosterSize() int32`

GetMinRosterSize returns the MinRosterSize field if non-nil, zero value otherwise.

### GetMinRosterSizeOk

`func (o *CreateCustomRequest) GetMinRosterSizeOk() (*int32, bool)`

GetMinRosterSizeOk returns a tuple with the MinRosterSize field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMinRosterSize

`func (o *CreateCustomRequest) SetMinRosterSize(v int32)`

SetMinRosterSize sets MinRosterSize field to given value.

### HasMinRosterSize

`func (o *CreateCustomRequest) HasMinRosterSize() bool`

HasMinRosterSize returns a boolean if a field has been set.

### SetMinRosterSizeNil

`func (o *CreateCustomRequest) SetMinRosterSizeNil(b bool)`

 SetMinRosterSizeNil sets the value for MinRosterSize to be an explicit nil

### UnsetMinRosterSize
`func (o *CreateCustomRequest) UnsetMinRosterSize()`

UnsetMinRosterSize ensures that no value is present for MinRosterSize, not even an explicit nil
### GetRandomizeLanes

`func (o *CreateCustomRequest) GetRandomizeLanes() bool`

GetRandomizeLanes returns the RandomizeLanes field if non-nil, zero value otherwise.

### GetRandomizeLanesOk

`func (o *CreateCustomRequest) GetRandomizeLanesOk() (*bool, bool)`

GetRandomizeLanesOk returns a tuple with the RandomizeLanes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRandomizeLanes

`func (o *CreateCustomRequest) SetRandomizeLanes(v bool)`

SetRandomizeLanes sets RandomizeLanes field to given value.

### HasRandomizeLanes

`func (o *CreateCustomRequest) HasRandomizeLanes() bool`

HasRandomizeLanes returns a boolean if a field has been set.

### SetRandomizeLanesNil

`func (o *CreateCustomRequest) SetRandomizeLanesNil(b bool)`

 SetRandomizeLanesNil sets the value for RandomizeLanes to be an explicit nil

### UnsetRandomizeLanes
`func (o *CreateCustomRequest) UnsetRandomizeLanes()`

UnsetRandomizeLanes ensures that no value is present for RandomizeLanes, not even an explicit nil
### GetRegionMode

`func (o *CreateCustomRequest) GetRegionMode() RegionMode`

GetRegionMode returns the RegionMode field if non-nil, zero value otherwise.

### GetRegionModeOk

`func (o *CreateCustomRequest) GetRegionModeOk() (*RegionMode, bool)`

GetRegionModeOk returns a tuple with the RegionMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegionMode

`func (o *CreateCustomRequest) SetRegionMode(v RegionMode)`

SetRegionMode sets RegionMode field to given value.

### HasRegionMode

`func (o *CreateCustomRequest) HasRegionMode() bool`

HasRegionMode returns a boolean if a field has been set.

### SetRegionModeNil

`func (o *CreateCustomRequest) SetRegionModeNil(b bool)`

 SetRegionModeNil sets the value for RegionMode to be an explicit nil

### UnsetRegionMode
`func (o *CreateCustomRequest) UnsetRegionMode()`

UnsetRegionMode ensures that no value is present for RegionMode, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


