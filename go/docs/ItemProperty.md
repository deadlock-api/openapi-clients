# ItemProperty

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CanSetTokenOverride** | Pointer to **NullableBool** |  | [optional] 
**Conditional** | Pointer to **NullableString** |  | [optional] 
**CssClass** | Pointer to **NullableString** |  | [optional] 
**DisableValue** | Pointer to **NullableString** |  | [optional] 
**DisplayUnits** | Pointer to **NullableString** |  | [optional] 
**Icon** | Pointer to **NullableString** |  | [optional] 
**Label** | Pointer to **NullableString** |  | [optional] 
**LocTokenOverride** | Pointer to **NullableString** |  | [optional] 
**NegativeAttribute** | Pointer to **NullableBool** |  | [optional] 
**Postfix** | Pointer to **NullableString** |  | [optional] 
**PostvalueLabel** | Pointer to **NullableString** |  | [optional] 
**Prefix** | Pointer to **NullableString** |  | [optional] 
**ProvidedPropertyType** | Pointer to **NullableString** |  | [optional] 
**ScaleFunction** | Pointer to [**NullableRawItemPropertyScaleFunctionSubclass**](RawItemPropertyScaleFunctionSubclass.md) |  | [optional] 
**StreetBrawlValue** | Pointer to **NullableString** |  | [optional] 
**UsageFlags** | Pointer to [**[]StatsUsageFlag**](StatsUsageFlag.md) |  | [optional] 
**Value** | Pointer to **NullableString** | Raw JSON value preserves the source distinction between numeric and stringly-typed bonuses (&#x60;\&quot;14.5\&quot;&#x60; vs &#x60;14.5&#x60;). | [optional] 

## Methods

### NewItemProperty

`func NewItemProperty() *ItemProperty`

NewItemProperty instantiates a new ItemProperty object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewItemPropertyWithDefaults

`func NewItemPropertyWithDefaults() *ItemProperty`

NewItemPropertyWithDefaults instantiates a new ItemProperty object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCanSetTokenOverride

`func (o *ItemProperty) GetCanSetTokenOverride() bool`

GetCanSetTokenOverride returns the CanSetTokenOverride field if non-nil, zero value otherwise.

### GetCanSetTokenOverrideOk

`func (o *ItemProperty) GetCanSetTokenOverrideOk() (*bool, bool)`

GetCanSetTokenOverrideOk returns a tuple with the CanSetTokenOverride field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCanSetTokenOverride

`func (o *ItemProperty) SetCanSetTokenOverride(v bool)`

SetCanSetTokenOverride sets CanSetTokenOverride field to given value.

### HasCanSetTokenOverride

`func (o *ItemProperty) HasCanSetTokenOverride() bool`

HasCanSetTokenOverride returns a boolean if a field has been set.

### SetCanSetTokenOverrideNil

`func (o *ItemProperty) SetCanSetTokenOverrideNil(b bool)`

 SetCanSetTokenOverrideNil sets the value for CanSetTokenOverride to be an explicit nil

### UnsetCanSetTokenOverride
`func (o *ItemProperty) UnsetCanSetTokenOverride()`

UnsetCanSetTokenOverride ensures that no value is present for CanSetTokenOverride, not even an explicit nil
### GetConditional

`func (o *ItemProperty) GetConditional() string`

GetConditional returns the Conditional field if non-nil, zero value otherwise.

### GetConditionalOk

`func (o *ItemProperty) GetConditionalOk() (*string, bool)`

GetConditionalOk returns a tuple with the Conditional field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConditional

`func (o *ItemProperty) SetConditional(v string)`

SetConditional sets Conditional field to given value.

### HasConditional

`func (o *ItemProperty) HasConditional() bool`

HasConditional returns a boolean if a field has been set.

### SetConditionalNil

`func (o *ItemProperty) SetConditionalNil(b bool)`

 SetConditionalNil sets the value for Conditional to be an explicit nil

### UnsetConditional
`func (o *ItemProperty) UnsetConditional()`

UnsetConditional ensures that no value is present for Conditional, not even an explicit nil
### GetCssClass

`func (o *ItemProperty) GetCssClass() string`

GetCssClass returns the CssClass field if non-nil, zero value otherwise.

### GetCssClassOk

`func (o *ItemProperty) GetCssClassOk() (*string, bool)`

GetCssClassOk returns a tuple with the CssClass field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCssClass

`func (o *ItemProperty) SetCssClass(v string)`

SetCssClass sets CssClass field to given value.

### HasCssClass

`func (o *ItemProperty) HasCssClass() bool`

HasCssClass returns a boolean if a field has been set.

### SetCssClassNil

`func (o *ItemProperty) SetCssClassNil(b bool)`

 SetCssClassNil sets the value for CssClass to be an explicit nil

### UnsetCssClass
`func (o *ItemProperty) UnsetCssClass()`

UnsetCssClass ensures that no value is present for CssClass, not even an explicit nil
### GetDisableValue

`func (o *ItemProperty) GetDisableValue() string`

GetDisableValue returns the DisableValue field if non-nil, zero value otherwise.

### GetDisableValueOk

`func (o *ItemProperty) GetDisableValueOk() (*string, bool)`

GetDisableValueOk returns a tuple with the DisableValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisableValue

`func (o *ItemProperty) SetDisableValue(v string)`

SetDisableValue sets DisableValue field to given value.

### HasDisableValue

`func (o *ItemProperty) HasDisableValue() bool`

HasDisableValue returns a boolean if a field has been set.

### SetDisableValueNil

`func (o *ItemProperty) SetDisableValueNil(b bool)`

 SetDisableValueNil sets the value for DisableValue to be an explicit nil

### UnsetDisableValue
`func (o *ItemProperty) UnsetDisableValue()`

UnsetDisableValue ensures that no value is present for DisableValue, not even an explicit nil
### GetDisplayUnits

`func (o *ItemProperty) GetDisplayUnits() string`

GetDisplayUnits returns the DisplayUnits field if non-nil, zero value otherwise.

### GetDisplayUnitsOk

`func (o *ItemProperty) GetDisplayUnitsOk() (*string, bool)`

GetDisplayUnitsOk returns a tuple with the DisplayUnits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayUnits

`func (o *ItemProperty) SetDisplayUnits(v string)`

SetDisplayUnits sets DisplayUnits field to given value.

### HasDisplayUnits

`func (o *ItemProperty) HasDisplayUnits() bool`

HasDisplayUnits returns a boolean if a field has been set.

### SetDisplayUnitsNil

`func (o *ItemProperty) SetDisplayUnitsNil(b bool)`

 SetDisplayUnitsNil sets the value for DisplayUnits to be an explicit nil

### UnsetDisplayUnits
`func (o *ItemProperty) UnsetDisplayUnits()`

UnsetDisplayUnits ensures that no value is present for DisplayUnits, not even an explicit nil
### GetIcon

`func (o *ItemProperty) GetIcon() string`

GetIcon returns the Icon field if non-nil, zero value otherwise.

### GetIconOk

`func (o *ItemProperty) GetIconOk() (*string, bool)`

GetIconOk returns a tuple with the Icon field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIcon

`func (o *ItemProperty) SetIcon(v string)`

SetIcon sets Icon field to given value.

### HasIcon

`func (o *ItemProperty) HasIcon() bool`

HasIcon returns a boolean if a field has been set.

### SetIconNil

`func (o *ItemProperty) SetIconNil(b bool)`

 SetIconNil sets the value for Icon to be an explicit nil

### UnsetIcon
`func (o *ItemProperty) UnsetIcon()`

UnsetIcon ensures that no value is present for Icon, not even an explicit nil
### GetLabel

`func (o *ItemProperty) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *ItemProperty) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *ItemProperty) SetLabel(v string)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *ItemProperty) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### SetLabelNil

`func (o *ItemProperty) SetLabelNil(b bool)`

 SetLabelNil sets the value for Label to be an explicit nil

### UnsetLabel
`func (o *ItemProperty) UnsetLabel()`

UnsetLabel ensures that no value is present for Label, not even an explicit nil
### GetLocTokenOverride

`func (o *ItemProperty) GetLocTokenOverride() string`

GetLocTokenOverride returns the LocTokenOverride field if non-nil, zero value otherwise.

### GetLocTokenOverrideOk

`func (o *ItemProperty) GetLocTokenOverrideOk() (*string, bool)`

GetLocTokenOverrideOk returns a tuple with the LocTokenOverride field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocTokenOverride

`func (o *ItemProperty) SetLocTokenOverride(v string)`

SetLocTokenOverride sets LocTokenOverride field to given value.

### HasLocTokenOverride

`func (o *ItemProperty) HasLocTokenOverride() bool`

HasLocTokenOverride returns a boolean if a field has been set.

### SetLocTokenOverrideNil

`func (o *ItemProperty) SetLocTokenOverrideNil(b bool)`

 SetLocTokenOverrideNil sets the value for LocTokenOverride to be an explicit nil

### UnsetLocTokenOverride
`func (o *ItemProperty) UnsetLocTokenOverride()`

UnsetLocTokenOverride ensures that no value is present for LocTokenOverride, not even an explicit nil
### GetNegativeAttribute

`func (o *ItemProperty) GetNegativeAttribute() bool`

GetNegativeAttribute returns the NegativeAttribute field if non-nil, zero value otherwise.

### GetNegativeAttributeOk

`func (o *ItemProperty) GetNegativeAttributeOk() (*bool, bool)`

GetNegativeAttributeOk returns a tuple with the NegativeAttribute field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNegativeAttribute

`func (o *ItemProperty) SetNegativeAttribute(v bool)`

SetNegativeAttribute sets NegativeAttribute field to given value.

### HasNegativeAttribute

`func (o *ItemProperty) HasNegativeAttribute() bool`

HasNegativeAttribute returns a boolean if a field has been set.

### SetNegativeAttributeNil

`func (o *ItemProperty) SetNegativeAttributeNil(b bool)`

 SetNegativeAttributeNil sets the value for NegativeAttribute to be an explicit nil

### UnsetNegativeAttribute
`func (o *ItemProperty) UnsetNegativeAttribute()`

UnsetNegativeAttribute ensures that no value is present for NegativeAttribute, not even an explicit nil
### GetPostfix

`func (o *ItemProperty) GetPostfix() string`

GetPostfix returns the Postfix field if non-nil, zero value otherwise.

### GetPostfixOk

`func (o *ItemProperty) GetPostfixOk() (*string, bool)`

GetPostfixOk returns a tuple with the Postfix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostfix

`func (o *ItemProperty) SetPostfix(v string)`

SetPostfix sets Postfix field to given value.

### HasPostfix

`func (o *ItemProperty) HasPostfix() bool`

HasPostfix returns a boolean if a field has been set.

### SetPostfixNil

`func (o *ItemProperty) SetPostfixNil(b bool)`

 SetPostfixNil sets the value for Postfix to be an explicit nil

### UnsetPostfix
`func (o *ItemProperty) UnsetPostfix()`

UnsetPostfix ensures that no value is present for Postfix, not even an explicit nil
### GetPostvalueLabel

`func (o *ItemProperty) GetPostvalueLabel() string`

GetPostvalueLabel returns the PostvalueLabel field if non-nil, zero value otherwise.

### GetPostvalueLabelOk

`func (o *ItemProperty) GetPostvalueLabelOk() (*string, bool)`

GetPostvalueLabelOk returns a tuple with the PostvalueLabel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostvalueLabel

`func (o *ItemProperty) SetPostvalueLabel(v string)`

SetPostvalueLabel sets PostvalueLabel field to given value.

### HasPostvalueLabel

`func (o *ItemProperty) HasPostvalueLabel() bool`

HasPostvalueLabel returns a boolean if a field has been set.

### SetPostvalueLabelNil

`func (o *ItemProperty) SetPostvalueLabelNil(b bool)`

 SetPostvalueLabelNil sets the value for PostvalueLabel to be an explicit nil

### UnsetPostvalueLabel
`func (o *ItemProperty) UnsetPostvalueLabel()`

UnsetPostvalueLabel ensures that no value is present for PostvalueLabel, not even an explicit nil
### GetPrefix

`func (o *ItemProperty) GetPrefix() string`

GetPrefix returns the Prefix field if non-nil, zero value otherwise.

### GetPrefixOk

`func (o *ItemProperty) GetPrefixOk() (*string, bool)`

GetPrefixOk returns a tuple with the Prefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefix

`func (o *ItemProperty) SetPrefix(v string)`

SetPrefix sets Prefix field to given value.

### HasPrefix

`func (o *ItemProperty) HasPrefix() bool`

HasPrefix returns a boolean if a field has been set.

### SetPrefixNil

`func (o *ItemProperty) SetPrefixNil(b bool)`

 SetPrefixNil sets the value for Prefix to be an explicit nil

### UnsetPrefix
`func (o *ItemProperty) UnsetPrefix()`

UnsetPrefix ensures that no value is present for Prefix, not even an explicit nil
### GetProvidedPropertyType

`func (o *ItemProperty) GetProvidedPropertyType() string`

GetProvidedPropertyType returns the ProvidedPropertyType field if non-nil, zero value otherwise.

### GetProvidedPropertyTypeOk

`func (o *ItemProperty) GetProvidedPropertyTypeOk() (*string, bool)`

GetProvidedPropertyTypeOk returns a tuple with the ProvidedPropertyType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvidedPropertyType

`func (o *ItemProperty) SetProvidedPropertyType(v string)`

SetProvidedPropertyType sets ProvidedPropertyType field to given value.

### HasProvidedPropertyType

`func (o *ItemProperty) HasProvidedPropertyType() bool`

HasProvidedPropertyType returns a boolean if a field has been set.

### SetProvidedPropertyTypeNil

`func (o *ItemProperty) SetProvidedPropertyTypeNil(b bool)`

 SetProvidedPropertyTypeNil sets the value for ProvidedPropertyType to be an explicit nil

### UnsetProvidedPropertyType
`func (o *ItemProperty) UnsetProvidedPropertyType()`

UnsetProvidedPropertyType ensures that no value is present for ProvidedPropertyType, not even an explicit nil
### GetScaleFunction

`func (o *ItemProperty) GetScaleFunction() RawItemPropertyScaleFunctionSubclass`

GetScaleFunction returns the ScaleFunction field if non-nil, zero value otherwise.

### GetScaleFunctionOk

`func (o *ItemProperty) GetScaleFunctionOk() (*RawItemPropertyScaleFunctionSubclass, bool)`

GetScaleFunctionOk returns a tuple with the ScaleFunction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScaleFunction

`func (o *ItemProperty) SetScaleFunction(v RawItemPropertyScaleFunctionSubclass)`

SetScaleFunction sets ScaleFunction field to given value.

### HasScaleFunction

`func (o *ItemProperty) HasScaleFunction() bool`

HasScaleFunction returns a boolean if a field has been set.

### SetScaleFunctionNil

`func (o *ItemProperty) SetScaleFunctionNil(b bool)`

 SetScaleFunctionNil sets the value for ScaleFunction to be an explicit nil

### UnsetScaleFunction
`func (o *ItemProperty) UnsetScaleFunction()`

UnsetScaleFunction ensures that no value is present for ScaleFunction, not even an explicit nil
### GetStreetBrawlValue

`func (o *ItemProperty) GetStreetBrawlValue() string`

GetStreetBrawlValue returns the StreetBrawlValue field if non-nil, zero value otherwise.

### GetStreetBrawlValueOk

`func (o *ItemProperty) GetStreetBrawlValueOk() (*string, bool)`

GetStreetBrawlValueOk returns a tuple with the StreetBrawlValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStreetBrawlValue

`func (o *ItemProperty) SetStreetBrawlValue(v string)`

SetStreetBrawlValue sets StreetBrawlValue field to given value.

### HasStreetBrawlValue

`func (o *ItemProperty) HasStreetBrawlValue() bool`

HasStreetBrawlValue returns a boolean if a field has been set.

### SetStreetBrawlValueNil

`func (o *ItemProperty) SetStreetBrawlValueNil(b bool)`

 SetStreetBrawlValueNil sets the value for StreetBrawlValue to be an explicit nil

### UnsetStreetBrawlValue
`func (o *ItemProperty) UnsetStreetBrawlValue()`

UnsetStreetBrawlValue ensures that no value is present for StreetBrawlValue, not even an explicit nil
### GetUsageFlags

`func (o *ItemProperty) GetUsageFlags() []StatsUsageFlag`

GetUsageFlags returns the UsageFlags field if non-nil, zero value otherwise.

### GetUsageFlagsOk

`func (o *ItemProperty) GetUsageFlagsOk() (*[]StatsUsageFlag, bool)`

GetUsageFlagsOk returns a tuple with the UsageFlags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsageFlags

`func (o *ItemProperty) SetUsageFlags(v []StatsUsageFlag)`

SetUsageFlags sets UsageFlags field to given value.

### HasUsageFlags

`func (o *ItemProperty) HasUsageFlags() bool`

HasUsageFlags returns a boolean if a field has been set.

### SetUsageFlagsNil

`func (o *ItemProperty) SetUsageFlagsNil(b bool)`

 SetUsageFlagsNil sets the value for UsageFlags to be an explicit nil

### UnsetUsageFlags
`func (o *ItemProperty) UnsetUsageFlags()`

UnsetUsageFlags ensures that no value is present for UsageFlags, not even an explicit nil
### GetValue

`func (o *ItemProperty) GetValue() string`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *ItemProperty) GetValueOk() (*string, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *ItemProperty) SetValue(v string)`

SetValue sets Value field to given value.

### HasValue

`func (o *ItemProperty) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValueNil

`func (o *ItemProperty) SetValueNil(b bool)`

 SetValueNil sets the value for Value to be an explicit nil

### UnsetValue
`func (o *ItemProperty) UnsetValue()`

UnsetValue ensures that no value is present for Value, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


