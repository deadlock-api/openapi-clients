# LeaderboardEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountName** | Pointer to **NullableString** | The account name of the player. | [optional] 
**PossibleAccountIds** | **[]int64** | The possible account IDs of the player. **CAVEAT: This is not always correct, as Steam account names are not unique.** | 
**Rank** | Pointer to **NullableInt64** | The player&#39;s place on the leaderboard, starting at 1. Players can share a place, and the following places are then skipped (1, 2, 2, 4). Not a rank badge. | [optional] 
**TopHeroIds** | **[]int64** | The top hero IDs of the player, as the game sends them. Since 2026-07-31 the game leaves them empty for about half of the entries. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 

## Methods

### NewLeaderboardEntry

`func NewLeaderboardEntry(possibleAccountIds []int64, topHeroIds []int64, ) *LeaderboardEntry`

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
### GetPossibleAccountIds

`func (o *LeaderboardEntry) GetPossibleAccountIds() []int64`

GetPossibleAccountIds returns the PossibleAccountIds field if non-nil, zero value otherwise.

### GetPossibleAccountIdsOk

`func (o *LeaderboardEntry) GetPossibleAccountIdsOk() (*[]int64, bool)`

GetPossibleAccountIdsOk returns a tuple with the PossibleAccountIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPossibleAccountIds

`func (o *LeaderboardEntry) SetPossibleAccountIds(v []int64)`

SetPossibleAccountIds sets PossibleAccountIds field to given value.


### GetRank

`func (o *LeaderboardEntry) GetRank() int64`

GetRank returns the Rank field if non-nil, zero value otherwise.

### GetRankOk

`func (o *LeaderboardEntry) GetRankOk() (*int64, bool)`

GetRankOk returns a tuple with the Rank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRank

`func (o *LeaderboardEntry) SetRank(v int64)`

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
### GetTopHeroIds

`func (o *LeaderboardEntry) GetTopHeroIds() []int64`

GetTopHeroIds returns the TopHeroIds field if non-nil, zero value otherwise.

### GetTopHeroIdsOk

`func (o *LeaderboardEntry) GetTopHeroIdsOk() (*[]int64, bool)`

GetTopHeroIdsOk returns a tuple with the TopHeroIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopHeroIds

`func (o *LeaderboardEntry) SetTopHeroIds(v []int64)`

SetTopHeroIds sets TopHeroIds field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


