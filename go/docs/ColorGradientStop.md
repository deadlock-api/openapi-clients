# ColorGradientStop

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Color** | [**Color**](Color.md) |  | 
**Position** | **float64** | Position of the stop along the flash&#39;s lifetime, &#x60;0.0..&#x3D;1.0&#x60;. | 

## Methods

### NewColorGradientStop

`func NewColorGradientStop(color Color, position float64, ) *ColorGradientStop`

NewColorGradientStop instantiates a new ColorGradientStop object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewColorGradientStopWithDefaults

`func NewColorGradientStopWithDefaults() *ColorGradientStop`

NewColorGradientStopWithDefaults instantiates a new ColorGradientStop object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetColor

`func (o *ColorGradientStop) GetColor() Color`

GetColor returns the Color field if non-nil, zero value otherwise.

### GetColorOk

`func (o *ColorGradientStop) GetColorOk() (*Color, bool)`

GetColorOk returns a tuple with the Color field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColor

`func (o *ColorGradientStop) SetColor(v Color)`

SetColor sets Color field to given value.


### GetPosition

`func (o *ColorGradientStop) GetPosition() float64`

GetPosition returns the Position field if non-nil, zero value otherwise.

### GetPositionOk

`func (o *ColorGradientStop) GetPositionOk() (*float64, bool)`

GetPositionOk returns a tuple with the Position field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPosition

`func (o *ColorGradientStop) SetPosition(v float64)`

SetPosition sets Position field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


