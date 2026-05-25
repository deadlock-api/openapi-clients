# HeroSynergyStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Assists1** | **int64** | The number of assists by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | 
**Assists2** | **int64** | The number of assists by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | 
**Creeps1** | **int64** | The number of creeps killed by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | 
**Creeps2** | **int64** | The number of creeps killed by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | 
**Deaths1** | **int64** | The number of deaths by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | 
**Deaths2** | **int64** | The number of deaths by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | 
**Denies1** | **int64** | The number of denies by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | 
**Denies2** | **int64** | The number of denies by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | 
**HeroId1** | **int32** | The ID of the first hero in the pair. | 
**HeroId2** | **int32** | The ID of the second hero in the pair. | 
**Kills1** | **int64** | The number of kills by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | 
**Kills2** | **int64** | The number of kills by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | 
**LastHits1** | **int64** | The number of last hits by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | 
**LastHits2** | **int64** | The number of last hits by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | 
**MatchesPlayed** | **int64** | The total number of matches played where &#x60;hero_id1&#x60; and &#x60;hero_id2&#x60; were on the same team, meeting the filter criteria. | 
**Networth1** | **int64** | The net worth of &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | 
**Networth2** | **int64** | The net worth of &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | 
**ObjDamage1** | **int64** | The amount of objective damage dealt by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | 
**ObjDamage2** | **int64** | The amount of objective damage dealt by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | 
**Wins** | **int64** | The number of times the team won when both &#x60;hero_id1&#x60; and &#x60;hero_id2&#x60; were on the same team. | 

## Methods

### NewHeroSynergyStats

`func NewHeroSynergyStats(assists1 int64, assists2 int64, creeps1 int64, creeps2 int64, deaths1 int64, deaths2 int64, denies1 int64, denies2 int64, heroId1 int32, heroId2 int32, kills1 int64, kills2 int64, lastHits1 int64, lastHits2 int64, matchesPlayed int64, networth1 int64, networth2 int64, objDamage1 int64, objDamage2 int64, wins int64, ) *HeroSynergyStats`

NewHeroSynergyStats instantiates a new HeroSynergyStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHeroSynergyStatsWithDefaults

`func NewHeroSynergyStatsWithDefaults() *HeroSynergyStats`

NewHeroSynergyStatsWithDefaults instantiates a new HeroSynergyStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAssists1

`func (o *HeroSynergyStats) GetAssists1() int64`

GetAssists1 returns the Assists1 field if non-nil, zero value otherwise.

### GetAssists1Ok

`func (o *HeroSynergyStats) GetAssists1Ok() (*int64, bool)`

GetAssists1Ok returns a tuple with the Assists1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssists1

`func (o *HeroSynergyStats) SetAssists1(v int64)`

SetAssists1 sets Assists1 field to given value.


### GetAssists2

`func (o *HeroSynergyStats) GetAssists2() int64`

GetAssists2 returns the Assists2 field if non-nil, zero value otherwise.

### GetAssists2Ok

`func (o *HeroSynergyStats) GetAssists2Ok() (*int64, bool)`

GetAssists2Ok returns a tuple with the Assists2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssists2

`func (o *HeroSynergyStats) SetAssists2(v int64)`

SetAssists2 sets Assists2 field to given value.


### GetCreeps1

`func (o *HeroSynergyStats) GetCreeps1() int64`

GetCreeps1 returns the Creeps1 field if non-nil, zero value otherwise.

### GetCreeps1Ok

`func (o *HeroSynergyStats) GetCreeps1Ok() (*int64, bool)`

GetCreeps1Ok returns a tuple with the Creeps1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreeps1

`func (o *HeroSynergyStats) SetCreeps1(v int64)`

SetCreeps1 sets Creeps1 field to given value.


### GetCreeps2

`func (o *HeroSynergyStats) GetCreeps2() int64`

GetCreeps2 returns the Creeps2 field if non-nil, zero value otherwise.

### GetCreeps2Ok

`func (o *HeroSynergyStats) GetCreeps2Ok() (*int64, bool)`

GetCreeps2Ok returns a tuple with the Creeps2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreeps2

`func (o *HeroSynergyStats) SetCreeps2(v int64)`

SetCreeps2 sets Creeps2 field to given value.


### GetDeaths1

`func (o *HeroSynergyStats) GetDeaths1() int64`

GetDeaths1 returns the Deaths1 field if non-nil, zero value otherwise.

### GetDeaths1Ok

`func (o *HeroSynergyStats) GetDeaths1Ok() (*int64, bool)`

GetDeaths1Ok returns a tuple with the Deaths1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeaths1

`func (o *HeroSynergyStats) SetDeaths1(v int64)`

SetDeaths1 sets Deaths1 field to given value.


### GetDeaths2

`func (o *HeroSynergyStats) GetDeaths2() int64`

GetDeaths2 returns the Deaths2 field if non-nil, zero value otherwise.

### GetDeaths2Ok

`func (o *HeroSynergyStats) GetDeaths2Ok() (*int64, bool)`

GetDeaths2Ok returns a tuple with the Deaths2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeaths2

`func (o *HeroSynergyStats) SetDeaths2(v int64)`

SetDeaths2 sets Deaths2 field to given value.


### GetDenies1

`func (o *HeroSynergyStats) GetDenies1() int64`

GetDenies1 returns the Denies1 field if non-nil, zero value otherwise.

### GetDenies1Ok

`func (o *HeroSynergyStats) GetDenies1Ok() (*int64, bool)`

GetDenies1Ok returns a tuple with the Denies1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDenies1

`func (o *HeroSynergyStats) SetDenies1(v int64)`

SetDenies1 sets Denies1 field to given value.


### GetDenies2

`func (o *HeroSynergyStats) GetDenies2() int64`

GetDenies2 returns the Denies2 field if non-nil, zero value otherwise.

### GetDenies2Ok

`func (o *HeroSynergyStats) GetDenies2Ok() (*int64, bool)`

GetDenies2Ok returns a tuple with the Denies2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDenies2

`func (o *HeroSynergyStats) SetDenies2(v int64)`

SetDenies2 sets Denies2 field to given value.


### GetHeroId1

`func (o *HeroSynergyStats) GetHeroId1() int32`

GetHeroId1 returns the HeroId1 field if non-nil, zero value otherwise.

### GetHeroId1Ok

`func (o *HeroSynergyStats) GetHeroId1Ok() (*int32, bool)`

GetHeroId1Ok returns a tuple with the HeroId1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroId1

`func (o *HeroSynergyStats) SetHeroId1(v int32)`

SetHeroId1 sets HeroId1 field to given value.


### GetHeroId2

`func (o *HeroSynergyStats) GetHeroId2() int32`

GetHeroId2 returns the HeroId2 field if non-nil, zero value otherwise.

### GetHeroId2Ok

`func (o *HeroSynergyStats) GetHeroId2Ok() (*int32, bool)`

GetHeroId2Ok returns a tuple with the HeroId2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroId2

`func (o *HeroSynergyStats) SetHeroId2(v int32)`

SetHeroId2 sets HeroId2 field to given value.


### GetKills1

`func (o *HeroSynergyStats) GetKills1() int64`

GetKills1 returns the Kills1 field if non-nil, zero value otherwise.

### GetKills1Ok

`func (o *HeroSynergyStats) GetKills1Ok() (*int64, bool)`

GetKills1Ok returns a tuple with the Kills1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKills1

`func (o *HeroSynergyStats) SetKills1(v int64)`

SetKills1 sets Kills1 field to given value.


### GetKills2

`func (o *HeroSynergyStats) GetKills2() int64`

GetKills2 returns the Kills2 field if non-nil, zero value otherwise.

### GetKills2Ok

`func (o *HeroSynergyStats) GetKills2Ok() (*int64, bool)`

GetKills2Ok returns a tuple with the Kills2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKills2

`func (o *HeroSynergyStats) SetKills2(v int64)`

SetKills2 sets Kills2 field to given value.


### GetLastHits1

`func (o *HeroSynergyStats) GetLastHits1() int64`

GetLastHits1 returns the LastHits1 field if non-nil, zero value otherwise.

### GetLastHits1Ok

`func (o *HeroSynergyStats) GetLastHits1Ok() (*int64, bool)`

GetLastHits1Ok returns a tuple with the LastHits1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastHits1

`func (o *HeroSynergyStats) SetLastHits1(v int64)`

SetLastHits1 sets LastHits1 field to given value.


### GetLastHits2

`func (o *HeroSynergyStats) GetLastHits2() int64`

GetLastHits2 returns the LastHits2 field if non-nil, zero value otherwise.

### GetLastHits2Ok

`func (o *HeroSynergyStats) GetLastHits2Ok() (*int64, bool)`

GetLastHits2Ok returns a tuple with the LastHits2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastHits2

`func (o *HeroSynergyStats) SetLastHits2(v int64)`

SetLastHits2 sets LastHits2 field to given value.


### GetMatchesPlayed

`func (o *HeroSynergyStats) GetMatchesPlayed() int64`

GetMatchesPlayed returns the MatchesPlayed field if non-nil, zero value otherwise.

### GetMatchesPlayedOk

`func (o *HeroSynergyStats) GetMatchesPlayedOk() (*int64, bool)`

GetMatchesPlayedOk returns a tuple with the MatchesPlayed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchesPlayed

`func (o *HeroSynergyStats) SetMatchesPlayed(v int64)`

SetMatchesPlayed sets MatchesPlayed field to given value.


### GetNetworth1

`func (o *HeroSynergyStats) GetNetworth1() int64`

GetNetworth1 returns the Networth1 field if non-nil, zero value otherwise.

### GetNetworth1Ok

`func (o *HeroSynergyStats) GetNetworth1Ok() (*int64, bool)`

GetNetworth1Ok returns a tuple with the Networth1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetworth1

`func (o *HeroSynergyStats) SetNetworth1(v int64)`

SetNetworth1 sets Networth1 field to given value.


### GetNetworth2

`func (o *HeroSynergyStats) GetNetworth2() int64`

GetNetworth2 returns the Networth2 field if non-nil, zero value otherwise.

### GetNetworth2Ok

`func (o *HeroSynergyStats) GetNetworth2Ok() (*int64, bool)`

GetNetworth2Ok returns a tuple with the Networth2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetworth2

`func (o *HeroSynergyStats) SetNetworth2(v int64)`

SetNetworth2 sets Networth2 field to given value.


### GetObjDamage1

`func (o *HeroSynergyStats) GetObjDamage1() int64`

GetObjDamage1 returns the ObjDamage1 field if non-nil, zero value otherwise.

### GetObjDamage1Ok

`func (o *HeroSynergyStats) GetObjDamage1Ok() (*int64, bool)`

GetObjDamage1Ok returns a tuple with the ObjDamage1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjDamage1

`func (o *HeroSynergyStats) SetObjDamage1(v int64)`

SetObjDamage1 sets ObjDamage1 field to given value.


### GetObjDamage2

`func (o *HeroSynergyStats) GetObjDamage2() int64`

GetObjDamage2 returns the ObjDamage2 field if non-nil, zero value otherwise.

### GetObjDamage2Ok

`func (o *HeroSynergyStats) GetObjDamage2Ok() (*int64, bool)`

GetObjDamage2Ok returns a tuple with the ObjDamage2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjDamage2

`func (o *HeroSynergyStats) SetObjDamage2(v int64)`

SetObjDamage2 sets ObjDamage2 field to given value.


### GetWins

`func (o *HeroSynergyStats) GetWins() int64`

GetWins returns the Wins field if non-nil, zero value otherwise.

### GetWinsOk

`func (o *HeroSynergyStats) GetWinsOk() (*int64, bool)`

GetWinsOk returns a tuple with the Wins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWins

`func (o *HeroSynergyStats) SetWins(v int64)`

SetWins sets Wins field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


