# RankedSeason

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BaseWinLossPointGrant** | Pointer to **NullableInt64** | Base rank points granted per win / taken per loss (build 6701+). | [optional] 
**CalibrationMatches** | **int64** |  | 
**CalibrationMaxRank** | Pointer to **NullableInt64** | Highest rank badge (tier * 10 + subrank) placements put a player at (build 6857+). Valve&#39;s notes for Beta Season 2 (101, Ascendant I) allow up to Ascendant III for strong previous-season performance. | [optional] 
**ClassName** | **string** |  | 
**Intervals** | [**[]SeasonInterval**](SeasonInterval.md) |  | 
**MinHeroUnlockPoints** | Pointer to **NullableInt64** | Points a hero needs to count towards &#x60;min_hero_unlocks&#x60;: 2 per win, 1 per loss (build 6857+). | [optional] 
**MinHeroUnlocks** | **int64** |  | 
**MinHeroWins** | Pointer to **NullableInt64** | Wins a hero needs to count towards &#x60;min_hero_unlocks&#x60;. Absent where the season counts hero points instead, see &#x60;min_hero_unlock_points&#x60;. | [optional] 
**MinWins** | **int64** |  | 
**Name** | **string** |  | 
**RankInfo** | Pointer to [**[]RankInfo**](RankInfo.md) | Rank progression settings (build 6857+). | [optional] 
**RankedType** | **string** |  | 
**ValidPartySizes** | **[]int64** |  | 

## Methods

### NewRankedSeason

`func NewRankedSeason(calibrationMatches int64, className string, intervals []SeasonInterval, minHeroUnlocks int64, minWins int64, name string, rankedType string, validPartySizes []int64, ) *RankedSeason`

NewRankedSeason instantiates a new RankedSeason object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRankedSeasonWithDefaults

`func NewRankedSeasonWithDefaults() *RankedSeason`

NewRankedSeasonWithDefaults instantiates a new RankedSeason object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBaseWinLossPointGrant

`func (o *RankedSeason) GetBaseWinLossPointGrant() int64`

GetBaseWinLossPointGrant returns the BaseWinLossPointGrant field if non-nil, zero value otherwise.

### GetBaseWinLossPointGrantOk

`func (o *RankedSeason) GetBaseWinLossPointGrantOk() (*int64, bool)`

GetBaseWinLossPointGrantOk returns a tuple with the BaseWinLossPointGrant field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaseWinLossPointGrant

`func (o *RankedSeason) SetBaseWinLossPointGrant(v int64)`

SetBaseWinLossPointGrant sets BaseWinLossPointGrant field to given value.

### HasBaseWinLossPointGrant

`func (o *RankedSeason) HasBaseWinLossPointGrant() bool`

HasBaseWinLossPointGrant returns a boolean if a field has been set.

### SetBaseWinLossPointGrantNil

`func (o *RankedSeason) SetBaseWinLossPointGrantNil(b bool)`

 SetBaseWinLossPointGrantNil sets the value for BaseWinLossPointGrant to be an explicit nil

### UnsetBaseWinLossPointGrant
`func (o *RankedSeason) UnsetBaseWinLossPointGrant()`

UnsetBaseWinLossPointGrant ensures that no value is present for BaseWinLossPointGrant, not even an explicit nil
### GetCalibrationMatches

`func (o *RankedSeason) GetCalibrationMatches() int64`

GetCalibrationMatches returns the CalibrationMatches field if non-nil, zero value otherwise.

### GetCalibrationMatchesOk

`func (o *RankedSeason) GetCalibrationMatchesOk() (*int64, bool)`

GetCalibrationMatchesOk returns a tuple with the CalibrationMatches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCalibrationMatches

`func (o *RankedSeason) SetCalibrationMatches(v int64)`

SetCalibrationMatches sets CalibrationMatches field to given value.


### GetCalibrationMaxRank

`func (o *RankedSeason) GetCalibrationMaxRank() int64`

GetCalibrationMaxRank returns the CalibrationMaxRank field if non-nil, zero value otherwise.

### GetCalibrationMaxRankOk

`func (o *RankedSeason) GetCalibrationMaxRankOk() (*int64, bool)`

GetCalibrationMaxRankOk returns a tuple with the CalibrationMaxRank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCalibrationMaxRank

`func (o *RankedSeason) SetCalibrationMaxRank(v int64)`

SetCalibrationMaxRank sets CalibrationMaxRank field to given value.

### HasCalibrationMaxRank

`func (o *RankedSeason) HasCalibrationMaxRank() bool`

HasCalibrationMaxRank returns a boolean if a field has been set.

### SetCalibrationMaxRankNil

`func (o *RankedSeason) SetCalibrationMaxRankNil(b bool)`

 SetCalibrationMaxRankNil sets the value for CalibrationMaxRank to be an explicit nil

### UnsetCalibrationMaxRank
`func (o *RankedSeason) UnsetCalibrationMaxRank()`

UnsetCalibrationMaxRank ensures that no value is present for CalibrationMaxRank, not even an explicit nil
### GetClassName

`func (o *RankedSeason) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *RankedSeason) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *RankedSeason) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetIntervals

`func (o *RankedSeason) GetIntervals() []SeasonInterval`

GetIntervals returns the Intervals field if non-nil, zero value otherwise.

### GetIntervalsOk

`func (o *RankedSeason) GetIntervalsOk() (*[]SeasonInterval, bool)`

GetIntervalsOk returns a tuple with the Intervals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIntervals

`func (o *RankedSeason) SetIntervals(v []SeasonInterval)`

SetIntervals sets Intervals field to given value.


### GetMinHeroUnlockPoints

`func (o *RankedSeason) GetMinHeroUnlockPoints() int64`

GetMinHeroUnlockPoints returns the MinHeroUnlockPoints field if non-nil, zero value otherwise.

### GetMinHeroUnlockPointsOk

`func (o *RankedSeason) GetMinHeroUnlockPointsOk() (*int64, bool)`

GetMinHeroUnlockPointsOk returns a tuple with the MinHeroUnlockPoints field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMinHeroUnlockPoints

`func (o *RankedSeason) SetMinHeroUnlockPoints(v int64)`

SetMinHeroUnlockPoints sets MinHeroUnlockPoints field to given value.

### HasMinHeroUnlockPoints

`func (o *RankedSeason) HasMinHeroUnlockPoints() bool`

HasMinHeroUnlockPoints returns a boolean if a field has been set.

### SetMinHeroUnlockPointsNil

`func (o *RankedSeason) SetMinHeroUnlockPointsNil(b bool)`

 SetMinHeroUnlockPointsNil sets the value for MinHeroUnlockPoints to be an explicit nil

### UnsetMinHeroUnlockPoints
`func (o *RankedSeason) UnsetMinHeroUnlockPoints()`

UnsetMinHeroUnlockPoints ensures that no value is present for MinHeroUnlockPoints, not even an explicit nil
### GetMinHeroUnlocks

`func (o *RankedSeason) GetMinHeroUnlocks() int64`

GetMinHeroUnlocks returns the MinHeroUnlocks field if non-nil, zero value otherwise.

### GetMinHeroUnlocksOk

`func (o *RankedSeason) GetMinHeroUnlocksOk() (*int64, bool)`

GetMinHeroUnlocksOk returns a tuple with the MinHeroUnlocks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMinHeroUnlocks

`func (o *RankedSeason) SetMinHeroUnlocks(v int64)`

SetMinHeroUnlocks sets MinHeroUnlocks field to given value.


### GetMinHeroWins

`func (o *RankedSeason) GetMinHeroWins() int64`

GetMinHeroWins returns the MinHeroWins field if non-nil, zero value otherwise.

### GetMinHeroWinsOk

`func (o *RankedSeason) GetMinHeroWinsOk() (*int64, bool)`

GetMinHeroWinsOk returns a tuple with the MinHeroWins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMinHeroWins

`func (o *RankedSeason) SetMinHeroWins(v int64)`

SetMinHeroWins sets MinHeroWins field to given value.

### HasMinHeroWins

`func (o *RankedSeason) HasMinHeroWins() bool`

HasMinHeroWins returns a boolean if a field has been set.

### SetMinHeroWinsNil

`func (o *RankedSeason) SetMinHeroWinsNil(b bool)`

 SetMinHeroWinsNil sets the value for MinHeroWins to be an explicit nil

### UnsetMinHeroWins
`func (o *RankedSeason) UnsetMinHeroWins()`

UnsetMinHeroWins ensures that no value is present for MinHeroWins, not even an explicit nil
### GetMinWins

`func (o *RankedSeason) GetMinWins() int64`

GetMinWins returns the MinWins field if non-nil, zero value otherwise.

### GetMinWinsOk

`func (o *RankedSeason) GetMinWinsOk() (*int64, bool)`

GetMinWinsOk returns a tuple with the MinWins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMinWins

`func (o *RankedSeason) SetMinWins(v int64)`

SetMinWins sets MinWins field to given value.


### GetName

`func (o *RankedSeason) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *RankedSeason) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *RankedSeason) SetName(v string)`

SetName sets Name field to given value.


### GetRankInfo

`func (o *RankedSeason) GetRankInfo() []RankInfo`

GetRankInfo returns the RankInfo field if non-nil, zero value otherwise.

### GetRankInfoOk

`func (o *RankedSeason) GetRankInfoOk() (*[]RankInfo, bool)`

GetRankInfoOk returns a tuple with the RankInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRankInfo

`func (o *RankedSeason) SetRankInfo(v []RankInfo)`

SetRankInfo sets RankInfo field to given value.

### HasRankInfo

`func (o *RankedSeason) HasRankInfo() bool`

HasRankInfo returns a boolean if a field has been set.

### GetRankedType

`func (o *RankedSeason) GetRankedType() string`

GetRankedType returns the RankedType field if non-nil, zero value otherwise.

### GetRankedTypeOk

`func (o *RankedSeason) GetRankedTypeOk() (*string, bool)`

GetRankedTypeOk returns a tuple with the RankedType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRankedType

`func (o *RankedSeason) SetRankedType(v string)`

SetRankedType sets RankedType field to given value.


### GetValidPartySizes

`func (o *RankedSeason) GetValidPartySizes() []int64`

GetValidPartySizes returns the ValidPartySizes field if non-nil, zero value otherwise.

### GetValidPartySizesOk

`func (o *RankedSeason) GetValidPartySizesOk() (*[]int64, bool)`

GetValidPartySizesOk returns a tuple with the ValidPartySizes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValidPartySizes

`func (o *RankedSeason) SetValidPartySizes(v []int64)`

SetValidPartySizes sets ValidPartySizes field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


