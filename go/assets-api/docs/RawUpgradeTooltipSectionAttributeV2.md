# RawUpgradeTooltipSectionAttributeV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LocString** | Pointer to **NullableString** |  | [optional] 
**Properties** | Pointer to **[]string** |  | [optional] 
**ElevatedProperties** | Pointer to **[]string** |  | [optional] 
**ImportantProperties** | Pointer to [**[]RawUpgradeTooltipSectionAttributeImportantPropertyV2**](RawUpgradeTooltipSectionAttributeImportantPropertyV2.md) |  | [optional] 
**ImportantPropertiesWithIconPath** | [**[]RawUpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon**](RawUpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon.md) |  | 

## Methods

### NewRawUpgradeTooltipSectionAttributeV2

`func NewRawUpgradeTooltipSectionAttributeV2(importantPropertiesWithIconPath []RawUpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon, ) *RawUpgradeTooltipSectionAttributeV2`

NewRawUpgradeTooltipSectionAttributeV2 instantiates a new RawUpgradeTooltipSectionAttributeV2 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRawUpgradeTooltipSectionAttributeV2WithDefaults

`func NewRawUpgradeTooltipSectionAttributeV2WithDefaults() *RawUpgradeTooltipSectionAttributeV2`

NewRawUpgradeTooltipSectionAttributeV2WithDefaults instantiates a new RawUpgradeTooltipSectionAttributeV2 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLocString

`func (o *RawUpgradeTooltipSectionAttributeV2) GetLocString() string`

GetLocString returns the LocString field if non-nil, zero value otherwise.

### GetLocStringOk

`func (o *RawUpgradeTooltipSectionAttributeV2) GetLocStringOk() (*string, bool)`

GetLocStringOk returns a tuple with the LocString field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocString

`func (o *RawUpgradeTooltipSectionAttributeV2) SetLocString(v string)`

SetLocString sets LocString field to given value.

### HasLocString

`func (o *RawUpgradeTooltipSectionAttributeV2) HasLocString() bool`

HasLocString returns a boolean if a field has been set.

### SetLocStringNil

`func (o *RawUpgradeTooltipSectionAttributeV2) SetLocStringNil(b bool)`

 SetLocStringNil sets the value for LocString to be an explicit nil

### UnsetLocString
`func (o *RawUpgradeTooltipSectionAttributeV2) UnsetLocString()`

UnsetLocString ensures that no value is present for LocString, not even an explicit nil
### GetProperties

`func (o *RawUpgradeTooltipSectionAttributeV2) GetProperties() []string`

GetProperties returns the Properties field if non-nil, zero value otherwise.

### GetPropertiesOk

`func (o *RawUpgradeTooltipSectionAttributeV2) GetPropertiesOk() (*[]string, bool)`

GetPropertiesOk returns a tuple with the Properties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperties

`func (o *RawUpgradeTooltipSectionAttributeV2) SetProperties(v []string)`

SetProperties sets Properties field to given value.

### HasProperties

`func (o *RawUpgradeTooltipSectionAttributeV2) HasProperties() bool`

HasProperties returns a boolean if a field has been set.

### SetPropertiesNil

`func (o *RawUpgradeTooltipSectionAttributeV2) SetPropertiesNil(b bool)`

 SetPropertiesNil sets the value for Properties to be an explicit nil

### UnsetProperties
`func (o *RawUpgradeTooltipSectionAttributeV2) UnsetProperties()`

UnsetProperties ensures that no value is present for Properties, not even an explicit nil
### GetElevatedProperties

`func (o *RawUpgradeTooltipSectionAttributeV2) GetElevatedProperties() []string`

GetElevatedProperties returns the ElevatedProperties field if non-nil, zero value otherwise.

### GetElevatedPropertiesOk

`func (o *RawUpgradeTooltipSectionAttributeV2) GetElevatedPropertiesOk() (*[]string, bool)`

GetElevatedPropertiesOk returns a tuple with the ElevatedProperties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetElevatedProperties

`func (o *RawUpgradeTooltipSectionAttributeV2) SetElevatedProperties(v []string)`

SetElevatedProperties sets ElevatedProperties field to given value.

### HasElevatedProperties

`func (o *RawUpgradeTooltipSectionAttributeV2) HasElevatedProperties() bool`

HasElevatedProperties returns a boolean if a field has been set.

### SetElevatedPropertiesNil

`func (o *RawUpgradeTooltipSectionAttributeV2) SetElevatedPropertiesNil(b bool)`

 SetElevatedPropertiesNil sets the value for ElevatedProperties to be an explicit nil

### UnsetElevatedProperties
`func (o *RawUpgradeTooltipSectionAttributeV2) UnsetElevatedProperties()`

UnsetElevatedProperties ensures that no value is present for ElevatedProperties, not even an explicit nil
### GetImportantProperties

`func (o *RawUpgradeTooltipSectionAttributeV2) GetImportantProperties() []RawUpgradeTooltipSectionAttributeImportantPropertyV2`

GetImportantProperties returns the ImportantProperties field if non-nil, zero value otherwise.

### GetImportantPropertiesOk

`func (o *RawUpgradeTooltipSectionAttributeV2) GetImportantPropertiesOk() (*[]RawUpgradeTooltipSectionAttributeImportantPropertyV2, bool)`

GetImportantPropertiesOk returns a tuple with the ImportantProperties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImportantProperties

`func (o *RawUpgradeTooltipSectionAttributeV2) SetImportantProperties(v []RawUpgradeTooltipSectionAttributeImportantPropertyV2)`

SetImportantProperties sets ImportantProperties field to given value.

### HasImportantProperties

`func (o *RawUpgradeTooltipSectionAttributeV2) HasImportantProperties() bool`

HasImportantProperties returns a boolean if a field has been set.

### SetImportantPropertiesNil

`func (o *RawUpgradeTooltipSectionAttributeV2) SetImportantPropertiesNil(b bool)`

 SetImportantPropertiesNil sets the value for ImportantProperties to be an explicit nil

### UnsetImportantProperties
`func (o *RawUpgradeTooltipSectionAttributeV2) UnsetImportantProperties()`

UnsetImportantProperties ensures that no value is present for ImportantProperties, not even an explicit nil
### GetImportantPropertiesWithIconPath

`func (o *RawUpgradeTooltipSectionAttributeV2) GetImportantPropertiesWithIconPath() []RawUpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon`

GetImportantPropertiesWithIconPath returns the ImportantPropertiesWithIconPath field if non-nil, zero value otherwise.

### GetImportantPropertiesWithIconPathOk

`func (o *RawUpgradeTooltipSectionAttributeV2) GetImportantPropertiesWithIconPathOk() (*[]RawUpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon, bool)`

GetImportantPropertiesWithIconPathOk returns a tuple with the ImportantPropertiesWithIconPath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImportantPropertiesWithIconPath

`func (o *RawUpgradeTooltipSectionAttributeV2) SetImportantPropertiesWithIconPath(v []RawUpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon)`

SetImportantPropertiesWithIconPath sets ImportantPropertiesWithIconPath field to given value.


### SetImportantPropertiesWithIconPathNil

`func (o *RawUpgradeTooltipSectionAttributeV2) SetImportantPropertiesWithIconPathNil(b bool)`

 SetImportantPropertiesWithIconPathNil sets the value for ImportantPropertiesWithIconPath to be an explicit nil

### UnsetImportantPropertiesWithIconPath
`func (o *RawUpgradeTooltipSectionAttributeV2) UnsetImportantPropertiesWithIconPath()`

UnsetImportantPropertiesWithIconPath ensures that no value is present for ImportantPropertiesWithIconPath, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


