# HeroBuildStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**HeroBuildId** | **int64** | The ID of the hero build. The &#x60;hero_build_id&#x60; is the first build the player had selected when the game started. | 
**HeroId** | **int32** | The ID of the hero. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**Losses** | **int64** | The number of losses with this build. | 
**Matches** | **int64** | The total number of matches played with this build (&#x60;wins + losses&#x60;). | 
**Players** | **int64** | The number of unique players who used this build. | 
**Wins** | **int64** | The number of wins with this build. | 

## Methods

### NewHeroBuildStats

`func NewHeroBuildStats(heroBuildId int64, heroId int32, losses int64, matches int64, players int64, wins int64, ) *HeroBuildStats`

NewHeroBuildStats instantiates a new HeroBuildStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHeroBuildStatsWithDefaults

`func NewHeroBuildStatsWithDefaults() *HeroBuildStats`

NewHeroBuildStatsWithDefaults instantiates a new HeroBuildStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

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


