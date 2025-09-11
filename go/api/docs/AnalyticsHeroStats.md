# AnalyticsHeroStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Bucket** | Pointer to **NullableInt32** |  | [optional] 
**HeroId** | **int32** | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**Losses** | **int64** |  | 
**Matches** | **int64** |  | 
**MatchesPerBucket** | **int64** |  | 
**Players** | **int64** |  | 
**TotalAssists** | **int64** |  | 
**TotalBossDamage** | **int64** |  | 
**TotalCreepDamage** | **int64** |  | 
**TotalDeaths** | **int64** |  | 
**TotalDenies** | **int64** |  | 
**TotalKills** | **int64** |  | 
**TotalLastHits** | **int64** |  | 
**TotalMaxHealth** | **int64** |  | 
**TotalNetWorth** | **int64** |  | 
**TotalNeutralDamage** | **int64** |  | 
**TotalPlayerDamage** | **int64** |  | 
**TotalPlayerDamageTaken** | **int64** |  | 
**TotalShotsHit** | **int64** |  | 
**TotalShotsMissed** | **int64** |  | 
**Wins** | **int64** |  | 

## Methods

### NewAnalyticsHeroStats

`func NewAnalyticsHeroStats(heroId int32, losses int64, matches int64, matchesPerBucket int64, players int64, totalAssists int64, totalBossDamage int64, totalCreepDamage int64, totalDeaths int64, totalDenies int64, totalKills int64, totalLastHits int64, totalMaxHealth int64, totalNetWorth int64, totalNeutralDamage int64, totalPlayerDamage int64, totalPlayerDamageTaken int64, totalShotsHit int64, totalShotsMissed int64, wins int64, ) *AnalyticsHeroStats`

NewAnalyticsHeroStats instantiates a new AnalyticsHeroStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAnalyticsHeroStatsWithDefaults

`func NewAnalyticsHeroStatsWithDefaults() *AnalyticsHeroStats`

NewAnalyticsHeroStatsWithDefaults instantiates a new AnalyticsHeroStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBucket

`func (o *AnalyticsHeroStats) GetBucket() int32`

GetBucket returns the Bucket field if non-nil, zero value otherwise.

### GetBucketOk

`func (o *AnalyticsHeroStats) GetBucketOk() (*int32, bool)`

GetBucketOk returns a tuple with the Bucket field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBucket

`func (o *AnalyticsHeroStats) SetBucket(v int32)`

SetBucket sets Bucket field to given value.

### HasBucket

`func (o *AnalyticsHeroStats) HasBucket() bool`

HasBucket returns a boolean if a field has been set.

### SetBucketNil

`func (o *AnalyticsHeroStats) SetBucketNil(b bool)`

 SetBucketNil sets the value for Bucket to be an explicit nil

### UnsetBucket
`func (o *AnalyticsHeroStats) UnsetBucket()`

UnsetBucket ensures that no value is present for Bucket, not even an explicit nil
### GetHeroId

`func (o *AnalyticsHeroStats) GetHeroId() int32`

GetHeroId returns the HeroId field if non-nil, zero value otherwise.

### GetHeroIdOk

`func (o *AnalyticsHeroStats) GetHeroIdOk() (*int32, bool)`

GetHeroIdOk returns a tuple with the HeroId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroId

`func (o *AnalyticsHeroStats) SetHeroId(v int32)`

SetHeroId sets HeroId field to given value.


### GetLosses

`func (o *AnalyticsHeroStats) GetLosses() int64`

GetLosses returns the Losses field if non-nil, zero value otherwise.

### GetLossesOk

`func (o *AnalyticsHeroStats) GetLossesOk() (*int64, bool)`

GetLossesOk returns a tuple with the Losses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLosses

`func (o *AnalyticsHeroStats) SetLosses(v int64)`

SetLosses sets Losses field to given value.


### GetMatches

`func (o *AnalyticsHeroStats) GetMatches() int64`

GetMatches returns the Matches field if non-nil, zero value otherwise.

### GetMatchesOk

`func (o *AnalyticsHeroStats) GetMatchesOk() (*int64, bool)`

GetMatchesOk returns a tuple with the Matches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatches

`func (o *AnalyticsHeroStats) SetMatches(v int64)`

SetMatches sets Matches field to given value.


### GetMatchesPerBucket

`func (o *AnalyticsHeroStats) GetMatchesPerBucket() int64`

GetMatchesPerBucket returns the MatchesPerBucket field if non-nil, zero value otherwise.

### GetMatchesPerBucketOk

`func (o *AnalyticsHeroStats) GetMatchesPerBucketOk() (*int64, bool)`

GetMatchesPerBucketOk returns a tuple with the MatchesPerBucket field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchesPerBucket

`func (o *AnalyticsHeroStats) SetMatchesPerBucket(v int64)`

SetMatchesPerBucket sets MatchesPerBucket field to given value.


### GetPlayers

`func (o *AnalyticsHeroStats) GetPlayers() int64`

GetPlayers returns the Players field if non-nil, zero value otherwise.

### GetPlayersOk

`func (o *AnalyticsHeroStats) GetPlayersOk() (*int64, bool)`

GetPlayersOk returns a tuple with the Players field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayers

`func (o *AnalyticsHeroStats) SetPlayers(v int64)`

SetPlayers sets Players field to given value.


### GetTotalAssists

`func (o *AnalyticsHeroStats) GetTotalAssists() int64`

GetTotalAssists returns the TotalAssists field if non-nil, zero value otherwise.

### GetTotalAssistsOk

`func (o *AnalyticsHeroStats) GetTotalAssistsOk() (*int64, bool)`

GetTotalAssistsOk returns a tuple with the TotalAssists field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalAssists

`func (o *AnalyticsHeroStats) SetTotalAssists(v int64)`

SetTotalAssists sets TotalAssists field to given value.


### GetTotalBossDamage

`func (o *AnalyticsHeroStats) GetTotalBossDamage() int64`

GetTotalBossDamage returns the TotalBossDamage field if non-nil, zero value otherwise.

### GetTotalBossDamageOk

`func (o *AnalyticsHeroStats) GetTotalBossDamageOk() (*int64, bool)`

GetTotalBossDamageOk returns a tuple with the TotalBossDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalBossDamage

`func (o *AnalyticsHeroStats) SetTotalBossDamage(v int64)`

SetTotalBossDamage sets TotalBossDamage field to given value.


### GetTotalCreepDamage

`func (o *AnalyticsHeroStats) GetTotalCreepDamage() int64`

GetTotalCreepDamage returns the TotalCreepDamage field if non-nil, zero value otherwise.

### GetTotalCreepDamageOk

`func (o *AnalyticsHeroStats) GetTotalCreepDamageOk() (*int64, bool)`

GetTotalCreepDamageOk returns a tuple with the TotalCreepDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalCreepDamage

`func (o *AnalyticsHeroStats) SetTotalCreepDamage(v int64)`

SetTotalCreepDamage sets TotalCreepDamage field to given value.


### GetTotalDeaths

`func (o *AnalyticsHeroStats) GetTotalDeaths() int64`

GetTotalDeaths returns the TotalDeaths field if non-nil, zero value otherwise.

### GetTotalDeathsOk

`func (o *AnalyticsHeroStats) GetTotalDeathsOk() (*int64, bool)`

GetTotalDeathsOk returns a tuple with the TotalDeaths field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalDeaths

`func (o *AnalyticsHeroStats) SetTotalDeaths(v int64)`

SetTotalDeaths sets TotalDeaths field to given value.


### GetTotalDenies

`func (o *AnalyticsHeroStats) GetTotalDenies() int64`

GetTotalDenies returns the TotalDenies field if non-nil, zero value otherwise.

### GetTotalDeniesOk

`func (o *AnalyticsHeroStats) GetTotalDeniesOk() (*int64, bool)`

GetTotalDeniesOk returns a tuple with the TotalDenies field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalDenies

`func (o *AnalyticsHeroStats) SetTotalDenies(v int64)`

SetTotalDenies sets TotalDenies field to given value.


### GetTotalKills

`func (o *AnalyticsHeroStats) GetTotalKills() int64`

GetTotalKills returns the TotalKills field if non-nil, zero value otherwise.

### GetTotalKillsOk

`func (o *AnalyticsHeroStats) GetTotalKillsOk() (*int64, bool)`

GetTotalKillsOk returns a tuple with the TotalKills field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalKills

`func (o *AnalyticsHeroStats) SetTotalKills(v int64)`

SetTotalKills sets TotalKills field to given value.


### GetTotalLastHits

`func (o *AnalyticsHeroStats) GetTotalLastHits() int64`

GetTotalLastHits returns the TotalLastHits field if non-nil, zero value otherwise.

### GetTotalLastHitsOk

`func (o *AnalyticsHeroStats) GetTotalLastHitsOk() (*int64, bool)`

GetTotalLastHitsOk returns a tuple with the TotalLastHits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalLastHits

`func (o *AnalyticsHeroStats) SetTotalLastHits(v int64)`

SetTotalLastHits sets TotalLastHits field to given value.


### GetTotalMaxHealth

`func (o *AnalyticsHeroStats) GetTotalMaxHealth() int64`

GetTotalMaxHealth returns the TotalMaxHealth field if non-nil, zero value otherwise.

### GetTotalMaxHealthOk

`func (o *AnalyticsHeroStats) GetTotalMaxHealthOk() (*int64, bool)`

GetTotalMaxHealthOk returns a tuple with the TotalMaxHealth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalMaxHealth

`func (o *AnalyticsHeroStats) SetTotalMaxHealth(v int64)`

SetTotalMaxHealth sets TotalMaxHealth field to given value.


### GetTotalNetWorth

`func (o *AnalyticsHeroStats) GetTotalNetWorth() int64`

GetTotalNetWorth returns the TotalNetWorth field if non-nil, zero value otherwise.

### GetTotalNetWorthOk

`func (o *AnalyticsHeroStats) GetTotalNetWorthOk() (*int64, bool)`

GetTotalNetWorthOk returns a tuple with the TotalNetWorth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalNetWorth

`func (o *AnalyticsHeroStats) SetTotalNetWorth(v int64)`

SetTotalNetWorth sets TotalNetWorth field to given value.


### GetTotalNeutralDamage

`func (o *AnalyticsHeroStats) GetTotalNeutralDamage() int64`

GetTotalNeutralDamage returns the TotalNeutralDamage field if non-nil, zero value otherwise.

### GetTotalNeutralDamageOk

`func (o *AnalyticsHeroStats) GetTotalNeutralDamageOk() (*int64, bool)`

GetTotalNeutralDamageOk returns a tuple with the TotalNeutralDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalNeutralDamage

`func (o *AnalyticsHeroStats) SetTotalNeutralDamage(v int64)`

SetTotalNeutralDamage sets TotalNeutralDamage field to given value.


### GetTotalPlayerDamage

`func (o *AnalyticsHeroStats) GetTotalPlayerDamage() int64`

GetTotalPlayerDamage returns the TotalPlayerDamage field if non-nil, zero value otherwise.

### GetTotalPlayerDamageOk

`func (o *AnalyticsHeroStats) GetTotalPlayerDamageOk() (*int64, bool)`

GetTotalPlayerDamageOk returns a tuple with the TotalPlayerDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalPlayerDamage

`func (o *AnalyticsHeroStats) SetTotalPlayerDamage(v int64)`

SetTotalPlayerDamage sets TotalPlayerDamage field to given value.


### GetTotalPlayerDamageTaken

`func (o *AnalyticsHeroStats) GetTotalPlayerDamageTaken() int64`

GetTotalPlayerDamageTaken returns the TotalPlayerDamageTaken field if non-nil, zero value otherwise.

### GetTotalPlayerDamageTakenOk

`func (o *AnalyticsHeroStats) GetTotalPlayerDamageTakenOk() (*int64, bool)`

GetTotalPlayerDamageTakenOk returns a tuple with the TotalPlayerDamageTaken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalPlayerDamageTaken

`func (o *AnalyticsHeroStats) SetTotalPlayerDamageTaken(v int64)`

SetTotalPlayerDamageTaken sets TotalPlayerDamageTaken field to given value.


### GetTotalShotsHit

`func (o *AnalyticsHeroStats) GetTotalShotsHit() int64`

GetTotalShotsHit returns the TotalShotsHit field if non-nil, zero value otherwise.

### GetTotalShotsHitOk

`func (o *AnalyticsHeroStats) GetTotalShotsHitOk() (*int64, bool)`

GetTotalShotsHitOk returns a tuple with the TotalShotsHit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalShotsHit

`func (o *AnalyticsHeroStats) SetTotalShotsHit(v int64)`

SetTotalShotsHit sets TotalShotsHit field to given value.


### GetTotalShotsMissed

`func (o *AnalyticsHeroStats) GetTotalShotsMissed() int64`

GetTotalShotsMissed returns the TotalShotsMissed field if non-nil, zero value otherwise.

### GetTotalShotsMissedOk

`func (o *AnalyticsHeroStats) GetTotalShotsMissedOk() (*int64, bool)`

GetTotalShotsMissedOk returns a tuple with the TotalShotsMissed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalShotsMissed

`func (o *AnalyticsHeroStats) SetTotalShotsMissed(v int64)`

SetTotalShotsMissed sets TotalShotsMissed field to given value.


### GetWins

`func (o *AnalyticsHeroStats) GetWins() int64`

GetWins returns the Wins field if non-nil, zero value otherwise.

### GetWinsOk

`func (o *AnalyticsHeroStats) GetWinsOk() (*int64, bool)`

GetWinsOk returns a tuple with the Wins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWins

`func (o *AnalyticsHeroStats) SetWins(v int64)`

SetWins sets Wins field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


