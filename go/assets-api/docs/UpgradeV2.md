# UpgradeV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** |  | 
**ClassName** | **string** |  | 
**Name** | **string** |  | 
**StartTrained** | Pointer to **NullableBool** |  | [optional] 
**Image** | Pointer to **NullableString** |  | [optional] 
**ImageWebp** | Pointer to **NullableString** |  | [optional] 
**Hero** | Pointer to **NullableInt32** |  | [optional] 
**Heroes** | Pointer to **[]int32** |  | [optional] 
**UpdateTime** | Pointer to **NullableInt32** |  | [optional] 
**Properties** | Pointer to [**map[string]UpgradePropertyV2**](UpgradePropertyV2.md) |  | [optional] 
**WeaponInfo** | Pointer to [**NullableRawItemWeaponInfoV2**](RawItemWeaponInfoV2.md) |  | [optional] 
**Type** | Pointer to **string** |  | [optional] [default to "upgrade"]
**ShopImage** | Pointer to **NullableString** |  | [optional] 
**ShopImageWebp** | Pointer to **NullableString** |  | [optional] 
**ShopImageSmall** | Pointer to **NullableString** |  | [optional] 
**ShopImageSmallWebp** | Pointer to **NullableString** |  | [optional] 
**ItemSlotType** | [**ItemSlotTypeV2**](ItemSlotTypeV2.md) |  | 
**ItemTier** | [**ItemTierV2**](ItemTierV2.md) |  | 
**Disabled** | Pointer to **NullableBool** |  | [optional] 
**Description** | Pointer to [**NullableUpgradeDescriptionV2**](UpgradeDescriptionV2.md) |  | [optional] 
**Activation** | [**RawAbilityActivationV2**](RawAbilityActivationV2.md) |  | 
**Imbue** | Pointer to [**NullableRawAbilityImbueV2**](RawAbilityImbueV2.md) |  | [optional] 
**ComponentItems** | Pointer to **[]string** |  | [optional] 
**TooltipSections** | Pointer to [**[]UpgradeTooltipSectionV2**](UpgradeTooltipSectionV2.md) |  | [optional] 
**Upgrades** | Pointer to [**[]RawAbilityUpgradeV2**](RawAbilityUpgradeV2.md) |  | [optional] 
**IsActiveItem** | **bool** |  | [readonly] 
**Shopable** | **bool** |  | [readonly] 
**Cost** | **NullableInt32** |  | [readonly] 

## Methods

### NewUpgradeV2

`func NewUpgradeV2(id int32, className string, name string, itemSlotType ItemSlotTypeV2, itemTier ItemTierV2, activation RawAbilityActivationV2, isActiveItem bool, shopable bool, cost NullableInt32, ) *UpgradeV2`

NewUpgradeV2 instantiates a new UpgradeV2 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpgradeV2WithDefaults

`func NewUpgradeV2WithDefaults() *UpgradeV2`

NewUpgradeV2WithDefaults instantiates a new UpgradeV2 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *UpgradeV2) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *UpgradeV2) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *UpgradeV2) SetId(v int32)`

SetId sets Id field to given value.


### GetClassName

`func (o *UpgradeV2) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *UpgradeV2) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *UpgradeV2) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetName

`func (o *UpgradeV2) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *UpgradeV2) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *UpgradeV2) SetName(v string)`

SetName sets Name field to given value.


### GetStartTrained

`func (o *UpgradeV2) GetStartTrained() bool`

GetStartTrained returns the StartTrained field if non-nil, zero value otherwise.

### GetStartTrainedOk

`func (o *UpgradeV2) GetStartTrainedOk() (*bool, bool)`

GetStartTrainedOk returns a tuple with the StartTrained field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTrained

`func (o *UpgradeV2) SetStartTrained(v bool)`

SetStartTrained sets StartTrained field to given value.

### HasStartTrained

`func (o *UpgradeV2) HasStartTrained() bool`

HasStartTrained returns a boolean if a field has been set.

### SetStartTrainedNil

`func (o *UpgradeV2) SetStartTrainedNil(b bool)`

 SetStartTrainedNil sets the value for StartTrained to be an explicit nil

### UnsetStartTrained
`func (o *UpgradeV2) UnsetStartTrained()`

UnsetStartTrained ensures that no value is present for StartTrained, not even an explicit nil
### GetImage

`func (o *UpgradeV2) GetImage() string`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *UpgradeV2) GetImageOk() (*string, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *UpgradeV2) SetImage(v string)`

SetImage sets Image field to given value.

### HasImage

`func (o *UpgradeV2) HasImage() bool`

HasImage returns a boolean if a field has been set.

### SetImageNil

`func (o *UpgradeV2) SetImageNil(b bool)`

 SetImageNil sets the value for Image to be an explicit nil

### UnsetImage
`func (o *UpgradeV2) UnsetImage()`

UnsetImage ensures that no value is present for Image, not even an explicit nil
### GetImageWebp

`func (o *UpgradeV2) GetImageWebp() string`

GetImageWebp returns the ImageWebp field if non-nil, zero value otherwise.

### GetImageWebpOk

`func (o *UpgradeV2) GetImageWebpOk() (*string, bool)`

GetImageWebpOk returns a tuple with the ImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImageWebp

`func (o *UpgradeV2) SetImageWebp(v string)`

SetImageWebp sets ImageWebp field to given value.

### HasImageWebp

`func (o *UpgradeV2) HasImageWebp() bool`

HasImageWebp returns a boolean if a field has been set.

### SetImageWebpNil

`func (o *UpgradeV2) SetImageWebpNil(b bool)`

 SetImageWebpNil sets the value for ImageWebp to be an explicit nil

### UnsetImageWebp
`func (o *UpgradeV2) UnsetImageWebp()`

UnsetImageWebp ensures that no value is present for ImageWebp, not even an explicit nil
### GetHero

`func (o *UpgradeV2) GetHero() int32`

GetHero returns the Hero field if non-nil, zero value otherwise.

### GetHeroOk

`func (o *UpgradeV2) GetHeroOk() (*int32, bool)`

GetHeroOk returns a tuple with the Hero field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHero

`func (o *UpgradeV2) SetHero(v int32)`

SetHero sets Hero field to given value.

### HasHero

`func (o *UpgradeV2) HasHero() bool`

HasHero returns a boolean if a field has been set.

### SetHeroNil

`func (o *UpgradeV2) SetHeroNil(b bool)`

 SetHeroNil sets the value for Hero to be an explicit nil

### UnsetHero
`func (o *UpgradeV2) UnsetHero()`

UnsetHero ensures that no value is present for Hero, not even an explicit nil
### GetHeroes

`func (o *UpgradeV2) GetHeroes() []int32`

GetHeroes returns the Heroes field if non-nil, zero value otherwise.

### GetHeroesOk

`func (o *UpgradeV2) GetHeroesOk() (*[]int32, bool)`

GetHeroesOk returns a tuple with the Heroes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroes

`func (o *UpgradeV2) SetHeroes(v []int32)`

SetHeroes sets Heroes field to given value.

### HasHeroes

`func (o *UpgradeV2) HasHeroes() bool`

HasHeroes returns a boolean if a field has been set.

### SetHeroesNil

`func (o *UpgradeV2) SetHeroesNil(b bool)`

 SetHeroesNil sets the value for Heroes to be an explicit nil

### UnsetHeroes
`func (o *UpgradeV2) UnsetHeroes()`

UnsetHeroes ensures that no value is present for Heroes, not even an explicit nil
### GetUpdateTime

`func (o *UpgradeV2) GetUpdateTime() int32`

GetUpdateTime returns the UpdateTime field if non-nil, zero value otherwise.

### GetUpdateTimeOk

`func (o *UpgradeV2) GetUpdateTimeOk() (*int32, bool)`

GetUpdateTimeOk returns a tuple with the UpdateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateTime

`func (o *UpgradeV2) SetUpdateTime(v int32)`

SetUpdateTime sets UpdateTime field to given value.

### HasUpdateTime

`func (o *UpgradeV2) HasUpdateTime() bool`

HasUpdateTime returns a boolean if a field has been set.

### SetUpdateTimeNil

`func (o *UpgradeV2) SetUpdateTimeNil(b bool)`

 SetUpdateTimeNil sets the value for UpdateTime to be an explicit nil

### UnsetUpdateTime
`func (o *UpgradeV2) UnsetUpdateTime()`

UnsetUpdateTime ensures that no value is present for UpdateTime, not even an explicit nil
### GetProperties

`func (o *UpgradeV2) GetProperties() map[string]UpgradePropertyV2`

GetProperties returns the Properties field if non-nil, zero value otherwise.

### GetPropertiesOk

`func (o *UpgradeV2) GetPropertiesOk() (*map[string]UpgradePropertyV2, bool)`

GetPropertiesOk returns a tuple with the Properties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperties

`func (o *UpgradeV2) SetProperties(v map[string]UpgradePropertyV2)`

SetProperties sets Properties field to given value.

### HasProperties

`func (o *UpgradeV2) HasProperties() bool`

HasProperties returns a boolean if a field has been set.

### SetPropertiesNil

`func (o *UpgradeV2) SetPropertiesNil(b bool)`

 SetPropertiesNil sets the value for Properties to be an explicit nil

### UnsetProperties
`func (o *UpgradeV2) UnsetProperties()`

UnsetProperties ensures that no value is present for Properties, not even an explicit nil
### GetWeaponInfo

`func (o *UpgradeV2) GetWeaponInfo() RawItemWeaponInfoV2`

GetWeaponInfo returns the WeaponInfo field if non-nil, zero value otherwise.

### GetWeaponInfoOk

`func (o *UpgradeV2) GetWeaponInfoOk() (*RawItemWeaponInfoV2, bool)`

GetWeaponInfoOk returns a tuple with the WeaponInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponInfo

`func (o *UpgradeV2) SetWeaponInfo(v RawItemWeaponInfoV2)`

SetWeaponInfo sets WeaponInfo field to given value.

### HasWeaponInfo

`func (o *UpgradeV2) HasWeaponInfo() bool`

HasWeaponInfo returns a boolean if a field has been set.

### SetWeaponInfoNil

`func (o *UpgradeV2) SetWeaponInfoNil(b bool)`

 SetWeaponInfoNil sets the value for WeaponInfo to be an explicit nil

### UnsetWeaponInfo
`func (o *UpgradeV2) UnsetWeaponInfo()`

UnsetWeaponInfo ensures that no value is present for WeaponInfo, not even an explicit nil
### GetType

`func (o *UpgradeV2) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *UpgradeV2) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *UpgradeV2) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *UpgradeV2) HasType() bool`

HasType returns a boolean if a field has been set.

### GetShopImage

`func (o *UpgradeV2) GetShopImage() string`

GetShopImage returns the ShopImage field if non-nil, zero value otherwise.

### GetShopImageOk

`func (o *UpgradeV2) GetShopImageOk() (*string, bool)`

GetShopImageOk returns a tuple with the ShopImage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImage

`func (o *UpgradeV2) SetShopImage(v string)`

SetShopImage sets ShopImage field to given value.

### HasShopImage

`func (o *UpgradeV2) HasShopImage() bool`

HasShopImage returns a boolean if a field has been set.

### SetShopImageNil

`func (o *UpgradeV2) SetShopImageNil(b bool)`

 SetShopImageNil sets the value for ShopImage to be an explicit nil

### UnsetShopImage
`func (o *UpgradeV2) UnsetShopImage()`

UnsetShopImage ensures that no value is present for ShopImage, not even an explicit nil
### GetShopImageWebp

`func (o *UpgradeV2) GetShopImageWebp() string`

GetShopImageWebp returns the ShopImageWebp field if non-nil, zero value otherwise.

### GetShopImageWebpOk

`func (o *UpgradeV2) GetShopImageWebpOk() (*string, bool)`

GetShopImageWebpOk returns a tuple with the ShopImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageWebp

`func (o *UpgradeV2) SetShopImageWebp(v string)`

SetShopImageWebp sets ShopImageWebp field to given value.

### HasShopImageWebp

`func (o *UpgradeV2) HasShopImageWebp() bool`

HasShopImageWebp returns a boolean if a field has been set.

### SetShopImageWebpNil

`func (o *UpgradeV2) SetShopImageWebpNil(b bool)`

 SetShopImageWebpNil sets the value for ShopImageWebp to be an explicit nil

### UnsetShopImageWebp
`func (o *UpgradeV2) UnsetShopImageWebp()`

UnsetShopImageWebp ensures that no value is present for ShopImageWebp, not even an explicit nil
### GetShopImageSmall

`func (o *UpgradeV2) GetShopImageSmall() string`

GetShopImageSmall returns the ShopImageSmall field if non-nil, zero value otherwise.

### GetShopImageSmallOk

`func (o *UpgradeV2) GetShopImageSmallOk() (*string, bool)`

GetShopImageSmallOk returns a tuple with the ShopImageSmall field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageSmall

`func (o *UpgradeV2) SetShopImageSmall(v string)`

SetShopImageSmall sets ShopImageSmall field to given value.

### HasShopImageSmall

`func (o *UpgradeV2) HasShopImageSmall() bool`

HasShopImageSmall returns a boolean if a field has been set.

### SetShopImageSmallNil

`func (o *UpgradeV2) SetShopImageSmallNil(b bool)`

 SetShopImageSmallNil sets the value for ShopImageSmall to be an explicit nil

### UnsetShopImageSmall
`func (o *UpgradeV2) UnsetShopImageSmall()`

UnsetShopImageSmall ensures that no value is present for ShopImageSmall, not even an explicit nil
### GetShopImageSmallWebp

`func (o *UpgradeV2) GetShopImageSmallWebp() string`

GetShopImageSmallWebp returns the ShopImageSmallWebp field if non-nil, zero value otherwise.

### GetShopImageSmallWebpOk

`func (o *UpgradeV2) GetShopImageSmallWebpOk() (*string, bool)`

GetShopImageSmallWebpOk returns a tuple with the ShopImageSmallWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageSmallWebp

`func (o *UpgradeV2) SetShopImageSmallWebp(v string)`

SetShopImageSmallWebp sets ShopImageSmallWebp field to given value.

### HasShopImageSmallWebp

`func (o *UpgradeV2) HasShopImageSmallWebp() bool`

HasShopImageSmallWebp returns a boolean if a field has been set.

### SetShopImageSmallWebpNil

`func (o *UpgradeV2) SetShopImageSmallWebpNil(b bool)`

 SetShopImageSmallWebpNil sets the value for ShopImageSmallWebp to be an explicit nil

### UnsetShopImageSmallWebp
`func (o *UpgradeV2) UnsetShopImageSmallWebp()`

UnsetShopImageSmallWebp ensures that no value is present for ShopImageSmallWebp, not even an explicit nil
### GetItemSlotType

`func (o *UpgradeV2) GetItemSlotType() ItemSlotTypeV2`

GetItemSlotType returns the ItemSlotType field if non-nil, zero value otherwise.

### GetItemSlotTypeOk

`func (o *UpgradeV2) GetItemSlotTypeOk() (*ItemSlotTypeV2, bool)`

GetItemSlotTypeOk returns a tuple with the ItemSlotType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemSlotType

`func (o *UpgradeV2) SetItemSlotType(v ItemSlotTypeV2)`

SetItemSlotType sets ItemSlotType field to given value.


### GetItemTier

`func (o *UpgradeV2) GetItemTier() ItemTierV2`

GetItemTier returns the ItemTier field if non-nil, zero value otherwise.

### GetItemTierOk

`func (o *UpgradeV2) GetItemTierOk() (*ItemTierV2, bool)`

GetItemTierOk returns a tuple with the ItemTier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemTier

`func (o *UpgradeV2) SetItemTier(v ItemTierV2)`

SetItemTier sets ItemTier field to given value.


### GetDisabled

`func (o *UpgradeV2) GetDisabled() bool`

GetDisabled returns the Disabled field if non-nil, zero value otherwise.

### GetDisabledOk

`func (o *UpgradeV2) GetDisabledOk() (*bool, bool)`

GetDisabledOk returns a tuple with the Disabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisabled

`func (o *UpgradeV2) SetDisabled(v bool)`

SetDisabled sets Disabled field to given value.

### HasDisabled

`func (o *UpgradeV2) HasDisabled() bool`

HasDisabled returns a boolean if a field has been set.

### SetDisabledNil

`func (o *UpgradeV2) SetDisabledNil(b bool)`

 SetDisabledNil sets the value for Disabled to be an explicit nil

### UnsetDisabled
`func (o *UpgradeV2) UnsetDisabled()`

UnsetDisabled ensures that no value is present for Disabled, not even an explicit nil
### GetDescription

`func (o *UpgradeV2) GetDescription() UpgradeDescriptionV2`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *UpgradeV2) GetDescriptionOk() (*UpgradeDescriptionV2, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *UpgradeV2) SetDescription(v UpgradeDescriptionV2)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *UpgradeV2) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *UpgradeV2) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *UpgradeV2) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetActivation

`func (o *UpgradeV2) GetActivation() RawAbilityActivationV2`

GetActivation returns the Activation field if non-nil, zero value otherwise.

### GetActivationOk

`func (o *UpgradeV2) GetActivationOk() (*RawAbilityActivationV2, bool)`

GetActivationOk returns a tuple with the Activation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActivation

`func (o *UpgradeV2) SetActivation(v RawAbilityActivationV2)`

SetActivation sets Activation field to given value.


### GetImbue

`func (o *UpgradeV2) GetImbue() RawAbilityImbueV2`

GetImbue returns the Imbue field if non-nil, zero value otherwise.

### GetImbueOk

`func (o *UpgradeV2) GetImbueOk() (*RawAbilityImbueV2, bool)`

GetImbueOk returns a tuple with the Imbue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImbue

`func (o *UpgradeV2) SetImbue(v RawAbilityImbueV2)`

SetImbue sets Imbue field to given value.

### HasImbue

`func (o *UpgradeV2) HasImbue() bool`

HasImbue returns a boolean if a field has been set.

### SetImbueNil

`func (o *UpgradeV2) SetImbueNil(b bool)`

 SetImbueNil sets the value for Imbue to be an explicit nil

### UnsetImbue
`func (o *UpgradeV2) UnsetImbue()`

UnsetImbue ensures that no value is present for Imbue, not even an explicit nil
### GetComponentItems

`func (o *UpgradeV2) GetComponentItems() []string`

GetComponentItems returns the ComponentItems field if non-nil, zero value otherwise.

### GetComponentItemsOk

`func (o *UpgradeV2) GetComponentItemsOk() (*[]string, bool)`

GetComponentItemsOk returns a tuple with the ComponentItems field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComponentItems

`func (o *UpgradeV2) SetComponentItems(v []string)`

SetComponentItems sets ComponentItems field to given value.

### HasComponentItems

`func (o *UpgradeV2) HasComponentItems() bool`

HasComponentItems returns a boolean if a field has been set.

### SetComponentItemsNil

`func (o *UpgradeV2) SetComponentItemsNil(b bool)`

 SetComponentItemsNil sets the value for ComponentItems to be an explicit nil

### UnsetComponentItems
`func (o *UpgradeV2) UnsetComponentItems()`

UnsetComponentItems ensures that no value is present for ComponentItems, not even an explicit nil
### GetTooltipSections

`func (o *UpgradeV2) GetTooltipSections() []UpgradeTooltipSectionV2`

GetTooltipSections returns the TooltipSections field if non-nil, zero value otherwise.

### GetTooltipSectionsOk

`func (o *UpgradeV2) GetTooltipSectionsOk() (*[]UpgradeTooltipSectionV2, bool)`

GetTooltipSectionsOk returns a tuple with the TooltipSections field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipSections

`func (o *UpgradeV2) SetTooltipSections(v []UpgradeTooltipSectionV2)`

SetTooltipSections sets TooltipSections field to given value.

### HasTooltipSections

`func (o *UpgradeV2) HasTooltipSections() bool`

HasTooltipSections returns a boolean if a field has been set.

### SetTooltipSectionsNil

`func (o *UpgradeV2) SetTooltipSectionsNil(b bool)`

 SetTooltipSectionsNil sets the value for TooltipSections to be an explicit nil

### UnsetTooltipSections
`func (o *UpgradeV2) UnsetTooltipSections()`

UnsetTooltipSections ensures that no value is present for TooltipSections, not even an explicit nil
### GetUpgrades

`func (o *UpgradeV2) GetUpgrades() []RawAbilityUpgradeV2`

GetUpgrades returns the Upgrades field if non-nil, zero value otherwise.

### GetUpgradesOk

`func (o *UpgradeV2) GetUpgradesOk() (*[]RawAbilityUpgradeV2, bool)`

GetUpgradesOk returns a tuple with the Upgrades field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpgrades

`func (o *UpgradeV2) SetUpgrades(v []RawAbilityUpgradeV2)`

SetUpgrades sets Upgrades field to given value.

### HasUpgrades

`func (o *UpgradeV2) HasUpgrades() bool`

HasUpgrades returns a boolean if a field has been set.

### SetUpgradesNil

`func (o *UpgradeV2) SetUpgradesNil(b bool)`

 SetUpgradesNil sets the value for Upgrades to be an explicit nil

### UnsetUpgrades
`func (o *UpgradeV2) UnsetUpgrades()`

UnsetUpgrades ensures that no value is present for Upgrades, not even an explicit nil
### GetIsActiveItem

`func (o *UpgradeV2) GetIsActiveItem() bool`

GetIsActiveItem returns the IsActiveItem field if non-nil, zero value otherwise.

### GetIsActiveItemOk

`func (o *UpgradeV2) GetIsActiveItemOk() (*bool, bool)`

GetIsActiveItemOk returns a tuple with the IsActiveItem field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsActiveItem

`func (o *UpgradeV2) SetIsActiveItem(v bool)`

SetIsActiveItem sets IsActiveItem field to given value.


### GetShopable

`func (o *UpgradeV2) GetShopable() bool`

GetShopable returns the Shopable field if non-nil, zero value otherwise.

### GetShopableOk

`func (o *UpgradeV2) GetShopableOk() (*bool, bool)`

GetShopableOk returns a tuple with the Shopable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopable

`func (o *UpgradeV2) SetShopable(v bool)`

SetShopable sets Shopable field to given value.


### GetCost

`func (o *UpgradeV2) GetCost() int32`

GetCost returns the Cost field if non-nil, zero value otherwise.

### GetCostOk

`func (o *UpgradeV2) GetCostOk() (*int32, bool)`

GetCostOk returns a tuple with the Cost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCost

`func (o *UpgradeV2) SetCost(v int32)`

SetCost sets Cost field to given value.


### SetCostNil

`func (o *UpgradeV2) SetCostNil(b bool)`

 SetCostNil sets the value for Cost to be an explicit nil

### UnsetCost
`func (o *UpgradeV2) UnsetCost()`

UnsetCost ensures that no value is present for Cost, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


