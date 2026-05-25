# SubclassModifierDefinitionSubclass

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AlwaysShowInUi** | Pointer to **[]string** |  | [optional] 
**ClassName** | Pointer to **NullableString** |  | [optional] 
**Duration** | Pointer to **NullableFloat64** |  | [optional] 
**ModifierValues** | Pointer to [**[]ModifierValue**](ModifierValue.md) |  | [optional] 
**ScriptValues** | Pointer to [**[]ModifierValue**](ModifierValue.md) |  | [optional] 
**SubclassName** | Pointer to **NullableString** |  | [optional] 
**TimeMax** | Pointer to **NullableFloat64** |  | [optional] 
**TimeMin** | Pointer to **NullableFloat64** |  | [optional] 

## Methods

### NewSubclassModifierDefinitionSubclass

`func NewSubclassModifierDefinitionSubclass() *SubclassModifierDefinitionSubclass`

NewSubclassModifierDefinitionSubclass instantiates a new SubclassModifierDefinitionSubclass object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSubclassModifierDefinitionSubclassWithDefaults

`func NewSubclassModifierDefinitionSubclassWithDefaults() *SubclassModifierDefinitionSubclass`

NewSubclassModifierDefinitionSubclassWithDefaults instantiates a new SubclassModifierDefinitionSubclass object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAlwaysShowInUi

`func (o *SubclassModifierDefinitionSubclass) GetAlwaysShowInUi() []string`

GetAlwaysShowInUi returns the AlwaysShowInUi field if non-nil, zero value otherwise.

### GetAlwaysShowInUiOk

`func (o *SubclassModifierDefinitionSubclass) GetAlwaysShowInUiOk() (*[]string, bool)`

GetAlwaysShowInUiOk returns a tuple with the AlwaysShowInUi field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAlwaysShowInUi

`func (o *SubclassModifierDefinitionSubclass) SetAlwaysShowInUi(v []string)`

SetAlwaysShowInUi sets AlwaysShowInUi field to given value.

### HasAlwaysShowInUi

`func (o *SubclassModifierDefinitionSubclass) HasAlwaysShowInUi() bool`

HasAlwaysShowInUi returns a boolean if a field has been set.

### SetAlwaysShowInUiNil

`func (o *SubclassModifierDefinitionSubclass) SetAlwaysShowInUiNil(b bool)`

 SetAlwaysShowInUiNil sets the value for AlwaysShowInUi to be an explicit nil

### UnsetAlwaysShowInUi
`func (o *SubclassModifierDefinitionSubclass) UnsetAlwaysShowInUi()`

UnsetAlwaysShowInUi ensures that no value is present for AlwaysShowInUi, not even an explicit nil
### GetClassName

`func (o *SubclassModifierDefinitionSubclass) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *SubclassModifierDefinitionSubclass) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *SubclassModifierDefinitionSubclass) SetClassName(v string)`

SetClassName sets ClassName field to given value.

### HasClassName

`func (o *SubclassModifierDefinitionSubclass) HasClassName() bool`

HasClassName returns a boolean if a field has been set.

### SetClassNameNil

`func (o *SubclassModifierDefinitionSubclass) SetClassNameNil(b bool)`

 SetClassNameNil sets the value for ClassName to be an explicit nil

### UnsetClassName
`func (o *SubclassModifierDefinitionSubclass) UnsetClassName()`

UnsetClassName ensures that no value is present for ClassName, not even an explicit nil
### GetDuration

`func (o *SubclassModifierDefinitionSubclass) GetDuration() float64`

GetDuration returns the Duration field if non-nil, zero value otherwise.

### GetDurationOk

`func (o *SubclassModifierDefinitionSubclass) GetDurationOk() (*float64, bool)`

GetDurationOk returns a tuple with the Duration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDuration

`func (o *SubclassModifierDefinitionSubclass) SetDuration(v float64)`

SetDuration sets Duration field to given value.

### HasDuration

`func (o *SubclassModifierDefinitionSubclass) HasDuration() bool`

HasDuration returns a boolean if a field has been set.

### SetDurationNil

`func (o *SubclassModifierDefinitionSubclass) SetDurationNil(b bool)`

 SetDurationNil sets the value for Duration to be an explicit nil

### UnsetDuration
`func (o *SubclassModifierDefinitionSubclass) UnsetDuration()`

UnsetDuration ensures that no value is present for Duration, not even an explicit nil
### GetModifierValues

`func (o *SubclassModifierDefinitionSubclass) GetModifierValues() []ModifierValue`

GetModifierValues returns the ModifierValues field if non-nil, zero value otherwise.

### GetModifierValuesOk

`func (o *SubclassModifierDefinitionSubclass) GetModifierValuesOk() (*[]ModifierValue, bool)`

GetModifierValuesOk returns a tuple with the ModifierValues field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifierValues

`func (o *SubclassModifierDefinitionSubclass) SetModifierValues(v []ModifierValue)`

SetModifierValues sets ModifierValues field to given value.

### HasModifierValues

`func (o *SubclassModifierDefinitionSubclass) HasModifierValues() bool`

HasModifierValues returns a boolean if a field has been set.

### SetModifierValuesNil

`func (o *SubclassModifierDefinitionSubclass) SetModifierValuesNil(b bool)`

 SetModifierValuesNil sets the value for ModifierValues to be an explicit nil

### UnsetModifierValues
`func (o *SubclassModifierDefinitionSubclass) UnsetModifierValues()`

UnsetModifierValues ensures that no value is present for ModifierValues, not even an explicit nil
### GetScriptValues

`func (o *SubclassModifierDefinitionSubclass) GetScriptValues() []ModifierValue`

GetScriptValues returns the ScriptValues field if non-nil, zero value otherwise.

### GetScriptValuesOk

`func (o *SubclassModifierDefinitionSubclass) GetScriptValuesOk() (*[]ModifierValue, bool)`

GetScriptValuesOk returns a tuple with the ScriptValues field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScriptValues

`func (o *SubclassModifierDefinitionSubclass) SetScriptValues(v []ModifierValue)`

SetScriptValues sets ScriptValues field to given value.

### HasScriptValues

`func (o *SubclassModifierDefinitionSubclass) HasScriptValues() bool`

HasScriptValues returns a boolean if a field has been set.

### SetScriptValuesNil

`func (o *SubclassModifierDefinitionSubclass) SetScriptValuesNil(b bool)`

 SetScriptValuesNil sets the value for ScriptValues to be an explicit nil

### UnsetScriptValues
`func (o *SubclassModifierDefinitionSubclass) UnsetScriptValues()`

UnsetScriptValues ensures that no value is present for ScriptValues, not even an explicit nil
### GetSubclassName

`func (o *SubclassModifierDefinitionSubclass) GetSubclassName() string`

GetSubclassName returns the SubclassName field if non-nil, zero value otherwise.

### GetSubclassNameOk

`func (o *SubclassModifierDefinitionSubclass) GetSubclassNameOk() (*string, bool)`

GetSubclassNameOk returns a tuple with the SubclassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubclassName

`func (o *SubclassModifierDefinitionSubclass) SetSubclassName(v string)`

SetSubclassName sets SubclassName field to given value.

### HasSubclassName

`func (o *SubclassModifierDefinitionSubclass) HasSubclassName() bool`

HasSubclassName returns a boolean if a field has been set.

### SetSubclassNameNil

`func (o *SubclassModifierDefinitionSubclass) SetSubclassNameNil(b bool)`

 SetSubclassNameNil sets the value for SubclassName to be an explicit nil

### UnsetSubclassName
`func (o *SubclassModifierDefinitionSubclass) UnsetSubclassName()`

UnsetSubclassName ensures that no value is present for SubclassName, not even an explicit nil
### GetTimeMax

`func (o *SubclassModifierDefinitionSubclass) GetTimeMax() float64`

GetTimeMax returns the TimeMax field if non-nil, zero value otherwise.

### GetTimeMaxOk

`func (o *SubclassModifierDefinitionSubclass) GetTimeMaxOk() (*float64, bool)`

GetTimeMaxOk returns a tuple with the TimeMax field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimeMax

`func (o *SubclassModifierDefinitionSubclass) SetTimeMax(v float64)`

SetTimeMax sets TimeMax field to given value.

### HasTimeMax

`func (o *SubclassModifierDefinitionSubclass) HasTimeMax() bool`

HasTimeMax returns a boolean if a field has been set.

### SetTimeMaxNil

`func (o *SubclassModifierDefinitionSubclass) SetTimeMaxNil(b bool)`

 SetTimeMaxNil sets the value for TimeMax to be an explicit nil

### UnsetTimeMax
`func (o *SubclassModifierDefinitionSubclass) UnsetTimeMax()`

UnsetTimeMax ensures that no value is present for TimeMax, not even an explicit nil
### GetTimeMin

`func (o *SubclassModifierDefinitionSubclass) GetTimeMin() float64`

GetTimeMin returns the TimeMin field if non-nil, zero value otherwise.

### GetTimeMinOk

`func (o *SubclassModifierDefinitionSubclass) GetTimeMinOk() (*float64, bool)`

GetTimeMinOk returns a tuple with the TimeMin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimeMin

`func (o *SubclassModifierDefinitionSubclass) SetTimeMin(v float64)`

SetTimeMin sets TimeMin field to given value.

### HasTimeMin

`func (o *SubclassModifierDefinitionSubclass) HasTimeMin() bool`

HasTimeMin returns a boolean if a field has been set.

### SetTimeMinNil

`func (o *SubclassModifierDefinitionSubclass) SetTimeMinNil(b bool)`

 SetTimeMinNil sets the value for TimeMin to be an explicit nil

### UnsetTimeMin
`func (o *SubclassModifierDefinitionSubclass) UnsetTimeMin()`

UnsetTimeMin ensures that no value is present for TimeMin, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


