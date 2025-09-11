# HeroStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **int32** |  | 
**Accuracy** | **float64** |  | 
**Assists** | **int64** |  | 
**AssistsPerMin** | **float64** |  | 
**CreepsPerMin** | **float64** |  | 
**CritShotRate** | **float64** |  | 
**DamageMitigatedPerMin** | **float64** |  | 
**DamagePerMin** | **float64** |  | 
**DamagePerSoul** | **float64** |  | 
**DamageTakenPerMin** | **float64** |  | 
**DamageTakenPerSoul** | **float64** |  | 
**Deaths** | **int64** |  | 
**DeathsPerMin** | **float64** |  | 
**DeniesPerMatch** | **float64** |  | 
**DeniesPerMin** | **float64** |  | 
**EndingLevel** | **float64** |  | 
**HeroId** | **int32** | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**Kills** | **int64** |  | 
**KillsPerMin** | **float64** |  | 
**LastHitsPerMin** | **float64** |  | 
**LastPlayed** | **int32** |  | 
**Matches** | **[]int64** |  | 
**MatchesPlayed** | **int64** |  | 
**NetworthPerMin** | **float64** |  | 
**ObjDamagePerMin** | **float64** |  | 
**ObjDamagePerSoul** | **float64** |  | 
**TimePlayed** | **int64** |  | 
**Wins** | **int64** |  | 

## Methods

### NewHeroStats

`func NewHeroStats(accountId int32, accuracy float64, assists int64, assistsPerMin float64, creepsPerMin float64, critShotRate float64, damageMitigatedPerMin float64, damagePerMin float64, damagePerSoul float64, damageTakenPerMin float64, damageTakenPerSoul float64, deaths int64, deathsPerMin float64, deniesPerMatch float64, deniesPerMin float64, endingLevel float64, heroId int32, kills int64, killsPerMin float64, lastHitsPerMin float64, lastPlayed int32, matches []int64, matchesPlayed int64, networthPerMin float64, objDamagePerMin float64, objDamagePerSoul float64, timePlayed int64, wins int64, ) *HeroStats`

NewHeroStats instantiates a new HeroStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHeroStatsWithDefaults

`func NewHeroStatsWithDefaults() *HeroStats`

NewHeroStatsWithDefaults instantiates a new HeroStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccountId

`func (o *HeroStats) GetAccountId() int32`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *HeroStats) GetAccountIdOk() (*int32, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *HeroStats) SetAccountId(v int32)`

SetAccountId sets AccountId field to given value.


### GetAccuracy

`func (o *HeroStats) GetAccuracy() float64`

GetAccuracy returns the Accuracy field if non-nil, zero value otherwise.

### GetAccuracyOk

`func (o *HeroStats) GetAccuracyOk() (*float64, bool)`

GetAccuracyOk returns a tuple with the Accuracy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccuracy

`func (o *HeroStats) SetAccuracy(v float64)`

SetAccuracy sets Accuracy field to given value.


### GetAssists

`func (o *HeroStats) GetAssists() int64`

GetAssists returns the Assists field if non-nil, zero value otherwise.

### GetAssistsOk

`func (o *HeroStats) GetAssistsOk() (*int64, bool)`

GetAssistsOk returns a tuple with the Assists field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssists

`func (o *HeroStats) SetAssists(v int64)`

SetAssists sets Assists field to given value.


### GetAssistsPerMin

`func (o *HeroStats) GetAssistsPerMin() float64`

GetAssistsPerMin returns the AssistsPerMin field if non-nil, zero value otherwise.

### GetAssistsPerMinOk

`func (o *HeroStats) GetAssistsPerMinOk() (*float64, bool)`

GetAssistsPerMinOk returns a tuple with the AssistsPerMin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssistsPerMin

`func (o *HeroStats) SetAssistsPerMin(v float64)`

SetAssistsPerMin sets AssistsPerMin field to given value.


### GetCreepsPerMin

`func (o *HeroStats) GetCreepsPerMin() float64`

GetCreepsPerMin returns the CreepsPerMin field if non-nil, zero value otherwise.

### GetCreepsPerMinOk

`func (o *HeroStats) GetCreepsPerMinOk() (*float64, bool)`

GetCreepsPerMinOk returns a tuple with the CreepsPerMin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreepsPerMin

`func (o *HeroStats) SetCreepsPerMin(v float64)`

SetCreepsPerMin sets CreepsPerMin field to given value.


### GetCritShotRate

`func (o *HeroStats) GetCritShotRate() float64`

GetCritShotRate returns the CritShotRate field if non-nil, zero value otherwise.

### GetCritShotRateOk

`func (o *HeroStats) GetCritShotRateOk() (*float64, bool)`

GetCritShotRateOk returns a tuple with the CritShotRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCritShotRate

`func (o *HeroStats) SetCritShotRate(v float64)`

SetCritShotRate sets CritShotRate field to given value.


### GetDamageMitigatedPerMin

`func (o *HeroStats) GetDamageMitigatedPerMin() float64`

GetDamageMitigatedPerMin returns the DamageMitigatedPerMin field if non-nil, zero value otherwise.

### GetDamageMitigatedPerMinOk

`func (o *HeroStats) GetDamageMitigatedPerMinOk() (*float64, bool)`

GetDamageMitigatedPerMinOk returns a tuple with the DamageMitigatedPerMin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamageMitigatedPerMin

`func (o *HeroStats) SetDamageMitigatedPerMin(v float64)`

SetDamageMitigatedPerMin sets DamageMitigatedPerMin field to given value.


### GetDamagePerMin

`func (o *HeroStats) GetDamagePerMin() float64`

GetDamagePerMin returns the DamagePerMin field if non-nil, zero value otherwise.

### GetDamagePerMinOk

`func (o *HeroStats) GetDamagePerMinOk() (*float64, bool)`

GetDamagePerMinOk returns a tuple with the DamagePerMin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamagePerMin

`func (o *HeroStats) SetDamagePerMin(v float64)`

SetDamagePerMin sets DamagePerMin field to given value.


### GetDamagePerSoul

`func (o *HeroStats) GetDamagePerSoul() float64`

GetDamagePerSoul returns the DamagePerSoul field if non-nil, zero value otherwise.

### GetDamagePerSoulOk

`func (o *HeroStats) GetDamagePerSoulOk() (*float64, bool)`

GetDamagePerSoulOk returns a tuple with the DamagePerSoul field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamagePerSoul

`func (o *HeroStats) SetDamagePerSoul(v float64)`

SetDamagePerSoul sets DamagePerSoul field to given value.


### GetDamageTakenPerMin

`func (o *HeroStats) GetDamageTakenPerMin() float64`

GetDamageTakenPerMin returns the DamageTakenPerMin field if non-nil, zero value otherwise.

### GetDamageTakenPerMinOk

`func (o *HeroStats) GetDamageTakenPerMinOk() (*float64, bool)`

GetDamageTakenPerMinOk returns a tuple with the DamageTakenPerMin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamageTakenPerMin

`func (o *HeroStats) SetDamageTakenPerMin(v float64)`

SetDamageTakenPerMin sets DamageTakenPerMin field to given value.


### GetDamageTakenPerSoul

`func (o *HeroStats) GetDamageTakenPerSoul() float64`

GetDamageTakenPerSoul returns the DamageTakenPerSoul field if non-nil, zero value otherwise.

### GetDamageTakenPerSoulOk

`func (o *HeroStats) GetDamageTakenPerSoulOk() (*float64, bool)`

GetDamageTakenPerSoulOk returns a tuple with the DamageTakenPerSoul field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamageTakenPerSoul

`func (o *HeroStats) SetDamageTakenPerSoul(v float64)`

SetDamageTakenPerSoul sets DamageTakenPerSoul field to given value.


### GetDeaths

`func (o *HeroStats) GetDeaths() int64`

GetDeaths returns the Deaths field if non-nil, zero value otherwise.

### GetDeathsOk

`func (o *HeroStats) GetDeathsOk() (*int64, bool)`

GetDeathsOk returns a tuple with the Deaths field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeaths

`func (o *HeroStats) SetDeaths(v int64)`

SetDeaths sets Deaths field to given value.


### GetDeathsPerMin

`func (o *HeroStats) GetDeathsPerMin() float64`

GetDeathsPerMin returns the DeathsPerMin field if non-nil, zero value otherwise.

### GetDeathsPerMinOk

`func (o *HeroStats) GetDeathsPerMinOk() (*float64, bool)`

GetDeathsPerMinOk returns a tuple with the DeathsPerMin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeathsPerMin

`func (o *HeroStats) SetDeathsPerMin(v float64)`

SetDeathsPerMin sets DeathsPerMin field to given value.


### GetDeniesPerMatch

`func (o *HeroStats) GetDeniesPerMatch() float64`

GetDeniesPerMatch returns the DeniesPerMatch field if non-nil, zero value otherwise.

### GetDeniesPerMatchOk

`func (o *HeroStats) GetDeniesPerMatchOk() (*float64, bool)`

GetDeniesPerMatchOk returns a tuple with the DeniesPerMatch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeniesPerMatch

`func (o *HeroStats) SetDeniesPerMatch(v float64)`

SetDeniesPerMatch sets DeniesPerMatch field to given value.


### GetDeniesPerMin

`func (o *HeroStats) GetDeniesPerMin() float64`

GetDeniesPerMin returns the DeniesPerMin field if non-nil, zero value otherwise.

### GetDeniesPerMinOk

`func (o *HeroStats) GetDeniesPerMinOk() (*float64, bool)`

GetDeniesPerMinOk returns a tuple with the DeniesPerMin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeniesPerMin

`func (o *HeroStats) SetDeniesPerMin(v float64)`

SetDeniesPerMin sets DeniesPerMin field to given value.


### GetEndingLevel

`func (o *HeroStats) GetEndingLevel() float64`

GetEndingLevel returns the EndingLevel field if non-nil, zero value otherwise.

### GetEndingLevelOk

`func (o *HeroStats) GetEndingLevelOk() (*float64, bool)`

GetEndingLevelOk returns a tuple with the EndingLevel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndingLevel

`func (o *HeroStats) SetEndingLevel(v float64)`

SetEndingLevel sets EndingLevel field to given value.


### GetHeroId

`func (o *HeroStats) GetHeroId() int32`

GetHeroId returns the HeroId field if non-nil, zero value otherwise.

### GetHeroIdOk

`func (o *HeroStats) GetHeroIdOk() (*int32, bool)`

GetHeroIdOk returns a tuple with the HeroId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroId

`func (o *HeroStats) SetHeroId(v int32)`

SetHeroId sets HeroId field to given value.


### GetKills

`func (o *HeroStats) GetKills() int64`

GetKills returns the Kills field if non-nil, zero value otherwise.

### GetKillsOk

`func (o *HeroStats) GetKillsOk() (*int64, bool)`

GetKillsOk returns a tuple with the Kills field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKills

`func (o *HeroStats) SetKills(v int64)`

SetKills sets Kills field to given value.


### GetKillsPerMin

`func (o *HeroStats) GetKillsPerMin() float64`

GetKillsPerMin returns the KillsPerMin field if non-nil, zero value otherwise.

### GetKillsPerMinOk

`func (o *HeroStats) GetKillsPerMinOk() (*float64, bool)`

GetKillsPerMinOk returns a tuple with the KillsPerMin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKillsPerMin

`func (o *HeroStats) SetKillsPerMin(v float64)`

SetKillsPerMin sets KillsPerMin field to given value.


### GetLastHitsPerMin

`func (o *HeroStats) GetLastHitsPerMin() float64`

GetLastHitsPerMin returns the LastHitsPerMin field if non-nil, zero value otherwise.

### GetLastHitsPerMinOk

`func (o *HeroStats) GetLastHitsPerMinOk() (*float64, bool)`

GetLastHitsPerMinOk returns a tuple with the LastHitsPerMin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastHitsPerMin

`func (o *HeroStats) SetLastHitsPerMin(v float64)`

SetLastHitsPerMin sets LastHitsPerMin field to given value.


### GetLastPlayed

`func (o *HeroStats) GetLastPlayed() int32`

GetLastPlayed returns the LastPlayed field if non-nil, zero value otherwise.

### GetLastPlayedOk

`func (o *HeroStats) GetLastPlayedOk() (*int32, bool)`

GetLastPlayedOk returns a tuple with the LastPlayed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastPlayed

`func (o *HeroStats) SetLastPlayed(v int32)`

SetLastPlayed sets LastPlayed field to given value.


### GetMatches

`func (o *HeroStats) GetMatches() []int64`

GetMatches returns the Matches field if non-nil, zero value otherwise.

### GetMatchesOk

`func (o *HeroStats) GetMatchesOk() (*[]int64, bool)`

GetMatchesOk returns a tuple with the Matches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatches

`func (o *HeroStats) SetMatches(v []int64)`

SetMatches sets Matches field to given value.


### GetMatchesPlayed

`func (o *HeroStats) GetMatchesPlayed() int64`

GetMatchesPlayed returns the MatchesPlayed field if non-nil, zero value otherwise.

### GetMatchesPlayedOk

`func (o *HeroStats) GetMatchesPlayedOk() (*int64, bool)`

GetMatchesPlayedOk returns a tuple with the MatchesPlayed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchesPlayed

`func (o *HeroStats) SetMatchesPlayed(v int64)`

SetMatchesPlayed sets MatchesPlayed field to given value.


### GetNetworthPerMin

`func (o *HeroStats) GetNetworthPerMin() float64`

GetNetworthPerMin returns the NetworthPerMin field if non-nil, zero value otherwise.

### GetNetworthPerMinOk

`func (o *HeroStats) GetNetworthPerMinOk() (*float64, bool)`

GetNetworthPerMinOk returns a tuple with the NetworthPerMin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetworthPerMin

`func (o *HeroStats) SetNetworthPerMin(v float64)`

SetNetworthPerMin sets NetworthPerMin field to given value.


### GetObjDamagePerMin

`func (o *HeroStats) GetObjDamagePerMin() float64`

GetObjDamagePerMin returns the ObjDamagePerMin field if non-nil, zero value otherwise.

### GetObjDamagePerMinOk

`func (o *HeroStats) GetObjDamagePerMinOk() (*float64, bool)`

GetObjDamagePerMinOk returns a tuple with the ObjDamagePerMin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjDamagePerMin

`func (o *HeroStats) SetObjDamagePerMin(v float64)`

SetObjDamagePerMin sets ObjDamagePerMin field to given value.


### GetObjDamagePerSoul

`func (o *HeroStats) GetObjDamagePerSoul() float64`

GetObjDamagePerSoul returns the ObjDamagePerSoul field if non-nil, zero value otherwise.

### GetObjDamagePerSoulOk

`func (o *HeroStats) GetObjDamagePerSoulOk() (*float64, bool)`

GetObjDamagePerSoulOk returns a tuple with the ObjDamagePerSoul field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjDamagePerSoul

`func (o *HeroStats) SetObjDamagePerSoul(v float64)`

SetObjDamagePerSoul sets ObjDamagePerSoul field to given value.


### GetTimePlayed

`func (o *HeroStats) GetTimePlayed() int64`

GetTimePlayed returns the TimePlayed field if non-nil, zero value otherwise.

### GetTimePlayedOk

`func (o *HeroStats) GetTimePlayedOk() (*int64, bool)`

GetTimePlayedOk returns a tuple with the TimePlayed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimePlayed

`func (o *HeroStats) SetTimePlayed(v int64)`

SetTimePlayed sets TimePlayed field to given value.


### GetWins

`func (o *HeroStats) GetWins() int64`

GetWins returns the Wins field if non-nil, zero value otherwise.

### GetWinsOk

`func (o *HeroStats) GetWinsOk() (*int64, bool)`

GetWinsOk returns a tuple with the Wins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWins

`func (o *HeroStats) SetWins(v int64)`

SetWins sets Wins field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


