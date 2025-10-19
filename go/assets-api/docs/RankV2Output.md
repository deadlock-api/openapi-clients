# RankV2Output

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Tier** | **int32** |  | 
**Name** | **string** |  | 
**Images** | [**RankImagesV2**](RankImagesV2.md) |  | 
**Color** | **string** |  | [readonly] 

## Methods

### NewRankV2Output

`func NewRankV2Output(tier int32, name string, images RankImagesV2, color string, ) *RankV2Output`

NewRankV2Output instantiates a new RankV2Output object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRankV2OutputWithDefaults

`func NewRankV2OutputWithDefaults() *RankV2Output`

NewRankV2OutputWithDefaults instantiates a new RankV2Output object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTier

`func (o *RankV2Output) GetTier() int32`

GetTier returns the Tier field if non-nil, zero value otherwise.

### GetTierOk

`func (o *RankV2Output) GetTierOk() (*int32, bool)`

GetTierOk returns a tuple with the Tier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTier

`func (o *RankV2Output) SetTier(v int32)`

SetTier sets Tier field to given value.


### GetName

`func (o *RankV2Output) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *RankV2Output) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *RankV2Output) SetName(v string)`

SetName sets Name field to given value.


### GetImages

`func (o *RankV2Output) GetImages() RankImagesV2`

GetImages returns the Images field if non-nil, zero value otherwise.

### GetImagesOk

`func (o *RankV2Output) GetImagesOk() (*RankImagesV2, bool)`

GetImagesOk returns a tuple with the Images field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImages

`func (o *RankV2Output) SetImages(v RankImagesV2)`

SetImages sets Images field to given value.


### GetColor

`func (o *RankV2Output) GetColor() string`

GetColor returns the Color field if non-nil, zero value otherwise.

### GetColorOk

`func (o *RankV2Output) GetColorOk() (*string, bool)`

GetColorOk returns a tuple with the Color field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColor

`func (o *RankV2Output) SetColor(v string)`

SetColor sets Color field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


