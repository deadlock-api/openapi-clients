# Status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Services** | [**StatusServices**](StatusServices.md) | Status of the services. | 

## Methods

### NewStatus

`func NewStatus(services StatusServices, ) *Status`

NewStatus instantiates a new Status object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStatusWithDefaults

`func NewStatusWithDefaults() *Status`

NewStatusWithDefaults instantiates a new Status object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetServices

`func (o *Status) GetServices() StatusServices`

GetServices returns the Services field if non-nil, zero value otherwise.

### GetServicesOk

`func (o *Status) GetServicesOk() (*StatusServices, bool)`

GetServicesOk returns a tuple with the Services field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetServices

`func (o *Status) SetServices(v StatusServices)`

SetServices sets Services field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


