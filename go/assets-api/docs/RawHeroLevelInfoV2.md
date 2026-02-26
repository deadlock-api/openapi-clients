# RawHeroLevelInfoV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**UseStandardUpgrade** | Pointer to **NullableBool** |  | [optional] 
**BonusCurrencies** | Pointer to **map[string]int32** |  | [optional] 
**RequiredGold** | **int32** |  | 

## Methods

### NewRawHeroLevelInfoV2

`func NewRawHeroLevelInfoV2(requiredGold int32, ) *RawHeroLevelInfoV2`

NewRawHeroLevelInfoV2 instantiates a new RawHeroLevelInfoV2 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRawHeroLevelInfoV2WithDefaults

`func NewRawHeroLevelInfoV2WithDefaults() *RawHeroLevelInfoV2`

NewRawHeroLevelInfoV2WithDefaults instantiates a new RawHeroLevelInfoV2 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUseStandardUpgrade

`func (o *RawHeroLevelInfoV2) GetUseStandardUpgrade() bool`

GetUseStandardUpgrade returns the UseStandardUpgrade field if non-nil, zero value otherwise.

### GetUseStandardUpgradeOk

`func (o *RawHeroLevelInfoV2) GetUseStandardUpgradeOk() (*bool, bool)`

GetUseStandardUpgradeOk returns a tuple with the UseStandardUpgrade field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUseStandardUpgrade

`func (o *RawHeroLevelInfoV2) SetUseStandardUpgrade(v bool)`

SetUseStandardUpgrade sets UseStandardUpgrade field to given value.

### HasUseStandardUpgrade

`func (o *RawHeroLevelInfoV2) HasUseStandardUpgrade() bool`

HasUseStandardUpgrade returns a boolean if a field has been set.

### SetUseStandardUpgradeNil

`func (o *RawHeroLevelInfoV2) SetUseStandardUpgradeNil(b bool)`

 SetUseStandardUpgradeNil sets the value for UseStandardUpgrade to be an explicit nil

### UnsetUseStandardUpgrade
`func (o *RawHeroLevelInfoV2) UnsetUseStandardUpgrade()`

UnsetUseStandardUpgrade ensures that no value is present for UseStandardUpgrade, not even an explicit nil
### GetBonusCurrencies

`func (o *RawHeroLevelInfoV2) GetBonusCurrencies() map[string]int32`

GetBonusCurrencies returns the BonusCurrencies field if non-nil, zero value otherwise.

### GetBonusCurrenciesOk

`func (o *RawHeroLevelInfoV2) GetBonusCurrenciesOk() (*map[string]int32, bool)`

GetBonusCurrenciesOk returns a tuple with the BonusCurrencies field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBonusCurrencies

`func (o *RawHeroLevelInfoV2) SetBonusCurrencies(v map[string]int32)`

SetBonusCurrencies sets BonusCurrencies field to given value.

### HasBonusCurrencies

`func (o *RawHeroLevelInfoV2) HasBonusCurrencies() bool`

HasBonusCurrencies returns a boolean if a field has been set.

### SetBonusCurrenciesNil

`func (o *RawHeroLevelInfoV2) SetBonusCurrenciesNil(b bool)`

 SetBonusCurrenciesNil sets the value for BonusCurrencies to be an explicit nil

### UnsetBonusCurrencies
`func (o *RawHeroLevelInfoV2) UnsetBonusCurrencies()`

UnsetBonusCurrencies ensures that no value is present for BonusCurrencies, not even an explicit nil
### GetRequiredGold

`func (o *RawHeroLevelInfoV2) GetRequiredGold() int32`

GetRequiredGold returns the RequiredGold field if non-nil, zero value otherwise.

### GetRequiredGoldOk

`func (o *RawHeroLevelInfoV2) GetRequiredGoldOk() (*int32, bool)`

GetRequiredGoldOk returns a tuple with the RequiredGold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequiredGold

`func (o *RawHeroLevelInfoV2) SetRequiredGold(v int32)`

SetRequiredGold sets RequiredGold field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


