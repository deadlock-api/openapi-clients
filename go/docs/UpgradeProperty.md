# UpgradeProperty

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CanSetTokenOverride** | Pointer to **bool** |  | [optional] 
**Conditional** | Pointer to **string** |  | [optional] 
**CssClass** | Pointer to **string** |  | [optional] 
**DisableValue** | Pointer to **string** |  | [optional] 
**DisplayUnits** | Pointer to **string** |  | [optional] 
**Icon** | Pointer to **string** |  | [optional] 
**Label** | Pointer to **string** |  | [optional] 
**LocTokenOverride** | Pointer to **string** |  | [optional] 
**NegativeAttribute** | Pointer to **bool** |  | [optional] 
**Postfix** | Pointer to **string** |  | [optional] 
**PostvalueLabel** | Pointer to **string** |  | [optional] 
**Prefix** | Pointer to **string** |  | [optional] 
**ProvidedPropertyType** | Pointer to **string** |  | [optional] 
**ScaleFunction** | Pointer to [**RawItemPropertyScaleFunctionSubclass**](RawItemPropertyScaleFunctionSubclass.md) |  | [optional] 
**StreetBrawlValue** | Pointer to **string** |  | [optional] 
**UsageFlags** | Pointer to [**[]StatsUsageFlag**](StatsUsageFlag.md) |  | [optional] 
**Value** | Pointer to **string** | Raw JSON value preserves the source distinction between numeric and stringly-typed bonuses (&#x60;\&quot;14.5\&quot;&#x60; vs &#x60;14.5&#x60;). | [optional] 
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


