# Upgrade

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Activation** | [**AbilityActivation**](AbilityActivation.md) |  | 
**ClassName** | **string** |  | 
**ComponentItems** | Pointer to **[]string** |  | [optional] 
**Cost** | Pointer to **NullableInt32** |  | [optional] 
**Description** | Pointer to [**NullableUpgradeDescription**](UpgradeDescription.md) |  | [optional] 
**Disabled** | Pointer to **NullableBool** |  | [optional] 
**Hero** | Pointer to **NullableInt32** |  | [optional] 
**Heroes** | Pointer to **[]int32** |  | [optional] 
**Id** | **int32** |  | 
**Image** | Pointer to **NullableString** |  | [optional] 
**ImageWebp** | Pointer to **NullableString** |  | [optional] 
**Imbue** | Pointer to [**NullableAbilityImbue**](AbilityImbue.md) |  | [optional] 
**IsActiveItem** | **bool** |  | 
**ItemSlotType** | [**ItemSlotType**](ItemSlotType.md) |  | 
**ItemTier** | **int32** |  | 
**Name** | **string** |  | 
**Properties** | Pointer to [**map[string]UpgradeProperty**](UpgradeProperty.md) |  | [optional] 
**ShopImage** | Pointer to **NullableString** |  | [optional] 
**ShopImageSmall** | Pointer to **NullableString** |  | [optional] 
**ShopImageSmallWebp** | Pointer to **NullableString** |  | [optional] 
**ShopImageWebp** | Pointer to **NullableString** |  | [optional] 
**Shopable** | **bool** |  | 
**StartTrained** | Pointer to **NullableBool** |  | [optional] 
**TooltipSections** | Pointer to [**[]UpgradeTooltipSection**](UpgradeTooltipSection.md) |  | [optional] 
**Type** | [**ItemType**](ItemType.md) |  | 
**UpdateTime** | Pointer to **NullableInt64** |  | [optional] 
**Upgrades** | Pointer to [**[]RawAbilityUpgrade**](RawAbilityUpgrade.md) |  | [optional] 
**WeaponInfo** | Pointer to [**NullableRawItemWeaponInfoInner**](RawItemWeaponInfoInner.md) |  | [optional] 

## Methods

### NewUpgrade

`func NewUpgrade(activation AbilityActivation, className string, id int32, isActiveItem bool, itemSlotType ItemSlotType, itemTier int32, name string, shopable bool, type_ ItemType, ) *Upgrade`

NewUpgrade instantiates a new Upgrade object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpgradeWithDefaults

`func NewUpgradeWithDefaults() *Upgrade`

NewUpgradeWithDefaults instantiates a new Upgrade object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetActivation

`func (o *Upgrade) GetActivation() AbilityActivation`

GetActivation returns the Activation field if non-nil, zero value otherwise.

### GetActivationOk

`func (o *Upgrade) GetActivationOk() (*AbilityActivation, bool)`

GetActivationOk returns a tuple with the Activation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActivation

`func (o *Upgrade) SetActivation(v AbilityActivation)`

SetActivation sets Activation field to given value.


### GetClassName

`func (o *Upgrade) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *Upgrade) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *Upgrade) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetComponentItems

`func (o *Upgrade) GetComponentItems() []string`

GetComponentItems returns the ComponentItems field if non-nil, zero value otherwise.

### GetComponentItemsOk

`func (o *Upgrade) GetComponentItemsOk() (*[]string, bool)`

GetComponentItemsOk returns a tuple with the ComponentItems field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComponentItems

`func (o *Upgrade) SetComponentItems(v []string)`

SetComponentItems sets ComponentItems field to given value.

### HasComponentItems

`func (o *Upgrade) HasComponentItems() bool`

HasComponentItems returns a boolean if a field has been set.

### SetComponentItemsNil

`func (o *Upgrade) SetComponentItemsNil(b bool)`

 SetComponentItemsNil sets the value for ComponentItems to be an explicit nil

### UnsetComponentItems
`func (o *Upgrade) UnsetComponentItems()`

UnsetComponentItems ensures that no value is present for ComponentItems, not even an explicit nil
### GetCost

`func (o *Upgrade) GetCost() int32`

GetCost returns the Cost field if non-nil, zero value otherwise.

### GetCostOk

`func (o *Upgrade) GetCostOk() (*int32, bool)`

GetCostOk returns a tuple with the Cost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCost

`func (o *Upgrade) SetCost(v int32)`

SetCost sets Cost field to given value.

### HasCost

`func (o *Upgrade) HasCost() bool`

HasCost returns a boolean if a field has been set.

### SetCostNil

`func (o *Upgrade) SetCostNil(b bool)`

 SetCostNil sets the value for Cost to be an explicit nil

### UnsetCost
`func (o *Upgrade) UnsetCost()`

UnsetCost ensures that no value is present for Cost, not even an explicit nil
### GetDescription

`func (o *Upgrade) GetDescription() UpgradeDescription`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Upgrade) GetDescriptionOk() (*UpgradeDescription, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Upgrade) SetDescription(v UpgradeDescription)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *Upgrade) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *Upgrade) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *Upgrade) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetDisabled

`func (o *Upgrade) GetDisabled() bool`

GetDisabled returns the Disabled field if non-nil, zero value otherwise.

### GetDisabledOk

`func (o *Upgrade) GetDisabledOk() (*bool, bool)`

GetDisabledOk returns a tuple with the Disabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisabled

`func (o *Upgrade) SetDisabled(v bool)`

SetDisabled sets Disabled field to given value.

### HasDisabled

`func (o *Upgrade) HasDisabled() bool`

HasDisabled returns a boolean if a field has been set.

### SetDisabledNil

`func (o *Upgrade) SetDisabledNil(b bool)`

 SetDisabledNil sets the value for Disabled to be an explicit nil

### UnsetDisabled
`func (o *Upgrade) UnsetDisabled()`

UnsetDisabled ensures that no value is present for Disabled, not even an explicit nil
### GetHero

`func (o *Upgrade) GetHero() int32`

GetHero returns the Hero field if non-nil, zero value otherwise.

### GetHeroOk

`func (o *Upgrade) GetHeroOk() (*int32, bool)`

GetHeroOk returns a tuple with the Hero field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHero

`func (o *Upgrade) SetHero(v int32)`

SetHero sets Hero field to given value.

### HasHero

`func (o *Upgrade) HasHero() bool`

HasHero returns a boolean if a field has been set.

### SetHeroNil

`func (o *Upgrade) SetHeroNil(b bool)`

 SetHeroNil sets the value for Hero to be an explicit nil

### UnsetHero
`func (o *Upgrade) UnsetHero()`

UnsetHero ensures that no value is present for Hero, not even an explicit nil
### GetHeroes

`func (o *Upgrade) GetHeroes() []int32`

GetHeroes returns the Heroes field if non-nil, zero value otherwise.

### GetHeroesOk

`func (o *Upgrade) GetHeroesOk() (*[]int32, bool)`

GetHeroesOk returns a tuple with the Heroes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroes

`func (o *Upgrade) SetHeroes(v []int32)`

SetHeroes sets Heroes field to given value.

### HasHeroes

`func (o *Upgrade) HasHeroes() bool`

HasHeroes returns a boolean if a field has been set.

### SetHeroesNil

`func (o *Upgrade) SetHeroesNil(b bool)`

 SetHeroesNil sets the value for Heroes to be an explicit nil

### UnsetHeroes
`func (o *Upgrade) UnsetHeroes()`

UnsetHeroes ensures that no value is present for Heroes, not even an explicit nil
### GetId

`func (o *Upgrade) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Upgrade) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Upgrade) SetId(v int32)`

SetId sets Id field to given value.


### GetImage

`func (o *Upgrade) GetImage() string`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *Upgrade) GetImageOk() (*string, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *Upgrade) SetImage(v string)`

SetImage sets Image field to given value.

### HasImage

`func (o *Upgrade) HasImage() bool`

HasImage returns a boolean if a field has been set.

### SetImageNil

`func (o *Upgrade) SetImageNil(b bool)`

 SetImageNil sets the value for Image to be an explicit nil

### UnsetImage
`func (o *Upgrade) UnsetImage()`

UnsetImage ensures that no value is present for Image, not even an explicit nil
### GetImageWebp

`func (o *Upgrade) GetImageWebp() string`

GetImageWebp returns the ImageWebp field if non-nil, zero value otherwise.

### GetImageWebpOk

`func (o *Upgrade) GetImageWebpOk() (*string, bool)`

GetImageWebpOk returns a tuple with the ImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImageWebp

`func (o *Upgrade) SetImageWebp(v string)`

SetImageWebp sets ImageWebp field to given value.

### HasImageWebp

`func (o *Upgrade) HasImageWebp() bool`

HasImageWebp returns a boolean if a field has been set.

### SetImageWebpNil

`func (o *Upgrade) SetImageWebpNil(b bool)`

 SetImageWebpNil sets the value for ImageWebp to be an explicit nil

### UnsetImageWebp
`func (o *Upgrade) UnsetImageWebp()`

UnsetImageWebp ensures that no value is present for ImageWebp, not even an explicit nil
### GetImbue

`func (o *Upgrade) GetImbue() AbilityImbue`

GetImbue returns the Imbue field if non-nil, zero value otherwise.

### GetImbueOk

`func (o *Upgrade) GetImbueOk() (*AbilityImbue, bool)`

GetImbueOk returns a tuple with the Imbue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImbue

`func (o *Upgrade) SetImbue(v AbilityImbue)`

SetImbue sets Imbue field to given value.

### HasImbue

`func (o *Upgrade) HasImbue() bool`

HasImbue returns a boolean if a field has been set.

### SetImbueNil

`func (o *Upgrade) SetImbueNil(b bool)`

 SetImbueNil sets the value for Imbue to be an explicit nil

### UnsetImbue
`func (o *Upgrade) UnsetImbue()`

UnsetImbue ensures that no value is present for Imbue, not even an explicit nil
### GetIsActiveItem

`func (o *Upgrade) GetIsActiveItem() bool`

GetIsActiveItem returns the IsActiveItem field if non-nil, zero value otherwise.

### GetIsActiveItemOk

`func (o *Upgrade) GetIsActiveItemOk() (*bool, bool)`

GetIsActiveItemOk returns a tuple with the IsActiveItem field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsActiveItem

`func (o *Upgrade) SetIsActiveItem(v bool)`

SetIsActiveItem sets IsActiveItem field to given value.


### GetItemSlotType

`func (o *Upgrade) GetItemSlotType() ItemSlotType`

GetItemSlotType returns the ItemSlotType field if non-nil, zero value otherwise.

### GetItemSlotTypeOk

`func (o *Upgrade) GetItemSlotTypeOk() (*ItemSlotType, bool)`

GetItemSlotTypeOk returns a tuple with the ItemSlotType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemSlotType

`func (o *Upgrade) SetItemSlotType(v ItemSlotType)`

SetItemSlotType sets ItemSlotType field to given value.


### GetItemTier

`func (o *Upgrade) GetItemTier() int32`

GetItemTier returns the ItemTier field if non-nil, zero value otherwise.

### GetItemTierOk

`func (o *Upgrade) GetItemTierOk() (*int32, bool)`

GetItemTierOk returns a tuple with the ItemTier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemTier

`func (o *Upgrade) SetItemTier(v int32)`

SetItemTier sets ItemTier field to given value.


### GetName

`func (o *Upgrade) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Upgrade) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Upgrade) SetName(v string)`

SetName sets Name field to given value.


### GetProperties

`func (o *Upgrade) GetProperties() map[string]UpgradeProperty`

GetProperties returns the Properties field if non-nil, zero value otherwise.

### GetPropertiesOk

`func (o *Upgrade) GetPropertiesOk() (*map[string]UpgradeProperty, bool)`

GetPropertiesOk returns a tuple with the Properties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperties

`func (o *Upgrade) SetProperties(v map[string]UpgradeProperty)`

SetProperties sets Properties field to given value.

### HasProperties

`func (o *Upgrade) HasProperties() bool`

HasProperties returns a boolean if a field has been set.

### GetShopImage

`func (o *Upgrade) GetShopImage() string`

GetShopImage returns the ShopImage field if non-nil, zero value otherwise.

### GetShopImageOk

`func (o *Upgrade) GetShopImageOk() (*string, bool)`

GetShopImageOk returns a tuple with the ShopImage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImage

`func (o *Upgrade) SetShopImage(v string)`

SetShopImage sets ShopImage field to given value.

### HasShopImage

`func (o *Upgrade) HasShopImage() bool`

HasShopImage returns a boolean if a field has been set.

### SetShopImageNil

`func (o *Upgrade) SetShopImageNil(b bool)`

 SetShopImageNil sets the value for ShopImage to be an explicit nil

### UnsetShopImage
`func (o *Upgrade) UnsetShopImage()`

UnsetShopImage ensures that no value is present for ShopImage, not even an explicit nil
### GetShopImageSmall

`func (o *Upgrade) GetShopImageSmall() string`

GetShopImageSmall returns the ShopImageSmall field if non-nil, zero value otherwise.

### GetShopImageSmallOk

`func (o *Upgrade) GetShopImageSmallOk() (*string, bool)`

GetShopImageSmallOk returns a tuple with the ShopImageSmall field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageSmall

`func (o *Upgrade) SetShopImageSmall(v string)`

SetShopImageSmall sets ShopImageSmall field to given value.

### HasShopImageSmall

`func (o *Upgrade) HasShopImageSmall() bool`

HasShopImageSmall returns a boolean if a field has been set.

### SetShopImageSmallNil

`func (o *Upgrade) SetShopImageSmallNil(b bool)`

 SetShopImageSmallNil sets the value for ShopImageSmall to be an explicit nil

### UnsetShopImageSmall
`func (o *Upgrade) UnsetShopImageSmall()`

UnsetShopImageSmall ensures that no value is present for ShopImageSmall, not even an explicit nil
### GetShopImageSmallWebp

`func (o *Upgrade) GetShopImageSmallWebp() string`

GetShopImageSmallWebp returns the ShopImageSmallWebp field if non-nil, zero value otherwise.

### GetShopImageSmallWebpOk

`func (o *Upgrade) GetShopImageSmallWebpOk() (*string, bool)`

GetShopImageSmallWebpOk returns a tuple with the ShopImageSmallWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageSmallWebp

`func (o *Upgrade) SetShopImageSmallWebp(v string)`

SetShopImageSmallWebp sets ShopImageSmallWebp field to given value.

### HasShopImageSmallWebp

`func (o *Upgrade) HasShopImageSmallWebp() bool`

HasShopImageSmallWebp returns a boolean if a field has been set.

### SetShopImageSmallWebpNil

`func (o *Upgrade) SetShopImageSmallWebpNil(b bool)`

 SetShopImageSmallWebpNil sets the value for ShopImageSmallWebp to be an explicit nil

### UnsetShopImageSmallWebp
`func (o *Upgrade) UnsetShopImageSmallWebp()`

UnsetShopImageSmallWebp ensures that no value is present for ShopImageSmallWebp, not even an explicit nil
### GetShopImageWebp

`func (o *Upgrade) GetShopImageWebp() string`

GetShopImageWebp returns the ShopImageWebp field if non-nil, zero value otherwise.

### GetShopImageWebpOk

`func (o *Upgrade) GetShopImageWebpOk() (*string, bool)`

GetShopImageWebpOk returns a tuple with the ShopImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageWebp

`func (o *Upgrade) SetShopImageWebp(v string)`

SetShopImageWebp sets ShopImageWebp field to given value.

### HasShopImageWebp

`func (o *Upgrade) HasShopImageWebp() bool`

HasShopImageWebp returns a boolean if a field has been set.

### SetShopImageWebpNil

`func (o *Upgrade) SetShopImageWebpNil(b bool)`

 SetShopImageWebpNil sets the value for ShopImageWebp to be an explicit nil

### UnsetShopImageWebp
`func (o *Upgrade) UnsetShopImageWebp()`

UnsetShopImageWebp ensures that no value is present for ShopImageWebp, not even an explicit nil
### GetShopable

`func (o *Upgrade) GetShopable() bool`

GetShopable returns the Shopable field if non-nil, zero value otherwise.

### GetShopableOk

`func (o *Upgrade) GetShopableOk() (*bool, bool)`

GetShopableOk returns a tuple with the Shopable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopable

`func (o *Upgrade) SetShopable(v bool)`

SetShopable sets Shopable field to given value.


### GetStartTrained

`func (o *Upgrade) GetStartTrained() bool`

GetStartTrained returns the StartTrained field if non-nil, zero value otherwise.

### GetStartTrainedOk

`func (o *Upgrade) GetStartTrainedOk() (*bool, bool)`

GetStartTrainedOk returns a tuple with the StartTrained field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTrained

`func (o *Upgrade) SetStartTrained(v bool)`

SetStartTrained sets StartTrained field to given value.

### HasStartTrained

`func (o *Upgrade) HasStartTrained() bool`

HasStartTrained returns a boolean if a field has been set.

### SetStartTrainedNil

`func (o *Upgrade) SetStartTrainedNil(b bool)`

 SetStartTrainedNil sets the value for StartTrained to be an explicit nil

### UnsetStartTrained
`func (o *Upgrade) UnsetStartTrained()`

UnsetStartTrained ensures that no value is present for StartTrained, not even an explicit nil
### GetTooltipSections

`func (o *Upgrade) GetTooltipSections() []UpgradeTooltipSection`

GetTooltipSections returns the TooltipSections field if non-nil, zero value otherwise.

### GetTooltipSectionsOk

`func (o *Upgrade) GetTooltipSectionsOk() (*[]UpgradeTooltipSection, bool)`

GetTooltipSectionsOk returns a tuple with the TooltipSections field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipSections

`func (o *Upgrade) SetTooltipSections(v []UpgradeTooltipSection)`

SetTooltipSections sets TooltipSections field to given value.

### HasTooltipSections

`func (o *Upgrade) HasTooltipSections() bool`

HasTooltipSections returns a boolean if a field has been set.

### SetTooltipSectionsNil

`func (o *Upgrade) SetTooltipSectionsNil(b bool)`

 SetTooltipSectionsNil sets the value for TooltipSections to be an explicit nil

### UnsetTooltipSections
`func (o *Upgrade) UnsetTooltipSections()`

UnsetTooltipSections ensures that no value is present for TooltipSections, not even an explicit nil
### GetType

`func (o *Upgrade) GetType() ItemType`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Upgrade) GetTypeOk() (*ItemType, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Upgrade) SetType(v ItemType)`

SetType sets Type field to given value.


### GetUpdateTime

`func (o *Upgrade) GetUpdateTime() int64`

GetUpdateTime returns the UpdateTime field if non-nil, zero value otherwise.

### GetUpdateTimeOk

`func (o *Upgrade) GetUpdateTimeOk() (*int64, bool)`

GetUpdateTimeOk returns a tuple with the UpdateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateTime

`func (o *Upgrade) SetUpdateTime(v int64)`

SetUpdateTime sets UpdateTime field to given value.

### HasUpdateTime

`func (o *Upgrade) HasUpdateTime() bool`

HasUpdateTime returns a boolean if a field has been set.

### SetUpdateTimeNil

`func (o *Upgrade) SetUpdateTimeNil(b bool)`

 SetUpdateTimeNil sets the value for UpdateTime to be an explicit nil

### UnsetUpdateTime
`func (o *Upgrade) UnsetUpdateTime()`

UnsetUpdateTime ensures that no value is present for UpdateTime, not even an explicit nil
### GetUpgrades

`func (o *Upgrade) GetUpgrades() []RawAbilityUpgrade`

GetUpgrades returns the Upgrades field if non-nil, zero value otherwise.

### GetUpgradesOk

`func (o *Upgrade) GetUpgradesOk() (*[]RawAbilityUpgrade, bool)`

GetUpgradesOk returns a tuple with the Upgrades field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpgrades

`func (o *Upgrade) SetUpgrades(v []RawAbilityUpgrade)`

SetUpgrades sets Upgrades field to given value.

### HasUpgrades

`func (o *Upgrade) HasUpgrades() bool`

HasUpgrades returns a boolean if a field has been set.

### SetUpgradesNil

`func (o *Upgrade) SetUpgradesNil(b bool)`

 SetUpgradesNil sets the value for Upgrades to be an explicit nil

### UnsetUpgrades
`func (o *Upgrade) UnsetUpgrades()`

UnsetUpgrades ensures that no value is present for Upgrades, not even an explicit nil
### GetWeaponInfo

`func (o *Upgrade) GetWeaponInfo() RawItemWeaponInfoInner`

GetWeaponInfo returns the WeaponInfo field if non-nil, zero value otherwise.

### GetWeaponInfoOk

`func (o *Upgrade) GetWeaponInfoOk() (*RawItemWeaponInfoInner, bool)`

GetWeaponInfoOk returns a tuple with the WeaponInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponInfo

`func (o *Upgrade) SetWeaponInfo(v RawItemWeaponInfoInner)`

SetWeaponInfo sets WeaponInfo field to given value.

### HasWeaponInfo

`func (o *Upgrade) HasWeaponInfo() bool`

HasWeaponInfo returns a boolean if a field has been set.

### SetWeaponInfoNil

`func (o *Upgrade) SetWeaponInfoNil(b bool)`

 SetWeaponInfoNil sets the value for WeaponInfo to be an explicit nil

### UnsetWeaponInfo
`func (o *Upgrade) UnsetWeaponInfo()`

UnsetWeaponInfo ensures that no value is present for WeaponInfo, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


