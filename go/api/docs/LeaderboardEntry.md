# LeaderboardEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountName** | Pointer to **NullableString** | The account name of the player. | [optional] 
**BadgeLevel** | Pointer to **NullableInt32** | The badge level of the player. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**PossibleAccountIds** | Pointer to **[]int32** | The possible account IDs of the player. **CAVEAT: This is not always correct, as Steam account names are not unique.** | [optional] 
**Rank** | Pointer to **NullableInt32** | The rank of the player. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**RankedRank** | Pointer to **NullableInt32** | The ranked rank of the player. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**RankedSubrank** | Pointer to **NullableInt32** | The ranked subrank of the player. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**TopHeroIds** | Pointer to **[]int32** | The top hero IDs of the player. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] 

## Methods

### NewLeaderboardEntry

`func NewLeaderboardEntry() *LeaderboardEntry`

NewLeaderboardEntry instantiates a new LeaderboardEntry object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewLeaderboardEntryWithDefaults

`func NewLeaderboardEntryWithDefaults() *LeaderboardEntry`

NewLeaderboardEntryWithDefaults instantiates a new LeaderboardEntry object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccountName

`func (o *LeaderboardEntry) GetAccountName() string`

GetAccountName returns the AccountName field if non-nil, zero value otherwise.

### GetAccountNameOk

`func (o *LeaderboardEntry) GetAccountNameOk() (*string, bool)`

GetAccountNameOk returns a tuple with the AccountName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountName

`func (o *LeaderboardEntry) SetAccountName(v string)`

SetAccountName sets AccountName field to given value.

### HasAccountName

`func (o *LeaderboardEntry) HasAccountName() bool`

HasAccountName returns a boolean if a field has been set.

### SetAccountNameNil

`func (o *LeaderboardEntry) SetAccountNameNil(b bool)`

 SetAccountNameNil sets the value for AccountName to be an explicit nil

### UnsetAccountName
`func (o *LeaderboardEntry) UnsetAccountName()`

UnsetAccountName ensures that no value is present for AccountName, not even an explicit nil
### GetBadgeLevel

`func (o *LeaderboardEntry) GetBadgeLevel() int32`

GetBadgeLevel returns the BadgeLevel field if non-nil, zero value otherwise.

### GetBadgeLevelOk

`func (o *LeaderboardEntry) GetBadgeLevelOk() (*int32, bool)`

GetBadgeLevelOk returns a tuple with the BadgeLevel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBadgeLevel

`func (o *LeaderboardEntry) SetBadgeLevel(v int32)`

SetBadgeLevel sets BadgeLevel field to given value.

### HasBadgeLevel

`func (o *LeaderboardEntry) HasBadgeLevel() bool`

HasBadgeLevel returns a boolean if a field has been set.

### SetBadgeLevelNil

`func (o *LeaderboardEntry) SetBadgeLevelNil(b bool)`

 SetBadgeLevelNil sets the value for BadgeLevel to be an explicit nil

### UnsetBadgeLevel
`func (o *LeaderboardEntry) UnsetBadgeLevel()`

UnsetBadgeLevel ensures that no value is present for BadgeLevel, not even an explicit nil
### GetPossibleAccountIds

`func (o *LeaderboardEntry) GetPossibleAccountIds() []int32`

GetPossibleAccountIds returns the PossibleAccountIds field if non-nil, zero value otherwise.

### GetPossibleAccountIdsOk

`func (o *LeaderboardEntry) GetPossibleAccountIdsOk() (*[]int32, bool)`

GetPossibleAccountIdsOk returns a tuple with the PossibleAccountIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPossibleAccountIds

`func (o *LeaderboardEntry) SetPossibleAccountIds(v []int32)`

SetPossibleAccountIds sets PossibleAccountIds field to given value.

### HasPossibleAccountIds

`func (o *LeaderboardEntry) HasPossibleAccountIds() bool`

HasPossibleAccountIds returns a boolean if a field has been set.

### GetRank

`func (o *LeaderboardEntry) GetRank() int32`

GetRank returns the Rank field if non-nil, zero value otherwise.

### GetRankOk

`func (o *LeaderboardEntry) GetRankOk() (*int32, bool)`

GetRankOk returns a tuple with the Rank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRank

`func (o *LeaderboardEntry) SetRank(v int32)`

SetRank sets Rank field to given value.

### HasRank

`func (o *LeaderboardEntry) HasRank() bool`

HasRank returns a boolean if a field has been set.

### SetRankNil

`func (o *LeaderboardEntry) SetRankNil(b bool)`

 SetRankNil sets the value for Rank to be an explicit nil

### UnsetRank
`func (o *LeaderboardEntry) UnsetRank()`

UnsetRank ensures that no value is present for Rank, not even an explicit nil
### GetRankedRank

`func (o *LeaderboardEntry) GetRankedRank() int32`

GetRankedRank returns the RankedRank field if non-nil, zero value otherwise.

### GetRankedRankOk

`func (o *LeaderboardEntry) GetRankedRankOk() (*int32, bool)`

GetRankedRankOk returns a tuple with the RankedRank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRankedRank

`func (o *LeaderboardEntry) SetRankedRank(v int32)`

SetRankedRank sets RankedRank field to given value.

### HasRankedRank

`func (o *LeaderboardEntry) HasRankedRank() bool`

HasRankedRank returns a boolean if a field has been set.

### SetRankedRankNil

`func (o *LeaderboardEntry) SetRankedRankNil(b bool)`

 SetRankedRankNil sets the value for RankedRank to be an explicit nil

### UnsetRankedRank
`func (o *LeaderboardEntry) UnsetRankedRank()`

UnsetRankedRank ensures that no value is present for RankedRank, not even an explicit nil
### GetRankedSubrank

`func (o *LeaderboardEntry) GetRankedSubrank() int32`

GetRankedSubrank returns the RankedSubrank field if non-nil, zero value otherwise.

### GetRankedSubrankOk

`func (o *LeaderboardEntry) GetRankedSubrankOk() (*int32, bool)`

GetRankedSubrankOk returns a tuple with the RankedSubrank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRankedSubrank

`func (o *LeaderboardEntry) SetRankedSubrank(v int32)`

SetRankedSubrank sets RankedSubrank field to given value.

### HasRankedSubrank

`func (o *LeaderboardEntry) HasRankedSubrank() bool`

HasRankedSubrank returns a boolean if a field has been set.

### SetRankedSubrankNil

`func (o *LeaderboardEntry) SetRankedSubrankNil(b bool)`

 SetRankedSubrankNil sets the value for RankedSubrank to be an explicit nil

### UnsetRankedSubrank
`func (o *LeaderboardEntry) UnsetRankedSubrank()`

UnsetRankedSubrank ensures that no value is present for RankedSubrank, not even an explicit nil
### GetTopHeroIds

`func (o *LeaderboardEntry) GetTopHeroIds() []int32`

GetTopHeroIds returns the TopHeroIds field if non-nil, zero value otherwise.

### GetTopHeroIdsOk

`func (o *LeaderboardEntry) GetTopHeroIdsOk() (*[]int32, bool)`

GetTopHeroIdsOk returns a tuple with the TopHeroIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopHeroIds

`func (o *LeaderboardEntry) SetTopHeroIds(v []int32)`

SetTopHeroIds sets TopHeroIds field to given value.

### HasTopHeroIds

`func (o *LeaderboardEntry) HasTopHeroIds() bool`

HasTopHeroIds returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


