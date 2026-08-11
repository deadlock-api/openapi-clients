# LaneMatchupStat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Diff** | **float64** | Mean of the duo&#39;s combined value minus the enemy duo&#39;s. Negative means behind. | 
**DiffStd** | **float64** | Population standard deviation of &#x60;diff&#x60; across the counted matchups. | 
**Value** | **float64** | Mean of the duo&#39;s combined value, summed over its two players. | 
**ValueStd** | **float64** | Population standard deviation of &#x60;value&#x60; across the counted matchups. | 

## Methods

### NewLaneMatchupStat

`func NewLaneMatchupStat(diff float64, diffStd float64, value float64, valueStd float64, ) *LaneMatchupStat`

NewLaneMatchupStat instantiates a new LaneMatchupStat object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewLaneMatchupStatWithDefaults

`func NewLaneMatchupStatWithDefaults() *LaneMatchupStat`

NewLaneMatchupStatWithDefaults instantiates a new LaneMatchupStat object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDiff

`func (o *LaneMatchupStat) GetDiff() float64`

GetDiff returns the Diff field if non-nil, zero value otherwise.

### GetDiffOk

`func (o *LaneMatchupStat) GetDiffOk() (*float64, bool)`

GetDiffOk returns a tuple with the Diff field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiff

`func (o *LaneMatchupStat) SetDiff(v float64)`

SetDiff sets Diff field to given value.


### GetDiffStd

`func (o *LaneMatchupStat) GetDiffStd() float64`

GetDiffStd returns the DiffStd field if non-nil, zero value otherwise.

### GetDiffStdOk

`func (o *LaneMatchupStat) GetDiffStdOk() (*float64, bool)`

GetDiffStdOk returns a tuple with the DiffStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiffStd

`func (o *LaneMatchupStat) SetDiffStd(v float64)`

SetDiffStd sets DiffStd field to given value.


### GetValue

`func (o *LaneMatchupStat) GetValue() float64`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *LaneMatchupStat) GetValueOk() (*float64, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *LaneMatchupStat) SetValue(v float64)`

SetValue sets Value field to given value.


### GetValueStd

`func (o *LaneMatchupStat) GetValueStd() float64`

GetValueStd returns the ValueStd field if non-nil, zero value otherwise.

### GetValueStdOk

`func (o *LaneMatchupStat) GetValueStdOk() (*float64, bool)`

GetValueStdOk returns a tuple with the ValueStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValueStd

`func (o *LaneMatchupStat) SetValueStd(v float64)`

SetValueStd sets ValueStd field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


