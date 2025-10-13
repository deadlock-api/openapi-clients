# ItemStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Bucket** | **int32** |  | 
**ItemId** | **int32** | See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | 
**Losses** | **int64** |  | 
**Matches** | **int64** |  | 
**Players** | **int64** |  | 
**Wins** | **int64** |  | 

## Methods

### NewItemStats

`func NewItemStats(bucket int32, itemId int32, losses int64, matches int64, players int64, wins int64, ) *ItemStats`

NewItemStats instantiates a new ItemStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewItemStatsWithDefaults

`func NewItemStatsWithDefaults() *ItemStats`

NewItemStatsWithDefaults instantiates a new ItemStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

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


