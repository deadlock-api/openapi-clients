# GameServerInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CurrentPlayerCount** | **int32** |  | 
**GameMode** | **string** |  | 
**Hostname** | Pointer to **NullableString** |  | [optional] 
**Ip** | **string** |  | 
**LastUpdated** | **string** |  | 
**Port** | **int32** |  | 
**Region** | **string** |  | 
**ServerId** | **string** |  | 

## Methods

### NewGameServerInfo

`func NewGameServerInfo(currentPlayerCount int32, gameMode string, ip string, lastUpdated string, port int32, region string, serverId string, ) *GameServerInfo`

NewGameServerInfo instantiates a new GameServerInfo object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGameServerInfoWithDefaults

`func NewGameServerInfoWithDefaults() *GameServerInfo`

NewGameServerInfoWithDefaults instantiates a new GameServerInfo object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCurrentPlayerCount

`func (o *GameServerInfo) GetCurrentPlayerCount() int32`

GetCurrentPlayerCount returns the CurrentPlayerCount field if non-nil, zero value otherwise.

### GetCurrentPlayerCountOk

`func (o *GameServerInfo) GetCurrentPlayerCountOk() (*int32, bool)`

GetCurrentPlayerCountOk returns a tuple with the CurrentPlayerCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrentPlayerCount

`func (o *GameServerInfo) SetCurrentPlayerCount(v int32)`

SetCurrentPlayerCount sets CurrentPlayerCount field to given value.


### GetGameMode

`func (o *GameServerInfo) GetGameMode() string`

GetGameMode returns the GameMode field if non-nil, zero value otherwise.

### GetGameModeOk

`func (o *GameServerInfo) GetGameModeOk() (*string, bool)`

GetGameModeOk returns a tuple with the GameMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGameMode

`func (o *GameServerInfo) SetGameMode(v string)`

SetGameMode sets GameMode field to given value.


### GetHostname

`func (o *GameServerInfo) GetHostname() string`

GetHostname returns the Hostname field if non-nil, zero value otherwise.

### GetHostnameOk

`func (o *GameServerInfo) GetHostnameOk() (*string, bool)`

GetHostnameOk returns a tuple with the Hostname field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHostname

`func (o *GameServerInfo) SetHostname(v string)`

SetHostname sets Hostname field to given value.

### HasHostname

`func (o *GameServerInfo) HasHostname() bool`

HasHostname returns a boolean if a field has been set.

### SetHostnameNil

`func (o *GameServerInfo) SetHostnameNil(b bool)`

 SetHostnameNil sets the value for Hostname to be an explicit nil

### UnsetHostname
`func (o *GameServerInfo) UnsetHostname()`

UnsetHostname ensures that no value is present for Hostname, not even an explicit nil
### GetIp

`func (o *GameServerInfo) GetIp() string`

GetIp returns the Ip field if non-nil, zero value otherwise.

### GetIpOk

`func (o *GameServerInfo) GetIpOk() (*string, bool)`

GetIpOk returns a tuple with the Ip field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIp

`func (o *GameServerInfo) SetIp(v string)`

SetIp sets Ip field to given value.


### GetLastUpdated

`func (o *GameServerInfo) GetLastUpdated() string`

GetLastUpdated returns the LastUpdated field if non-nil, zero value otherwise.

### GetLastUpdatedOk

`func (o *GameServerInfo) GetLastUpdatedOk() (*string, bool)`

GetLastUpdatedOk returns a tuple with the LastUpdated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastUpdated

`func (o *GameServerInfo) SetLastUpdated(v string)`

SetLastUpdated sets LastUpdated field to given value.


### GetPort

`func (o *GameServerInfo) GetPort() int32`

GetPort returns the Port field if non-nil, zero value otherwise.

### GetPortOk

`func (o *GameServerInfo) GetPortOk() (*int32, bool)`

GetPortOk returns a tuple with the Port field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPort

`func (o *GameServerInfo) SetPort(v int32)`

SetPort sets Port field to given value.


### GetRegion

`func (o *GameServerInfo) GetRegion() string`

GetRegion returns the Region field if non-nil, zero value otherwise.

### GetRegionOk

`func (o *GameServerInfo) GetRegionOk() (*string, bool)`

GetRegionOk returns a tuple with the Region field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegion

`func (o *GameServerInfo) SetRegion(v string)`

SetRegion sets Region field to given value.


### GetServerId

`func (o *GameServerInfo) GetServerId() string`

GetServerId returns the ServerId field if non-nil, zero value otherwise.

### GetServerIdOk

`func (o *GameServerInfo) GetServerIdOk() (*string, bool)`

GetServerIdOk returns a tuple with the ServerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetServerId

`func (o *GameServerInfo) SetServerId(v string)`

SetServerId sets ServerId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


