# MMRHistory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **int32** |  | 
**Division** | **int32** | Extracted from the rank the division (rank // 10) | 
**DivisionTier** | **int32** | Extracted from the rank the division tier (rank % 10) | 
**MatchId** | **int64** |  | 
**PlayerScore** | **float64** | Player Score is the index for the rank array (internally used for the rank regression) | 
**Rank** | **int32** | The Player Rank. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
**StartTime** | **int32** | Start time of the match | 

## Methods

### NewMMRHistory

`func NewMMRHistory(accountId int32, division int32, divisionTier int32, matchId int64, playerScore float64, rank int32, startTime int32, ) *MMRHistory`

NewMMRHistory instantiates a new MMRHistory object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMMRHistoryWithDefaults

`func NewMMRHistoryWithDefaults() *MMRHistory`

NewMMRHistoryWithDefaults instantiates a new MMRHistory object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccountId

`func (o *MMRHistory) GetAccountId() int32`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *MMRHistory) GetAccountIdOk() (*int32, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *MMRHistory) SetAccountId(v int32)`

SetAccountId sets AccountId field to given value.


### GetDivision

`func (o *MMRHistory) GetDivision() int32`

GetDivision returns the Division field if non-nil, zero value otherwise.

### GetDivisionOk

`func (o *MMRHistory) GetDivisionOk() (*int32, bool)`

GetDivisionOk returns a tuple with the Division field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDivision

`func (o *MMRHistory) SetDivision(v int32)`

SetDivision sets Division field to given value.


### GetDivisionTier

`func (o *MMRHistory) GetDivisionTier() int32`

GetDivisionTier returns the DivisionTier field if non-nil, zero value otherwise.

### GetDivisionTierOk

`func (o *MMRHistory) GetDivisionTierOk() (*int32, bool)`

GetDivisionTierOk returns a tuple with the DivisionTier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDivisionTier

`func (o *MMRHistory) SetDivisionTier(v int32)`

SetDivisionTier sets DivisionTier field to given value.


### GetMatchId

`func (o *MMRHistory) GetMatchId() int64`

GetMatchId returns the MatchId field if non-nil, zero value otherwise.

### GetMatchIdOk

`func (o *MMRHistory) GetMatchIdOk() (*int64, bool)`

GetMatchIdOk returns a tuple with the MatchId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchId

`func (o *MMRHistory) SetMatchId(v int64)`

SetMatchId sets MatchId field to given value.


### GetPlayerScore

`func (o *MMRHistory) GetPlayerScore() float64`

GetPlayerScore returns the PlayerScore field if non-nil, zero value otherwise.

### GetPlayerScoreOk

`func (o *MMRHistory) GetPlayerScoreOk() (*float64, bool)`

GetPlayerScoreOk returns a tuple with the PlayerScore field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerScore

`func (o *MMRHistory) SetPlayerScore(v float64)`

SetPlayerScore sets PlayerScore field to given value.


### GetRank

`func (o *MMRHistory) GetRank() int32`

GetRank returns the Rank field if non-nil, zero value otherwise.

### GetRankOk

`func (o *MMRHistory) GetRankOk() (*int32, bool)`

GetRankOk returns a tuple with the Rank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRank

`func (o *MMRHistory) SetRank(v int32)`

SetRank sets Rank field to given value.


### GetStartTime

`func (o *MMRHistory) GetStartTime() int32`

GetStartTime returns the StartTime field if non-nil, zero value otherwise.

### GetStartTimeOk

`func (o *MMRHistory) GetStartTimeOk() (*int32, bool)`

GetStartTimeOk returns a tuple with the StartTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTime

`func (o *MMRHistory) SetStartTime(v int32)`

SetStartTime sets StartTime field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


