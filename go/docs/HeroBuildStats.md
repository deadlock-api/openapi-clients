# HeroBuildStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AvgAverageBadge** | Pointer to **NullableFloat64** | Average badge (tier &#x3D; first digits, subtier &#x3D; last digit) of the matches with this build that have one; 0 without any. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional] 
**Bucket** | **int32** | The bucket value (depends on the bucket query parameter, 0 without one). | 
**HeroBuildId** | **int64** | The ID of the hero build. The &#x60;hero_build_id&#x60; is the first build the player had selected when the game started. | 
**HeroId** | **int32** | The ID of the hero. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**Losses** | **int64** | The number of losses with this build. | 
**Matches** | **int64** | The total number of matches played with this build (&#x60;wins + losses&#x60;). | 
**Players** | **int64** | The number of unique players who used this build. | 
**TotalAssists** | Pointer to **NullableInt64** |  | [optional] 
**TotalBossDamage** | Pointer to **NullableInt64** |  | [optional] 
**TotalCreepDamage** | Pointer to **NullableInt64** |  | [optional] 
**TotalCreepKills** | Pointer to **NullableInt64** |  | [optional] 
**TotalDamageMitigated** | Pointer to **NullableInt64** |  | [optional] 
**TotalDeaths** | Pointer to **NullableInt64** |  | [optional] 
**TotalDenies** | Pointer to **NullableInt64** |  | [optional] 
**TotalDurationS** | Pointer to **NullableInt64** | Sum of the match durations (seconds), for per-minute rates. | [optional] 
**TotalHeroBulletsHit** | Pointer to **NullableInt64** | Bullets that hit an enemy hero. | [optional] 
**TotalHeroBulletsHitCrit** | Pointer to **NullableInt64** | Hero hits that were crits (headshots). | [optional] 
**TotalKills** | Pointer to **NullableInt64** | Sum of the kills of every match with this build. Average per match: &#x60;total_kills / matches&#x60;. This and the other totals are only present with &#x60;include_performance&#x3D;true&#x60;. | [optional] 
**TotalLastHits** | Pointer to **NullableInt64** |  | [optional] 
**TotalLevel** | Pointer to **NullableInt64** | Sum of the final hero levels. | [optional] 
**TotalMaxHealth** | Pointer to **NullableInt64** |  | [optional] 
**TotalNetWorth** | Pointer to **NullableInt64** | Sum of the final net worth (souls). | [optional] 
**TotalNeutralDamage** | Pointer to **NullableInt64** |  | [optional] 
**TotalNeutralKills** | Pointer to **NullableInt64** |  | [optional] 
**TotalPlayerDamage** | Pointer to **NullableInt64** |  | [optional] 
**TotalPlayerDamageTaken** | Pointer to **NullableInt64** |  | [optional] 
**TotalPlayerHealing** | Pointer to **NullableInt64** |  | [optional] 
**TotalSelfHealing** | Pointer to **NullableInt64** |  | [optional] 
**TotalShotsHit** | Pointer to **NullableInt64** |  | [optional] 
**TotalShotsMissed** | Pointer to **NullableInt64** |  | [optional] 
**TotalTeammateHealing** | Pointer to **NullableInt64** |  | [optional] 
**Wins** | **int64** | The number of wins with this build. | 

## Methods

### NewHeroBuildStats

`func NewHeroBuildStats(bucket int32, heroBuildId int64, heroId int32, losses int64, matches int64, players int64, wins int64, ) *HeroBuildStats`

NewHeroBuildStats instantiates a new HeroBuildStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHeroBuildStatsWithDefaults

`func NewHeroBuildStatsWithDefaults() *HeroBuildStats`

NewHeroBuildStatsWithDefaults instantiates a new HeroBuildStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAvgAverageBadge

`func (o *HeroBuildStats) GetAvgAverageBadge() float64`

GetAvgAverageBadge returns the AvgAverageBadge field if non-nil, zero value otherwise.

### GetAvgAverageBadgeOk

`func (o *HeroBuildStats) GetAvgAverageBadgeOk() (*float64, bool)`

GetAvgAverageBadgeOk returns a tuple with the AvgAverageBadge field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgAverageBadge

`func (o *HeroBuildStats) SetAvgAverageBadge(v float64)`

SetAvgAverageBadge sets AvgAverageBadge field to given value.

### HasAvgAverageBadge

`func (o *HeroBuildStats) HasAvgAverageBadge() bool`

HasAvgAverageBadge returns a boolean if a field has been set.

### SetAvgAverageBadgeNil

`func (o *HeroBuildStats) SetAvgAverageBadgeNil(b bool)`

 SetAvgAverageBadgeNil sets the value for AvgAverageBadge to be an explicit nil

### UnsetAvgAverageBadge
`func (o *HeroBuildStats) UnsetAvgAverageBadge()`

UnsetAvgAverageBadge ensures that no value is present for AvgAverageBadge, not even an explicit nil
### GetBucket

`func (o *HeroBuildStats) GetBucket() int32`

GetBucket returns the Bucket field if non-nil, zero value otherwise.

### GetBucketOk

`func (o *HeroBuildStats) GetBucketOk() (*int32, bool)`

GetBucketOk returns a tuple with the Bucket field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBucket

`func (o *HeroBuildStats) SetBucket(v int32)`

SetBucket sets Bucket field to given value.


### GetHeroBuildId

`func (o *HeroBuildStats) GetHeroBuildId() int64`

GetHeroBuildId returns the HeroBuildId field if non-nil, zero value otherwise.

### GetHeroBuildIdOk

`func (o *HeroBuildStats) GetHeroBuildIdOk() (*int64, bool)`

GetHeroBuildIdOk returns a tuple with the HeroBuildId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroBuildId

`func (o *HeroBuildStats) SetHeroBuildId(v int64)`

SetHeroBuildId sets HeroBuildId field to given value.


### GetHeroId

`func (o *HeroBuildStats) GetHeroId() int32`

GetHeroId returns the HeroId field if non-nil, zero value otherwise.

### GetHeroIdOk

`func (o *HeroBuildStats) GetHeroIdOk() (*int32, bool)`

GetHeroIdOk returns a tuple with the HeroId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroId

`func (o *HeroBuildStats) SetHeroId(v int32)`

SetHeroId sets HeroId field to given value.


### GetLosses

`func (o *HeroBuildStats) GetLosses() int64`

GetLosses returns the Losses field if non-nil, zero value otherwise.

### GetLossesOk

`func (o *HeroBuildStats) GetLossesOk() (*int64, bool)`

GetLossesOk returns a tuple with the Losses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLosses

`func (o *HeroBuildStats) SetLosses(v int64)`

SetLosses sets Losses field to given value.


### GetMatches

`func (o *HeroBuildStats) GetMatches() int64`

GetMatches returns the Matches field if non-nil, zero value otherwise.

### GetMatchesOk

`func (o *HeroBuildStats) GetMatchesOk() (*int64, bool)`

GetMatchesOk returns a tuple with the Matches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatches

`func (o *HeroBuildStats) SetMatches(v int64)`

SetMatches sets Matches field to given value.


### GetPlayers

`func (o *HeroBuildStats) GetPlayers() int64`

GetPlayers returns the Players field if non-nil, zero value otherwise.

### GetPlayersOk

`func (o *HeroBuildStats) GetPlayersOk() (*int64, bool)`

GetPlayersOk returns a tuple with the Players field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayers

`func (o *HeroBuildStats) SetPlayers(v int64)`

SetPlayers sets Players field to given value.


### GetTotalAssists

`func (o *HeroBuildStats) GetTotalAssists() int64`

GetTotalAssists returns the TotalAssists field if non-nil, zero value otherwise.

### GetTotalAssistsOk

`func (o *HeroBuildStats) GetTotalAssistsOk() (*int64, bool)`

GetTotalAssistsOk returns a tuple with the TotalAssists field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalAssists

`func (o *HeroBuildStats) SetTotalAssists(v int64)`

SetTotalAssists sets TotalAssists field to given value.

### HasTotalAssists

`func (o *HeroBuildStats) HasTotalAssists() bool`

HasTotalAssists returns a boolean if a field has been set.

### SetTotalAssistsNil

`func (o *HeroBuildStats) SetTotalAssistsNil(b bool)`

 SetTotalAssistsNil sets the value for TotalAssists to be an explicit nil

### UnsetTotalAssists
`func (o *HeroBuildStats) UnsetTotalAssists()`

UnsetTotalAssists ensures that no value is present for TotalAssists, not even an explicit nil
### GetTotalBossDamage

`func (o *HeroBuildStats) GetTotalBossDamage() int64`

GetTotalBossDamage returns the TotalBossDamage field if non-nil, zero value otherwise.

### GetTotalBossDamageOk

`func (o *HeroBuildStats) GetTotalBossDamageOk() (*int64, bool)`

GetTotalBossDamageOk returns a tuple with the TotalBossDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalBossDamage

`func (o *HeroBuildStats) SetTotalBossDamage(v int64)`

SetTotalBossDamage sets TotalBossDamage field to given value.

### HasTotalBossDamage

`func (o *HeroBuildStats) HasTotalBossDamage() bool`

HasTotalBossDamage returns a boolean if a field has been set.

### SetTotalBossDamageNil

`func (o *HeroBuildStats) SetTotalBossDamageNil(b bool)`

 SetTotalBossDamageNil sets the value for TotalBossDamage to be an explicit nil

### UnsetTotalBossDamage
`func (o *HeroBuildStats) UnsetTotalBossDamage()`

UnsetTotalBossDamage ensures that no value is present for TotalBossDamage, not even an explicit nil
### GetTotalCreepDamage

`func (o *HeroBuildStats) GetTotalCreepDamage() int64`

GetTotalCreepDamage returns the TotalCreepDamage field if non-nil, zero value otherwise.

### GetTotalCreepDamageOk

`func (o *HeroBuildStats) GetTotalCreepDamageOk() (*int64, bool)`

GetTotalCreepDamageOk returns a tuple with the TotalCreepDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalCreepDamage

`func (o *HeroBuildStats) SetTotalCreepDamage(v int64)`

SetTotalCreepDamage sets TotalCreepDamage field to given value.

### HasTotalCreepDamage

`func (o *HeroBuildStats) HasTotalCreepDamage() bool`

HasTotalCreepDamage returns a boolean if a field has been set.

### SetTotalCreepDamageNil

`func (o *HeroBuildStats) SetTotalCreepDamageNil(b bool)`

 SetTotalCreepDamageNil sets the value for TotalCreepDamage to be an explicit nil

### UnsetTotalCreepDamage
`func (o *HeroBuildStats) UnsetTotalCreepDamage()`

UnsetTotalCreepDamage ensures that no value is present for TotalCreepDamage, not even an explicit nil
### GetTotalCreepKills

`func (o *HeroBuildStats) GetTotalCreepKills() int64`

GetTotalCreepKills returns the TotalCreepKills field if non-nil, zero value otherwise.

### GetTotalCreepKillsOk

`func (o *HeroBuildStats) GetTotalCreepKillsOk() (*int64, bool)`

GetTotalCreepKillsOk returns a tuple with the TotalCreepKills field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalCreepKills

`func (o *HeroBuildStats) SetTotalCreepKills(v int64)`

SetTotalCreepKills sets TotalCreepKills field to given value.

### HasTotalCreepKills

`func (o *HeroBuildStats) HasTotalCreepKills() bool`

HasTotalCreepKills returns a boolean if a field has been set.

### SetTotalCreepKillsNil

`func (o *HeroBuildStats) SetTotalCreepKillsNil(b bool)`

 SetTotalCreepKillsNil sets the value for TotalCreepKills to be an explicit nil

### UnsetTotalCreepKills
`func (o *HeroBuildStats) UnsetTotalCreepKills()`

UnsetTotalCreepKills ensures that no value is present for TotalCreepKills, not even an explicit nil
### GetTotalDamageMitigated

`func (o *HeroBuildStats) GetTotalDamageMitigated() int64`

GetTotalDamageMitigated returns the TotalDamageMitigated field if non-nil, zero value otherwise.

### GetTotalDamageMitigatedOk

`func (o *HeroBuildStats) GetTotalDamageMitigatedOk() (*int64, bool)`

GetTotalDamageMitigatedOk returns a tuple with the TotalDamageMitigated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalDamageMitigated

`func (o *HeroBuildStats) SetTotalDamageMitigated(v int64)`

SetTotalDamageMitigated sets TotalDamageMitigated field to given value.

### HasTotalDamageMitigated

`func (o *HeroBuildStats) HasTotalDamageMitigated() bool`

HasTotalDamageMitigated returns a boolean if a field has been set.

### SetTotalDamageMitigatedNil

`func (o *HeroBuildStats) SetTotalDamageMitigatedNil(b bool)`

 SetTotalDamageMitigatedNil sets the value for TotalDamageMitigated to be an explicit nil

### UnsetTotalDamageMitigated
`func (o *HeroBuildStats) UnsetTotalDamageMitigated()`

UnsetTotalDamageMitigated ensures that no value is present for TotalDamageMitigated, not even an explicit nil
### GetTotalDeaths

`func (o *HeroBuildStats) GetTotalDeaths() int64`

GetTotalDeaths returns the TotalDeaths field if non-nil, zero value otherwise.

### GetTotalDeathsOk

`func (o *HeroBuildStats) GetTotalDeathsOk() (*int64, bool)`

GetTotalDeathsOk returns a tuple with the TotalDeaths field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalDeaths

`func (o *HeroBuildStats) SetTotalDeaths(v int64)`

SetTotalDeaths sets TotalDeaths field to given value.

### HasTotalDeaths

`func (o *HeroBuildStats) HasTotalDeaths() bool`

HasTotalDeaths returns a boolean if a field has been set.

### SetTotalDeathsNil

`func (o *HeroBuildStats) SetTotalDeathsNil(b bool)`

 SetTotalDeathsNil sets the value for TotalDeaths to be an explicit nil

### UnsetTotalDeaths
`func (o *HeroBuildStats) UnsetTotalDeaths()`

UnsetTotalDeaths ensures that no value is present for TotalDeaths, not even an explicit nil
### GetTotalDenies

`func (o *HeroBuildStats) GetTotalDenies() int64`

GetTotalDenies returns the TotalDenies field if non-nil, zero value otherwise.

### GetTotalDeniesOk

`func (o *HeroBuildStats) GetTotalDeniesOk() (*int64, bool)`

GetTotalDeniesOk returns a tuple with the TotalDenies field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalDenies

`func (o *HeroBuildStats) SetTotalDenies(v int64)`

SetTotalDenies sets TotalDenies field to given value.

### HasTotalDenies

`func (o *HeroBuildStats) HasTotalDenies() bool`

HasTotalDenies returns a boolean if a field has been set.

### SetTotalDeniesNil

`func (o *HeroBuildStats) SetTotalDeniesNil(b bool)`

 SetTotalDeniesNil sets the value for TotalDenies to be an explicit nil

### UnsetTotalDenies
`func (o *HeroBuildStats) UnsetTotalDenies()`

UnsetTotalDenies ensures that no value is present for TotalDenies, not even an explicit nil
### GetTotalDurationS

`func (o *HeroBuildStats) GetTotalDurationS() int64`

GetTotalDurationS returns the TotalDurationS field if non-nil, zero value otherwise.

### GetTotalDurationSOk

`func (o *HeroBuildStats) GetTotalDurationSOk() (*int64, bool)`

GetTotalDurationSOk returns a tuple with the TotalDurationS field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalDurationS

`func (o *HeroBuildStats) SetTotalDurationS(v int64)`

SetTotalDurationS sets TotalDurationS field to given value.

### HasTotalDurationS

`func (o *HeroBuildStats) HasTotalDurationS() bool`

HasTotalDurationS returns a boolean if a field has been set.

### SetTotalDurationSNil

`func (o *HeroBuildStats) SetTotalDurationSNil(b bool)`

 SetTotalDurationSNil sets the value for TotalDurationS to be an explicit nil

### UnsetTotalDurationS
`func (o *HeroBuildStats) UnsetTotalDurationS()`

UnsetTotalDurationS ensures that no value is present for TotalDurationS, not even an explicit nil
### GetTotalHeroBulletsHit

`func (o *HeroBuildStats) GetTotalHeroBulletsHit() int64`

GetTotalHeroBulletsHit returns the TotalHeroBulletsHit field if non-nil, zero value otherwise.

### GetTotalHeroBulletsHitOk

`func (o *HeroBuildStats) GetTotalHeroBulletsHitOk() (*int64, bool)`

GetTotalHeroBulletsHitOk returns a tuple with the TotalHeroBulletsHit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalHeroBulletsHit

`func (o *HeroBuildStats) SetTotalHeroBulletsHit(v int64)`

SetTotalHeroBulletsHit sets TotalHeroBulletsHit field to given value.

### HasTotalHeroBulletsHit

`func (o *HeroBuildStats) HasTotalHeroBulletsHit() bool`

HasTotalHeroBulletsHit returns a boolean if a field has been set.

### SetTotalHeroBulletsHitNil

`func (o *HeroBuildStats) SetTotalHeroBulletsHitNil(b bool)`

 SetTotalHeroBulletsHitNil sets the value for TotalHeroBulletsHit to be an explicit nil

### UnsetTotalHeroBulletsHit
`func (o *HeroBuildStats) UnsetTotalHeroBulletsHit()`

UnsetTotalHeroBulletsHit ensures that no value is present for TotalHeroBulletsHit, not even an explicit nil
### GetTotalHeroBulletsHitCrit

`func (o *HeroBuildStats) GetTotalHeroBulletsHitCrit() int64`

GetTotalHeroBulletsHitCrit returns the TotalHeroBulletsHitCrit field if non-nil, zero value otherwise.

### GetTotalHeroBulletsHitCritOk

`func (o *HeroBuildStats) GetTotalHeroBulletsHitCritOk() (*int64, bool)`

GetTotalHeroBulletsHitCritOk returns a tuple with the TotalHeroBulletsHitCrit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalHeroBulletsHitCrit

`func (o *HeroBuildStats) SetTotalHeroBulletsHitCrit(v int64)`

SetTotalHeroBulletsHitCrit sets TotalHeroBulletsHitCrit field to given value.

### HasTotalHeroBulletsHitCrit

`func (o *HeroBuildStats) HasTotalHeroBulletsHitCrit() bool`

HasTotalHeroBulletsHitCrit returns a boolean if a field has been set.

### SetTotalHeroBulletsHitCritNil

`func (o *HeroBuildStats) SetTotalHeroBulletsHitCritNil(b bool)`

 SetTotalHeroBulletsHitCritNil sets the value for TotalHeroBulletsHitCrit to be an explicit nil

### UnsetTotalHeroBulletsHitCrit
`func (o *HeroBuildStats) UnsetTotalHeroBulletsHitCrit()`

UnsetTotalHeroBulletsHitCrit ensures that no value is present for TotalHeroBulletsHitCrit, not even an explicit nil
### GetTotalKills

`func (o *HeroBuildStats) GetTotalKills() int64`

GetTotalKills returns the TotalKills field if non-nil, zero value otherwise.

### GetTotalKillsOk

`func (o *HeroBuildStats) GetTotalKillsOk() (*int64, bool)`

GetTotalKillsOk returns a tuple with the TotalKills field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalKills

`func (o *HeroBuildStats) SetTotalKills(v int64)`

SetTotalKills sets TotalKills field to given value.

### HasTotalKills

`func (o *HeroBuildStats) HasTotalKills() bool`

HasTotalKills returns a boolean if a field has been set.

### SetTotalKillsNil

`func (o *HeroBuildStats) SetTotalKillsNil(b bool)`

 SetTotalKillsNil sets the value for TotalKills to be an explicit nil

### UnsetTotalKills
`func (o *HeroBuildStats) UnsetTotalKills()`

UnsetTotalKills ensures that no value is present for TotalKills, not even an explicit nil
### GetTotalLastHits

`func (o *HeroBuildStats) GetTotalLastHits() int64`

GetTotalLastHits returns the TotalLastHits field if non-nil, zero value otherwise.

### GetTotalLastHitsOk

`func (o *HeroBuildStats) GetTotalLastHitsOk() (*int64, bool)`

GetTotalLastHitsOk returns a tuple with the TotalLastHits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalLastHits

`func (o *HeroBuildStats) SetTotalLastHits(v int64)`

SetTotalLastHits sets TotalLastHits field to given value.

### HasTotalLastHits

`func (o *HeroBuildStats) HasTotalLastHits() bool`

HasTotalLastHits returns a boolean if a field has been set.

### SetTotalLastHitsNil

`func (o *HeroBuildStats) SetTotalLastHitsNil(b bool)`

 SetTotalLastHitsNil sets the value for TotalLastHits to be an explicit nil

### UnsetTotalLastHits
`func (o *HeroBuildStats) UnsetTotalLastHits()`

UnsetTotalLastHits ensures that no value is present for TotalLastHits, not even an explicit nil
### GetTotalLevel

`func (o *HeroBuildStats) GetTotalLevel() int64`

GetTotalLevel returns the TotalLevel field if non-nil, zero value otherwise.

### GetTotalLevelOk

`func (o *HeroBuildStats) GetTotalLevelOk() (*int64, bool)`

GetTotalLevelOk returns a tuple with the TotalLevel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalLevel

`func (o *HeroBuildStats) SetTotalLevel(v int64)`

SetTotalLevel sets TotalLevel field to given value.

### HasTotalLevel

`func (o *HeroBuildStats) HasTotalLevel() bool`

HasTotalLevel returns a boolean if a field has been set.

### SetTotalLevelNil

`func (o *HeroBuildStats) SetTotalLevelNil(b bool)`

 SetTotalLevelNil sets the value for TotalLevel to be an explicit nil

### UnsetTotalLevel
`func (o *HeroBuildStats) UnsetTotalLevel()`

UnsetTotalLevel ensures that no value is present for TotalLevel, not even an explicit nil
### GetTotalMaxHealth

`func (o *HeroBuildStats) GetTotalMaxHealth() int64`

GetTotalMaxHealth returns the TotalMaxHealth field if non-nil, zero value otherwise.

### GetTotalMaxHealthOk

`func (o *HeroBuildStats) GetTotalMaxHealthOk() (*int64, bool)`

GetTotalMaxHealthOk returns a tuple with the TotalMaxHealth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalMaxHealth

`func (o *HeroBuildStats) SetTotalMaxHealth(v int64)`

SetTotalMaxHealth sets TotalMaxHealth field to given value.

### HasTotalMaxHealth

`func (o *HeroBuildStats) HasTotalMaxHealth() bool`

HasTotalMaxHealth returns a boolean if a field has been set.

### SetTotalMaxHealthNil

`func (o *HeroBuildStats) SetTotalMaxHealthNil(b bool)`

 SetTotalMaxHealthNil sets the value for TotalMaxHealth to be an explicit nil

### UnsetTotalMaxHealth
`func (o *HeroBuildStats) UnsetTotalMaxHealth()`

UnsetTotalMaxHealth ensures that no value is present for TotalMaxHealth, not even an explicit nil
### GetTotalNetWorth

`func (o *HeroBuildStats) GetTotalNetWorth() int64`

GetTotalNetWorth returns the TotalNetWorth field if non-nil, zero value otherwise.

### GetTotalNetWorthOk

`func (o *HeroBuildStats) GetTotalNetWorthOk() (*int64, bool)`

GetTotalNetWorthOk returns a tuple with the TotalNetWorth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalNetWorth

`func (o *HeroBuildStats) SetTotalNetWorth(v int64)`

SetTotalNetWorth sets TotalNetWorth field to given value.

### HasTotalNetWorth

`func (o *HeroBuildStats) HasTotalNetWorth() bool`

HasTotalNetWorth returns a boolean if a field has been set.

### SetTotalNetWorthNil

`func (o *HeroBuildStats) SetTotalNetWorthNil(b bool)`

 SetTotalNetWorthNil sets the value for TotalNetWorth to be an explicit nil

### UnsetTotalNetWorth
`func (o *HeroBuildStats) UnsetTotalNetWorth()`

UnsetTotalNetWorth ensures that no value is present for TotalNetWorth, not even an explicit nil
### GetTotalNeutralDamage

`func (o *HeroBuildStats) GetTotalNeutralDamage() int64`

GetTotalNeutralDamage returns the TotalNeutralDamage field if non-nil, zero value otherwise.

### GetTotalNeutralDamageOk

`func (o *HeroBuildStats) GetTotalNeutralDamageOk() (*int64, bool)`

GetTotalNeutralDamageOk returns a tuple with the TotalNeutralDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalNeutralDamage

`func (o *HeroBuildStats) SetTotalNeutralDamage(v int64)`

SetTotalNeutralDamage sets TotalNeutralDamage field to given value.

### HasTotalNeutralDamage

`func (o *HeroBuildStats) HasTotalNeutralDamage() bool`

HasTotalNeutralDamage returns a boolean if a field has been set.

### SetTotalNeutralDamageNil

`func (o *HeroBuildStats) SetTotalNeutralDamageNil(b bool)`

 SetTotalNeutralDamageNil sets the value for TotalNeutralDamage to be an explicit nil

### UnsetTotalNeutralDamage
`func (o *HeroBuildStats) UnsetTotalNeutralDamage()`

UnsetTotalNeutralDamage ensures that no value is present for TotalNeutralDamage, not even an explicit nil
### GetTotalNeutralKills

`func (o *HeroBuildStats) GetTotalNeutralKills() int64`

GetTotalNeutralKills returns the TotalNeutralKills field if non-nil, zero value otherwise.

### GetTotalNeutralKillsOk

`func (o *HeroBuildStats) GetTotalNeutralKillsOk() (*int64, bool)`

GetTotalNeutralKillsOk returns a tuple with the TotalNeutralKills field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalNeutralKills

`func (o *HeroBuildStats) SetTotalNeutralKills(v int64)`

SetTotalNeutralKills sets TotalNeutralKills field to given value.

### HasTotalNeutralKills

`func (o *HeroBuildStats) HasTotalNeutralKills() bool`

HasTotalNeutralKills returns a boolean if a field has been set.

### SetTotalNeutralKillsNil

`func (o *HeroBuildStats) SetTotalNeutralKillsNil(b bool)`

 SetTotalNeutralKillsNil sets the value for TotalNeutralKills to be an explicit nil

### UnsetTotalNeutralKills
`func (o *HeroBuildStats) UnsetTotalNeutralKills()`

UnsetTotalNeutralKills ensures that no value is present for TotalNeutralKills, not even an explicit nil
### GetTotalPlayerDamage

`func (o *HeroBuildStats) GetTotalPlayerDamage() int64`

GetTotalPlayerDamage returns the TotalPlayerDamage field if non-nil, zero value otherwise.

### GetTotalPlayerDamageOk

`func (o *HeroBuildStats) GetTotalPlayerDamageOk() (*int64, bool)`

GetTotalPlayerDamageOk returns a tuple with the TotalPlayerDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalPlayerDamage

`func (o *HeroBuildStats) SetTotalPlayerDamage(v int64)`

SetTotalPlayerDamage sets TotalPlayerDamage field to given value.

### HasTotalPlayerDamage

`func (o *HeroBuildStats) HasTotalPlayerDamage() bool`

HasTotalPlayerDamage returns a boolean if a field has been set.

### SetTotalPlayerDamageNil

`func (o *HeroBuildStats) SetTotalPlayerDamageNil(b bool)`

 SetTotalPlayerDamageNil sets the value for TotalPlayerDamage to be an explicit nil

### UnsetTotalPlayerDamage
`func (o *HeroBuildStats) UnsetTotalPlayerDamage()`

UnsetTotalPlayerDamage ensures that no value is present for TotalPlayerDamage, not even an explicit nil
### GetTotalPlayerDamageTaken

`func (o *HeroBuildStats) GetTotalPlayerDamageTaken() int64`

GetTotalPlayerDamageTaken returns the TotalPlayerDamageTaken field if non-nil, zero value otherwise.

### GetTotalPlayerDamageTakenOk

`func (o *HeroBuildStats) GetTotalPlayerDamageTakenOk() (*int64, bool)`

GetTotalPlayerDamageTakenOk returns a tuple with the TotalPlayerDamageTaken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalPlayerDamageTaken

`func (o *HeroBuildStats) SetTotalPlayerDamageTaken(v int64)`

SetTotalPlayerDamageTaken sets TotalPlayerDamageTaken field to given value.

### HasTotalPlayerDamageTaken

`func (o *HeroBuildStats) HasTotalPlayerDamageTaken() bool`

HasTotalPlayerDamageTaken returns a boolean if a field has been set.

### SetTotalPlayerDamageTakenNil

`func (o *HeroBuildStats) SetTotalPlayerDamageTakenNil(b bool)`

 SetTotalPlayerDamageTakenNil sets the value for TotalPlayerDamageTaken to be an explicit nil

### UnsetTotalPlayerDamageTaken
`func (o *HeroBuildStats) UnsetTotalPlayerDamageTaken()`

UnsetTotalPlayerDamageTaken ensures that no value is present for TotalPlayerDamageTaken, not even an explicit nil
### GetTotalPlayerHealing

`func (o *HeroBuildStats) GetTotalPlayerHealing() int64`

GetTotalPlayerHealing returns the TotalPlayerHealing field if non-nil, zero value otherwise.

### GetTotalPlayerHealingOk

`func (o *HeroBuildStats) GetTotalPlayerHealingOk() (*int64, bool)`

GetTotalPlayerHealingOk returns a tuple with the TotalPlayerHealing field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalPlayerHealing

`func (o *HeroBuildStats) SetTotalPlayerHealing(v int64)`

SetTotalPlayerHealing sets TotalPlayerHealing field to given value.

### HasTotalPlayerHealing

`func (o *HeroBuildStats) HasTotalPlayerHealing() bool`

HasTotalPlayerHealing returns a boolean if a field has been set.

### SetTotalPlayerHealingNil

`func (o *HeroBuildStats) SetTotalPlayerHealingNil(b bool)`

 SetTotalPlayerHealingNil sets the value for TotalPlayerHealing to be an explicit nil

### UnsetTotalPlayerHealing
`func (o *HeroBuildStats) UnsetTotalPlayerHealing()`

UnsetTotalPlayerHealing ensures that no value is present for TotalPlayerHealing, not even an explicit nil
### GetTotalSelfHealing

`func (o *HeroBuildStats) GetTotalSelfHealing() int64`

GetTotalSelfHealing returns the TotalSelfHealing field if non-nil, zero value otherwise.

### GetTotalSelfHealingOk

`func (o *HeroBuildStats) GetTotalSelfHealingOk() (*int64, bool)`

GetTotalSelfHealingOk returns a tuple with the TotalSelfHealing field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalSelfHealing

`func (o *HeroBuildStats) SetTotalSelfHealing(v int64)`

SetTotalSelfHealing sets TotalSelfHealing field to given value.

### HasTotalSelfHealing

`func (o *HeroBuildStats) HasTotalSelfHealing() bool`

HasTotalSelfHealing returns a boolean if a field has been set.

### SetTotalSelfHealingNil

`func (o *HeroBuildStats) SetTotalSelfHealingNil(b bool)`

 SetTotalSelfHealingNil sets the value for TotalSelfHealing to be an explicit nil

### UnsetTotalSelfHealing
`func (o *HeroBuildStats) UnsetTotalSelfHealing()`

UnsetTotalSelfHealing ensures that no value is present for TotalSelfHealing, not even an explicit nil
### GetTotalShotsHit

`func (o *HeroBuildStats) GetTotalShotsHit() int64`

GetTotalShotsHit returns the TotalShotsHit field if non-nil, zero value otherwise.

### GetTotalShotsHitOk

`func (o *HeroBuildStats) GetTotalShotsHitOk() (*int64, bool)`

GetTotalShotsHitOk returns a tuple with the TotalShotsHit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalShotsHit

`func (o *HeroBuildStats) SetTotalShotsHit(v int64)`

SetTotalShotsHit sets TotalShotsHit field to given value.

### HasTotalShotsHit

`func (o *HeroBuildStats) HasTotalShotsHit() bool`

HasTotalShotsHit returns a boolean if a field has been set.

### SetTotalShotsHitNil

`func (o *HeroBuildStats) SetTotalShotsHitNil(b bool)`

 SetTotalShotsHitNil sets the value for TotalShotsHit to be an explicit nil

### UnsetTotalShotsHit
`func (o *HeroBuildStats) UnsetTotalShotsHit()`

UnsetTotalShotsHit ensures that no value is present for TotalShotsHit, not even an explicit nil
### GetTotalShotsMissed

`func (o *HeroBuildStats) GetTotalShotsMissed() int64`

GetTotalShotsMissed returns the TotalShotsMissed field if non-nil, zero value otherwise.

### GetTotalShotsMissedOk

`func (o *HeroBuildStats) GetTotalShotsMissedOk() (*int64, bool)`

GetTotalShotsMissedOk returns a tuple with the TotalShotsMissed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalShotsMissed

`func (o *HeroBuildStats) SetTotalShotsMissed(v int64)`

SetTotalShotsMissed sets TotalShotsMissed field to given value.

### HasTotalShotsMissed

`func (o *HeroBuildStats) HasTotalShotsMissed() bool`

HasTotalShotsMissed returns a boolean if a field has been set.

### SetTotalShotsMissedNil

`func (o *HeroBuildStats) SetTotalShotsMissedNil(b bool)`

 SetTotalShotsMissedNil sets the value for TotalShotsMissed to be an explicit nil

### UnsetTotalShotsMissed
`func (o *HeroBuildStats) UnsetTotalShotsMissed()`

UnsetTotalShotsMissed ensures that no value is present for TotalShotsMissed, not even an explicit nil
### GetTotalTeammateHealing

`func (o *HeroBuildStats) GetTotalTeammateHealing() int64`

GetTotalTeammateHealing returns the TotalTeammateHealing field if non-nil, zero value otherwise.

### GetTotalTeammateHealingOk

`func (o *HeroBuildStats) GetTotalTeammateHealingOk() (*int64, bool)`

GetTotalTeammateHealingOk returns a tuple with the TotalTeammateHealing field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalTeammateHealing

`func (o *HeroBuildStats) SetTotalTeammateHealing(v int64)`

SetTotalTeammateHealing sets TotalTeammateHealing field to given value.

### HasTotalTeammateHealing

`func (o *HeroBuildStats) HasTotalTeammateHealing() bool`

HasTotalTeammateHealing returns a boolean if a field has been set.

### SetTotalTeammateHealingNil

`func (o *HeroBuildStats) SetTotalTeammateHealingNil(b bool)`

 SetTotalTeammateHealingNil sets the value for TotalTeammateHealing to be an explicit nil

### UnsetTotalTeammateHealing
`func (o *HeroBuildStats) UnsetTotalTeammateHealing()`

UnsetTotalTeammateHealing ensures that no value is present for TotalTeammateHealing, not even an explicit nil
### GetWins

`func (o *HeroBuildStats) GetWins() int64`

GetWins returns the Wins field if non-nil, zero value otherwise.

### GetWinsOk

`func (o *HeroBuildStats) GetWinsOk() (*int64, bool)`

GetWinsOk returns a tuple with the Wins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWins

`func (o *HeroBuildStats) SetWins(v int64)`

SetWins sets Wins field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


