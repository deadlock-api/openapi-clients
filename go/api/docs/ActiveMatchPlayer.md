# ActiveMatchPlayer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Abandoned** | Pointer to **NullableBool** |  | [optional] 
**AccountId** | Pointer to **NullableInt32** |  | [optional] 
**HeroId** | Pointer to **NullableInt32** | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] 
**Team** | Pointer to **NullableInt32** |  | [optional] 
**TeamParsed** | Pointer to [**NullableActiveMatchTeam**](ActiveMatchTeam.md) |  | [optional] 

## Methods

### NewActiveMatchPlayer

`func NewActiveMatchPlayer() *ActiveMatchPlayer`

NewActiveMatchPlayer instantiates a new ActiveMatchPlayer object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewActiveMatchPlayerWithDefaults

`func NewActiveMatchPlayerWithDefaults() *ActiveMatchPlayer`

NewActiveMatchPlayerWithDefaults instantiates a new ActiveMatchPlayer object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAbandoned

`func (o *ActiveMatchPlayer) GetAbandoned() bool`

GetAbandoned returns the Abandoned field if non-nil, zero value otherwise.

### GetAbandonedOk

`func (o *ActiveMatchPlayer) GetAbandonedOk() (*bool, bool)`

GetAbandonedOk returns a tuple with the Abandoned field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAbandoned

`func (o *ActiveMatchPlayer) SetAbandoned(v bool)`

SetAbandoned sets Abandoned field to given value.

### HasAbandoned

`func (o *ActiveMatchPlayer) HasAbandoned() bool`

HasAbandoned returns a boolean if a field has been set.

### SetAbandonedNil

`func (o *ActiveMatchPlayer) SetAbandonedNil(b bool)`

 SetAbandonedNil sets the value for Abandoned to be an explicit nil

### UnsetAbandoned
`func (o *ActiveMatchPlayer) UnsetAbandoned()`

UnsetAbandoned ensures that no value is present for Abandoned, not even an explicit nil
### GetAccountId

`func (o *ActiveMatchPlayer) GetAccountId() int32`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *ActiveMatchPlayer) GetAccountIdOk() (*int32, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *ActiveMatchPlayer) SetAccountId(v int32)`

SetAccountId sets AccountId field to given value.

### HasAccountId

`func (o *ActiveMatchPlayer) HasAccountId() bool`

HasAccountId returns a boolean if a field has been set.

### SetAccountIdNil

`func (o *ActiveMatchPlayer) SetAccountIdNil(b bool)`

 SetAccountIdNil sets the value for AccountId to be an explicit nil

### UnsetAccountId
`func (o *ActiveMatchPlayer) UnsetAccountId()`

UnsetAccountId ensures that no value is present for AccountId, not even an explicit nil
### GetHeroId

`func (o *ActiveMatchPlayer) GetHeroId() int32`

GetHeroId returns the HeroId field if non-nil, zero value otherwise.

### GetHeroIdOk

`func (o *ActiveMatchPlayer) GetHeroIdOk() (*int32, bool)`

GetHeroIdOk returns a tuple with the HeroId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroId

`func (o *ActiveMatchPlayer) SetHeroId(v int32)`

SetHeroId sets HeroId field to given value.

### HasHeroId

`func (o *ActiveMatchPlayer) HasHeroId() bool`

HasHeroId returns a boolean if a field has been set.

### SetHeroIdNil

`func (o *ActiveMatchPlayer) SetHeroIdNil(b bool)`

 SetHeroIdNil sets the value for HeroId to be an explicit nil

### UnsetHeroId
`func (o *ActiveMatchPlayer) UnsetHeroId()`

UnsetHeroId ensures that no value is present for HeroId, not even an explicit nil
### GetTeam

`func (o *ActiveMatchPlayer) GetTeam() int32`

GetTeam returns the Team field if non-nil, zero value otherwise.

### GetTeamOk

`func (o *ActiveMatchPlayer) GetTeamOk() (*int32, bool)`

GetTeamOk returns a tuple with the Team field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTeam

`func (o *ActiveMatchPlayer) SetTeam(v int32)`

SetTeam sets Team field to given value.

### HasTeam

`func (o *ActiveMatchPlayer) HasTeam() bool`

HasTeam returns a boolean if a field has been set.

### SetTeamNil

`func (o *ActiveMatchPlayer) SetTeamNil(b bool)`

 SetTeamNil sets the value for Team to be an explicit nil

### UnsetTeam
`func (o *ActiveMatchPlayer) UnsetTeam()`

UnsetTeam ensures that no value is present for Team, not even an explicit nil
### GetTeamParsed

`func (o *ActiveMatchPlayer) GetTeamParsed() ActiveMatchTeam`

GetTeamParsed returns the TeamParsed field if non-nil, zero value otherwise.

### GetTeamParsedOk

`func (o *ActiveMatchPlayer) GetTeamParsedOk() (*ActiveMatchTeam, bool)`

GetTeamParsedOk returns a tuple with the TeamParsed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTeamParsed

`func (o *ActiveMatchPlayer) SetTeamParsed(v ActiveMatchTeam)`

SetTeamParsed sets TeamParsed field to given value.

### HasTeamParsed

`func (o *ActiveMatchPlayer) HasTeamParsed() bool`

HasTeamParsed returns a boolean if a field has been set.

### SetTeamParsedNil

`func (o *ActiveMatchPlayer) SetTeamParsedNil(b bool)`

 SetTeamParsedNil sets the value for TeamParsed to be an explicit nil

### UnsetTeamParsed
`func (o *ActiveMatchPlayer) UnsetTeamParsed()`

UnsetTeamParsed ensures that no value is present for TeamParsed, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


