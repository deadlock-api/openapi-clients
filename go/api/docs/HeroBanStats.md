# HeroBanStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Bans** | **int64** | The number of matches in which this hero was banned. | 
**HeroId** | **int32** | The ID of the banned hero. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 

## Methods

### NewHeroBanStats

`func NewHeroBanStats(bans int64, heroId int32, ) *HeroBanStats`

NewHeroBanStats instantiates a new HeroBanStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHeroBanStatsWithDefaults

`func NewHeroBanStatsWithDefaults() *HeroBanStats`

NewHeroBanStatsWithDefaults instantiates a new HeroBanStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBans

`func (o *HeroBanStats) GetBans() int64`

GetBans returns the Bans field if non-nil, zero value otherwise.

### GetBansOk

`func (o *HeroBanStats) GetBansOk() (*int64, bool)`

GetBansOk returns a tuple with the Bans field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBans

`func (o *HeroBanStats) SetBans(v int64)`

SetBans sets Bans field to given value.


### GetHeroId

`func (o *HeroBanStats) GetHeroId() int32`

GetHeroId returns the HeroId field if non-nil, zero value otherwise.

### GetHeroIdOk

`func (o *HeroBanStats) GetHeroIdOk() (*int32, bool)`

GetHeroIdOk returns a tuple with the HeroId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroId

`func (o *HeroBanStats) SetHeroId(v int32)`

SetHeroId sets HeroId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


