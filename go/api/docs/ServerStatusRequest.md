# ServerStatusRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CurrentPlayerCount** | **int32** | Current number of players on this server | 
**GameMode** | **string** | Game mode this server is running (e.g. \&quot;ranked\&quot;, \&quot;unranked\&quot;) | 
**Ip** | **string** | IP address of the game server | 
**Port** | **int32** | Port the game server is listening on | 
**Region** | **string** | Region the server is located in (e.g. \&quot;eu\&quot;, \&quot;na\&quot;, \&quot;sa\&quot;, \&quot;asia\&quot;, \&quot;oceania\&quot;) | 
**ServerId** | **string** | Unique identifier for the game server | 

## Methods

### NewServerStatusRequest

`func NewServerStatusRequest(currentPlayerCount int32, gameMode string, ip string, port int32, region string, serverId string, ) *ServerStatusRequest`

NewServerStatusRequest instantiates a new ServerStatusRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewServerStatusRequestWithDefaults

`func NewServerStatusRequestWithDefaults() *ServerStatusRequest`

NewServerStatusRequestWithDefaults instantiates a new ServerStatusRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCurrentPlayerCount

`func (o *ServerStatusRequest) GetCurrentPlayerCount() int32`

GetCurrentPlayerCount returns the CurrentPlayerCount field if non-nil, zero value otherwise.

### GetCurrentPlayerCountOk

`func (o *ServerStatusRequest) GetCurrentPlayerCountOk() (*int32, bool)`

GetCurrentPlayerCountOk returns a tuple with the CurrentPlayerCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrentPlayerCount

`func (o *ServerStatusRequest) SetCurrentPlayerCount(v int32)`

SetCurrentPlayerCount sets CurrentPlayerCount field to given value.


### GetGameMode

`func (o *ServerStatusRequest) GetGameMode() string`

GetGameMode returns the GameMode field if non-nil, zero value otherwise.

### GetGameModeOk

`func (o *ServerStatusRequest) GetGameModeOk() (*string, bool)`

GetGameModeOk returns a tuple with the GameMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGameMode

`func (o *ServerStatusRequest) SetGameMode(v string)`

SetGameMode sets GameMode field to given value.


### GetIp

`func (o *ServerStatusRequest) GetIp() string`

GetIp returns the Ip field if non-nil, zero value otherwise.

### GetIpOk

`func (o *ServerStatusRequest) GetIpOk() (*string, bool)`

GetIpOk returns a tuple with the Ip field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIp

`func (o *ServerStatusRequest) SetIp(v string)`

SetIp sets Ip field to given value.


### GetPort

`func (o *ServerStatusRequest) GetPort() int32`

GetPort returns the Port field if non-nil, zero value otherwise.

### GetPortOk

`func (o *ServerStatusRequest) GetPortOk() (*int32, bool)`

GetPortOk returns a tuple with the Port field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPort

`func (o *ServerStatusRequest) SetPort(v int32)`

SetPort sets Port field to given value.


### GetRegion

`func (o *ServerStatusRequest) GetRegion() string`

GetRegion returns the Region field if non-nil, zero value otherwise.

### GetRegionOk

`func (o *ServerStatusRequest) GetRegionOk() (*string, bool)`

GetRegionOk returns a tuple with the Region field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegion

`func (o *ServerStatusRequest) SetRegion(v string)`

SetRegion sets Region field to given value.


### GetServerId

`func (o *ServerStatusRequest) GetServerId() string`

GetServerId returns the ServerId field if non-nil, zero value otherwise.

### GetServerIdOk

`func (o *ServerStatusRequest) GetServerIdOk() (*string, bool)`

GetServerIdOk returns a tuple with the ServerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetServerId

`func (o *ServerStatusRequest) SetServerId(v string)`

SetServerId sets ServerId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


