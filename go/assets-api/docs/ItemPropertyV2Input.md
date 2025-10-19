# ItemPropertyV2Input

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MStrValue** | Pointer to [**NullableMStrvalue**](MStrvalue.md) |  | [optional] 
**MBCanSetTokenOverride** | Pointer to **NullableBool** |  | [optional] 
**MEProvidedPropertyType** | Pointer to **NullableString** |  | [optional] 
**MStrCSSClass** | Pointer to **NullableString** |  | [optional] 
**MEStatsUsageFlags** | Pointer to [**NullableMEstatsusageflags**](MEstatsusageflags.md) |  | [optional] 
**MBIsNegativeAttribute** | Pointer to **NullableBool** |  | [optional] 
**MStrDisableValue** | Pointer to **NullableString** |  | [optional] 
**MStrLocTokenOverride** | Pointer to **NullableString** |  | [optional] 
**MEDisplayUnits** | Pointer to **NullableString** |  | [optional] 
**ScaleFunction** | Pointer to [**NullableRawItemPropertyScaleFunctionSubclassV2Input**](RawItemPropertyScaleFunctionSubclassV2Input.md) |  | [optional] 
**Prefix** | Pointer to **NullableString** |  | [optional] 
**Label** | Pointer to **NullableString** |  | [optional] 
**Postfix** | Pointer to **NullableString** |  | [optional] 
**PostvalueLabel** | Pointer to **NullableString** |  | [optional] 
**Conditional** | Pointer to **NullableString** |  | [optional] 
**Icon** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewItemPropertyV2Input

`func NewItemPropertyV2Input() *ItemPropertyV2Input`

NewItemPropertyV2Input instantiates a new ItemPropertyV2Input object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewItemPropertyV2InputWithDefaults

`func NewItemPropertyV2InputWithDefaults() *ItemPropertyV2Input`

NewItemPropertyV2InputWithDefaults instantiates a new ItemPropertyV2Input object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMStrValue

`func (o *ItemPropertyV2Input) GetMStrValue() MStrvalue`

GetMStrValue returns the MStrValue field if non-nil, zero value otherwise.

### GetMStrValueOk

`func (o *ItemPropertyV2Input) GetMStrValueOk() (*MStrvalue, bool)`

GetMStrValueOk returns a tuple with the MStrValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMStrValue

`func (o *ItemPropertyV2Input) SetMStrValue(v MStrvalue)`

SetMStrValue sets MStrValue field to given value.

### HasMStrValue

`func (o *ItemPropertyV2Input) HasMStrValue() bool`

HasMStrValue returns a boolean if a field has been set.

### SetMStrValueNil

`func (o *ItemPropertyV2Input) SetMStrValueNil(b bool)`

 SetMStrValueNil sets the value for MStrValue to be an explicit nil

### UnsetMStrValue
`func (o *ItemPropertyV2Input) UnsetMStrValue()`

UnsetMStrValue ensures that no value is present for MStrValue, not even an explicit nil
### GetMBCanSetTokenOverride

`func (o *ItemPropertyV2Input) GetMBCanSetTokenOverride() bool`

GetMBCanSetTokenOverride returns the MBCanSetTokenOverride field if non-nil, zero value otherwise.

### GetMBCanSetTokenOverrideOk

`func (o *ItemPropertyV2Input) GetMBCanSetTokenOverrideOk() (*bool, bool)`

GetMBCanSetTokenOverrideOk returns a tuple with the MBCanSetTokenOverride field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMBCanSetTokenOverride

`func (o *ItemPropertyV2Input) SetMBCanSetTokenOverride(v bool)`

SetMBCanSetTokenOverride sets MBCanSetTokenOverride field to given value.

### HasMBCanSetTokenOverride

`func (o *ItemPropertyV2Input) HasMBCanSetTokenOverride() bool`

HasMBCanSetTokenOverride returns a boolean if a field has been set.

### SetMBCanSetTokenOverrideNil

`func (o *ItemPropertyV2Input) SetMBCanSetTokenOverrideNil(b bool)`

 SetMBCanSetTokenOverrideNil sets the value for MBCanSetTokenOverride to be an explicit nil

### UnsetMBCanSetTokenOverride
`func (o *ItemPropertyV2Input) UnsetMBCanSetTokenOverride()`

UnsetMBCanSetTokenOverride ensures that no value is present for MBCanSetTokenOverride, not even an explicit nil
### GetMEProvidedPropertyType

`func (o *ItemPropertyV2Input) GetMEProvidedPropertyType() string`

GetMEProvidedPropertyType returns the MEProvidedPropertyType field if non-nil, zero value otherwise.

### GetMEProvidedPropertyTypeOk

`func (o *ItemPropertyV2Input) GetMEProvidedPropertyTypeOk() (*string, bool)`

GetMEProvidedPropertyTypeOk returns a tuple with the MEProvidedPropertyType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMEProvidedPropertyType

`func (o *ItemPropertyV2Input) SetMEProvidedPropertyType(v string)`

SetMEProvidedPropertyType sets MEProvidedPropertyType field to given value.

### HasMEProvidedPropertyType

`func (o *ItemPropertyV2Input) HasMEProvidedPropertyType() bool`

HasMEProvidedPropertyType returns a boolean if a field has been set.

### SetMEProvidedPropertyTypeNil

`func (o *ItemPropertyV2Input) SetMEProvidedPropertyTypeNil(b bool)`

 SetMEProvidedPropertyTypeNil sets the value for MEProvidedPropertyType to be an explicit nil

### UnsetMEProvidedPropertyType
`func (o *ItemPropertyV2Input) UnsetMEProvidedPropertyType()`

UnsetMEProvidedPropertyType ensures that no value is present for MEProvidedPropertyType, not even an explicit nil
### GetMStrCSSClass

`func (o *ItemPropertyV2Input) GetMStrCSSClass() string`

GetMStrCSSClass returns the MStrCSSClass field if non-nil, zero value otherwise.

### GetMStrCSSClassOk

`func (o *ItemPropertyV2Input) GetMStrCSSClassOk() (*string, bool)`

GetMStrCSSClassOk returns a tuple with the MStrCSSClass field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMStrCSSClass

`func (o *ItemPropertyV2Input) SetMStrCSSClass(v string)`

SetMStrCSSClass sets MStrCSSClass field to given value.

### HasMStrCSSClass

`func (o *ItemPropertyV2Input) HasMStrCSSClass() bool`

HasMStrCSSClass returns a boolean if a field has been set.

### SetMStrCSSClassNil

`func (o *ItemPropertyV2Input) SetMStrCSSClassNil(b bool)`

 SetMStrCSSClassNil sets the value for MStrCSSClass to be an explicit nil

### UnsetMStrCSSClass
`func (o *ItemPropertyV2Input) UnsetMStrCSSClass()`

UnsetMStrCSSClass ensures that no value is present for MStrCSSClass, not even an explicit nil
### GetMEStatsUsageFlags

`func (o *ItemPropertyV2Input) GetMEStatsUsageFlags() MEstatsusageflags`

GetMEStatsUsageFlags returns the MEStatsUsageFlags field if non-nil, zero value otherwise.

### GetMEStatsUsageFlagsOk

`func (o *ItemPropertyV2Input) GetMEStatsUsageFlagsOk() (*MEstatsusageflags, bool)`

GetMEStatsUsageFlagsOk returns a tuple with the MEStatsUsageFlags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMEStatsUsageFlags

`func (o *ItemPropertyV2Input) SetMEStatsUsageFlags(v MEstatsusageflags)`

SetMEStatsUsageFlags sets MEStatsUsageFlags field to given value.

### HasMEStatsUsageFlags

`func (o *ItemPropertyV2Input) HasMEStatsUsageFlags() bool`

HasMEStatsUsageFlags returns a boolean if a field has been set.

### SetMEStatsUsageFlagsNil

`func (o *ItemPropertyV2Input) SetMEStatsUsageFlagsNil(b bool)`

 SetMEStatsUsageFlagsNil sets the value for MEStatsUsageFlags to be an explicit nil

### UnsetMEStatsUsageFlags
`func (o *ItemPropertyV2Input) UnsetMEStatsUsageFlags()`

UnsetMEStatsUsageFlags ensures that no value is present for MEStatsUsageFlags, not even an explicit nil
### GetMBIsNegativeAttribute

`func (o *ItemPropertyV2Input) GetMBIsNegativeAttribute() bool`

GetMBIsNegativeAttribute returns the MBIsNegativeAttribute field if non-nil, zero value otherwise.

### GetMBIsNegativeAttributeOk

`func (o *ItemPropertyV2Input) GetMBIsNegativeAttributeOk() (*bool, bool)`

GetMBIsNegativeAttributeOk returns a tuple with the MBIsNegativeAttribute field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMBIsNegativeAttribute

`func (o *ItemPropertyV2Input) SetMBIsNegativeAttribute(v bool)`

SetMBIsNegativeAttribute sets MBIsNegativeAttribute field to given value.

### HasMBIsNegativeAttribute

`func (o *ItemPropertyV2Input) HasMBIsNegativeAttribute() bool`

HasMBIsNegativeAttribute returns a boolean if a field has been set.

### SetMBIsNegativeAttributeNil

`func (o *ItemPropertyV2Input) SetMBIsNegativeAttributeNil(b bool)`

 SetMBIsNegativeAttributeNil sets the value for MBIsNegativeAttribute to be an explicit nil

### UnsetMBIsNegativeAttribute
`func (o *ItemPropertyV2Input) UnsetMBIsNegativeAttribute()`

UnsetMBIsNegativeAttribute ensures that no value is present for MBIsNegativeAttribute, not even an explicit nil
### GetMStrDisableValue

`func (o *ItemPropertyV2Input) GetMStrDisableValue() string`

GetMStrDisableValue returns the MStrDisableValue field if non-nil, zero value otherwise.

### GetMStrDisableValueOk

`func (o *ItemPropertyV2Input) GetMStrDisableValueOk() (*string, bool)`

GetMStrDisableValueOk returns a tuple with the MStrDisableValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMStrDisableValue

`func (o *ItemPropertyV2Input) SetMStrDisableValue(v string)`

SetMStrDisableValue sets MStrDisableValue field to given value.

### HasMStrDisableValue

`func (o *ItemPropertyV2Input) HasMStrDisableValue() bool`

HasMStrDisableValue returns a boolean if a field has been set.

### SetMStrDisableValueNil

`func (o *ItemPropertyV2Input) SetMStrDisableValueNil(b bool)`

 SetMStrDisableValueNil sets the value for MStrDisableValue to be an explicit nil

### UnsetMStrDisableValue
`func (o *ItemPropertyV2Input) UnsetMStrDisableValue()`

UnsetMStrDisableValue ensures that no value is present for MStrDisableValue, not even an explicit nil
### GetMStrLocTokenOverride

`func (o *ItemPropertyV2Input) GetMStrLocTokenOverride() string`

GetMStrLocTokenOverride returns the MStrLocTokenOverride field if non-nil, zero value otherwise.

### GetMStrLocTokenOverrideOk

`func (o *ItemPropertyV2Input) GetMStrLocTokenOverrideOk() (*string, bool)`

GetMStrLocTokenOverrideOk returns a tuple with the MStrLocTokenOverride field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMStrLocTokenOverride

`func (o *ItemPropertyV2Input) SetMStrLocTokenOverride(v string)`

SetMStrLocTokenOverride sets MStrLocTokenOverride field to given value.

### HasMStrLocTokenOverride

`func (o *ItemPropertyV2Input) HasMStrLocTokenOverride() bool`

HasMStrLocTokenOverride returns a boolean if a field has been set.

### SetMStrLocTokenOverrideNil

`func (o *ItemPropertyV2Input) SetMStrLocTokenOverrideNil(b bool)`

 SetMStrLocTokenOverrideNil sets the value for MStrLocTokenOverride to be an explicit nil

### UnsetMStrLocTokenOverride
`func (o *ItemPropertyV2Input) UnsetMStrLocTokenOverride()`

UnsetMStrLocTokenOverride ensures that no value is present for MStrLocTokenOverride, not even an explicit nil
### GetMEDisplayUnits

`func (o *ItemPropertyV2Input) GetMEDisplayUnits() string`

GetMEDisplayUnits returns the MEDisplayUnits field if non-nil, zero value otherwise.

### GetMEDisplayUnitsOk

`func (o *ItemPropertyV2Input) GetMEDisplayUnitsOk() (*string, bool)`

GetMEDisplayUnitsOk returns a tuple with the MEDisplayUnits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMEDisplayUnits

`func (o *ItemPropertyV2Input) SetMEDisplayUnits(v string)`

SetMEDisplayUnits sets MEDisplayUnits field to given value.

### HasMEDisplayUnits

`func (o *ItemPropertyV2Input) HasMEDisplayUnits() bool`

HasMEDisplayUnits returns a boolean if a field has been set.

### SetMEDisplayUnitsNil

`func (o *ItemPropertyV2Input) SetMEDisplayUnitsNil(b bool)`

 SetMEDisplayUnitsNil sets the value for MEDisplayUnits to be an explicit nil

### UnsetMEDisplayUnits
`func (o *ItemPropertyV2Input) UnsetMEDisplayUnits()`

UnsetMEDisplayUnits ensures that no value is present for MEDisplayUnits, not even an explicit nil
### GetScaleFunction

`func (o *ItemPropertyV2Input) GetScaleFunction() RawItemPropertyScaleFunctionSubclassV2Input`

GetScaleFunction returns the ScaleFunction field if non-nil, zero value otherwise.

### GetScaleFunctionOk

`func (o *ItemPropertyV2Input) GetScaleFunctionOk() (*RawItemPropertyScaleFunctionSubclassV2Input, bool)`

GetScaleFunctionOk returns a tuple with the ScaleFunction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScaleFunction

`func (o *ItemPropertyV2Input) SetScaleFunction(v RawItemPropertyScaleFunctionSubclassV2Input)`

SetScaleFunction sets ScaleFunction field to given value.

### HasScaleFunction

`func (o *ItemPropertyV2Input) HasScaleFunction() bool`

HasScaleFunction returns a boolean if a field has been set.

### SetScaleFunctionNil

`func (o *ItemPropertyV2Input) SetScaleFunctionNil(b bool)`

 SetScaleFunctionNil sets the value for ScaleFunction to be an explicit nil

### UnsetScaleFunction
`func (o *ItemPropertyV2Input) UnsetScaleFunction()`

UnsetScaleFunction ensures that no value is present for ScaleFunction, not even an explicit nil
### GetPrefix

`func (o *ItemPropertyV2Input) GetPrefix() string`

GetPrefix returns the Prefix field if non-nil, zero value otherwise.

### GetPrefixOk

`func (o *ItemPropertyV2Input) GetPrefixOk() (*string, bool)`

GetPrefixOk returns a tuple with the Prefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefix

`func (o *ItemPropertyV2Input) SetPrefix(v string)`

SetPrefix sets Prefix field to given value.

### HasPrefix

`func (o *ItemPropertyV2Input) HasPrefix() bool`

HasPrefix returns a boolean if a field has been set.

### SetPrefixNil

`func (o *ItemPropertyV2Input) SetPrefixNil(b bool)`

 SetPrefixNil sets the value for Prefix to be an explicit nil

### UnsetPrefix
`func (o *ItemPropertyV2Input) UnsetPrefix()`

UnsetPrefix ensures that no value is present for Prefix, not even an explicit nil
### GetLabel

`func (o *ItemPropertyV2Input) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *ItemPropertyV2Input) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *ItemPropertyV2Input) SetLabel(v string)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *ItemPropertyV2Input) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### SetLabelNil

`func (o *ItemPropertyV2Input) SetLabelNil(b bool)`

 SetLabelNil sets the value for Label to be an explicit nil

### UnsetLabel
`func (o *ItemPropertyV2Input) UnsetLabel()`

UnsetLabel ensures that no value is present for Label, not even an explicit nil
### GetPostfix

`func (o *ItemPropertyV2Input) GetPostfix() string`

GetPostfix returns the Postfix field if non-nil, zero value otherwise.

### GetPostfixOk

`func (o *ItemPropertyV2Input) GetPostfixOk() (*string, bool)`

GetPostfixOk returns a tuple with the Postfix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostfix

`func (o *ItemPropertyV2Input) SetPostfix(v string)`

SetPostfix sets Postfix field to given value.

### HasPostfix

`func (o *ItemPropertyV2Input) HasPostfix() bool`

HasPostfix returns a boolean if a field has been set.

### SetPostfixNil

`func (o *ItemPropertyV2Input) SetPostfixNil(b bool)`

 SetPostfixNil sets the value for Postfix to be an explicit nil

### UnsetPostfix
`func (o *ItemPropertyV2Input) UnsetPostfix()`

UnsetPostfix ensures that no value is present for Postfix, not even an explicit nil
### GetPostvalueLabel

`func (o *ItemPropertyV2Input) GetPostvalueLabel() string`

GetPostvalueLabel returns the PostvalueLabel field if non-nil, zero value otherwise.

### GetPostvalueLabelOk

`func (o *ItemPropertyV2Input) GetPostvalueLabelOk() (*string, bool)`

GetPostvalueLabelOk returns a tuple with the PostvalueLabel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostvalueLabel

`func (o *ItemPropertyV2Input) SetPostvalueLabel(v string)`

SetPostvalueLabel sets PostvalueLabel field to given value.

### HasPostvalueLabel

`func (o *ItemPropertyV2Input) HasPostvalueLabel() bool`

HasPostvalueLabel returns a boolean if a field has been set.

### SetPostvalueLabelNil

`func (o *ItemPropertyV2Input) SetPostvalueLabelNil(b bool)`

 SetPostvalueLabelNil sets the value for PostvalueLabel to be an explicit nil

### UnsetPostvalueLabel
`func (o *ItemPropertyV2Input) UnsetPostvalueLabel()`

UnsetPostvalueLabel ensures that no value is present for PostvalueLabel, not even an explicit nil
### GetConditional

`func (o *ItemPropertyV2Input) GetConditional() string`

GetConditional returns the Conditional field if non-nil, zero value otherwise.

### GetConditionalOk

`func (o *ItemPropertyV2Input) GetConditionalOk() (*string, bool)`

GetConditionalOk returns a tuple with the Conditional field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConditional

`func (o *ItemPropertyV2Input) SetConditional(v string)`

SetConditional sets Conditional field to given value.

### HasConditional

`func (o *ItemPropertyV2Input) HasConditional() bool`

HasConditional returns a boolean if a field has been set.

### SetConditionalNil

`func (o *ItemPropertyV2Input) SetConditionalNil(b bool)`

 SetConditionalNil sets the value for Conditional to be an explicit nil

### UnsetConditional
`func (o *ItemPropertyV2Input) UnsetConditional()`

UnsetConditional ensures that no value is present for Conditional, not even an explicit nil
### GetIcon

`func (o *ItemPropertyV2Input) GetIcon() string`

GetIcon returns the Icon field if non-nil, zero value otherwise.

### GetIconOk

`func (o *ItemPropertyV2Input) GetIconOk() (*string, bool)`

GetIconOk returns a tuple with the Icon field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIcon

`func (o *ItemPropertyV2Input) SetIcon(v string)`

SetIcon sets Icon field to given value.

### HasIcon

`func (o *ItemPropertyV2Input) HasIcon() bool`

HasIcon returns a boolean if a field has been set.

### SetIconNil

`func (o *ItemPropertyV2Input) SetIconNil(b bool)`

 SetIconNil sets the value for Icon to be an explicit nil

### UnsetIcon
`func (o *ItemPropertyV2Input) UnsetIcon()`

UnsetIcon ensures that no value is present for Icon, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


