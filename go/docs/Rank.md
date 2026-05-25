# Rank

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Color** | **string** |  | 
**Images** | [**RankImages**](RankImages.md) |  | 
**Name** | **string** |  | 
**Tier** | **int32** |  | 

## Methods

### NewRank

`func NewRank(color string, images RankImages, name string, tier int32, ) *Rank`

NewRank instantiates a new Rank object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRankWithDefaults

`func NewRankWithDefaults() *Rank`

NewRankWithDefaults instantiates a new Rank object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetColor

`func (o *Rank) GetColor() string`

GetColor returns the Color field if non-nil, zero value otherwise.

### GetColorOk

`func (o *Rank) GetColorOk() (*string, bool)`

GetColorOk returns a tuple with the Color field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColor

`func (o *Rank) SetColor(v string)`

SetColor sets Color field to given value.


### GetImages

`func (o *Rank) GetImages() RankImages`

GetImages returns the Images field if non-nil, zero value otherwise.

### GetImagesOk

`func (o *Rank) GetImagesOk() (*RankImages, bool)`

GetImagesOk returns a tuple with the Images field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImages

`func (o *Rank) SetImages(v RankImages)`

SetImages sets Images field to given value.


### GetName

`func (o *Rank) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Rank) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Rank) SetName(v string)`

SetName sets Name field to given value.


### GetTier

`func (o *Rank) GetTier() int32`

GetTier returns the Tier field if non-nil, zero value otherwise.

### GetTierOk

`func (o *Rank) GetTierOk() (*int32, bool)`

GetTierOk returns a tuple with the Tier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTier

`func (o *Rank) SetTier(v int32)`

SetTier sets Tier field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


