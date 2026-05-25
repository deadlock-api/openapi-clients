# SteamServer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Addr** | **string** | Full address of the server including port (e.g. &#x60;1.2.3.4:27015&#x60;) | 
**Appid** | **int32** | Steam appid of the game running on this server | 
**Bots** | **int32** | Number of bots on the server | 
**Dedicated** | **bool** | Whether this is a dedicated server | 
**Gamedir** | **string** | Internal game directory name | 
**Gameport** | **int32** | Game port the server is listening on | 
**Gametype** | **string** | Steam gametype tags | 
**Map** | **string** | Current map | 
**MaxPlayers** | **int32** | Maximum player count | 
**Name** | **string** | Server name as advertised to Steam | 
**Os** | **string** | Operating system the server is running on (e.g. &#x60;l&#x60; for Linux, &#x60;w&#x60; for Windows) | 
**Players** | **int32** | Current player count | 
**Product** | **string** | Product identifier reported by the server | 
**Region** | **int32** | Steam region code reported by the server | 
**Secure** | **bool** | Whether the server is VAC-secured | 
**Steamid** | **string** | &#x60;SteamID&#x60; of the server | 
**Version** | **string** | Server build version | 

## Methods

### NewSteamServer

`func NewSteamServer(addr string, appid int32, bots int32, dedicated bool, gamedir string, gameport int32, gametype string, map_ string, maxPlayers int32, name string, os string, players int32, product string, region int32, secure bool, steamid string, version string, ) *SteamServer`

NewSteamServer instantiates a new SteamServer object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSteamServerWithDefaults

`func NewSteamServerWithDefaults() *SteamServer`

NewSteamServerWithDefaults instantiates a new SteamServer object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAddr

`func (o *SteamServer) GetAddr() string`

GetAddr returns the Addr field if non-nil, zero value otherwise.

### GetAddrOk

`func (o *SteamServer) GetAddrOk() (*string, bool)`

GetAddrOk returns a tuple with the Addr field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddr

`func (o *SteamServer) SetAddr(v string)`

SetAddr sets Addr field to given value.


### GetAppid

`func (o *SteamServer) GetAppid() int32`

GetAppid returns the Appid field if non-nil, zero value otherwise.

### GetAppidOk

`func (o *SteamServer) GetAppidOk() (*int32, bool)`

GetAppidOk returns a tuple with the Appid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAppid

`func (o *SteamServer) SetAppid(v int32)`

SetAppid sets Appid field to given value.


### GetBots

`func (o *SteamServer) GetBots() int32`

GetBots returns the Bots field if non-nil, zero value otherwise.

### GetBotsOk

`func (o *SteamServer) GetBotsOk() (*int32, bool)`

GetBotsOk returns a tuple with the Bots field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBots

`func (o *SteamServer) SetBots(v int32)`

SetBots sets Bots field to given value.


### GetDedicated

`func (o *SteamServer) GetDedicated() bool`

GetDedicated returns the Dedicated field if non-nil, zero value otherwise.

### GetDedicatedOk

`func (o *SteamServer) GetDedicatedOk() (*bool, bool)`

GetDedicatedOk returns a tuple with the Dedicated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDedicated

`func (o *SteamServer) SetDedicated(v bool)`

SetDedicated sets Dedicated field to given value.


### GetGamedir

`func (o *SteamServer) GetGamedir() string`

GetGamedir returns the Gamedir field if non-nil, zero value otherwise.

### GetGamedirOk

`func (o *SteamServer) GetGamedirOk() (*string, bool)`

GetGamedirOk returns a tuple with the Gamedir field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGamedir

`func (o *SteamServer) SetGamedir(v string)`

SetGamedir sets Gamedir field to given value.


### GetGameport

`func (o *SteamServer) GetGameport() int32`

GetGameport returns the Gameport field if non-nil, zero value otherwise.

### GetGameportOk

`func (o *SteamServer) GetGameportOk() (*int32, bool)`

GetGameportOk returns a tuple with the Gameport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGameport

`func (o *SteamServer) SetGameport(v int32)`

SetGameport sets Gameport field to given value.


### GetGametype

`func (o *SteamServer) GetGametype() string`

GetGametype returns the Gametype field if non-nil, zero value otherwise.

### GetGametypeOk

`func (o *SteamServer) GetGametypeOk() (*string, bool)`

GetGametypeOk returns a tuple with the Gametype field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGametype

`func (o *SteamServer) SetGametype(v string)`

SetGametype sets Gametype field to given value.


### GetMap

`func (o *SteamServer) GetMap() string`

GetMap returns the Map field if non-nil, zero value otherwise.

### GetMapOk

`func (o *SteamServer) GetMapOk() (*string, bool)`

GetMapOk returns a tuple with the Map field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMap

`func (o *SteamServer) SetMap(v string)`

SetMap sets Map field to given value.


### GetMaxPlayers

`func (o *SteamServer) GetMaxPlayers() int32`

GetMaxPlayers returns the MaxPlayers field if non-nil, zero value otherwise.

### GetMaxPlayersOk

`func (o *SteamServer) GetMaxPlayersOk() (*int32, bool)`

GetMaxPlayersOk returns a tuple with the MaxPlayers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxPlayers

`func (o *SteamServer) SetMaxPlayers(v int32)`

SetMaxPlayers sets MaxPlayers field to given value.


### GetName

`func (o *SteamServer) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *SteamServer) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *SteamServer) SetName(v string)`

SetName sets Name field to given value.


### GetOs

`func (o *SteamServer) GetOs() string`

GetOs returns the Os field if non-nil, zero value otherwise.

### GetOsOk

`func (o *SteamServer) GetOsOk() (*string, bool)`

GetOsOk returns a tuple with the Os field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOs

`func (o *SteamServer) SetOs(v string)`

SetOs sets Os field to given value.


### GetPlayers

`func (o *SteamServer) GetPlayers() int32`

GetPlayers returns the Players field if non-nil, zero value otherwise.

### GetPlayersOk

`func (o *SteamServer) GetPlayersOk() (*int32, bool)`

GetPlayersOk returns a tuple with the Players field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayers

`func (o *SteamServer) SetPlayers(v int32)`

SetPlayers sets Players field to given value.


### GetProduct

`func (o *SteamServer) GetProduct() string`

GetProduct returns the Product field if non-nil, zero value otherwise.

### GetProductOk

`func (o *SteamServer) GetProductOk() (*string, bool)`

GetProductOk returns a tuple with the Product field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProduct

`func (o *SteamServer) SetProduct(v string)`

SetProduct sets Product field to given value.


### GetRegion

`func (o *SteamServer) GetRegion() int32`

GetRegion returns the Region field if non-nil, zero value otherwise.

### GetRegionOk

`func (o *SteamServer) GetRegionOk() (*int32, bool)`

GetRegionOk returns a tuple with the Region field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegion

`func (o *SteamServer) SetRegion(v int32)`

SetRegion sets Region field to given value.


### GetSecure

`func (o *SteamServer) GetSecure() bool`

GetSecure returns the Secure field if non-nil, zero value otherwise.

### GetSecureOk

`func (o *SteamServer) GetSecureOk() (*bool, bool)`

GetSecureOk returns a tuple with the Secure field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecure

`func (o *SteamServer) SetSecure(v bool)`

SetSecure sets Secure field to given value.


### GetSteamid

`func (o *SteamServer) GetSteamid() string`

GetSteamid returns the Steamid field if non-nil, zero value otherwise.

### GetSteamidOk

`func (o *SteamServer) GetSteamidOk() (*string, bool)`

GetSteamidOk returns a tuple with the Steamid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSteamid

`func (o *SteamServer) SetSteamid(v string)`

SetSteamid sets Steamid field to given value.


### GetVersion

`func (o *SteamServer) GetVersion() string`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *SteamServer) GetVersionOk() (*string, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *SteamServer) SetVersion(v string)`

SetVersion sets Version field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


