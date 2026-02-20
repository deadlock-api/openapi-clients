# PlayerAccountHeroStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**HeroId** | Pointer to **NullableInt32** |  | [optional] 
**MedalsBronze** | **[]int32** |  | 
**MedalsGold** | **[]int32** |  | 
**MedalsSilver** | **[]int32** |  | 
**StatId** | **[]int32** |  | 
**TotalValue** | **[]int64** |  | 

## Methods

### NewPlayerAccountHeroStats

`func NewPlayerAccountHeroStats(medalsBronze []int32, medalsGold []int32, medalsSilver []int32, statId []int32, totalValue []int64, ) *PlayerAccountHeroStats`

NewPlayerAccountHeroStats instantiates a new PlayerAccountHeroStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPlayerAccountHeroStatsWithDefaults

`func NewPlayerAccountHeroStatsWithDefaults() *PlayerAccountHeroStats`

NewPlayerAccountHeroStatsWithDefaults instantiates a new PlayerAccountHeroStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetHeroId

`func (o *PlayerAccountHeroStats) GetHeroId() int32`

GetHeroId returns the HeroId field if non-nil, zero value otherwise.

### GetHeroIdOk

`func (o *PlayerAccountHeroStats) GetHeroIdOk() (*int32, bool)`

GetHeroIdOk returns a tuple with the HeroId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroId

`func (o *PlayerAccountHeroStats) SetHeroId(v int32)`

SetHeroId sets HeroId field to given value.

### HasHeroId

`func (o *PlayerAccountHeroStats) HasHeroId() bool`

HasHeroId returns a boolean if a field has been set.

### SetHeroIdNil

`func (o *PlayerAccountHeroStats) SetHeroIdNil(b bool)`

 SetHeroIdNil sets the value for HeroId to be an explicit nil

### UnsetHeroId
`func (o *PlayerAccountHeroStats) UnsetHeroId()`

UnsetHeroId ensures that no value is present for HeroId, not even an explicit nil
### GetMedalsBronze

`func (o *PlayerAccountHeroStats) GetMedalsBronze() []int32`

GetMedalsBronze returns the MedalsBronze field if non-nil, zero value otherwise.

### GetMedalsBronzeOk

`func (o *PlayerAccountHeroStats) GetMedalsBronzeOk() (*[]int32, bool)`

GetMedalsBronzeOk returns a tuple with the MedalsBronze field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMedalsBronze

`func (o *PlayerAccountHeroStats) SetMedalsBronze(v []int32)`

SetMedalsBronze sets MedalsBronze field to given value.


### GetMedalsGold

`func (o *PlayerAccountHeroStats) GetMedalsGold() []int32`

GetMedalsGold returns the MedalsGold field if non-nil, zero value otherwise.

### GetMedalsGoldOk

`func (o *PlayerAccountHeroStats) GetMedalsGoldOk() (*[]int32, bool)`

GetMedalsGoldOk returns a tuple with the MedalsGold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMedalsGold

`func (o *PlayerAccountHeroStats) SetMedalsGold(v []int32)`

SetMedalsGold sets MedalsGold field to given value.


### GetMedalsSilver

`func (o *PlayerAccountHeroStats) GetMedalsSilver() []int32`

GetMedalsSilver returns the MedalsSilver field if non-nil, zero value otherwise.

### GetMedalsSilverOk

`func (o *PlayerAccountHeroStats) GetMedalsSilverOk() (*[]int32, bool)`

GetMedalsSilverOk returns a tuple with the MedalsSilver field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMedalsSilver

`func (o *PlayerAccountHeroStats) SetMedalsSilver(v []int32)`

SetMedalsSilver sets MedalsSilver field to given value.


### GetStatId

`func (o *PlayerAccountHeroStats) GetStatId() []int32`

GetStatId returns the StatId field if non-nil, zero value otherwise.

### GetStatIdOk

`func (o *PlayerAccountHeroStats) GetStatIdOk() (*[]int32, bool)`

GetStatIdOk returns a tuple with the StatId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatId

`func (o *PlayerAccountHeroStats) SetStatId(v []int32)`

SetStatId sets StatId field to given value.


### GetTotalValue

`func (o *PlayerAccountHeroStats) GetTotalValue() []int64`

GetTotalValue returns the TotalValue field if non-nil, zero value otherwise.

### GetTotalValueOk

`func (o *PlayerAccountHeroStats) GetTotalValueOk() (*[]int64, bool)`

GetTotalValueOk returns a tuple with the TotalValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalValue

`func (o *PlayerAccountHeroStats) SetTotalValue(v []int64)`

SetTotalValue sets TotalValue field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


