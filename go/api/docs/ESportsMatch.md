# ESportsMatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MatchId** | Pointer to **NullableInt64** | Valve&#39;s match id of the match. | [optional] 
**Provider** | **string** | The provider of the match data. Some string that identifies the source of the data. | 
**ScheduledDate** | Pointer to **NullableTime** | The scheduled date of the match. | [optional] 
**Status** | Pointer to [**NullableESportsMatchStatus**](ESportsMatchStatus.md) | The status of the match, e.g. live, completed, scheduled, cancelled. | [optional] 
**Team0Name** | Pointer to **NullableString** | The name of the first team. | [optional] 
**Team1Name** | Pointer to **NullableString** | The name of the second team. | [optional] 
**TournamentName** | Pointer to **NullableString** | The name of the tournament. | [optional] 
**TournamentStage** | Pointer to **NullableString** | The stage of the tournament. | [optional] 
**UpdateId** | Pointer to **NullableString** | If you want to update an existing match, you can provide an update id. | [optional] 

## Methods

### NewESportsMatch

`func NewESportsMatch(provider string, ) *ESportsMatch`

NewESportsMatch instantiates a new ESportsMatch object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewESportsMatchWithDefaults

`func NewESportsMatchWithDefaults() *ESportsMatch`

NewESportsMatchWithDefaults instantiates a new ESportsMatch object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMatchId

`func (o *ESportsMatch) GetMatchId() int64`

GetMatchId returns the MatchId field if non-nil, zero value otherwise.

### GetMatchIdOk

`func (o *ESportsMatch) GetMatchIdOk() (*int64, bool)`

GetMatchIdOk returns a tuple with the MatchId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchId

`func (o *ESportsMatch) SetMatchId(v int64)`

SetMatchId sets MatchId field to given value.

### HasMatchId

`func (o *ESportsMatch) HasMatchId() bool`

HasMatchId returns a boolean if a field has been set.

### SetMatchIdNil

`func (o *ESportsMatch) SetMatchIdNil(b bool)`

 SetMatchIdNil sets the value for MatchId to be an explicit nil

### UnsetMatchId
`func (o *ESportsMatch) UnsetMatchId()`

UnsetMatchId ensures that no value is present for MatchId, not even an explicit nil
### GetProvider

`func (o *ESportsMatch) GetProvider() string`

GetProvider returns the Provider field if non-nil, zero value otherwise.

### GetProviderOk

`func (o *ESportsMatch) GetProviderOk() (*string, bool)`

GetProviderOk returns a tuple with the Provider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvider

`func (o *ESportsMatch) SetProvider(v string)`

SetProvider sets Provider field to given value.


### GetScheduledDate

`func (o *ESportsMatch) GetScheduledDate() time.Time`

GetScheduledDate returns the ScheduledDate field if non-nil, zero value otherwise.

### GetScheduledDateOk

`func (o *ESportsMatch) GetScheduledDateOk() (*time.Time, bool)`

GetScheduledDateOk returns a tuple with the ScheduledDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScheduledDate

`func (o *ESportsMatch) SetScheduledDate(v time.Time)`

SetScheduledDate sets ScheduledDate field to given value.

### HasScheduledDate

`func (o *ESportsMatch) HasScheduledDate() bool`

HasScheduledDate returns a boolean if a field has been set.

### SetScheduledDateNil

`func (o *ESportsMatch) SetScheduledDateNil(b bool)`

 SetScheduledDateNil sets the value for ScheduledDate to be an explicit nil

### UnsetScheduledDate
`func (o *ESportsMatch) UnsetScheduledDate()`

UnsetScheduledDate ensures that no value is present for ScheduledDate, not even an explicit nil
### GetStatus

`func (o *ESportsMatch) GetStatus() ESportsMatchStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *ESportsMatch) GetStatusOk() (*ESportsMatchStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *ESportsMatch) SetStatus(v ESportsMatchStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *ESportsMatch) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### SetStatusNil

`func (o *ESportsMatch) SetStatusNil(b bool)`

 SetStatusNil sets the value for Status to be an explicit nil

### UnsetStatus
`func (o *ESportsMatch) UnsetStatus()`

UnsetStatus ensures that no value is present for Status, not even an explicit nil
### GetTeam0Name

`func (o *ESportsMatch) GetTeam0Name() string`

GetTeam0Name returns the Team0Name field if non-nil, zero value otherwise.

### GetTeam0NameOk

`func (o *ESportsMatch) GetTeam0NameOk() (*string, bool)`

GetTeam0NameOk returns a tuple with the Team0Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTeam0Name

`func (o *ESportsMatch) SetTeam0Name(v string)`

SetTeam0Name sets Team0Name field to given value.

### HasTeam0Name

`func (o *ESportsMatch) HasTeam0Name() bool`

HasTeam0Name returns a boolean if a field has been set.

### SetTeam0NameNil

`func (o *ESportsMatch) SetTeam0NameNil(b bool)`

 SetTeam0NameNil sets the value for Team0Name to be an explicit nil

### UnsetTeam0Name
`func (o *ESportsMatch) UnsetTeam0Name()`

UnsetTeam0Name ensures that no value is present for Team0Name, not even an explicit nil
### GetTeam1Name

`func (o *ESportsMatch) GetTeam1Name() string`

GetTeam1Name returns the Team1Name field if non-nil, zero value otherwise.

### GetTeam1NameOk

`func (o *ESportsMatch) GetTeam1NameOk() (*string, bool)`

GetTeam1NameOk returns a tuple with the Team1Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTeam1Name

`func (o *ESportsMatch) SetTeam1Name(v string)`

SetTeam1Name sets Team1Name field to given value.

### HasTeam1Name

`func (o *ESportsMatch) HasTeam1Name() bool`

HasTeam1Name returns a boolean if a field has been set.

### SetTeam1NameNil

`func (o *ESportsMatch) SetTeam1NameNil(b bool)`

 SetTeam1NameNil sets the value for Team1Name to be an explicit nil

### UnsetTeam1Name
`func (o *ESportsMatch) UnsetTeam1Name()`

UnsetTeam1Name ensures that no value is present for Team1Name, not even an explicit nil
### GetTournamentName

`func (o *ESportsMatch) GetTournamentName() string`

GetTournamentName returns the TournamentName field if non-nil, zero value otherwise.

### GetTournamentNameOk

`func (o *ESportsMatch) GetTournamentNameOk() (*string, bool)`

GetTournamentNameOk returns a tuple with the TournamentName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTournamentName

`func (o *ESportsMatch) SetTournamentName(v string)`

SetTournamentName sets TournamentName field to given value.

### HasTournamentName

`func (o *ESportsMatch) HasTournamentName() bool`

HasTournamentName returns a boolean if a field has been set.

### SetTournamentNameNil

`func (o *ESportsMatch) SetTournamentNameNil(b bool)`

 SetTournamentNameNil sets the value for TournamentName to be an explicit nil

### UnsetTournamentName
`func (o *ESportsMatch) UnsetTournamentName()`

UnsetTournamentName ensures that no value is present for TournamentName, not even an explicit nil
### GetTournamentStage

`func (o *ESportsMatch) GetTournamentStage() string`

GetTournamentStage returns the TournamentStage field if non-nil, zero value otherwise.

### GetTournamentStageOk

`func (o *ESportsMatch) GetTournamentStageOk() (*string, bool)`

GetTournamentStageOk returns a tuple with the TournamentStage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTournamentStage

`func (o *ESportsMatch) SetTournamentStage(v string)`

SetTournamentStage sets TournamentStage field to given value.

### HasTournamentStage

`func (o *ESportsMatch) HasTournamentStage() bool`

HasTournamentStage returns a boolean if a field has been set.

### SetTournamentStageNil

`func (o *ESportsMatch) SetTournamentStageNil(b bool)`

 SetTournamentStageNil sets the value for TournamentStage to be an explicit nil

### UnsetTournamentStage
`func (o *ESportsMatch) UnsetTournamentStage()`

UnsetTournamentStage ensures that no value is present for TournamentStage, not even an explicit nil
### GetUpdateId

`func (o *ESportsMatch) GetUpdateId() string`

GetUpdateId returns the UpdateId field if non-nil, zero value otherwise.

### GetUpdateIdOk

`func (o *ESportsMatch) GetUpdateIdOk() (*string, bool)`

GetUpdateIdOk returns a tuple with the UpdateId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateId

`func (o *ESportsMatch) SetUpdateId(v string)`

SetUpdateId sets UpdateId field to given value.

### HasUpdateId

`func (o *ESportsMatch) HasUpdateId() bool`

HasUpdateId returns a boolean if a field has been set.

### SetUpdateIdNil

`func (o *ESportsMatch) SetUpdateIdNil(b bool)`

 SetUpdateIdNil sets the value for UpdateId to be an explicit nil

### UnsetUpdateId
`func (o *ESportsMatch) UnsetUpdateId()`

UnsetUpdateId ensures that no value is present for UpdateId, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


