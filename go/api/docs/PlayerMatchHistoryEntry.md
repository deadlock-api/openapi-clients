# PlayerMatchHistoryEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AbandonedTimeS** | Pointer to **NullableInt32** |  | [optional] 
**AccountId** | **int32** |  | 
**Denies** | **int32** |  | 
**GameMode** | **int32** |  | 
**HeroId** | **int32** | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**HeroLevel** | **int32** |  | 
**LastHits** | **int32** |  | 
**MatchDurationS** | **int32** |  | 
**MatchId** | **int64** |  | 
**MatchMode** | **int32** |  | 
**MatchResult** | **int32** |  | 
**NetWorth** | **int32** |  | 
**ObjectivesMaskTeam0** | **int32** |  | 
**ObjectivesMaskTeam1** | **int32** |  | 
**PlayerAssists** | **int32** |  | 
**PlayerDeaths** | **int32** |  | 
**PlayerKills** | **int32** |  | 
**PlayerTeam** | **int32** |  | 
**StartTime** | **int32** |  | 
**TeamAbandoned** | Pointer to **NullableBool** |  | [optional] 

## Methods

### NewPlayerMatchHistoryEntry

`func NewPlayerMatchHistoryEntry(accountId int32, denies int32, gameMode int32, heroId int32, heroLevel int32, lastHits int32, matchDurationS int32, matchId int64, matchMode int32, matchResult int32, netWorth int32, objectivesMaskTeam0 int32, objectivesMaskTeam1 int32, playerAssists int32, playerDeaths int32, playerKills int32, playerTeam int32, startTime int32, ) *PlayerMatchHistoryEntry`

NewPlayerMatchHistoryEntry instantiates a new PlayerMatchHistoryEntry object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPlayerMatchHistoryEntryWithDefaults

`func NewPlayerMatchHistoryEntryWithDefaults() *PlayerMatchHistoryEntry`

NewPlayerMatchHistoryEntryWithDefaults instantiates a new PlayerMatchHistoryEntry object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAbandonedTimeS

`func (o *PlayerMatchHistoryEntry) GetAbandonedTimeS() int32`

GetAbandonedTimeS returns the AbandonedTimeS field if non-nil, zero value otherwise.

### GetAbandonedTimeSOk

`func (o *PlayerMatchHistoryEntry) GetAbandonedTimeSOk() (*int32, bool)`

GetAbandonedTimeSOk returns a tuple with the AbandonedTimeS field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAbandonedTimeS

`func (o *PlayerMatchHistoryEntry) SetAbandonedTimeS(v int32)`

SetAbandonedTimeS sets AbandonedTimeS field to given value.

### HasAbandonedTimeS

`func (o *PlayerMatchHistoryEntry) HasAbandonedTimeS() bool`

HasAbandonedTimeS returns a boolean if a field has been set.

### SetAbandonedTimeSNil

`func (o *PlayerMatchHistoryEntry) SetAbandonedTimeSNil(b bool)`

 SetAbandonedTimeSNil sets the value for AbandonedTimeS to be an explicit nil

### UnsetAbandonedTimeS
`func (o *PlayerMatchHistoryEntry) UnsetAbandonedTimeS()`

UnsetAbandonedTimeS ensures that no value is present for AbandonedTimeS, not even an explicit nil
### GetAccountId

`func (o *PlayerMatchHistoryEntry) GetAccountId() int32`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *PlayerMatchHistoryEntry) GetAccountIdOk() (*int32, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *PlayerMatchHistoryEntry) SetAccountId(v int32)`

SetAccountId sets AccountId field to given value.


### GetDenies

`func (o *PlayerMatchHistoryEntry) GetDenies() int32`

GetDenies returns the Denies field if non-nil, zero value otherwise.

### GetDeniesOk

`func (o *PlayerMatchHistoryEntry) GetDeniesOk() (*int32, bool)`

GetDeniesOk returns a tuple with the Denies field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDenies

`func (o *PlayerMatchHistoryEntry) SetDenies(v int32)`

SetDenies sets Denies field to given value.


### GetGameMode

`func (o *PlayerMatchHistoryEntry) GetGameMode() int32`

GetGameMode returns the GameMode field if non-nil, zero value otherwise.

### GetGameModeOk

`func (o *PlayerMatchHistoryEntry) GetGameModeOk() (*int32, bool)`

GetGameModeOk returns a tuple with the GameMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGameMode

`func (o *PlayerMatchHistoryEntry) SetGameMode(v int32)`

SetGameMode sets GameMode field to given value.


### GetHeroId

`func (o *PlayerMatchHistoryEntry) GetHeroId() int32`

GetHeroId returns the HeroId field if non-nil, zero value otherwise.

### GetHeroIdOk

`func (o *PlayerMatchHistoryEntry) GetHeroIdOk() (*int32, bool)`

GetHeroIdOk returns a tuple with the HeroId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroId

`func (o *PlayerMatchHistoryEntry) SetHeroId(v int32)`

SetHeroId sets HeroId field to given value.


### GetHeroLevel

`func (o *PlayerMatchHistoryEntry) GetHeroLevel() int32`

GetHeroLevel returns the HeroLevel field if non-nil, zero value otherwise.

### GetHeroLevelOk

`func (o *PlayerMatchHistoryEntry) GetHeroLevelOk() (*int32, bool)`

GetHeroLevelOk returns a tuple with the HeroLevel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroLevel

`func (o *PlayerMatchHistoryEntry) SetHeroLevel(v int32)`

SetHeroLevel sets HeroLevel field to given value.


### GetLastHits

`func (o *PlayerMatchHistoryEntry) GetLastHits() int32`

GetLastHits returns the LastHits field if non-nil, zero value otherwise.

### GetLastHitsOk

`func (o *PlayerMatchHistoryEntry) GetLastHitsOk() (*int32, bool)`

GetLastHitsOk returns a tuple with the LastHits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastHits

`func (o *PlayerMatchHistoryEntry) SetLastHits(v int32)`

SetLastHits sets LastHits field to given value.


### GetMatchDurationS

`func (o *PlayerMatchHistoryEntry) GetMatchDurationS() int32`

GetMatchDurationS returns the MatchDurationS field if non-nil, zero value otherwise.

### GetMatchDurationSOk

`func (o *PlayerMatchHistoryEntry) GetMatchDurationSOk() (*int32, bool)`

GetMatchDurationSOk returns a tuple with the MatchDurationS field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchDurationS

`func (o *PlayerMatchHistoryEntry) SetMatchDurationS(v int32)`

SetMatchDurationS sets MatchDurationS field to given value.


### GetMatchId

`func (o *PlayerMatchHistoryEntry) GetMatchId() int64`

GetMatchId returns the MatchId field if non-nil, zero value otherwise.

### GetMatchIdOk

`func (o *PlayerMatchHistoryEntry) GetMatchIdOk() (*int64, bool)`

GetMatchIdOk returns a tuple with the MatchId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchId

`func (o *PlayerMatchHistoryEntry) SetMatchId(v int64)`

SetMatchId sets MatchId field to given value.


### GetMatchMode

`func (o *PlayerMatchHistoryEntry) GetMatchMode() int32`

GetMatchMode returns the MatchMode field if non-nil, zero value otherwise.

### GetMatchModeOk

`func (o *PlayerMatchHistoryEntry) GetMatchModeOk() (*int32, bool)`

GetMatchModeOk returns a tuple with the MatchMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchMode

`func (o *PlayerMatchHistoryEntry) SetMatchMode(v int32)`

SetMatchMode sets MatchMode field to given value.


### GetMatchResult

`func (o *PlayerMatchHistoryEntry) GetMatchResult() int32`

GetMatchResult returns the MatchResult field if non-nil, zero value otherwise.

### GetMatchResultOk

`func (o *PlayerMatchHistoryEntry) GetMatchResultOk() (*int32, bool)`

GetMatchResultOk returns a tuple with the MatchResult field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchResult

`func (o *PlayerMatchHistoryEntry) SetMatchResult(v int32)`

SetMatchResult sets MatchResult field to given value.


### GetNetWorth

`func (o *PlayerMatchHistoryEntry) GetNetWorth() int32`

GetNetWorth returns the NetWorth field if non-nil, zero value otherwise.

### GetNetWorthOk

`func (o *PlayerMatchHistoryEntry) GetNetWorthOk() (*int32, bool)`

GetNetWorthOk returns a tuple with the NetWorth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetWorth

`func (o *PlayerMatchHistoryEntry) SetNetWorth(v int32)`

SetNetWorth sets NetWorth field to given value.


### GetObjectivesMaskTeam0

`func (o *PlayerMatchHistoryEntry) GetObjectivesMaskTeam0() int32`

GetObjectivesMaskTeam0 returns the ObjectivesMaskTeam0 field if non-nil, zero value otherwise.

### GetObjectivesMaskTeam0Ok

`func (o *PlayerMatchHistoryEntry) GetObjectivesMaskTeam0Ok() (*int32, bool)`

GetObjectivesMaskTeam0Ok returns a tuple with the ObjectivesMaskTeam0 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectivesMaskTeam0

`func (o *PlayerMatchHistoryEntry) SetObjectivesMaskTeam0(v int32)`

SetObjectivesMaskTeam0 sets ObjectivesMaskTeam0 field to given value.


### GetObjectivesMaskTeam1

`func (o *PlayerMatchHistoryEntry) GetObjectivesMaskTeam1() int32`

GetObjectivesMaskTeam1 returns the ObjectivesMaskTeam1 field if non-nil, zero value otherwise.

### GetObjectivesMaskTeam1Ok

`func (o *PlayerMatchHistoryEntry) GetObjectivesMaskTeam1Ok() (*int32, bool)`

GetObjectivesMaskTeam1Ok returns a tuple with the ObjectivesMaskTeam1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectivesMaskTeam1

`func (o *PlayerMatchHistoryEntry) SetObjectivesMaskTeam1(v int32)`

SetObjectivesMaskTeam1 sets ObjectivesMaskTeam1 field to given value.


### GetPlayerAssists

`func (o *PlayerMatchHistoryEntry) GetPlayerAssists() int32`

GetPlayerAssists returns the PlayerAssists field if non-nil, zero value otherwise.

### GetPlayerAssistsOk

`func (o *PlayerMatchHistoryEntry) GetPlayerAssistsOk() (*int32, bool)`

GetPlayerAssistsOk returns a tuple with the PlayerAssists field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerAssists

`func (o *PlayerMatchHistoryEntry) SetPlayerAssists(v int32)`

SetPlayerAssists sets PlayerAssists field to given value.


### GetPlayerDeaths

`func (o *PlayerMatchHistoryEntry) GetPlayerDeaths() int32`

GetPlayerDeaths returns the PlayerDeaths field if non-nil, zero value otherwise.

### GetPlayerDeathsOk

`func (o *PlayerMatchHistoryEntry) GetPlayerDeathsOk() (*int32, bool)`

GetPlayerDeathsOk returns a tuple with the PlayerDeaths field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerDeaths

`func (o *PlayerMatchHistoryEntry) SetPlayerDeaths(v int32)`

SetPlayerDeaths sets PlayerDeaths field to given value.


### GetPlayerKills

`func (o *PlayerMatchHistoryEntry) GetPlayerKills() int32`

GetPlayerKills returns the PlayerKills field if non-nil, zero value otherwise.

### GetPlayerKillsOk

`func (o *PlayerMatchHistoryEntry) GetPlayerKillsOk() (*int32, bool)`

GetPlayerKillsOk returns a tuple with the PlayerKills field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerKills

`func (o *PlayerMatchHistoryEntry) SetPlayerKills(v int32)`

SetPlayerKills sets PlayerKills field to given value.


### GetPlayerTeam

`func (o *PlayerMatchHistoryEntry) GetPlayerTeam() int32`

GetPlayerTeam returns the PlayerTeam field if non-nil, zero value otherwise.

### GetPlayerTeamOk

`func (o *PlayerMatchHistoryEntry) GetPlayerTeamOk() (*int32, bool)`

GetPlayerTeamOk returns a tuple with the PlayerTeam field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerTeam

`func (o *PlayerMatchHistoryEntry) SetPlayerTeam(v int32)`

SetPlayerTeam sets PlayerTeam field to given value.


### GetStartTime

`func (o *PlayerMatchHistoryEntry) GetStartTime() int32`

GetStartTime returns the StartTime field if non-nil, zero value otherwise.

### GetStartTimeOk

`func (o *PlayerMatchHistoryEntry) GetStartTimeOk() (*int32, bool)`

GetStartTimeOk returns a tuple with the StartTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTime

`func (o *PlayerMatchHistoryEntry) SetStartTime(v int32)`

SetStartTime sets StartTime field to given value.


### GetTeamAbandoned

`func (o *PlayerMatchHistoryEntry) GetTeamAbandoned() bool`

GetTeamAbandoned returns the TeamAbandoned field if non-nil, zero value otherwise.

### GetTeamAbandonedOk

`func (o *PlayerMatchHistoryEntry) GetTeamAbandonedOk() (*bool, bool)`

GetTeamAbandonedOk returns a tuple with the TeamAbandoned field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTeamAbandoned

`func (o *PlayerMatchHistoryEntry) SetTeamAbandoned(v bool)`

SetTeamAbandoned sets TeamAbandoned field to given value.

### HasTeamAbandoned

`func (o *PlayerMatchHistoryEntry) HasTeamAbandoned() bool`

HasTeamAbandoned returns a boolean if a field has been set.

### SetTeamAbandonedNil

`func (o *PlayerMatchHistoryEntry) SetTeamAbandonedNil(b bool)`

 SetTeamAbandonedNil sets the value for TeamAbandoned to be an explicit nil

### UnsetTeamAbandoned
`func (o *PlayerMatchHistoryEntry) UnsetTeamAbandoned()`

UnsetTeamAbandoned ensures that no value is present for TeamAbandoned, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


