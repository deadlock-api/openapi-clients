# HeroStatsUI

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DisplayStats** | [**[]HeroStatsUIDisplay**](HeroStatsUIDisplay.md) |  | 
**WeaponStatDisplay** | **string** |  | 

## Methods

### NewHeroStatsUI

`func NewHeroStatsUI(displayStats []HeroStatsUIDisplay, weaponStatDisplay string, ) *HeroStatsUI`

NewHeroStatsUI instantiates a new HeroStatsUI object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHeroStatsUIWithDefaults

`func NewHeroStatsUIWithDefaults() *HeroStatsUI`

NewHeroStatsUIWithDefaults instantiates a new HeroStatsUI object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDisplayStats

`func (o *HeroStatsUI) GetDisplayStats() []HeroStatsUIDisplay`

GetDisplayStats returns the DisplayStats field if non-nil, zero value otherwise.

### GetDisplayStatsOk

`func (o *HeroStatsUI) GetDisplayStatsOk() (*[]HeroStatsUIDisplay, bool)`

GetDisplayStatsOk returns a tuple with the DisplayStats field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayStats

`func (o *HeroStatsUI) SetDisplayStats(v []HeroStatsUIDisplay)`

SetDisplayStats sets DisplayStats field to given value.


### GetWeaponStatDisplay

`func (o *HeroStatsUI) GetWeaponStatDisplay() string`

GetWeaponStatDisplay returns the WeaponStatDisplay field if non-nil, zero value otherwise.

### GetWeaponStatDisplayOk

`func (o *HeroStatsUI) GetWeaponStatDisplayOk() (*string, bool)`

GetWeaponStatDisplayOk returns a tuple with the WeaponStatDisplay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponStatDisplay

`func (o *HeroStatsUI) SetWeaponStatDisplay(v string)`

SetWeaponStatDisplay sets WeaponStatDisplay field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


