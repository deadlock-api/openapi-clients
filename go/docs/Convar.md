# Convar

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Default** | **map[string]interface{}** | Default value, typed by &#x60;type&#x60;: a bool, number or string, &#x60;[r, g, b, a]&#x60; for &#x60;color&#x60;, and an array of floats for vectors / &#x60;qangle&#x60;. | 
**Description** | Pointer to **NullableString** | Help text shown by the in-game console. | [optional] 
**Flags** | **int64** | Raw &#x60;FCVAR_*&#x60; flag bits. | 
**Type** | [**ConvarType**](ConvarType.md) |  | 

## Methods

### NewConvar

`func NewConvar(default_ map[string]interface{}, flags int64, type_ ConvarType, ) *Convar`

NewConvar instantiates a new Convar object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewConvarWithDefaults

`func NewConvarWithDefaults() *Convar`

NewConvarWithDefaults instantiates a new Convar object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDefault

`func (o *Convar) GetDefault() map[string]interface{}`

GetDefault returns the Default field if non-nil, zero value otherwise.

### GetDefaultOk

`func (o *Convar) GetDefaultOk() (*map[string]interface{}, bool)`

GetDefaultOk returns a tuple with the Default field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefault

`func (o *Convar) SetDefault(v map[string]interface{})`

SetDefault sets Default field to given value.


### GetDescription

`func (o *Convar) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Convar) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Convar) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *Convar) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *Convar) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *Convar) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetFlags

`func (o *Convar) GetFlags() int64`

GetFlags returns the Flags field if non-nil, zero value otherwise.

### GetFlagsOk

`func (o *Convar) GetFlagsOk() (*int64, bool)`

GetFlagsOk returns a tuple with the Flags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlags

`func (o *Convar) SetFlags(v int64)`

SetFlags sets Flags field to given value.


### GetType

`func (o *Convar) GetType() ConvarType`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Convar) GetTypeOk() (*ConvarType, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Convar) SetType(v ConvarType)`

SetType sets Type field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


