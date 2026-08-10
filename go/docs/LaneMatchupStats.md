# LaneMatchupStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AssignedLane** | **int32** | The lane the matchup was played in. See the &#x60;lane_info&#x60; array of &lt;https://api.deadlock-api.com/v1/assets/generic-data&gt;. | 
**EnemyHeroIds** | **[]int32** | The ascending hero id pair they laned against. | 
**HeroIds** | **[]int32** | The ascending hero id pair that shared the lane. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**MatchesPlayed** | **int64** | The total number of lane matchups between &#x60;hero_ids&#x60; and &#x60;enemy_hero_ids&#x60; in this lane. | 
**NetWorthDiff15min** | **float64** | Mean souls the duo is ahead by 15 minutes in, against that duo. Negative means behind. &#x60;0&#x60; when no counted matchup had net-worth samples for all four players. | 
**NetWorthMatches** | **int64** | How many of &#x60;matches_played&#x60; carried net-worth samples for all four players. | 
**Wins** | **int64** | The number of matches &#x60;hero_ids&#x60; won against &#x60;enemy_hero_ids&#x60; in this lane. | 

## Methods

### NewLaneMatchupStats

`func NewLaneMatchupStats(assignedLane int32, enemyHeroIds []int32, heroIds []int32, matchesPlayed int64, netWorthDiff15min float64, netWorthMatches int64, wins int64, ) *LaneMatchupStats`

NewLaneMatchupStats instantiates a new LaneMatchupStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewLaneMatchupStatsWithDefaults

`func NewLaneMatchupStatsWithDefaults() *LaneMatchupStats`

NewLaneMatchupStatsWithDefaults instantiates a new LaneMatchupStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAssignedLane

`func (o *LaneMatchupStats) GetAssignedLane() int32`

GetAssignedLane returns the AssignedLane field if non-nil, zero value otherwise.

### GetAssignedLaneOk

`func (o *LaneMatchupStats) GetAssignedLaneOk() (*int32, bool)`

GetAssignedLaneOk returns a tuple with the AssignedLane field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssignedLane

`func (o *LaneMatchupStats) SetAssignedLane(v int32)`

SetAssignedLane sets AssignedLane field to given value.


### GetEnemyHeroIds

`func (o *LaneMatchupStats) GetEnemyHeroIds() []int32`

GetEnemyHeroIds returns the EnemyHeroIds field if non-nil, zero value otherwise.

### GetEnemyHeroIdsOk

`func (o *LaneMatchupStats) GetEnemyHeroIdsOk() (*[]int32, bool)`

GetEnemyHeroIdsOk returns a tuple with the EnemyHeroIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyHeroIds

`func (o *LaneMatchupStats) SetEnemyHeroIds(v []int32)`

SetEnemyHeroIds sets EnemyHeroIds field to given value.


### GetHeroIds

`func (o *LaneMatchupStats) GetHeroIds() []int32`

GetHeroIds returns the HeroIds field if non-nil, zero value otherwise.

### GetHeroIdsOk

`func (o *LaneMatchupStats) GetHeroIdsOk() (*[]int32, bool)`

GetHeroIdsOk returns a tuple with the HeroIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroIds

`func (o *LaneMatchupStats) SetHeroIds(v []int32)`

SetHeroIds sets HeroIds field to given value.


### GetMatchesPlayed

`func (o *LaneMatchupStats) GetMatchesPlayed() int64`

GetMatchesPlayed returns the MatchesPlayed field if non-nil, zero value otherwise.

### GetMatchesPlayedOk

`func (o *LaneMatchupStats) GetMatchesPlayedOk() (*int64, bool)`

GetMatchesPlayedOk returns a tuple with the MatchesPlayed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchesPlayed

`func (o *LaneMatchupStats) SetMatchesPlayed(v int64)`

SetMatchesPlayed sets MatchesPlayed field to given value.


### GetNetWorthDiff15min

`func (o *LaneMatchupStats) GetNetWorthDiff15min() float64`

GetNetWorthDiff15min returns the NetWorthDiff15min field if non-nil, zero value otherwise.

### GetNetWorthDiff15minOk

`func (o *LaneMatchupStats) GetNetWorthDiff15minOk() (*float64, bool)`

GetNetWorthDiff15minOk returns a tuple with the NetWorthDiff15min field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetWorthDiff15min

`func (o *LaneMatchupStats) SetNetWorthDiff15min(v float64)`

SetNetWorthDiff15min sets NetWorthDiff15min field to given value.


### GetNetWorthMatches

`func (o *LaneMatchupStats) GetNetWorthMatches() int64`

GetNetWorthMatches returns the NetWorthMatches field if non-nil, zero value otherwise.

### GetNetWorthMatchesOk

`func (o *LaneMatchupStats) GetNetWorthMatchesOk() (*int64, bool)`

GetNetWorthMatchesOk returns a tuple with the NetWorthMatches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetWorthMatches

`func (o *LaneMatchupStats) SetNetWorthMatches(v int64)`

SetNetWorthMatches sets NetWorthMatches field to given value.


### GetWins

`func (o *LaneMatchupStats) GetWins() int64`

GetWins returns the Wins field if non-nil, zero value otherwise.

### GetWinsOk

`func (o *LaneMatchupStats) GetWinsOk() (*int64, bool)`

GetWinsOk returns a tuple with the Wins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWins

`func (o *LaneMatchupStats) SetWins(v int64)`

SetWins sets Wins field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


