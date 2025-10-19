# RankV2Input

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Tier** | **int32** |  | 
**Name** | **string** |  | 
**Images** | [**RankImagesV2**](RankImagesV2.md) |  | 

## Methods

### NewRankV2Input

`func NewRankV2Input(tier int32, name string, images RankImagesV2, ) *RankV2Input`

NewRankV2Input instantiates a new RankV2Input object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRankV2InputWithDefaults

`func NewRankV2InputWithDefaults() *RankV2Input`

NewRankV2InputWithDefaults instantiates a new RankV2Input object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTier

`func (o *RankV2Input) GetTier() int32`

GetTier returns the Tier field if non-nil, zero value otherwise.

### GetTierOk

`func (o *RankV2Input) GetTierOk() (*int32, bool)`

GetTierOk returns a tuple with the Tier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTier

`func (o *RankV2Input) SetTier(v int32)`

SetTier sets Tier field to given value.


### GetName

`func (o *RankV2Input) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *RankV2Input) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *RankV2Input) SetName(v string)`

SetName sets Name field to given value.


### GetImages

`func (o *RankV2Input) GetImages() RankImagesV2`

GetImages returns the Images field if non-nil, zero value otherwise.

### GetImagesOk

`func (o *RankV2Input) GetImagesOk() (*RankImagesV2, bool)`

GetImagesOk returns a tuple with the Images field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImages

`func (o *RankV2Input) SetImages(v RankImagesV2)`

SetImages sets Images field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


