# LastRankedMatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MatchId** | **int64** |  | 
**PlayerRankConsumedDemotionProtection** | Pointer to **NullableBool** | Whether the match used up one of the player&#39;s demotion protection games. | [optional] 
**PlayerRankDesiredProgressChange** | Pointer to **NullableInt32** | Progress change the match was supposed to award, before demotion protection is applied. | [optional] 
**PlayerRankFinalFlatProgress** | Pointer to **NullableInt64** | Rank progress the player ended the match with. | [optional] 
**PlayerRankInitialCalibrationGames** | Pointer to **NullableInt64** | Remaining placement games at the start of the match. | [optional] 
**PlayerRankInitialDemotionProtectionGames** | Pointer to **NullableInt64** | Remaining demotion protection games at the start of the match. | [optional] 
**PlayerRankInitialDisplayRank** | **int64** | Rank badge the player entered the match with, &#x60;tier * 10 + subrank&#x60;. | 
**PlayerRankInitialFlatProgress** | Pointer to **NullableInt64** | Rank progress the player entered the match with. | [optional] 
**PlayerRankInitialWinStreak** | Pointer to **NullableInt64** | Win streak the player entered the match with. | [optional] 
**RankInterval** | Pointer to **NullableInt64** | Ranked interval the match counted for, which sets the scale of the flat progress. See &lt;https://api.deadlock-api.com/v1/assets/ranked-seasons&gt;. &#x60;null&#x60; for matches before 2026-11-05 19:00 UTC, which are all interval 1. | [optional] 
**StartTime** | **int64** | Match start time as a unix timestamp. | 

## Methods

### NewLastRankedMatch

`func NewLastRankedMatch(matchId int64, playerRankInitialDisplayRank int64, startTime int64, ) *LastRankedMatch`

NewLastRankedMatch instantiates a new LastRankedMatch object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewLastRankedMatchWithDefaults

`func NewLastRankedMatchWithDefaults() *LastRankedMatch`

NewLastRankedMatchWithDefaults instantiates a new LastRankedMatch object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMatchId

`func (o *LastRankedMatch) GetMatchId() int64`

GetMatchId returns the MatchId field if non-nil, zero value otherwise.

### GetMatchIdOk

`func (o *LastRankedMatch) GetMatchIdOk() (*int64, bool)`

GetMatchIdOk returns a tuple with the MatchId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchId

`func (o *LastRankedMatch) SetMatchId(v int64)`

SetMatchId sets MatchId field to given value.


### GetPlayerRankConsumedDemotionProtection

`func (o *LastRankedMatch) GetPlayerRankConsumedDemotionProtection() bool`

GetPlayerRankConsumedDemotionProtection returns the PlayerRankConsumedDemotionProtection field if non-nil, zero value otherwise.

### GetPlayerRankConsumedDemotionProtectionOk

`func (o *LastRankedMatch) GetPlayerRankConsumedDemotionProtectionOk() (*bool, bool)`

GetPlayerRankConsumedDemotionProtectionOk returns a tuple with the PlayerRankConsumedDemotionProtection field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerRankConsumedDemotionProtection

`func (o *LastRankedMatch) SetPlayerRankConsumedDemotionProtection(v bool)`

SetPlayerRankConsumedDemotionProtection sets PlayerRankConsumedDemotionProtection field to given value.

### HasPlayerRankConsumedDemotionProtection

`func (o *LastRankedMatch) HasPlayerRankConsumedDemotionProtection() bool`

HasPlayerRankConsumedDemotionProtection returns a boolean if a field has been set.

### SetPlayerRankConsumedDemotionProtectionNil

`func (o *LastRankedMatch) SetPlayerRankConsumedDemotionProtectionNil(b bool)`

 SetPlayerRankConsumedDemotionProtectionNil sets the value for PlayerRankConsumedDemotionProtection to be an explicit nil

### UnsetPlayerRankConsumedDemotionProtection
`func (o *LastRankedMatch) UnsetPlayerRankConsumedDemotionProtection()`

UnsetPlayerRankConsumedDemotionProtection ensures that no value is present for PlayerRankConsumedDemotionProtection, not even an explicit nil
### GetPlayerRankDesiredProgressChange

`func (o *LastRankedMatch) GetPlayerRankDesiredProgressChange() int32`

GetPlayerRankDesiredProgressChange returns the PlayerRankDesiredProgressChange field if non-nil, zero value otherwise.

### GetPlayerRankDesiredProgressChangeOk

`func (o *LastRankedMatch) GetPlayerRankDesiredProgressChangeOk() (*int32, bool)`

GetPlayerRankDesiredProgressChangeOk returns a tuple with the PlayerRankDesiredProgressChange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerRankDesiredProgressChange

`func (o *LastRankedMatch) SetPlayerRankDesiredProgressChange(v int32)`

SetPlayerRankDesiredProgressChange sets PlayerRankDesiredProgressChange field to given value.

### HasPlayerRankDesiredProgressChange

`func (o *LastRankedMatch) HasPlayerRankDesiredProgressChange() bool`

HasPlayerRankDesiredProgressChange returns a boolean if a field has been set.

### SetPlayerRankDesiredProgressChangeNil

`func (o *LastRankedMatch) SetPlayerRankDesiredProgressChangeNil(b bool)`

 SetPlayerRankDesiredProgressChangeNil sets the value for PlayerRankDesiredProgressChange to be an explicit nil

### UnsetPlayerRankDesiredProgressChange
`func (o *LastRankedMatch) UnsetPlayerRankDesiredProgressChange()`

UnsetPlayerRankDesiredProgressChange ensures that no value is present for PlayerRankDesiredProgressChange, not even an explicit nil
### GetPlayerRankFinalFlatProgress

`func (o *LastRankedMatch) GetPlayerRankFinalFlatProgress() int64`

GetPlayerRankFinalFlatProgress returns the PlayerRankFinalFlatProgress field if non-nil, zero value otherwise.

### GetPlayerRankFinalFlatProgressOk

`func (o *LastRankedMatch) GetPlayerRankFinalFlatProgressOk() (*int64, bool)`

GetPlayerRankFinalFlatProgressOk returns a tuple with the PlayerRankFinalFlatProgress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerRankFinalFlatProgress

`func (o *LastRankedMatch) SetPlayerRankFinalFlatProgress(v int64)`

SetPlayerRankFinalFlatProgress sets PlayerRankFinalFlatProgress field to given value.

### HasPlayerRankFinalFlatProgress

`func (o *LastRankedMatch) HasPlayerRankFinalFlatProgress() bool`

HasPlayerRankFinalFlatProgress returns a boolean if a field has been set.

### SetPlayerRankFinalFlatProgressNil

`func (o *LastRankedMatch) SetPlayerRankFinalFlatProgressNil(b bool)`

 SetPlayerRankFinalFlatProgressNil sets the value for PlayerRankFinalFlatProgress to be an explicit nil

### UnsetPlayerRankFinalFlatProgress
`func (o *LastRankedMatch) UnsetPlayerRankFinalFlatProgress()`

UnsetPlayerRankFinalFlatProgress ensures that no value is present for PlayerRankFinalFlatProgress, not even an explicit nil
### GetPlayerRankInitialCalibrationGames

`func (o *LastRankedMatch) GetPlayerRankInitialCalibrationGames() int64`

GetPlayerRankInitialCalibrationGames returns the PlayerRankInitialCalibrationGames field if non-nil, zero value otherwise.

### GetPlayerRankInitialCalibrationGamesOk

`func (o *LastRankedMatch) GetPlayerRankInitialCalibrationGamesOk() (*int64, bool)`

GetPlayerRankInitialCalibrationGamesOk returns a tuple with the PlayerRankInitialCalibrationGames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerRankInitialCalibrationGames

`func (o *LastRankedMatch) SetPlayerRankInitialCalibrationGames(v int64)`

SetPlayerRankInitialCalibrationGames sets PlayerRankInitialCalibrationGames field to given value.

### HasPlayerRankInitialCalibrationGames

`func (o *LastRankedMatch) HasPlayerRankInitialCalibrationGames() bool`

HasPlayerRankInitialCalibrationGames returns a boolean if a field has been set.

### SetPlayerRankInitialCalibrationGamesNil

`func (o *LastRankedMatch) SetPlayerRankInitialCalibrationGamesNil(b bool)`

 SetPlayerRankInitialCalibrationGamesNil sets the value for PlayerRankInitialCalibrationGames to be an explicit nil

### UnsetPlayerRankInitialCalibrationGames
`func (o *LastRankedMatch) UnsetPlayerRankInitialCalibrationGames()`

UnsetPlayerRankInitialCalibrationGames ensures that no value is present for PlayerRankInitialCalibrationGames, not even an explicit nil
### GetPlayerRankInitialDemotionProtectionGames

`func (o *LastRankedMatch) GetPlayerRankInitialDemotionProtectionGames() int64`

GetPlayerRankInitialDemotionProtectionGames returns the PlayerRankInitialDemotionProtectionGames field if non-nil, zero value otherwise.

### GetPlayerRankInitialDemotionProtectionGamesOk

`func (o *LastRankedMatch) GetPlayerRankInitialDemotionProtectionGamesOk() (*int64, bool)`

GetPlayerRankInitialDemotionProtectionGamesOk returns a tuple with the PlayerRankInitialDemotionProtectionGames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerRankInitialDemotionProtectionGames

`func (o *LastRankedMatch) SetPlayerRankInitialDemotionProtectionGames(v int64)`

SetPlayerRankInitialDemotionProtectionGames sets PlayerRankInitialDemotionProtectionGames field to given value.

### HasPlayerRankInitialDemotionProtectionGames

`func (o *LastRankedMatch) HasPlayerRankInitialDemotionProtectionGames() bool`

HasPlayerRankInitialDemotionProtectionGames returns a boolean if a field has been set.

### SetPlayerRankInitialDemotionProtectionGamesNil

`func (o *LastRankedMatch) SetPlayerRankInitialDemotionProtectionGamesNil(b bool)`

 SetPlayerRankInitialDemotionProtectionGamesNil sets the value for PlayerRankInitialDemotionProtectionGames to be an explicit nil

### UnsetPlayerRankInitialDemotionProtectionGames
`func (o *LastRankedMatch) UnsetPlayerRankInitialDemotionProtectionGames()`

UnsetPlayerRankInitialDemotionProtectionGames ensures that no value is present for PlayerRankInitialDemotionProtectionGames, not even an explicit nil
### GetPlayerRankInitialDisplayRank

`func (o *LastRankedMatch) GetPlayerRankInitialDisplayRank() int64`

GetPlayerRankInitialDisplayRank returns the PlayerRankInitialDisplayRank field if non-nil, zero value otherwise.

### GetPlayerRankInitialDisplayRankOk

`func (o *LastRankedMatch) GetPlayerRankInitialDisplayRankOk() (*int64, bool)`

GetPlayerRankInitialDisplayRankOk returns a tuple with the PlayerRankInitialDisplayRank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerRankInitialDisplayRank

`func (o *LastRankedMatch) SetPlayerRankInitialDisplayRank(v int64)`

SetPlayerRankInitialDisplayRank sets PlayerRankInitialDisplayRank field to given value.


### GetPlayerRankInitialFlatProgress

`func (o *LastRankedMatch) GetPlayerRankInitialFlatProgress() int64`

GetPlayerRankInitialFlatProgress returns the PlayerRankInitialFlatProgress field if non-nil, zero value otherwise.

### GetPlayerRankInitialFlatProgressOk

`func (o *LastRankedMatch) GetPlayerRankInitialFlatProgressOk() (*int64, bool)`

GetPlayerRankInitialFlatProgressOk returns a tuple with the PlayerRankInitialFlatProgress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerRankInitialFlatProgress

`func (o *LastRankedMatch) SetPlayerRankInitialFlatProgress(v int64)`

SetPlayerRankInitialFlatProgress sets PlayerRankInitialFlatProgress field to given value.

### HasPlayerRankInitialFlatProgress

`func (o *LastRankedMatch) HasPlayerRankInitialFlatProgress() bool`

HasPlayerRankInitialFlatProgress returns a boolean if a field has been set.

### SetPlayerRankInitialFlatProgressNil

`func (o *LastRankedMatch) SetPlayerRankInitialFlatProgressNil(b bool)`

 SetPlayerRankInitialFlatProgressNil sets the value for PlayerRankInitialFlatProgress to be an explicit nil

### UnsetPlayerRankInitialFlatProgress
`func (o *LastRankedMatch) UnsetPlayerRankInitialFlatProgress()`

UnsetPlayerRankInitialFlatProgress ensures that no value is present for PlayerRankInitialFlatProgress, not even an explicit nil
### GetPlayerRankInitialWinStreak

`func (o *LastRankedMatch) GetPlayerRankInitialWinStreak() int64`

GetPlayerRankInitialWinStreak returns the PlayerRankInitialWinStreak field if non-nil, zero value otherwise.

### GetPlayerRankInitialWinStreakOk

`func (o *LastRankedMatch) GetPlayerRankInitialWinStreakOk() (*int64, bool)`

GetPlayerRankInitialWinStreakOk returns a tuple with the PlayerRankInitialWinStreak field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerRankInitialWinStreak

`func (o *LastRankedMatch) SetPlayerRankInitialWinStreak(v int64)`

SetPlayerRankInitialWinStreak sets PlayerRankInitialWinStreak field to given value.

### HasPlayerRankInitialWinStreak

`func (o *LastRankedMatch) HasPlayerRankInitialWinStreak() bool`

HasPlayerRankInitialWinStreak returns a boolean if a field has been set.

### SetPlayerRankInitialWinStreakNil

`func (o *LastRankedMatch) SetPlayerRankInitialWinStreakNil(b bool)`

 SetPlayerRankInitialWinStreakNil sets the value for PlayerRankInitialWinStreak to be an explicit nil

### UnsetPlayerRankInitialWinStreak
`func (o *LastRankedMatch) UnsetPlayerRankInitialWinStreak()`

UnsetPlayerRankInitialWinStreak ensures that no value is present for PlayerRankInitialWinStreak, not even an explicit nil
### GetRankInterval

`func (o *LastRankedMatch) GetRankInterval() int64`

GetRankInterval returns the RankInterval field if non-nil, zero value otherwise.

### GetRankIntervalOk

`func (o *LastRankedMatch) GetRankIntervalOk() (*int64, bool)`

GetRankIntervalOk returns a tuple with the RankInterval field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRankInterval

`func (o *LastRankedMatch) SetRankInterval(v int64)`

SetRankInterval sets RankInterval field to given value.

### HasRankInterval

`func (o *LastRankedMatch) HasRankInterval() bool`

HasRankInterval returns a boolean if a field has been set.

### SetRankIntervalNil

`func (o *LastRankedMatch) SetRankIntervalNil(b bool)`

 SetRankIntervalNil sets the value for RankInterval to be an explicit nil

### UnsetRankInterval
`func (o *LastRankedMatch) UnsetRankInterval()`

UnsetRankInterval ensures that no value is present for RankInterval, not even an explicit nil
### GetStartTime

`func (o *LastRankedMatch) GetStartTime() int64`

GetStartTime returns the StartTime field if non-nil, zero value otherwise.

### GetStartTimeOk

`func (o *LastRankedMatch) GetStartTimeOk() (*int64, bool)`

GetStartTimeOk returns a tuple with the StartTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTime

`func (o *LastRankedMatch) SetStartTime(v int64)`

SetStartTime sets StartTime field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


