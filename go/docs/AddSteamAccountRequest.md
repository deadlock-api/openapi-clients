# AddSteamAccountRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SteamId3** | **int64** | Steam ID3 (32-bit unsigned integer format) | 

## Methods

### NewAddSteamAccountRequest

`func NewAddSteamAccountRequest(steamId3 int64, ) *AddSteamAccountRequest`

NewAddSteamAccountRequest instantiates a new AddSteamAccountRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAddSteamAccountRequestWithDefaults

`func NewAddSteamAccountRequestWithDefaults() *AddSteamAccountRequest`

NewAddSteamAccountRequestWithDefaults instantiates a new AddSteamAccountRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSteamId3

`func (o *AddSteamAccountRequest) GetSteamId3() int64`

GetSteamId3 returns the SteamId3 field if non-nil, zero value otherwise.

### GetSteamId3Ok

`func (o *AddSteamAccountRequest) GetSteamId3Ok() (*int64, bool)`

GetSteamId3Ok returns a tuple with the SteamId3 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSteamId3

`func (o *AddSteamAccountRequest) SetSteamId3(v int64)`

SetSteamId3 sets SteamId3 field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


