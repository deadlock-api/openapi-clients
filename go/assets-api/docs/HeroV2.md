# HeroV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** |  | 
**ClassName** | **string** |  | 
**Name** | **string** |  | 
**Description** | [**HeroDescriptionV2**](HeroDescriptionV2.md) |  | 
**ItemDraftWeights** | Pointer to **map[string]float32** |  | [optional] 
**PlayerSelectable** | **bool** |  | 
**Disabled** | **bool** |  | 
**InDevelopment** | **bool** |  | 
**NeedsTesting** | **bool** |  | 
**AssignedPlayersOnly** | **bool** |  | 
**Tags** | Pointer to **[]string** |  | [optional] 
**GunTag** | Pointer to **NullableString** |  | [optional] 
**HideoutRichPresence** | Pointer to **NullableString** |  | [optional] 
**HeroType** | Pointer to [**NullableHeroTypeV2**](HeroTypeV2.md) |  | [optional] 
**PrereleaseOnly** | Pointer to **NullableBool** |  | [optional] 
**LimitedTesting** | **bool** |  | 
**Complexity** | **int32** |  | 
**Skin** | **int32** |  | 
**Images** | [**HeroImagesV2**](HeroImagesV2.md) |  | 
**Items** | **map[string]string** |  | 
**StartingStats** | [**HeroStartingStatsV2**](HeroStartingStatsV2.md) |  | 
**ItemSlotInfo** | [**map[string]RawHeroItemSlotInfoValueV2**](RawHeroItemSlotInfoValueV2.md) |  | 
**Physics** | [**HeroPhysicsV2**](HeroPhysicsV2.md) |  | 
**Colors** | [**HeroColorsV2**](HeroColorsV2.md) |  | 
**ShopStatDisplay** | [**HeroShopStatDisplayV2**](HeroShopStatDisplayV2.md) |  | 
**CostBonuses** | Pointer to [**map[string][]RawHeroMapModCostBonusesV2**](array.md) |  | [optional] 
**StatsDisplay** | [**RawHeroStatsDisplayV2**](RawHeroStatsDisplayV2.md) |  | 
**HeroStatsUi** | [**RawHeroStatsUIV2**](RawHeroStatsUIV2.md) |  | 
**LevelInfo** | [**map[string]HeroLevelInfoV2**](HeroLevelInfoV2.md) |  | 
**ScalingStats** | [**map[string]RawHeroScalingStatV2**](RawHeroScalingStatV2.md) |  | 
**PurchaseBonuses** | [**map[string][]RawHeroPurchaseBonusV2**](array.md) |  | 
**StandardLevelUpUpgrades** | **map[string]float32** |  | 

## Methods

### NewHeroV2

`func NewHeroV2(id int32, className string, name string, description HeroDescriptionV2, playerSelectable bool, disabled bool, inDevelopment bool, needsTesting bool, assignedPlayersOnly bool, limitedTesting bool, complexity int32, skin int32, images HeroImagesV2, items map[string]string, startingStats HeroStartingStatsV2, itemSlotInfo map[string]RawHeroItemSlotInfoValueV2, physics HeroPhysicsV2, colors HeroColorsV2, shopStatDisplay HeroShopStatDisplayV2, statsDisplay RawHeroStatsDisplayV2, heroStatsUi RawHeroStatsUIV2, levelInfo map[string]HeroLevelInfoV2, scalingStats map[string]RawHeroScalingStatV2, purchaseBonuses map[string][]RawHeroPurchaseBonusV2, standardLevelUpUpgrades map[string]float32, ) *HeroV2`

NewHeroV2 instantiates a new HeroV2 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHeroV2WithDefaults

`func NewHeroV2WithDefaults() *HeroV2`

NewHeroV2WithDefaults instantiates a new HeroV2 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *HeroV2) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *HeroV2) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *HeroV2) SetId(v int32)`

SetId sets Id field to given value.


### GetClassName

`func (o *HeroV2) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *HeroV2) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *HeroV2) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetName

`func (o *HeroV2) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *HeroV2) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *HeroV2) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *HeroV2) GetDescription() HeroDescriptionV2`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *HeroV2) GetDescriptionOk() (*HeroDescriptionV2, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *HeroV2) SetDescription(v HeroDescriptionV2)`

SetDescription sets Description field to given value.


### GetItemDraftWeights

`func (o *HeroV2) GetItemDraftWeights() map[string]float32`

GetItemDraftWeights returns the ItemDraftWeights field if non-nil, zero value otherwise.

### GetItemDraftWeightsOk

`func (o *HeroV2) GetItemDraftWeightsOk() (*map[string]float32, bool)`

GetItemDraftWeightsOk returns a tuple with the ItemDraftWeights field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemDraftWeights

`func (o *HeroV2) SetItemDraftWeights(v map[string]float32)`

SetItemDraftWeights sets ItemDraftWeights field to given value.

### HasItemDraftWeights

`func (o *HeroV2) HasItemDraftWeights() bool`

HasItemDraftWeights returns a boolean if a field has been set.

### SetItemDraftWeightsNil

`func (o *HeroV2) SetItemDraftWeightsNil(b bool)`

 SetItemDraftWeightsNil sets the value for ItemDraftWeights to be an explicit nil

### UnsetItemDraftWeights
`func (o *HeroV2) UnsetItemDraftWeights()`

UnsetItemDraftWeights ensures that no value is present for ItemDraftWeights, not even an explicit nil
### GetPlayerSelectable

`func (o *HeroV2) GetPlayerSelectable() bool`

GetPlayerSelectable returns the PlayerSelectable field if non-nil, zero value otherwise.

### GetPlayerSelectableOk

`func (o *HeroV2) GetPlayerSelectableOk() (*bool, bool)`

GetPlayerSelectableOk returns a tuple with the PlayerSelectable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerSelectable

`func (o *HeroV2) SetPlayerSelectable(v bool)`

SetPlayerSelectable sets PlayerSelectable field to given value.


### GetDisabled

`func (o *HeroV2) GetDisabled() bool`

GetDisabled returns the Disabled field if non-nil, zero value otherwise.

### GetDisabledOk

`func (o *HeroV2) GetDisabledOk() (*bool, bool)`

GetDisabledOk returns a tuple with the Disabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisabled

`func (o *HeroV2) SetDisabled(v bool)`

SetDisabled sets Disabled field to given value.


### GetInDevelopment

`func (o *HeroV2) GetInDevelopment() bool`

GetInDevelopment returns the InDevelopment field if non-nil, zero value otherwise.

### GetInDevelopmentOk

`func (o *HeroV2) GetInDevelopmentOk() (*bool, bool)`

GetInDevelopmentOk returns a tuple with the InDevelopment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInDevelopment

`func (o *HeroV2) SetInDevelopment(v bool)`

SetInDevelopment sets InDevelopment field to given value.


### GetNeedsTesting

`func (o *HeroV2) GetNeedsTesting() bool`

GetNeedsTesting returns the NeedsTesting field if non-nil, zero value otherwise.

### GetNeedsTestingOk

`func (o *HeroV2) GetNeedsTestingOk() (*bool, bool)`

GetNeedsTestingOk returns a tuple with the NeedsTesting field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNeedsTesting

`func (o *HeroV2) SetNeedsTesting(v bool)`

SetNeedsTesting sets NeedsTesting field to given value.


### GetAssignedPlayersOnly

`func (o *HeroV2) GetAssignedPlayersOnly() bool`

GetAssignedPlayersOnly returns the AssignedPlayersOnly field if non-nil, zero value otherwise.

### GetAssignedPlayersOnlyOk

`func (o *HeroV2) GetAssignedPlayersOnlyOk() (*bool, bool)`

GetAssignedPlayersOnlyOk returns a tuple with the AssignedPlayersOnly field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssignedPlayersOnly

`func (o *HeroV2) SetAssignedPlayersOnly(v bool)`

SetAssignedPlayersOnly sets AssignedPlayersOnly field to given value.


### GetTags

`func (o *HeroV2) GetTags() []string`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *HeroV2) GetTagsOk() (*[]string, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTags

`func (o *HeroV2) SetTags(v []string)`

SetTags sets Tags field to given value.

### HasTags

`func (o *HeroV2) HasTags() bool`

HasTags returns a boolean if a field has been set.

### SetTagsNil

`func (o *HeroV2) SetTagsNil(b bool)`

 SetTagsNil sets the value for Tags to be an explicit nil

### UnsetTags
`func (o *HeroV2) UnsetTags()`

UnsetTags ensures that no value is present for Tags, not even an explicit nil
### GetGunTag

`func (o *HeroV2) GetGunTag() string`

GetGunTag returns the GunTag field if non-nil, zero value otherwise.

### GetGunTagOk

`func (o *HeroV2) GetGunTagOk() (*string, bool)`

GetGunTagOk returns a tuple with the GunTag field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGunTag

`func (o *HeroV2) SetGunTag(v string)`

SetGunTag sets GunTag field to given value.

### HasGunTag

`func (o *HeroV2) HasGunTag() bool`

HasGunTag returns a boolean if a field has been set.

### SetGunTagNil

`func (o *HeroV2) SetGunTagNil(b bool)`

 SetGunTagNil sets the value for GunTag to be an explicit nil

### UnsetGunTag
`func (o *HeroV2) UnsetGunTag()`

UnsetGunTag ensures that no value is present for GunTag, not even an explicit nil
### GetHideoutRichPresence

`func (o *HeroV2) GetHideoutRichPresence() string`

GetHideoutRichPresence returns the HideoutRichPresence field if non-nil, zero value otherwise.

### GetHideoutRichPresenceOk

`func (o *HeroV2) GetHideoutRichPresenceOk() (*string, bool)`

GetHideoutRichPresenceOk returns a tuple with the HideoutRichPresence field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHideoutRichPresence

`func (o *HeroV2) SetHideoutRichPresence(v string)`

SetHideoutRichPresence sets HideoutRichPresence field to given value.

### HasHideoutRichPresence

`func (o *HeroV2) HasHideoutRichPresence() bool`

HasHideoutRichPresence returns a boolean if a field has been set.

### SetHideoutRichPresenceNil

`func (o *HeroV2) SetHideoutRichPresenceNil(b bool)`

 SetHideoutRichPresenceNil sets the value for HideoutRichPresence to be an explicit nil

### UnsetHideoutRichPresence
`func (o *HeroV2) UnsetHideoutRichPresence()`

UnsetHideoutRichPresence ensures that no value is present for HideoutRichPresence, not even an explicit nil
### GetHeroType

`func (o *HeroV2) GetHeroType() HeroTypeV2`

GetHeroType returns the HeroType field if non-nil, zero value otherwise.

### GetHeroTypeOk

`func (o *HeroV2) GetHeroTypeOk() (*HeroTypeV2, bool)`

GetHeroTypeOk returns a tuple with the HeroType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroType

`func (o *HeroV2) SetHeroType(v HeroTypeV2)`

SetHeroType sets HeroType field to given value.

### HasHeroType

`func (o *HeroV2) HasHeroType() bool`

HasHeroType returns a boolean if a field has been set.

### SetHeroTypeNil

`func (o *HeroV2) SetHeroTypeNil(b bool)`

 SetHeroTypeNil sets the value for HeroType to be an explicit nil

### UnsetHeroType
`func (o *HeroV2) UnsetHeroType()`

UnsetHeroType ensures that no value is present for HeroType, not even an explicit nil
### GetPrereleaseOnly

`func (o *HeroV2) GetPrereleaseOnly() bool`

GetPrereleaseOnly returns the PrereleaseOnly field if non-nil, zero value otherwise.

### GetPrereleaseOnlyOk

`func (o *HeroV2) GetPrereleaseOnlyOk() (*bool, bool)`

GetPrereleaseOnlyOk returns a tuple with the PrereleaseOnly field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrereleaseOnly

`func (o *HeroV2) SetPrereleaseOnly(v bool)`

SetPrereleaseOnly sets PrereleaseOnly field to given value.

### HasPrereleaseOnly

`func (o *HeroV2) HasPrereleaseOnly() bool`

HasPrereleaseOnly returns a boolean if a field has been set.

### SetPrereleaseOnlyNil

`func (o *HeroV2) SetPrereleaseOnlyNil(b bool)`

 SetPrereleaseOnlyNil sets the value for PrereleaseOnly to be an explicit nil

### UnsetPrereleaseOnly
`func (o *HeroV2) UnsetPrereleaseOnly()`

UnsetPrereleaseOnly ensures that no value is present for PrereleaseOnly, not even an explicit nil
### GetLimitedTesting

`func (o *HeroV2) GetLimitedTesting() bool`

GetLimitedTesting returns the LimitedTesting field if non-nil, zero value otherwise.

### GetLimitedTestingOk

`func (o *HeroV2) GetLimitedTestingOk() (*bool, bool)`

GetLimitedTestingOk returns a tuple with the LimitedTesting field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimitedTesting

`func (o *HeroV2) SetLimitedTesting(v bool)`

SetLimitedTesting sets LimitedTesting field to given value.


### GetComplexity

`func (o *HeroV2) GetComplexity() int32`

GetComplexity returns the Complexity field if non-nil, zero value otherwise.

### GetComplexityOk

`func (o *HeroV2) GetComplexityOk() (*int32, bool)`

GetComplexityOk returns a tuple with the Complexity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComplexity

`func (o *HeroV2) SetComplexity(v int32)`

SetComplexity sets Complexity field to given value.


### GetSkin

`func (o *HeroV2) GetSkin() int32`

GetSkin returns the Skin field if non-nil, zero value otherwise.

### GetSkinOk

`func (o *HeroV2) GetSkinOk() (*int32, bool)`

GetSkinOk returns a tuple with the Skin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSkin

`func (o *HeroV2) SetSkin(v int32)`

SetSkin sets Skin field to given value.


### GetImages

`func (o *HeroV2) GetImages() HeroImagesV2`

GetImages returns the Images field if non-nil, zero value otherwise.

### GetImagesOk

`func (o *HeroV2) GetImagesOk() (*HeroImagesV2, bool)`

GetImagesOk returns a tuple with the Images field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImages

`func (o *HeroV2) SetImages(v HeroImagesV2)`

SetImages sets Images field to given value.


### GetItems

`func (o *HeroV2) GetItems() map[string]string`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *HeroV2) GetItemsOk() (*map[string]string, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *HeroV2) SetItems(v map[string]string)`

SetItems sets Items field to given value.


### GetStartingStats

`func (o *HeroV2) GetStartingStats() HeroStartingStatsV2`

GetStartingStats returns the StartingStats field if non-nil, zero value otherwise.

### GetStartingStatsOk

`func (o *HeroV2) GetStartingStatsOk() (*HeroStartingStatsV2, bool)`

GetStartingStatsOk returns a tuple with the StartingStats field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartingStats

`func (o *HeroV2) SetStartingStats(v HeroStartingStatsV2)`

SetStartingStats sets StartingStats field to given value.


### GetItemSlotInfo

`func (o *HeroV2) GetItemSlotInfo() map[string]RawHeroItemSlotInfoValueV2`

GetItemSlotInfo returns the ItemSlotInfo field if non-nil, zero value otherwise.

### GetItemSlotInfoOk

`func (o *HeroV2) GetItemSlotInfoOk() (*map[string]RawHeroItemSlotInfoValueV2, bool)`

GetItemSlotInfoOk returns a tuple with the ItemSlotInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemSlotInfo

`func (o *HeroV2) SetItemSlotInfo(v map[string]RawHeroItemSlotInfoValueV2)`

SetItemSlotInfo sets ItemSlotInfo field to given value.


### GetPhysics

`func (o *HeroV2) GetPhysics() HeroPhysicsV2`

GetPhysics returns the Physics field if non-nil, zero value otherwise.

### GetPhysicsOk

`func (o *HeroV2) GetPhysicsOk() (*HeroPhysicsV2, bool)`

GetPhysicsOk returns a tuple with the Physics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPhysics

`func (o *HeroV2) SetPhysics(v HeroPhysicsV2)`

SetPhysics sets Physics field to given value.


### GetColors

`func (o *HeroV2) GetColors() HeroColorsV2`

GetColors returns the Colors field if non-nil, zero value otherwise.

### GetColorsOk

`func (o *HeroV2) GetColorsOk() (*HeroColorsV2, bool)`

GetColorsOk returns a tuple with the Colors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColors

`func (o *HeroV2) SetColors(v HeroColorsV2)`

SetColors sets Colors field to given value.


### GetShopStatDisplay

`func (o *HeroV2) GetShopStatDisplay() HeroShopStatDisplayV2`

GetShopStatDisplay returns the ShopStatDisplay field if non-nil, zero value otherwise.

### GetShopStatDisplayOk

`func (o *HeroV2) GetShopStatDisplayOk() (*HeroShopStatDisplayV2, bool)`

GetShopStatDisplayOk returns a tuple with the ShopStatDisplay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopStatDisplay

`func (o *HeroV2) SetShopStatDisplay(v HeroShopStatDisplayV2)`

SetShopStatDisplay sets ShopStatDisplay field to given value.


### GetCostBonuses

`func (o *HeroV2) GetCostBonuses() map[string][]RawHeroMapModCostBonusesV2`

GetCostBonuses returns the CostBonuses field if non-nil, zero value otherwise.

### GetCostBonusesOk

`func (o *HeroV2) GetCostBonusesOk() (*map[string][]RawHeroMapModCostBonusesV2, bool)`

GetCostBonusesOk returns a tuple with the CostBonuses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCostBonuses

`func (o *HeroV2) SetCostBonuses(v map[string][]RawHeroMapModCostBonusesV2)`

SetCostBonuses sets CostBonuses field to given value.

### HasCostBonuses

`func (o *HeroV2) HasCostBonuses() bool`

HasCostBonuses returns a boolean if a field has been set.

### SetCostBonusesNil

`func (o *HeroV2) SetCostBonusesNil(b bool)`

 SetCostBonusesNil sets the value for CostBonuses to be an explicit nil

### UnsetCostBonuses
`func (o *HeroV2) UnsetCostBonuses()`

UnsetCostBonuses ensures that no value is present for CostBonuses, not even an explicit nil
### GetStatsDisplay

`func (o *HeroV2) GetStatsDisplay() RawHeroStatsDisplayV2`

GetStatsDisplay returns the StatsDisplay field if non-nil, zero value otherwise.

### GetStatsDisplayOk

`func (o *HeroV2) GetStatsDisplayOk() (*RawHeroStatsDisplayV2, bool)`

GetStatsDisplayOk returns a tuple with the StatsDisplay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatsDisplay

`func (o *HeroV2) SetStatsDisplay(v RawHeroStatsDisplayV2)`

SetStatsDisplay sets StatsDisplay field to given value.


### GetHeroStatsUi

`func (o *HeroV2) GetHeroStatsUi() RawHeroStatsUIV2`

GetHeroStatsUi returns the HeroStatsUi field if non-nil, zero value otherwise.

### GetHeroStatsUiOk

`func (o *HeroV2) GetHeroStatsUiOk() (*RawHeroStatsUIV2, bool)`

GetHeroStatsUiOk returns a tuple with the HeroStatsUi field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroStatsUi

`func (o *HeroV2) SetHeroStatsUi(v RawHeroStatsUIV2)`

SetHeroStatsUi sets HeroStatsUi field to given value.


### GetLevelInfo

`func (o *HeroV2) GetLevelInfo() map[string]HeroLevelInfoV2`

GetLevelInfo returns the LevelInfo field if non-nil, zero value otherwise.

### GetLevelInfoOk

`func (o *HeroV2) GetLevelInfoOk() (*map[string]HeroLevelInfoV2, bool)`

GetLevelInfoOk returns a tuple with the LevelInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLevelInfo

`func (o *HeroV2) SetLevelInfo(v map[string]HeroLevelInfoV2)`

SetLevelInfo sets LevelInfo field to given value.


### GetScalingStats

`func (o *HeroV2) GetScalingStats() map[string]RawHeroScalingStatV2`

GetScalingStats returns the ScalingStats field if non-nil, zero value otherwise.

### GetScalingStatsOk

`func (o *HeroV2) GetScalingStatsOk() (*map[string]RawHeroScalingStatV2, bool)`

GetScalingStatsOk returns a tuple with the ScalingStats field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScalingStats

`func (o *HeroV2) SetScalingStats(v map[string]RawHeroScalingStatV2)`

SetScalingStats sets ScalingStats field to given value.


### GetPurchaseBonuses

`func (o *HeroV2) GetPurchaseBonuses() map[string][]RawHeroPurchaseBonusV2`

GetPurchaseBonuses returns the PurchaseBonuses field if non-nil, zero value otherwise.

### GetPurchaseBonusesOk

`func (o *HeroV2) GetPurchaseBonusesOk() (*map[string][]RawHeroPurchaseBonusV2, bool)`

GetPurchaseBonusesOk returns a tuple with the PurchaseBonuses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPurchaseBonuses

`func (o *HeroV2) SetPurchaseBonuses(v map[string][]RawHeroPurchaseBonusV2)`

SetPurchaseBonuses sets PurchaseBonuses field to given value.


### GetStandardLevelUpUpgrades

`func (o *HeroV2) GetStandardLevelUpUpgrades() map[string]float32`

GetStandardLevelUpUpgrades returns the StandardLevelUpUpgrades field if non-nil, zero value otherwise.

### GetStandardLevelUpUpgradesOk

`func (o *HeroV2) GetStandardLevelUpUpgradesOk() (*map[string]float32, bool)`

GetStandardLevelUpUpgradesOk returns a tuple with the StandardLevelUpUpgrades field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStandardLevelUpUpgrades

`func (o *HeroV2) SetStandardLevelUpUpgrades(v map[string]float32)`

SetStandardLevelUpUpgrades sets StandardLevelUpUpgrades field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


