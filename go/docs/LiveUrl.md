# LiveUrl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BroadcastUrl** | **string** |  | 
**LobbyId** | Pointer to **NullableInt64** |  | [optional] 
**MatchId** | **int64** |  | 
**StartedAt** | Pointer to **NullableInt64** |  | [optional] 
**UpdatedAt** | Pointer to **NullableInt64** |  | [optional] 

## Methods

### NewLiveUrl

`func NewLiveUrl(broadcastUrl string, matchId int64, ) *LiveUrl`

NewLiveUrl instantiates a new LiveUrl object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewLiveUrlWithDefaults

`func NewLiveUrlWithDefaults() *LiveUrl`

NewLiveUrlWithDefaults instantiates a new LiveUrl object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBroadcastUrl

`func (o *LiveUrl) GetBroadcastUrl() string`

GetBroadcastUrl returns the BroadcastUrl field if non-nil, zero value otherwise.

### GetBroadcastUrlOk

`func (o *LiveUrl) GetBroadcastUrlOk() (*string, bool)`

GetBroadcastUrlOk returns a tuple with the BroadcastUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBroadcastUrl

`func (o *LiveUrl) SetBroadcastUrl(v string)`

SetBroadcastUrl sets BroadcastUrl field to given value.


### GetLobbyId

`func (o *LiveUrl) GetLobbyId() int64`

GetLobbyId returns the LobbyId field if non-nil, zero value otherwise.

### GetLobbyIdOk

`func (o *LiveUrl) GetLobbyIdOk() (*int64, bool)`

GetLobbyIdOk returns a tuple with the LobbyId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLobbyId

`func (o *LiveUrl) SetLobbyId(v int64)`

SetLobbyId sets LobbyId field to given value.

### HasLobbyId

`func (o *LiveUrl) HasLobbyId() bool`

HasLobbyId returns a boolean if a field has been set.

### SetLobbyIdNil

`func (o *LiveUrl) SetLobbyIdNil(b bool)`

 SetLobbyIdNil sets the value for LobbyId to be an explicit nil

### UnsetLobbyId
`func (o *LiveUrl) UnsetLobbyId()`

UnsetLobbyId ensures that no value is present for LobbyId, not even an explicit nil
### GetMatchId

`func (o *LiveUrl) GetMatchId() int64`

GetMatchId returns the MatchId field if non-nil, zero value otherwise.

### GetMatchIdOk

`func (o *LiveUrl) GetMatchIdOk() (*int64, bool)`

GetMatchIdOk returns a tuple with the MatchId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchId

`func (o *LiveUrl) SetMatchId(v int64)`

SetMatchId sets MatchId field to given value.


### GetStartedAt

`func (o *LiveUrl) GetStartedAt() int64`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *LiveUrl) GetStartedAtOk() (*int64, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *LiveUrl) SetStartedAt(v int64)`

SetStartedAt sets StartedAt field to given value.

### HasStartedAt

`func (o *LiveUrl) HasStartedAt() bool`

HasStartedAt returns a boolean if a field has been set.

### SetStartedAtNil

`func (o *LiveUrl) SetStartedAtNil(b bool)`

 SetStartedAtNil sets the value for StartedAt to be an explicit nil

### UnsetStartedAt
`func (o *LiveUrl) UnsetStartedAt()`

UnsetStartedAt ensures that no value is present for StartedAt, not even an explicit nil
### GetUpdatedAt

`func (o *LiveUrl) GetUpdatedAt() int64`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *LiveUrl) GetUpdatedAtOk() (*int64, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *LiveUrl) SetUpdatedAt(v int64)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *LiveUrl) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### SetUpdatedAtNil

`func (o *LiveUrl) SetUpdatedAtNil(b bool)`

 SetUpdatedAtNil sets the value for UpdatedAt to be an explicit nil

### UnsetUpdatedAt
`func (o *LiveUrl) UnsetUpdatedAt()`

UnsetUpdatedAt ensures that no value is present for UpdatedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


