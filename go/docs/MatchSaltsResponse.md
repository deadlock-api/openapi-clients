# MatchSaltsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClusterId** | Pointer to **NullableInt32** |  | [optional] 
**DemoUrl** | Pointer to **NullableString** |  | [optional] 
**MatchId** | **int64** |  | 
**MetadataSalt** | Pointer to **NullableInt32** |  | [optional] 
**MetadataUrl** | Pointer to **NullableString** |  | [optional] 
**ReplaySalt** | Pointer to **NullableInt32** |  | [optional] 

## Methods

### NewMatchSaltsResponse

`func NewMatchSaltsResponse(matchId int64, ) *MatchSaltsResponse`

NewMatchSaltsResponse instantiates a new MatchSaltsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMatchSaltsResponseWithDefaults

`func NewMatchSaltsResponseWithDefaults() *MatchSaltsResponse`

NewMatchSaltsResponseWithDefaults instantiates a new MatchSaltsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClusterId

`func (o *MatchSaltsResponse) GetClusterId() int32`

GetClusterId returns the ClusterId field if non-nil, zero value otherwise.

### GetClusterIdOk

`func (o *MatchSaltsResponse) GetClusterIdOk() (*int32, bool)`

GetClusterIdOk returns a tuple with the ClusterId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClusterId

`func (o *MatchSaltsResponse) SetClusterId(v int32)`

SetClusterId sets ClusterId field to given value.

### HasClusterId

`func (o *MatchSaltsResponse) HasClusterId() bool`

HasClusterId returns a boolean if a field has been set.

### SetClusterIdNil

`func (o *MatchSaltsResponse) SetClusterIdNil(b bool)`

 SetClusterIdNil sets the value for ClusterId to be an explicit nil

### UnsetClusterId
`func (o *MatchSaltsResponse) UnsetClusterId()`

UnsetClusterId ensures that no value is present for ClusterId, not even an explicit nil
### GetDemoUrl

`func (o *MatchSaltsResponse) GetDemoUrl() string`

GetDemoUrl returns the DemoUrl field if non-nil, zero value otherwise.

### GetDemoUrlOk

`func (o *MatchSaltsResponse) GetDemoUrlOk() (*string, bool)`

GetDemoUrlOk returns a tuple with the DemoUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDemoUrl

`func (o *MatchSaltsResponse) SetDemoUrl(v string)`

SetDemoUrl sets DemoUrl field to given value.

### HasDemoUrl

`func (o *MatchSaltsResponse) HasDemoUrl() bool`

HasDemoUrl returns a boolean if a field has been set.

### SetDemoUrlNil

`func (o *MatchSaltsResponse) SetDemoUrlNil(b bool)`

 SetDemoUrlNil sets the value for DemoUrl to be an explicit nil

### UnsetDemoUrl
`func (o *MatchSaltsResponse) UnsetDemoUrl()`

UnsetDemoUrl ensures that no value is present for DemoUrl, not even an explicit nil
### GetMatchId

`func (o *MatchSaltsResponse) GetMatchId() int64`

GetMatchId returns the MatchId field if non-nil, zero value otherwise.

### GetMatchIdOk

`func (o *MatchSaltsResponse) GetMatchIdOk() (*int64, bool)`

GetMatchIdOk returns a tuple with the MatchId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchId

`func (o *MatchSaltsResponse) SetMatchId(v int64)`

SetMatchId sets MatchId field to given value.


### GetMetadataSalt

`func (o *MatchSaltsResponse) GetMetadataSalt() int32`

GetMetadataSalt returns the MetadataSalt field if non-nil, zero value otherwise.

### GetMetadataSaltOk

`func (o *MatchSaltsResponse) GetMetadataSaltOk() (*int32, bool)`

GetMetadataSaltOk returns a tuple with the MetadataSalt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadataSalt

`func (o *MatchSaltsResponse) SetMetadataSalt(v int32)`

SetMetadataSalt sets MetadataSalt field to given value.

### HasMetadataSalt

`func (o *MatchSaltsResponse) HasMetadataSalt() bool`

HasMetadataSalt returns a boolean if a field has been set.

### SetMetadataSaltNil

`func (o *MatchSaltsResponse) SetMetadataSaltNil(b bool)`

 SetMetadataSaltNil sets the value for MetadataSalt to be an explicit nil

### UnsetMetadataSalt
`func (o *MatchSaltsResponse) UnsetMetadataSalt()`

UnsetMetadataSalt ensures that no value is present for MetadataSalt, not even an explicit nil
### GetMetadataUrl

`func (o *MatchSaltsResponse) GetMetadataUrl() string`

GetMetadataUrl returns the MetadataUrl field if non-nil, zero value otherwise.

### GetMetadataUrlOk

`func (o *MatchSaltsResponse) GetMetadataUrlOk() (*string, bool)`

GetMetadataUrlOk returns a tuple with the MetadataUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadataUrl

`func (o *MatchSaltsResponse) SetMetadataUrl(v string)`

SetMetadataUrl sets MetadataUrl field to given value.

### HasMetadataUrl

`func (o *MatchSaltsResponse) HasMetadataUrl() bool`

HasMetadataUrl returns a boolean if a field has been set.

### SetMetadataUrlNil

`func (o *MatchSaltsResponse) SetMetadataUrlNil(b bool)`

 SetMetadataUrlNil sets the value for MetadataUrl to be an explicit nil

### UnsetMetadataUrl
`func (o *MatchSaltsResponse) UnsetMetadataUrl()`

UnsetMetadataUrl ensures that no value is present for MetadataUrl, not even an explicit nil
### GetReplaySalt

`func (o *MatchSaltsResponse) GetReplaySalt() int32`

GetReplaySalt returns the ReplaySalt field if non-nil, zero value otherwise.

### GetReplaySaltOk

`func (o *MatchSaltsResponse) GetReplaySaltOk() (*int32, bool)`

GetReplaySaltOk returns a tuple with the ReplaySalt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReplaySalt

`func (o *MatchSaltsResponse) SetReplaySalt(v int32)`

SetReplaySalt sets ReplaySalt field to given value.

### HasReplaySalt

`func (o *MatchSaltsResponse) HasReplaySalt() bool`

HasReplaySalt returns a boolean if a field has been set.

### SetReplaySaltNil

`func (o *MatchSaltsResponse) SetReplaySaltNil(b bool)`

 SetReplaySaltNil sets the value for ReplaySalt to be an explicit nil

### UnsetReplaySalt
`func (o *MatchSaltsResponse) UnsetReplaySalt()`

UnsetReplaySalt ensures that no value is present for ReplaySalt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


