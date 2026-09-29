# SeasonInterval

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EndTimestamp** | **int64** | Unix timestamp (seconds) at which the interval ends. | 
**Interval** | **int32** |  | 
**LeaderboardId** | Pointer to **NullableInt32** | Leaderboard backing this interval (build 6701+). | [optional] 
**StartTimestamp** | **int64** | Unix timestamp (seconds) at which the interval starts. | 

## Methods

### NewSeasonInterval

`func NewSeasonInterval(endTimestamp int64, interval int32, startTimestamp int64, ) *SeasonInterval`

NewSeasonInterval instantiates a new SeasonInterval object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSeasonIntervalWithDefaults

`func NewSeasonIntervalWithDefaults() *SeasonInterval`

NewSeasonIntervalWithDefaults instantiates a new SeasonInterval object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEndTimestamp

`func (o *SeasonInterval) GetEndTimestamp() int64`

GetEndTimestamp returns the EndTimestamp field if non-nil, zero value otherwise.

### GetEndTimestampOk

`func (o *SeasonInterval) GetEndTimestampOk() (*int64, bool)`

GetEndTimestampOk returns a tuple with the EndTimestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndTimestamp

`func (o *SeasonInterval) SetEndTimestamp(v int64)`

SetEndTimestamp sets EndTimestamp field to given value.


### GetInterval

`func (o *SeasonInterval) GetInterval() int32`

GetInterval returns the Interval field if non-nil, zero value otherwise.

### GetIntervalOk

`func (o *SeasonInterval) GetIntervalOk() (*int32, bool)`

GetIntervalOk returns a tuple with the Interval field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInterval

`func (o *SeasonInterval) SetInterval(v int32)`

SetInterval sets Interval field to given value.


### GetLeaderboardId

`func (o *SeasonInterval) GetLeaderboardId() int32`

GetLeaderboardId returns the LeaderboardId field if non-nil, zero value otherwise.

### GetLeaderboardIdOk

`func (o *SeasonInterval) GetLeaderboardIdOk() (*int32, bool)`

GetLeaderboardIdOk returns a tuple with the LeaderboardId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLeaderboardId

`func (o *SeasonInterval) SetLeaderboardId(v int32)`

SetLeaderboardId sets LeaderboardId field to given value.

### HasLeaderboardId

`func (o *SeasonInterval) HasLeaderboardId() bool`

HasLeaderboardId returns a boolean if a field has been set.

### SetLeaderboardIdNil

`func (o *SeasonInterval) SetLeaderboardIdNil(b bool)`

 SetLeaderboardIdNil sets the value for LeaderboardId to be an explicit nil

### UnsetLeaderboardId
`func (o *SeasonInterval) UnsetLeaderboardId()`

UnsetLeaderboardId ensures that no value is present for LeaderboardId, not even an explicit nil
### GetStartTimestamp

`func (o *SeasonInterval) GetStartTimestamp() int64`

GetStartTimestamp returns the StartTimestamp field if non-nil, zero value otherwise.

### GetStartTimestampOk

`func (o *SeasonInterval) GetStartTimestampOk() (*int64, bool)`

GetStartTimestampOk returns a tuple with the StartTimestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTimestamp

`func (o *SeasonInterval) SetStartTimestamp(v int64)`

SetStartTimestamp sets StartTimestamp field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


