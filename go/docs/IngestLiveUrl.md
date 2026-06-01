# IngestLiveUrl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BroadcastUrl** | **string** |  | 
**LobbyId** | Pointer to **NullableInt64** |  | [optional] 
**MatchId** | **int64** |  | 
**StartedAt** | Pointer to **NullableInt64** |  | [optional] 

## Methods

### NewIngestLiveUrl

`func NewIngestLiveUrl(broadcastUrl string, matchId int64, ) *IngestLiveUrl`

NewIngestLiveUrl instantiates a new IngestLiveUrl object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewIngestLiveUrlWithDefaults

`func NewIngestLiveUrlWithDefaults() *IngestLiveUrl`

NewIngestLiveUrlWithDefaults instantiates a new IngestLiveUrl object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBroadcastUrl

`func (o *IngestLiveUrl) GetBroadcastUrl() string`

GetBroadcastUrl returns the BroadcastUrl field if non-nil, zero value otherwise.

### GetBroadcastUrlOk

`func (o *IngestLiveUrl) GetBroadcastUrlOk() (*string, bool)`

GetBroadcastUrlOk returns a tuple with the BroadcastUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBroadcastUrl

`func (o *IngestLiveUrl) SetBroadcastUrl(v string)`

SetBroadcastUrl sets BroadcastUrl field to given value.


### GetLobbyId

`func (o *IngestLiveUrl) GetLobbyId() int64`

GetLobbyId returns the LobbyId field if non-nil, zero value otherwise.

### GetLobbyIdOk

`func (o *IngestLiveUrl) GetLobbyIdOk() (*int64, bool)`

GetLobbyIdOk returns a tuple with the LobbyId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLobbyId

`func (o *IngestLiveUrl) SetLobbyId(v int64)`

SetLobbyId sets LobbyId field to given value.

### HasLobbyId

`func (o *IngestLiveUrl) HasLobbyId() bool`

HasLobbyId returns a boolean if a field has been set.

### SetLobbyIdNil

`func (o *IngestLiveUrl) SetLobbyIdNil(b bool)`

 SetLobbyIdNil sets the value for LobbyId to be an explicit nil

### UnsetLobbyId
`func (o *IngestLiveUrl) UnsetLobbyId()`

UnsetLobbyId ensures that no value is present for LobbyId, not even an explicit nil
### GetMatchId

`func (o *IngestLiveUrl) GetMatchId() int64`

GetMatchId returns the MatchId field if non-nil, zero value otherwise.

### GetMatchIdOk

`func (o *IngestLiveUrl) GetMatchIdOk() (*int64, bool)`

GetMatchIdOk returns a tuple with the MatchId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchId

`func (o *IngestLiveUrl) SetMatchId(v int64)`

SetMatchId sets MatchId field to given value.


### GetStartedAt

`func (o *IngestLiveUrl) GetStartedAt() int64`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *IngestLiveUrl) GetStartedAtOk() (*int64, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *IngestLiveUrl) SetStartedAt(v int64)`

SetStartedAt sets StartedAt field to given value.

### HasStartedAt

`func (o *IngestLiveUrl) HasStartedAt() bool`

HasStartedAt returns a boolean if a field has been set.

### SetStartedAtNil

`func (o *IngestLiveUrl) SetStartedAtNil(b bool)`

 SetStartedAtNil sets the value for StartedAt to be an explicit nil

### UnsetStartedAt
`func (o *IngestLiveUrl) UnsetStartedAt()`

UnsetStartedAt ensures that no value is present for StartedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


