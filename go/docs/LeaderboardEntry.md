# LeaderboardEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountName** | Pointer to **NullableString** | The account name of the player. | [optional] 
**PossibleAccountIds** | Pointer to **[]int32** | The possible account IDs of the player. **CAVEAT: This is not always correct, as Steam account names are not unique.** | [optional] 
**Rank** | Pointer to **NullableInt32** | The rank of the player (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional] 
**TopHeroIds** | Pointer to **[]int32** | The top hero IDs of the player. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [optional] 

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


