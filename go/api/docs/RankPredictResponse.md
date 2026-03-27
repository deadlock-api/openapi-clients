# RankPredictResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Badge** | **int32** | See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
**RawScore** | **float32** | Raw model output (float index into badge space) | 
**MatchesUsed** | **int32** | Number of recent matches used for the prediction | 

## Methods

### NewRankPredictResponse

`func NewRankPredictResponse(badge int32, rawScore float32, matchesUsed int32, ) *RankPredictResponse`

NewRankPredictResponse instantiates a new RankPredictResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRankPredictResponseWithDefaults

`func NewRankPredictResponseWithDefaults() *RankPredictResponse`

NewRankPredictResponseWithDefaults instantiates a new RankPredictResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBadge

`func (o *RankPredictResponse) GetBadge() int32`

GetBadge returns the Badge field if non-nil, zero value otherwise.

### GetBadgeOk

`func (o *RankPredictResponse) GetBadgeOk() (*int32, bool)`

GetBadgeOk returns a tuple with the Badge field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBadge

`func (o *RankPredictResponse) SetBadge(v int32)`

SetBadge sets Badge field to given value.


### GetRawScore

`func (o *RankPredictResponse) GetRawScore() float32`

GetRawScore returns the RawScore field if non-nil, zero value otherwise.

### GetRawScoreOk

`func (o *RankPredictResponse) GetRawScoreOk() (*float32, bool)`

GetRawScoreOk returns a tuple with the RawScore field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRawScore

`func (o *RankPredictResponse) SetRawScore(v float32)`

SetRawScore sets RawScore field to given value.


### GetMatchesUsed

`func (o *RankPredictResponse) GetMatchesUsed() int32`

GetMatchesUsed returns the MatchesUsed field if non-nil, zero value otherwise.

### GetMatchesUsedOk

`func (o *RankPredictResponse) GetMatchesUsedOk() (*int32, bool)`

GetMatchesUsedOk returns a tuple with the MatchesUsed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchesUsed

`func (o *RankPredictResponse) SetMatchesUsed(v int32)`

SetMatchesUsed sets MatchesUsed field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


