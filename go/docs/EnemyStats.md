# EnemyStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EnemyId** | **int32** |  | 
**Matches** | **[]int64** |  | 
**MatchesPlayed** | **int64** |  | 
**Wins** | **int64** | The amount of matches won against the enemy. | 

## Methods

### NewEnemyStats

`func NewEnemyStats(enemyId int32, matches []int64, matchesPlayed int64, wins int64, ) *EnemyStats`

NewEnemyStats instantiates a new EnemyStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEnemyStatsWithDefaults

`func NewEnemyStatsWithDefaults() *EnemyStats`

NewEnemyStatsWithDefaults instantiates a new EnemyStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEnemyId

`func (o *EnemyStats) GetEnemyId() int32`

GetEnemyId returns the EnemyId field if non-nil, zero value otherwise.

### GetEnemyIdOk

`func (o *EnemyStats) GetEnemyIdOk() (*int32, bool)`

GetEnemyIdOk returns a tuple with the EnemyId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyId

`func (o *EnemyStats) SetEnemyId(v int32)`

SetEnemyId sets EnemyId field to given value.


### GetMatches

`func (o *EnemyStats) GetMatches() []int64`

GetMatches returns the Matches field if non-nil, zero value otherwise.

### GetMatchesOk

`func (o *EnemyStats) GetMatchesOk() (*[]int64, bool)`

GetMatchesOk returns a tuple with the Matches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatches

`func (o *EnemyStats) SetMatches(v []int64)`

SetMatches sets Matches field to given value.


### GetMatchesPlayed

`func (o *EnemyStats) GetMatchesPlayed() int64`

GetMatchesPlayed returns the MatchesPlayed field if non-nil, zero value otherwise.

### GetMatchesPlayedOk

`func (o *EnemyStats) GetMatchesPlayedOk() (*int64, bool)`

GetMatchesPlayedOk returns a tuple with the MatchesPlayed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchesPlayed

`func (o *EnemyStats) SetMatchesPlayed(v int64)`

SetMatchesPlayed sets MatchesPlayed field to given value.


### GetWins

`func (o *EnemyStats) GetWins() int64`

GetWins returns the Wins field if non-nil, zero value otherwise.

### GetWinsOk

`func (o *EnemyStats) GetWinsOk() (*int64, bool)`

GetWinsOk returns a tuple with the Wins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWins

`func (o *EnemyStats) SetWins(v int64)`

SetWins sets Wins field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


