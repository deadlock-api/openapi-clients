# ItemPropertyV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Value** | Pointer to [**NullableValue1**](Value1.md) |  | [optional] 
**StreetBrawlValue** | Pointer to [**NullableStreetBrawlValue**](StreetBrawlValue.md) |  | [optional] 
**CanSetTokenOverride** | Pointer to **NullableBool** |  | [optional] 
**ProvidedPropertyType** | Pointer to **NullableString** |  | [optional] 
**CssClass** | Pointer to **NullableString** |  | [optional] 
**UsageFlags** | Pointer to [**NullableUsageFlags**](UsageFlags.md) |  | [optional] 
**NegativeAttribute** | Pointer to **NullableBool** |  | [optional] 
**DisableValue** | Pointer to **NullableString** |  | [optional] 
**LocTokenOverride** | Pointer to **NullableString** |  | [optional] 
**DisplayUnits** | Pointer to **NullableString** |  | [optional] 
**IconPath** | Pointer to **NullableString** |  | [optional] 
**ScaleFunction** | Pointer to [**NullableRawItemPropertyScaleFunctionSubclassV2**](RawItemPropertyScaleFunctionSubclassV2.md) |  | [optional] 
**Prefix** | Pointer to **NullableString** |  | [optional] 
**Label** | Pointer to **NullableString** |  | [optional] 
**Postfix** | Pointer to **NullableString** |  | [optional] 
**PostvalueLabel** | Pointer to **NullableString** |  | [optional] 
**Conditional** | Pointer to **NullableString** |  | [optional] 
**Icon** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewItemPropertyV2

`func NewItemPropertyV2() *ItemPropertyV2`

NewItemPropertyV2 instantiates a new ItemPropertyV2 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewItemPropertyV2WithDefaults

`func NewItemPropertyV2WithDefaults() *ItemPropertyV2`

NewItemPropertyV2WithDefaults instantiates a new ItemPropertyV2 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetValue

`func (o *ItemPropertyV2) GetValue() Value1`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *ItemPropertyV2) GetValueOk() (*Value1, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *ItemPropertyV2) SetValue(v Value1)`

SetValue sets Value field to given value.

### HasValue

`func (o *ItemPropertyV2) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValueNil

`func (o *ItemPropertyV2) SetValueNil(b bool)`

 SetValueNil sets the value for Value to be an explicit nil

### UnsetValue
`func (o *ItemPropertyV2) UnsetValue()`

UnsetValue ensures that no value is present for Value, not even an explicit nil
### GetStreetBrawlValue

`func (o *ItemPropertyV2) GetStreetBrawlValue() StreetBrawlValue`

GetStreetBrawlValue returns the StreetBrawlValue field if non-nil, zero value otherwise.

### GetStreetBrawlValueOk

`func (o *ItemPropertyV2) GetStreetBrawlValueOk() (*StreetBrawlValue, bool)`

GetStreetBrawlValueOk returns a tuple with the StreetBrawlValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStreetBrawlValue

`func (o *ItemPropertyV2) SetStreetBrawlValue(v StreetBrawlValue)`

SetStreetBrawlValue sets StreetBrawlValue field to given value.

### HasStreetBrawlValue

`func (o *ItemPropertyV2) HasStreetBrawlValue() bool`

HasStreetBrawlValue returns a boolean if a field has been set.

### SetStreetBrawlValueNil

`func (o *ItemPropertyV2) SetStreetBrawlValueNil(b bool)`

 SetStreetBrawlValueNil sets the value for StreetBrawlValue to be an explicit nil

### UnsetStreetBrawlValue
`func (o *ItemPropertyV2) UnsetStreetBrawlValue()`

UnsetStreetBrawlValue ensures that no value is present for StreetBrawlValue, not even an explicit nil
### GetCanSetTokenOverride

`func (o *ItemPropertyV2) GetCanSetTokenOverride() bool`

GetCanSetTokenOverride returns the CanSetTokenOverride field if non-nil, zero value otherwise.

### GetCanSetTokenOverrideOk

`func (o *ItemPropertyV2) GetCanSetTokenOverrideOk() (*bool, bool)`

GetCanSetTokenOverrideOk returns a tuple with the CanSetTokenOverride field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCanSetTokenOverride

`func (o *ItemPropertyV2) SetCanSetTokenOverride(v bool)`

SetCanSetTokenOverride sets CanSetTokenOverride field to given value.

### HasCanSetTokenOverride

`func (o *ItemPropertyV2) HasCanSetTokenOverride() bool`

HasCanSetTokenOverride returns a boolean if a field has been set.

### SetCanSetTokenOverrideNil

`func (o *ItemPropertyV2) SetCanSetTokenOverrideNil(b bool)`

 SetCanSetTokenOverrideNil sets the value for CanSetTokenOverride to be an explicit nil

### UnsetCanSetTokenOverride
`func (o *ItemPropertyV2) UnsetCanSetTokenOverride()`

UnsetCanSetTokenOverride ensures that no value is present for CanSetTokenOverride, not even an explicit nil
### GetProvidedPropertyType

`func (o *ItemPropertyV2) GetProvidedPropertyType() string`

GetProvidedPropertyType returns the ProvidedPropertyType field if non-nil, zero value otherwise.

### GetProvidedPropertyTypeOk

`func (o *ItemPropertyV2) GetProvidedPropertyTypeOk() (*string, bool)`

GetProvidedPropertyTypeOk returns a tuple with the ProvidedPropertyType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvidedPropertyType

`func (o *ItemPropertyV2) SetProvidedPropertyType(v string)`

SetProvidedPropertyType sets ProvidedPropertyType field to given value.

### HasProvidedPropertyType

`func (o *ItemPropertyV2) HasProvidedPropertyType() bool`

HasProvidedPropertyType returns a boolean if a field has been set.

### SetProvidedPropertyTypeNil

`func (o *ItemPropertyV2) SetProvidedPropertyTypeNil(b bool)`

 SetProvidedPropertyTypeNil sets the value for ProvidedPropertyType to be an explicit nil

### UnsetProvidedPropertyType
`func (o *ItemPropertyV2) UnsetProvidedPropertyType()`

UnsetProvidedPropertyType ensures that no value is present for ProvidedPropertyType, not even an explicit nil
### GetCssClass

`func (o *ItemPropertyV2) GetCssClass() string`

GetCssClass returns the CssClass field if non-nil, zero value otherwise.

### GetCssClassOk

`func (o *ItemPropertyV2) GetCssClassOk() (*string, bool)`

GetCssClassOk returns a tuple with the CssClass field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCssClass

`func (o *ItemPropertyV2) SetCssClass(v string)`

SetCssClass sets CssClass field to given value.

### HasCssClass

`func (o *ItemPropertyV2) HasCssClass() bool`

HasCssClass returns a boolean if a field has been set.

### SetCssClassNil

`func (o *ItemPropertyV2) SetCssClassNil(b bool)`

 SetCssClassNil sets the value for CssClass to be an explicit nil

### UnsetCssClass
`func (o *ItemPropertyV2) UnsetCssClass()`

UnsetCssClass ensures that no value is present for CssClass, not even an explicit nil
### GetUsageFlags

`func (o *ItemPropertyV2) GetUsageFlags() UsageFlags`

GetUsageFlags returns the UsageFlags field if non-nil, zero value otherwise.

### GetUsageFlagsOk

`func (o *ItemPropertyV2) GetUsageFlagsOk() (*UsageFlags, bool)`

GetUsageFlagsOk returns a tuple with the UsageFlags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsageFlags

`func (o *ItemPropertyV2) SetUsageFlags(v UsageFlags)`

SetUsageFlags sets UsageFlags field to given value.

### HasUsageFlags

`func (o *ItemPropertyV2) HasUsageFlags() bool`

HasUsageFlags returns a boolean if a field has been set.

### SetUsageFlagsNil

`func (o *ItemPropertyV2) SetUsageFlagsNil(b bool)`

 SetUsageFlagsNil sets the value for UsageFlags to be an explicit nil

### UnsetUsageFlags
`func (o *ItemPropertyV2) UnsetUsageFlags()`

UnsetUsageFlags ensures that no value is present for UsageFlags, not even an explicit nil
### GetNegativeAttribute

`func (o *ItemPropertyV2) GetNegativeAttribute() bool`

GetNegativeAttribute returns the NegativeAttribute field if non-nil, zero value otherwise.

### GetNegativeAttributeOk

`func (o *ItemPropertyV2) GetNegativeAttributeOk() (*bool, bool)`

GetNegativeAttributeOk returns a tuple with the NegativeAttribute field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNegativeAttribute

`func (o *ItemPropertyV2) SetNegativeAttribute(v bool)`

SetNegativeAttribute sets NegativeAttribute field to given value.

### HasNegativeAttribute

`func (o *ItemPropertyV2) HasNegativeAttribute() bool`

HasNegativeAttribute returns a boolean if a field has been set.

### SetNegativeAttributeNil

`func (o *ItemPropertyV2) SetNegativeAttributeNil(b bool)`

 SetNegativeAttributeNil sets the value for NegativeAttribute to be an explicit nil

### UnsetNegativeAttribute
`func (o *ItemPropertyV2) UnsetNegativeAttribute()`

UnsetNegativeAttribute ensures that no value is present for NegativeAttribute, not even an explicit nil
### GetDisableValue

`func (o *ItemPropertyV2) GetDisableValue() string`

GetDisableValue returns the DisableValue field if non-nil, zero value otherwise.

### GetDisableValueOk

`func (o *ItemPropertyV2) GetDisableValueOk() (*string, bool)`

GetDisableValueOk returns a tuple with the DisableValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisableValue

`func (o *ItemPropertyV2) SetDisableValue(v string)`

SetDisableValue sets DisableValue field to given value.

### HasDisableValue

`func (o *ItemPropertyV2) HasDisableValue() bool`

HasDisableValue returns a boolean if a field has been set.

### SetDisableValueNil

`func (o *ItemPropertyV2) SetDisableValueNil(b bool)`

 SetDisableValueNil sets the value for DisableValue to be an explicit nil

### UnsetDisableValue
`func (o *ItemPropertyV2) UnsetDisableValue()`

UnsetDisableValue ensures that no value is present for DisableValue, not even an explicit nil
### GetLocTokenOverride

`func (o *ItemPropertyV2) GetLocTokenOverride() string`

GetLocTokenOverride returns the LocTokenOverride field if non-nil, zero value otherwise.

### GetLocTokenOverrideOk

`func (o *ItemPropertyV2) GetLocTokenOverrideOk() (*string, bool)`

GetLocTokenOverrideOk returns a tuple with the LocTokenOverride field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocTokenOverride

`func (o *ItemPropertyV2) SetLocTokenOverride(v string)`

SetLocTokenOverride sets LocTokenOverride field to given value.

### HasLocTokenOverride

`func (o *ItemPropertyV2) HasLocTokenOverride() bool`

HasLocTokenOverride returns a boolean if a field has been set.

### SetLocTokenOverrideNil

`func (o *ItemPropertyV2) SetLocTokenOverrideNil(b bool)`

 SetLocTokenOverrideNil sets the value for LocTokenOverride to be an explicit nil

### UnsetLocTokenOverride
`func (o *ItemPropertyV2) UnsetLocTokenOverride()`

UnsetLocTokenOverride ensures that no value is present for LocTokenOverride, not even an explicit nil
### GetDisplayUnits

`func (o *ItemPropertyV2) GetDisplayUnits() string`

GetDisplayUnits returns the DisplayUnits field if non-nil, zero value otherwise.

### GetDisplayUnitsOk

`func (o *ItemPropertyV2) GetDisplayUnitsOk() (*string, bool)`

GetDisplayUnitsOk returns a tuple with the DisplayUnits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayUnits

`func (o *ItemPropertyV2) SetDisplayUnits(v string)`

SetDisplayUnits sets DisplayUnits field to given value.

### HasDisplayUnits

`func (o *ItemPropertyV2) HasDisplayUnits() bool`

HasDisplayUnits returns a boolean if a field has been set.

### SetDisplayUnitsNil

`func (o *ItemPropertyV2) SetDisplayUnitsNil(b bool)`

 SetDisplayUnitsNil sets the value for DisplayUnits to be an explicit nil

### UnsetDisplayUnits
`func (o *ItemPropertyV2) UnsetDisplayUnits()`

UnsetDisplayUnits ensures that no value is present for DisplayUnits, not even an explicit nil
### GetIconPath

`func (o *ItemPropertyV2) GetIconPath() string`

GetIconPath returns the IconPath field if non-nil, zero value otherwise.

### GetIconPathOk

`func (o *ItemPropertyV2) GetIconPathOk() (*string, bool)`

GetIconPathOk returns a tuple with the IconPath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIconPath

`func (o *ItemPropertyV2) SetIconPath(v string)`

SetIconPath sets IconPath field to given value.

### HasIconPath

`func (o *ItemPropertyV2) HasIconPath() bool`

HasIconPath returns a boolean if a field has been set.

### SetIconPathNil

`func (o *ItemPropertyV2) SetIconPathNil(b bool)`

 SetIconPathNil sets the value for IconPath to be an explicit nil

### UnsetIconPath
`func (o *ItemPropertyV2) UnsetIconPath()`

UnsetIconPath ensures that no value is present for IconPath, not even an explicit nil
### GetScaleFunction

`func (o *ItemPropertyV2) GetScaleFunction() RawItemPropertyScaleFunctionSubclassV2`

GetScaleFunction returns the ScaleFunction field if non-nil, zero value otherwise.

### GetScaleFunctionOk

`func (o *ItemPropertyV2) GetScaleFunctionOk() (*RawItemPropertyScaleFunctionSubclassV2, bool)`

GetScaleFunctionOk returns a tuple with the ScaleFunction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScaleFunction

`func (o *ItemPropertyV2) SetScaleFunction(v RawItemPropertyScaleFunctionSubclassV2)`

SetScaleFunction sets ScaleFunction field to given value.

### HasScaleFunction

`func (o *ItemPropertyV2) HasScaleFunction() bool`

HasScaleFunction returns a boolean if a field has been set.

### SetScaleFunctionNil

`func (o *ItemPropertyV2) SetScaleFunctionNil(b bool)`

 SetScaleFunctionNil sets the value for ScaleFunction to be an explicit nil

### UnsetScaleFunction
`func (o *ItemPropertyV2) UnsetScaleFunction()`

UnsetScaleFunction ensures that no value is present for ScaleFunction, not even an explicit nil
### GetPrefix

`func (o *ItemPropertyV2) GetPrefix() string`

GetPrefix returns the Prefix field if non-nil, zero value otherwise.

### GetPrefixOk

`func (o *ItemPropertyV2) GetPrefixOk() (*string, bool)`

GetPrefixOk returns a tuple with the Prefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefix

`func (o *ItemPropertyV2) SetPrefix(v string)`

SetPrefix sets Prefix field to given value.

### HasPrefix

`func (o *ItemPropertyV2) HasPrefix() bool`

HasPrefix returns a boolean if a field has been set.

### SetPrefixNil

`func (o *ItemPropertyV2) SetPrefixNil(b bool)`

 SetPrefixNil sets the value for Prefix to be an explicit nil

### UnsetPrefix
`func (o *ItemPropertyV2) UnsetPrefix()`

UnsetPrefix ensures that no value is present for Prefix, not even an explicit nil
### GetLabel

`func (o *ItemPropertyV2) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *ItemPropertyV2) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *ItemPropertyV2) SetLabel(v string)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *ItemPropertyV2) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### SetLabelNil

`func (o *ItemPropertyV2) SetLabelNil(b bool)`

 SetLabelNil sets the value for Label to be an explicit nil

### UnsetLabel
`func (o *ItemPropertyV2) UnsetLabel()`

UnsetLabel ensures that no value is present for Label, not even an explicit nil
### GetPostfix

`func (o *ItemPropertyV2) GetPostfix() string`

GetPostfix returns the Postfix field if non-nil, zero value otherwise.

### GetPostfixOk

`func (o *ItemPropertyV2) GetPostfixOk() (*string, bool)`

GetPostfixOk returns a tuple with the Postfix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostfix

`func (o *ItemPropertyV2) SetPostfix(v string)`

SetPostfix sets Postfix field to given value.

### HasPostfix

`func (o *ItemPropertyV2) HasPostfix() bool`

HasPostfix returns a boolean if a field has been set.

### SetPostfixNil

`func (o *ItemPropertyV2) SetPostfixNil(b bool)`

 SetPostfixNil sets the value for Postfix to be an explicit nil

### UnsetPostfix
`func (o *ItemPropertyV2) UnsetPostfix()`

UnsetPostfix ensures that no value is present for Postfix, not even an explicit nil
### GetPostvalueLabel

`func (o *ItemPropertyV2) GetPostvalueLabel() string`

GetPostvalueLabel returns the PostvalueLabel field if non-nil, zero value otherwise.

### GetPostvalueLabelOk

`func (o *ItemPropertyV2) GetPostvalueLabelOk() (*string, bool)`

GetPostvalueLabelOk returns a tuple with the PostvalueLabel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostvalueLabel

`func (o *ItemPropertyV2) SetPostvalueLabel(v string)`

SetPostvalueLabel sets PostvalueLabel field to given value.

### HasPostvalueLabel

`func (o *ItemPropertyV2) HasPostvalueLabel() bool`

HasPostvalueLabel returns a boolean if a field has been set.

### SetPostvalueLabelNil

`func (o *ItemPropertyV2) SetPostvalueLabelNil(b bool)`

 SetPostvalueLabelNil sets the value for PostvalueLabel to be an explicit nil

### UnsetPostvalueLabel
`func (o *ItemPropertyV2) UnsetPostvalueLabel()`

UnsetPostvalueLabel ensures that no value is present for PostvalueLabel, not even an explicit nil
### GetConditional

`func (o *ItemPropertyV2) GetConditional() string`

GetConditional returns the Conditional field if non-nil, zero value otherwise.

### GetConditionalOk

`func (o *ItemPropertyV2) GetConditionalOk() (*string, bool)`

GetConditionalOk returns a tuple with the Conditional field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConditional

`func (o *ItemPropertyV2) SetConditional(v string)`

SetConditional sets Conditional field to given value.

### HasConditional

`func (o *ItemPropertyV2) HasConditional() bool`

HasConditional returns a boolean if a field has been set.

### SetConditionalNil

`func (o *ItemPropertyV2) SetConditionalNil(b bool)`

 SetConditionalNil sets the value for Conditional to be an explicit nil

### UnsetConditional
`func (o *ItemPropertyV2) UnsetConditional()`

UnsetConditional ensures that no value is present for Conditional, not even an explicit nil
### GetIcon

`func (o *ItemPropertyV2) GetIcon() string`

GetIcon returns the Icon field if non-nil, zero value otherwise.

### GetIconOk

`func (o *ItemPropertyV2) GetIconOk() (*string, bool)`

GetIconOk returns a tuple with the Icon field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIcon

`func (o *ItemPropertyV2) SetIcon(v string)`

SetIcon sets Icon field to given value.

### HasIcon

`func (o *ItemPropertyV2) HasIcon() bool`

HasIcon returns a boolean if a field has been set.

### SetIconNil

`func (o *ItemPropertyV2) SetIconNil(b bool)`

 SetIconNil sets the value for Icon to be an explicit nil

### UnsetIcon
`func (o *ItemPropertyV2) UnsetIcon()`

UnsetIcon ensures that no value is present for Icon, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


