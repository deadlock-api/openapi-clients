# LaneInfoV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LaneName** | **string** |  | 
**CssClass** | Pointer to **NullableString** |  | [optional] 
**Color** | [**ColorV1**](ColorV1.md) |  | 
**MinimapZiplineColorOverride** | Pointer to [**NullableColorV1**](ColorV1.md) |  | [optional] 
**ObjectiveColor** | Pointer to [**NullableColorV1**](ColorV1.md) |  | [optional] 

## Methods

### NewLaneInfoV2

`func NewLaneInfoV2(laneName string, color ColorV1, ) *LaneInfoV2`

NewLaneInfoV2 instantiates a new LaneInfoV2 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewLaneInfoV2WithDefaults

`func NewLaneInfoV2WithDefaults() *LaneInfoV2`

NewLaneInfoV2WithDefaults instantiates a new LaneInfoV2 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLaneName

`func (o *LaneInfoV2) GetLaneName() string`

GetLaneName returns the LaneName field if non-nil, zero value otherwise.

### GetLaneNameOk

`func (o *LaneInfoV2) GetLaneNameOk() (*string, bool)`

GetLaneNameOk returns a tuple with the LaneName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLaneName

`func (o *LaneInfoV2) SetLaneName(v string)`

SetLaneName sets LaneName field to given value.


### GetCssClass

`func (o *LaneInfoV2) GetCssClass() string`

GetCssClass returns the CssClass field if non-nil, zero value otherwise.

### GetCssClassOk

`func (o *LaneInfoV2) GetCssClassOk() (*string, bool)`

GetCssClassOk returns a tuple with the CssClass field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCssClass

`func (o *LaneInfoV2) SetCssClass(v string)`

SetCssClass sets CssClass field to given value.

### HasCssClass

`func (o *LaneInfoV2) HasCssClass() bool`

HasCssClass returns a boolean if a field has been set.

### SetCssClassNil

`func (o *LaneInfoV2) SetCssClassNil(b bool)`

 SetCssClassNil sets the value for CssClass to be an explicit nil

### UnsetCssClass
`func (o *LaneInfoV2) UnsetCssClass()`

UnsetCssClass ensures that no value is present for CssClass, not even an explicit nil
### GetColor

`func (o *LaneInfoV2) GetColor() ColorV1`

GetColor returns the Color field if non-nil, zero value otherwise.

### GetColorOk

`func (o *LaneInfoV2) GetColorOk() (*ColorV1, bool)`

GetColorOk returns a tuple with the Color field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColor

`func (o *LaneInfoV2) SetColor(v ColorV1)`

SetColor sets Color field to given value.


### GetMinimapZiplineColorOverride

`func (o *LaneInfoV2) GetMinimapZiplineColorOverride() ColorV1`

GetMinimapZiplineColorOverride returns the MinimapZiplineColorOverride field if non-nil, zero value otherwise.

### GetMinimapZiplineColorOverrideOk

`func (o *LaneInfoV2) GetMinimapZiplineColorOverrideOk() (*ColorV1, bool)`

GetMinimapZiplineColorOverrideOk returns a tuple with the MinimapZiplineColorOverride field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMinimapZiplineColorOverride

`func (o *LaneInfoV2) SetMinimapZiplineColorOverride(v ColorV1)`

SetMinimapZiplineColorOverride sets MinimapZiplineColorOverride field to given value.

### HasMinimapZiplineColorOverride

`func (o *LaneInfoV2) HasMinimapZiplineColorOverride() bool`

HasMinimapZiplineColorOverride returns a boolean if a field has been set.

### SetMinimapZiplineColorOverrideNil

`func (o *LaneInfoV2) SetMinimapZiplineColorOverrideNil(b bool)`

 SetMinimapZiplineColorOverrideNil sets the value for MinimapZiplineColorOverride to be an explicit nil

### UnsetMinimapZiplineColorOverride
`func (o *LaneInfoV2) UnsetMinimapZiplineColorOverride()`

UnsetMinimapZiplineColorOverride ensures that no value is present for MinimapZiplineColorOverride, not even an explicit nil
### GetObjectiveColor

`func (o *LaneInfoV2) GetObjectiveColor() ColorV1`

GetObjectiveColor returns the ObjectiveColor field if non-nil, zero value otherwise.

### GetObjectiveColorOk

`func (o *LaneInfoV2) GetObjectiveColorOk() (*ColorV1, bool)`

GetObjectiveColorOk returns a tuple with the ObjectiveColor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectiveColor

`func (o *LaneInfoV2) SetObjectiveColor(v ColorV1)`

SetObjectiveColor sets ObjectiveColor field to given value.

### HasObjectiveColor

`func (o *LaneInfoV2) HasObjectiveColor() bool`

HasObjectiveColor returns a boolean if a field has been set.

### SetObjectiveColorNil

`func (o *LaneInfoV2) SetObjectiveColorNil(b bool)`

 SetObjectiveColorNil sets the value for ObjectiveColor to be an explicit nil

### UnsetObjectiveColor
`func (o *LaneInfoV2) UnsetObjectiveColor()`

UnsetObjectiveColor ensures that no value is present for ObjectiveColor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


