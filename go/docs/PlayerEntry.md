# PlayerEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **int32** |  | 
**Badge** | Pointer to **NullableInt32** | &#x60;rank&#x60; and &#x60;peak_rank&#x60; sorts only: the rank badge the progress in &#x60;value&#x60; falls in, &#x60;0&#x60; when the player has no ranked match in range. Omitted for every other sort. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional] 
**BadgeProgress** | Pointer to **NullableInt32** | &#x60;rank&#x60; and &#x60;peak_rank&#x60; sorts only: progress points into &#x60;badge&#x60;, out of &#x60;badge_progress_max&#x60;. In Eternus, whose subranks are percentile cuts rather than point spans, the points past the start of Eternus. &#x60;null&#x60; when the player has no ranked match in range. | [optional] 
**BadgeProgressMax** | Pointer to **NullableInt32** | &#x60;rank&#x60; and &#x60;peak_rank&#x60; sorts only: the points the subrank of &#x60;badge&#x60; spans in that match&#39;s season (&#x60;sub_rank_xp&#x60; in &lt;https://api.deadlock-api.com/v1/assets/ranked-seasons&gt;). &#x60;null&#x60; in Eternus and when the player has no ranked match in range. | [optional] 
**Matches** | **int64** |  | 
**Rank** | **int64** |  | 
**Value** | **float64** |  | 

## Methods

### NewPlayerEntry

`func NewPlayerEntry(accountId int32, matches int64, rank int64, value float64, ) *PlayerEntry`

NewPlayerEntry instantiates a new PlayerEntry object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPlayerEntryWithDefaults

`func NewPlayerEntryWithDefaults() *PlayerEntry`

NewPlayerEntryWithDefaults instantiates a new PlayerEntry object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccountId

`func (o *PlayerEntry) GetAccountId() int32`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *PlayerEntry) GetAccountIdOk() (*int32, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *PlayerEntry) SetAccountId(v int32)`

SetAccountId sets AccountId field to given value.


### GetBadge

`func (o *PlayerEntry) GetBadge() int32`

GetBadge returns the Badge field if non-nil, zero value otherwise.

### GetBadgeOk

`func (o *PlayerEntry) GetBadgeOk() (*int32, bool)`

GetBadgeOk returns a tuple with the Badge field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBadge

`func (o *PlayerEntry) SetBadge(v int32)`

SetBadge sets Badge field to given value.

### HasBadge

`func (o *PlayerEntry) HasBadge() bool`

HasBadge returns a boolean if a field has been set.

### SetBadgeNil

`func (o *PlayerEntry) SetBadgeNil(b bool)`

 SetBadgeNil sets the value for Badge to be an explicit nil

### UnsetBadge
`func (o *PlayerEntry) UnsetBadge()`

UnsetBadge ensures that no value is present for Badge, not even an explicit nil
### GetBadgeProgress

`func (o *PlayerEntry) GetBadgeProgress() int32`

GetBadgeProgress returns the BadgeProgress field if non-nil, zero value otherwise.

### GetBadgeProgressOk

`func (o *PlayerEntry) GetBadgeProgressOk() (*int32, bool)`

GetBadgeProgressOk returns a tuple with the BadgeProgress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBadgeProgress

`func (o *PlayerEntry) SetBadgeProgress(v int32)`

SetBadgeProgress sets BadgeProgress field to given value.

### HasBadgeProgress

`func (o *PlayerEntry) HasBadgeProgress() bool`

HasBadgeProgress returns a boolean if a field has been set.

### SetBadgeProgressNil

`func (o *PlayerEntry) SetBadgeProgressNil(b bool)`

 SetBadgeProgressNil sets the value for BadgeProgress to be an explicit nil

### UnsetBadgeProgress
`func (o *PlayerEntry) UnsetBadgeProgress()`

UnsetBadgeProgress ensures that no value is present for BadgeProgress, not even an explicit nil
### GetBadgeProgressMax

`func (o *PlayerEntry) GetBadgeProgressMax() int32`

GetBadgeProgressMax returns the BadgeProgressMax field if non-nil, zero value otherwise.

### GetBadgeProgressMaxOk

`func (o *PlayerEntry) GetBadgeProgressMaxOk() (*int32, bool)`

GetBadgeProgressMaxOk returns a tuple with the BadgeProgressMax field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBadgeProgressMax

`func (o *PlayerEntry) SetBadgeProgressMax(v int32)`

SetBadgeProgressMax sets BadgeProgressMax field to given value.

### HasBadgeProgressMax

`func (o *PlayerEntry) HasBadgeProgressMax() bool`

HasBadgeProgressMax returns a boolean if a field has been set.

### SetBadgeProgressMaxNil

`func (o *PlayerEntry) SetBadgeProgressMaxNil(b bool)`

 SetBadgeProgressMaxNil sets the value for BadgeProgressMax to be an explicit nil

### UnsetBadgeProgressMax
`func (o *PlayerEntry) UnsetBadgeProgressMax()`

UnsetBadgeProgressMax ensures that no value is present for BadgeProgressMax, not even an explicit nil
### GetMatches

`func (o *PlayerEntry) GetMatches() int64`

GetMatches returns the Matches field if non-nil, zero value otherwise.

### GetMatchesOk

`func (o *PlayerEntry) GetMatchesOk() (*int64, bool)`

GetMatchesOk returns a tuple with the Matches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatches

`func (o *PlayerEntry) SetMatches(v int64)`

SetMatches sets Matches field to given value.


### GetRank

`func (o *PlayerEntry) GetRank() int64`

GetRank returns the Rank field if non-nil, zero value otherwise.

### GetRankOk

`func (o *PlayerEntry) GetRankOk() (*int64, bool)`

GetRankOk returns a tuple with the Rank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRank

`func (o *PlayerEntry) SetRank(v int64)`

SetRank sets Rank field to given value.


### GetValue

`func (o *PlayerEntry) GetValue() float64`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *PlayerEntry) GetValueOk() (*float64, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *PlayerEntry) SetValue(v float64)`

SetValue sets Value field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


