# ServerStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ServerId** | **string** | The server ID that reported status | 
**TtlSecs** | **int64** | TTL in seconds before this registration expires | 

## Methods

### NewServerStatusResponse

`func NewServerStatusResponse(serverId string, ttlSecs int64, ) *ServerStatusResponse`

NewServerStatusResponse instantiates a new ServerStatusResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewServerStatusResponseWithDefaults

`func NewServerStatusResponseWithDefaults() *ServerStatusResponse`

NewServerStatusResponseWithDefaults instantiates a new ServerStatusResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetServerId

`func (o *ServerStatusResponse) GetServerId() string`

GetServerId returns the ServerId field if non-nil, zero value otherwise.

### GetServerIdOk

`func (o *ServerStatusResponse) GetServerIdOk() (*string, bool)`

GetServerIdOk returns a tuple with the ServerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetServerId

`func (o *ServerStatusResponse) SetServerId(v string)`

SetServerId sets ServerId field to given value.


### GetTtlSecs

`func (o *ServerStatusResponse) GetTtlSecs() int64`

GetTtlSecs returns the TtlSecs field if non-nil, zero value otherwise.

### GetTtlSecsOk

`func (o *ServerStatusResponse) GetTtlSecsOk() (*int64, bool)`

GetTtlSecsOk returns a tuple with the TtlSecs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTtlSecs

`func (o *ServerStatusResponse) SetTtlSecs(v int64)`

SetTtlSecs sets TtlSecs field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


