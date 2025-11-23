# ScriptValues

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ModifierValue** | Pointer to **NullableString** |  | [optional] 
**Value** | Pointer to **NullableFloat32** |  | [optional] 

## Methods

### NewScriptValues

`func NewScriptValues() *ScriptValues`

NewScriptValues instantiates a new ScriptValues object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewScriptValuesWithDefaults

`func NewScriptValuesWithDefaults() *ScriptValues`

NewScriptValuesWithDefaults instantiates a new ScriptValues object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetModifierValue

`func (o *ScriptValues) GetModifierValue() string`

GetModifierValue returns the ModifierValue field if non-nil, zero value otherwise.

### GetModifierValueOk

`func (o *ScriptValues) GetModifierValueOk() (*string, bool)`

GetModifierValueOk returns a tuple with the ModifierValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifierValue

`func (o *ScriptValues) SetModifierValue(v string)`

SetModifierValue sets ModifierValue field to given value.

### HasModifierValue

`func (o *ScriptValues) HasModifierValue() bool`

HasModifierValue returns a boolean if a field has been set.

### SetModifierValueNil

`func (o *ScriptValues) SetModifierValueNil(b bool)`

 SetModifierValueNil sets the value for ModifierValue to be an explicit nil

### UnsetModifierValue
`func (o *ScriptValues) UnsetModifierValue()`

UnsetModifierValue ensures that no value is present for ModifierValue, not even an explicit nil
### GetValue

`func (o *ScriptValues) GetValue() float32`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *ScriptValues) GetValueOk() (*float32, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *ScriptValues) SetValue(v float32)`

SetValue sets Value field to given value.

### HasValue

`func (o *ScriptValues) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValueNil

`func (o *ScriptValues) SetValueNil(b bool)`

 SetValueNil sets the value for Value to be an explicit nil

### UnsetValue
`func (o *ScriptValues) UnsetValue()`

UnsetValue ensures that no value is present for Value, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


