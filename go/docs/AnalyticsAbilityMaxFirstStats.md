# AnalyticsAbilityMaxFirstStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AbilityId** | Pointer to **NullableInt32** | The ability these players maxed first (unlocked and upgraded three times before any other), null for the players who maxed none. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [optional] 
**Losses** | **int64** |  | 
**Matches** | **int64** |  | 
**Players** | **int64** | Distinct players, counted exactly. | 
**Wins** | **int64** |  | 

## Methods

### NewAnalyticsAbilityMaxFirstStats

`func NewAnalyticsAbilityMaxFirstStats(losses int64, matches int64, players int64, wins int64, ) *AnalyticsAbilityMaxFirstStats`

NewAnalyticsAbilityMaxFirstStats instantiates a new AnalyticsAbilityMaxFirstStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAnalyticsAbilityMaxFirstStatsWithDefaults

`func NewAnalyticsAbilityMaxFirstStatsWithDefaults() *AnalyticsAbilityMaxFirstStats`

NewAnalyticsAbilityMaxFirstStatsWithDefaults instantiates a new AnalyticsAbilityMaxFirstStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAbilityId

`func (o *AnalyticsAbilityMaxFirstStats) GetAbilityId() int32`

GetAbilityId returns the AbilityId field if non-nil, zero value otherwise.

### GetAbilityIdOk

`func (o *AnalyticsAbilityMaxFirstStats) GetAbilityIdOk() (*int32, bool)`

GetAbilityIdOk returns a tuple with the AbilityId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAbilityId

`func (o *AnalyticsAbilityMaxFirstStats) SetAbilityId(v int32)`

SetAbilityId sets AbilityId field to given value.

### HasAbilityId

`func (o *AnalyticsAbilityMaxFirstStats) HasAbilityId() bool`

HasAbilityId returns a boolean if a field has been set.

### SetAbilityIdNil

`func (o *AnalyticsAbilityMaxFirstStats) SetAbilityIdNil(b bool)`

 SetAbilityIdNil sets the value for AbilityId to be an explicit nil

### UnsetAbilityId
`func (o *AnalyticsAbilityMaxFirstStats) UnsetAbilityId()`

UnsetAbilityId ensures that no value is present for AbilityId, not even an explicit nil
### GetLosses

`func (o *AnalyticsAbilityMaxFirstStats) GetLosses() int64`

GetLosses returns the Losses field if non-nil, zero value otherwise.

### GetLossesOk

`func (o *AnalyticsAbilityMaxFirstStats) GetLossesOk() (*int64, bool)`

GetLossesOk returns a tuple with the Losses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLosses

`func (o *AnalyticsAbilityMaxFirstStats) SetLosses(v int64)`

SetLosses sets Losses field to given value.


### GetMatches

`func (o *AnalyticsAbilityMaxFirstStats) GetMatches() int64`

GetMatches returns the Matches field if non-nil, zero value otherwise.

### GetMatchesOk

`func (o *AnalyticsAbilityMaxFirstStats) GetMatchesOk() (*int64, bool)`

GetMatchesOk returns a tuple with the Matches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatches

`func (o *AnalyticsAbilityMaxFirstStats) SetMatches(v int64)`

SetMatches sets Matches field to given value.


### GetPlayers

`func (o *AnalyticsAbilityMaxFirstStats) GetPlayers() int64`

GetPlayers returns the Players field if non-nil, zero value otherwise.

### GetPlayersOk

`func (o *AnalyticsAbilityMaxFirstStats) GetPlayersOk() (*int64, bool)`

GetPlayersOk returns a tuple with the Players field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayers

`func (o *AnalyticsAbilityMaxFirstStats) SetPlayers(v int64)`

SetPlayers sets Players field to given value.


### GetWins

`func (o *AnalyticsAbilityMaxFirstStats) GetWins() int64`

GetWins returns the Wins field if non-nil, zero value otherwise.

### GetWinsOk

`func (o *AnalyticsAbilityMaxFirstStats) GetWinsOk() (*int64, bool)`

GetWinsOk returns a tuple with the Wins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWins

`func (o *AnalyticsAbilityMaxFirstStats) SetWins(v int64)`

SetWins sets Wins field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


