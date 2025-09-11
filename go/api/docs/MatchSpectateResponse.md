# MatchSpectateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BroadcastUrl** | **string** |  | 
**LobbyId** | Pointer to **NullableInt64** |  | [optional] 

## Methods

### NewMatchSpectateResponse

`func NewMatchSpectateResponse(broadcastUrl string, ) *MatchSpectateResponse`

NewMatchSpectateResponse instantiates a new MatchSpectateResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMatchSpectateResponseWithDefaults

`func NewMatchSpectateResponseWithDefaults() *MatchSpectateResponse`

NewMatchSpectateResponseWithDefaults instantiates a new MatchSpectateResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBroadcastUrl

`func (o *MatchSpectateResponse) GetBroadcastUrl() string`

GetBroadcastUrl returns the BroadcastUrl field if non-nil, zero value otherwise.

### GetBroadcastUrlOk

`func (o *MatchSpectateResponse) GetBroadcastUrlOk() (*string, bool)`

GetBroadcastUrlOk returns a tuple with the BroadcastUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBroadcastUrl

`func (o *MatchSpectateResponse) SetBroadcastUrl(v string)`

SetBroadcastUrl sets BroadcastUrl field to given value.


### GetLobbyId

`func (o *MatchSpectateResponse) GetLobbyId() int64`

GetLobbyId returns the LobbyId field if non-nil, zero value otherwise.

### GetLobbyIdOk

`func (o *MatchSpectateResponse) GetLobbyIdOk() (*int64, bool)`

GetLobbyIdOk returns a tuple with the LobbyId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLobbyId

`func (o *MatchSpectateResponse) SetLobbyId(v int64)`

SetLobbyId sets LobbyId field to given value.

### HasLobbyId

`func (o *MatchSpectateResponse) HasLobbyId() bool`

HasLobbyId returns a boolean if a field has been set.

### SetLobbyIdNil

`func (o *MatchSpectateResponse) SetLobbyIdNil(b bool)`

 SetLobbyIdNil sets the value for LobbyId to be an explicit nil

### UnsetLobbyId
`func (o *MatchSpectateResponse) UnsetLobbyId()`

UnsetLobbyId ensures that no value is present for LobbyId, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


