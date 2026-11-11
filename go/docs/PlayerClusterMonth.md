# PlayerClusterMonth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClusterId** | **int32** | The server cluster the matches were played on. | 
**Datacenter** | Pointer to **NullableString** | Datacenter(s) of the cluster&#39;s servers, e.g. &#x60;fra2&#x60;; comma-separated if the cluster spans several. &#x60;null&#x60; if the cluster has not been seen in a replay yet. | [optional] 
**Matches** | **int64** | Number of the player&#39;s matches on this cluster in this month. | 
**Month** | **int32** | Unix timestamp of the first day of the month (UTC). | 
**Region** | Pointer to **NullableString** | Region of the cluster&#39;s servers, e.g. &#x60;eu_west&#x60; or &#x60;us_north_central&#x60;. &#x60;null&#x60; if the cluster has not been seen in a replay yet. | [optional] 

## Methods

### NewPlayerClusterMonth

`func NewPlayerClusterMonth(clusterId int32, matches int64, month int32, ) *PlayerClusterMonth`

NewPlayerClusterMonth instantiates a new PlayerClusterMonth object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPlayerClusterMonthWithDefaults

`func NewPlayerClusterMonthWithDefaults() *PlayerClusterMonth`

NewPlayerClusterMonthWithDefaults instantiates a new PlayerClusterMonth object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClusterId

`func (o *PlayerClusterMonth) GetClusterId() int32`

GetClusterId returns the ClusterId field if non-nil, zero value otherwise.

### GetClusterIdOk

`func (o *PlayerClusterMonth) GetClusterIdOk() (*int32, bool)`

GetClusterIdOk returns a tuple with the ClusterId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClusterId

`func (o *PlayerClusterMonth) SetClusterId(v int32)`

SetClusterId sets ClusterId field to given value.


### GetDatacenter

`func (o *PlayerClusterMonth) GetDatacenter() string`

GetDatacenter returns the Datacenter field if non-nil, zero value otherwise.

### GetDatacenterOk

`func (o *PlayerClusterMonth) GetDatacenterOk() (*string, bool)`

GetDatacenterOk returns a tuple with the Datacenter field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDatacenter

`func (o *PlayerClusterMonth) SetDatacenter(v string)`

SetDatacenter sets Datacenter field to given value.

### HasDatacenter

`func (o *PlayerClusterMonth) HasDatacenter() bool`

HasDatacenter returns a boolean if a field has been set.

### SetDatacenterNil

`func (o *PlayerClusterMonth) SetDatacenterNil(b bool)`

 SetDatacenterNil sets the value for Datacenter to be an explicit nil

### UnsetDatacenter
`func (o *PlayerClusterMonth) UnsetDatacenter()`

UnsetDatacenter ensures that no value is present for Datacenter, not even an explicit nil
### GetMatches

`func (o *PlayerClusterMonth) GetMatches() int64`

GetMatches returns the Matches field if non-nil, zero value otherwise.

### GetMatchesOk

`func (o *PlayerClusterMonth) GetMatchesOk() (*int64, bool)`

GetMatchesOk returns a tuple with the Matches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatches

`func (o *PlayerClusterMonth) SetMatches(v int64)`

SetMatches sets Matches field to given value.


### GetMonth

`func (o *PlayerClusterMonth) GetMonth() int32`

GetMonth returns the Month field if non-nil, zero value otherwise.

### GetMonthOk

`func (o *PlayerClusterMonth) GetMonthOk() (*int32, bool)`

GetMonthOk returns a tuple with the Month field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMonth

`func (o *PlayerClusterMonth) SetMonth(v int32)`

SetMonth sets Month field to given value.


### GetRegion

`func (o *PlayerClusterMonth) GetRegion() string`

GetRegion returns the Region field if non-nil, zero value otherwise.

### GetRegionOk

`func (o *PlayerClusterMonth) GetRegionOk() (*string, bool)`

GetRegionOk returns a tuple with the Region field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegion

`func (o *PlayerClusterMonth) SetRegion(v string)`

SetRegion sets Region field to given value.

### HasRegion

`func (o *PlayerClusterMonth) HasRegion() bool`

HasRegion returns a boolean if a field has been set.

### SetRegionNil

`func (o *PlayerClusterMonth) SetRegionNil(b bool)`

 SetRegionNil sets the value for Region to be an explicit nil

### UnsetRegion
`func (o *PlayerClusterMonth) UnsetRegion()`

UnsetRegion ensures that no value is present for Region, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


