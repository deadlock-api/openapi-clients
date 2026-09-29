# CorruptedPenaltyEffect

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BonusPerTier** | **[]float64** | Penalty value indexed by item tier (same indexing as &#x60;item_price_per_tier&#x60;; tiers that can&#39;t be corrupted are &#x60;0&#x60;), in display units: distances are meters (source suffix &#x60;m&#x60; stripped), matching &#x60;postfix&#x60;. | 
**CssClass** | Pointer to **NullableString** |  | [optional] 
**Display** | **bool** | &#x60;false&#x60; for effects the game applies but doesn&#39;t list in tooltips. | 
**DisplayType** | Pointer to **NullableString** |  | [optional] 
**Label** | Pointer to **NullableString** | Localized stat label (from &#x60;loc_token_override&#x60;). | [optional] 
**LocTokenOverride** | Pointer to **NullableString** |  | [optional] 
**ModifierValue** | **string** | Modifier the penalty applies, e.g. &#x60;MODIFIER_VALUE_COOLDOWN_REDUCTION_PERCENTAGE&#x60;. | 
**Postfix** | Pointer to **NullableString** | Localized unit suffix, e.g. &#x60;%&#x60; or &#x60; m&#x60;. | [optional] 

## Methods

### NewCorruptedPenaltyEffect

`func NewCorruptedPenaltyEffect(bonusPerTier []float64, display bool, modifierValue string, ) *CorruptedPenaltyEffect`

NewCorruptedPenaltyEffect instantiates a new CorruptedPenaltyEffect object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCorruptedPenaltyEffectWithDefaults

`func NewCorruptedPenaltyEffectWithDefaults() *CorruptedPenaltyEffect`

NewCorruptedPenaltyEffectWithDefaults instantiates a new CorruptedPenaltyEffect object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBonusPerTier

`func (o *CorruptedPenaltyEffect) GetBonusPerTier() []float64`

GetBonusPerTier returns the BonusPerTier field if non-nil, zero value otherwise.

### GetBonusPerTierOk

`func (o *CorruptedPenaltyEffect) GetBonusPerTierOk() (*[]float64, bool)`

GetBonusPerTierOk returns a tuple with the BonusPerTier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBonusPerTier

`func (o *CorruptedPenaltyEffect) SetBonusPerTier(v []float64)`

SetBonusPerTier sets BonusPerTier field to given value.


### GetCssClass

`func (o *CorruptedPenaltyEffect) GetCssClass() string`

GetCssClass returns the CssClass field if non-nil, zero value otherwise.

### GetCssClassOk

`func (o *CorruptedPenaltyEffect) GetCssClassOk() (*string, bool)`

GetCssClassOk returns a tuple with the CssClass field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCssClass

`func (o *CorruptedPenaltyEffect) SetCssClass(v string)`

SetCssClass sets CssClass field to given value.

### HasCssClass

`func (o *CorruptedPenaltyEffect) HasCssClass() bool`

HasCssClass returns a boolean if a field has been set.

### SetCssClassNil

`func (o *CorruptedPenaltyEffect) SetCssClassNil(b bool)`

 SetCssClassNil sets the value for CssClass to be an explicit nil

### UnsetCssClass
`func (o *CorruptedPenaltyEffect) UnsetCssClass()`

UnsetCssClass ensures that no value is present for CssClass, not even an explicit nil
### GetDisplay

`func (o *CorruptedPenaltyEffect) GetDisplay() bool`

GetDisplay returns the Display field if non-nil, zero value otherwise.

### GetDisplayOk

`func (o *CorruptedPenaltyEffect) GetDisplayOk() (*bool, bool)`

GetDisplayOk returns a tuple with the Display field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplay

`func (o *CorruptedPenaltyEffect) SetDisplay(v bool)`

SetDisplay sets Display field to given value.


### GetDisplayType

`func (o *CorruptedPenaltyEffect) GetDisplayType() string`

GetDisplayType returns the DisplayType field if non-nil, zero value otherwise.

### GetDisplayTypeOk

`func (o *CorruptedPenaltyEffect) GetDisplayTypeOk() (*string, bool)`

GetDisplayTypeOk returns a tuple with the DisplayType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayType

`func (o *CorruptedPenaltyEffect) SetDisplayType(v string)`

SetDisplayType sets DisplayType field to given value.

### HasDisplayType

`func (o *CorruptedPenaltyEffect) HasDisplayType() bool`

HasDisplayType returns a boolean if a field has been set.

### SetDisplayTypeNil

`func (o *CorruptedPenaltyEffect) SetDisplayTypeNil(b bool)`

 SetDisplayTypeNil sets the value for DisplayType to be an explicit nil

### UnsetDisplayType
`func (o *CorruptedPenaltyEffect) UnsetDisplayType()`

UnsetDisplayType ensures that no value is present for DisplayType, not even an explicit nil
### GetLabel

`func (o *CorruptedPenaltyEffect) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *CorruptedPenaltyEffect) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *CorruptedPenaltyEffect) SetLabel(v string)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *CorruptedPenaltyEffect) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### SetLabelNil

`func (o *CorruptedPenaltyEffect) SetLabelNil(b bool)`

 SetLabelNil sets the value for Label to be an explicit nil

### UnsetLabel
`func (o *CorruptedPenaltyEffect) UnsetLabel()`

UnsetLabel ensures that no value is present for Label, not even an explicit nil
### GetLocTokenOverride

`func (o *CorruptedPenaltyEffect) GetLocTokenOverride() string`

GetLocTokenOverride returns the LocTokenOverride field if non-nil, zero value otherwise.

### GetLocTokenOverrideOk

`func (o *CorruptedPenaltyEffect) GetLocTokenOverrideOk() (*string, bool)`

GetLocTokenOverrideOk returns a tuple with the LocTokenOverride field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocTokenOverride

`func (o *CorruptedPenaltyEffect) SetLocTokenOverride(v string)`

SetLocTokenOverride sets LocTokenOverride field to given value.

### HasLocTokenOverride

`func (o *CorruptedPenaltyEffect) HasLocTokenOverride() bool`

HasLocTokenOverride returns a boolean if a field has been set.

### SetLocTokenOverrideNil

`func (o *CorruptedPenaltyEffect) SetLocTokenOverrideNil(b bool)`

 SetLocTokenOverrideNil sets the value for LocTokenOverride to be an explicit nil

### UnsetLocTokenOverride
`func (o *CorruptedPenaltyEffect) UnsetLocTokenOverride()`

UnsetLocTokenOverride ensures that no value is present for LocTokenOverride, not even an explicit nil
### GetModifierValue

`func (o *CorruptedPenaltyEffect) GetModifierValue() string`

GetModifierValue returns the ModifierValue field if non-nil, zero value otherwise.

### GetModifierValueOk

`func (o *CorruptedPenaltyEffect) GetModifierValueOk() (*string, bool)`

GetModifierValueOk returns a tuple with the ModifierValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifierValue

`func (o *CorruptedPenaltyEffect) SetModifierValue(v string)`

SetModifierValue sets ModifierValue field to given value.


### GetPostfix

`func (o *CorruptedPenaltyEffect) GetPostfix() string`

GetPostfix returns the Postfix field if non-nil, zero value otherwise.

### GetPostfixOk

`func (o *CorruptedPenaltyEffect) GetPostfixOk() (*string, bool)`

GetPostfixOk returns a tuple with the Postfix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostfix

`func (o *CorruptedPenaltyEffect) SetPostfix(v string)`

SetPostfix sets Postfix field to given value.

### HasPostfix

`func (o *CorruptedPenaltyEffect) HasPostfix() bool`

HasPostfix returns a boolean if a field has been set.

### SetPostfixNil

`func (o *CorruptedPenaltyEffect) SetPostfixNil(b bool)`

 SetPostfixNil sets the value for Postfix to be an explicit nil

### UnsetPostfix
`func (o *CorruptedPenaltyEffect) UnsetPostfix()`

UnsetPostfix ensures that no value is present for Postfix, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


