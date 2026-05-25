# ItemPermutationStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ItemIds** | **[]int32** | See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | 
**Losses** | **int64** |  | 
**Matches** | **int64** |  | 
**Wins** | **int64** |  | 

## Methods

### NewItemPermutationStats

`func NewItemPermutationStats(itemIds []int32, losses int64, matches int64, wins int64, ) *ItemPermutationStats`

NewItemPermutationStats instantiates a new ItemPermutationStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewItemPermutationStatsWithDefaults

`func NewItemPermutationStatsWithDefaults() *ItemPermutationStats`

NewItemPermutationStatsWithDefaults instantiates a new ItemPermutationStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItemIds

`func (o *ItemPermutationStats) GetItemIds() []int32`

GetItemIds returns the ItemIds field if non-nil, zero value otherwise.

### GetItemIdsOk

`func (o *ItemPermutationStats) GetItemIdsOk() (*[]int32, bool)`

GetItemIdsOk returns a tuple with the ItemIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemIds

`func (o *ItemPermutationStats) SetItemIds(v []int32)`

SetItemIds sets ItemIds field to given value.


### GetLosses

`func (o *ItemPermutationStats) GetLosses() int64`

GetLosses returns the Losses field if non-nil, zero value otherwise.

### GetLossesOk

`func (o *ItemPermutationStats) GetLossesOk() (*int64, bool)`

GetLossesOk returns a tuple with the Losses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLosses

`func (o *ItemPermutationStats) SetLosses(v int64)`

SetLosses sets Losses field to given value.


### GetMatches

`func (o *ItemPermutationStats) GetMatches() int64`

GetMatches returns the Matches field if non-nil, zero value otherwise.

### GetMatchesOk

`func (o *ItemPermutationStats) GetMatchesOk() (*int64, bool)`

GetMatchesOk returns a tuple with the Matches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatches

`func (o *ItemPermutationStats) SetMatches(v int64)`

SetMatches sets Matches field to given value.


### GetWins

`func (o *ItemPermutationStats) GetWins() int64`

GetWins returns the Wins field if non-nil, zero value otherwise.

### GetWinsOk

`func (o *ItemPermutationStats) GetWinsOk() (*int64, bool)`

GetWinsOk returns a tuple with the Wins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWins

`func (o *ItemPermutationStats) SetWins(v int64)`

SetWins sets Wins field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


