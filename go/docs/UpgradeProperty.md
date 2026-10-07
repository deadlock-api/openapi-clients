# UpgradeProperty

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
**RequiredUpgradeBits** | Pointer to **[]string** | Raw &#x60;ABILITY_UPGRADE_BIT_*&#x60; flags the ability needs for this property to apply (e.g. &#x60;ABILITY_UPGRADE_BIT_TRAINED&#x60;, &#x60;ABILITY_UPGRADE_BIT_4&#x60;). | [optional] 
**ScaleFunction** | Pointer to [**NullableRawItemPropertyScaleFunctionSubclass**](RawItemPropertyScaleFunctionSubclass.md) |  | [optional] 
**StreetBrawlValue** | Pointer to **NullableString** |  | [optional] 
**UsageFlags** | Pointer to [**[]StatsUsageFlag**](StatsUsageFlag.md) |  | [optional] 
**Value** | Pointer to **NullableString** | Raw JSON value preserves the source distinction between numeric and stringly-typed bonuses (&#x60;\&quot;14.5\&quot;&#x60; vs &#x60;14.5&#x60;). | [optional] 
**TooltipIsElevated** | Pointer to **NullableBool** |  | [optional] 
**TooltipIsImportant** | Pointer to **NullableBool** |  | [optional] 
**TooltipSection** | Pointer to [**NullableAbilitySectionType**](AbilitySectionType.md) |  | [optional] 

## Methods

### NewUpgradeProperty

`func NewUpgradeProperty() *UpgradeProperty`

NewUpgradeProperty instantiates a new UpgradeProperty object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpgradePropertyWithDefaults

`func NewUpgradePropertyWithDefaults() *UpgradeProperty`

NewUpgradePropertyWithDefaults instantiates a new UpgradeProperty object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCanSetTokenOverride

`func (o *UpgradeProperty) GetCanSetTokenOverride() bool`

GetCanSetTokenOverride returns the CanSetTokenOverride field if non-nil, zero value otherwise.

### GetCanSetTokenOverrideOk

`func (o *UpgradeProperty) GetCanSetTokenOverrideOk() (*bool, bool)`

GetCanSetTokenOverrideOk returns a tuple with the CanSetTokenOverride field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCanSetTokenOverride

`func (o *UpgradeProperty) SetCanSetTokenOverride(v bool)`

SetCanSetTokenOverride sets CanSetTokenOverride field to given value.

### HasCanSetTokenOverride

`func (o *UpgradeProperty) HasCanSetTokenOverride() bool`

HasCanSetTokenOverride returns a boolean if a field has been set.

### SetCanSetTokenOverrideNil

`func (o *UpgradeProperty) SetCanSetTokenOverrideNil(b bool)`

 SetCanSetTokenOverrideNil sets the value for CanSetTokenOverride to be an explicit nil

### UnsetCanSetTokenOverride
`func (o *UpgradeProperty) UnsetCanSetTokenOverride()`

UnsetCanSetTokenOverride ensures that no value is present for CanSetTokenOverride, not even an explicit nil
### GetConditional

`func (o *UpgradeProperty) GetConditional() string`

GetConditional returns the Conditional field if non-nil, zero value otherwise.

### GetConditionalOk

`func (o *UpgradeProperty) GetConditionalOk() (*string, bool)`

GetConditionalOk returns a tuple with the Conditional field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConditional

`func (o *UpgradeProperty) SetConditional(v string)`

SetConditional sets Conditional field to given value.

### HasConditional

`func (o *UpgradeProperty) HasConditional() bool`

HasConditional returns a boolean if a field has been set.

### SetConditionalNil

`func (o *UpgradeProperty) SetConditionalNil(b bool)`

 SetConditionalNil sets the value for Conditional to be an explicit nil

### UnsetConditional
`func (o *UpgradeProperty) UnsetConditional()`

UnsetConditional ensures that no value is present for Conditional, not even an explicit nil
### GetCssClass

`func (o *UpgradeProperty) GetCssClass() string`

GetCssClass returns the CssClass field if non-nil, zero value otherwise.

### GetCssClassOk

`func (o *UpgradeProperty) GetCssClassOk() (*string, bool)`

GetCssClassOk returns a tuple with the CssClass field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCssClass

`func (o *UpgradeProperty) SetCssClass(v string)`

SetCssClass sets CssClass field to given value.

### HasCssClass

`func (o *UpgradeProperty) HasCssClass() bool`

HasCssClass returns a boolean if a field has been set.

### SetCssClassNil

`func (o *UpgradeProperty) SetCssClassNil(b bool)`

 SetCssClassNil sets the value for CssClass to be an explicit nil

### UnsetCssClass
`func (o *UpgradeProperty) UnsetCssClass()`

UnsetCssClass ensures that no value is present for CssClass, not even an explicit nil
### GetDisableValue

`func (o *UpgradeProperty) GetDisableValue() string`

GetDisableValue returns the DisableValue field if non-nil, zero value otherwise.

### GetDisableValueOk

`func (o *UpgradeProperty) GetDisableValueOk() (*string, bool)`

GetDisableValueOk returns a tuple with the DisableValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisableValue

`func (o *UpgradeProperty) SetDisableValue(v string)`

SetDisableValue sets DisableValue field to given value.

### HasDisableValue

`func (o *UpgradeProperty) HasDisableValue() bool`

HasDisableValue returns a boolean if a field has been set.

### SetDisableValueNil

`func (o *UpgradeProperty) SetDisableValueNil(b bool)`

 SetDisableValueNil sets the value for DisableValue to be an explicit nil

### UnsetDisableValue
`func (o *UpgradeProperty) UnsetDisableValue()`

UnsetDisableValue ensures that no value is present for DisableValue, not even an explicit nil
### GetDisplayUnits

`func (o *UpgradeProperty) GetDisplayUnits() string`

GetDisplayUnits returns the DisplayUnits field if non-nil, zero value otherwise.

### GetDisplayUnitsOk

`func (o *UpgradeProperty) GetDisplayUnitsOk() (*string, bool)`

GetDisplayUnitsOk returns a tuple with the DisplayUnits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayUnits

`func (o *UpgradeProperty) SetDisplayUnits(v string)`

SetDisplayUnits sets DisplayUnits field to given value.

### HasDisplayUnits

`func (o *UpgradeProperty) HasDisplayUnits() bool`

HasDisplayUnits returns a boolean if a field has been set.

### SetDisplayUnitsNil

`func (o *UpgradeProperty) SetDisplayUnitsNil(b bool)`

 SetDisplayUnitsNil sets the value for DisplayUnits to be an explicit nil

### UnsetDisplayUnits
`func (o *UpgradeProperty) UnsetDisplayUnits()`

UnsetDisplayUnits ensures that no value is present for DisplayUnits, not even an explicit nil
### GetIcon

`func (o *UpgradeProperty) GetIcon() string`

GetIcon returns the Icon field if non-nil, zero value otherwise.

### GetIconOk

`func (o *UpgradeProperty) GetIconOk() (*string, bool)`

GetIconOk returns a tuple with the Icon field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIcon

`func (o *UpgradeProperty) SetIcon(v string)`

SetIcon sets Icon field to given value.

### HasIcon

`func (o *UpgradeProperty) HasIcon() bool`

HasIcon returns a boolean if a field has been set.

### SetIconNil

`func (o *UpgradeProperty) SetIconNil(b bool)`

 SetIconNil sets the value for Icon to be an explicit nil

### UnsetIcon
`func (o *UpgradeProperty) UnsetIcon()`

UnsetIcon ensures that no value is present for Icon, not even an explicit nil
### GetLabel

`func (o *UpgradeProperty) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *UpgradeProperty) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *UpgradeProperty) SetLabel(v string)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *UpgradeProperty) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### SetLabelNil

`func (o *UpgradeProperty) SetLabelNil(b bool)`

 SetLabelNil sets the value for Label to be an explicit nil

### UnsetLabel
`func (o *UpgradeProperty) UnsetLabel()`

UnsetLabel ensures that no value is present for Label, not even an explicit nil
### GetLocTokenOverride

`func (o *UpgradeProperty) GetLocTokenOverride() string`

GetLocTokenOverride returns the LocTokenOverride field if non-nil, zero value otherwise.

### GetLocTokenOverrideOk

`func (o *UpgradeProperty) GetLocTokenOverrideOk() (*string, bool)`

GetLocTokenOverrideOk returns a tuple with the LocTokenOverride field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocTokenOverride

`func (o *UpgradeProperty) SetLocTokenOverride(v string)`

SetLocTokenOverride sets LocTokenOverride field to given value.

### HasLocTokenOverride

`func (o *UpgradeProperty) HasLocTokenOverride() bool`

HasLocTokenOverride returns a boolean if a field has been set.

### SetLocTokenOverrideNil

`func (o *UpgradeProperty) SetLocTokenOverrideNil(b bool)`

 SetLocTokenOverrideNil sets the value for LocTokenOverride to be an explicit nil

### UnsetLocTokenOverride
`func (o *UpgradeProperty) UnsetLocTokenOverride()`

UnsetLocTokenOverride ensures that no value is present for LocTokenOverride, not even an explicit nil
### GetNegativeAttribute

`func (o *UpgradeProperty) GetNegativeAttribute() bool`

GetNegativeAttribute returns the NegativeAttribute field if non-nil, zero value otherwise.

### GetNegativeAttributeOk

`func (o *UpgradeProperty) GetNegativeAttributeOk() (*bool, bool)`

GetNegativeAttributeOk returns a tuple with the NegativeAttribute field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNegativeAttribute

`func (o *UpgradeProperty) SetNegativeAttribute(v bool)`

SetNegativeAttribute sets NegativeAttribute field to given value.

### HasNegativeAttribute

`func (o *UpgradeProperty) HasNegativeAttribute() bool`

HasNegativeAttribute returns a boolean if a field has been set.

### SetNegativeAttributeNil

`func (o *UpgradeProperty) SetNegativeAttributeNil(b bool)`

 SetNegativeAttributeNil sets the value for NegativeAttribute to be an explicit nil

### UnsetNegativeAttribute
`func (o *UpgradeProperty) UnsetNegativeAttribute()`

UnsetNegativeAttribute ensures that no value is present for NegativeAttribute, not even an explicit nil
### GetPostfix

`func (o *UpgradeProperty) GetPostfix() string`

GetPostfix returns the Postfix field if non-nil, zero value otherwise.

### GetPostfixOk

`func (o *UpgradeProperty) GetPostfixOk() (*string, bool)`

GetPostfixOk returns a tuple with the Postfix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostfix

`func (o *UpgradeProperty) SetPostfix(v string)`

SetPostfix sets Postfix field to given value.

### HasPostfix

`func (o *UpgradeProperty) HasPostfix() bool`

HasPostfix returns a boolean if a field has been set.

### SetPostfixNil

`func (o *UpgradeProperty) SetPostfixNil(b bool)`

 SetPostfixNil sets the value for Postfix to be an explicit nil

### UnsetPostfix
`func (o *UpgradeProperty) UnsetPostfix()`

UnsetPostfix ensures that no value is present for Postfix, not even an explicit nil
### GetPostvalueLabel

`func (o *UpgradeProperty) GetPostvalueLabel() string`

GetPostvalueLabel returns the PostvalueLabel field if non-nil, zero value otherwise.

### GetPostvalueLabelOk

`func (o *UpgradeProperty) GetPostvalueLabelOk() (*string, bool)`

GetPostvalueLabelOk returns a tuple with the PostvalueLabel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostvalueLabel

`func (o *UpgradeProperty) SetPostvalueLabel(v string)`

SetPostvalueLabel sets PostvalueLabel field to given value.

### HasPostvalueLabel

`func (o *UpgradeProperty) HasPostvalueLabel() bool`

HasPostvalueLabel returns a boolean if a field has been set.

### SetPostvalueLabelNil

`func (o *UpgradeProperty) SetPostvalueLabelNil(b bool)`

 SetPostvalueLabelNil sets the value for PostvalueLabel to be an explicit nil

### UnsetPostvalueLabel
`func (o *UpgradeProperty) UnsetPostvalueLabel()`

UnsetPostvalueLabel ensures that no value is present for PostvalueLabel, not even an explicit nil
### GetPrefix

`func (o *UpgradeProperty) GetPrefix() string`

GetPrefix returns the Prefix field if non-nil, zero value otherwise.

### GetPrefixOk

`func (o *UpgradeProperty) GetPrefixOk() (*string, bool)`

GetPrefixOk returns a tuple with the Prefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefix

`func (o *UpgradeProperty) SetPrefix(v string)`

SetPrefix sets Prefix field to given value.

### HasPrefix

`func (o *UpgradeProperty) HasPrefix() bool`

HasPrefix returns a boolean if a field has been set.

### SetPrefixNil

`func (o *UpgradeProperty) SetPrefixNil(b bool)`

 SetPrefixNil sets the value for Prefix to be an explicit nil

### UnsetPrefix
`func (o *UpgradeProperty) UnsetPrefix()`

UnsetPrefix ensures that no value is present for Prefix, not even an explicit nil
### GetProvidedPropertyType

`func (o *UpgradeProperty) GetProvidedPropertyType() string`

GetProvidedPropertyType returns the ProvidedPropertyType field if non-nil, zero value otherwise.

### GetProvidedPropertyTypeOk

`func (o *UpgradeProperty) GetProvidedPropertyTypeOk() (*string, bool)`

GetProvidedPropertyTypeOk returns a tuple with the ProvidedPropertyType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvidedPropertyType

`func (o *UpgradeProperty) SetProvidedPropertyType(v string)`

SetProvidedPropertyType sets ProvidedPropertyType field to given value.

### HasProvidedPropertyType

`func (o *UpgradeProperty) HasProvidedPropertyType() bool`

HasProvidedPropertyType returns a boolean if a field has been set.

### SetProvidedPropertyTypeNil

`func (o *UpgradeProperty) SetProvidedPropertyTypeNil(b bool)`

 SetProvidedPropertyTypeNil sets the value for ProvidedPropertyType to be an explicit nil

### UnsetProvidedPropertyType
`func (o *UpgradeProperty) UnsetProvidedPropertyType()`

UnsetProvidedPropertyType ensures that no value is present for ProvidedPropertyType, not even an explicit nil
### GetRequiredUpgradeBits

`func (o *UpgradeProperty) GetRequiredUpgradeBits() []string`

GetRequiredUpgradeBits returns the RequiredUpgradeBits field if non-nil, zero value otherwise.

### GetRequiredUpgradeBitsOk

`func (o *UpgradeProperty) GetRequiredUpgradeBitsOk() (*[]string, bool)`

GetRequiredUpgradeBitsOk returns a tuple with the RequiredUpgradeBits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequiredUpgradeBits

`func (o *UpgradeProperty) SetRequiredUpgradeBits(v []string)`

SetRequiredUpgradeBits sets RequiredUpgradeBits field to given value.

### HasRequiredUpgradeBits

`func (o *UpgradeProperty) HasRequiredUpgradeBits() bool`

HasRequiredUpgradeBits returns a boolean if a field has been set.

### SetRequiredUpgradeBitsNil

`func (o *UpgradeProperty) SetRequiredUpgradeBitsNil(b bool)`

 SetRequiredUpgradeBitsNil sets the value for RequiredUpgradeBits to be an explicit nil

### UnsetRequiredUpgradeBits
`func (o *UpgradeProperty) UnsetRequiredUpgradeBits()`

UnsetRequiredUpgradeBits ensures that no value is present for RequiredUpgradeBits, not even an explicit nil
### GetScaleFunction

`func (o *UpgradeProperty) GetScaleFunction() RawItemPropertyScaleFunctionSubclass`

GetScaleFunction returns the ScaleFunction field if non-nil, zero value otherwise.

### GetScaleFunctionOk

`func (o *UpgradeProperty) GetScaleFunctionOk() (*RawItemPropertyScaleFunctionSubclass, bool)`

GetScaleFunctionOk returns a tuple with the ScaleFunction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScaleFunction

`func (o *UpgradeProperty) SetScaleFunction(v RawItemPropertyScaleFunctionSubclass)`

SetScaleFunction sets ScaleFunction field to given value.

### HasScaleFunction

`func (o *UpgradeProperty) HasScaleFunction() bool`

HasScaleFunction returns a boolean if a field has been set.

### SetScaleFunctionNil

`func (o *UpgradeProperty) SetScaleFunctionNil(b bool)`

 SetScaleFunctionNil sets the value for ScaleFunction to be an explicit nil

### UnsetScaleFunction
`func (o *UpgradeProperty) UnsetScaleFunction()`

UnsetScaleFunction ensures that no value is present for ScaleFunction, not even an explicit nil
### GetStreetBrawlValue

`func (o *UpgradeProperty) GetStreetBrawlValue() string`

GetStreetBrawlValue returns the StreetBrawlValue field if non-nil, zero value otherwise.

### GetStreetBrawlValueOk

`func (o *UpgradeProperty) GetStreetBrawlValueOk() (*string, bool)`

GetStreetBrawlValueOk returns a tuple with the StreetBrawlValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStreetBrawlValue

`func (o *UpgradeProperty) SetStreetBrawlValue(v string)`

SetStreetBrawlValue sets StreetBrawlValue field to given value.

### HasStreetBrawlValue

`func (o *UpgradeProperty) HasStreetBrawlValue() bool`

HasStreetBrawlValue returns a boolean if a field has been set.

### SetStreetBrawlValueNil

`func (o *UpgradeProperty) SetStreetBrawlValueNil(b bool)`

 SetStreetBrawlValueNil sets the value for StreetBrawlValue to be an explicit nil

### UnsetStreetBrawlValue
`func (o *UpgradeProperty) UnsetStreetBrawlValue()`

UnsetStreetBrawlValue ensures that no value is present for StreetBrawlValue, not even an explicit nil
### GetUsageFlags

`func (o *UpgradeProperty) GetUsageFlags() []StatsUsageFlag`

GetUsageFlags returns the UsageFlags field if non-nil, zero value otherwise.

### GetUsageFlagsOk

`func (o *UpgradeProperty) GetUsageFlagsOk() (*[]StatsUsageFlag, bool)`

GetUsageFlagsOk returns a tuple with the UsageFlags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsageFlags

`func (o *UpgradeProperty) SetUsageFlags(v []StatsUsageFlag)`

SetUsageFlags sets UsageFlags field to given value.

### HasUsageFlags

`func (o *UpgradeProperty) HasUsageFlags() bool`

HasUsageFlags returns a boolean if a field has been set.

### SetUsageFlagsNil

`func (o *UpgradeProperty) SetUsageFlagsNil(b bool)`

 SetUsageFlagsNil sets the value for UsageFlags to be an explicit nil

### UnsetUsageFlags
`func (o *UpgradeProperty) UnsetUsageFlags()`

UnsetUsageFlags ensures that no value is present for UsageFlags, not even an explicit nil
### GetValue

`func (o *UpgradeProperty) GetValue() string`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *UpgradeProperty) GetValueOk() (*string, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *UpgradeProperty) SetValue(v string)`

SetValue sets Value field to given value.

### HasValue

`func (o *UpgradeProperty) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValueNil

`func (o *UpgradeProperty) SetValueNil(b bool)`

 SetValueNil sets the value for Value to be an explicit nil

### UnsetValue
`func (o *UpgradeProperty) UnsetValue()`

UnsetValue ensures that no value is present for Value, not even an explicit nil
### GetTooltipIsElevated

`func (o *UpgradeProperty) GetTooltipIsElevated() bool`

GetTooltipIsElevated returns the TooltipIsElevated field if non-nil, zero value otherwise.

### GetTooltipIsElevatedOk

`func (o *UpgradeProperty) GetTooltipIsElevatedOk() (*bool, bool)`

GetTooltipIsElevatedOk returns a tuple with the TooltipIsElevated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipIsElevated

`func (o *UpgradeProperty) SetTooltipIsElevated(v bool)`

SetTooltipIsElevated sets TooltipIsElevated field to given value.

### HasTooltipIsElevated

`func (o *UpgradeProperty) HasTooltipIsElevated() bool`

HasTooltipIsElevated returns a boolean if a field has been set.

### SetTooltipIsElevatedNil

`func (o *UpgradeProperty) SetTooltipIsElevatedNil(b bool)`

 SetTooltipIsElevatedNil sets the value for TooltipIsElevated to be an explicit nil

### UnsetTooltipIsElevated
`func (o *UpgradeProperty) UnsetTooltipIsElevated()`

UnsetTooltipIsElevated ensures that no value is present for TooltipIsElevated, not even an explicit nil
### GetTooltipIsImportant

`func (o *UpgradeProperty) GetTooltipIsImportant() bool`

GetTooltipIsImportant returns the TooltipIsImportant field if non-nil, zero value otherwise.

### GetTooltipIsImportantOk

`func (o *UpgradeProperty) GetTooltipIsImportantOk() (*bool, bool)`

GetTooltipIsImportantOk returns a tuple with the TooltipIsImportant field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipIsImportant

`func (o *UpgradeProperty) SetTooltipIsImportant(v bool)`

SetTooltipIsImportant sets TooltipIsImportant field to given value.

### HasTooltipIsImportant

`func (o *UpgradeProperty) HasTooltipIsImportant() bool`

HasTooltipIsImportant returns a boolean if a field has been set.

### SetTooltipIsImportantNil

`func (o *UpgradeProperty) SetTooltipIsImportantNil(b bool)`

 SetTooltipIsImportantNil sets the value for TooltipIsImportant to be an explicit nil

### UnsetTooltipIsImportant
`func (o *UpgradeProperty) UnsetTooltipIsImportant()`

UnsetTooltipIsImportant ensures that no value is present for TooltipIsImportant, not even an explicit nil
### GetTooltipSection

`func (o *UpgradeProperty) GetTooltipSection() AbilitySectionType`

GetTooltipSection returns the TooltipSection field if non-nil, zero value otherwise.

### GetTooltipSectionOk

`func (o *UpgradeProperty) GetTooltipSectionOk() (*AbilitySectionType, bool)`

GetTooltipSectionOk returns a tuple with the TooltipSection field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipSection

`func (o *UpgradeProperty) SetTooltipSection(v AbilitySectionType)`

SetTooltipSection sets TooltipSection field to given value.

### HasTooltipSection

`func (o *UpgradeProperty) HasTooltipSection() bool`

HasTooltipSection returns a boolean if a field has been set.

### SetTooltipSectionNil

`func (o *UpgradeProperty) SetTooltipSectionNil(b bool)`

 SetTooltipSectionNil sets the value for TooltipSection to be an explicit nil

### UnsetTooltipSection
`func (o *UpgradeProperty) UnsetTooltipSection()`

UnsetTooltipSection ensures that no value is present for TooltipSection, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


