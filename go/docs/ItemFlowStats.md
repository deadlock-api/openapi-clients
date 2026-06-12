# ItemFlowStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Baseline** | [**ItemFlowSummary**](ItemFlowSummary.md) | Totals ignoring the locked build path (item filters only). Denominator for chained pick rate. | 
**Edges** | [**[]ItemFlowEdge**](ItemFlowEdge.md) |  | 
**Nodes** | [**[]ItemFlowNode**](ItemFlowNode.md) |  | 
**ReachedPerColumn** | **[]int64** | Distinct baseline games that bought any upgrade in each stage column (index &#x3D; column). &#x60;reached / baseline.matches&#x60; shows how survivorship-selected a (late) stage is. | 
**Summary** | [**ItemFlowSummary**](ItemFlowSummary.md) | Totals for the locked build-path population (all filters applied). Denominator for pick rate. | 

## Methods

### NewItemFlowStats

`func NewItemFlowStats(baseline ItemFlowSummary, edges []ItemFlowEdge, nodes []ItemFlowNode, reachedPerColumn []int64, summary ItemFlowSummary, ) *ItemFlowStats`

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



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


