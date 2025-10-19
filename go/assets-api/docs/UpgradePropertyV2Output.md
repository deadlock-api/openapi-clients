# UpgradePropertyV2Output

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
**TooltipSection** | Pointer to [**NullableRawAbilitySectionTypeV2**](RawAbilitySectionTypeV2.md) |  | [optional] 
**TooltipIsElevated** | Pointer to **NullableBool** |  | [optional] 
**TooltipIsImportant** | Pointer to **NullableBool** |  | [optional] 

## Methods

### NewUpgradePropertyV2Output

`func NewUpgradePropertyV2Output() *UpgradePropertyV2Output`

NewUpgradePropertyV2Output instantiates a new UpgradePropertyV2Output object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpgradePropertyV2OutputWithDefaults

`func NewUpgradePropertyV2OutputWithDefaults() *UpgradePropertyV2Output`

NewUpgradePropertyV2OutputWithDefaults instantiates a new UpgradePropertyV2Output object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetValue

`func (o *UpgradePropertyV2Output) GetValue() Value1`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *UpgradePropertyV2Output) GetValueOk() (*Value1, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *UpgradePropertyV2Output) SetValue(v Value1)`

SetValue sets Value field to given value.

### HasValue

`func (o *UpgradePropertyV2Output) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValueNil

`func (o *UpgradePropertyV2Output) SetValueNil(b bool)`

 SetValueNil sets the value for Value to be an explicit nil

### UnsetValue
`func (o *UpgradePropertyV2Output) UnsetValue()`

UnsetValue ensures that no value is present for Value, not even an explicit nil
### GetCanSetTokenOverride

`func (o *UpgradePropertyV2Output) GetCanSetTokenOverride() bool`

GetCanSetTokenOverride returns the CanSetTokenOverride field if non-nil, zero value otherwise.

### GetCanSetTokenOverrideOk

`func (o *UpgradePropertyV2Output) GetCanSetTokenOverrideOk() (*bool, bool)`

GetCanSetTokenOverrideOk returns a tuple with the CanSetTokenOverride field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCanSetTokenOverride

`func (o *UpgradePropertyV2Output) SetCanSetTokenOverride(v bool)`

SetCanSetTokenOverride sets CanSetTokenOverride field to given value.

### HasCanSetTokenOverride

`func (o *UpgradePropertyV2Output) HasCanSetTokenOverride() bool`

HasCanSetTokenOverride returns a boolean if a field has been set.

### SetCanSetTokenOverrideNil

`func (o *UpgradePropertyV2Output) SetCanSetTokenOverrideNil(b bool)`

 SetCanSetTokenOverrideNil sets the value for CanSetTokenOverride to be an explicit nil

### UnsetCanSetTokenOverride
`func (o *UpgradePropertyV2Output) UnsetCanSetTokenOverride()`

UnsetCanSetTokenOverride ensures that no value is present for CanSetTokenOverride, not even an explicit nil
### GetProvidedPropertyType

`func (o *UpgradePropertyV2Output) GetProvidedPropertyType() string`

GetProvidedPropertyType returns the ProvidedPropertyType field if non-nil, zero value otherwise.

### GetProvidedPropertyTypeOk

`func (o *UpgradePropertyV2Output) GetProvidedPropertyTypeOk() (*string, bool)`

GetProvidedPropertyTypeOk returns a tuple with the ProvidedPropertyType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvidedPropertyType

`func (o *UpgradePropertyV2Output) SetProvidedPropertyType(v string)`

SetProvidedPropertyType sets ProvidedPropertyType field to given value.

### HasProvidedPropertyType

`func (o *UpgradePropertyV2Output) HasProvidedPropertyType() bool`

HasProvidedPropertyType returns a boolean if a field has been set.

### SetProvidedPropertyTypeNil

`func (o *UpgradePropertyV2Output) SetProvidedPropertyTypeNil(b bool)`

 SetProvidedPropertyTypeNil sets the value for ProvidedPropertyType to be an explicit nil

### UnsetProvidedPropertyType
`func (o *UpgradePropertyV2Output) UnsetProvidedPropertyType()`

UnsetProvidedPropertyType ensures that no value is present for ProvidedPropertyType, not even an explicit nil
### GetCssClass

`func (o *UpgradePropertyV2Output) GetCssClass() string`

GetCssClass returns the CssClass field if non-nil, zero value otherwise.

### GetCssClassOk

`func (o *UpgradePropertyV2Output) GetCssClassOk() (*string, bool)`

GetCssClassOk returns a tuple with the CssClass field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCssClass

`func (o *UpgradePropertyV2Output) SetCssClass(v string)`

SetCssClass sets CssClass field to given value.

### HasCssClass

`func (o *UpgradePropertyV2Output) HasCssClass() bool`

HasCssClass returns a boolean if a field has been set.

### SetCssClassNil

`func (o *UpgradePropertyV2Output) SetCssClassNil(b bool)`

 SetCssClassNil sets the value for CssClass to be an explicit nil

### UnsetCssClass
`func (o *UpgradePropertyV2Output) UnsetCssClass()`

UnsetCssClass ensures that no value is present for CssClass, not even an explicit nil
### GetUsageFlags

`func (o *UpgradePropertyV2Output) GetUsageFlags() UsageFlags`

GetUsageFlags returns the UsageFlags field if non-nil, zero value otherwise.

### GetUsageFlagsOk

`func (o *UpgradePropertyV2Output) GetUsageFlagsOk() (*UsageFlags, bool)`

GetUsageFlagsOk returns a tuple with the UsageFlags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsageFlags

`func (o *UpgradePropertyV2Output) SetUsageFlags(v UsageFlags)`

SetUsageFlags sets UsageFlags field to given value.

### HasUsageFlags

`func (o *UpgradePropertyV2Output) HasUsageFlags() bool`

HasUsageFlags returns a boolean if a field has been set.

### SetUsageFlagsNil

`func (o *UpgradePropertyV2Output) SetUsageFlagsNil(b bool)`

 SetUsageFlagsNil sets the value for UsageFlags to be an explicit nil

### UnsetUsageFlags
`func (o *UpgradePropertyV2Output) UnsetUsageFlags()`

UnsetUsageFlags ensures that no value is present for UsageFlags, not even an explicit nil
### GetNegativeAttribute

`func (o *UpgradePropertyV2Output) GetNegativeAttribute() bool`

GetNegativeAttribute returns the NegativeAttribute field if non-nil, zero value otherwise.

### GetNegativeAttributeOk

`func (o *UpgradePropertyV2Output) GetNegativeAttributeOk() (*bool, bool)`

GetNegativeAttributeOk returns a tuple with the NegativeAttribute field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNegativeAttribute

`func (o *UpgradePropertyV2Output) SetNegativeAttribute(v bool)`

SetNegativeAttribute sets NegativeAttribute field to given value.

### HasNegativeAttribute

`func (o *UpgradePropertyV2Output) HasNegativeAttribute() bool`

HasNegativeAttribute returns a boolean if a field has been set.

### SetNegativeAttributeNil

`func (o *UpgradePropertyV2Output) SetNegativeAttributeNil(b bool)`

 SetNegativeAttributeNil sets the value for NegativeAttribute to be an explicit nil

### UnsetNegativeAttribute
`func (o *UpgradePropertyV2Output) UnsetNegativeAttribute()`

UnsetNegativeAttribute ensures that no value is present for NegativeAttribute, not even an explicit nil
### GetDisableValue

`func (o *UpgradePropertyV2Output) GetDisableValue() string`

GetDisableValue returns the DisableValue field if non-nil, zero value otherwise.

### GetDisableValueOk

`func (o *UpgradePropertyV2Output) GetDisableValueOk() (*string, bool)`

GetDisableValueOk returns a tuple with the DisableValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisableValue

`func (o *UpgradePropertyV2Output) SetDisableValue(v string)`

SetDisableValue sets DisableValue field to given value.

### HasDisableValue

`func (o *UpgradePropertyV2Output) HasDisableValue() bool`

HasDisableValue returns a boolean if a field has been set.

### SetDisableValueNil

`func (o *UpgradePropertyV2Output) SetDisableValueNil(b bool)`

 SetDisableValueNil sets the value for DisableValue to be an explicit nil

### UnsetDisableValue
`func (o *UpgradePropertyV2Output) UnsetDisableValue()`

UnsetDisableValue ensures that no value is present for DisableValue, not even an explicit nil
### GetLocTokenOverride

`func (o *UpgradePropertyV2Output) GetLocTokenOverride() string`

GetLocTokenOverride returns the LocTokenOverride field if non-nil, zero value otherwise.

### GetLocTokenOverrideOk

`func (o *UpgradePropertyV2Output) GetLocTokenOverrideOk() (*string, bool)`

GetLocTokenOverrideOk returns a tuple with the LocTokenOverride field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocTokenOverride

`func (o *UpgradePropertyV2Output) SetLocTokenOverride(v string)`

SetLocTokenOverride sets LocTokenOverride field to given value.

### HasLocTokenOverride

`func (o *UpgradePropertyV2Output) HasLocTokenOverride() bool`

HasLocTokenOverride returns a boolean if a field has been set.

### SetLocTokenOverrideNil

`func (o *UpgradePropertyV2Output) SetLocTokenOverrideNil(b bool)`

 SetLocTokenOverrideNil sets the value for LocTokenOverride to be an explicit nil

### UnsetLocTokenOverride
`func (o *UpgradePropertyV2Output) UnsetLocTokenOverride()`

UnsetLocTokenOverride ensures that no value is present for LocTokenOverride, not even an explicit nil
### GetDisplayUnits

`func (o *UpgradePropertyV2Output) GetDisplayUnits() string`

GetDisplayUnits returns the DisplayUnits field if non-nil, zero value otherwise.

### GetDisplayUnitsOk

`func (o *UpgradePropertyV2Output) GetDisplayUnitsOk() (*string, bool)`

GetDisplayUnitsOk returns a tuple with the DisplayUnits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayUnits

`func (o *UpgradePropertyV2Output) SetDisplayUnits(v string)`

SetDisplayUnits sets DisplayUnits field to given value.

### HasDisplayUnits

`func (o *UpgradePropertyV2Output) HasDisplayUnits() bool`

HasDisplayUnits returns a boolean if a field has been set.

### SetDisplayUnitsNil

`func (o *UpgradePropertyV2Output) SetDisplayUnitsNil(b bool)`

 SetDisplayUnitsNil sets the value for DisplayUnits to be an explicit nil

### UnsetDisplayUnits
`func (o *UpgradePropertyV2Output) UnsetDisplayUnits()`

UnsetDisplayUnits ensures that no value is present for DisplayUnits, not even an explicit nil
### GetIconPath

`func (o *UpgradePropertyV2Output) GetIconPath() string`

GetIconPath returns the IconPath field if non-nil, zero value otherwise.

### GetIconPathOk

`func (o *UpgradePropertyV2Output) GetIconPathOk() (*string, bool)`

GetIconPathOk returns a tuple with the IconPath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIconPath

`func (o *UpgradePropertyV2Output) SetIconPath(v string)`

SetIconPath sets IconPath field to given value.

### HasIconPath

`func (o *UpgradePropertyV2Output) HasIconPath() bool`

HasIconPath returns a boolean if a field has been set.

### SetIconPathNil

`func (o *UpgradePropertyV2Output) SetIconPathNil(b bool)`

 SetIconPathNil sets the value for IconPath to be an explicit nil

### UnsetIconPath
`func (o *UpgradePropertyV2Output) UnsetIconPath()`

UnsetIconPath ensures that no value is present for IconPath, not even an explicit nil
### GetScaleFunction

`func (o *UpgradePropertyV2Output) GetScaleFunction() RawItemPropertyScaleFunctionSubclassV2Output`

GetScaleFunction returns the ScaleFunction field if non-nil, zero value otherwise.

### GetScaleFunctionOk

`func (o *UpgradePropertyV2Output) GetScaleFunctionOk() (*RawItemPropertyScaleFunctionSubclassV2Output, bool)`

GetScaleFunctionOk returns a tuple with the ScaleFunction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScaleFunction

`func (o *UpgradePropertyV2Output) SetScaleFunction(v RawItemPropertyScaleFunctionSubclassV2Output)`

SetScaleFunction sets ScaleFunction field to given value.

### HasScaleFunction

`func (o *UpgradePropertyV2Output) HasScaleFunction() bool`

HasScaleFunction returns a boolean if a field has been set.

### SetScaleFunctionNil

`func (o *UpgradePropertyV2Output) SetScaleFunctionNil(b bool)`

 SetScaleFunctionNil sets the value for ScaleFunction to be an explicit nil

### UnsetScaleFunction
`func (o *UpgradePropertyV2Output) UnsetScaleFunction()`

UnsetScaleFunction ensures that no value is present for ScaleFunction, not even an explicit nil
### GetPrefix

`func (o *UpgradePropertyV2Output) GetPrefix() string`

GetPrefix returns the Prefix field if non-nil, zero value otherwise.

### GetPrefixOk

`func (o *UpgradePropertyV2Output) GetPrefixOk() (*string, bool)`

GetPrefixOk returns a tuple with the Prefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefix

`func (o *UpgradePropertyV2Output) SetPrefix(v string)`

SetPrefix sets Prefix field to given value.

### HasPrefix

`func (o *UpgradePropertyV2Output) HasPrefix() bool`

HasPrefix returns a boolean if a field has been set.

### SetPrefixNil

`func (o *UpgradePropertyV2Output) SetPrefixNil(b bool)`

 SetPrefixNil sets the value for Prefix to be an explicit nil

### UnsetPrefix
`func (o *UpgradePropertyV2Output) UnsetPrefix()`

UnsetPrefix ensures that no value is present for Prefix, not even an explicit nil
### GetLabel

`func (o *UpgradePropertyV2Output) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *UpgradePropertyV2Output) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *UpgradePropertyV2Output) SetLabel(v string)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *UpgradePropertyV2Output) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### SetLabelNil

`func (o *UpgradePropertyV2Output) SetLabelNil(b bool)`

 SetLabelNil sets the value for Label to be an explicit nil

### UnsetLabel
`func (o *UpgradePropertyV2Output) UnsetLabel()`

UnsetLabel ensures that no value is present for Label, not even an explicit nil
### GetPostfix

`func (o *UpgradePropertyV2Output) GetPostfix() string`

GetPostfix returns the Postfix field if non-nil, zero value otherwise.

### GetPostfixOk

`func (o *UpgradePropertyV2Output) GetPostfixOk() (*string, bool)`

GetPostfixOk returns a tuple with the Postfix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostfix

`func (o *UpgradePropertyV2Output) SetPostfix(v string)`

SetPostfix sets Postfix field to given value.

### HasPostfix

`func (o *UpgradePropertyV2Output) HasPostfix() bool`

HasPostfix returns a boolean if a field has been set.

### SetPostfixNil

`func (o *UpgradePropertyV2Output) SetPostfixNil(b bool)`

 SetPostfixNil sets the value for Postfix to be an explicit nil

### UnsetPostfix
`func (o *UpgradePropertyV2Output) UnsetPostfix()`

UnsetPostfix ensures that no value is present for Postfix, not even an explicit nil
### GetPostvalueLabel

`func (o *UpgradePropertyV2Output) GetPostvalueLabel() string`

GetPostvalueLabel returns the PostvalueLabel field if non-nil, zero value otherwise.

### GetPostvalueLabelOk

`func (o *UpgradePropertyV2Output) GetPostvalueLabelOk() (*string, bool)`

GetPostvalueLabelOk returns a tuple with the PostvalueLabel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostvalueLabel

`func (o *UpgradePropertyV2Output) SetPostvalueLabel(v string)`

SetPostvalueLabel sets PostvalueLabel field to given value.

### HasPostvalueLabel

`func (o *UpgradePropertyV2Output) HasPostvalueLabel() bool`

HasPostvalueLabel returns a boolean if a field has been set.

### SetPostvalueLabelNil

`func (o *UpgradePropertyV2Output) SetPostvalueLabelNil(b bool)`

 SetPostvalueLabelNil sets the value for PostvalueLabel to be an explicit nil

### UnsetPostvalueLabel
`func (o *UpgradePropertyV2Output) UnsetPostvalueLabel()`

UnsetPostvalueLabel ensures that no value is present for PostvalueLabel, not even an explicit nil
### GetConditional

`func (o *UpgradePropertyV2Output) GetConditional() string`

GetConditional returns the Conditional field if non-nil, zero value otherwise.

### GetConditionalOk

`func (o *UpgradePropertyV2Output) GetConditionalOk() (*string, bool)`

GetConditionalOk returns a tuple with the Conditional field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConditional

`func (o *UpgradePropertyV2Output) SetConditional(v string)`

SetConditional sets Conditional field to given value.

### HasConditional

`func (o *UpgradePropertyV2Output) HasConditional() bool`

HasConditional returns a boolean if a field has been set.

### SetConditionalNil

`func (o *UpgradePropertyV2Output) SetConditionalNil(b bool)`

 SetConditionalNil sets the value for Conditional to be an explicit nil

### UnsetConditional
`func (o *UpgradePropertyV2Output) UnsetConditional()`

UnsetConditional ensures that no value is present for Conditional, not even an explicit nil
### GetIcon

`func (o *UpgradePropertyV2Output) GetIcon() string`

GetIcon returns the Icon field if non-nil, zero value otherwise.

### GetIconOk

`func (o *UpgradePropertyV2Output) GetIconOk() (*string, bool)`

GetIconOk returns a tuple with the Icon field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIcon

`func (o *UpgradePropertyV2Output) SetIcon(v string)`

SetIcon sets Icon field to given value.

### HasIcon

`func (o *UpgradePropertyV2Output) HasIcon() bool`

HasIcon returns a boolean if a field has been set.

### SetIconNil

`func (o *UpgradePropertyV2Output) SetIconNil(b bool)`

 SetIconNil sets the value for Icon to be an explicit nil

### UnsetIcon
`func (o *UpgradePropertyV2Output) UnsetIcon()`

UnsetIcon ensures that no value is present for Icon, not even an explicit nil
### GetTooltipSection

`func (o *UpgradePropertyV2Output) GetTooltipSection() RawAbilitySectionTypeV2`

GetTooltipSection returns the TooltipSection field if non-nil, zero value otherwise.

### GetTooltipSectionOk

`func (o *UpgradePropertyV2Output) GetTooltipSectionOk() (*RawAbilitySectionTypeV2, bool)`

GetTooltipSectionOk returns a tuple with the TooltipSection field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipSection

`func (o *UpgradePropertyV2Output) SetTooltipSection(v RawAbilitySectionTypeV2)`

SetTooltipSection sets TooltipSection field to given value.

### HasTooltipSection

`func (o *UpgradePropertyV2Output) HasTooltipSection() bool`

HasTooltipSection returns a boolean if a field has been set.

### SetTooltipSectionNil

`func (o *UpgradePropertyV2Output) SetTooltipSectionNil(b bool)`

 SetTooltipSectionNil sets the value for TooltipSection to be an explicit nil

### UnsetTooltipSection
`func (o *UpgradePropertyV2Output) UnsetTooltipSection()`

UnsetTooltipSection ensures that no value is present for TooltipSection, not even an explicit nil
### GetTooltipIsElevated

`func (o *UpgradePropertyV2Output) GetTooltipIsElevated() bool`

GetTooltipIsElevated returns the TooltipIsElevated field if non-nil, zero value otherwise.

### GetTooltipIsElevatedOk

`func (o *UpgradePropertyV2Output) GetTooltipIsElevatedOk() (*bool, bool)`

GetTooltipIsElevatedOk returns a tuple with the TooltipIsElevated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipIsElevated

`func (o *UpgradePropertyV2Output) SetTooltipIsElevated(v bool)`

SetTooltipIsElevated sets TooltipIsElevated field to given value.

### HasTooltipIsElevated

`func (o *UpgradePropertyV2Output) HasTooltipIsElevated() bool`

HasTooltipIsElevated returns a boolean if a field has been set.

### SetTooltipIsElevatedNil

`func (o *UpgradePropertyV2Output) SetTooltipIsElevatedNil(b bool)`

 SetTooltipIsElevatedNil sets the value for TooltipIsElevated to be an explicit nil

### UnsetTooltipIsElevated
`func (o *UpgradePropertyV2Output) UnsetTooltipIsElevated()`

UnsetTooltipIsElevated ensures that no value is present for TooltipIsElevated, not even an explicit nil
### GetTooltipIsImportant

`func (o *UpgradePropertyV2Output) GetTooltipIsImportant() bool`

GetTooltipIsImportant returns the TooltipIsImportant field if non-nil, zero value otherwise.

### GetTooltipIsImportantOk

`func (o *UpgradePropertyV2Output) GetTooltipIsImportantOk() (*bool, bool)`

GetTooltipIsImportantOk returns a tuple with the TooltipIsImportant field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipIsImportant

`func (o *UpgradePropertyV2Output) SetTooltipIsImportant(v bool)`

SetTooltipIsImportant sets TooltipIsImportant field to given value.

### HasTooltipIsImportant

`func (o *UpgradePropertyV2Output) HasTooltipIsImportant() bool`

HasTooltipIsImportant returns a boolean if a field has been set.

### SetTooltipIsImportantNil

`func (o *UpgradePropertyV2Output) SetTooltipIsImportantNil(b bool)`

 SetTooltipIsImportantNil sets the value for TooltipIsImportant to be an explicit nil

### UnsetTooltipIsImportant
`func (o *UpgradePropertyV2Output) UnsetTooltipIsImportant()`

UnsetTooltipIsImportant ensures that no value is present for TooltipIsImportant, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


