# ItemFlowNode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AdjustedWinRate** | **float64** | Win rate standardized to the stage&#39;s net-worth-at-buy distribution, removing the \&quot;richer buyers win more\&quot; confound. See the endpoint description. | 
**AvgNetWorthAtBuy** | **float64** | Average net worth of buyers at the moment they bought this item (confound visibility). | 
**Column** | **int32** | The phase column (0-based) the item was bought in. | 
**ItemId** | **int32** | See more: &lt;https://api.deadlock-api.com/v1/assets/items&gt; | 
**Losses** | **int64** |  | 
**Matches** | **int64** |  | 
**Players** | **int64** |  | 
**TotalAssists** | **int64** |  | 
**TotalDeaths** | **int64** |  | 
**TotalKills** | **int64** |  | 
**Wins** | **int64** |  | 

## Methods

### NewItemFlowNode

`func NewItemFlowNode(adjustedWinRate float64, avgNetWorthAtBuy float64, column int32, itemId int32, losses int64, matches int64, players int64, totalAssists int64, totalDeaths int64, totalKills int64, wins int64, ) *ItemFlowNode`

NewItemFlowNode instantiates a new ItemFlowNode object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewItemFlowNodeWithDefaults

`func NewItemFlowNodeWithDefaults() *ItemFlowNode`

NewItemFlowNodeWithDefaults instantiates a new ItemFlowNode object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAdjustedWinRate

`func (o *ItemFlowNode) GetAdjustedWinRate() float64`

GetAdjustedWinRate returns the AdjustedWinRate field if non-nil, zero value otherwise.

### GetAdjustedWinRateOk

`func (o *ItemFlowNode) GetAdjustedWinRateOk() (*float64, bool)`

GetAdjustedWinRateOk returns a tuple with the AdjustedWinRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdjustedWinRate

`func (o *ItemFlowNode) SetAdjustedWinRate(v float64)`

SetAdjustedWinRate sets AdjustedWinRate field to given value.


### GetAvgNetWorthAtBuy

`func (o *ItemFlowNode) GetAvgNetWorthAtBuy() float64`

GetAvgNetWorthAtBuy returns the AvgNetWorthAtBuy field if non-nil, zero value otherwise.

### GetAvgNetWorthAtBuyOk

`func (o *ItemFlowNode) GetAvgNetWorthAtBuyOk() (*float64, bool)`

GetAvgNetWorthAtBuyOk returns a tuple with the AvgNetWorthAtBuy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgNetWorthAtBuy

`func (o *ItemFlowNode) SetAvgNetWorthAtBuy(v float64)`

SetAvgNetWorthAtBuy sets AvgNetWorthAtBuy field to given value.


### GetColumn

`func (o *ItemFlowNode) GetColumn() int32`

GetColumn returns the Column field if non-nil, zero value otherwise.

### GetColumnOk

`func (o *ItemFlowNode) GetColumnOk() (*int32, bool)`

GetColumnOk returns a tuple with the Column field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColumn

`func (o *ItemFlowNode) SetColumn(v int32)`

SetColumn sets Column field to given value.


### GetItemId

`func (o *ItemFlowNode) GetItemId() int32`

GetItemId returns the ItemId field if non-nil, zero value otherwise.

### GetItemIdOk

`func (o *ItemFlowNode) GetItemIdOk() (*int32, bool)`

GetItemIdOk returns a tuple with the ItemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemId

`func (o *ItemFlowNode) SetItemId(v int32)`

SetItemId sets ItemId field to given value.


### GetLosses

`func (o *ItemFlowNode) GetLosses() int64`

GetLosses returns the Losses field if non-nil, zero value otherwise.

### GetLossesOk

`func (o *ItemFlowNode) GetLossesOk() (*int64, bool)`

GetLossesOk returns a tuple with the Losses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLosses

`func (o *ItemFlowNode) SetLosses(v int64)`

SetLosses sets Losses field to given value.


### GetMatches

`func (o *ItemFlowNode) GetMatches() int64`

GetMatches returns the Matches field if non-nil, zero value otherwise.

### GetMatchesOk

`func (o *ItemFlowNode) GetMatchesOk() (*int64, bool)`

GetMatchesOk returns a tuple with the Matches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatches

`func (o *ItemFlowNode) SetMatches(v int64)`

SetMatches sets Matches field to given value.


### GetPlayers

`func (o *ItemFlowNode) GetPlayers() int64`

GetPlayers returns the Players field if non-nil, zero value otherwise.

### GetPlayersOk

`func (o *ItemFlowNode) GetPlayersOk() (*int64, bool)`

GetPlayersOk returns a tuple with the Players field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayers

`func (o *ItemFlowNode) SetPlayers(v int64)`

SetPlayers sets Players field to given value.


### GetTotalAssists

`func (o *ItemFlowNode) GetTotalAssists() int64`

GetTotalAssists returns the TotalAssists field if non-nil, zero value otherwise.

### GetTotalAssistsOk

`func (o *ItemFlowNode) GetTotalAssistsOk() (*int64, bool)`

GetTotalAssistsOk returns a tuple with the TotalAssists field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalAssists

`func (o *ItemFlowNode) SetTotalAssists(v int64)`

SetTotalAssists sets TotalAssists field to given value.


### GetTotalDeaths

`func (o *ItemFlowNode) GetTotalDeaths() int64`

GetTotalDeaths returns the TotalDeaths field if non-nil, zero value otherwise.

### GetTotalDeathsOk

`func (o *ItemFlowNode) GetTotalDeathsOk() (*int64, bool)`

GetTotalDeathsOk returns a tuple with the TotalDeaths field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalDeaths

`func (o *ItemFlowNode) SetTotalDeaths(v int64)`

SetTotalDeaths sets TotalDeaths field to given value.


### GetTotalKills

`func (o *ItemFlowNode) GetTotalKills() int64`

GetTotalKills returns the TotalKills field if non-nil, zero value otherwise.

### GetTotalKillsOk

`func (o *ItemFlowNode) GetTotalKillsOk() (*int64, bool)`

GetTotalKillsOk returns a tuple with the TotalKills field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalKills

`func (o *ItemFlowNode) SetTotalKills(v int64)`

SetTotalKills sets TotalKills field to given value.


### GetWins

`func (o *ItemFlowNode) GetWins() int64`

GetWins returns the Wins field if non-nil, zero value otherwise.

### GetWinsOk

`func (o *ItemFlowNode) GetWinsOk() (*int64, bool)`

GetWinsOk returns a tuple with the Wins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWins

`func (o *ItemFlowNode) SetWins(v int64)`

SetWins sets Wins field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


