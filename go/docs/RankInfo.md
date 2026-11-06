# RankInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BadgeShields** | Pointer to **NullableInt32** | Losses a player at a badge&#39;s first subrank with 0 rank points can take before dropping a badge (rank loss protection shields). | [optional] 
**RankEnd** | Pointer to **NullableInt32** | Rank badge (tier * 10 + subrank) the entry stops at: it covers the ranks below it. In Beta Season 2, 91 (Phantom I) gives every rank below Phantom shields and Phantom and up none. | [optional] 
**SubRankShields** | Pointer to **NullableInt32** | Losses a player can take before dropping a subrank (rank loss protection shields). | [optional] 
**SubRankXp** | Pointer to **[]int32** | Rank points needed per subrank step, the last one being the step to the next badge (Beta Season 2: 1000 between subranks, 1500 from the final subrank). | [optional] 

## Methods

### NewRankInfo

`func NewRankInfo() *RankInfo`

NewRankInfo instantiates a new RankInfo object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRankInfoWithDefaults

`func NewRankInfoWithDefaults() *RankInfo`

NewRankInfoWithDefaults instantiates a new RankInfo object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBadgeShields

`func (o *RankInfo) GetBadgeShields() int32`

GetBadgeShields returns the BadgeShields field if non-nil, zero value otherwise.

### GetBadgeShieldsOk

`func (o *RankInfo) GetBadgeShieldsOk() (*int32, bool)`

GetBadgeShieldsOk returns a tuple with the BadgeShields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBadgeShields

`func (o *RankInfo) SetBadgeShields(v int32)`

SetBadgeShields sets BadgeShields field to given value.

### HasBadgeShields

`func (o *RankInfo) HasBadgeShields() bool`

HasBadgeShields returns a boolean if a field has been set.

### SetBadgeShieldsNil

`func (o *RankInfo) SetBadgeShieldsNil(b bool)`

 SetBadgeShieldsNil sets the value for BadgeShields to be an explicit nil

### UnsetBadgeShields
`func (o *RankInfo) UnsetBadgeShields()`

UnsetBadgeShields ensures that no value is present for BadgeShields, not even an explicit nil
### GetRankEnd

`func (o *RankInfo) GetRankEnd() int32`

GetRankEnd returns the RankEnd field if non-nil, zero value otherwise.

### GetRankEndOk

`func (o *RankInfo) GetRankEndOk() (*int32, bool)`

GetRankEndOk returns a tuple with the RankEnd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRankEnd

`func (o *RankInfo) SetRankEnd(v int32)`

SetRankEnd sets RankEnd field to given value.

### HasRankEnd

`func (o *RankInfo) HasRankEnd() bool`

HasRankEnd returns a boolean if a field has been set.

### SetRankEndNil

`func (o *RankInfo) SetRankEndNil(b bool)`

 SetRankEndNil sets the value for RankEnd to be an explicit nil

### UnsetRankEnd
`func (o *RankInfo) UnsetRankEnd()`

UnsetRankEnd ensures that no value is present for RankEnd, not even an explicit nil
### GetSubRankShields

`func (o *RankInfo) GetSubRankShields() int32`

GetSubRankShields returns the SubRankShields field if non-nil, zero value otherwise.

### GetSubRankShieldsOk

`func (o *RankInfo) GetSubRankShieldsOk() (*int32, bool)`

GetSubRankShieldsOk returns a tuple with the SubRankShields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubRankShields

`func (o *RankInfo) SetSubRankShields(v int32)`

SetSubRankShields sets SubRankShields field to given value.

### HasSubRankShields

`func (o *RankInfo) HasSubRankShields() bool`

HasSubRankShields returns a boolean if a field has been set.

### SetSubRankShieldsNil

`func (o *RankInfo) SetSubRankShieldsNil(b bool)`

 SetSubRankShieldsNil sets the value for SubRankShields to be an explicit nil

### UnsetSubRankShields
`func (o *RankInfo) UnsetSubRankShields()`

UnsetSubRankShields ensures that no value is present for SubRankShields, not even an explicit nil
### GetSubRankXp

`func (o *RankInfo) GetSubRankXp() []int32`

GetSubRankXp returns the SubRankXp field if non-nil, zero value otherwise.

### GetSubRankXpOk

`func (o *RankInfo) GetSubRankXpOk() (*[]int32, bool)`

GetSubRankXpOk returns a tuple with the SubRankXp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubRankXp

`func (o *RankInfo) SetSubRankXp(v []int32)`

SetSubRankXp sets SubRankXp field to given value.

### HasSubRankXp

`func (o *RankInfo) HasSubRankXp() bool`

HasSubRankXp returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


