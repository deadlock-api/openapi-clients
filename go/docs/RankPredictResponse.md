# RankPredictResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Badge** | **int32** | Rank badge, &#x60;tier * 10 + subrank&#x60;. &#x60;0&#x60; when no recent ranked match reports a rank. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | 
**Rank** | **int32** | Rank tier, &#x60;0&#x60; when unknown. | 
**Subrank** | **int32** | Sub-rank within the tier, &#x60;0&#x60; when unknown. | 

## Methods

### NewRankPredictResponse

`func NewRankPredictResponse(badge int32, rank int32, subrank int32, ) *RankPredictResponse`

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


### GetRank

`func (o *RankPredictResponse) GetRank() int32`

GetRank returns the Rank field if non-nil, zero value otherwise.

### GetRankOk

`func (o *RankPredictResponse) GetRankOk() (*int32, bool)`

GetRankOk returns a tuple with the Rank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRank

`func (o *RankPredictResponse) SetRank(v int32)`

SetRank sets Rank field to given value.


### GetSubrank

`func (o *RankPredictResponse) GetSubrank() int32`

GetSubrank returns the Subrank field if non-nil, zero value otherwise.

### GetSubrankOk

`func (o *RankPredictResponse) GetSubrankOk() (*int32, bool)`

GetSubrankOk returns a tuple with the Subrank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubrank

`func (o *RankPredictResponse) SetSubrank(v int32)`

SetSubrank sets Subrank field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


