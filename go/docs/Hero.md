# Hero

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AssignedPlayersOnly** | **bool** |  | 
**ClassName** | **string** |  | 
**Colors** | [**HeroColors**](HeroColors.md) |  | 
**Complexity** | **int64** |  | 
**CostBonuses** | Pointer to [**map[string][]HashMapItemSlotTypeVecMapModCostBonusValueInner**](array.md) |  | [optional] 
**Description** | [**HeroDescription**](HeroDescription.md) |  | 
**Disabled** | **bool** |  | 
**GunTag** | Pointer to **NullableString** |  | [optional] 
**HeroStatsUi** | [**HeroStatsUI**](HeroStatsUI.md) |  | 
**HeroType** | Pointer to [**NullableHeroType**](HeroType.md) |  | [optional] 
**HideoutRichPresence** | Pointer to **NullableString** |  | [optional] 
**Id** | **int32** |  | 
**Images** | [**HeroImages**](HeroImages.md) |  | 
**InDevelopment** | **bool** |  | 
**ItemDraftBucketing** | Pointer to [**map[string]HashMapStringOptionDraftBucketingValue**](HashMapStringOptionDraftBucketingValue.md) |  | [optional] 
**ItemDraftWeights** | Pointer to **map[string]float64** |  | [optional] 
**ItemSlotInfo** | [**map[string]HashMapItemSlotTypeItemSlotInfoValue**](HashMapItemSlotTypeItemSlotInfoValue.md) |  | 
**Items** | **map[string]string** |  | 
**LevelInfo** | [**map[string]HashMapStringLevelInfoValue**](HashMapStringLevelInfoValue.md) |  | 
**LimitedTesting** | **bool** |  | 
**Name** | **string** |  | 
**NeedsTesting** | **bool** |  | 
**Physics** | [**HeroPhysics**](HeroPhysics.md) |  | 
**PlayerSelectable** | **bool** |  | 
**PrereleaseOnly** | Pointer to **NullableBool** |  | [optional] 
**PurchaseBonuses** | [**map[string][]HashMapItemSlotTypeVecPurchaseBonusValueInner**](array.md) |  | 
**ScalingStats** | [**map[string]HashMapStringScalingStatValue**](HashMapStringScalingStatValue.md) |  | 
**ShopStatDisplay** | [**ShopStatDisplay**](ShopStatDisplay.md) |  | 
**Skin** | **int64** |  | 
**StandardLevelUpUpgrades** | **map[string]float64** |  | 
**StartingStats** | [**StartingStats**](StartingStats.md) |  | 
**StatsDisplay** | [**StatsDisplay**](StatsDisplay.md) |  | 
**Tags** | **[]string** | Always emitted (empty if the hero declares no &#x60;m_vecHeroTags&#x60;). | 

## Methods

### NewHero

`func NewHero(assignedPlayersOnly bool, className string, colors HeroColors, complexity int64, description HeroDescription, disabled bool, heroStatsUi HeroStatsUI, id int32, images HeroImages, inDevelopment bool, itemSlotInfo map[string]HashMapItemSlotTypeItemSlotInfoValue, items map[string]string, levelInfo map[string]HashMapStringLevelInfoValue, limitedTesting bool, name string, needsTesting bool, physics HeroPhysics, playerSelectable bool, purchaseBonuses map[string][]HashMapItemSlotTypeVecPurchaseBonusValueInner, scalingStats map[string]HashMapStringScalingStatValue, shopStatDisplay ShopStatDisplay, skin int64, standardLevelUpUpgrades map[string]float64, startingStats StartingStats, statsDisplay StatsDisplay, tags []string, ) *Hero`

NewHero instantiates a new Hero object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHeroWithDefaults

`func NewHeroWithDefaults() *Hero`

NewHeroWithDefaults instantiates a new Hero object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAssignedPlayersOnly

`func (o *Hero) GetAssignedPlayersOnly() bool`

GetAssignedPlayersOnly returns the AssignedPlayersOnly field if non-nil, zero value otherwise.

### GetAssignedPlayersOnlyOk

`func (o *Hero) GetAssignedPlayersOnlyOk() (*bool, bool)`

GetAssignedPlayersOnlyOk returns a tuple with the AssignedPlayersOnly field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssignedPlayersOnly

`func (o *Hero) SetAssignedPlayersOnly(v bool)`

SetAssignedPlayersOnly sets AssignedPlayersOnly field to given value.


### GetClassName

`func (o *Hero) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *Hero) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *Hero) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetColors

`func (o *Hero) GetColors() HeroColors`

GetColors returns the Colors field if non-nil, zero value otherwise.

### GetColorsOk

`func (o *Hero) GetColorsOk() (*HeroColors, bool)`

GetColorsOk returns a tuple with the Colors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColors

`func (o *Hero) SetColors(v HeroColors)`

SetColors sets Colors field to given value.


### GetComplexity

`func (o *Hero) GetComplexity() int64`

GetComplexity returns the Complexity field if non-nil, zero value otherwise.

### GetComplexityOk

`func (o *Hero) GetComplexityOk() (*int64, bool)`

GetComplexityOk returns a tuple with the Complexity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComplexity

`func (o *Hero) SetComplexity(v int64)`

SetComplexity sets Complexity field to given value.


### GetCostBonuses

`func (o *Hero) GetCostBonuses() map[string][]HashMapItemSlotTypeVecMapModCostBonusValueInner`

GetCostBonuses returns the CostBonuses field if non-nil, zero value otherwise.

### GetCostBonusesOk

`func (o *Hero) GetCostBonusesOk() (*map[string][]HashMapItemSlotTypeVecMapModCostBonusValueInner, bool)`

GetCostBonusesOk returns a tuple with the CostBonuses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCostBonuses

`func (o *Hero) SetCostBonuses(v map[string][]HashMapItemSlotTypeVecMapModCostBonusValueInner)`

SetCostBonuses sets CostBonuses field to given value.

### HasCostBonuses

`func (o *Hero) HasCostBonuses() bool`

HasCostBonuses returns a boolean if a field has been set.

### SetCostBonusesNil

`func (o *Hero) SetCostBonusesNil(b bool)`

 SetCostBonusesNil sets the value for CostBonuses to be an explicit nil

### UnsetCostBonuses
`func (o *Hero) UnsetCostBonuses()`

UnsetCostBonuses ensures that no value is present for CostBonuses, not even an explicit nil
### GetDescription

`func (o *Hero) GetDescription() HeroDescription`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Hero) GetDescriptionOk() (*HeroDescription, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Hero) SetDescription(v HeroDescription)`

SetDescription sets Description field to given value.


### GetDisabled

`func (o *Hero) GetDisabled() bool`

GetDisabled returns the Disabled field if non-nil, zero value otherwise.

### GetDisabledOk

`func (o *Hero) GetDisabledOk() (*bool, bool)`

GetDisabledOk returns a tuple with the Disabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisabled

`func (o *Hero) SetDisabled(v bool)`

SetDisabled sets Disabled field to given value.


### GetGunTag

`func (o *Hero) GetGunTag() string`

GetGunTag returns the GunTag field if non-nil, zero value otherwise.

### GetGunTagOk

`func (o *Hero) GetGunTagOk() (*string, bool)`

GetGunTagOk returns a tuple with the GunTag field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGunTag

`func (o *Hero) SetGunTag(v string)`

SetGunTag sets GunTag field to given value.

### HasGunTag

`func (o *Hero) HasGunTag() bool`

HasGunTag returns a boolean if a field has been set.

### SetGunTagNil

`func (o *Hero) SetGunTagNil(b bool)`

 SetGunTagNil sets the value for GunTag to be an explicit nil

### UnsetGunTag
`func (o *Hero) UnsetGunTag()`

UnsetGunTag ensures that no value is present for GunTag, not even an explicit nil
### GetHeroStatsUi

`func (o *Hero) GetHeroStatsUi() HeroStatsUI`

GetHeroStatsUi returns the HeroStatsUi field if non-nil, zero value otherwise.

### GetHeroStatsUiOk

`func (o *Hero) GetHeroStatsUiOk() (*HeroStatsUI, bool)`

GetHeroStatsUiOk returns a tuple with the HeroStatsUi field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroStatsUi

`func (o *Hero) SetHeroStatsUi(v HeroStatsUI)`

SetHeroStatsUi sets HeroStatsUi field to given value.


### GetHeroType

`func (o *Hero) GetHeroType() HeroType`

GetHeroType returns the HeroType field if non-nil, zero value otherwise.

### GetHeroTypeOk

`func (o *Hero) GetHeroTypeOk() (*HeroType, bool)`

GetHeroTypeOk returns a tuple with the HeroType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroType

`func (o *Hero) SetHeroType(v HeroType)`

SetHeroType sets HeroType field to given value.

### HasHeroType

`func (o *Hero) HasHeroType() bool`

HasHeroType returns a boolean if a field has been set.

### SetHeroTypeNil

`func (o *Hero) SetHeroTypeNil(b bool)`

 SetHeroTypeNil sets the value for HeroType to be an explicit nil

### UnsetHeroType
`func (o *Hero) UnsetHeroType()`

UnsetHeroType ensures that no value is present for HeroType, not even an explicit nil
### GetHideoutRichPresence

`func (o *Hero) GetHideoutRichPresence() string`

GetHideoutRichPresence returns the HideoutRichPresence field if non-nil, zero value otherwise.

### GetHideoutRichPresenceOk

`func (o *Hero) GetHideoutRichPresenceOk() (*string, bool)`

GetHideoutRichPresenceOk returns a tuple with the HideoutRichPresence field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHideoutRichPresence

`func (o *Hero) SetHideoutRichPresence(v string)`

SetHideoutRichPresence sets HideoutRichPresence field to given value.

### HasHideoutRichPresence

`func (o *Hero) HasHideoutRichPresence() bool`

HasHideoutRichPresence returns a boolean if a field has been set.

### SetHideoutRichPresenceNil

`func (o *Hero) SetHideoutRichPresenceNil(b bool)`

 SetHideoutRichPresenceNil sets the value for HideoutRichPresence to be an explicit nil

### UnsetHideoutRichPresence
`func (o *Hero) UnsetHideoutRichPresence()`

UnsetHideoutRichPresence ensures that no value is present for HideoutRichPresence, not even an explicit nil
### GetId

`func (o *Hero) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Hero) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Hero) SetId(v int32)`

SetId sets Id field to given value.


### GetImages

`func (o *Hero) GetImages() HeroImages`

GetImages returns the Images field if non-nil, zero value otherwise.

### GetImagesOk

`func (o *Hero) GetImagesOk() (*HeroImages, bool)`

GetImagesOk returns a tuple with the Images field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImages

`func (o *Hero) SetImages(v HeroImages)`

SetImages sets Images field to given value.


### GetInDevelopment

`func (o *Hero) GetInDevelopment() bool`

GetInDevelopment returns the InDevelopment field if non-nil, zero value otherwise.

### GetInDevelopmentOk

`func (o *Hero) GetInDevelopmentOk() (*bool, bool)`

GetInDevelopmentOk returns a tuple with the InDevelopment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInDevelopment

`func (o *Hero) SetInDevelopment(v bool)`

SetInDevelopment sets InDevelopment field to given value.


### GetItemDraftBucketing

`func (o *Hero) GetItemDraftBucketing() map[string]HashMapStringOptionDraftBucketingValue`

GetItemDraftBucketing returns the ItemDraftBucketing field if non-nil, zero value otherwise.

### GetItemDraftBucketingOk

`func (o *Hero) GetItemDraftBucketingOk() (*map[string]HashMapStringOptionDraftBucketingValue, bool)`

GetItemDraftBucketingOk returns a tuple with the ItemDraftBucketing field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemDraftBucketing

`func (o *Hero) SetItemDraftBucketing(v map[string]HashMapStringOptionDraftBucketingValue)`

SetItemDraftBucketing sets ItemDraftBucketing field to given value.

### HasItemDraftBucketing

`func (o *Hero) HasItemDraftBucketing() bool`

HasItemDraftBucketing returns a boolean if a field has been set.

### SetItemDraftBucketingNil

`func (o *Hero) SetItemDraftBucketingNil(b bool)`

 SetItemDraftBucketingNil sets the value for ItemDraftBucketing to be an explicit nil

### UnsetItemDraftBucketing
`func (o *Hero) UnsetItemDraftBucketing()`

UnsetItemDraftBucketing ensures that no value is present for ItemDraftBucketing, not even an explicit nil
### GetItemDraftWeights

`func (o *Hero) GetItemDraftWeights() map[string]float64`

GetItemDraftWeights returns the ItemDraftWeights field if non-nil, zero value otherwise.

### GetItemDraftWeightsOk

`func (o *Hero) GetItemDraftWeightsOk() (*map[string]float64, bool)`

GetItemDraftWeightsOk returns a tuple with the ItemDraftWeights field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemDraftWeights

`func (o *Hero) SetItemDraftWeights(v map[string]float64)`

SetItemDraftWeights sets ItemDraftWeights field to given value.

### HasItemDraftWeights

`func (o *Hero) HasItemDraftWeights() bool`

HasItemDraftWeights returns a boolean if a field has been set.

### SetItemDraftWeightsNil

`func (o *Hero) SetItemDraftWeightsNil(b bool)`

 SetItemDraftWeightsNil sets the value for ItemDraftWeights to be an explicit nil

### UnsetItemDraftWeights
`func (o *Hero) UnsetItemDraftWeights()`

UnsetItemDraftWeights ensures that no value is present for ItemDraftWeights, not even an explicit nil
### GetItemSlotInfo

`func (o *Hero) GetItemSlotInfo() map[string]HashMapItemSlotTypeItemSlotInfoValue`

GetItemSlotInfo returns the ItemSlotInfo field if non-nil, zero value otherwise.

### GetItemSlotInfoOk

`func (o *Hero) GetItemSlotInfoOk() (*map[string]HashMapItemSlotTypeItemSlotInfoValue, bool)`

GetItemSlotInfoOk returns a tuple with the ItemSlotInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemSlotInfo

`func (o *Hero) SetItemSlotInfo(v map[string]HashMapItemSlotTypeItemSlotInfoValue)`

SetItemSlotInfo sets ItemSlotInfo field to given value.


### GetItems

`func (o *Hero) GetItems() map[string]string`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *Hero) GetItemsOk() (*map[string]string, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *Hero) SetItems(v map[string]string)`

SetItems sets Items field to given value.


### GetLevelInfo

`func (o *Hero) GetLevelInfo() map[string]HashMapStringLevelInfoValue`

GetLevelInfo returns the LevelInfo field if non-nil, zero value otherwise.

### GetLevelInfoOk

`func (o *Hero) GetLevelInfoOk() (*map[string]HashMapStringLevelInfoValue, bool)`

GetLevelInfoOk returns a tuple with the LevelInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLevelInfo

`func (o *Hero) SetLevelInfo(v map[string]HashMapStringLevelInfoValue)`

SetLevelInfo sets LevelInfo field to given value.


### GetLimitedTesting

`func (o *Hero) GetLimitedTesting() bool`

GetLimitedTesting returns the LimitedTesting field if non-nil, zero value otherwise.

### GetLimitedTestingOk

`func (o *Hero) GetLimitedTestingOk() (*bool, bool)`

GetLimitedTestingOk returns a tuple with the LimitedTesting field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimitedTesting

`func (o *Hero) SetLimitedTesting(v bool)`

SetLimitedTesting sets LimitedTesting field to given value.


### GetName

`func (o *Hero) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Hero) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Hero) SetName(v string)`

SetName sets Name field to given value.


### GetNeedsTesting

`func (o *Hero) GetNeedsTesting() bool`

GetNeedsTesting returns the NeedsTesting field if non-nil, zero value otherwise.

### GetNeedsTestingOk

`func (o *Hero) GetNeedsTestingOk() (*bool, bool)`

GetNeedsTestingOk returns a tuple with the NeedsTesting field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNeedsTesting

`func (o *Hero) SetNeedsTesting(v bool)`

SetNeedsTesting sets NeedsTesting field to given value.


### GetPhysics

`func (o *Hero) GetPhysics() HeroPhysics`

GetPhysics returns the Physics field if non-nil, zero value otherwise.

### GetPhysicsOk

`func (o *Hero) GetPhysicsOk() (*HeroPhysics, bool)`

GetPhysicsOk returns a tuple with the Physics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPhysics

`func (o *Hero) SetPhysics(v HeroPhysics)`

SetPhysics sets Physics field to given value.


### GetPlayerSelectable

`func (o *Hero) GetPlayerSelectable() bool`

GetPlayerSelectable returns the PlayerSelectable field if non-nil, zero value otherwise.

### GetPlayerSelectableOk

`func (o *Hero) GetPlayerSelectableOk() (*bool, bool)`

GetPlayerSelectableOk returns a tuple with the PlayerSelectable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerSelectable

`func (o *Hero) SetPlayerSelectable(v bool)`

SetPlayerSelectable sets PlayerSelectable field to given value.


### GetPrereleaseOnly

`func (o *Hero) GetPrereleaseOnly() bool`

GetPrereleaseOnly returns the PrereleaseOnly field if non-nil, zero value otherwise.

### GetPrereleaseOnlyOk

`func (o *Hero) GetPrereleaseOnlyOk() (*bool, bool)`

GetPrereleaseOnlyOk returns a tuple with the PrereleaseOnly field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrereleaseOnly

`func (o *Hero) SetPrereleaseOnly(v bool)`

SetPrereleaseOnly sets PrereleaseOnly field to given value.

### HasPrereleaseOnly

`func (o *Hero) HasPrereleaseOnly() bool`

HasPrereleaseOnly returns a boolean if a field has been set.

### SetPrereleaseOnlyNil

`func (o *Hero) SetPrereleaseOnlyNil(b bool)`

 SetPrereleaseOnlyNil sets the value for PrereleaseOnly to be an explicit nil

### UnsetPrereleaseOnly
`func (o *Hero) UnsetPrereleaseOnly()`

UnsetPrereleaseOnly ensures that no value is present for PrereleaseOnly, not even an explicit nil
### GetPurchaseBonuses

`func (o *Hero) GetPurchaseBonuses() map[string][]HashMapItemSlotTypeVecPurchaseBonusValueInner`

GetPurchaseBonuses returns the PurchaseBonuses field if non-nil, zero value otherwise.

### GetPurchaseBonusesOk

`func (o *Hero) GetPurchaseBonusesOk() (*map[string][]HashMapItemSlotTypeVecPurchaseBonusValueInner, bool)`

GetPurchaseBonusesOk returns a tuple with the PurchaseBonuses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPurchaseBonuses

`func (o *Hero) SetPurchaseBonuses(v map[string][]HashMapItemSlotTypeVecPurchaseBonusValueInner)`

SetPurchaseBonuses sets PurchaseBonuses field to given value.


### GetScalingStats

`func (o *Hero) GetScalingStats() map[string]HashMapStringScalingStatValue`

GetScalingStats returns the ScalingStats field if non-nil, zero value otherwise.

### GetScalingStatsOk

`func (o *Hero) GetScalingStatsOk() (*map[string]HashMapStringScalingStatValue, bool)`

GetScalingStatsOk returns a tuple with the ScalingStats field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScalingStats

`func (o *Hero) SetScalingStats(v map[string]HashMapStringScalingStatValue)`

SetScalingStats sets ScalingStats field to given value.


### GetShopStatDisplay

`func (o *Hero) GetShopStatDisplay() ShopStatDisplay`

GetShopStatDisplay returns the ShopStatDisplay field if non-nil, zero value otherwise.

### GetShopStatDisplayOk

`func (o *Hero) GetShopStatDisplayOk() (*ShopStatDisplay, bool)`

GetShopStatDisplayOk returns a tuple with the ShopStatDisplay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopStatDisplay

`func (o *Hero) SetShopStatDisplay(v ShopStatDisplay)`

SetShopStatDisplay sets ShopStatDisplay field to given value.


### GetSkin

`func (o *Hero) GetSkin() int64`

GetSkin returns the Skin field if non-nil, zero value otherwise.

### GetSkinOk

`func (o *Hero) GetSkinOk() (*int64, bool)`

GetSkinOk returns a tuple with the Skin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSkin

`func (o *Hero) SetSkin(v int64)`

SetSkin sets Skin field to given value.


### GetStandardLevelUpUpgrades

`func (o *Hero) GetStandardLevelUpUpgrades() map[string]float64`

GetStandardLevelUpUpgrades returns the StandardLevelUpUpgrades field if non-nil, zero value otherwise.

### GetStandardLevelUpUpgradesOk

`func (o *Hero) GetStandardLevelUpUpgradesOk() (*map[string]float64, bool)`

GetStandardLevelUpUpgradesOk returns a tuple with the StandardLevelUpUpgrades field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStandardLevelUpUpgrades

`func (o *Hero) SetStandardLevelUpUpgrades(v map[string]float64)`

SetStandardLevelUpUpgrades sets StandardLevelUpUpgrades field to given value.


### GetStartingStats

`func (o *Hero) GetStartingStats() StartingStats`

GetStartingStats returns the StartingStats field if non-nil, zero value otherwise.

### GetStartingStatsOk

`func (o *Hero) GetStartingStatsOk() (*StartingStats, bool)`

GetStartingStatsOk returns a tuple with the StartingStats field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartingStats

`func (o *Hero) SetStartingStats(v StartingStats)`

SetStartingStats sets StartingStats field to given value.


### GetStatsDisplay

`func (o *Hero) GetStatsDisplay() StatsDisplay`

GetStatsDisplay returns the StatsDisplay field if non-nil, zero value otherwise.

### GetStatsDisplayOk

`func (o *Hero) GetStatsDisplayOk() (*StatsDisplay, bool)`

GetStatsDisplayOk returns a tuple with the StatsDisplay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatsDisplay

`func (o *Hero) SetStatsDisplay(v StatsDisplay)`

SetStatsDisplay sets StatsDisplay field to given value.


### GetTags

`func (o *Hero) GetTags() []string`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *Hero) GetTagsOk() (*[]string, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTags

`func (o *Hero) SetTags(v []string)`

SetTags sets Tags field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


