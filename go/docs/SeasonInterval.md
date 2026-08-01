# SeasonInterval

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EndTimestamp** | **int64** | Unix timestamp (seconds) at which the interval ends. | 
**Interval** | **int32** |  | 
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


