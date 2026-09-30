# Settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ColorB** | Pointer to **int32** |  | [optional] [default to 255]
**ColorG** | Pointer to **int32** |  | [optional] [default to 255]
**ColorR** | Pointer to **int32** |  | [optional] [default to 255]
**DotOpacity** | Pointer to **float32** | 0 to 1. | [optional] [default to 0.7]
**DotOutlineBorder** | Pointer to **int32** |  | [optional] [default to 2]
**DotOutlineGap** | Pointer to **int32** |  | [optional] [default to 0]
**DotOutlineOpacity** | Pointer to **float32** | 0 to 1. | [optional] [default to 0.7]
**DotSize** | Pointer to **int32** |  | [optional] [default to 4]
**OutlineColorB** | Pointer to **int32** |  | [optional] [default to 0]
**OutlineColorG** | Pointer to **int32** |  | [optional] [default to 0]
**OutlineColorR** | Pointer to **int32** |  | [optional] [default to 0]
**PipGap** | Pointer to **int32** |  | [optional] [default to 4]
**PipGapStatic** | Pointer to **bool** | Keep the pips at a fixed distance instead of spreading them with weapon spread. | [optional] [default to false]
**PipHeight** | Pointer to **int32** |  | [optional] [default to 16]
**PipOpacity** | Pointer to **float32** | 0 to 1. | [optional] [default to 0.5]
**PipOutlineBorder** | Pointer to **int32** |  | [optional] [default to 1]
**PipOutlineGap** | Pointer to **int32** |  | [optional] [default to 0]
**PipOutlineOpacity** | Pointer to **float32** | 0 to 1. | [optional] [default to 0.7]
**PipWidth** | Pointer to **int32** |  | [optional] [default to 2]
**Themed** | Pointer to **bool** | Use the hero&#39;s own crosshair instead of these settings. | [optional] [default to false]

## Methods

### NewSettings

`func NewSettings() *Settings`

NewSettings instantiates a new Settings object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSettingsWithDefaults

`func NewSettingsWithDefaults() *Settings`

NewSettingsWithDefaults instantiates a new Settings object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetColorB

`func (o *Settings) GetColorB() int32`

GetColorB returns the ColorB field if non-nil, zero value otherwise.

### GetColorBOk

`func (o *Settings) GetColorBOk() (*int32, bool)`

GetColorBOk returns a tuple with the ColorB field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColorB

`func (o *Settings) SetColorB(v int32)`

SetColorB sets ColorB field to given value.

### HasColorB

`func (o *Settings) HasColorB() bool`

HasColorB returns a boolean if a field has been set.

### GetColorG

`func (o *Settings) GetColorG() int32`

GetColorG returns the ColorG field if non-nil, zero value otherwise.

### GetColorGOk

`func (o *Settings) GetColorGOk() (*int32, bool)`

GetColorGOk returns a tuple with the ColorG field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColorG

`func (o *Settings) SetColorG(v int32)`

SetColorG sets ColorG field to given value.

### HasColorG

`func (o *Settings) HasColorG() bool`

HasColorG returns a boolean if a field has been set.

### GetColorR

`func (o *Settings) GetColorR() int32`

GetColorR returns the ColorR field if non-nil, zero value otherwise.

### GetColorROk

`func (o *Settings) GetColorROk() (*int32, bool)`

GetColorROk returns a tuple with the ColorR field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColorR

`func (o *Settings) SetColorR(v int32)`

SetColorR sets ColorR field to given value.

### HasColorR

`func (o *Settings) HasColorR() bool`

HasColorR returns a boolean if a field has been set.

### GetDotOpacity

`func (o *Settings) GetDotOpacity() float32`

GetDotOpacity returns the DotOpacity field if non-nil, zero value otherwise.

### GetDotOpacityOk

`func (o *Settings) GetDotOpacityOk() (*float32, bool)`

GetDotOpacityOk returns a tuple with the DotOpacity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDotOpacity

`func (o *Settings) SetDotOpacity(v float32)`

SetDotOpacity sets DotOpacity field to given value.

### HasDotOpacity

`func (o *Settings) HasDotOpacity() bool`

HasDotOpacity returns a boolean if a field has been set.

### GetDotOutlineBorder

`func (o *Settings) GetDotOutlineBorder() int32`

GetDotOutlineBorder returns the DotOutlineBorder field if non-nil, zero value otherwise.

### GetDotOutlineBorderOk

`func (o *Settings) GetDotOutlineBorderOk() (*int32, bool)`

GetDotOutlineBorderOk returns a tuple with the DotOutlineBorder field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDotOutlineBorder

`func (o *Settings) SetDotOutlineBorder(v int32)`

SetDotOutlineBorder sets DotOutlineBorder field to given value.

### HasDotOutlineBorder

`func (o *Settings) HasDotOutlineBorder() bool`

HasDotOutlineBorder returns a boolean if a field has been set.

### GetDotOutlineGap

`func (o *Settings) GetDotOutlineGap() int32`

GetDotOutlineGap returns the DotOutlineGap field if non-nil, zero value otherwise.

### GetDotOutlineGapOk

`func (o *Settings) GetDotOutlineGapOk() (*int32, bool)`

GetDotOutlineGapOk returns a tuple with the DotOutlineGap field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDotOutlineGap

`func (o *Settings) SetDotOutlineGap(v int32)`

SetDotOutlineGap sets DotOutlineGap field to given value.

### HasDotOutlineGap

`func (o *Settings) HasDotOutlineGap() bool`

HasDotOutlineGap returns a boolean if a field has been set.

### GetDotOutlineOpacity

`func (o *Settings) GetDotOutlineOpacity() float32`

GetDotOutlineOpacity returns the DotOutlineOpacity field if non-nil, zero value otherwise.

### GetDotOutlineOpacityOk

`func (o *Settings) GetDotOutlineOpacityOk() (*float32, bool)`

GetDotOutlineOpacityOk returns a tuple with the DotOutlineOpacity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDotOutlineOpacity

`func (o *Settings) SetDotOutlineOpacity(v float32)`

SetDotOutlineOpacity sets DotOutlineOpacity field to given value.

### HasDotOutlineOpacity

`func (o *Settings) HasDotOutlineOpacity() bool`

HasDotOutlineOpacity returns a boolean if a field has been set.

### GetDotSize

`func (o *Settings) GetDotSize() int32`

GetDotSize returns the DotSize field if non-nil, zero value otherwise.

### GetDotSizeOk

`func (o *Settings) GetDotSizeOk() (*int32, bool)`

GetDotSizeOk returns a tuple with the DotSize field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDotSize

`func (o *Settings) SetDotSize(v int32)`

SetDotSize sets DotSize field to given value.

### HasDotSize

`func (o *Settings) HasDotSize() bool`

HasDotSize returns a boolean if a field has been set.

### GetOutlineColorB

`func (o *Settings) GetOutlineColorB() int32`

GetOutlineColorB returns the OutlineColorB field if non-nil, zero value otherwise.

### GetOutlineColorBOk

`func (o *Settings) GetOutlineColorBOk() (*int32, bool)`

GetOutlineColorBOk returns a tuple with the OutlineColorB field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutlineColorB

`func (o *Settings) SetOutlineColorB(v int32)`

SetOutlineColorB sets OutlineColorB field to given value.

### HasOutlineColorB

`func (o *Settings) HasOutlineColorB() bool`

HasOutlineColorB returns a boolean if a field has been set.

### GetOutlineColorG

`func (o *Settings) GetOutlineColorG() int32`

GetOutlineColorG returns the OutlineColorG field if non-nil, zero value otherwise.

### GetOutlineColorGOk

`func (o *Settings) GetOutlineColorGOk() (*int32, bool)`

GetOutlineColorGOk returns a tuple with the OutlineColorG field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutlineColorG

`func (o *Settings) SetOutlineColorG(v int32)`

SetOutlineColorG sets OutlineColorG field to given value.

### HasOutlineColorG

`func (o *Settings) HasOutlineColorG() bool`

HasOutlineColorG returns a boolean if a field has been set.

### GetOutlineColorR

`func (o *Settings) GetOutlineColorR() int32`

GetOutlineColorR returns the OutlineColorR field if non-nil, zero value otherwise.

### GetOutlineColorROk

`func (o *Settings) GetOutlineColorROk() (*int32, bool)`

GetOutlineColorROk returns a tuple with the OutlineColorR field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutlineColorR

`func (o *Settings) SetOutlineColorR(v int32)`

SetOutlineColorR sets OutlineColorR field to given value.

### HasOutlineColorR

`func (o *Settings) HasOutlineColorR() bool`

HasOutlineColorR returns a boolean if a field has been set.

### GetPipGap

`func (o *Settings) GetPipGap() int32`

GetPipGap returns the PipGap field if non-nil, zero value otherwise.

### GetPipGapOk

`func (o *Settings) GetPipGapOk() (*int32, bool)`

GetPipGapOk returns a tuple with the PipGap field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPipGap

`func (o *Settings) SetPipGap(v int32)`

SetPipGap sets PipGap field to given value.

### HasPipGap

`func (o *Settings) HasPipGap() bool`

HasPipGap returns a boolean if a field has been set.

### GetPipGapStatic

`func (o *Settings) GetPipGapStatic() bool`

GetPipGapStatic returns the PipGapStatic field if non-nil, zero value otherwise.

### GetPipGapStaticOk

`func (o *Settings) GetPipGapStaticOk() (*bool, bool)`

GetPipGapStaticOk returns a tuple with the PipGapStatic field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPipGapStatic

`func (o *Settings) SetPipGapStatic(v bool)`

SetPipGapStatic sets PipGapStatic field to given value.

### HasPipGapStatic

`func (o *Settings) HasPipGapStatic() bool`

HasPipGapStatic returns a boolean if a field has been set.

### GetPipHeight

`func (o *Settings) GetPipHeight() int32`

GetPipHeight returns the PipHeight field if non-nil, zero value otherwise.

### GetPipHeightOk

`func (o *Settings) GetPipHeightOk() (*int32, bool)`

GetPipHeightOk returns a tuple with the PipHeight field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPipHeight

`func (o *Settings) SetPipHeight(v int32)`

SetPipHeight sets PipHeight field to given value.

### HasPipHeight

`func (o *Settings) HasPipHeight() bool`

HasPipHeight returns a boolean if a field has been set.

### GetPipOpacity

`func (o *Settings) GetPipOpacity() float32`

GetPipOpacity returns the PipOpacity field if non-nil, zero value otherwise.

### GetPipOpacityOk

`func (o *Settings) GetPipOpacityOk() (*float32, bool)`

GetPipOpacityOk returns a tuple with the PipOpacity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPipOpacity

`func (o *Settings) SetPipOpacity(v float32)`

SetPipOpacity sets PipOpacity field to given value.

### HasPipOpacity

`func (o *Settings) HasPipOpacity() bool`

HasPipOpacity returns a boolean if a field has been set.

### GetPipOutlineBorder

`func (o *Settings) GetPipOutlineBorder() int32`

GetPipOutlineBorder returns the PipOutlineBorder field if non-nil, zero value otherwise.

### GetPipOutlineBorderOk

`func (o *Settings) GetPipOutlineBorderOk() (*int32, bool)`

GetPipOutlineBorderOk returns a tuple with the PipOutlineBorder field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPipOutlineBorder

`func (o *Settings) SetPipOutlineBorder(v int32)`

SetPipOutlineBorder sets PipOutlineBorder field to given value.

### HasPipOutlineBorder

`func (o *Settings) HasPipOutlineBorder() bool`

HasPipOutlineBorder returns a boolean if a field has been set.

### GetPipOutlineGap

`func (o *Settings) GetPipOutlineGap() int32`

GetPipOutlineGap returns the PipOutlineGap field if non-nil, zero value otherwise.

### GetPipOutlineGapOk

`func (o *Settings) GetPipOutlineGapOk() (*int32, bool)`

GetPipOutlineGapOk returns a tuple with the PipOutlineGap field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPipOutlineGap

`func (o *Settings) SetPipOutlineGap(v int32)`

SetPipOutlineGap sets PipOutlineGap field to given value.

### HasPipOutlineGap

`func (o *Settings) HasPipOutlineGap() bool`

HasPipOutlineGap returns a boolean if a field has been set.

### GetPipOutlineOpacity

`func (o *Settings) GetPipOutlineOpacity() float32`

GetPipOutlineOpacity returns the PipOutlineOpacity field if non-nil, zero value otherwise.

### GetPipOutlineOpacityOk

`func (o *Settings) GetPipOutlineOpacityOk() (*float32, bool)`

GetPipOutlineOpacityOk returns a tuple with the PipOutlineOpacity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPipOutlineOpacity

`func (o *Settings) SetPipOutlineOpacity(v float32)`

SetPipOutlineOpacity sets PipOutlineOpacity field to given value.

### HasPipOutlineOpacity

`func (o *Settings) HasPipOutlineOpacity() bool`

HasPipOutlineOpacity returns a boolean if a field has been set.

### GetPipWidth

`func (o *Settings) GetPipWidth() int32`

GetPipWidth returns the PipWidth field if non-nil, zero value otherwise.

### GetPipWidthOk

`func (o *Settings) GetPipWidthOk() (*int32, bool)`

GetPipWidthOk returns a tuple with the PipWidth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPipWidth

`func (o *Settings) SetPipWidth(v int32)`

SetPipWidth sets PipWidth field to given value.

### HasPipWidth

`func (o *Settings) HasPipWidth() bool`

HasPipWidth returns a boolean if a field has been set.

### GetThemed

`func (o *Settings) GetThemed() bool`

GetThemed returns the Themed field if non-nil, zero value otherwise.

### GetThemedOk

`func (o *Settings) GetThemedOk() (*bool, bool)`

GetThemedOk returns a tuple with the Themed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThemed

`func (o *Settings) SetThemed(v bool)`

SetThemed sets Themed field to given value.

### HasThemed

`func (o *Settings) HasThemed() bool`

HasThemed returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


