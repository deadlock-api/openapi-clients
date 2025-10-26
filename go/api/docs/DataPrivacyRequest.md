# DataPrivacyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OpenIdParams** | **map[string]string** |  | 
**SteamId** | **int32** |  | 

## Methods

### NewDataPrivacyRequest

`func NewDataPrivacyRequest(openIdParams map[string]string, steamId int32, ) *DataPrivacyRequest`

NewDataPrivacyRequest instantiates a new DataPrivacyRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDataPrivacyRequestWithDefaults

`func NewDataPrivacyRequestWithDefaults() *DataPrivacyRequest`

NewDataPrivacyRequestWithDefaults instantiates a new DataPrivacyRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOpenIdParams

`func (o *DataPrivacyRequest) GetOpenIdParams() map[string]string`

GetOpenIdParams returns the OpenIdParams field if non-nil, zero value otherwise.

### GetOpenIdParamsOk

`func (o *DataPrivacyRequest) GetOpenIdParamsOk() (*map[string]string, bool)`

GetOpenIdParamsOk returns a tuple with the OpenIdParams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpenIdParams

`func (o *DataPrivacyRequest) SetOpenIdParams(v map[string]string)`

SetOpenIdParams sets OpenIdParams field to given value.


### GetSteamId

`func (o *DataPrivacyRequest) GetSteamId() int32`

GetSteamId returns the SteamId field if non-nil, zero value otherwise.

### GetSteamIdOk

`func (o *DataPrivacyRequest) GetSteamIdOk() (*int32, bool)`

GetSteamIdOk returns a tuple with the SteamId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSteamId

`func (o *DataPrivacyRequest) SetSteamId(v int32)`

SetSteamId sets SteamId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


