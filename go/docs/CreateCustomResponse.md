# CreateCustomResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CallbackSecret** | Pointer to **NullableString** | If a callback url is provided, this is the secret that should be used to verify the callback. The secret is a base64 encoded random string. To verify it you should compare it with the X-Callback-Secret header. If no callback url is provided, this will be None. | [optional] 
**PartyCode** | **string** |  | 
**PartyId** | **string** |  | 

## Methods

### NewCreateCustomResponse

`func NewCreateCustomResponse(partyCode string, partyId string, ) *CreateCustomResponse`

NewCreateCustomResponse instantiates a new CreateCustomResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateCustomResponseWithDefaults

`func NewCreateCustomResponseWithDefaults() *CreateCustomResponse`

NewCreateCustomResponseWithDefaults instantiates a new CreateCustomResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCallbackSecret

`func (o *CreateCustomResponse) GetCallbackSecret() string`

GetCallbackSecret returns the CallbackSecret field if non-nil, zero value otherwise.

### GetCallbackSecretOk

`func (o *CreateCustomResponse) GetCallbackSecretOk() (*string, bool)`

GetCallbackSecretOk returns a tuple with the CallbackSecret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCallbackSecret

`func (o *CreateCustomResponse) SetCallbackSecret(v string)`

SetCallbackSecret sets CallbackSecret field to given value.

### HasCallbackSecret

`func (o *CreateCustomResponse) HasCallbackSecret() bool`

HasCallbackSecret returns a boolean if a field has been set.

### SetCallbackSecretNil

`func (o *CreateCustomResponse) SetCallbackSecretNil(b bool)`

 SetCallbackSecretNil sets the value for CallbackSecret to be an explicit nil

### UnsetCallbackSecret
`func (o *CreateCustomResponse) UnsetCallbackSecret()`

UnsetCallbackSecret ensures that no value is present for CallbackSecret, not even an explicit nil
### GetPartyCode

`func (o *CreateCustomResponse) GetPartyCode() string`

GetPartyCode returns the PartyCode field if non-nil, zero value otherwise.

### GetPartyCodeOk

`func (o *CreateCustomResponse) GetPartyCodeOk() (*string, bool)`

GetPartyCodeOk returns a tuple with the PartyCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPartyCode

`func (o *CreateCustomResponse) SetPartyCode(v string)`

SetPartyCode sets PartyCode field to given value.


### GetPartyId

`func (o *CreateCustomResponse) GetPartyId() string`

GetPartyId returns the PartyId field if non-nil, zero value otherwise.

### GetPartyIdOk

`func (o *CreateCustomResponse) GetPartyIdOk() (*string, bool)`

GetPartyIdOk returns a tuple with the PartyId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPartyId

`func (o *CreateCustomResponse) SetPartyId(v string)`

SetPartyId sets PartyId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


