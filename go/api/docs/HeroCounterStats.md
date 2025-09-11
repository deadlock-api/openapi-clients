# HeroCounterStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Assists** | **int64** | The number of assists by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | 
**Creeps** | **int64** | The number of creeps killed by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | 
**Deaths** | **int64** | The number of deaths by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | 
**Denies** | **int64** | The number of denies by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | 
**EnemyAssists** | **int64** | The number of assists by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | 
**EnemyCreeps** | **int64** | The number of creeps killed by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | 
**EnemyDeaths** | **int64** | The number of deaths by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | 
**EnemyDenies** | **int64** | The number of denies by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | 
**EnemyHeroId** | **int32** | The ID of the opposing hero. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**EnemyKills** | **int64** | The number of kills by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | 
**EnemyLastHits** | **int64** | The number of last hits by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | 
**EnemyNetworth** | **int64** | The net worth of &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | 
**EnemyObjDamage** | **int64** | The amount of objective damage dealt by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | 
**HeroId** | **int32** | The ID of the hero. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**Kills** | **int64** | The number of kills by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | 
**LastHits** | **int64** | The number of last hits by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | 
**MatchesPlayed** | **int64** | The total number of matches played between &#x60;hero_id&#x60; and &#x60;enemy_hero_id&#x60; that meet the filter criteria. | 
**Networth** | **int64** | The net worth of &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | 
**ObjDamage** | **int64** | The amount of objective damage dealt by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | 
**Wins** | **int64** | The number of times &#x60;hero_id&#x60; won the match when facing &#x60;enemy_hero_id&#x60;. | 

## Methods

### NewHeroCounterStats

`func NewHeroCounterStats(assists int64, creeps int64, deaths int64, denies int64, enemyAssists int64, enemyCreeps int64, enemyDeaths int64, enemyDenies int64, enemyHeroId int32, enemyKills int64, enemyLastHits int64, enemyNetworth int64, enemyObjDamage int64, heroId int32, kills int64, lastHits int64, matchesPlayed int64, networth int64, objDamage int64, wins int64, ) *HeroCounterStats`

NewHeroCounterStats instantiates a new HeroCounterStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHeroCounterStatsWithDefaults

`func NewHeroCounterStatsWithDefaults() *HeroCounterStats`

NewHeroCounterStatsWithDefaults instantiates a new HeroCounterStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAssists

`func (o *HeroCounterStats) GetAssists() int64`

GetAssists returns the Assists field if non-nil, zero value otherwise.

### GetAssistsOk

`func (o *HeroCounterStats) GetAssistsOk() (*int64, bool)`

GetAssistsOk returns a tuple with the Assists field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssists

`func (o *HeroCounterStats) SetAssists(v int64)`

SetAssists sets Assists field to given value.


### GetCreeps

`func (o *HeroCounterStats) GetCreeps() int64`

GetCreeps returns the Creeps field if non-nil, zero value otherwise.

### GetCreepsOk

`func (o *HeroCounterStats) GetCreepsOk() (*int64, bool)`

GetCreepsOk returns a tuple with the Creeps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreeps

`func (o *HeroCounterStats) SetCreeps(v int64)`

SetCreeps sets Creeps field to given value.


### GetDeaths

`func (o *HeroCounterStats) GetDeaths() int64`

GetDeaths returns the Deaths field if non-nil, zero value otherwise.

### GetDeathsOk

`func (o *HeroCounterStats) GetDeathsOk() (*int64, bool)`

GetDeathsOk returns a tuple with the Deaths field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeaths

`func (o *HeroCounterStats) SetDeaths(v int64)`

SetDeaths sets Deaths field to given value.


### GetDenies

`func (o *HeroCounterStats) GetDenies() int64`

GetDenies returns the Denies field if non-nil, zero value otherwise.

### GetDeniesOk

`func (o *HeroCounterStats) GetDeniesOk() (*int64, bool)`

GetDeniesOk returns a tuple with the Denies field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDenies

`func (o *HeroCounterStats) SetDenies(v int64)`

SetDenies sets Denies field to given value.


### GetEnemyAssists

`func (o *HeroCounterStats) GetEnemyAssists() int64`

GetEnemyAssists returns the EnemyAssists field if non-nil, zero value otherwise.

### GetEnemyAssistsOk

`func (o *HeroCounterStats) GetEnemyAssistsOk() (*int64, bool)`

GetEnemyAssistsOk returns a tuple with the EnemyAssists field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyAssists

`func (o *HeroCounterStats) SetEnemyAssists(v int64)`

SetEnemyAssists sets EnemyAssists field to given value.


### GetEnemyCreeps

`func (o *HeroCounterStats) GetEnemyCreeps() int64`

GetEnemyCreeps returns the EnemyCreeps field if non-nil, zero value otherwise.

### GetEnemyCreepsOk

`func (o *HeroCounterStats) GetEnemyCreepsOk() (*int64, bool)`

GetEnemyCreepsOk returns a tuple with the EnemyCreeps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyCreeps

`func (o *HeroCounterStats) SetEnemyCreeps(v int64)`

SetEnemyCreeps sets EnemyCreeps field to given value.


### GetEnemyDeaths

`func (o *HeroCounterStats) GetEnemyDeaths() int64`

GetEnemyDeaths returns the EnemyDeaths field if non-nil, zero value otherwise.

### GetEnemyDeathsOk

`func (o *HeroCounterStats) GetEnemyDeathsOk() (*int64, bool)`

GetEnemyDeathsOk returns a tuple with the EnemyDeaths field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyDeaths

`func (o *HeroCounterStats) SetEnemyDeaths(v int64)`

SetEnemyDeaths sets EnemyDeaths field to given value.


### GetEnemyDenies

`func (o *HeroCounterStats) GetEnemyDenies() int64`

GetEnemyDenies returns the EnemyDenies field if non-nil, zero value otherwise.

### GetEnemyDeniesOk

`func (o *HeroCounterStats) GetEnemyDeniesOk() (*int64, bool)`

GetEnemyDeniesOk returns a tuple with the EnemyDenies field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyDenies

`func (o *HeroCounterStats) SetEnemyDenies(v int64)`

SetEnemyDenies sets EnemyDenies field to given value.


### GetEnemyHeroId

`func (o *HeroCounterStats) GetEnemyHeroId() int32`

GetEnemyHeroId returns the EnemyHeroId field if non-nil, zero value otherwise.

### GetEnemyHeroIdOk

`func (o *HeroCounterStats) GetEnemyHeroIdOk() (*int32, bool)`

GetEnemyHeroIdOk returns a tuple with the EnemyHeroId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyHeroId

`func (o *HeroCounterStats) SetEnemyHeroId(v int32)`

SetEnemyHeroId sets EnemyHeroId field to given value.


### GetEnemyKills

`func (o *HeroCounterStats) GetEnemyKills() int64`

GetEnemyKills returns the EnemyKills field if non-nil, zero value otherwise.

### GetEnemyKillsOk

`func (o *HeroCounterStats) GetEnemyKillsOk() (*int64, bool)`

GetEnemyKillsOk returns a tuple with the EnemyKills field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyKills

`func (o *HeroCounterStats) SetEnemyKills(v int64)`

SetEnemyKills sets EnemyKills field to given value.


### GetEnemyLastHits

`func (o *HeroCounterStats) GetEnemyLastHits() int64`

GetEnemyLastHits returns the EnemyLastHits field if non-nil, zero value otherwise.

### GetEnemyLastHitsOk

`func (o *HeroCounterStats) GetEnemyLastHitsOk() (*int64, bool)`

GetEnemyLastHitsOk returns a tuple with the EnemyLastHits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyLastHits

`func (o *HeroCounterStats) SetEnemyLastHits(v int64)`

SetEnemyLastHits sets EnemyLastHits field to given value.


### GetEnemyNetworth

`func (o *HeroCounterStats) GetEnemyNetworth() int64`

GetEnemyNetworth returns the EnemyNetworth field if non-nil, zero value otherwise.

### GetEnemyNetworthOk

`func (o *HeroCounterStats) GetEnemyNetworthOk() (*int64, bool)`

GetEnemyNetworthOk returns a tuple with the EnemyNetworth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyNetworth

`func (o *HeroCounterStats) SetEnemyNetworth(v int64)`

SetEnemyNetworth sets EnemyNetworth field to given value.


### GetEnemyObjDamage

`func (o *HeroCounterStats) GetEnemyObjDamage() int64`

GetEnemyObjDamage returns the EnemyObjDamage field if non-nil, zero value otherwise.

### GetEnemyObjDamageOk

`func (o *HeroCounterStats) GetEnemyObjDamageOk() (*int64, bool)`

GetEnemyObjDamageOk returns a tuple with the EnemyObjDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyObjDamage

`func (o *HeroCounterStats) SetEnemyObjDamage(v int64)`

SetEnemyObjDamage sets EnemyObjDamage field to given value.


### GetHeroId

`func (o *HeroCounterStats) GetHeroId() int32`

GetHeroId returns the HeroId field if non-nil, zero value otherwise.

### GetHeroIdOk

`func (o *HeroCounterStats) GetHeroIdOk() (*int32, bool)`

GetHeroIdOk returns a tuple with the HeroId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroId

`func (o *HeroCounterStats) SetHeroId(v int32)`

SetHeroId sets HeroId field to given value.


### GetKills

`func (o *HeroCounterStats) GetKills() int64`

GetKills returns the Kills field if non-nil, zero value otherwise.

### GetKillsOk

`func (o *HeroCounterStats) GetKillsOk() (*int64, bool)`

GetKillsOk returns a tuple with the Kills field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKills

`func (o *HeroCounterStats) SetKills(v int64)`

SetKills sets Kills field to given value.


### GetLastHits

`func (o *HeroCounterStats) GetLastHits() int64`

GetLastHits returns the LastHits field if non-nil, zero value otherwise.

### GetLastHitsOk

`func (o *HeroCounterStats) GetLastHitsOk() (*int64, bool)`

GetLastHitsOk returns a tuple with the LastHits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastHits

`func (o *HeroCounterStats) SetLastHits(v int64)`

SetLastHits sets LastHits field to given value.


### GetMatchesPlayed

`func (o *HeroCounterStats) GetMatchesPlayed() int64`

GetMatchesPlayed returns the MatchesPlayed field if non-nil, zero value otherwise.

### GetMatchesPlayedOk

`func (o *HeroCounterStats) GetMatchesPlayedOk() (*int64, bool)`

GetMatchesPlayedOk returns a tuple with the MatchesPlayed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchesPlayed

`func (o *HeroCounterStats) SetMatchesPlayed(v int64)`

SetMatchesPlayed sets MatchesPlayed field to given value.


### GetNetworth

`func (o *HeroCounterStats) GetNetworth() int64`

GetNetworth returns the Networth field if non-nil, zero value otherwise.

### GetNetworthOk

`func (o *HeroCounterStats) GetNetworthOk() (*int64, bool)`

GetNetworthOk returns a tuple with the Networth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetworth

`func (o *HeroCounterStats) SetNetworth(v int64)`

SetNetworth sets Networth field to given value.


### GetObjDamage

`func (o *HeroCounterStats) GetObjDamage() int64`

GetObjDamage returns the ObjDamage field if non-nil, zero value otherwise.

### GetObjDamageOk

`func (o *HeroCounterStats) GetObjDamageOk() (*int64, bool)`

GetObjDamageOk returns a tuple with the ObjDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjDamage

`func (o *HeroCounterStats) SetObjDamage(v int64)`

SetObjDamage sets ObjDamage field to given value.


### GetWins

`func (o *HeroCounterStats) GetWins() int64`

GetWins returns the Wins field if non-nil, zero value otherwise.

### GetWinsOk

`func (o *HeroCounterStats) GetWinsOk() (*int64, bool)`

GetWinsOk returns a tuple with the Wins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWins

`func (o *HeroCounterStats) SetWins(v int64)`

SetWins sets Wins field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


