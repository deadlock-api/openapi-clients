# LaneInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Color** | Pointer to [**NullableColor**](Color.md) | Absent for unused lane slots (build 6711+). | [optional] 
**CssClass** | Pointer to **NullableString** |  | [optional] 
**IsEnemyLane** | **bool** |  | 
**LaneName** | **string** | Localized lane name. Unused lane slots are named &#x60;Unused&#x60;. | 
**MinimapColor** | Pointer to [**NullableColor**](Color.md) | Build 6711+. | [optional] 
**MinimapZiplineColorOverride** | Pointer to [**NullableColor**](Color.md) | Only present up to build 6701. | [optional] 
**ObjectiveColor** | Pointer to [**NullableColor**](Color.md) | Only present up to build 6701. | [optional] 

## Methods

### NewLaneInfo

`func NewLaneInfo(isEnemyLane bool, laneName string, ) *LaneInfo`

NewLaneInfo instantiates a new LaneInfo object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewLaneInfoWithDefaults

`func NewLaneInfoWithDefaults() *LaneInfo`

NewLaneInfoWithDefaults instantiates a new LaneInfo object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetColor

`func (o *LaneInfo) GetColor() Color`

GetColor returns the Color field if non-nil, zero value otherwise.

### GetColorOk

`func (o *LaneInfo) GetColorOk() (*Color, bool)`

GetColorOk returns a tuple with the Color field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColor

`func (o *LaneInfo) SetColor(v Color)`

SetColor sets Color field to given value.

### HasColor

`func (o *LaneInfo) HasColor() bool`

HasColor returns a boolean if a field has been set.

### SetColorNil

`func (o *LaneInfo) SetColorNil(b bool)`

 SetColorNil sets the value for Color to be an explicit nil

### UnsetColor
`func (o *LaneInfo) UnsetColor()`

UnsetColor ensures that no value is present for Color, not even an explicit nil
### GetCssClass

`func (o *LaneInfo) GetCssClass() string`

GetCssClass returns the CssClass field if non-nil, zero value otherwise.

### GetCssClassOk

`func (o *LaneInfo) GetCssClassOk() (*string, bool)`

GetCssClassOk returns a tuple with the CssClass field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCssClass

`func (o *LaneInfo) SetCssClass(v string)`

SetCssClass sets CssClass field to given value.

### HasCssClass

`func (o *LaneInfo) HasCssClass() bool`

HasCssClass returns a boolean if a field has been set.

### SetCssClassNil

`func (o *LaneInfo) SetCssClassNil(b bool)`

 SetCssClassNil sets the value for CssClass to be an explicit nil

### UnsetCssClass
`func (o *LaneInfo) UnsetCssClass()`

UnsetCssClass ensures that no value is present for CssClass, not even an explicit nil
### GetIsEnemyLane

`func (o *LaneInfo) GetIsEnemyLane() bool`

GetIsEnemyLane returns the IsEnemyLane field if non-nil, zero value otherwise.

### GetIsEnemyLaneOk

`func (o *LaneInfo) GetIsEnemyLaneOk() (*bool, bool)`

GetIsEnemyLaneOk returns a tuple with the IsEnemyLane field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsEnemyLane

`func (o *LaneInfo) SetIsEnemyLane(v bool)`

SetIsEnemyLane sets IsEnemyLane field to given value.


### GetLaneName

`func (o *LaneInfo) GetLaneName() string`

GetLaneName returns the LaneName field if non-nil, zero value otherwise.

### GetLaneNameOk

`func (o *LaneInfo) GetLaneNameOk() (*string, bool)`

GetLaneNameOk returns a tuple with the LaneName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLaneName

`func (o *LaneInfo) SetLaneName(v string)`

SetLaneName sets LaneName field to given value.


### GetMinimapColor

`func (o *LaneInfo) GetMinimapColor() Color`

GetMinimapColor returns the MinimapColor field if non-nil, zero value otherwise.

### GetMinimapColorOk

`func (o *LaneInfo) GetMinimapColorOk() (*Color, bool)`

GetMinimapColorOk returns a tuple with the MinimapColor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMinimapColor

`func (o *LaneInfo) SetMinimapColor(v Color)`

SetMinimapColor sets MinimapColor field to given value.

### HasMinimapColor

`func (o *LaneInfo) HasMinimapColor() bool`

HasMinimapColor returns a boolean if a field has been set.

### SetMinimapColorNil

`func (o *LaneInfo) SetMinimapColorNil(b bool)`

 SetMinimapColorNil sets the value for MinimapColor to be an explicit nil

### UnsetMinimapColor
`func (o *LaneInfo) UnsetMinimapColor()`

UnsetMinimapColor ensures that no value is present for MinimapColor, not even an explicit nil
### GetMinimapZiplineColorOverride

`func (o *LaneInfo) GetMinimapZiplineColorOverride() Color`

GetMinimapZiplineColorOverride returns the MinimapZiplineColorOverride field if non-nil, zero value otherwise.

### GetMinimapZiplineColorOverrideOk

`func (o *LaneInfo) GetMinimapZiplineColorOverrideOk() (*Color, bool)`

GetMinimapZiplineColorOverrideOk returns a tuple with the MinimapZiplineColorOverride field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMinimapZiplineColorOverride

`func (o *LaneInfo) SetMinimapZiplineColorOverride(v Color)`

SetMinimapZiplineColorOverride sets MinimapZiplineColorOverride field to given value.

### HasMinimapZiplineColorOverride

`func (o *LaneInfo) HasMinimapZiplineColorOverride() bool`

HasMinimapZiplineColorOverride returns a boolean if a field has been set.

### SetMinimapZiplineColorOverrideNil

`func (o *LaneInfo) SetMinimapZiplineColorOverrideNil(b bool)`

 SetMinimapZiplineColorOverrideNil sets the value for MinimapZiplineColorOverride to be an explicit nil

### UnsetMinimapZiplineColorOverride
`func (o *LaneInfo) UnsetMinimapZiplineColorOverride()`

UnsetMinimapZiplineColorOverride ensures that no value is present for MinimapZiplineColorOverride, not even an explicit nil
### GetObjectiveColor

`func (o *LaneInfo) GetObjectiveColor() Color`

GetObjectiveColor returns the ObjectiveColor field if non-nil, zero value otherwise.

### GetObjectiveColorOk

`func (o *LaneInfo) GetObjectiveColorOk() (*Color, bool)`

GetObjectiveColorOk returns a tuple with the ObjectiveColor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectiveColor

`func (o *LaneInfo) SetObjectiveColor(v Color)`

SetObjectiveColor sets ObjectiveColor field to given value.

### HasObjectiveColor

`func (o *LaneInfo) HasObjectiveColor() bool`

HasObjectiveColor returns a boolean if a field has been set.

### SetObjectiveColorNil

`func (o *LaneInfo) SetObjectiveColorNil(b bool)`

 SetObjectiveColorNil sets the value for ObjectiveColor to be an explicit nil

### UnsetObjectiveColor
`func (o *LaneInfo) UnsetObjectiveColor()`

UnsetObjectiveColor ensures that no value is present for ObjectiveColor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


