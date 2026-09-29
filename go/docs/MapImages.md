# MapImages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Background** | Pointer to **NullableString** | Background layer drawn under &#x60;mid&#x60;. Only for builds before 6711; the game no longer ships it, so it is omitted from build 6711 on. | [optional] 
**Frame** | **string** |  | 
**Mid** | **string** | Midtown base layer. | 
**MidTunnels** | Pointer to **NullableString** | Mid tunnels overlay, drawn above &#x60;mid&#x60; (build 6711+). | [optional] 
**Minimap** | **string** | Full minimap. From build 6711 on the game ships no composed minimap, so this is the same image as &#x60;mid&#x60;: the midtown street layer as a black mask on transparency, meant to be drawn over a base colour rather than shown on its own. | 
**Plain** | **string** | Minimap without overlays. From build 6711 on this is the same street mask as &#x60;mid&#x60; (see &#x60;minimap&#x60;). | 
**RatTunnels** | Pointer to **NullableString** | Rat tunnels overlay, drawn above &#x60;mid_tunnels&#x60; (build 6711+). | [optional] 

## Methods

### NewMapImages

`func NewMapImages(frame string, mid string, minimap string, plain string, ) *MapImages`

NewMapImages instantiates a new MapImages object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMapImagesWithDefaults

`func NewMapImagesWithDefaults() *MapImages`

NewMapImagesWithDefaults instantiates a new MapImages object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBackground

`func (o *MapImages) GetBackground() string`

GetBackground returns the Background field if non-nil, zero value otherwise.

### GetBackgroundOk

`func (o *MapImages) GetBackgroundOk() (*string, bool)`

GetBackgroundOk returns a tuple with the Background field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBackground

`func (o *MapImages) SetBackground(v string)`

SetBackground sets Background field to given value.

### HasBackground

`func (o *MapImages) HasBackground() bool`

HasBackground returns a boolean if a field has been set.

### SetBackgroundNil

`func (o *MapImages) SetBackgroundNil(b bool)`

 SetBackgroundNil sets the value for Background to be an explicit nil

### UnsetBackground
`func (o *MapImages) UnsetBackground()`

UnsetBackground ensures that no value is present for Background, not even an explicit nil
### GetFrame

`func (o *MapImages) GetFrame() string`

GetFrame returns the Frame field if non-nil, zero value otherwise.

### GetFrameOk

`func (o *MapImages) GetFrameOk() (*string, bool)`

GetFrameOk returns a tuple with the Frame field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFrame

`func (o *MapImages) SetFrame(v string)`

SetFrame sets Frame field to given value.


### GetMid

`func (o *MapImages) GetMid() string`

GetMid returns the Mid field if non-nil, zero value otherwise.

### GetMidOk

`func (o *MapImages) GetMidOk() (*string, bool)`

GetMidOk returns a tuple with the Mid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMid

`func (o *MapImages) SetMid(v string)`

SetMid sets Mid field to given value.


### GetMidTunnels

`func (o *MapImages) GetMidTunnels() string`

GetMidTunnels returns the MidTunnels field if non-nil, zero value otherwise.

### GetMidTunnelsOk

`func (o *MapImages) GetMidTunnelsOk() (*string, bool)`

GetMidTunnelsOk returns a tuple with the MidTunnels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMidTunnels

`func (o *MapImages) SetMidTunnels(v string)`

SetMidTunnels sets MidTunnels field to given value.

### HasMidTunnels

`func (o *MapImages) HasMidTunnels() bool`

HasMidTunnels returns a boolean if a field has been set.

### SetMidTunnelsNil

`func (o *MapImages) SetMidTunnelsNil(b bool)`

 SetMidTunnelsNil sets the value for MidTunnels to be an explicit nil

### UnsetMidTunnels
`func (o *MapImages) UnsetMidTunnels()`

UnsetMidTunnels ensures that no value is present for MidTunnels, not even an explicit nil
### GetMinimap

`func (o *MapImages) GetMinimap() string`

GetMinimap returns the Minimap field if non-nil, zero value otherwise.

### GetMinimapOk

`func (o *MapImages) GetMinimapOk() (*string, bool)`

GetMinimapOk returns a tuple with the Minimap field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMinimap

`func (o *MapImages) SetMinimap(v string)`

SetMinimap sets Minimap field to given value.


### GetPlain

`func (o *MapImages) GetPlain() string`

GetPlain returns the Plain field if non-nil, zero value otherwise.

### GetPlainOk

`func (o *MapImages) GetPlainOk() (*string, bool)`

GetPlainOk returns a tuple with the Plain field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlain

`func (o *MapImages) SetPlain(v string)`

SetPlain sets Plain field to given value.


### GetRatTunnels

`func (o *MapImages) GetRatTunnels() string`

GetRatTunnels returns the RatTunnels field if non-nil, zero value otherwise.

### GetRatTunnelsOk

`func (o *MapImages) GetRatTunnelsOk() (*string, bool)`

GetRatTunnelsOk returns a tuple with the RatTunnels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRatTunnels

`func (o *MapImages) SetRatTunnels(v string)`

SetRatTunnels sets RatTunnels field to given value.

### HasRatTunnels

`func (o *MapImages) HasRatTunnels() bool`

HasRatTunnels returns a boolean if a field has been set.

### SetRatTunnelsNil

`func (o *MapImages) SetRatTunnelsNil(b bool)`

 SetRatTunnelsNil sets the value for RatTunnels to be an explicit nil

### UnsetRatTunnels
`func (o *MapImages) UnsetRatTunnels()`

UnsetRatTunnels ensures that no value is present for RatTunnels, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


