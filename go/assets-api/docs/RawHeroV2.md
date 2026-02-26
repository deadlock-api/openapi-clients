# RawHeroV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** |  | 
**ClassName** | **string** |  | 
**ItemDraftWeights** | Pointer to **map[string]float32** |  | [optional] 
**PlayerSelectable** | **bool** |  | 
**Disabled** | **bool** |  | 
**InDevelopment** | **bool** |  | 
**NeedsTesting** | **bool** |  | 
**AssignedPlayersOnly** | **bool** |  | 
**AvailableInHeroLabs** | Pointer to **NullableBool** |  | [optional] 
**PrereleaseOnly** | Pointer to **NullableBool** |  | [optional] 
**LimitedTesting** | **bool** |  | 
**Complexity** | **int32** |  | 
**Skin** | **int32** |  | 
**StartingStats** | [**RawHeroStartingStatsV2**](RawHeroStartingStatsV2.md) |  | 
**IconHeroCard** | Pointer to **NullableString** |  | [optional] 
**IconImageSmall** | Pointer to **NullableString** |  | [optional] 
**MinimapImage** | Pointer to **NullableString** |  | [optional] 
**NameImage** | Pointer to **NullableString** |  | [optional] 
**HeroCardCritical** | Pointer to **NullableString** |  | [optional] 
**HeroCardGloat** | Pointer to **NullableString** |  | [optional] 
**TopBarVerticalImage** | Pointer to **NullableString** |  | [optional] 
**Tags** | Pointer to **[]string** |  | [optional] 
**GunTag** | Pointer to **NullableString** |  | [optional] 
**HideoutRichPresence** | Pointer to **NullableString** |  | [optional] 
**HeroType** | Pointer to [**NullableHeroTypeV2**](HeroTypeV2.md) |  | [optional] 
**ShopStatDisplay** | [**RawHeroShopStatDisplayV2**](RawHeroShopStatDisplayV2.md) |  | 
**CostBonuses** | [**map[string][]RawHeroMapModCostBonusesV2**](array.md) |  | 
**ColorUi** | **[]interface{}** |  | 
**CollisionHeight** | Pointer to **NullableFloat32** |  | [optional] 
**CollisionRadius** | Pointer to **NullableFloat32** |  | [optional] 
**FootstepSoundTravelDistanceMeters** | Pointer to **NullableFloat32** |  | [optional] 
**StealthSpeedMetersPerSecond** | **float32** |  | 
**StepHeight** | Pointer to **NullableFloat32** |  | [optional] 
**StepSoundTime** | Pointer to **NullableFloat32** |  | [optional] 
**StepSoundTimeSprinting** | Pointer to **NullableFloat32** |  | [optional] 
**StatsDisplay** | [**RawHeroStatsDisplayV2**](RawHeroStatsDisplayV2.md) |  | 
**HeroStatsUi** | [**RawHeroStatsUIV2**](RawHeroStatsUIV2.md) |  | 
**Items** | **map[string]string** |  | 
**ItemSlotInfo** | [**map[string]RawHeroItemSlotInfoValueV2**](RawHeroItemSlotInfoValueV2.md) |  | 
**LevelInfo** | [**map[string]RawHeroLevelInfoV2**](RawHeroLevelInfoV2.md) |  | 
**PurchaseBonuses** | Pointer to [**map[string][]RawHeroPurchaseBonusV2**](array.md) |  | [optional] 
**ScalingStats** | [**map[string]RawHeroScalingStatV2**](RawHeroScalingStatV2.md) |  | 
**StandardLevelUpUpgrades** | **map[string]float32** |  | 
**BackgroundImage** | **NullableString** |  | [readonly] 

## Methods

### NewRawHeroV2

`func NewRawHeroV2(id int32, className string, playerSelectable bool, disabled bool, inDevelopment bool, needsTesting bool, assignedPlayersOnly bool, limitedTesting bool, complexity int32, skin int32, startingStats RawHeroStartingStatsV2, shopStatDisplay RawHeroShopStatDisplayV2, costBonuses map[string][]RawHeroMapModCostBonusesV2, colorUi []interface{}, stealthSpeedMetersPerSecond float32, statsDisplay RawHeroStatsDisplayV2, heroStatsUi RawHeroStatsUIV2, items map[string]string, itemSlotInfo map[string]RawHeroItemSlotInfoValueV2, levelInfo map[string]RawHeroLevelInfoV2, scalingStats map[string]RawHeroScalingStatV2, standardLevelUpUpgrades map[string]float32, backgroundImage NullableString, ) *RawHeroV2`

NewRawHeroV2 instantiates a new RawHeroV2 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRawHeroV2WithDefaults

`func NewRawHeroV2WithDefaults() *RawHeroV2`

NewRawHeroV2WithDefaults instantiates a new RawHeroV2 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *RawHeroV2) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *RawHeroV2) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *RawHeroV2) SetId(v int32)`

SetId sets Id field to given value.


### GetClassName

`func (o *RawHeroV2) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *RawHeroV2) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *RawHeroV2) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetItemDraftWeights

`func (o *RawHeroV2) GetItemDraftWeights() map[string]float32`

GetItemDraftWeights returns the ItemDraftWeights field if non-nil, zero value otherwise.

### GetItemDraftWeightsOk

`func (o *RawHeroV2) GetItemDraftWeightsOk() (*map[string]float32, bool)`

GetItemDraftWeightsOk returns a tuple with the ItemDraftWeights field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemDraftWeights

`func (o *RawHeroV2) SetItemDraftWeights(v map[string]float32)`

SetItemDraftWeights sets ItemDraftWeights field to given value.

### HasItemDraftWeights

`func (o *RawHeroV2) HasItemDraftWeights() bool`

HasItemDraftWeights returns a boolean if a field has been set.

### SetItemDraftWeightsNil

`func (o *RawHeroV2) SetItemDraftWeightsNil(b bool)`

 SetItemDraftWeightsNil sets the value for ItemDraftWeights to be an explicit nil

### UnsetItemDraftWeights
`func (o *RawHeroV2) UnsetItemDraftWeights()`

UnsetItemDraftWeights ensures that no value is present for ItemDraftWeights, not even an explicit nil
### GetPlayerSelectable

`func (o *RawHeroV2) GetPlayerSelectable() bool`

GetPlayerSelectable returns the PlayerSelectable field if non-nil, zero value otherwise.

### GetPlayerSelectableOk

`func (o *RawHeroV2) GetPlayerSelectableOk() (*bool, bool)`

GetPlayerSelectableOk returns a tuple with the PlayerSelectable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerSelectable

`func (o *RawHeroV2) SetPlayerSelectable(v bool)`

SetPlayerSelectable sets PlayerSelectable field to given value.


### GetDisabled

`func (o *RawHeroV2) GetDisabled() bool`

GetDisabled returns the Disabled field if non-nil, zero value otherwise.

### GetDisabledOk

`func (o *RawHeroV2) GetDisabledOk() (*bool, bool)`

GetDisabledOk returns a tuple with the Disabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisabled

`func (o *RawHeroV2) SetDisabled(v bool)`

SetDisabled sets Disabled field to given value.


### GetInDevelopment

`func (o *RawHeroV2) GetInDevelopment() bool`

GetInDevelopment returns the InDevelopment field if non-nil, zero value otherwise.

### GetInDevelopmentOk

`func (o *RawHeroV2) GetInDevelopmentOk() (*bool, bool)`

GetInDevelopmentOk returns a tuple with the InDevelopment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInDevelopment

`func (o *RawHeroV2) SetInDevelopment(v bool)`

SetInDevelopment sets InDevelopment field to given value.


### GetNeedsTesting

`func (o *RawHeroV2) GetNeedsTesting() bool`

GetNeedsTesting returns the NeedsTesting field if non-nil, zero value otherwise.

### GetNeedsTestingOk

`func (o *RawHeroV2) GetNeedsTestingOk() (*bool, bool)`

GetNeedsTestingOk returns a tuple with the NeedsTesting field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNeedsTesting

`func (o *RawHeroV2) SetNeedsTesting(v bool)`

SetNeedsTesting sets NeedsTesting field to given value.


### GetAssignedPlayersOnly

`func (o *RawHeroV2) GetAssignedPlayersOnly() bool`

GetAssignedPlayersOnly returns the AssignedPlayersOnly field if non-nil, zero value otherwise.

### GetAssignedPlayersOnlyOk

`func (o *RawHeroV2) GetAssignedPlayersOnlyOk() (*bool, bool)`

GetAssignedPlayersOnlyOk returns a tuple with the AssignedPlayersOnly field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssignedPlayersOnly

`func (o *RawHeroV2) SetAssignedPlayersOnly(v bool)`

SetAssignedPlayersOnly sets AssignedPlayersOnly field to given value.


### GetAvailableInHeroLabs

`func (o *RawHeroV2) GetAvailableInHeroLabs() bool`

GetAvailableInHeroLabs returns the AvailableInHeroLabs field if non-nil, zero value otherwise.

### GetAvailableInHeroLabsOk

`func (o *RawHeroV2) GetAvailableInHeroLabsOk() (*bool, bool)`

GetAvailableInHeroLabsOk returns a tuple with the AvailableInHeroLabs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvailableInHeroLabs

`func (o *RawHeroV2) SetAvailableInHeroLabs(v bool)`

SetAvailableInHeroLabs sets AvailableInHeroLabs field to given value.

### HasAvailableInHeroLabs

`func (o *RawHeroV2) HasAvailableInHeroLabs() bool`

HasAvailableInHeroLabs returns a boolean if a field has been set.

### SetAvailableInHeroLabsNil

`func (o *RawHeroV2) SetAvailableInHeroLabsNil(b bool)`

 SetAvailableInHeroLabsNil sets the value for AvailableInHeroLabs to be an explicit nil

### UnsetAvailableInHeroLabs
`func (o *RawHeroV2) UnsetAvailableInHeroLabs()`

UnsetAvailableInHeroLabs ensures that no value is present for AvailableInHeroLabs, not even an explicit nil
### GetPrereleaseOnly

`func (o *RawHeroV2) GetPrereleaseOnly() bool`

GetPrereleaseOnly returns the PrereleaseOnly field if non-nil, zero value otherwise.

### GetPrereleaseOnlyOk

`func (o *RawHeroV2) GetPrereleaseOnlyOk() (*bool, bool)`

GetPrereleaseOnlyOk returns a tuple with the PrereleaseOnly field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrereleaseOnly

`func (o *RawHeroV2) SetPrereleaseOnly(v bool)`

SetPrereleaseOnly sets PrereleaseOnly field to given value.

### HasPrereleaseOnly

`func (o *RawHeroV2) HasPrereleaseOnly() bool`

HasPrereleaseOnly returns a boolean if a field has been set.

### SetPrereleaseOnlyNil

`func (o *RawHeroV2) SetPrereleaseOnlyNil(b bool)`

 SetPrereleaseOnlyNil sets the value for PrereleaseOnly to be an explicit nil

### UnsetPrereleaseOnly
`func (o *RawHeroV2) UnsetPrereleaseOnly()`

UnsetPrereleaseOnly ensures that no value is present for PrereleaseOnly, not even an explicit nil
### GetLimitedTesting

`func (o *RawHeroV2) GetLimitedTesting() bool`

GetLimitedTesting returns the LimitedTesting field if non-nil, zero value otherwise.

### GetLimitedTestingOk

`func (o *RawHeroV2) GetLimitedTestingOk() (*bool, bool)`

GetLimitedTestingOk returns a tuple with the LimitedTesting field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimitedTesting

`func (o *RawHeroV2) SetLimitedTesting(v bool)`

SetLimitedTesting sets LimitedTesting field to given value.


### GetComplexity

`func (o *RawHeroV2) GetComplexity() int32`

GetComplexity returns the Complexity field if non-nil, zero value otherwise.

### GetComplexityOk

`func (o *RawHeroV2) GetComplexityOk() (*int32, bool)`

GetComplexityOk returns a tuple with the Complexity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComplexity

`func (o *RawHeroV2) SetComplexity(v int32)`

SetComplexity sets Complexity field to given value.


### GetSkin

`func (o *RawHeroV2) GetSkin() int32`

GetSkin returns the Skin field if non-nil, zero value otherwise.

### GetSkinOk

`func (o *RawHeroV2) GetSkinOk() (*int32, bool)`

GetSkinOk returns a tuple with the Skin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSkin

`func (o *RawHeroV2) SetSkin(v int32)`

SetSkin sets Skin field to given value.


### GetStartingStats

`func (o *RawHeroV2) GetStartingStats() RawHeroStartingStatsV2`

GetStartingStats returns the StartingStats field if non-nil, zero value otherwise.

### GetStartingStatsOk

`func (o *RawHeroV2) GetStartingStatsOk() (*RawHeroStartingStatsV2, bool)`

GetStartingStatsOk returns a tuple with the StartingStats field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartingStats

`func (o *RawHeroV2) SetStartingStats(v RawHeroStartingStatsV2)`

SetStartingStats sets StartingStats field to given value.


### GetIconHeroCard

`func (o *RawHeroV2) GetIconHeroCard() string`

GetIconHeroCard returns the IconHeroCard field if non-nil, zero value otherwise.

### GetIconHeroCardOk

`func (o *RawHeroV2) GetIconHeroCardOk() (*string, bool)`

GetIconHeroCardOk returns a tuple with the IconHeroCard field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIconHeroCard

`func (o *RawHeroV2) SetIconHeroCard(v string)`

SetIconHeroCard sets IconHeroCard field to given value.

### HasIconHeroCard

`func (o *RawHeroV2) HasIconHeroCard() bool`

HasIconHeroCard returns a boolean if a field has been set.

### SetIconHeroCardNil

`func (o *RawHeroV2) SetIconHeroCardNil(b bool)`

 SetIconHeroCardNil sets the value for IconHeroCard to be an explicit nil

### UnsetIconHeroCard
`func (o *RawHeroV2) UnsetIconHeroCard()`

UnsetIconHeroCard ensures that no value is present for IconHeroCard, not even an explicit nil
### GetIconImageSmall

`func (o *RawHeroV2) GetIconImageSmall() string`

GetIconImageSmall returns the IconImageSmall field if non-nil, zero value otherwise.

### GetIconImageSmallOk

`func (o *RawHeroV2) GetIconImageSmallOk() (*string, bool)`

GetIconImageSmallOk returns a tuple with the IconImageSmall field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIconImageSmall

`func (o *RawHeroV2) SetIconImageSmall(v string)`

SetIconImageSmall sets IconImageSmall field to given value.

### HasIconImageSmall

`func (o *RawHeroV2) HasIconImageSmall() bool`

HasIconImageSmall returns a boolean if a field has been set.

### SetIconImageSmallNil

`func (o *RawHeroV2) SetIconImageSmallNil(b bool)`

 SetIconImageSmallNil sets the value for IconImageSmall to be an explicit nil

### UnsetIconImageSmall
`func (o *RawHeroV2) UnsetIconImageSmall()`

UnsetIconImageSmall ensures that no value is present for IconImageSmall, not even an explicit nil
### GetMinimapImage

`func (o *RawHeroV2) GetMinimapImage() string`

GetMinimapImage returns the MinimapImage field if non-nil, zero value otherwise.

### GetMinimapImageOk

`func (o *RawHeroV2) GetMinimapImageOk() (*string, bool)`

GetMinimapImageOk returns a tuple with the MinimapImage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMinimapImage

`func (o *RawHeroV2) SetMinimapImage(v string)`

SetMinimapImage sets MinimapImage field to given value.

### HasMinimapImage

`func (o *RawHeroV2) HasMinimapImage() bool`

HasMinimapImage returns a boolean if a field has been set.

### SetMinimapImageNil

`func (o *RawHeroV2) SetMinimapImageNil(b bool)`

 SetMinimapImageNil sets the value for MinimapImage to be an explicit nil

### UnsetMinimapImage
`func (o *RawHeroV2) UnsetMinimapImage()`

UnsetMinimapImage ensures that no value is present for MinimapImage, not even an explicit nil
### GetNameImage

`func (o *RawHeroV2) GetNameImage() string`

GetNameImage returns the NameImage field if non-nil, zero value otherwise.

### GetNameImageOk

`func (o *RawHeroV2) GetNameImageOk() (*string, bool)`

GetNameImageOk returns a tuple with the NameImage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNameImage

`func (o *RawHeroV2) SetNameImage(v string)`

SetNameImage sets NameImage field to given value.

### HasNameImage

`func (o *RawHeroV2) HasNameImage() bool`

HasNameImage returns a boolean if a field has been set.

### SetNameImageNil

`func (o *RawHeroV2) SetNameImageNil(b bool)`

 SetNameImageNil sets the value for NameImage to be an explicit nil

### UnsetNameImage
`func (o *RawHeroV2) UnsetNameImage()`

UnsetNameImage ensures that no value is present for NameImage, not even an explicit nil
### GetHeroCardCritical

`func (o *RawHeroV2) GetHeroCardCritical() string`

GetHeroCardCritical returns the HeroCardCritical field if non-nil, zero value otherwise.

### GetHeroCardCriticalOk

`func (o *RawHeroV2) GetHeroCardCriticalOk() (*string, bool)`

GetHeroCardCriticalOk returns a tuple with the HeroCardCritical field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroCardCritical

`func (o *RawHeroV2) SetHeroCardCritical(v string)`

SetHeroCardCritical sets HeroCardCritical field to given value.

### HasHeroCardCritical

`func (o *RawHeroV2) HasHeroCardCritical() bool`

HasHeroCardCritical returns a boolean if a field has been set.

### SetHeroCardCriticalNil

`func (o *RawHeroV2) SetHeroCardCriticalNil(b bool)`

 SetHeroCardCriticalNil sets the value for HeroCardCritical to be an explicit nil

### UnsetHeroCardCritical
`func (o *RawHeroV2) UnsetHeroCardCritical()`

UnsetHeroCardCritical ensures that no value is present for HeroCardCritical, not even an explicit nil
### GetHeroCardGloat

`func (o *RawHeroV2) GetHeroCardGloat() string`

GetHeroCardGloat returns the HeroCardGloat field if non-nil, zero value otherwise.

### GetHeroCardGloatOk

`func (o *RawHeroV2) GetHeroCardGloatOk() (*string, bool)`

GetHeroCardGloatOk returns a tuple with the HeroCardGloat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroCardGloat

`func (o *RawHeroV2) SetHeroCardGloat(v string)`

SetHeroCardGloat sets HeroCardGloat field to given value.

### HasHeroCardGloat

`func (o *RawHeroV2) HasHeroCardGloat() bool`

HasHeroCardGloat returns a boolean if a field has been set.

### SetHeroCardGloatNil

`func (o *RawHeroV2) SetHeroCardGloatNil(b bool)`

 SetHeroCardGloatNil sets the value for HeroCardGloat to be an explicit nil

### UnsetHeroCardGloat
`func (o *RawHeroV2) UnsetHeroCardGloat()`

UnsetHeroCardGloat ensures that no value is present for HeroCardGloat, not even an explicit nil
### GetTopBarVerticalImage

`func (o *RawHeroV2) GetTopBarVerticalImage() string`

GetTopBarVerticalImage returns the TopBarVerticalImage field if non-nil, zero value otherwise.

### GetTopBarVerticalImageOk

`func (o *RawHeroV2) GetTopBarVerticalImageOk() (*string, bool)`

GetTopBarVerticalImageOk returns a tuple with the TopBarVerticalImage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopBarVerticalImage

`func (o *RawHeroV2) SetTopBarVerticalImage(v string)`

SetTopBarVerticalImage sets TopBarVerticalImage field to given value.

### HasTopBarVerticalImage

`func (o *RawHeroV2) HasTopBarVerticalImage() bool`

HasTopBarVerticalImage returns a boolean if a field has been set.

### SetTopBarVerticalImageNil

`func (o *RawHeroV2) SetTopBarVerticalImageNil(b bool)`

 SetTopBarVerticalImageNil sets the value for TopBarVerticalImage to be an explicit nil

### UnsetTopBarVerticalImage
`func (o *RawHeroV2) UnsetTopBarVerticalImage()`

UnsetTopBarVerticalImage ensures that no value is present for TopBarVerticalImage, not even an explicit nil
### GetTags

`func (o *RawHeroV2) GetTags() []string`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *RawHeroV2) GetTagsOk() (*[]string, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTags

`func (o *RawHeroV2) SetTags(v []string)`

SetTags sets Tags field to given value.

### HasTags

`func (o *RawHeroV2) HasTags() bool`

HasTags returns a boolean if a field has been set.

### SetTagsNil

`func (o *RawHeroV2) SetTagsNil(b bool)`

 SetTagsNil sets the value for Tags to be an explicit nil

### UnsetTags
`func (o *RawHeroV2) UnsetTags()`

UnsetTags ensures that no value is present for Tags, not even an explicit nil
### GetGunTag

`func (o *RawHeroV2) GetGunTag() string`

GetGunTag returns the GunTag field if non-nil, zero value otherwise.

### GetGunTagOk

`func (o *RawHeroV2) GetGunTagOk() (*string, bool)`

GetGunTagOk returns a tuple with the GunTag field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGunTag

`func (o *RawHeroV2) SetGunTag(v string)`

SetGunTag sets GunTag field to given value.

### HasGunTag

`func (o *RawHeroV2) HasGunTag() bool`

HasGunTag returns a boolean if a field has been set.

### SetGunTagNil

`func (o *RawHeroV2) SetGunTagNil(b bool)`

 SetGunTagNil sets the value for GunTag to be an explicit nil

### UnsetGunTag
`func (o *RawHeroV2) UnsetGunTag()`

UnsetGunTag ensures that no value is present for GunTag, not even an explicit nil
### GetHideoutRichPresence

`func (o *RawHeroV2) GetHideoutRichPresence() string`

GetHideoutRichPresence returns the HideoutRichPresence field if non-nil, zero value otherwise.

### GetHideoutRichPresenceOk

`func (o *RawHeroV2) GetHideoutRichPresenceOk() (*string, bool)`

GetHideoutRichPresenceOk returns a tuple with the HideoutRichPresence field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHideoutRichPresence

`func (o *RawHeroV2) SetHideoutRichPresence(v string)`

SetHideoutRichPresence sets HideoutRichPresence field to given value.

### HasHideoutRichPresence

`func (o *RawHeroV2) HasHideoutRichPresence() bool`

HasHideoutRichPresence returns a boolean if a field has been set.

### SetHideoutRichPresenceNil

`func (o *RawHeroV2) SetHideoutRichPresenceNil(b bool)`

 SetHideoutRichPresenceNil sets the value for HideoutRichPresence to be an explicit nil

### UnsetHideoutRichPresence
`func (o *RawHeroV2) UnsetHideoutRichPresence()`

UnsetHideoutRichPresence ensures that no value is present for HideoutRichPresence, not even an explicit nil
### GetHeroType

`func (o *RawHeroV2) GetHeroType() HeroTypeV2`

GetHeroType returns the HeroType field if non-nil, zero value otherwise.

### GetHeroTypeOk

`func (o *RawHeroV2) GetHeroTypeOk() (*HeroTypeV2, bool)`

GetHeroTypeOk returns a tuple with the HeroType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroType

`func (o *RawHeroV2) SetHeroType(v HeroTypeV2)`

SetHeroType sets HeroType field to given value.

### HasHeroType

`func (o *RawHeroV2) HasHeroType() bool`

HasHeroType returns a boolean if a field has been set.

### SetHeroTypeNil

`func (o *RawHeroV2) SetHeroTypeNil(b bool)`

 SetHeroTypeNil sets the value for HeroType to be an explicit nil

### UnsetHeroType
`func (o *RawHeroV2) UnsetHeroType()`

UnsetHeroType ensures that no value is present for HeroType, not even an explicit nil
### GetShopStatDisplay

`func (o *RawHeroV2) GetShopStatDisplay() RawHeroShopStatDisplayV2`

GetShopStatDisplay returns the ShopStatDisplay field if non-nil, zero value otherwise.

### GetShopStatDisplayOk

`func (o *RawHeroV2) GetShopStatDisplayOk() (*RawHeroShopStatDisplayV2, bool)`

GetShopStatDisplayOk returns a tuple with the ShopStatDisplay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopStatDisplay

`func (o *RawHeroV2) SetShopStatDisplay(v RawHeroShopStatDisplayV2)`

SetShopStatDisplay sets ShopStatDisplay field to given value.


### GetCostBonuses

`func (o *RawHeroV2) GetCostBonuses() map[string][]RawHeroMapModCostBonusesV2`

GetCostBonuses returns the CostBonuses field if non-nil, zero value otherwise.

### GetCostBonusesOk

`func (o *RawHeroV2) GetCostBonusesOk() (*map[string][]RawHeroMapModCostBonusesV2, bool)`

GetCostBonusesOk returns a tuple with the CostBonuses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCostBonuses

`func (o *RawHeroV2) SetCostBonuses(v map[string][]RawHeroMapModCostBonusesV2)`

SetCostBonuses sets CostBonuses field to given value.


### GetColorUi

`func (o *RawHeroV2) GetColorUi() []interface{}`

GetColorUi returns the ColorUi field if non-nil, zero value otherwise.

### GetColorUiOk

`func (o *RawHeroV2) GetColorUiOk() (*[]interface{}, bool)`

GetColorUiOk returns a tuple with the ColorUi field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColorUi

`func (o *RawHeroV2) SetColorUi(v []interface{})`

SetColorUi sets ColorUi field to given value.


### GetCollisionHeight

`func (o *RawHeroV2) GetCollisionHeight() float32`

GetCollisionHeight returns the CollisionHeight field if non-nil, zero value otherwise.

### GetCollisionHeightOk

`func (o *RawHeroV2) GetCollisionHeightOk() (*float32, bool)`

GetCollisionHeightOk returns a tuple with the CollisionHeight field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCollisionHeight

`func (o *RawHeroV2) SetCollisionHeight(v float32)`

SetCollisionHeight sets CollisionHeight field to given value.

### HasCollisionHeight

`func (o *RawHeroV2) HasCollisionHeight() bool`

HasCollisionHeight returns a boolean if a field has been set.

### SetCollisionHeightNil

`func (o *RawHeroV2) SetCollisionHeightNil(b bool)`

 SetCollisionHeightNil sets the value for CollisionHeight to be an explicit nil

### UnsetCollisionHeight
`func (o *RawHeroV2) UnsetCollisionHeight()`

UnsetCollisionHeight ensures that no value is present for CollisionHeight, not even an explicit nil
### GetCollisionRadius

`func (o *RawHeroV2) GetCollisionRadius() float32`

GetCollisionRadius returns the CollisionRadius field if non-nil, zero value otherwise.

### GetCollisionRadiusOk

`func (o *RawHeroV2) GetCollisionRadiusOk() (*float32, bool)`

GetCollisionRadiusOk returns a tuple with the CollisionRadius field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCollisionRadius

`func (o *RawHeroV2) SetCollisionRadius(v float32)`

SetCollisionRadius sets CollisionRadius field to given value.

### HasCollisionRadius

`func (o *RawHeroV2) HasCollisionRadius() bool`

HasCollisionRadius returns a boolean if a field has been set.

### SetCollisionRadiusNil

`func (o *RawHeroV2) SetCollisionRadiusNil(b bool)`

 SetCollisionRadiusNil sets the value for CollisionRadius to be an explicit nil

### UnsetCollisionRadius
`func (o *RawHeroV2) UnsetCollisionRadius()`

UnsetCollisionRadius ensures that no value is present for CollisionRadius, not even an explicit nil
### GetFootstepSoundTravelDistanceMeters

`func (o *RawHeroV2) GetFootstepSoundTravelDistanceMeters() float32`

GetFootstepSoundTravelDistanceMeters returns the FootstepSoundTravelDistanceMeters field if non-nil, zero value otherwise.

### GetFootstepSoundTravelDistanceMetersOk

`func (o *RawHeroV2) GetFootstepSoundTravelDistanceMetersOk() (*float32, bool)`

GetFootstepSoundTravelDistanceMetersOk returns a tuple with the FootstepSoundTravelDistanceMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFootstepSoundTravelDistanceMeters

`func (o *RawHeroV2) SetFootstepSoundTravelDistanceMeters(v float32)`

SetFootstepSoundTravelDistanceMeters sets FootstepSoundTravelDistanceMeters field to given value.

### HasFootstepSoundTravelDistanceMeters

`func (o *RawHeroV2) HasFootstepSoundTravelDistanceMeters() bool`

HasFootstepSoundTravelDistanceMeters returns a boolean if a field has been set.

### SetFootstepSoundTravelDistanceMetersNil

`func (o *RawHeroV2) SetFootstepSoundTravelDistanceMetersNil(b bool)`

 SetFootstepSoundTravelDistanceMetersNil sets the value for FootstepSoundTravelDistanceMeters to be an explicit nil

### UnsetFootstepSoundTravelDistanceMeters
`func (o *RawHeroV2) UnsetFootstepSoundTravelDistanceMeters()`

UnsetFootstepSoundTravelDistanceMeters ensures that no value is present for FootstepSoundTravelDistanceMeters, not even an explicit nil
### GetStealthSpeedMetersPerSecond

`func (o *RawHeroV2) GetStealthSpeedMetersPerSecond() float32`

GetStealthSpeedMetersPerSecond returns the StealthSpeedMetersPerSecond field if non-nil, zero value otherwise.

### GetStealthSpeedMetersPerSecondOk

`func (o *RawHeroV2) GetStealthSpeedMetersPerSecondOk() (*float32, bool)`

GetStealthSpeedMetersPerSecondOk returns a tuple with the StealthSpeedMetersPerSecond field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStealthSpeedMetersPerSecond

`func (o *RawHeroV2) SetStealthSpeedMetersPerSecond(v float32)`

SetStealthSpeedMetersPerSecond sets StealthSpeedMetersPerSecond field to given value.


### GetStepHeight

`func (o *RawHeroV2) GetStepHeight() float32`

GetStepHeight returns the StepHeight field if non-nil, zero value otherwise.

### GetStepHeightOk

`func (o *RawHeroV2) GetStepHeightOk() (*float32, bool)`

GetStepHeightOk returns a tuple with the StepHeight field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepHeight

`func (o *RawHeroV2) SetStepHeight(v float32)`

SetStepHeight sets StepHeight field to given value.

### HasStepHeight

`func (o *RawHeroV2) HasStepHeight() bool`

HasStepHeight returns a boolean if a field has been set.

### SetStepHeightNil

`func (o *RawHeroV2) SetStepHeightNil(b bool)`

 SetStepHeightNil sets the value for StepHeight to be an explicit nil

### UnsetStepHeight
`func (o *RawHeroV2) UnsetStepHeight()`

UnsetStepHeight ensures that no value is present for StepHeight, not even an explicit nil
### GetStepSoundTime

`func (o *RawHeroV2) GetStepSoundTime() float32`

GetStepSoundTime returns the StepSoundTime field if non-nil, zero value otherwise.

### GetStepSoundTimeOk

`func (o *RawHeroV2) GetStepSoundTimeOk() (*float32, bool)`

GetStepSoundTimeOk returns a tuple with the StepSoundTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepSoundTime

`func (o *RawHeroV2) SetStepSoundTime(v float32)`

SetStepSoundTime sets StepSoundTime field to given value.

### HasStepSoundTime

`func (o *RawHeroV2) HasStepSoundTime() bool`

HasStepSoundTime returns a boolean if a field has been set.

### SetStepSoundTimeNil

`func (o *RawHeroV2) SetStepSoundTimeNil(b bool)`

 SetStepSoundTimeNil sets the value for StepSoundTime to be an explicit nil

### UnsetStepSoundTime
`func (o *RawHeroV2) UnsetStepSoundTime()`

UnsetStepSoundTime ensures that no value is present for StepSoundTime, not even an explicit nil
### GetStepSoundTimeSprinting

`func (o *RawHeroV2) GetStepSoundTimeSprinting() float32`

GetStepSoundTimeSprinting returns the StepSoundTimeSprinting field if non-nil, zero value otherwise.

### GetStepSoundTimeSprintingOk

`func (o *RawHeroV2) GetStepSoundTimeSprintingOk() (*float32, bool)`

GetStepSoundTimeSprintingOk returns a tuple with the StepSoundTimeSprinting field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepSoundTimeSprinting

`func (o *RawHeroV2) SetStepSoundTimeSprinting(v float32)`

SetStepSoundTimeSprinting sets StepSoundTimeSprinting field to given value.

### HasStepSoundTimeSprinting

`func (o *RawHeroV2) HasStepSoundTimeSprinting() bool`

HasStepSoundTimeSprinting returns a boolean if a field has been set.

### SetStepSoundTimeSprintingNil

`func (o *RawHeroV2) SetStepSoundTimeSprintingNil(b bool)`

 SetStepSoundTimeSprintingNil sets the value for StepSoundTimeSprinting to be an explicit nil

### UnsetStepSoundTimeSprinting
`func (o *RawHeroV2) UnsetStepSoundTimeSprinting()`

UnsetStepSoundTimeSprinting ensures that no value is present for StepSoundTimeSprinting, not even an explicit nil
### GetStatsDisplay

`func (o *RawHeroV2) GetStatsDisplay() RawHeroStatsDisplayV2`

GetStatsDisplay returns the StatsDisplay field if non-nil, zero value otherwise.

### GetStatsDisplayOk

`func (o *RawHeroV2) GetStatsDisplayOk() (*RawHeroStatsDisplayV2, bool)`

GetStatsDisplayOk returns a tuple with the StatsDisplay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatsDisplay

`func (o *RawHeroV2) SetStatsDisplay(v RawHeroStatsDisplayV2)`

SetStatsDisplay sets StatsDisplay field to given value.


### GetHeroStatsUi

`func (o *RawHeroV2) GetHeroStatsUi() RawHeroStatsUIV2`

GetHeroStatsUi returns the HeroStatsUi field if non-nil, zero value otherwise.

### GetHeroStatsUiOk

`func (o *RawHeroV2) GetHeroStatsUiOk() (*RawHeroStatsUIV2, bool)`

GetHeroStatsUiOk returns a tuple with the HeroStatsUi field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroStatsUi

`func (o *RawHeroV2) SetHeroStatsUi(v RawHeroStatsUIV2)`

SetHeroStatsUi sets HeroStatsUi field to given value.


### GetItems

`func (o *RawHeroV2) GetItems() map[string]string`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *RawHeroV2) GetItemsOk() (*map[string]string, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *RawHeroV2) SetItems(v map[string]string)`

SetItems sets Items field to given value.


### GetItemSlotInfo

`func (o *RawHeroV2) GetItemSlotInfo() map[string]RawHeroItemSlotInfoValueV2`

GetItemSlotInfo returns the ItemSlotInfo field if non-nil, zero value otherwise.

### GetItemSlotInfoOk

`func (o *RawHeroV2) GetItemSlotInfoOk() (*map[string]RawHeroItemSlotInfoValueV2, bool)`

GetItemSlotInfoOk returns a tuple with the ItemSlotInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemSlotInfo

`func (o *RawHeroV2) SetItemSlotInfo(v map[string]RawHeroItemSlotInfoValueV2)`

SetItemSlotInfo sets ItemSlotInfo field to given value.


### GetLevelInfo

`func (o *RawHeroV2) GetLevelInfo() map[string]RawHeroLevelInfoV2`

GetLevelInfo returns the LevelInfo field if non-nil, zero value otherwise.

### GetLevelInfoOk

`func (o *RawHeroV2) GetLevelInfoOk() (*map[string]RawHeroLevelInfoV2, bool)`

GetLevelInfoOk returns a tuple with the LevelInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLevelInfo

`func (o *RawHeroV2) SetLevelInfo(v map[string]RawHeroLevelInfoV2)`

SetLevelInfo sets LevelInfo field to given value.


### GetPurchaseBonuses

`func (o *RawHeroV2) GetPurchaseBonuses() map[string][]RawHeroPurchaseBonusV2`

GetPurchaseBonuses returns the PurchaseBonuses field if non-nil, zero value otherwise.

### GetPurchaseBonusesOk

`func (o *RawHeroV2) GetPurchaseBonusesOk() (*map[string][]RawHeroPurchaseBonusV2, bool)`

GetPurchaseBonusesOk returns a tuple with the PurchaseBonuses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPurchaseBonuses

`func (o *RawHeroV2) SetPurchaseBonuses(v map[string][]RawHeroPurchaseBonusV2)`

SetPurchaseBonuses sets PurchaseBonuses field to given value.

### HasPurchaseBonuses

`func (o *RawHeroV2) HasPurchaseBonuses() bool`

HasPurchaseBonuses returns a boolean if a field has been set.

### SetPurchaseBonusesNil

`func (o *RawHeroV2) SetPurchaseBonusesNil(b bool)`

 SetPurchaseBonusesNil sets the value for PurchaseBonuses to be an explicit nil

### UnsetPurchaseBonuses
`func (o *RawHeroV2) UnsetPurchaseBonuses()`

UnsetPurchaseBonuses ensures that no value is present for PurchaseBonuses, not even an explicit nil
### GetScalingStats

`func (o *RawHeroV2) GetScalingStats() map[string]RawHeroScalingStatV2`

GetScalingStats returns the ScalingStats field if non-nil, zero value otherwise.

### GetScalingStatsOk

`func (o *RawHeroV2) GetScalingStatsOk() (*map[string]RawHeroScalingStatV2, bool)`

GetScalingStatsOk returns a tuple with the ScalingStats field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScalingStats

`func (o *RawHeroV2) SetScalingStats(v map[string]RawHeroScalingStatV2)`

SetScalingStats sets ScalingStats field to given value.


### GetStandardLevelUpUpgrades

`func (o *RawHeroV2) GetStandardLevelUpUpgrades() map[string]float32`

GetStandardLevelUpUpgrades returns the StandardLevelUpUpgrades field if non-nil, zero value otherwise.

### GetStandardLevelUpUpgradesOk

`func (o *RawHeroV2) GetStandardLevelUpUpgradesOk() (*map[string]float32, bool)`

GetStandardLevelUpUpgradesOk returns a tuple with the StandardLevelUpUpgrades field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStandardLevelUpUpgrades

`func (o *RawHeroV2) SetStandardLevelUpUpgrades(v map[string]float32)`

SetStandardLevelUpUpgrades sets StandardLevelUpUpgrades field to given value.


### GetBackgroundImage

`func (o *RawHeroV2) GetBackgroundImage() string`

GetBackgroundImage returns the BackgroundImage field if non-nil, zero value otherwise.

### GetBackgroundImageOk

`func (o *RawHeroV2) GetBackgroundImageOk() (*string, bool)`

GetBackgroundImageOk returns a tuple with the BackgroundImage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBackgroundImage

`func (o *RawHeroV2) SetBackgroundImage(v string)`

SetBackgroundImage sets BackgroundImage field to given value.


### SetBackgroundImageNil

`func (o *RawHeroV2) SetBackgroundImageNil(b bool)`

 SetBackgroundImageNil sets the value for BackgroundImage to be an explicit nil

### UnsetBackgroundImage
`func (o *RawHeroV2) UnsetBackgroundImage()`

UnsetBackgroundImage ensures that no value is present for BackgroundImage, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


