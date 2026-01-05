# ItemStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AvgBuyTimeRelative** | **float64** | Average buy time as percentage of match duration | 
**AvgBuyTimeS** | **float64** | Average buy time in seconds (absolute) | 
**AvgSellTimeRelative** | **float64** | Average sell time as percentage of match duration (for items that were sold) | 
**AvgSellTimeS** | **float64** | Average sell time in seconds (absolute, for items that were sold) | 
**Bucket** | **int32** |  | 
**ItemId** | **int32** | See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | 
**Losses** | **int64** |  | 
**Matches** | **int64** |  | 
**Players** | **int64** |  | 
**Wins** | **int64** |  | 

## Methods

### NewItemStats

`func NewItemStats(avgBuyTimeRelative float64, avgBuyTimeS float64, avgSellTimeRelative float64, avgSellTimeS float64, bucket int32, itemId int32, losses int64, matches int64, players int64, wins int64, ) *ItemStats`

NewItemStats instantiates a new ItemStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewItemStatsWithDefaults

`func NewItemStatsWithDefaults() *ItemStats`

NewItemStatsWithDefaults instantiates a new ItemStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAvgBuyTimeRelative

`func (o *ItemStats) GetAvgBuyTimeRelative() float64`

GetAvgBuyTimeRelative returns the AvgBuyTimeRelative field if non-nil, zero value otherwise.

### GetAvgBuyTimeRelativeOk

`func (o *ItemStats) GetAvgBuyTimeRelativeOk() (*float64, bool)`

GetAvgBuyTimeRelativeOk returns a tuple with the AvgBuyTimeRelative field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgBuyTimeRelative

`func (o *ItemStats) SetAvgBuyTimeRelative(v float64)`

SetAvgBuyTimeRelative sets AvgBuyTimeRelative field to given value.


### GetAvgBuyTimeS

`func (o *ItemStats) GetAvgBuyTimeS() float64`

GetAvgBuyTimeS returns the AvgBuyTimeS field if non-nil, zero value otherwise.

### GetAvgBuyTimeSOk

`func (o *ItemStats) GetAvgBuyTimeSOk() (*float64, bool)`

GetAvgBuyTimeSOk returns a tuple with the AvgBuyTimeS field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgBuyTimeS

`func (o *ItemStats) SetAvgBuyTimeS(v float64)`

SetAvgBuyTimeS sets AvgBuyTimeS field to given value.


### GetAvgSellTimeRelative

`func (o *ItemStats) GetAvgSellTimeRelative() float64`

GetAvgSellTimeRelative returns the AvgSellTimeRelative field if non-nil, zero value otherwise.

### GetAvgSellTimeRelativeOk

`func (o *ItemStats) GetAvgSellTimeRelativeOk() (*float64, bool)`

GetAvgSellTimeRelativeOk returns a tuple with the AvgSellTimeRelative field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgSellTimeRelative

`func (o *ItemStats) SetAvgSellTimeRelative(v float64)`

SetAvgSellTimeRelative sets AvgSellTimeRelative field to given value.


### GetAvgSellTimeS

`func (o *ItemStats) GetAvgSellTimeS() float64`

GetAvgSellTimeS returns the AvgSellTimeS field if non-nil, zero value otherwise.

### GetAvgSellTimeSOk

`func (o *ItemStats) GetAvgSellTimeSOk() (*float64, bool)`

GetAvgSellTimeSOk returns a tuple with the AvgSellTimeS field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgSellTimeS

`func (o *ItemStats) SetAvgSellTimeS(v float64)`

SetAvgSellTimeS sets AvgSellTimeS field to given value.


### GetBucket

`func (o *ItemStats) GetBucket() int32`

GetBucket returns the Bucket field if non-nil, zero value otherwise.

### GetBucketOk

`func (o *ItemStats) GetBucketOk() (*int32, bool)`

GetBucketOk returns a tuple with the Bucket field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBucket

`func (o *ItemStats) SetBucket(v int32)`

SetBucket sets Bucket field to given value.


### GetItemId

`func (o *ItemStats) GetItemId() int32`

GetItemId returns the ItemId field if non-nil, zero value otherwise.

### GetItemIdOk

`func (o *ItemStats) GetItemIdOk() (*int32, bool)`

GetItemIdOk returns a tuple with the ItemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemId

`func (o *ItemStats) SetItemId(v int32)`

SetItemId sets ItemId field to given value.


### GetLosses

`func (o *ItemStats) GetLosses() int64`

GetLosses returns the Losses field if non-nil, zero value otherwise.

### GetLossesOk

`func (o *ItemStats) GetLossesOk() (*int64, bool)`

GetLossesOk returns a tuple with the Losses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLosses

`func (o *ItemStats) SetLosses(v int64)`

SetLosses sets Losses field to given value.


### GetMatches

`func (o *ItemStats) GetMatches() int64`

GetMatches returns the Matches field if non-nil, zero value otherwise.

### GetMatchesOk

`func (o *ItemStats) GetMatchesOk() (*int64, bool)`

GetMatchesOk returns a tuple with the Matches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatches

`func (o *ItemStats) SetMatches(v int64)`

SetMatches sets Matches field to given value.


### GetPlayers

`func (o *ItemStats) GetPlayers() int64`

GetPlayers returns the Players field if non-nil, zero value otherwise.

### GetPlayersOk

`func (o *ItemStats) GetPlayersOk() (*int64, bool)`

GetPlayersOk returns a tuple with the Players field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayers

`func (o *ItemStats) SetPlayers(v int64)`

SetPlayers sets Players field to given value.


### GetWins

`func (o *ItemStats) GetWins() int64`

GetWins returns the Wins field if non-nil, zero value otherwise.

### GetWinsOk

`func (o *ItemStats) GetWinsOk() (*int64, bool)`

GetWinsOk returns a tuple with the Wins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWins

`func (o *ItemStats) SetWins(v int64)`

SetWins sets Wins field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


