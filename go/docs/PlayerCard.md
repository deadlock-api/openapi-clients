# PlayerCard

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **int32** |  | 
**RankedBadgeLevel** | Pointer to **NullableInt32** | See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**RankedRank** | Pointer to **NullableInt32** | See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**RankedSubrank** | Pointer to **NullableInt32** | See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**Slots** | [**[]PlayerCardSlot**](PlayerCardSlot.md) |  | 

## Methods

### NewPlayerCard

`func NewPlayerCard(accountId int32, slots []PlayerCardSlot, ) *PlayerCard`

NewPlayerCard instantiates a new PlayerCard object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPlayerCardWithDefaults

`func NewPlayerCardWithDefaults() *PlayerCard`

NewPlayerCardWithDefaults instantiates a new PlayerCard object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccountId

`func (o *PlayerCard) GetAccountId() int32`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *PlayerCard) GetAccountIdOk() (*int32, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *PlayerCard) SetAccountId(v int32)`

SetAccountId sets AccountId field to given value.


### GetRankedBadgeLevel

`func (o *PlayerCard) GetRankedBadgeLevel() int32`

GetRankedBadgeLevel returns the RankedBadgeLevel field if non-nil, zero value otherwise.

### GetRankedBadgeLevelOk

`func (o *PlayerCard) GetRankedBadgeLevelOk() (*int32, bool)`

GetRankedBadgeLevelOk returns a tuple with the RankedBadgeLevel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRankedBadgeLevel

`func (o *PlayerCard) SetRankedBadgeLevel(v int32)`

SetRankedBadgeLevel sets RankedBadgeLevel field to given value.

### HasRankedBadgeLevel

`func (o *PlayerCard) HasRankedBadgeLevel() bool`

HasRankedBadgeLevel returns a boolean if a field has been set.

### SetRankedBadgeLevelNil

`func (o *PlayerCard) SetRankedBadgeLevelNil(b bool)`

 SetRankedBadgeLevelNil sets the value for RankedBadgeLevel to be an explicit nil

### UnsetRankedBadgeLevel
`func (o *PlayerCard) UnsetRankedBadgeLevel()`

UnsetRankedBadgeLevel ensures that no value is present for RankedBadgeLevel, not even an explicit nil
### GetRankedRank

`func (o *PlayerCard) GetRankedRank() int32`

GetRankedRank returns the RankedRank field if non-nil, zero value otherwise.

### GetRankedRankOk

`func (o *PlayerCard) GetRankedRankOk() (*int32, bool)`

GetRankedRankOk returns a tuple with the RankedRank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRankedRank

`func (o *PlayerCard) SetRankedRank(v int32)`

SetRankedRank sets RankedRank field to given value.

### HasRankedRank

`func (o *PlayerCard) HasRankedRank() bool`

HasRankedRank returns a boolean if a field has been set.

### SetRankedRankNil

`func (o *PlayerCard) SetRankedRankNil(b bool)`

 SetRankedRankNil sets the value for RankedRank to be an explicit nil

### UnsetRankedRank
`func (o *PlayerCard) UnsetRankedRank()`

UnsetRankedRank ensures that no value is present for RankedRank, not even an explicit nil
### GetRankedSubrank

`func (o *PlayerCard) GetRankedSubrank() int32`

GetRankedSubrank returns the RankedSubrank field if non-nil, zero value otherwise.

### GetRankedSubrankOk

`func (o *PlayerCard) GetRankedSubrankOk() (*int32, bool)`

GetRankedSubrankOk returns a tuple with the RankedSubrank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRankedSubrank

`func (o *PlayerCard) SetRankedSubrank(v int32)`

SetRankedSubrank sets RankedSubrank field to given value.

### HasRankedSubrank

`func (o *PlayerCard) HasRankedSubrank() bool`

HasRankedSubrank returns a boolean if a field has been set.

### SetRankedSubrankNil

`func (o *PlayerCard) SetRankedSubrankNil(b bool)`

 SetRankedSubrankNil sets the value for RankedSubrank to be an explicit nil

### UnsetRankedSubrank
`func (o *PlayerCard) UnsetRankedSubrank()`

UnsetRankedSubrank ensures that no value is present for RankedSubrank, not even an explicit nil
### GetSlots

`func (o *PlayerCard) GetSlots() []PlayerCardSlot`

GetSlots returns the Slots field if non-nil, zero value otherwise.

### GetSlotsOk

`func (o *PlayerCard) GetSlotsOk() (*[]PlayerCardSlot, bool)`

GetSlotsOk returns a tuple with the Slots field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlots

`func (o *PlayerCard) SetSlots(v []PlayerCardSlot)`

SetSlots sets Slots field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


