# SteamAccountListItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CreatedAt** | **time.Time** |  | 
**DeletedAt** | Pointer to **NullableTime** |  | [optional] 
**Id** | **string** |  | 
**IsInCooldown** | **bool** |  | 
**SteamId3** | **int64** |  | 

## Methods

### NewSteamAccountListItem

`func NewSteamAccountListItem(createdAt time.Time, id string, isInCooldown bool, steamId3 int64, ) *SteamAccountListItem`

NewSteamAccountListItem instantiates a new SteamAccountListItem object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSteamAccountListItemWithDefaults

`func NewSteamAccountListItemWithDefaults() *SteamAccountListItem`

NewSteamAccountListItemWithDefaults instantiates a new SteamAccountListItem object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCreatedAt

`func (o *SteamAccountListItem) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *SteamAccountListItem) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *SteamAccountListItem) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetDeletedAt

`func (o *SteamAccountListItem) GetDeletedAt() time.Time`

GetDeletedAt returns the DeletedAt field if non-nil, zero value otherwise.

### GetDeletedAtOk

`func (o *SteamAccountListItem) GetDeletedAtOk() (*time.Time, bool)`

GetDeletedAtOk returns a tuple with the DeletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeletedAt

`func (o *SteamAccountListItem) SetDeletedAt(v time.Time)`

SetDeletedAt sets DeletedAt field to given value.

### HasDeletedAt

`func (o *SteamAccountListItem) HasDeletedAt() bool`

HasDeletedAt returns a boolean if a field has been set.

### SetDeletedAtNil

`func (o *SteamAccountListItem) SetDeletedAtNil(b bool)`

 SetDeletedAtNil sets the value for DeletedAt to be an explicit nil

### UnsetDeletedAt
`func (o *SteamAccountListItem) UnsetDeletedAt()`

UnsetDeletedAt ensures that no value is present for DeletedAt, not even an explicit nil
### GetId

`func (o *SteamAccountListItem) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SteamAccountListItem) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SteamAccountListItem) SetId(v string)`

SetId sets Id field to given value.


### GetIsInCooldown

`func (o *SteamAccountListItem) GetIsInCooldown() bool`

GetIsInCooldown returns the IsInCooldown field if non-nil, zero value otherwise.

### GetIsInCooldownOk

`func (o *SteamAccountListItem) GetIsInCooldownOk() (*bool, bool)`

GetIsInCooldownOk returns a tuple with the IsInCooldown field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsInCooldown

`func (o *SteamAccountListItem) SetIsInCooldown(v bool)`

SetIsInCooldown sets IsInCooldown field to given value.


### GetSteamId3

`func (o *SteamAccountListItem) GetSteamId3() int64`

GetSteamId3 returns the SteamId3 field if non-nil, zero value otherwise.

### GetSteamId3Ok

`func (o *SteamAccountListItem) GetSteamId3Ok() (*int64, bool)`

GetSteamId3Ok returns a tuple with the SteamId3 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSteamId3

`func (o *SteamAccountListItem) SetSteamId3(v int64)`

SetSteamId3 sets SteamId3 field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


