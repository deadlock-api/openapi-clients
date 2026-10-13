# BotFriendStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Invites** | **[]string** | Friend invite links of bots to add, empty once &#x60;is_friend&#x60; is true | 
**IsFriend** | **bool** |  | 

## Methods

### NewBotFriendStatus

`func NewBotFriendStatus(invites []string, isFriend bool, ) *BotFriendStatus`

NewBotFriendStatus instantiates a new BotFriendStatus object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBotFriendStatusWithDefaults

`func NewBotFriendStatusWithDefaults() *BotFriendStatus`

NewBotFriendStatusWithDefaults instantiates a new BotFriendStatus object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetInvites

`func (o *BotFriendStatus) GetInvites() []string`

GetInvites returns the Invites field if non-nil, zero value otherwise.

### GetInvitesOk

`func (o *BotFriendStatus) GetInvitesOk() (*[]string, bool)`

GetInvitesOk returns a tuple with the Invites field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInvites

`func (o *BotFriendStatus) SetInvites(v []string)`

SetInvites sets Invites field to given value.


### GetIsFriend

`func (o *BotFriendStatus) GetIsFriend() bool`

GetIsFriend returns the IsFriend field if non-nil, zero value otherwise.

### GetIsFriendOk

`func (o *BotFriendStatus) GetIsFriendOk() (*bool, bool)`

GetIsFriendOk returns a tuple with the IsFriend field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsFriend

`func (o *BotFriendStatus) SetIsFriend(v bool)`

SetIsFriend sets IsFriend field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


