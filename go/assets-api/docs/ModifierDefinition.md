# ModifierDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClassName** | Pointer to **NullableString** |  | [optional] 
**SubclassName** | Pointer to **NullableString** |  | [optional] 
**Duration** | Pointer to **NullableFloat32** |  | [optional] 
**TimeMin** | Pointer to **NullableFloat32** |  | [optional] 
**TimeMax** | Pointer to **NullableFloat32** |  | [optional] 
**DebuffType** | Pointer to **NullableString** |  | [optional] 
**AlwaysShowInUi** | Pointer to **[]string** |  | [optional] 
**ModifierValues** | Pointer to [**[]ModifierValue**](ModifierValue.md) |  | [optional] 
**ScriptValues** | Pointer to [**[]ModifierValue**](ModifierValue.md) |  | [optional] 

## Methods

### NewModifierDefinition

`func NewModifierDefinition() *ModifierDefinition`

NewModifierDefinition instantiates a new ModifierDefinition object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewModifierDefinitionWithDefaults

`func NewModifierDefinitionWithDefaults() *ModifierDefinition`

NewModifierDefinitionWithDefaults instantiates a new ModifierDefinition object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClassName

`func (o *ModifierDefinition) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *ModifierDefinition) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *ModifierDefinition) SetClassName(v string)`

SetClassName sets ClassName field to given value.

### HasClassName

`func (o *ModifierDefinition) HasClassName() bool`

HasClassName returns a boolean if a field has been set.

### SetClassNameNil

`func (o *ModifierDefinition) SetClassNameNil(b bool)`

 SetClassNameNil sets the value for ClassName to be an explicit nil

### UnsetClassName
`func (o *ModifierDefinition) UnsetClassName()`

UnsetClassName ensures that no value is present for ClassName, not even an explicit nil
### GetSubclassName

`func (o *ModifierDefinition) GetSubclassName() string`

GetSubclassName returns the SubclassName field if non-nil, zero value otherwise.

### GetSubclassNameOk

`func (o *ModifierDefinition) GetSubclassNameOk() (*string, bool)`

GetSubclassNameOk returns a tuple with the SubclassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubclassName

`func (o *ModifierDefinition) SetSubclassName(v string)`

SetSubclassName sets SubclassName field to given value.

### HasSubclassName

`func (o *ModifierDefinition) HasSubclassName() bool`

HasSubclassName returns a boolean if a field has been set.

### SetSubclassNameNil

`func (o *ModifierDefinition) SetSubclassNameNil(b bool)`

 SetSubclassNameNil sets the value for SubclassName to be an explicit nil

### UnsetSubclassName
`func (o *ModifierDefinition) UnsetSubclassName()`

UnsetSubclassName ensures that no value is present for SubclassName, not even an explicit nil
### GetDuration

`func (o *ModifierDefinition) GetDuration() float32`

GetDuration returns the Duration field if non-nil, zero value otherwise.

### GetDurationOk

`func (o *ModifierDefinition) GetDurationOk() (*float32, bool)`

GetDurationOk returns a tuple with the Duration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDuration

`func (o *ModifierDefinition) SetDuration(v float32)`

SetDuration sets Duration field to given value.

### HasDuration

`func (o *ModifierDefinition) HasDuration() bool`

HasDuration returns a boolean if a field has been set.

### SetDurationNil

`func (o *ModifierDefinition) SetDurationNil(b bool)`

 SetDurationNil sets the value for Duration to be an explicit nil

### UnsetDuration
`func (o *ModifierDefinition) UnsetDuration()`

UnsetDuration ensures that no value is present for Duration, not even an explicit nil
### GetTimeMin

`func (o *ModifierDefinition) GetTimeMin() float32`

GetTimeMin returns the TimeMin field if non-nil, zero value otherwise.

### GetTimeMinOk

`func (o *ModifierDefinition) GetTimeMinOk() (*float32, bool)`

GetTimeMinOk returns a tuple with the TimeMin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimeMin

`func (o *ModifierDefinition) SetTimeMin(v float32)`

SetTimeMin sets TimeMin field to given value.

### HasTimeMin

`func (o *ModifierDefinition) HasTimeMin() bool`

HasTimeMin returns a boolean if a field has been set.

### SetTimeMinNil

`func (o *ModifierDefinition) SetTimeMinNil(b bool)`

 SetTimeMinNil sets the value for TimeMin to be an explicit nil

### UnsetTimeMin
`func (o *ModifierDefinition) UnsetTimeMin()`

UnsetTimeMin ensures that no value is present for TimeMin, not even an explicit nil
### GetTimeMax

`func (o *ModifierDefinition) GetTimeMax() float32`

GetTimeMax returns the TimeMax field if non-nil, zero value otherwise.

### GetTimeMaxOk

`func (o *ModifierDefinition) GetTimeMaxOk() (*float32, bool)`

GetTimeMaxOk returns a tuple with the TimeMax field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimeMax

`func (o *ModifierDefinition) SetTimeMax(v float32)`

SetTimeMax sets TimeMax field to given value.

### HasTimeMax

`func (o *ModifierDefinition) HasTimeMax() bool`

HasTimeMax returns a boolean if a field has been set.

### SetTimeMaxNil

`func (o *ModifierDefinition) SetTimeMaxNil(b bool)`

 SetTimeMaxNil sets the value for TimeMax to be an explicit nil

### UnsetTimeMax
`func (o *ModifierDefinition) UnsetTimeMax()`

UnsetTimeMax ensures that no value is present for TimeMax, not even an explicit nil
### GetDebuffType

`func (o *ModifierDefinition) GetDebuffType() string`

GetDebuffType returns the DebuffType field if non-nil, zero value otherwise.

### GetDebuffTypeOk

`func (o *ModifierDefinition) GetDebuffTypeOk() (*string, bool)`

GetDebuffTypeOk returns a tuple with the DebuffType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDebuffType

`func (o *ModifierDefinition) SetDebuffType(v string)`

SetDebuffType sets DebuffType field to given value.

### HasDebuffType

`func (o *ModifierDefinition) HasDebuffType() bool`

HasDebuffType returns a boolean if a field has been set.

### SetDebuffTypeNil

`func (o *ModifierDefinition) SetDebuffTypeNil(b bool)`

 SetDebuffTypeNil sets the value for DebuffType to be an explicit nil

### UnsetDebuffType
`func (o *ModifierDefinition) UnsetDebuffType()`

UnsetDebuffType ensures that no value is present for DebuffType, not even an explicit nil
### GetAlwaysShowInUi

`func (o *ModifierDefinition) GetAlwaysShowInUi() []string`

GetAlwaysShowInUi returns the AlwaysShowInUi field if non-nil, zero value otherwise.

### GetAlwaysShowInUiOk

`func (o *ModifierDefinition) GetAlwaysShowInUiOk() (*[]string, bool)`

GetAlwaysShowInUiOk returns a tuple with the AlwaysShowInUi field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAlwaysShowInUi

`func (o *ModifierDefinition) SetAlwaysShowInUi(v []string)`

SetAlwaysShowInUi sets AlwaysShowInUi field to given value.

### HasAlwaysShowInUi

`func (o *ModifierDefinition) HasAlwaysShowInUi() bool`

HasAlwaysShowInUi returns a boolean if a field has been set.

### SetAlwaysShowInUiNil

`func (o *ModifierDefinition) SetAlwaysShowInUiNil(b bool)`

 SetAlwaysShowInUiNil sets the value for AlwaysShowInUi to be an explicit nil

### UnsetAlwaysShowInUi
`func (o *ModifierDefinition) UnsetAlwaysShowInUi()`

UnsetAlwaysShowInUi ensures that no value is present for AlwaysShowInUi, not even an explicit nil
### GetModifierValues

`func (o *ModifierDefinition) GetModifierValues() []ModifierValue`

GetModifierValues returns the ModifierValues field if non-nil, zero value otherwise.

### GetModifierValuesOk

`func (o *ModifierDefinition) GetModifierValuesOk() (*[]ModifierValue, bool)`

GetModifierValuesOk returns a tuple with the ModifierValues field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifierValues

`func (o *ModifierDefinition) SetModifierValues(v []ModifierValue)`

SetModifierValues sets ModifierValues field to given value.

### HasModifierValues

`func (o *ModifierDefinition) HasModifierValues() bool`

HasModifierValues returns a boolean if a field has been set.

### SetModifierValuesNil

`func (o *ModifierDefinition) SetModifierValuesNil(b bool)`

 SetModifierValuesNil sets the value for ModifierValues to be an explicit nil

### UnsetModifierValues
`func (o *ModifierDefinition) UnsetModifierValues()`

UnsetModifierValues ensures that no value is present for ModifierValues, not even an explicit nil
### GetScriptValues

`func (o *ModifierDefinition) GetScriptValues() []ModifierValue`

GetScriptValues returns the ScriptValues field if non-nil, zero value otherwise.

### GetScriptValuesOk

`func (o *ModifierDefinition) GetScriptValuesOk() (*[]ModifierValue, bool)`

GetScriptValuesOk returns a tuple with the ScriptValues field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScriptValues

`func (o *ModifierDefinition) SetScriptValues(v []ModifierValue)`

SetScriptValues sets ScriptValues field to given value.

### HasScriptValues

`func (o *ModifierDefinition) HasScriptValues() bool`

HasScriptValues returns a boolean if a field has been set.

### SetScriptValuesNil

`func (o *ModifierDefinition) SetScriptValuesNil(b bool)`

 SetScriptValuesNil sets the value for ScriptValues to be an explicit nil

### UnsetScriptValues
`func (o *ModifierDefinition) UnsetScriptValues()`

UnsetScriptValues ensures that no value is present for ScriptValues, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


