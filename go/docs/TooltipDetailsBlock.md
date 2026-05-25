# TooltipDetailsBlock

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LocString** | Pointer to **NullableString** |  | [optional] 
**Properties** | Pointer to [**[]TooltipDetailsBlockProperty**](TooltipDetailsBlockProperty.md) |  | [optional] 

## Methods

### NewTooltipDetailsBlock

`func NewTooltipDetailsBlock() *TooltipDetailsBlock`

NewTooltipDetailsBlock instantiates a new TooltipDetailsBlock object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTooltipDetailsBlockWithDefaults

`func NewTooltipDetailsBlockWithDefaults() *TooltipDetailsBlock`

NewTooltipDetailsBlockWithDefaults instantiates a new TooltipDetailsBlock object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLocString

`func (o *TooltipDetailsBlock) GetLocString() string`

GetLocString returns the LocString field if non-nil, zero value otherwise.

### GetLocStringOk

`func (o *TooltipDetailsBlock) GetLocStringOk() (*string, bool)`

GetLocStringOk returns a tuple with the LocString field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocString

`func (o *TooltipDetailsBlock) SetLocString(v string)`

SetLocString sets LocString field to given value.

### HasLocString

`func (o *TooltipDetailsBlock) HasLocString() bool`

HasLocString returns a boolean if a field has been set.

### SetLocStringNil

`func (o *TooltipDetailsBlock) SetLocStringNil(b bool)`

 SetLocStringNil sets the value for LocString to be an explicit nil

### UnsetLocString
`func (o *TooltipDetailsBlock) UnsetLocString()`

UnsetLocString ensures that no value is present for LocString, not even an explicit nil
### GetProperties

`func (o *TooltipDetailsBlock) GetProperties() []TooltipDetailsBlockProperty`

GetProperties returns the Properties field if non-nil, zero value otherwise.

### GetPropertiesOk

`func (o *TooltipDetailsBlock) GetPropertiesOk() (*[]TooltipDetailsBlockProperty, bool)`

GetPropertiesOk returns a tuple with the Properties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperties

`func (o *TooltipDetailsBlock) SetProperties(v []TooltipDetailsBlockProperty)`

SetProperties sets Properties field to given value.

### HasProperties

`func (o *TooltipDetailsBlock) HasProperties() bool`

HasProperties returns a boolean if a field has been set.

### SetPropertiesNil

`func (o *TooltipDetailsBlock) SetPropertiesNil(b bool)`

 SetPropertiesNil sets the value for Properties to be an explicit nil

### UnsetProperties
`func (o *TooltipDetailsBlock) UnsetProperties()`

UnsetProperties ensures that no value is present for Properties, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


