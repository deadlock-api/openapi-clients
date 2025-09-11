# SteamProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **int32** |  | 
**Avatar** | **string** |  | 
**Avatarfull** | **string** |  | 
**Avatarmedium** | **string** |  | 
**Countrycode** | Pointer to **NullableString** |  | [optional] 
**LastUpdated** | **time.Time** |  | 
**Personaname** | **string** |  | 
**Profileurl** | **string** |  | 
**Realname** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewSteamProfile

`func NewSteamProfile(accountId int32, avatar string, avatarfull string, avatarmedium string, lastUpdated time.Time, personaname string, profileurl string, ) *SteamProfile`

NewSteamProfile instantiates a new SteamProfile object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSteamProfileWithDefaults

`func NewSteamProfileWithDefaults() *SteamProfile`

NewSteamProfileWithDefaults instantiates a new SteamProfile object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccountId

`func (o *SteamProfile) GetAccountId() int32`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *SteamProfile) GetAccountIdOk() (*int32, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *SteamProfile) SetAccountId(v int32)`

SetAccountId sets AccountId field to given value.


### GetAvatar

`func (o *SteamProfile) GetAvatar() string`

GetAvatar returns the Avatar field if non-nil, zero value otherwise.

### GetAvatarOk

`func (o *SteamProfile) GetAvatarOk() (*string, bool)`

GetAvatarOk returns a tuple with the Avatar field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvatar

`func (o *SteamProfile) SetAvatar(v string)`

SetAvatar sets Avatar field to given value.


### GetAvatarfull

`func (o *SteamProfile) GetAvatarfull() string`

GetAvatarfull returns the Avatarfull field if non-nil, zero value otherwise.

### GetAvatarfullOk

`func (o *SteamProfile) GetAvatarfullOk() (*string, bool)`

GetAvatarfullOk returns a tuple with the Avatarfull field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvatarfull

`func (o *SteamProfile) SetAvatarfull(v string)`

SetAvatarfull sets Avatarfull field to given value.


### GetAvatarmedium

`func (o *SteamProfile) GetAvatarmedium() string`

GetAvatarmedium returns the Avatarmedium field if non-nil, zero value otherwise.

### GetAvatarmediumOk

`func (o *SteamProfile) GetAvatarmediumOk() (*string, bool)`

GetAvatarmediumOk returns a tuple with the Avatarmedium field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvatarmedium

`func (o *SteamProfile) SetAvatarmedium(v string)`

SetAvatarmedium sets Avatarmedium field to given value.


### GetCountrycode

`func (o *SteamProfile) GetCountrycode() string`

GetCountrycode returns the Countrycode field if non-nil, zero value otherwise.

### GetCountrycodeOk

`func (o *SteamProfile) GetCountrycodeOk() (*string, bool)`

GetCountrycodeOk returns a tuple with the Countrycode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountrycode

`func (o *SteamProfile) SetCountrycode(v string)`

SetCountrycode sets Countrycode field to given value.

### HasCountrycode

`func (o *SteamProfile) HasCountrycode() bool`

HasCountrycode returns a boolean if a field has been set.

### SetCountrycodeNil

`func (o *SteamProfile) SetCountrycodeNil(b bool)`

 SetCountrycodeNil sets the value for Countrycode to be an explicit nil

### UnsetCountrycode
`func (o *SteamProfile) UnsetCountrycode()`

UnsetCountrycode ensures that no value is present for Countrycode, not even an explicit nil
### GetLastUpdated

`func (o *SteamProfile) GetLastUpdated() time.Time`

GetLastUpdated returns the LastUpdated field if non-nil, zero value otherwise.

### GetLastUpdatedOk

`func (o *SteamProfile) GetLastUpdatedOk() (*time.Time, bool)`

GetLastUpdatedOk returns a tuple with the LastUpdated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastUpdated

`func (o *SteamProfile) SetLastUpdated(v time.Time)`

SetLastUpdated sets LastUpdated field to given value.


### GetPersonaname

`func (o *SteamProfile) GetPersonaname() string`

GetPersonaname returns the Personaname field if non-nil, zero value otherwise.

### GetPersonanameOk

`func (o *SteamProfile) GetPersonanameOk() (*string, bool)`

GetPersonanameOk returns a tuple with the Personaname field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPersonaname

`func (o *SteamProfile) SetPersonaname(v string)`

SetPersonaname sets Personaname field to given value.


### GetProfileurl

`func (o *SteamProfile) GetProfileurl() string`

GetProfileurl returns the Profileurl field if non-nil, zero value otherwise.

### GetProfileurlOk

`func (o *SteamProfile) GetProfileurlOk() (*string, bool)`

GetProfileurlOk returns a tuple with the Profileurl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProfileurl

`func (o *SteamProfile) SetProfileurl(v string)`

SetProfileurl sets Profileurl field to given value.


### GetRealname

`func (o *SteamProfile) GetRealname() string`

GetRealname returns the Realname field if non-nil, zero value otherwise.

### GetRealnameOk

`func (o *SteamProfile) GetRealnameOk() (*string, bool)`

GetRealnameOk returns a tuple with the Realname field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRealname

`func (o *SteamProfile) SetRealname(v string)`

SetRealname sets Realname field to given value.

### HasRealname

`func (o *SteamProfile) HasRealname() bool`

HasRealname returns a boolean if a field has been set.

### SetRealnameNil

`func (o *SteamProfile) SetRealnameNil(b bool)`

 SetRealnameNil sets the value for Realname to be an explicit nil

### UnsetRealname
`func (o *SteamProfile) UnsetRealname()`

UnsetRealname ensures that no value is present for Realname, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


