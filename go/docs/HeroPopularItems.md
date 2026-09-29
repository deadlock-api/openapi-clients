# HeroPopularItems

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EarlyGame** | [**[]HeroPopularItem**](HeroPopularItem.md) |  | 
**LateGame** | [**[]HeroPopularItem**](HeroPopularItem.md) |  | 
**MidGame** | [**[]HeroPopularItem**](HeroPopularItem.md) |  | 
**Timestamp** | Pointer to **NullableInt64** | Unix timestamp (seconds) at which Valve generated the data. | [optional] 

## Methods

### NewHeroPopularItems

`func NewHeroPopularItems(earlyGame []HeroPopularItem, lateGame []HeroPopularItem, midGame []HeroPopularItem, ) *HeroPopularItems`

NewHeroPopularItems instantiates a new HeroPopularItems object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHeroPopularItemsWithDefaults

`func NewHeroPopularItemsWithDefaults() *HeroPopularItems`

NewHeroPopularItemsWithDefaults instantiates a new HeroPopularItems object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEarlyGame

`func (o *HeroPopularItems) GetEarlyGame() []HeroPopularItem`

GetEarlyGame returns the EarlyGame field if non-nil, zero value otherwise.

### GetEarlyGameOk

`func (o *HeroPopularItems) GetEarlyGameOk() (*[]HeroPopularItem, bool)`

GetEarlyGameOk returns a tuple with the EarlyGame field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEarlyGame

`func (o *HeroPopularItems) SetEarlyGame(v []HeroPopularItem)`

SetEarlyGame sets EarlyGame field to given value.


### GetLateGame

`func (o *HeroPopularItems) GetLateGame() []HeroPopularItem`

GetLateGame returns the LateGame field if non-nil, zero value otherwise.

### GetLateGameOk

`func (o *HeroPopularItems) GetLateGameOk() (*[]HeroPopularItem, bool)`

GetLateGameOk returns a tuple with the LateGame field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLateGame

`func (o *HeroPopularItems) SetLateGame(v []HeroPopularItem)`

SetLateGame sets LateGame field to given value.


### GetMidGame

`func (o *HeroPopularItems) GetMidGame() []HeroPopularItem`

GetMidGame returns the MidGame field if non-nil, zero value otherwise.

### GetMidGameOk

`func (o *HeroPopularItems) GetMidGameOk() (*[]HeroPopularItem, bool)`

GetMidGameOk returns a tuple with the MidGame field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMidGame

`func (o *HeroPopularItems) SetMidGame(v []HeroPopularItem)`

SetMidGame sets MidGame field to given value.


### GetTimestamp

`func (o *HeroPopularItems) GetTimestamp() int64`

GetTimestamp returns the Timestamp field if non-nil, zero value otherwise.

### GetTimestampOk

`func (o *HeroPopularItems) GetTimestampOk() (*int64, bool)`

GetTimestampOk returns a tuple with the Timestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimestamp

`func (o *HeroPopularItems) SetTimestamp(v int64)`

SetTimestamp sets Timestamp field to given value.

### HasTimestamp

`func (o *HeroPopularItems) HasTimestamp() bool`

HasTimestamp returns a boolean if a field has been set.

### SetTimestampNil

`func (o *HeroPopularItems) SetTimestampNil(b bool)`

 SetTimestampNil sets the value for Timestamp to be an explicit nil

### UnsetTimestamp
`func (o *HeroPopularItems) UnsetTimestamp()`

UnsetTimestamp ensures that no value is present for Timestamp, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


