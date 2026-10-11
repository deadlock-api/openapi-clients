# ItemFlowLeaveOneOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Column** | **int32** | Its locked stage column. | 
**ItemId** | **int32** | The locked item left out. See more: &lt;https://api.deadlock-api.com/v1/assets/items&gt; | 
**Matches** | **int64** |  | 
**Wins** | **int64** |  | 

## Methods

### NewItemFlowLeaveOneOut

`func NewItemFlowLeaveOneOut(column int32, itemId int32, matches int64, wins int64, ) *ItemFlowLeaveOneOut`

NewItemFlowLeaveOneOut instantiates a new ItemFlowLeaveOneOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewItemFlowLeaveOneOutWithDefaults

`func NewItemFlowLeaveOneOutWithDefaults() *ItemFlowLeaveOneOut`

NewItemFlowLeaveOneOutWithDefaults instantiates a new ItemFlowLeaveOneOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetColumn

`func (o *ItemFlowLeaveOneOut) GetColumn() int32`

GetColumn returns the Column field if non-nil, zero value otherwise.

### GetColumnOk

`func (o *ItemFlowLeaveOneOut) GetColumnOk() (*int32, bool)`

GetColumnOk returns a tuple with the Column field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColumn

`func (o *ItemFlowLeaveOneOut) SetColumn(v int32)`

SetColumn sets Column field to given value.


### GetItemId

`func (o *ItemFlowLeaveOneOut) GetItemId() int32`

GetItemId returns the ItemId field if non-nil, zero value otherwise.

### GetItemIdOk

`func (o *ItemFlowLeaveOneOut) GetItemIdOk() (*int32, bool)`

GetItemIdOk returns a tuple with the ItemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemId

`func (o *ItemFlowLeaveOneOut) SetItemId(v int32)`

SetItemId sets ItemId field to given value.


### GetMatches

`func (o *ItemFlowLeaveOneOut) GetMatches() int64`

GetMatches returns the Matches field if non-nil, zero value otherwise.

### GetMatchesOk

`func (o *ItemFlowLeaveOneOut) GetMatchesOk() (*int64, bool)`

GetMatchesOk returns a tuple with the Matches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatches

`func (o *ItemFlowLeaveOneOut) SetMatches(v int64)`

SetMatches sets Matches field to given value.


### GetWins

`func (o *ItemFlowLeaveOneOut) GetWins() int64`

GetWins returns the Wins field if non-nil, zero value otherwise.

### GetWinsOk

`func (o *ItemFlowLeaveOneOut) GetWinsOk() (*int64, bool)`

GetWinsOk returns a tuple with the Wins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWins

`func (o *ItemFlowLeaveOneOut) SetWins(v int64)`

SetWins sets Wins field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


