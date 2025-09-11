# ActiveMatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CompatVersion** | Pointer to **NullableInt32** |  | [optional] 
**DurationS** | Pointer to **NullableInt32** |  | [optional] 
**GameMode** | Pointer to **NullableInt32** |  | [optional] 
**GameModeParsed** | Pointer to [**NullableActiveMatchGameMode**](ActiveMatchGameMode.md) |  | [optional] 
**GameModeVersion** | Pointer to **NullableInt32** |  | [optional] 
**LobbyId** | Pointer to **NullableInt64** |  | [optional] 
**MatchId** | Pointer to **NullableInt64** |  | [optional] 
**MatchMode** | Pointer to **NullableInt32** |  | [optional] 
**MatchModeParsed** | Pointer to [**NullableActiveMatchMode**](ActiveMatchMode.md) |  | [optional] 
**MatchScore** | Pointer to **NullableInt32** |  | [optional] 
**NetWorthTeam0** | Pointer to **NullableInt32** |  | [optional] 
**NetWorthTeam1** | Pointer to **NullableInt32** |  | [optional] 
**ObjectivesMaskTeam0** | Pointer to **NullableInt64** |  | [optional] 
**ObjectivesMaskTeam1** | Pointer to **NullableInt64** |  | [optional] 
**OpenSpectatorSlots** | Pointer to **NullableInt32** |  | [optional] 
**Players** | [**[]ActiveMatchPlayer**](ActiveMatchPlayer.md) |  | 
**RegionMode** | Pointer to **NullableInt32** |  | [optional] 
**RegionModeParsed** | Pointer to [**NullableActiveMatchRegionMode**](ActiveMatchRegionMode.md) |  | [optional] 
**Spectators** | Pointer to **NullableInt32** |  | [optional] 
**StartTime** | Pointer to **NullableInt32** |  | [optional] 
**WinningTeam** | Pointer to **NullableInt32** |  | [optional] 
**WinningTeamParsed** | Pointer to [**NullableActiveMatchTeam**](ActiveMatchTeam.md) |  | [optional] 

## Methods

### NewActiveMatch

`func NewActiveMatch(players []ActiveMatchPlayer, ) *ActiveMatch`

NewActiveMatch instantiates a new ActiveMatch object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewActiveMatchWithDefaults

`func NewActiveMatchWithDefaults() *ActiveMatch`

NewActiveMatchWithDefaults instantiates a new ActiveMatch object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCompatVersion

`func (o *ActiveMatch) GetCompatVersion() int32`

GetCompatVersion returns the CompatVersion field if non-nil, zero value otherwise.

### GetCompatVersionOk

`func (o *ActiveMatch) GetCompatVersionOk() (*int32, bool)`

GetCompatVersionOk returns a tuple with the CompatVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompatVersion

`func (o *ActiveMatch) SetCompatVersion(v int32)`

SetCompatVersion sets CompatVersion field to given value.

### HasCompatVersion

`func (o *ActiveMatch) HasCompatVersion() bool`

HasCompatVersion returns a boolean if a field has been set.

### SetCompatVersionNil

`func (o *ActiveMatch) SetCompatVersionNil(b bool)`

 SetCompatVersionNil sets the value for CompatVersion to be an explicit nil

### UnsetCompatVersion
`func (o *ActiveMatch) UnsetCompatVersion()`

UnsetCompatVersion ensures that no value is present for CompatVersion, not even an explicit nil
### GetDurationS

`func (o *ActiveMatch) GetDurationS() int32`

GetDurationS returns the DurationS field if non-nil, zero value otherwise.

### GetDurationSOk

`func (o *ActiveMatch) GetDurationSOk() (*int32, bool)`

GetDurationSOk returns a tuple with the DurationS field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDurationS

`func (o *ActiveMatch) SetDurationS(v int32)`

SetDurationS sets DurationS field to given value.

### HasDurationS

`func (o *ActiveMatch) HasDurationS() bool`

HasDurationS returns a boolean if a field has been set.

### SetDurationSNil

`func (o *ActiveMatch) SetDurationSNil(b bool)`

 SetDurationSNil sets the value for DurationS to be an explicit nil

### UnsetDurationS
`func (o *ActiveMatch) UnsetDurationS()`

UnsetDurationS ensures that no value is present for DurationS, not even an explicit nil
### GetGameMode

`func (o *ActiveMatch) GetGameMode() int32`

GetGameMode returns the GameMode field if non-nil, zero value otherwise.

### GetGameModeOk

`func (o *ActiveMatch) GetGameModeOk() (*int32, bool)`

GetGameModeOk returns a tuple with the GameMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGameMode

`func (o *ActiveMatch) SetGameMode(v int32)`

SetGameMode sets GameMode field to given value.

### HasGameMode

`func (o *ActiveMatch) HasGameMode() bool`

HasGameMode returns a boolean if a field has been set.

### SetGameModeNil

`func (o *ActiveMatch) SetGameModeNil(b bool)`

 SetGameModeNil sets the value for GameMode to be an explicit nil

### UnsetGameMode
`func (o *ActiveMatch) UnsetGameMode()`

UnsetGameMode ensures that no value is present for GameMode, not even an explicit nil
### GetGameModeParsed

`func (o *ActiveMatch) GetGameModeParsed() ActiveMatchGameMode`

GetGameModeParsed returns the GameModeParsed field if non-nil, zero value otherwise.

### GetGameModeParsedOk

`func (o *ActiveMatch) GetGameModeParsedOk() (*ActiveMatchGameMode, bool)`

GetGameModeParsedOk returns a tuple with the GameModeParsed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGameModeParsed

`func (o *ActiveMatch) SetGameModeParsed(v ActiveMatchGameMode)`

SetGameModeParsed sets GameModeParsed field to given value.

### HasGameModeParsed

`func (o *ActiveMatch) HasGameModeParsed() bool`

HasGameModeParsed returns a boolean if a field has been set.

### SetGameModeParsedNil

`func (o *ActiveMatch) SetGameModeParsedNil(b bool)`

 SetGameModeParsedNil sets the value for GameModeParsed to be an explicit nil

### UnsetGameModeParsed
`func (o *ActiveMatch) UnsetGameModeParsed()`

UnsetGameModeParsed ensures that no value is present for GameModeParsed, not even an explicit nil
### GetGameModeVersion

`func (o *ActiveMatch) GetGameModeVersion() int32`

GetGameModeVersion returns the GameModeVersion field if non-nil, zero value otherwise.

### GetGameModeVersionOk

`func (o *ActiveMatch) GetGameModeVersionOk() (*int32, bool)`

GetGameModeVersionOk returns a tuple with the GameModeVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGameModeVersion

`func (o *ActiveMatch) SetGameModeVersion(v int32)`

SetGameModeVersion sets GameModeVersion field to given value.

### HasGameModeVersion

`func (o *ActiveMatch) HasGameModeVersion() bool`

HasGameModeVersion returns a boolean if a field has been set.

### SetGameModeVersionNil

`func (o *ActiveMatch) SetGameModeVersionNil(b bool)`

 SetGameModeVersionNil sets the value for GameModeVersion to be an explicit nil

### UnsetGameModeVersion
`func (o *ActiveMatch) UnsetGameModeVersion()`

UnsetGameModeVersion ensures that no value is present for GameModeVersion, not even an explicit nil
### GetLobbyId

`func (o *ActiveMatch) GetLobbyId() int64`

GetLobbyId returns the LobbyId field if non-nil, zero value otherwise.

### GetLobbyIdOk

`func (o *ActiveMatch) GetLobbyIdOk() (*int64, bool)`

GetLobbyIdOk returns a tuple with the LobbyId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLobbyId

`func (o *ActiveMatch) SetLobbyId(v int64)`

SetLobbyId sets LobbyId field to given value.

### HasLobbyId

`func (o *ActiveMatch) HasLobbyId() bool`

HasLobbyId returns a boolean if a field has been set.

### SetLobbyIdNil

`func (o *ActiveMatch) SetLobbyIdNil(b bool)`

 SetLobbyIdNil sets the value for LobbyId to be an explicit nil

### UnsetLobbyId
`func (o *ActiveMatch) UnsetLobbyId()`

UnsetLobbyId ensures that no value is present for LobbyId, not even an explicit nil
### GetMatchId

`func (o *ActiveMatch) GetMatchId() int64`

GetMatchId returns the MatchId field if non-nil, zero value otherwise.

### GetMatchIdOk

`func (o *ActiveMatch) GetMatchIdOk() (*int64, bool)`

GetMatchIdOk returns a tuple with the MatchId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchId

`func (o *ActiveMatch) SetMatchId(v int64)`

SetMatchId sets MatchId field to given value.

### HasMatchId

`func (o *ActiveMatch) HasMatchId() bool`

HasMatchId returns a boolean if a field has been set.

### SetMatchIdNil

`func (o *ActiveMatch) SetMatchIdNil(b bool)`

 SetMatchIdNil sets the value for MatchId to be an explicit nil

### UnsetMatchId
`func (o *ActiveMatch) UnsetMatchId()`

UnsetMatchId ensures that no value is present for MatchId, not even an explicit nil
### GetMatchMode

`func (o *ActiveMatch) GetMatchMode() int32`

GetMatchMode returns the MatchMode field if non-nil, zero value otherwise.

### GetMatchModeOk

`func (o *ActiveMatch) GetMatchModeOk() (*int32, bool)`

GetMatchModeOk returns a tuple with the MatchMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchMode

`func (o *ActiveMatch) SetMatchMode(v int32)`

SetMatchMode sets MatchMode field to given value.

### HasMatchMode

`func (o *ActiveMatch) HasMatchMode() bool`

HasMatchMode returns a boolean if a field has been set.

### SetMatchModeNil

`func (o *ActiveMatch) SetMatchModeNil(b bool)`

 SetMatchModeNil sets the value for MatchMode to be an explicit nil

### UnsetMatchMode
`func (o *ActiveMatch) UnsetMatchMode()`

UnsetMatchMode ensures that no value is present for MatchMode, not even an explicit nil
### GetMatchModeParsed

`func (o *ActiveMatch) GetMatchModeParsed() ActiveMatchMode`

GetMatchModeParsed returns the MatchModeParsed field if non-nil, zero value otherwise.

### GetMatchModeParsedOk

`func (o *ActiveMatch) GetMatchModeParsedOk() (*ActiveMatchMode, bool)`

GetMatchModeParsedOk returns a tuple with the MatchModeParsed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchModeParsed

`func (o *ActiveMatch) SetMatchModeParsed(v ActiveMatchMode)`

SetMatchModeParsed sets MatchModeParsed field to given value.

### HasMatchModeParsed

`func (o *ActiveMatch) HasMatchModeParsed() bool`

HasMatchModeParsed returns a boolean if a field has been set.

### SetMatchModeParsedNil

`func (o *ActiveMatch) SetMatchModeParsedNil(b bool)`

 SetMatchModeParsedNil sets the value for MatchModeParsed to be an explicit nil

### UnsetMatchModeParsed
`func (o *ActiveMatch) UnsetMatchModeParsed()`

UnsetMatchModeParsed ensures that no value is present for MatchModeParsed, not even an explicit nil
### GetMatchScore

`func (o *ActiveMatch) GetMatchScore() int32`

GetMatchScore returns the MatchScore field if non-nil, zero value otherwise.

### GetMatchScoreOk

`func (o *ActiveMatch) GetMatchScoreOk() (*int32, bool)`

GetMatchScoreOk returns a tuple with the MatchScore field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchScore

`func (o *ActiveMatch) SetMatchScore(v int32)`

SetMatchScore sets MatchScore field to given value.

### HasMatchScore

`func (o *ActiveMatch) HasMatchScore() bool`

HasMatchScore returns a boolean if a field has been set.

### SetMatchScoreNil

`func (o *ActiveMatch) SetMatchScoreNil(b bool)`

 SetMatchScoreNil sets the value for MatchScore to be an explicit nil

### UnsetMatchScore
`func (o *ActiveMatch) UnsetMatchScore()`

UnsetMatchScore ensures that no value is present for MatchScore, not even an explicit nil
### GetNetWorthTeam0

`func (o *ActiveMatch) GetNetWorthTeam0() int32`

GetNetWorthTeam0 returns the NetWorthTeam0 field if non-nil, zero value otherwise.

### GetNetWorthTeam0Ok

`func (o *ActiveMatch) GetNetWorthTeam0Ok() (*int32, bool)`

GetNetWorthTeam0Ok returns a tuple with the NetWorthTeam0 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetWorthTeam0

`func (o *ActiveMatch) SetNetWorthTeam0(v int32)`

SetNetWorthTeam0 sets NetWorthTeam0 field to given value.

### HasNetWorthTeam0

`func (o *ActiveMatch) HasNetWorthTeam0() bool`

HasNetWorthTeam0 returns a boolean if a field has been set.

### SetNetWorthTeam0Nil

`func (o *ActiveMatch) SetNetWorthTeam0Nil(b bool)`

 SetNetWorthTeam0Nil sets the value for NetWorthTeam0 to be an explicit nil

### UnsetNetWorthTeam0
`func (o *ActiveMatch) UnsetNetWorthTeam0()`

UnsetNetWorthTeam0 ensures that no value is present for NetWorthTeam0, not even an explicit nil
### GetNetWorthTeam1

`func (o *ActiveMatch) GetNetWorthTeam1() int32`

GetNetWorthTeam1 returns the NetWorthTeam1 field if non-nil, zero value otherwise.

### GetNetWorthTeam1Ok

`func (o *ActiveMatch) GetNetWorthTeam1Ok() (*int32, bool)`

GetNetWorthTeam1Ok returns a tuple with the NetWorthTeam1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetWorthTeam1

`func (o *ActiveMatch) SetNetWorthTeam1(v int32)`

SetNetWorthTeam1 sets NetWorthTeam1 field to given value.

### HasNetWorthTeam1

`func (o *ActiveMatch) HasNetWorthTeam1() bool`

HasNetWorthTeam1 returns a boolean if a field has been set.

### SetNetWorthTeam1Nil

`func (o *ActiveMatch) SetNetWorthTeam1Nil(b bool)`

 SetNetWorthTeam1Nil sets the value for NetWorthTeam1 to be an explicit nil

### UnsetNetWorthTeam1
`func (o *ActiveMatch) UnsetNetWorthTeam1()`

UnsetNetWorthTeam1 ensures that no value is present for NetWorthTeam1, not even an explicit nil
### GetObjectivesMaskTeam0

`func (o *ActiveMatch) GetObjectivesMaskTeam0() int64`

GetObjectivesMaskTeam0 returns the ObjectivesMaskTeam0 field if non-nil, zero value otherwise.

### GetObjectivesMaskTeam0Ok

`func (o *ActiveMatch) GetObjectivesMaskTeam0Ok() (*int64, bool)`

GetObjectivesMaskTeam0Ok returns a tuple with the ObjectivesMaskTeam0 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectivesMaskTeam0

`func (o *ActiveMatch) SetObjectivesMaskTeam0(v int64)`

SetObjectivesMaskTeam0 sets ObjectivesMaskTeam0 field to given value.

### HasObjectivesMaskTeam0

`func (o *ActiveMatch) HasObjectivesMaskTeam0() bool`

HasObjectivesMaskTeam0 returns a boolean if a field has been set.

### SetObjectivesMaskTeam0Nil

`func (o *ActiveMatch) SetObjectivesMaskTeam0Nil(b bool)`

 SetObjectivesMaskTeam0Nil sets the value for ObjectivesMaskTeam0 to be an explicit nil

### UnsetObjectivesMaskTeam0
`func (o *ActiveMatch) UnsetObjectivesMaskTeam0()`

UnsetObjectivesMaskTeam0 ensures that no value is present for ObjectivesMaskTeam0, not even an explicit nil
### GetObjectivesMaskTeam1

`func (o *ActiveMatch) GetObjectivesMaskTeam1() int64`

GetObjectivesMaskTeam1 returns the ObjectivesMaskTeam1 field if non-nil, zero value otherwise.

### GetObjectivesMaskTeam1Ok

`func (o *ActiveMatch) GetObjectivesMaskTeam1Ok() (*int64, bool)`

GetObjectivesMaskTeam1Ok returns a tuple with the ObjectivesMaskTeam1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectivesMaskTeam1

`func (o *ActiveMatch) SetObjectivesMaskTeam1(v int64)`

SetObjectivesMaskTeam1 sets ObjectivesMaskTeam1 field to given value.

### HasObjectivesMaskTeam1

`func (o *ActiveMatch) HasObjectivesMaskTeam1() bool`

HasObjectivesMaskTeam1 returns a boolean if a field has been set.

### SetObjectivesMaskTeam1Nil

`func (o *ActiveMatch) SetObjectivesMaskTeam1Nil(b bool)`

 SetObjectivesMaskTeam1Nil sets the value for ObjectivesMaskTeam1 to be an explicit nil

### UnsetObjectivesMaskTeam1
`func (o *ActiveMatch) UnsetObjectivesMaskTeam1()`

UnsetObjectivesMaskTeam1 ensures that no value is present for ObjectivesMaskTeam1, not even an explicit nil
### GetOpenSpectatorSlots

`func (o *ActiveMatch) GetOpenSpectatorSlots() int32`

GetOpenSpectatorSlots returns the OpenSpectatorSlots field if non-nil, zero value otherwise.

### GetOpenSpectatorSlotsOk

`func (o *ActiveMatch) GetOpenSpectatorSlotsOk() (*int32, bool)`

GetOpenSpectatorSlotsOk returns a tuple with the OpenSpectatorSlots field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpenSpectatorSlots

`func (o *ActiveMatch) SetOpenSpectatorSlots(v int32)`

SetOpenSpectatorSlots sets OpenSpectatorSlots field to given value.

### HasOpenSpectatorSlots

`func (o *ActiveMatch) HasOpenSpectatorSlots() bool`

HasOpenSpectatorSlots returns a boolean if a field has been set.

### SetOpenSpectatorSlotsNil

`func (o *ActiveMatch) SetOpenSpectatorSlotsNil(b bool)`

 SetOpenSpectatorSlotsNil sets the value for OpenSpectatorSlots to be an explicit nil

### UnsetOpenSpectatorSlots
`func (o *ActiveMatch) UnsetOpenSpectatorSlots()`

UnsetOpenSpectatorSlots ensures that no value is present for OpenSpectatorSlots, not even an explicit nil
### GetPlayers

`func (o *ActiveMatch) GetPlayers() []ActiveMatchPlayer`

GetPlayers returns the Players field if non-nil, zero value otherwise.

### GetPlayersOk

`func (o *ActiveMatch) GetPlayersOk() (*[]ActiveMatchPlayer, bool)`

GetPlayersOk returns a tuple with the Players field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayers

`func (o *ActiveMatch) SetPlayers(v []ActiveMatchPlayer)`

SetPlayers sets Players field to given value.


### GetRegionMode

`func (o *ActiveMatch) GetRegionMode() int32`

GetRegionMode returns the RegionMode field if non-nil, zero value otherwise.

### GetRegionModeOk

`func (o *ActiveMatch) GetRegionModeOk() (*int32, bool)`

GetRegionModeOk returns a tuple with the RegionMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegionMode

`func (o *ActiveMatch) SetRegionMode(v int32)`

SetRegionMode sets RegionMode field to given value.

### HasRegionMode

`func (o *ActiveMatch) HasRegionMode() bool`

HasRegionMode returns a boolean if a field has been set.

### SetRegionModeNil

`func (o *ActiveMatch) SetRegionModeNil(b bool)`

 SetRegionModeNil sets the value for RegionMode to be an explicit nil

### UnsetRegionMode
`func (o *ActiveMatch) UnsetRegionMode()`

UnsetRegionMode ensures that no value is present for RegionMode, not even an explicit nil
### GetRegionModeParsed

`func (o *ActiveMatch) GetRegionModeParsed() ActiveMatchRegionMode`

GetRegionModeParsed returns the RegionModeParsed field if non-nil, zero value otherwise.

### GetRegionModeParsedOk

`func (o *ActiveMatch) GetRegionModeParsedOk() (*ActiveMatchRegionMode, bool)`

GetRegionModeParsedOk returns a tuple with the RegionModeParsed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegionModeParsed

`func (o *ActiveMatch) SetRegionModeParsed(v ActiveMatchRegionMode)`

SetRegionModeParsed sets RegionModeParsed field to given value.

### HasRegionModeParsed

`func (o *ActiveMatch) HasRegionModeParsed() bool`

HasRegionModeParsed returns a boolean if a field has been set.

### SetRegionModeParsedNil

`func (o *ActiveMatch) SetRegionModeParsedNil(b bool)`

 SetRegionModeParsedNil sets the value for RegionModeParsed to be an explicit nil

### UnsetRegionModeParsed
`func (o *ActiveMatch) UnsetRegionModeParsed()`

UnsetRegionModeParsed ensures that no value is present for RegionModeParsed, not even an explicit nil
### GetSpectators

`func (o *ActiveMatch) GetSpectators() int32`

GetSpectators returns the Spectators field if non-nil, zero value otherwise.

### GetSpectatorsOk

`func (o *ActiveMatch) GetSpectatorsOk() (*int32, bool)`

GetSpectatorsOk returns a tuple with the Spectators field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpectators

`func (o *ActiveMatch) SetSpectators(v int32)`

SetSpectators sets Spectators field to given value.

### HasSpectators

`func (o *ActiveMatch) HasSpectators() bool`

HasSpectators returns a boolean if a field has been set.

### SetSpectatorsNil

`func (o *ActiveMatch) SetSpectatorsNil(b bool)`

 SetSpectatorsNil sets the value for Spectators to be an explicit nil

### UnsetSpectators
`func (o *ActiveMatch) UnsetSpectators()`

UnsetSpectators ensures that no value is present for Spectators, not even an explicit nil
### GetStartTime

`func (o *ActiveMatch) GetStartTime() int32`

GetStartTime returns the StartTime field if non-nil, zero value otherwise.

### GetStartTimeOk

`func (o *ActiveMatch) GetStartTimeOk() (*int32, bool)`

GetStartTimeOk returns a tuple with the StartTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTime

`func (o *ActiveMatch) SetStartTime(v int32)`

SetStartTime sets StartTime field to given value.

### HasStartTime

`func (o *ActiveMatch) HasStartTime() bool`

HasStartTime returns a boolean if a field has been set.

### SetStartTimeNil

`func (o *ActiveMatch) SetStartTimeNil(b bool)`

 SetStartTimeNil sets the value for StartTime to be an explicit nil

### UnsetStartTime
`func (o *ActiveMatch) UnsetStartTime()`

UnsetStartTime ensures that no value is present for StartTime, not even an explicit nil
### GetWinningTeam

`func (o *ActiveMatch) GetWinningTeam() int32`

GetWinningTeam returns the WinningTeam field if non-nil, zero value otherwise.

### GetWinningTeamOk

`func (o *ActiveMatch) GetWinningTeamOk() (*int32, bool)`

GetWinningTeamOk returns a tuple with the WinningTeam field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWinningTeam

`func (o *ActiveMatch) SetWinningTeam(v int32)`

SetWinningTeam sets WinningTeam field to given value.

### HasWinningTeam

`func (o *ActiveMatch) HasWinningTeam() bool`

HasWinningTeam returns a boolean if a field has been set.

### SetWinningTeamNil

`func (o *ActiveMatch) SetWinningTeamNil(b bool)`

 SetWinningTeamNil sets the value for WinningTeam to be an explicit nil

### UnsetWinningTeam
`func (o *ActiveMatch) UnsetWinningTeam()`

UnsetWinningTeam ensures that no value is present for WinningTeam, not even an explicit nil
### GetWinningTeamParsed

`func (o *ActiveMatch) GetWinningTeamParsed() ActiveMatchTeam`

GetWinningTeamParsed returns the WinningTeamParsed field if non-nil, zero value otherwise.

### GetWinningTeamParsedOk

`func (o *ActiveMatch) GetWinningTeamParsedOk() (*ActiveMatchTeam, bool)`

GetWinningTeamParsedOk returns a tuple with the WinningTeamParsed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWinningTeamParsed

`func (o *ActiveMatch) SetWinningTeamParsed(v ActiveMatchTeam)`

SetWinningTeamParsed sets WinningTeamParsed field to given value.

### HasWinningTeamParsed

`func (o *ActiveMatch) HasWinningTeamParsed() bool`

HasWinningTeamParsed returns a boolean if a field has been set.

### SetWinningTeamParsedNil

`func (o *ActiveMatch) SetWinningTeamParsedNil(b bool)`

 SetWinningTeamParsedNil sets the value for WinningTeamParsed to be an explicit nil

### UnsetWinningTeamParsed
`func (o *ActiveMatch) UnsetWinningTeamParsed()`

UnsetWinningTeamParsed ensures that no value is present for WinningTeamParsed, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


