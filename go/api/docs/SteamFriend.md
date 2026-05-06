# SteamFriend

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **int32** |  | 
**FriendSince** | **time.Time** |  | 

## Methods

### NewSteamFriend

`func NewSteamFriend(accountId int32, friendSince time.Time, ) *SteamFriend`

NewSteamFriend instantiates a new SteamFriend object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSteamFriendWithDefaults

`func NewSteamFriendWithDefaults() *SteamFriend`

NewSteamFriendWithDefaults instantiates a new SteamFriend object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccountId

`func (o *SteamFriend) GetAccountId() int32`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *SteamFriend) GetAccountIdOk() (*int32, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *SteamFriend) SetAccountId(v int32)`

SetAccountId sets AccountId field to given value.


### GetFriendSince

`func (o *SteamFriend) GetFriendSince() time.Time`

GetFriendSince returns the FriendSince field if non-nil, zero value otherwise.

### GetFriendSinceOk

`func (o *SteamFriend) GetFriendSinceOk() (*time.Time, bool)`

GetFriendSinceOk returns a tuple with the FriendSince field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFriendSince

`func (o *SteamFriend) SetFriendSince(v time.Time)`

SetFriendSince sets FriendSince field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


