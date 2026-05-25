# BuildItemStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Builds** | **int64** |  | 
**ItemId** | **int64** | See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | 

## Methods

### NewBuildItemStats

`func NewBuildItemStats(builds int64, itemId int64, ) *BuildItemStats`

NewBuildItemStats instantiates a new BuildItemStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBuildItemStatsWithDefaults

`func NewBuildItemStatsWithDefaults() *BuildItemStats`

NewBuildItemStatsWithDefaults instantiates a new BuildItemStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBuilds

`func (o *BuildItemStats) GetBuilds() int64`

GetBuilds returns the Builds field if non-nil, zero value otherwise.

### GetBuildsOk

`func (o *BuildItemStats) GetBuildsOk() (*int64, bool)`

GetBuildsOk returns a tuple with the Builds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuilds

`func (o *BuildItemStats) SetBuilds(v int64)`

SetBuilds sets Builds field to given value.


### GetItemId

`func (o *BuildItemStats) GetItemId() int64`

GetItemId returns the ItemId field if non-nil, zero value otherwise.

### GetItemIdOk

`func (o *BuildItemStats) GetItemIdOk() (*int64, bool)`

GetItemIdOk returns a tuple with the ItemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemId

`func (o *BuildItemStats) SetItemId(v int64)`

SetItemId sets ItemId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


