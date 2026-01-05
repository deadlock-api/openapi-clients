# NetWorthCurvePoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Avg** | **float64** | Average net worth at this timestamp | 
**Percentile1** | **float64** | 1st percentile net worth | 
**Percentile10** | **float64** | 10th percentile net worth | 
**Percentile25** | **float64** | 25th percentile net worth | 
**Percentile5** | **float64** | 5th percentile net worth | 
**Percentile50** | **float64** | 50th percentile net worth | 
**Percentile75** | **float64** | 75th percentile net worth | 
**Percentile90** | **float64** | 90th percentile net worth | 
**Percentile95** | **float64** | 95th percentile net worth | 
**Percentile99** | **float64** | 99th percentile net worth | 
**RelativeTimestamp** | **int32** | Percentage interval of match duration (0%, 5%, 10%, ..., 100%) | 
**Std** | **float64** | Standard deviation of net worth at this timestamp | 

## Methods

### NewNetWorthCurvePoint

`func NewNetWorthCurvePoint(avg float64, percentile1 float64, percentile10 float64, percentile25 float64, percentile5 float64, percentile50 float64, percentile75 float64, percentile90 float64, percentile95 float64, percentile99 float64, relativeTimestamp int32, std float64, ) *NetWorthCurvePoint`

NewNetWorthCurvePoint instantiates a new NetWorthCurvePoint object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNetWorthCurvePointWithDefaults

`func NewNetWorthCurvePointWithDefaults() *NetWorthCurvePoint`

NewNetWorthCurvePointWithDefaults instantiates a new NetWorthCurvePoint object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAvg

`func (o *NetWorthCurvePoint) GetAvg() float64`

GetAvg returns the Avg field if non-nil, zero value otherwise.

### GetAvgOk

`func (o *NetWorthCurvePoint) GetAvgOk() (*float64, bool)`

GetAvgOk returns a tuple with the Avg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvg

`func (o *NetWorthCurvePoint) SetAvg(v float64)`

SetAvg sets Avg field to given value.


### GetPercentile1

`func (o *NetWorthCurvePoint) GetPercentile1() float64`

GetPercentile1 returns the Percentile1 field if non-nil, zero value otherwise.

### GetPercentile1Ok

`func (o *NetWorthCurvePoint) GetPercentile1Ok() (*float64, bool)`

GetPercentile1Ok returns a tuple with the Percentile1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPercentile1

`func (o *NetWorthCurvePoint) SetPercentile1(v float64)`

SetPercentile1 sets Percentile1 field to given value.


### GetPercentile10

`func (o *NetWorthCurvePoint) GetPercentile10() float64`

GetPercentile10 returns the Percentile10 field if non-nil, zero value otherwise.

### GetPercentile10Ok

`func (o *NetWorthCurvePoint) GetPercentile10Ok() (*float64, bool)`

GetPercentile10Ok returns a tuple with the Percentile10 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPercentile10

`func (o *NetWorthCurvePoint) SetPercentile10(v float64)`

SetPercentile10 sets Percentile10 field to given value.


### GetPercentile25

`func (o *NetWorthCurvePoint) GetPercentile25() float64`

GetPercentile25 returns the Percentile25 field if non-nil, zero value otherwise.

### GetPercentile25Ok

`func (o *NetWorthCurvePoint) GetPercentile25Ok() (*float64, bool)`

GetPercentile25Ok returns a tuple with the Percentile25 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPercentile25

`func (o *NetWorthCurvePoint) SetPercentile25(v float64)`

SetPercentile25 sets Percentile25 field to given value.


### GetPercentile5

`func (o *NetWorthCurvePoint) GetPercentile5() float64`

GetPercentile5 returns the Percentile5 field if non-nil, zero value otherwise.

### GetPercentile5Ok

`func (o *NetWorthCurvePoint) GetPercentile5Ok() (*float64, bool)`

GetPercentile5Ok returns a tuple with the Percentile5 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPercentile5

`func (o *NetWorthCurvePoint) SetPercentile5(v float64)`

SetPercentile5 sets Percentile5 field to given value.


### GetPercentile50

`func (o *NetWorthCurvePoint) GetPercentile50() float64`

GetPercentile50 returns the Percentile50 field if non-nil, zero value otherwise.

### GetPercentile50Ok

`func (o *NetWorthCurvePoint) GetPercentile50Ok() (*float64, bool)`

GetPercentile50Ok returns a tuple with the Percentile50 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPercentile50

`func (o *NetWorthCurvePoint) SetPercentile50(v float64)`

SetPercentile50 sets Percentile50 field to given value.


### GetPercentile75

`func (o *NetWorthCurvePoint) GetPercentile75() float64`

GetPercentile75 returns the Percentile75 field if non-nil, zero value otherwise.

### GetPercentile75Ok

`func (o *NetWorthCurvePoint) GetPercentile75Ok() (*float64, bool)`

GetPercentile75Ok returns a tuple with the Percentile75 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPercentile75

`func (o *NetWorthCurvePoint) SetPercentile75(v float64)`

SetPercentile75 sets Percentile75 field to given value.


### GetPercentile90

`func (o *NetWorthCurvePoint) GetPercentile90() float64`

GetPercentile90 returns the Percentile90 field if non-nil, zero value otherwise.

### GetPercentile90Ok

`func (o *NetWorthCurvePoint) GetPercentile90Ok() (*float64, bool)`

GetPercentile90Ok returns a tuple with the Percentile90 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPercentile90

`func (o *NetWorthCurvePoint) SetPercentile90(v float64)`

SetPercentile90 sets Percentile90 field to given value.


### GetPercentile95

`func (o *NetWorthCurvePoint) GetPercentile95() float64`

GetPercentile95 returns the Percentile95 field if non-nil, zero value otherwise.

### GetPercentile95Ok

`func (o *NetWorthCurvePoint) GetPercentile95Ok() (*float64, bool)`

GetPercentile95Ok returns a tuple with the Percentile95 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPercentile95

`func (o *NetWorthCurvePoint) SetPercentile95(v float64)`

SetPercentile95 sets Percentile95 field to given value.


### GetPercentile99

`func (o *NetWorthCurvePoint) GetPercentile99() float64`

GetPercentile99 returns the Percentile99 field if non-nil, zero value otherwise.

### GetPercentile99Ok

`func (o *NetWorthCurvePoint) GetPercentile99Ok() (*float64, bool)`

GetPercentile99Ok returns a tuple with the Percentile99 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPercentile99

`func (o *NetWorthCurvePoint) SetPercentile99(v float64)`

SetPercentile99 sets Percentile99 field to given value.


### GetRelativeTimestamp

`func (o *NetWorthCurvePoint) GetRelativeTimestamp() int32`

GetRelativeTimestamp returns the RelativeTimestamp field if non-nil, zero value otherwise.

### GetRelativeTimestampOk

`func (o *NetWorthCurvePoint) GetRelativeTimestampOk() (*int32, bool)`

GetRelativeTimestampOk returns a tuple with the RelativeTimestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRelativeTimestamp

`func (o *NetWorthCurvePoint) SetRelativeTimestamp(v int32)`

SetRelativeTimestamp sets RelativeTimestamp field to given value.


### GetStd

`func (o *NetWorthCurvePoint) GetStd() float64`

GetStd returns the Std field if non-nil, zero value otherwise.

### GetStdOk

`func (o *NetWorthCurvePoint) GetStdOk() (*float64, bool)`

GetStdOk returns a tuple with the Std field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStd

`func (o *NetWorthCurvePoint) SetStd(v float64)`

SetStd sets Std field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


