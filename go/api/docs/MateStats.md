# MateStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Matches** | **[]int64** |  | 
**MatchesPlayed** | **int64** |  | 
**MateId** | **int32** |  | 
**Wins** | **int64** |  | 

## Methods

### NewMateStats

`func NewMateStats(matches []int64, matchesPlayed int64, mateId int32, wins int64, ) *MateStats`

NewMateStats instantiates a new MateStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMateStatsWithDefaults

`func NewMateStatsWithDefaults() *MateStats`

NewMateStatsWithDefaults instantiates a new MateStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMatches

`func (o *MateStats) GetMatches() []int64`

GetMatches returns the Matches field if non-nil, zero value otherwise.

### GetMatchesOk

`func (o *MateStats) GetMatchesOk() (*[]int64, bool)`

GetMatchesOk returns a tuple with the Matches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatches

`func (o *MateStats) SetMatches(v []int64)`

SetMatches sets Matches field to given value.


### GetMatchesPlayed

`func (o *MateStats) GetMatchesPlayed() int64`

GetMatchesPlayed returns the MatchesPlayed field if non-nil, zero value otherwise.

### GetMatchesPlayedOk

`func (o *MateStats) GetMatchesPlayedOk() (*int64, bool)`

GetMatchesPlayedOk returns a tuple with the MatchesPlayed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchesPlayed

`func (o *MateStats) SetMatchesPlayed(v int64)`

SetMatchesPlayed sets MatchesPlayed field to given value.


### GetMateId

`func (o *MateStats) GetMateId() int32`

GetMateId returns the MateId field if non-nil, zero value otherwise.

### GetMateIdOk

`func (o *MateStats) GetMateIdOk() (*int32, bool)`

GetMateIdOk returns a tuple with the MateId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMateId

`func (o *MateStats) SetMateId(v int32)`

SetMateId sets MateId field to given value.


### GetWins

`func (o *MateStats) GetWins() int64`

GetWins returns the Wins field if non-nil, zero value otherwise.

### GetWinsOk

`func (o *MateStats) GetWinsOk() (*int64, bool)`

GetWinsOk returns a tuple with the Wins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWins

`func (o *MateStats) SetWins(v int64)`

SetWins sets Wins field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


