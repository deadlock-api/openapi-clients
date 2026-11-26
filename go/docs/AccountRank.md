# AccountRank

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Badge** | **int64** | Rank badge, &#x60;tier * 10 + subrank&#x60;, including the progress the last ranked match awarded. Eternus subranks are percentile-based and refreshed daily by Valve, so within Eternus this is the badge the player entered their latest ranked match with. &#x60;0&#x60; when no recent ranked match reports a rank. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | 
**LastMatch** | Pointer to [**NullableLastRankedMatch**](LastRankedMatch.md) | Rank metadata of the ranked match the badge was read from. &#x60;null&#x60; when none of the player&#39;s recent ranked matches reports a rank. | [optional] 
**Rank** | **int64** | Rank tier, &#x60;0&#x60; when unknown. | 
**Subrank** | **int64** | Sub-rank within the tier, &#x60;0&#x60; when unknown. | 
**AccountId** | **int64** | The players &#x60;SteamID3&#x60; | 

## Methods

### NewAccountRank

`func NewAccountRank(badge int64, rank int64, subrank int64, accountId int64, ) *AccountRank`

NewAccountRank instantiates a new AccountRank object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAccountRankWithDefaults

`func NewAccountRankWithDefaults() *AccountRank`

NewAccountRankWithDefaults instantiates a new AccountRank object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBadge

`func (o *AccountRank) GetBadge() int64`

GetBadge returns the Badge field if non-nil, zero value otherwise.

### GetBadgeOk

`func (o *AccountRank) GetBadgeOk() (*int64, bool)`

GetBadgeOk returns a tuple with the Badge field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBadge

`func (o *AccountRank) SetBadge(v int64)`

SetBadge sets Badge field to given value.


### GetLastMatch

`func (o *AccountRank) GetLastMatch() LastRankedMatch`

GetLastMatch returns the LastMatch field if non-nil, zero value otherwise.

### GetLastMatchOk

`func (o *AccountRank) GetLastMatchOk() (*LastRankedMatch, bool)`

GetLastMatchOk returns a tuple with the LastMatch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastMatch

`func (o *AccountRank) SetLastMatch(v LastRankedMatch)`

SetLastMatch sets LastMatch field to given value.

### HasLastMatch

`func (o *AccountRank) HasLastMatch() bool`

HasLastMatch returns a boolean if a field has been set.

### SetLastMatchNil

`func (o *AccountRank) SetLastMatchNil(b bool)`

 SetLastMatchNil sets the value for LastMatch to be an explicit nil

### UnsetLastMatch
`func (o *AccountRank) UnsetLastMatch()`

UnsetLastMatch ensures that no value is present for LastMatch, not even an explicit nil
### GetRank

`func (o *AccountRank) GetRank() int64`

GetRank returns the Rank field if non-nil, zero value otherwise.

### GetRankOk

`func (o *AccountRank) GetRankOk() (*int64, bool)`

GetRankOk returns a tuple with the Rank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRank

`func (o *AccountRank) SetRank(v int64)`

SetRank sets Rank field to given value.


### GetSubrank

`func (o *AccountRank) GetSubrank() int64`

GetSubrank returns the Subrank field if non-nil, zero value otherwise.

### GetSubrankOk

`func (o *AccountRank) GetSubrankOk() (*int64, bool)`

GetSubrankOk returns a tuple with the Subrank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubrank

`func (o *AccountRank) SetSubrank(v int64)`

SetSubrank sets Subrank field to given value.


### GetAccountId

`func (o *AccountRank) GetAccountId() int64`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *AccountRank) GetAccountIdOk() (*int64, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *AccountRank) SetAccountId(v int64)`

SetAccountId sets AccountId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


