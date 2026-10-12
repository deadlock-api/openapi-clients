# HeroSwapStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Bucket** | **int32** | The bucket value (depends on the bucket query parameter). | 
**HeroId** | **int32** | The ID of the hero. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**Matches** | **int64** | The number of players who played this hero, counting only players whose pre-game hero is known. | 
**PregamePicks** | **int64** | The number of players who had this hero locked before the pre-game swap window. | 
**SwappedAway** | **int64** | The number of &#x60;pregame_picks&#x60; players who swapped away from this hero. | 
**SwappedIn** | **int64** | The number of players who played this hero after swapping to it from another pre-game hero. | 
**SwappedInWins** | **int64** | The number of &#x60;swapped_in&#x60; players who won the match. | 

## Methods

### NewHeroSwapStats

`func NewHeroSwapStats(bucket int32, heroId int32, matches int64, pregamePicks int64, swappedAway int64, swappedIn int64, swappedInWins int64, ) *HeroSwapStats`

NewHeroSwapStats instantiates a new HeroSwapStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHeroSwapStatsWithDefaults

`func NewHeroSwapStatsWithDefaults() *HeroSwapStats`

NewHeroSwapStatsWithDefaults instantiates a new HeroSwapStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBucket

`func (o *HeroSwapStats) GetBucket() int32`

GetBucket returns the Bucket field if non-nil, zero value otherwise.

### GetBucketOk

`func (o *HeroSwapStats) GetBucketOk() (*int32, bool)`

GetBucketOk returns a tuple with the Bucket field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBucket

`func (o *HeroSwapStats) SetBucket(v int32)`

SetBucket sets Bucket field to given value.


### GetHeroId

`func (o *HeroSwapStats) GetHeroId() int32`

GetHeroId returns the HeroId field if non-nil, zero value otherwise.

### GetHeroIdOk

`func (o *HeroSwapStats) GetHeroIdOk() (*int32, bool)`

GetHeroIdOk returns a tuple with the HeroId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroId

`func (o *HeroSwapStats) SetHeroId(v int32)`

SetHeroId sets HeroId field to given value.


### GetMatches

`func (o *HeroSwapStats) GetMatches() int64`

GetMatches returns the Matches field if non-nil, zero value otherwise.

### GetMatchesOk

`func (o *HeroSwapStats) GetMatchesOk() (*int64, bool)`

GetMatchesOk returns a tuple with the Matches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatches

`func (o *HeroSwapStats) SetMatches(v int64)`

SetMatches sets Matches field to given value.


### GetPregamePicks

`func (o *HeroSwapStats) GetPregamePicks() int64`

GetPregamePicks returns the PregamePicks field if non-nil, zero value otherwise.

### GetPregamePicksOk

`func (o *HeroSwapStats) GetPregamePicksOk() (*int64, bool)`

GetPregamePicksOk returns a tuple with the PregamePicks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPregamePicks

`func (o *HeroSwapStats) SetPregamePicks(v int64)`

SetPregamePicks sets PregamePicks field to given value.


### GetSwappedAway

`func (o *HeroSwapStats) GetSwappedAway() int64`

GetSwappedAway returns the SwappedAway field if non-nil, zero value otherwise.

### GetSwappedAwayOk

`func (o *HeroSwapStats) GetSwappedAwayOk() (*int64, bool)`

GetSwappedAwayOk returns a tuple with the SwappedAway field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSwappedAway

`func (o *HeroSwapStats) SetSwappedAway(v int64)`

SetSwappedAway sets SwappedAway field to given value.


### GetSwappedIn

`func (o *HeroSwapStats) GetSwappedIn() int64`

GetSwappedIn returns the SwappedIn field if non-nil, zero value otherwise.

### GetSwappedInOk

`func (o *HeroSwapStats) GetSwappedInOk() (*int64, bool)`

GetSwappedInOk returns a tuple with the SwappedIn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSwappedIn

`func (o *HeroSwapStats) SetSwappedIn(v int64)`

SetSwappedIn sets SwappedIn field to given value.


### GetSwappedInWins

`func (o *HeroSwapStats) GetSwappedInWins() int64`

GetSwappedInWins returns the SwappedInWins field if non-nil, zero value otherwise.

### GetSwappedInWinsOk

`func (o *HeroSwapStats) GetSwappedInWinsOk() (*int64, bool)`

GetSwappedInWinsOk returns a tuple with the SwappedInWins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSwappedInWins

`func (o *HeroSwapStats) SetSwappedInWins(v int64)`

SetSwappedInWins sets SwappedInWins field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


