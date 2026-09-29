# CorruptedItemInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ExcludedPenalties** | **[]string** | Names of corrupted penalty definitions (&#x60;generic_data&#x60;) that can never roll on this item. | 
**PropertyUpgrades** | [**[]RawAbilityUpgradePropertyUpgrade**](RawAbilityUpgradePropertyUpgrade.md) | Property bonuses the corrupted variant gains. | 

## Methods

### NewCorruptedItemInfo

`func NewCorruptedItemInfo(excludedPenalties []string, propertyUpgrades []RawAbilityUpgradePropertyUpgrade, ) *CorruptedItemInfo`

NewCorruptedItemInfo instantiates a new CorruptedItemInfo object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCorruptedItemInfoWithDefaults

`func NewCorruptedItemInfoWithDefaults() *CorruptedItemInfo`

NewCorruptedItemInfoWithDefaults instantiates a new CorruptedItemInfo object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetExcludedPenalties

`func (o *CorruptedItemInfo) GetExcludedPenalties() []string`

GetExcludedPenalties returns the ExcludedPenalties field if non-nil, zero value otherwise.

### GetExcludedPenaltiesOk

`func (o *CorruptedItemInfo) GetExcludedPenaltiesOk() (*[]string, bool)`

GetExcludedPenaltiesOk returns a tuple with the ExcludedPenalties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludedPenalties

`func (o *CorruptedItemInfo) SetExcludedPenalties(v []string)`

SetExcludedPenalties sets ExcludedPenalties field to given value.


### GetPropertyUpgrades

`func (o *CorruptedItemInfo) GetPropertyUpgrades() []RawAbilityUpgradePropertyUpgrade`

GetPropertyUpgrades returns the PropertyUpgrades field if non-nil, zero value otherwise.

### GetPropertyUpgradesOk

`func (o *CorruptedItemInfo) GetPropertyUpgradesOk() (*[]RawAbilityUpgradePropertyUpgrade, bool)`

GetPropertyUpgradesOk returns a tuple with the PropertyUpgrades field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPropertyUpgrades

`func (o *CorruptedItemInfo) SetPropertyUpgrades(v []RawAbilityUpgradePropertyUpgrade)`

SetPropertyUpgrades sets PropertyUpgrades field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


