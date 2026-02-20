# PlayerAccountStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **int32** |  | 
**Stats** | [**[]PlayerAccountHeroStats**](PlayerAccountHeroStats.md) |  | 

## Methods

### NewPlayerAccountStats

`func NewPlayerAccountStats(accountId int32, stats []PlayerAccountHeroStats, ) *PlayerAccountStats`

NewPlayerAccountStats instantiates a new PlayerAccountStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPlayerAccountStatsWithDefaults

`func NewPlayerAccountStatsWithDefaults() *PlayerAccountStats`

NewPlayerAccountStatsWithDefaults instantiates a new PlayerAccountStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccountId

`func (o *PlayerAccountStats) GetAccountId() int32`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *PlayerAccountStats) GetAccountIdOk() (*int32, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *PlayerAccountStats) SetAccountId(v int32)`

SetAccountId sets AccountId field to given value.


### GetStats

`func (o *PlayerAccountStats) GetStats() []PlayerAccountHeroStats`

GetStats returns the Stats field if non-nil, zero value otherwise.

### GetStatsOk

`func (o *PlayerAccountStats) GetStatsOk() (*[]PlayerAccountHeroStats, bool)`

GetStatsOk returns a tuple with the Stats field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStats

`func (o *PlayerAccountStats) SetStats(v []PlayerAccountHeroStats)`

SetStats sets Stats field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


