# ItemFlowStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Baseline** | [**ItemFlowSummary**](ItemFlowSummary.md) | Totals ignoring the locked build path (item filters only). Denominator for chained pick rate. | 
**Edges** | [**[]ItemFlowEdge**](ItemFlowEdge.md) |  | 
**LeaveOneOut** | [**[]ItemFlowLeaveOneOut**](ItemFlowLeaveOneOut.md) | One entry per locked item, in request order: the totals of the locked build path without that item. &#x60;summary&#x60; against an entry is what that one item adds to the build. Empty without locks. | 
**Nodes** | [**[]ItemFlowNode**](ItemFlowNode.md) |  | 
**ReachedPerColumn** | **[]int64** | Distinct baseline games that bought any upgrade in each stage column (index &#x3D; column). &#x60;reached / baseline.matches&#x60; shows how survivorship-selected a (late) stage is. | 
**ReachedWinsPerColumn** | Pointer to **[]int64** | Of &#x60;reached_per_column&#x60;, the games that were won (index &#x3D; column). &#x60;reached_wins / reached&#x60; is the win rate of games that got that far, the fair baseline for a build ending there. | [optional] 
**Summary** | [**ItemFlowSummary**](ItemFlowSummary.md) | Totals for the locked build-path population (all filters applied). Denominator for pick rate. | 
**SummaryReachedPerColumn** | Pointer to **[]int64** | &#x60;reached_per_column&#x60; for the locked build path&#39;s games (&#x60;summary&#x60;). Late stages hold long games only, so an item bought there is compared with the build&#39;s games that got that far. | [optional] 
**SummaryReachedWinsPerColumn** | Pointer to **[]int64** | Of &#x60;summary_reached_per_column&#x60;, the games that were won (index &#x3D; column). | [optional] 

## Methods

### NewItemFlowStats

`func NewItemFlowStats(baseline ItemFlowSummary, edges []ItemFlowEdge, leaveOneOut []ItemFlowLeaveOneOut, nodes []ItemFlowNode, reachedPerColumn []int64, summary ItemFlowSummary, ) *ItemFlowStats`

NewItemFlowStats instantiates a new ItemFlowStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewItemFlowStatsWithDefaults

`func NewItemFlowStatsWithDefaults() *ItemFlowStats`

NewItemFlowStatsWithDefaults instantiates a new ItemFlowStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBaseline

`func (o *ItemFlowStats) GetBaseline() ItemFlowSummary`

GetBaseline returns the Baseline field if non-nil, zero value otherwise.

### GetBaselineOk

`func (o *ItemFlowStats) GetBaselineOk() (*ItemFlowSummary, bool)`

GetBaselineOk returns a tuple with the Baseline field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaseline

`func (o *ItemFlowStats) SetBaseline(v ItemFlowSummary)`

SetBaseline sets Baseline field to given value.


### GetEdges

`func (o *ItemFlowStats) GetEdges() []ItemFlowEdge`

GetEdges returns the Edges field if non-nil, zero value otherwise.

### GetEdgesOk

`func (o *ItemFlowStats) GetEdgesOk() (*[]ItemFlowEdge, bool)`

GetEdgesOk returns a tuple with the Edges field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEdges

`func (o *ItemFlowStats) SetEdges(v []ItemFlowEdge)`

SetEdges sets Edges field to given value.


### GetLeaveOneOut

`func (o *ItemFlowStats) GetLeaveOneOut() []ItemFlowLeaveOneOut`

GetLeaveOneOut returns the LeaveOneOut field if non-nil, zero value otherwise.

### GetLeaveOneOutOk

`func (o *ItemFlowStats) GetLeaveOneOutOk() (*[]ItemFlowLeaveOneOut, bool)`

GetLeaveOneOutOk returns a tuple with the LeaveOneOut field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLeaveOneOut

`func (o *ItemFlowStats) SetLeaveOneOut(v []ItemFlowLeaveOneOut)`

SetLeaveOneOut sets LeaveOneOut field to given value.


### GetNodes

`func (o *ItemFlowStats) GetNodes() []ItemFlowNode`

GetNodes returns the Nodes field if non-nil, zero value otherwise.

### GetNodesOk

`func (o *ItemFlowStats) GetNodesOk() (*[]ItemFlowNode, bool)`

GetNodesOk returns a tuple with the Nodes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNodes

`func (o *ItemFlowStats) SetNodes(v []ItemFlowNode)`

SetNodes sets Nodes field to given value.


### GetReachedPerColumn

`func (o *ItemFlowStats) GetReachedPerColumn() []int64`

GetReachedPerColumn returns the ReachedPerColumn field if non-nil, zero value otherwise.

### GetReachedPerColumnOk

`func (o *ItemFlowStats) GetReachedPerColumnOk() (*[]int64, bool)`

GetReachedPerColumnOk returns a tuple with the ReachedPerColumn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReachedPerColumn

`func (o *ItemFlowStats) SetReachedPerColumn(v []int64)`

SetReachedPerColumn sets ReachedPerColumn field to given value.


### GetReachedWinsPerColumn

`func (o *ItemFlowStats) GetReachedWinsPerColumn() []int64`

GetReachedWinsPerColumn returns the ReachedWinsPerColumn field if non-nil, zero value otherwise.

### GetReachedWinsPerColumnOk

`func (o *ItemFlowStats) GetReachedWinsPerColumnOk() (*[]int64, bool)`

GetReachedWinsPerColumnOk returns a tuple with the ReachedWinsPerColumn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReachedWinsPerColumn

`func (o *ItemFlowStats) SetReachedWinsPerColumn(v []int64)`

SetReachedWinsPerColumn sets ReachedWinsPerColumn field to given value.

### HasReachedWinsPerColumn

`func (o *ItemFlowStats) HasReachedWinsPerColumn() bool`

HasReachedWinsPerColumn returns a boolean if a field has been set.

### GetSummary

`func (o *ItemFlowStats) GetSummary() ItemFlowSummary`

GetSummary returns the Summary field if non-nil, zero value otherwise.

### GetSummaryOk

`func (o *ItemFlowStats) GetSummaryOk() (*ItemFlowSummary, bool)`

GetSummaryOk returns a tuple with the Summary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSummary

`func (o *ItemFlowStats) SetSummary(v ItemFlowSummary)`

SetSummary sets Summary field to given value.


### GetSummaryReachedPerColumn

`func (o *ItemFlowStats) GetSummaryReachedPerColumn() []int64`

GetSummaryReachedPerColumn returns the SummaryReachedPerColumn field if non-nil, zero value otherwise.

### GetSummaryReachedPerColumnOk

`func (o *ItemFlowStats) GetSummaryReachedPerColumnOk() (*[]int64, bool)`

GetSummaryReachedPerColumnOk returns a tuple with the SummaryReachedPerColumn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSummaryReachedPerColumn

`func (o *ItemFlowStats) SetSummaryReachedPerColumn(v []int64)`

SetSummaryReachedPerColumn sets SummaryReachedPerColumn field to given value.

### HasSummaryReachedPerColumn

`func (o *ItemFlowStats) HasSummaryReachedPerColumn() bool`

HasSummaryReachedPerColumn returns a boolean if a field has been set.

### GetSummaryReachedWinsPerColumn

`func (o *ItemFlowStats) GetSummaryReachedWinsPerColumn() []int64`

GetSummaryReachedWinsPerColumn returns the SummaryReachedWinsPerColumn field if non-nil, zero value otherwise.

### GetSummaryReachedWinsPerColumnOk

`func (o *ItemFlowStats) GetSummaryReachedWinsPerColumnOk() (*[]int64, bool)`

GetSummaryReachedWinsPerColumnOk returns a tuple with the SummaryReachedWinsPerColumn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSummaryReachedWinsPerColumn

`func (o *ItemFlowStats) SetSummaryReachedWinsPerColumn(v []int64)`

SetSummaryReachedWinsPerColumn sets SummaryReachedWinsPerColumn field to given value.

### HasSummaryReachedWinsPerColumn

`func (o *ItemFlowStats) HasSummaryReachedWinsPerColumn() bool`

HasSummaryReachedWinsPerColumn returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


