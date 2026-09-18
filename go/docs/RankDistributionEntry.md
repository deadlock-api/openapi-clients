# RankDistributionEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Badge** | **int32** | Rank badge, &#x60;tier * 10 + subrank&#x60;. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | 
**Players** | **int64** | Number of players whose rank at the end of their latest ranked match in the filtered range is this badge. | 
**Rank** | **int32** | Rank tier. | 
**Subrank** | **int32** | Sub-rank within the tier. | 

## Methods

### NewRankDistributionEntry

`func NewRankDistributionEntry(badge int32, players int64, rank int32, subrank int32, ) *RankDistributionEntry`

NewRankDistributionEntry instantiates a new RankDistributionEntry object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRankDistributionEntryWithDefaults

`func NewRankDistributionEntryWithDefaults() *RankDistributionEntry`

NewRankDistributionEntryWithDefaults instantiates a new RankDistributionEntry object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBadge

`func (o *RankDistributionEntry) GetBadge() int32`

GetBadge returns the Badge field if non-nil, zero value otherwise.

### GetBadgeOk

`func (o *RankDistributionEntry) GetBadgeOk() (*int32, bool)`

GetBadgeOk returns a tuple with the Badge field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBadge

`func (o *RankDistributionEntry) SetBadge(v int32)`

SetBadge sets Badge field to given value.


### GetPlayers

`func (o *RankDistributionEntry) GetPlayers() int64`

GetPlayers returns the Players field if non-nil, zero value otherwise.

### GetPlayersOk

`func (o *RankDistributionEntry) GetPlayersOk() (*int64, bool)`

GetPlayersOk returns a tuple with the Players field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayers

`func (o *RankDistributionEntry) SetPlayers(v int64)`

SetPlayers sets Players field to given value.


### GetRank

`func (o *RankDistributionEntry) GetRank() int32`

GetRank returns the Rank field if non-nil, zero value otherwise.

### GetRankOk

`func (o *RankDistributionEntry) GetRankOk() (*int32, bool)`

GetRankOk returns a tuple with the Rank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRank

`func (o *RankDistributionEntry) SetRank(v int32)`

SetRank sets Rank field to given value.


### GetSubrank

`func (o *RankDistributionEntry) GetSubrank() int32`

GetSubrank returns the Subrank field if non-nil, zero value otherwise.

### GetSubrankOk

`func (o *RankDistributionEntry) GetSubrankOk() (*int32, bool)`

GetSubrankOk returns a tuple with the Subrank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubrank

`func (o *RankDistributionEntry) SetSubrank(v int32)`

SetSubrank sets Subrank field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


