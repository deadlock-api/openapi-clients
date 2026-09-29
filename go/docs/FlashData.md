# FlashData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Brightness** | Pointer to **NullableFloat64** |  | [optional] 
**BrightnessInLightSensitivityMode** | Pointer to **NullableFloat64** |  | [optional] 
**Color** | [**Color**](Color.md) | Flat flash color. From build 6711 on it is derived from the first &#x60;color_gradient&#x60; stop. | 
**ColorGradient** | Pointer to [**[]ColorGradientStop**](ColorGradientStop.md) | Color gradient over the flash&#39;s lifetime (build 6711+). | [optional] 
**Coverage** | Pointer to **NullableFloat64** | Only present up to build 6701. | [optional] 
**Duration** | **float64** |  | 
**Hardness** | Pointer to **NullableFloat64** | Only present up to build 6701. | [optional] 

## Methods

### NewFlashData

`func NewFlashData(color Color, duration float64, ) *FlashData`

NewFlashData instantiates a new FlashData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlashDataWithDefaults

`func NewFlashDataWithDefaults() *FlashData`

NewFlashDataWithDefaults instantiates a new FlashData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBrightness

`func (o *FlashData) GetBrightness() float64`

GetBrightness returns the Brightness field if non-nil, zero value otherwise.

### GetBrightnessOk

`func (o *FlashData) GetBrightnessOk() (*float64, bool)`

GetBrightnessOk returns a tuple with the Brightness field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrightness

`func (o *FlashData) SetBrightness(v float64)`

SetBrightness sets Brightness field to given value.

### HasBrightness

`func (o *FlashData) HasBrightness() bool`

HasBrightness returns a boolean if a field has been set.

### SetBrightnessNil

`func (o *FlashData) SetBrightnessNil(b bool)`

 SetBrightnessNil sets the value for Brightness to be an explicit nil

### UnsetBrightness
`func (o *FlashData) UnsetBrightness()`

UnsetBrightness ensures that no value is present for Brightness, not even an explicit nil
### GetBrightnessInLightSensitivityMode

`func (o *FlashData) GetBrightnessInLightSensitivityMode() float64`

GetBrightnessInLightSensitivityMode returns the BrightnessInLightSensitivityMode field if non-nil, zero value otherwise.

### GetBrightnessInLightSensitivityModeOk

`func (o *FlashData) GetBrightnessInLightSensitivityModeOk() (*float64, bool)`

GetBrightnessInLightSensitivityModeOk returns a tuple with the BrightnessInLightSensitivityMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrightnessInLightSensitivityMode

`func (o *FlashData) SetBrightnessInLightSensitivityMode(v float64)`

SetBrightnessInLightSensitivityMode sets BrightnessInLightSensitivityMode field to given value.

### HasBrightnessInLightSensitivityMode

`func (o *FlashData) HasBrightnessInLightSensitivityMode() bool`

HasBrightnessInLightSensitivityMode returns a boolean if a field has been set.

### SetBrightnessInLightSensitivityModeNil

`func (o *FlashData) SetBrightnessInLightSensitivityModeNil(b bool)`

 SetBrightnessInLightSensitivityModeNil sets the value for BrightnessInLightSensitivityMode to be an explicit nil

### UnsetBrightnessInLightSensitivityMode
`func (o *FlashData) UnsetBrightnessInLightSensitivityMode()`

UnsetBrightnessInLightSensitivityMode ensures that no value is present for BrightnessInLightSensitivityMode, not even an explicit nil
### GetColor

`func (o *FlashData) GetColor() Color`

GetColor returns the Color field if non-nil, zero value otherwise.

### GetColorOk

`func (o *FlashData) GetColorOk() (*Color, bool)`

GetColorOk returns a tuple with the Color field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColor

`func (o *FlashData) SetColor(v Color)`

SetColor sets Color field to given value.


### GetColorGradient

`func (o *FlashData) GetColorGradient() []ColorGradientStop`

GetColorGradient returns the ColorGradient field if non-nil, zero value otherwise.

### GetColorGradientOk

`func (o *FlashData) GetColorGradientOk() (*[]ColorGradientStop, bool)`

GetColorGradientOk returns a tuple with the ColorGradient field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColorGradient

`func (o *FlashData) SetColorGradient(v []ColorGradientStop)`

SetColorGradient sets ColorGradient field to given value.

### HasColorGradient

`func (o *FlashData) HasColorGradient() bool`

HasColorGradient returns a boolean if a field has been set.

### SetColorGradientNil

`func (o *FlashData) SetColorGradientNil(b bool)`

 SetColorGradientNil sets the value for ColorGradient to be an explicit nil

### UnsetColorGradient
`func (o *FlashData) UnsetColorGradient()`

UnsetColorGradient ensures that no value is present for ColorGradient, not even an explicit nil
### GetCoverage

`func (o *FlashData) GetCoverage() float64`

GetCoverage returns the Coverage field if non-nil, zero value otherwise.

### GetCoverageOk

`func (o *FlashData) GetCoverageOk() (*float64, bool)`

GetCoverageOk returns a tuple with the Coverage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCoverage

`func (o *FlashData) SetCoverage(v float64)`

SetCoverage sets Coverage field to given value.

### HasCoverage

`func (o *FlashData) HasCoverage() bool`

HasCoverage returns a boolean if a field has been set.

### SetCoverageNil

`func (o *FlashData) SetCoverageNil(b bool)`

 SetCoverageNil sets the value for Coverage to be an explicit nil

### UnsetCoverage
`func (o *FlashData) UnsetCoverage()`

UnsetCoverage ensures that no value is present for Coverage, not even an explicit nil
### GetDuration

`func (o *FlashData) GetDuration() float64`

GetDuration returns the Duration field if non-nil, zero value otherwise.

### GetDurationOk

`func (o *FlashData) GetDurationOk() (*float64, bool)`

GetDurationOk returns a tuple with the Duration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDuration

`func (o *FlashData) SetDuration(v float64)`

SetDuration sets Duration field to given value.


### GetHardness

`func (o *FlashData) GetHardness() float64`

GetHardness returns the Hardness field if non-nil, zero value otherwise.

### GetHardnessOk

`func (o *FlashData) GetHardnessOk() (*float64, bool)`

GetHardnessOk returns a tuple with the Hardness field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHardness

`func (o *FlashData) SetHardness(v float64)`

SetHardness sets Hardness field to given value.

### HasHardness

`func (o *FlashData) HasHardness() bool`

HasHardness returns a boolean if a field has been set.

### SetHardnessNil

`func (o *FlashData) SetHardnessNil(b bool)`

 SetHardnessNil sets the value for Hardness to be an explicit nil

### UnsetHardness
`func (o *FlashData) UnsetHardness()`

UnsetHardness ensures that no value is present for Hardness, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


