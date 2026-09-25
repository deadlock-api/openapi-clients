# SteamAccountResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CreatedAt** | **time.Time** |  | 
**DeletedAt** | Pointer to **NullableTime** |  | [optional] 
**Id** | **string** |  | 
**SteamId3** | **int64** |  | 

## Methods

### NewSteamAccountResponse

`func NewSteamAccountResponse(createdAt time.Time, id string, steamId3 int64, ) *SteamAccountResponse`

NewSteamAccountResponse instantiates a new SteamAccountResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSteamAccountResponseWithDefaults

`func NewSteamAccountResponseWithDefaults() *SteamAccountResponse`

NewSteamAccountResponseWithDefaults instantiates a new SteamAccountResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCreatedAt

`func (o *SteamAccountResponse) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *SteamAccountResponse) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *SteamAccountResponse) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetDeletedAt

`func (o *SteamAccountResponse) GetDeletedAt() time.Time`

GetDeletedAt returns the DeletedAt field if non-nil, zero value otherwise.

### GetDeletedAtOk

`func (o *SteamAccountResponse) GetDeletedAtOk() (*time.Time, bool)`

GetDeletedAtOk returns a tuple with the DeletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeletedAt

`func (o *SteamAccountResponse) SetDeletedAt(v time.Time)`

SetDeletedAt sets DeletedAt field to given value.

### HasDeletedAt

`func (o *SteamAccountResponse) HasDeletedAt() bool`

HasDeletedAt returns a boolean if a field has been set.

### SetDeletedAtNil

`func (o *SteamAccountResponse) SetDeletedAtNil(b bool)`

 SetDeletedAtNil sets the value for DeletedAt to be an explicit nil

### UnsetDeletedAt
`func (o *SteamAccountResponse) UnsetDeletedAt()`

UnsetDeletedAt ensures that no value is present for DeletedAt, not even an explicit nil
### GetId

`func (o *SteamAccountResponse) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SteamAccountResponse) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SteamAccountResponse) SetId(v string)`

SetId sets Id field to given value.


### GetSteamId3

`func (o *SteamAccountResponse) GetSteamId3() int64`

GetSteamId3 returns the SteamId3 field if non-nil, zero value otherwise.

### GetSteamId3Ok

`func (o *SteamAccountResponse) GetSteamId3Ok() (*int64, bool)`

GetSteamId3Ok returns a tuple with the SteamId3 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSteamId3

`func (o *SteamAccountResponse) SetSteamId3(v int64)`

SetSteamId3 sets SteamId3 field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


