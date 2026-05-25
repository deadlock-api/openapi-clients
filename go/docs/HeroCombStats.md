# HeroCombStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**HeroIds** | **[]int32** | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**Losses** | **int64** |  | 
**Matches** | **int64** |  | 
**Wins** | **int64** |  | 

## Methods

### NewHeroCombStats

`func NewHeroCombStats(heroIds []int32, losses int64, matches int64, wins int64, ) *HeroCombStats`

NewHeroCombStats instantiates a new HeroCombStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHeroCombStatsWithDefaults

`func NewHeroCombStatsWithDefaults() *HeroCombStats`

NewHeroCombStatsWithDefaults instantiates a new HeroCombStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetHeroIds

`func (o *HeroCombStats) GetHeroIds() []int32`

GetHeroIds returns the HeroIds field if non-nil, zero value otherwise.

### GetHeroIdsOk

`func (o *HeroCombStats) GetHeroIdsOk() (*[]int32, bool)`

GetHeroIdsOk returns a tuple with the HeroIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroIds

`func (o *HeroCombStats) SetHeroIds(v []int32)`

SetHeroIds sets HeroIds field to given value.


### GetLosses

`func (o *HeroCombStats) GetLosses() int64`

GetLosses returns the Losses field if non-nil, zero value otherwise.

### GetLossesOk

`func (o *HeroCombStats) GetLossesOk() (*int64, bool)`

GetLossesOk returns a tuple with the Losses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLosses

`func (o *HeroCombStats) SetLosses(v int64)`

SetLosses sets Losses field to given value.


### GetMatches

`func (o *HeroCombStats) GetMatches() int64`

GetMatches returns the Matches field if non-nil, zero value otherwise.

### GetMatchesOk

`func (o *HeroCombStats) GetMatchesOk() (*int64, bool)`

GetMatchesOk returns a tuple with the Matches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatches

`func (o *HeroCombStats) SetMatches(v int64)`

SetMatches sets Matches field to given value.


### GetWins

`func (o *HeroCombStats) GetWins() int64`

GetWins returns the Wins field if non-nil, zero value otherwise.

### GetWinsOk

`func (o *HeroCombStats) GetWinsOk() (*int64, bool)`

GetWinsOk returns a tuple with the Wins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWins

`func (o *HeroCombStats) SetWins(v int64)`

SetWins sets Wins field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


