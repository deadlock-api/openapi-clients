# Entry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**HeroId** | **int32** | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**Matches** | **int64** |  | 
**Rank** | **int64** | tier &#x3D; first digits, subtier &#x3D; last digit, see more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
**Value** | **float64** |  | 

## Methods

### NewEntry

`func NewEntry(heroId int32, matches int64, rank int64, value float64, ) *Entry`

NewEntry instantiates a new Entry object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEntryWithDefaults

`func NewEntryWithDefaults() *Entry`

NewEntryWithDefaults instantiates a new Entry object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetHeroId

`func (o *Entry) GetHeroId() int32`

GetHeroId returns the HeroId field if non-nil, zero value otherwise.

### GetHeroIdOk

`func (o *Entry) GetHeroIdOk() (*int32, bool)`

GetHeroIdOk returns a tuple with the HeroId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroId

`func (o *Entry) SetHeroId(v int32)`

SetHeroId sets HeroId field to given value.


### GetMatches

`func (o *Entry) GetMatches() int64`

GetMatches returns the Matches field if non-nil, zero value otherwise.

### GetMatchesOk

`func (o *Entry) GetMatchesOk() (*int64, bool)`

GetMatchesOk returns a tuple with the Matches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatches

`func (o *Entry) SetMatches(v int64)`

SetMatches sets Matches field to given value.


### GetRank

`func (o *Entry) GetRank() int64`

GetRank returns the Rank field if non-nil, zero value otherwise.

### GetRankOk

`func (o *Entry) GetRankOk() (*int64, bool)`

GetRankOk returns a tuple with the Rank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRank

`func (o *Entry) SetRank(v int64)`

SetRank sets Rank field to given value.


### GetValue

`func (o *Entry) GetValue() float64`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *Entry) GetValueOk() (*float64, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *Entry) SetValue(v float64)`

SetValue sets Value field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


