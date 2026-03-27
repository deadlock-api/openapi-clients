# RankPrediction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Badge** | **int32** | See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
**RawScore** | **float32** | Raw model output (float index into badge space) | 

## Methods

### NewRankPrediction

`func NewRankPrediction(badge int32, rawScore float32, ) *RankPrediction`

NewRankPrediction instantiates a new RankPrediction object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRankPredictionWithDefaults

`func NewRankPredictionWithDefaults() *RankPrediction`

NewRankPredictionWithDefaults instantiates a new RankPrediction object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBadge

`func (o *RankPrediction) GetBadge() int32`

GetBadge returns the Badge field if non-nil, zero value otherwise.

### GetBadgeOk

`func (o *RankPrediction) GetBadgeOk() (*int32, bool)`

GetBadgeOk returns a tuple with the Badge field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBadge

`func (o *RankPrediction) SetBadge(v int32)`

SetBadge sets Badge field to given value.


### GetRawScore

`func (o *RankPrediction) GetRawScore() float32`

GetRawScore returns the RawScore field if non-nil, zero value otherwise.

### GetRawScoreOk

`func (o *RankPrediction) GetRawScoreOk() (*float32, bool)`

GetRawScoreOk returns a tuple with the RawScore field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRawScore

`func (o *RankPrediction) SetRawScore(v float32)`

SetRawScore sets RawScore field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


