# PlayerPerformanceCurvePoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AssistsAvg** | **float64** | Average assists at this timestamp | 
**AssistsStd** | **float64** | Standard deviation of assists at this timestamp | 
**DeathsAvg** | **float64** | Average deaths at this timestamp | 
**DeathsStd** | **float64** | Standard deviation of deaths at this timestamp | 
**KillsAvg** | **float64** | Average kills at this timestamp | 
**KillsStd** | **float64** | Standard deviation of kills at this timestamp | 
**NetWorthAvg** | **float64** | Average net worth at this timestamp | 
**NetWorthStd** | **float64** | Standard deviation of net worth at this timestamp | 
**RelativeTimestamp** | **int32** | Percentage interval of match duration (0%, 5%, 10%, ..., 100%) | 

## Methods

### NewPlayerPerformanceCurvePoint

`func NewPlayerPerformanceCurvePoint(assistsAvg float64, assistsStd float64, deathsAvg float64, deathsStd float64, killsAvg float64, killsStd float64, netWorthAvg float64, netWorthStd float64, relativeTimestamp int32, ) *PlayerPerformanceCurvePoint`

NewPlayerPerformanceCurvePoint instantiates a new PlayerPerformanceCurvePoint object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPlayerPerformanceCurvePointWithDefaults

`func NewPlayerPerformanceCurvePointWithDefaults() *PlayerPerformanceCurvePoint`

NewPlayerPerformanceCurvePointWithDefaults instantiates a new PlayerPerformanceCurvePoint object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAssistsAvg

`func (o *PlayerPerformanceCurvePoint) GetAssistsAvg() float64`

GetAssistsAvg returns the AssistsAvg field if non-nil, zero value otherwise.

### GetAssistsAvgOk

`func (o *PlayerPerformanceCurvePoint) GetAssistsAvgOk() (*float64, bool)`

GetAssistsAvgOk returns a tuple with the AssistsAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssistsAvg

`func (o *PlayerPerformanceCurvePoint) SetAssistsAvg(v float64)`

SetAssistsAvg sets AssistsAvg field to given value.


### GetAssistsStd

`func (o *PlayerPerformanceCurvePoint) GetAssistsStd() float64`

GetAssistsStd returns the AssistsStd field if non-nil, zero value otherwise.

### GetAssistsStdOk

`func (o *PlayerPerformanceCurvePoint) GetAssistsStdOk() (*float64, bool)`

GetAssistsStdOk returns a tuple with the AssistsStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssistsStd

`func (o *PlayerPerformanceCurvePoint) SetAssistsStd(v float64)`

SetAssistsStd sets AssistsStd field to given value.


### GetDeathsAvg

`func (o *PlayerPerformanceCurvePoint) GetDeathsAvg() float64`

GetDeathsAvg returns the DeathsAvg field if non-nil, zero value otherwise.

### GetDeathsAvgOk

`func (o *PlayerPerformanceCurvePoint) GetDeathsAvgOk() (*float64, bool)`

GetDeathsAvgOk returns a tuple with the DeathsAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeathsAvg

`func (o *PlayerPerformanceCurvePoint) SetDeathsAvg(v float64)`

SetDeathsAvg sets DeathsAvg field to given value.


### GetDeathsStd

`func (o *PlayerPerformanceCurvePoint) GetDeathsStd() float64`

GetDeathsStd returns the DeathsStd field if non-nil, zero value otherwise.

### GetDeathsStdOk

`func (o *PlayerPerformanceCurvePoint) GetDeathsStdOk() (*float64, bool)`

GetDeathsStdOk returns a tuple with the DeathsStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeathsStd

`func (o *PlayerPerformanceCurvePoint) SetDeathsStd(v float64)`

SetDeathsStd sets DeathsStd field to given value.


### GetKillsAvg

`func (o *PlayerPerformanceCurvePoint) GetKillsAvg() float64`

GetKillsAvg returns the KillsAvg field if non-nil, zero value otherwise.

### GetKillsAvgOk

`func (o *PlayerPerformanceCurvePoint) GetKillsAvgOk() (*float64, bool)`

GetKillsAvgOk returns a tuple with the KillsAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKillsAvg

`func (o *PlayerPerformanceCurvePoint) SetKillsAvg(v float64)`

SetKillsAvg sets KillsAvg field to given value.


### GetKillsStd

`func (o *PlayerPerformanceCurvePoint) GetKillsStd() float64`

GetKillsStd returns the KillsStd field if non-nil, zero value otherwise.

### GetKillsStdOk

`func (o *PlayerPerformanceCurvePoint) GetKillsStdOk() (*float64, bool)`

GetKillsStdOk returns a tuple with the KillsStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKillsStd

`func (o *PlayerPerformanceCurvePoint) SetKillsStd(v float64)`

SetKillsStd sets KillsStd field to given value.


### GetNetWorthAvg

`func (o *PlayerPerformanceCurvePoint) GetNetWorthAvg() float64`

GetNetWorthAvg returns the NetWorthAvg field if non-nil, zero value otherwise.

### GetNetWorthAvgOk

`func (o *PlayerPerformanceCurvePoint) GetNetWorthAvgOk() (*float64, bool)`

GetNetWorthAvgOk returns a tuple with the NetWorthAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetWorthAvg

`func (o *PlayerPerformanceCurvePoint) SetNetWorthAvg(v float64)`

SetNetWorthAvg sets NetWorthAvg field to given value.


### GetNetWorthStd

`func (o *PlayerPerformanceCurvePoint) GetNetWorthStd() float64`

GetNetWorthStd returns the NetWorthStd field if non-nil, zero value otherwise.

### GetNetWorthStdOk

`func (o *PlayerPerformanceCurvePoint) GetNetWorthStdOk() (*float64, bool)`

GetNetWorthStdOk returns a tuple with the NetWorthStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetWorthStd

`func (o *PlayerPerformanceCurvePoint) SetNetWorthStd(v float64)`

SetNetWorthStd sets NetWorthStd field to given value.


### GetRelativeTimestamp

`func (o *PlayerPerformanceCurvePoint) GetRelativeTimestamp() int32`

GetRelativeTimestamp returns the RelativeTimestamp field if non-nil, zero value otherwise.

### GetRelativeTimestampOk

`func (o *PlayerPerformanceCurvePoint) GetRelativeTimestampOk() (*int32, bool)`

GetRelativeTimestampOk returns a tuple with the RelativeTimestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRelativeTimestamp

`func (o *PlayerPerformanceCurvePoint) SetRelativeTimestamp(v int32)`

SetRelativeTimestamp sets RelativeTimestamp field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


