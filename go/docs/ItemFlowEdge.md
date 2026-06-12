# ItemFlowEdge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FromColumn** | **int32** | The column of the source item. | 
**FromItemId** | **int32** |  | 
**Losses** | **int64** |  | 
**Matches** | **int64** |  | 
**ToItemId** | **int32** |  | 
**Wins** | **int64** |  | 

## Methods

### NewItemFlowEdge

`func NewItemFlowEdge(fromColumn int32, fromItemId int32, losses int64, matches int64, toItemId int32, wins int64, ) *ItemFlowEdge`

NewItemFlowEdge instantiates a new ItemFlowEdge object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewItemFlowEdgeWithDefaults

`func NewItemFlowEdgeWithDefaults() *ItemFlowEdge`

NewItemFlowEdgeWithDefaults instantiates a new ItemFlowEdge object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFromColumn

`func (o *ItemFlowEdge) GetFromColumn() int32`

GetFromColumn returns the FromColumn field if non-nil, zero value otherwise.

### GetFromColumnOk

`func (o *ItemFlowEdge) GetFromColumnOk() (*int32, bool)`

GetFromColumnOk returns a tuple with the FromColumn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFromColumn

`func (o *ItemFlowEdge) SetFromColumn(v int32)`

SetFromColumn sets FromColumn field to given value.


### GetFromItemId

`func (o *ItemFlowEdge) GetFromItemId() int32`

GetFromItemId returns the FromItemId field if non-nil, zero value otherwise.

### GetFromItemIdOk

`func (o *ItemFlowEdge) GetFromItemIdOk() (*int32, bool)`

GetFromItemIdOk returns a tuple with the FromItemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFromItemId

`func (o *ItemFlowEdge) SetFromItemId(v int32)`

SetFromItemId sets FromItemId field to given value.


### GetLosses

`func (o *ItemFlowEdge) GetLosses() int64`

GetLosses returns the Losses field if non-nil, zero value otherwise.

### GetLossesOk

`func (o *ItemFlowEdge) GetLossesOk() (*int64, bool)`

GetLossesOk returns a tuple with the Losses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLosses

`func (o *ItemFlowEdge) SetLosses(v int64)`

SetLosses sets Losses field to given value.


### GetMatches

`func (o *ItemFlowEdge) GetMatches() int64`

GetMatches returns the Matches field if non-nil, zero value otherwise.

### GetMatchesOk

`func (o *ItemFlowEdge) GetMatchesOk() (*int64, bool)`

GetMatchesOk returns a tuple with the Matches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatches

`func (o *ItemFlowEdge) SetMatches(v int64)`

SetMatches sets Matches field to given value.


### GetToItemId

`func (o *ItemFlowEdge) GetToItemId() int32`

GetToItemId returns the ToItemId field if non-nil, zero value otherwise.

### GetToItemIdOk

`func (o *ItemFlowEdge) GetToItemIdOk() (*int32, bool)`

GetToItemIdOk returns a tuple with the ToItemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToItemId

`func (o *ItemFlowEdge) SetToItemId(v int32)`

SetToItemId sets ToItemId field to given value.


### GetWins

`func (o *ItemFlowEdge) GetWins() int64`

GetWins returns the Wins field if non-nil, zero value otherwise.

### GetWinsOk

`func (o *ItemFlowEdge) GetWinsOk() (*int64, bool)`

GetWinsOk returns a tuple with the Wins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWins

`func (o *ItemFlowEdge) SetWins(v int64)`

SetWins sets Wins field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


