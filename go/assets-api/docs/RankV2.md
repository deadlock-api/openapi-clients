# RankV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Tier** | **int32** |  | 
**Name** | **string** |  | 
**Images** | [**RankImagesV2**](RankImagesV2.md) |  | 
**Color** | **string** |  | [readonly] 

## Methods

### NewRankV2

`func NewRankV2(tier int32, name string, images RankImagesV2, color string, ) *RankV2`

NewRankV2 instantiates a new RankV2 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRankV2WithDefaults

`func NewRankV2WithDefaults() *RankV2`

NewRankV2WithDefaults instantiates a new RankV2 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTier

`func (o *RankV2) GetTier() int32`

GetTier returns the Tier field if non-nil, zero value otherwise.

### GetTierOk

`func (o *RankV2) GetTierOk() (*int32, bool)`

GetTierOk returns a tuple with the Tier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTier

`func (o *RankV2) SetTier(v int32)`

SetTier sets Tier field to given value.


### GetName

`func (o *RankV2) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *RankV2) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *RankV2) SetName(v string)`

SetName sets Name field to given value.


### GetImages

`func (o *RankV2) GetImages() RankImagesV2`

GetImages returns the Images field if non-nil, zero value otherwise.

### GetImagesOk

`func (o *RankV2) GetImagesOk() (*RankImagesV2, bool)`

GetImagesOk returns a tuple with the Images field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImages

`func (o *RankV2) SetImages(v RankImagesV2)`

SetImages sets Images field to given value.


### GetColor

`func (o *RankV2) GetColor() string`

GetColor returns the Color field if non-nil, zero value otherwise.

### GetColorOk

`func (o *RankV2) GetColorOk() (*string, bool)`

GetColorOk returns a tuple with the Color field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColor

`func (o *RankV2) SetColor(v string)`

SetColor sets Color field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


