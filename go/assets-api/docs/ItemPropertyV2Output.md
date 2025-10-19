# ItemPropertyV2Output

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Value** | Pointer to [**NullableValue1**](Value1.md) |  | [optional] 
**CanSetTokenOverride** | Pointer to **NullableBool** |  | [optional] 
**ProvidedPropertyType** | Pointer to **NullableString** |  | [optional] 
**CssClass** | Pointer to **NullableString** |  | [optional] 
**UsageFlags** | Pointer to [**NullableUsageFlags**](UsageFlags.md) |  | [optional] 
**NegativeAttribute** | Pointer to **NullableBool** |  | [optional] 
**DisableValue** | Pointer to **NullableString** |  | [optional] 
**LocTokenOverride** | Pointer to **NullableString** |  | [optional] 
**DisplayUnits** | Pointer to **NullableString** |  | [optional] 
**IconPath** | Pointer to **NullableString** |  | [optional] 
**ScaleFunction** | Pointer to [**NullableRawItemPropertyScaleFunctionSubclassV2Output**](RawItemPropertyScaleFunctionSubclassV2Output.md) |  | [optional] 
**Prefix** | Pointer to **NullableString** |  | [optional] 
**Label** | Pointer to **NullableString** |  | [optional] 
**Postfix** | Pointer to **NullableString** |  | [optional] 
**PostvalueLabel** | Pointer to **NullableString** |  | [optional] 
**Conditional** | Pointer to **NullableString** |  | [optional] 
**Icon** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewItemPropertyV2Output

`func NewItemPropertyV2Output() *ItemPropertyV2Output`

NewItemPropertyV2Output instantiates a new ItemPropertyV2Output object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewItemPropertyV2OutputWithDefaults

`func NewItemPropertyV2OutputWithDefaults() *ItemPropertyV2Output`

NewItemPropertyV2OutputWithDefaults instantiates a new ItemPropertyV2Output object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetValue

`func (o *ItemPropertyV2Output) GetValue() Value1`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *ItemPropertyV2Output) GetValueOk() (*Value1, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *ItemPropertyV2Output) SetValue(v Value1)`

SetValue sets Value field to given value.

### HasValue

`func (o *ItemPropertyV2Output) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValueNil

`func (o *ItemPropertyV2Output) SetValueNil(b bool)`

 SetValueNil sets the value for Value to be an explicit nil

### UnsetValue
`func (o *ItemPropertyV2Output) UnsetValue()`

UnsetValue ensures that no value is present for Value, not even an explicit nil
### GetCanSetTokenOverride

`func (o *ItemPropertyV2Output) GetCanSetTokenOverride() bool`

GetCanSetTokenOverride returns the CanSetTokenOverride field if non-nil, zero value otherwise.

### GetCanSetTokenOverrideOk

`func (o *ItemPropertyV2Output) GetCanSetTokenOverrideOk() (*bool, bool)`

GetCanSetTokenOverrideOk returns a tuple with the CanSetTokenOverride field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCanSetTokenOverride

`func (o *ItemPropertyV2Output) SetCanSetTokenOverride(v bool)`

SetCanSetTokenOverride sets CanSetTokenOverride field to given value.

### HasCanSetTokenOverride

`func (o *ItemPropertyV2Output) HasCanSetTokenOverride() bool`

HasCanSetTokenOverride returns a boolean if a field has been set.

### SetCanSetTokenOverrideNil

`func (o *ItemPropertyV2Output) SetCanSetTokenOverrideNil(b bool)`

 SetCanSetTokenOverrideNil sets the value for CanSetTokenOverride to be an explicit nil

### UnsetCanSetTokenOverride
`func (o *ItemPropertyV2Output) UnsetCanSetTokenOverride()`

UnsetCanSetTokenOverride ensures that no value is present for CanSetTokenOverride, not even an explicit nil
### GetProvidedPropertyType

`func (o *ItemPropertyV2Output) GetProvidedPropertyType() string`

GetProvidedPropertyType returns the ProvidedPropertyType field if non-nil, zero value otherwise.

### GetProvidedPropertyTypeOk

`func (o *ItemPropertyV2Output) GetProvidedPropertyTypeOk() (*string, bool)`

GetProvidedPropertyTypeOk returns a tuple with the ProvidedPropertyType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvidedPropertyType

`func (o *ItemPropertyV2Output) SetProvidedPropertyType(v string)`

SetProvidedPropertyType sets ProvidedPropertyType field to given value.

### HasProvidedPropertyType

`func (o *ItemPropertyV2Output) HasProvidedPropertyType() bool`

HasProvidedPropertyType returns a boolean if a field has been set.

### SetProvidedPropertyTypeNil

`func (o *ItemPropertyV2Output) SetProvidedPropertyTypeNil(b bool)`

 SetProvidedPropertyTypeNil sets the value for ProvidedPropertyType to be an explicit nil

### UnsetProvidedPropertyType
`func (o *ItemPropertyV2Output) UnsetProvidedPropertyType()`

UnsetProvidedPropertyType ensures that no value is present for ProvidedPropertyType, not even an explicit nil
### GetCssClass

`func (o *ItemPropertyV2Output) GetCssClass() string`

GetCssClass returns the CssClass field if non-nil, zero value otherwise.

### GetCssClassOk

`func (o *ItemPropertyV2Output) GetCssClassOk() (*string, bool)`

GetCssClassOk returns a tuple with the CssClass field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCssClass

`func (o *ItemPropertyV2Output) SetCssClass(v string)`

SetCssClass sets CssClass field to given value.

### HasCssClass

`func (o *ItemPropertyV2Output) HasCssClass() bool`

HasCssClass returns a boolean if a field has been set.

### SetCssClassNil

`func (o *ItemPropertyV2Output) SetCssClassNil(b bool)`

 SetCssClassNil sets the value for CssClass to be an explicit nil

### UnsetCssClass
`func (o *ItemPropertyV2Output) UnsetCssClass()`

UnsetCssClass ensures that no value is present for CssClass, not even an explicit nil
### GetUsageFlags

`func (o *ItemPropertyV2Output) GetUsageFlags() UsageFlags`

GetUsageFlags returns the UsageFlags field if non-nil, zero value otherwise.

### GetUsageFlagsOk

`func (o *ItemPropertyV2Output) GetUsageFlagsOk() (*UsageFlags, bool)`

GetUsageFlagsOk returns a tuple with the UsageFlags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsageFlags

`func (o *ItemPropertyV2Output) SetUsageFlags(v UsageFlags)`

SetUsageFlags sets UsageFlags field to given value.

### HasUsageFlags

`func (o *ItemPropertyV2Output) HasUsageFlags() bool`

HasUsageFlags returns a boolean if a field has been set.

### SetUsageFlagsNil

`func (o *ItemPropertyV2Output) SetUsageFlagsNil(b bool)`

 SetUsageFlagsNil sets the value for UsageFlags to be an explicit nil

### UnsetUsageFlags
`func (o *ItemPropertyV2Output) UnsetUsageFlags()`

UnsetUsageFlags ensures that no value is present for UsageFlags, not even an explicit nil
### GetNegativeAttribute

`func (o *ItemPropertyV2Output) GetNegativeAttribute() bool`

GetNegativeAttribute returns the NegativeAttribute field if non-nil, zero value otherwise.

### GetNegativeAttributeOk

`func (o *ItemPropertyV2Output) GetNegativeAttributeOk() (*bool, bool)`

GetNegativeAttributeOk returns a tuple with the NegativeAttribute field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNegativeAttribute

`func (o *ItemPropertyV2Output) SetNegativeAttribute(v bool)`

SetNegativeAttribute sets NegativeAttribute field to given value.

### HasNegativeAttribute

`func (o *ItemPropertyV2Output) HasNegativeAttribute() bool`

HasNegativeAttribute returns a boolean if a field has been set.

### SetNegativeAttributeNil

`func (o *ItemPropertyV2Output) SetNegativeAttributeNil(b bool)`

 SetNegativeAttributeNil sets the value for NegativeAttribute to be an explicit nil

### UnsetNegativeAttribute
`func (o *ItemPropertyV2Output) UnsetNegativeAttribute()`

UnsetNegativeAttribute ensures that no value is present for NegativeAttribute, not even an explicit nil
### GetDisableValue

`func (o *ItemPropertyV2Output) GetDisableValue() string`

GetDisableValue returns the DisableValue field if non-nil, zero value otherwise.

### GetDisableValueOk

`func (o *ItemPropertyV2Output) GetDisableValueOk() (*string, bool)`

GetDisableValueOk returns a tuple with the DisableValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisableValue

`func (o *ItemPropertyV2Output) SetDisableValue(v string)`

SetDisableValue sets DisableValue field to given value.

### HasDisableValue

`func (o *ItemPropertyV2Output) HasDisableValue() bool`

HasDisableValue returns a boolean if a field has been set.

### SetDisableValueNil

`func (o *ItemPropertyV2Output) SetDisableValueNil(b bool)`

 SetDisableValueNil sets the value for DisableValue to be an explicit nil

### UnsetDisableValue
`func (o *ItemPropertyV2Output) UnsetDisableValue()`

UnsetDisableValue ensures that no value is present for DisableValue, not even an explicit nil
### GetLocTokenOverride

`func (o *ItemPropertyV2Output) GetLocTokenOverride() string`

GetLocTokenOverride returns the LocTokenOverride field if non-nil, zero value otherwise.

### GetLocTokenOverrideOk

`func (o *ItemPropertyV2Output) GetLocTokenOverrideOk() (*string, bool)`

GetLocTokenOverrideOk returns a tuple with the LocTokenOverride field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocTokenOverride

`func (o *ItemPropertyV2Output) SetLocTokenOverride(v string)`

SetLocTokenOverride sets LocTokenOverride field to given value.

### HasLocTokenOverride

`func (o *ItemPropertyV2Output) HasLocTokenOverride() bool`

HasLocTokenOverride returns a boolean if a field has been set.

### SetLocTokenOverrideNil

`func (o *ItemPropertyV2Output) SetLocTokenOverrideNil(b bool)`

 SetLocTokenOverrideNil sets the value for LocTokenOverride to be an explicit nil

### UnsetLocTokenOverride
`func (o *ItemPropertyV2Output) UnsetLocTokenOverride()`

UnsetLocTokenOverride ensures that no value is present for LocTokenOverride, not even an explicit nil
### GetDisplayUnits

`func (o *ItemPropertyV2Output) GetDisplayUnits() string`

GetDisplayUnits returns the DisplayUnits field if non-nil, zero value otherwise.

### GetDisplayUnitsOk

`func (o *ItemPropertyV2Output) GetDisplayUnitsOk() (*string, bool)`

GetDisplayUnitsOk returns a tuple with the DisplayUnits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayUnits

`func (o *ItemPropertyV2Output) SetDisplayUnits(v string)`

SetDisplayUnits sets DisplayUnits field to given value.

### HasDisplayUnits

`func (o *ItemPropertyV2Output) HasDisplayUnits() bool`

HasDisplayUnits returns a boolean if a field has been set.

### SetDisplayUnitsNil

`func (o *ItemPropertyV2Output) SetDisplayUnitsNil(b bool)`

 SetDisplayUnitsNil sets the value for DisplayUnits to be an explicit nil

### UnsetDisplayUnits
`func (o *ItemPropertyV2Output) UnsetDisplayUnits()`

UnsetDisplayUnits ensures that no value is present for DisplayUnits, not even an explicit nil
### GetIconPath

`func (o *ItemPropertyV2Output) GetIconPath() string`

GetIconPath returns the IconPath field if non-nil, zero value otherwise.

### GetIconPathOk

`func (o *ItemPropertyV2Output) GetIconPathOk() (*string, bool)`

GetIconPathOk returns a tuple with the IconPath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIconPath

`func (o *ItemPropertyV2Output) SetIconPath(v string)`

SetIconPath sets IconPath field to given value.

### HasIconPath

`func (o *ItemPropertyV2Output) HasIconPath() bool`

HasIconPath returns a boolean if a field has been set.

### SetIconPathNil

`func (o *ItemPropertyV2Output) SetIconPathNil(b bool)`

 SetIconPathNil sets the value for IconPath to be an explicit nil

### UnsetIconPath
`func (o *ItemPropertyV2Output) UnsetIconPath()`

UnsetIconPath ensures that no value is present for IconPath, not even an explicit nil
### GetScaleFunction

`func (o *ItemPropertyV2Output) GetScaleFunction() RawItemPropertyScaleFunctionSubclassV2Output`

GetScaleFunction returns the ScaleFunction field if non-nil, zero value otherwise.

### GetScaleFunctionOk

`func (o *ItemPropertyV2Output) GetScaleFunctionOk() (*RawItemPropertyScaleFunctionSubclassV2Output, bool)`

GetScaleFunctionOk returns a tuple with the ScaleFunction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScaleFunction

`func (o *ItemPropertyV2Output) SetScaleFunction(v RawItemPropertyScaleFunctionSubclassV2Output)`

SetScaleFunction sets ScaleFunction field to given value.

### HasScaleFunction

`func (o *ItemPropertyV2Output) HasScaleFunction() bool`

HasScaleFunction returns a boolean if a field has been set.

### SetScaleFunctionNil

`func (o *ItemPropertyV2Output) SetScaleFunctionNil(b bool)`

 SetScaleFunctionNil sets the value for ScaleFunction to be an explicit nil

### UnsetScaleFunction
`func (o *ItemPropertyV2Output) UnsetScaleFunction()`

UnsetScaleFunction ensures that no value is present for ScaleFunction, not even an explicit nil
### GetPrefix

`func (o *ItemPropertyV2Output) GetPrefix() string`

GetPrefix returns the Prefix field if non-nil, zero value otherwise.

### GetPrefixOk

`func (o *ItemPropertyV2Output) GetPrefixOk() (*string, bool)`

GetPrefixOk returns a tuple with the Prefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefix

`func (o *ItemPropertyV2Output) SetPrefix(v string)`

SetPrefix sets Prefix field to given value.

### HasPrefix

`func (o *ItemPropertyV2Output) HasPrefix() bool`

HasPrefix returns a boolean if a field has been set.

### SetPrefixNil

`func (o *ItemPropertyV2Output) SetPrefixNil(b bool)`

 SetPrefixNil sets the value for Prefix to be an explicit nil

### UnsetPrefix
`func (o *ItemPropertyV2Output) UnsetPrefix()`

UnsetPrefix ensures that no value is present for Prefix, not even an explicit nil
### GetLabel

`func (o *ItemPropertyV2Output) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *ItemPropertyV2Output) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *ItemPropertyV2Output) SetLabel(v string)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *ItemPropertyV2Output) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### SetLabelNil

`func (o *ItemPropertyV2Output) SetLabelNil(b bool)`

 SetLabelNil sets the value for Label to be an explicit nil

### UnsetLabel
`func (o *ItemPropertyV2Output) UnsetLabel()`

UnsetLabel ensures that no value is present for Label, not even an explicit nil
### GetPostfix

`func (o *ItemPropertyV2Output) GetPostfix() string`

GetPostfix returns the Postfix field if non-nil, zero value otherwise.

### GetPostfixOk

`func (o *ItemPropertyV2Output) GetPostfixOk() (*string, bool)`

GetPostfixOk returns a tuple with the Postfix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostfix

`func (o *ItemPropertyV2Output) SetPostfix(v string)`

SetPostfix sets Postfix field to given value.

### HasPostfix

`func (o *ItemPropertyV2Output) HasPostfix() bool`

HasPostfix returns a boolean if a field has been set.

### SetPostfixNil

`func (o *ItemPropertyV2Output) SetPostfixNil(b bool)`

 SetPostfixNil sets the value for Postfix to be an explicit nil

### UnsetPostfix
`func (o *ItemPropertyV2Output) UnsetPostfix()`

UnsetPostfix ensures that no value is present for Postfix, not even an explicit nil
### GetPostvalueLabel

`func (o *ItemPropertyV2Output) GetPostvalueLabel() string`

GetPostvalueLabel returns the PostvalueLabel field if non-nil, zero value otherwise.

### GetPostvalueLabelOk

`func (o *ItemPropertyV2Output) GetPostvalueLabelOk() (*string, bool)`

GetPostvalueLabelOk returns a tuple with the PostvalueLabel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostvalueLabel

`func (o *ItemPropertyV2Output) SetPostvalueLabel(v string)`

SetPostvalueLabel sets PostvalueLabel field to given value.

### HasPostvalueLabel

`func (o *ItemPropertyV2Output) HasPostvalueLabel() bool`

HasPostvalueLabel returns a boolean if a field has been set.

### SetPostvalueLabelNil

`func (o *ItemPropertyV2Output) SetPostvalueLabelNil(b bool)`

 SetPostvalueLabelNil sets the value for PostvalueLabel to be an explicit nil

### UnsetPostvalueLabel
`func (o *ItemPropertyV2Output) UnsetPostvalueLabel()`

UnsetPostvalueLabel ensures that no value is present for PostvalueLabel, not even an explicit nil
### GetConditional

`func (o *ItemPropertyV2Output) GetConditional() string`

GetConditional returns the Conditional field if non-nil, zero value otherwise.

### GetConditionalOk

`func (o *ItemPropertyV2Output) GetConditionalOk() (*string, bool)`

GetConditionalOk returns a tuple with the Conditional field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConditional

`func (o *ItemPropertyV2Output) SetConditional(v string)`

SetConditional sets Conditional field to given value.

### HasConditional

`func (o *ItemPropertyV2Output) HasConditional() bool`

HasConditional returns a boolean if a field has been set.

### SetConditionalNil

`func (o *ItemPropertyV2Output) SetConditionalNil(b bool)`

 SetConditionalNil sets the value for Conditional to be an explicit nil

### UnsetConditional
`func (o *ItemPropertyV2Output) UnsetConditional()`

UnsetConditional ensures that no value is present for Conditional, not even an explicit nil
### GetIcon

`func (o *ItemPropertyV2Output) GetIcon() string`

GetIcon returns the Icon field if non-nil, zero value otherwise.

### GetIconOk

`func (o *ItemPropertyV2Output) GetIconOk() (*string, bool)`

GetIconOk returns a tuple with the Icon field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIcon

`func (o *ItemPropertyV2Output) SetIcon(v string)`

SetIcon sets Icon field to given value.

### HasIcon

`func (o *ItemPropertyV2Output) HasIcon() bool`

HasIcon returns a boolean if a field has been set.

### SetIconNil

`func (o *ItemPropertyV2Output) SetIconNil(b bool)`

 SetIconNil sets the value for Icon to be an explicit nil

### UnsetIcon
`func (o *ItemPropertyV2Output) UnsetIcon()`

UnsetIcon ensures that no value is present for Icon, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


