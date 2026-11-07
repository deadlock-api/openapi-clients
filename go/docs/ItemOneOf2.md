# ItemOneOf2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Activation** | [**AbilityActivation**](AbilityActivation.md) |  | 
**ClassName** | **string** |  | 
**ComponentItems** | Pointer to **[]string** |  | [optional] 
**CorruptedInfo** | Pointer to [**NullableCorruptedItemInfo**](CorruptedItemInfo.md) | Present on upgrades the Broker can corrupt (build 6711+). | [optional] 
**Cost** | Pointer to **NullableInt32** |  | [optional] 
**Description** | Pointer to [**NullableUpgradeDescription**](UpgradeDescription.md) |  | [optional] 
**DisableItemTarget** | Pointer to **NullableString** |  | [optional] 
**Disabled** | Pointer to **NullableBool** |  | [optional] 
**DisabledShopFilters** | Pointer to **[]string** | Shop filters (&#x60;snake_case&#x60; &#x60;EShopFilter*&#x60; names) this item is hidden from even though its stats would match them. | [optional] 
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
**ShopFilters** | Pointer to **[]string** | Extra shop filters (&#x60;snake_case&#x60; &#x60;EShopFilter*&#x60; names, e.g. &#x60;status_grounded&#x60;) this item shows up under, beyond those derived from its stats. | [optional] 
**ShopImage** | Pointer to **NullableString** |  | [optional] 
**ShopImageSmall** | Pointer to **NullableString** |  | [optional] 
**ShopImageSmallWebp** | Pointer to **NullableString** |  | [optional] 
**ShopImageWebp** | Pointer to **NullableString** |  | [optional] 
**ShopVersion** | Pointer to **NullableInt64** |  | [optional] 
**Shopable** | **bool** |  | 
**StartTrained** | Pointer to **NullableBool** |  | [optional] 
**TooltipSections** | Pointer to [**[]UpgradeTooltipSection**](UpgradeTooltipSection.md) |  | [optional] 
**UpdateTime** | Pointer to **NullableInt64** |  | [optional] 
**Upgrades** | Pointer to [**[]RawAbilityUpgrade**](RawAbilityUpgrade.md) |  | [optional] 
**WeaponInfo** | Pointer to [**NullableRawItemWeaponInfoInner**](RawItemWeaponInfoInner.md) |  | [optional] 
**Type** | **string** |  | 

## Methods

### NewItemOneOf2

`func NewItemOneOf2(activation AbilityActivation, className string, id int32, isActiveItem bool, itemSlotType ItemSlotType, itemTier int32, name string, shopable bool, type_ string, ) *ItemOneOf2`

NewItemOneOf2 instantiates a new ItemOneOf2 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewItemOneOf2WithDefaults

`func NewItemOneOf2WithDefaults() *ItemOneOf2`

NewItemOneOf2WithDefaults instantiates a new ItemOneOf2 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetActivation

`func (o *ItemOneOf2) GetActivation() AbilityActivation`

GetActivation returns the Activation field if non-nil, zero value otherwise.

### GetActivationOk

`func (o *ItemOneOf2) GetActivationOk() (*AbilityActivation, bool)`

GetActivationOk returns a tuple with the Activation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActivation

`func (o *ItemOneOf2) SetActivation(v AbilityActivation)`

SetActivation sets Activation field to given value.


### GetClassName

`func (o *ItemOneOf2) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *ItemOneOf2) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *ItemOneOf2) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetComponentItems

`func (o *ItemOneOf2) GetComponentItems() []string`

GetComponentItems returns the ComponentItems field if non-nil, zero value otherwise.

### GetComponentItemsOk

`func (o *ItemOneOf2) GetComponentItemsOk() (*[]string, bool)`

GetComponentItemsOk returns a tuple with the ComponentItems field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComponentItems

`func (o *ItemOneOf2) SetComponentItems(v []string)`

SetComponentItems sets ComponentItems field to given value.

### HasComponentItems

`func (o *ItemOneOf2) HasComponentItems() bool`

HasComponentItems returns a boolean if a field has been set.

### SetComponentItemsNil

`func (o *ItemOneOf2) SetComponentItemsNil(b bool)`

 SetComponentItemsNil sets the value for ComponentItems to be an explicit nil

### UnsetComponentItems
`func (o *ItemOneOf2) UnsetComponentItems()`

UnsetComponentItems ensures that no value is present for ComponentItems, not even an explicit nil
### GetCorruptedInfo

`func (o *ItemOneOf2) GetCorruptedInfo() CorruptedItemInfo`

GetCorruptedInfo returns the CorruptedInfo field if non-nil, zero value otherwise.

### GetCorruptedInfoOk

`func (o *ItemOneOf2) GetCorruptedInfoOk() (*CorruptedItemInfo, bool)`

GetCorruptedInfoOk returns a tuple with the CorruptedInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCorruptedInfo

`func (o *ItemOneOf2) SetCorruptedInfo(v CorruptedItemInfo)`

SetCorruptedInfo sets CorruptedInfo field to given value.

### HasCorruptedInfo

`func (o *ItemOneOf2) HasCorruptedInfo() bool`

HasCorruptedInfo returns a boolean if a field has been set.

### SetCorruptedInfoNil

`func (o *ItemOneOf2) SetCorruptedInfoNil(b bool)`

 SetCorruptedInfoNil sets the value for CorruptedInfo to be an explicit nil

### UnsetCorruptedInfo
`func (o *ItemOneOf2) UnsetCorruptedInfo()`

UnsetCorruptedInfo ensures that no value is present for CorruptedInfo, not even an explicit nil
### GetCost

`func (o *ItemOneOf2) GetCost() int32`

GetCost returns the Cost field if non-nil, zero value otherwise.

### GetCostOk

`func (o *ItemOneOf2) GetCostOk() (*int32, bool)`

GetCostOk returns a tuple with the Cost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCost

`func (o *ItemOneOf2) SetCost(v int32)`

SetCost sets Cost field to given value.

### HasCost

`func (o *ItemOneOf2) HasCost() bool`

HasCost returns a boolean if a field has been set.

### SetCostNil

`func (o *ItemOneOf2) SetCostNil(b bool)`

 SetCostNil sets the value for Cost to be an explicit nil

### UnsetCost
`func (o *ItemOneOf2) UnsetCost()`

UnsetCost ensures that no value is present for Cost, not even an explicit nil
### GetDescription

`func (o *ItemOneOf2) GetDescription() UpgradeDescription`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ItemOneOf2) GetDescriptionOk() (*UpgradeDescription, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ItemOneOf2) SetDescription(v UpgradeDescription)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ItemOneOf2) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *ItemOneOf2) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *ItemOneOf2) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetDisableItemTarget

`func (o *ItemOneOf2) GetDisableItemTarget() string`

GetDisableItemTarget returns the DisableItemTarget field if non-nil, zero value otherwise.

### GetDisableItemTargetOk

`func (o *ItemOneOf2) GetDisableItemTargetOk() (*string, bool)`

GetDisableItemTargetOk returns a tuple with the DisableItemTarget field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisableItemTarget

`func (o *ItemOneOf2) SetDisableItemTarget(v string)`

SetDisableItemTarget sets DisableItemTarget field to given value.

### HasDisableItemTarget

`func (o *ItemOneOf2) HasDisableItemTarget() bool`

HasDisableItemTarget returns a boolean if a field has been set.

### SetDisableItemTargetNil

`func (o *ItemOneOf2) SetDisableItemTargetNil(b bool)`

 SetDisableItemTargetNil sets the value for DisableItemTarget to be an explicit nil

### UnsetDisableItemTarget
`func (o *ItemOneOf2) UnsetDisableItemTarget()`

UnsetDisableItemTarget ensures that no value is present for DisableItemTarget, not even an explicit nil
### GetDisabled

`func (o *ItemOneOf2) GetDisabled() bool`

GetDisabled returns the Disabled field if non-nil, zero value otherwise.

### GetDisabledOk

`func (o *ItemOneOf2) GetDisabledOk() (*bool, bool)`

GetDisabledOk returns a tuple with the Disabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisabled

`func (o *ItemOneOf2) SetDisabled(v bool)`

SetDisabled sets Disabled field to given value.

### HasDisabled

`func (o *ItemOneOf2) HasDisabled() bool`

HasDisabled returns a boolean if a field has been set.

### SetDisabledNil

`func (o *ItemOneOf2) SetDisabledNil(b bool)`

 SetDisabledNil sets the value for Disabled to be an explicit nil

### UnsetDisabled
`func (o *ItemOneOf2) UnsetDisabled()`

UnsetDisabled ensures that no value is present for Disabled, not even an explicit nil
### GetDisabledShopFilters

`func (o *ItemOneOf2) GetDisabledShopFilters() []string`

GetDisabledShopFilters returns the DisabledShopFilters field if non-nil, zero value otherwise.

### GetDisabledShopFiltersOk

`func (o *ItemOneOf2) GetDisabledShopFiltersOk() (*[]string, bool)`

GetDisabledShopFiltersOk returns a tuple with the DisabledShopFilters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisabledShopFilters

`func (o *ItemOneOf2) SetDisabledShopFilters(v []string)`

SetDisabledShopFilters sets DisabledShopFilters field to given value.

### HasDisabledShopFilters

`func (o *ItemOneOf2) HasDisabledShopFilters() bool`

HasDisabledShopFilters returns a boolean if a field has been set.

### SetDisabledShopFiltersNil

`func (o *ItemOneOf2) SetDisabledShopFiltersNil(b bool)`

 SetDisabledShopFiltersNil sets the value for DisabledShopFilters to be an explicit nil

### UnsetDisabledShopFilters
`func (o *ItemOneOf2) UnsetDisabledShopFilters()`

UnsetDisabledShopFilters ensures that no value is present for DisabledShopFilters, not even an explicit nil
### GetHero

`func (o *ItemOneOf2) GetHero() int32`

GetHero returns the Hero field if non-nil, zero value otherwise.

### GetHeroOk

`func (o *ItemOneOf2) GetHeroOk() (*int32, bool)`

GetHeroOk returns a tuple with the Hero field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHero

`func (o *ItemOneOf2) SetHero(v int32)`

SetHero sets Hero field to given value.

### HasHero

`func (o *ItemOneOf2) HasHero() bool`

HasHero returns a boolean if a field has been set.

### SetHeroNil

`func (o *ItemOneOf2) SetHeroNil(b bool)`

 SetHeroNil sets the value for Hero to be an explicit nil

### UnsetHero
`func (o *ItemOneOf2) UnsetHero()`

UnsetHero ensures that no value is present for Hero, not even an explicit nil
### GetHeroes

`func (o *ItemOneOf2) GetHeroes() []int32`

GetHeroes returns the Heroes field if non-nil, zero value otherwise.

### GetHeroesOk

`func (o *ItemOneOf2) GetHeroesOk() (*[]int32, bool)`

GetHeroesOk returns a tuple with the Heroes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroes

`func (o *ItemOneOf2) SetHeroes(v []int32)`

SetHeroes sets Heroes field to given value.

### HasHeroes

`func (o *ItemOneOf2) HasHeroes() bool`

HasHeroes returns a boolean if a field has been set.

### SetHeroesNil

`func (o *ItemOneOf2) SetHeroesNil(b bool)`

 SetHeroesNil sets the value for Heroes to be an explicit nil

### UnsetHeroes
`func (o *ItemOneOf2) UnsetHeroes()`

UnsetHeroes ensures that no value is present for Heroes, not even an explicit nil
### GetId

`func (o *ItemOneOf2) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ItemOneOf2) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ItemOneOf2) SetId(v int32)`

SetId sets Id field to given value.


### GetImage

`func (o *ItemOneOf2) GetImage() string`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *ItemOneOf2) GetImageOk() (*string, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *ItemOneOf2) SetImage(v string)`

SetImage sets Image field to given value.

### HasImage

`func (o *ItemOneOf2) HasImage() bool`

HasImage returns a boolean if a field has been set.

### SetImageNil

`func (o *ItemOneOf2) SetImageNil(b bool)`

 SetImageNil sets the value for Image to be an explicit nil

### UnsetImage
`func (o *ItemOneOf2) UnsetImage()`

UnsetImage ensures that no value is present for Image, not even an explicit nil
### GetImageWebp

`func (o *ItemOneOf2) GetImageWebp() string`

GetImageWebp returns the ImageWebp field if non-nil, zero value otherwise.

### GetImageWebpOk

`func (o *ItemOneOf2) GetImageWebpOk() (*string, bool)`

GetImageWebpOk returns a tuple with the ImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImageWebp

`func (o *ItemOneOf2) SetImageWebp(v string)`

SetImageWebp sets ImageWebp field to given value.

### HasImageWebp

`func (o *ItemOneOf2) HasImageWebp() bool`

HasImageWebp returns a boolean if a field has been set.

### SetImageWebpNil

`func (o *ItemOneOf2) SetImageWebpNil(b bool)`

 SetImageWebpNil sets the value for ImageWebp to be an explicit nil

### UnsetImageWebp
`func (o *ItemOneOf2) UnsetImageWebp()`

UnsetImageWebp ensures that no value is present for ImageWebp, not even an explicit nil
### GetImbue

`func (o *ItemOneOf2) GetImbue() AbilityImbue`

GetImbue returns the Imbue field if non-nil, zero value otherwise.

### GetImbueOk

`func (o *ItemOneOf2) GetImbueOk() (*AbilityImbue, bool)`

GetImbueOk returns a tuple with the Imbue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImbue

`func (o *ItemOneOf2) SetImbue(v AbilityImbue)`

SetImbue sets Imbue field to given value.

### HasImbue

`func (o *ItemOneOf2) HasImbue() bool`

HasImbue returns a boolean if a field has been set.

### SetImbueNil

`func (o *ItemOneOf2) SetImbueNil(b bool)`

 SetImbueNil sets the value for Imbue to be an explicit nil

### UnsetImbue
`func (o *ItemOneOf2) UnsetImbue()`

UnsetImbue ensures that no value is present for Imbue, not even an explicit nil
### GetIsActiveItem

`func (o *ItemOneOf2) GetIsActiveItem() bool`

GetIsActiveItem returns the IsActiveItem field if non-nil, zero value otherwise.

### GetIsActiveItemOk

`func (o *ItemOneOf2) GetIsActiveItemOk() (*bool, bool)`

GetIsActiveItemOk returns a tuple with the IsActiveItem field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsActiveItem

`func (o *ItemOneOf2) SetIsActiveItem(v bool)`

SetIsActiveItem sets IsActiveItem field to given value.


### GetItemSlotType

`func (o *ItemOneOf2) GetItemSlotType() ItemSlotType`

GetItemSlotType returns the ItemSlotType field if non-nil, zero value otherwise.

### GetItemSlotTypeOk

`func (o *ItemOneOf2) GetItemSlotTypeOk() (*ItemSlotType, bool)`

GetItemSlotTypeOk returns a tuple with the ItemSlotType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemSlotType

`func (o *ItemOneOf2) SetItemSlotType(v ItemSlotType)`

SetItemSlotType sets ItemSlotType field to given value.


### GetItemTier

`func (o *ItemOneOf2) GetItemTier() int32`

GetItemTier returns the ItemTier field if non-nil, zero value otherwise.

### GetItemTierOk

`func (o *ItemOneOf2) GetItemTierOk() (*int32, bool)`

GetItemTierOk returns a tuple with the ItemTier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemTier

`func (o *ItemOneOf2) SetItemTier(v int32)`

SetItemTier sets ItemTier field to given value.


### GetName

`func (o *ItemOneOf2) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ItemOneOf2) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ItemOneOf2) SetName(v string)`

SetName sets Name field to given value.


### GetProperties

`func (o *ItemOneOf2) GetProperties() map[string]UpgradeProperty`

GetProperties returns the Properties field if non-nil, zero value otherwise.

### GetPropertiesOk

`func (o *ItemOneOf2) GetPropertiesOk() (*map[string]UpgradeProperty, bool)`

GetPropertiesOk returns a tuple with the Properties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperties

`func (o *ItemOneOf2) SetProperties(v map[string]UpgradeProperty)`

SetProperties sets Properties field to given value.

### HasProperties

`func (o *ItemOneOf2) HasProperties() bool`

HasProperties returns a boolean if a field has been set.

### SetPropertiesNil

`func (o *ItemOneOf2) SetPropertiesNil(b bool)`

 SetPropertiesNil sets the value for Properties to be an explicit nil

### UnsetProperties
`func (o *ItemOneOf2) UnsetProperties()`

UnsetProperties ensures that no value is present for Properties, not even an explicit nil
### GetShopFilters

`func (o *ItemOneOf2) GetShopFilters() []string`

GetShopFilters returns the ShopFilters field if non-nil, zero value otherwise.

### GetShopFiltersOk

`func (o *ItemOneOf2) GetShopFiltersOk() (*[]string, bool)`

GetShopFiltersOk returns a tuple with the ShopFilters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopFilters

`func (o *ItemOneOf2) SetShopFilters(v []string)`

SetShopFilters sets ShopFilters field to given value.

### HasShopFilters

`func (o *ItemOneOf2) HasShopFilters() bool`

HasShopFilters returns a boolean if a field has been set.

### SetShopFiltersNil

`func (o *ItemOneOf2) SetShopFiltersNil(b bool)`

 SetShopFiltersNil sets the value for ShopFilters to be an explicit nil

### UnsetShopFilters
`func (o *ItemOneOf2) UnsetShopFilters()`

UnsetShopFilters ensures that no value is present for ShopFilters, not even an explicit nil
### GetShopImage

`func (o *ItemOneOf2) GetShopImage() string`

GetShopImage returns the ShopImage field if non-nil, zero value otherwise.

### GetShopImageOk

`func (o *ItemOneOf2) GetShopImageOk() (*string, bool)`

GetShopImageOk returns a tuple with the ShopImage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImage

`func (o *ItemOneOf2) SetShopImage(v string)`

SetShopImage sets ShopImage field to given value.

### HasShopImage

`func (o *ItemOneOf2) HasShopImage() bool`

HasShopImage returns a boolean if a field has been set.

### SetShopImageNil

`func (o *ItemOneOf2) SetShopImageNil(b bool)`

 SetShopImageNil sets the value for ShopImage to be an explicit nil

### UnsetShopImage
`func (o *ItemOneOf2) UnsetShopImage()`

UnsetShopImage ensures that no value is present for ShopImage, not even an explicit nil
### GetShopImageSmall

`func (o *ItemOneOf2) GetShopImageSmall() string`

GetShopImageSmall returns the ShopImageSmall field if non-nil, zero value otherwise.

### GetShopImageSmallOk

`func (o *ItemOneOf2) GetShopImageSmallOk() (*string, bool)`

GetShopImageSmallOk returns a tuple with the ShopImageSmall field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageSmall

`func (o *ItemOneOf2) SetShopImageSmall(v string)`

SetShopImageSmall sets ShopImageSmall field to given value.

### HasShopImageSmall

`func (o *ItemOneOf2) HasShopImageSmall() bool`

HasShopImageSmall returns a boolean if a field has been set.

### SetShopImageSmallNil

`func (o *ItemOneOf2) SetShopImageSmallNil(b bool)`

 SetShopImageSmallNil sets the value for ShopImageSmall to be an explicit nil

### UnsetShopImageSmall
`func (o *ItemOneOf2) UnsetShopImageSmall()`

UnsetShopImageSmall ensures that no value is present for ShopImageSmall, not even an explicit nil
### GetShopImageSmallWebp

`func (o *ItemOneOf2) GetShopImageSmallWebp() string`

GetShopImageSmallWebp returns the ShopImageSmallWebp field if non-nil, zero value otherwise.

### GetShopImageSmallWebpOk

`func (o *ItemOneOf2) GetShopImageSmallWebpOk() (*string, bool)`

GetShopImageSmallWebpOk returns a tuple with the ShopImageSmallWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageSmallWebp

`func (o *ItemOneOf2) SetShopImageSmallWebp(v string)`

SetShopImageSmallWebp sets ShopImageSmallWebp field to given value.

### HasShopImageSmallWebp

`func (o *ItemOneOf2) HasShopImageSmallWebp() bool`

HasShopImageSmallWebp returns a boolean if a field has been set.

### SetShopImageSmallWebpNil

`func (o *ItemOneOf2) SetShopImageSmallWebpNil(b bool)`

 SetShopImageSmallWebpNil sets the value for ShopImageSmallWebp to be an explicit nil

### UnsetShopImageSmallWebp
`func (o *ItemOneOf2) UnsetShopImageSmallWebp()`

UnsetShopImageSmallWebp ensures that no value is present for ShopImageSmallWebp, not even an explicit nil
### GetShopImageWebp

`func (o *ItemOneOf2) GetShopImageWebp() string`

GetShopImageWebp returns the ShopImageWebp field if non-nil, zero value otherwise.

### GetShopImageWebpOk

`func (o *ItemOneOf2) GetShopImageWebpOk() (*string, bool)`

GetShopImageWebpOk returns a tuple with the ShopImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageWebp

`func (o *ItemOneOf2) SetShopImageWebp(v string)`

SetShopImageWebp sets ShopImageWebp field to given value.

### HasShopImageWebp

`func (o *ItemOneOf2) HasShopImageWebp() bool`

HasShopImageWebp returns a boolean if a field has been set.

### SetShopImageWebpNil

`func (o *ItemOneOf2) SetShopImageWebpNil(b bool)`

 SetShopImageWebpNil sets the value for ShopImageWebp to be an explicit nil

### UnsetShopImageWebp
`func (o *ItemOneOf2) UnsetShopImageWebp()`

UnsetShopImageWebp ensures that no value is present for ShopImageWebp, not even an explicit nil
### GetShopVersion

`func (o *ItemOneOf2) GetShopVersion() int64`

GetShopVersion returns the ShopVersion field if non-nil, zero value otherwise.

### GetShopVersionOk

`func (o *ItemOneOf2) GetShopVersionOk() (*int64, bool)`

GetShopVersionOk returns a tuple with the ShopVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopVersion

`func (o *ItemOneOf2) SetShopVersion(v int64)`

SetShopVersion sets ShopVersion field to given value.

### HasShopVersion

`func (o *ItemOneOf2) HasShopVersion() bool`

HasShopVersion returns a boolean if a field has been set.

### SetShopVersionNil

`func (o *ItemOneOf2) SetShopVersionNil(b bool)`

 SetShopVersionNil sets the value for ShopVersion to be an explicit nil

### UnsetShopVersion
`func (o *ItemOneOf2) UnsetShopVersion()`

UnsetShopVersion ensures that no value is present for ShopVersion, not even an explicit nil
### GetShopable

`func (o *ItemOneOf2) GetShopable() bool`

GetShopable returns the Shopable field if non-nil, zero value otherwise.

### GetShopableOk

`func (o *ItemOneOf2) GetShopableOk() (*bool, bool)`

GetShopableOk returns a tuple with the Shopable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopable

`func (o *ItemOneOf2) SetShopable(v bool)`

SetShopable sets Shopable field to given value.


### GetStartTrained

`func (o *ItemOneOf2) GetStartTrained() bool`

GetStartTrained returns the StartTrained field if non-nil, zero value otherwise.

### GetStartTrainedOk

`func (o *ItemOneOf2) GetStartTrainedOk() (*bool, bool)`

GetStartTrainedOk returns a tuple with the StartTrained field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTrained

`func (o *ItemOneOf2) SetStartTrained(v bool)`

SetStartTrained sets StartTrained field to given value.

### HasStartTrained

`func (o *ItemOneOf2) HasStartTrained() bool`

HasStartTrained returns a boolean if a field has been set.

### SetStartTrainedNil

`func (o *ItemOneOf2) SetStartTrainedNil(b bool)`

 SetStartTrainedNil sets the value for StartTrained to be an explicit nil

### UnsetStartTrained
`func (o *ItemOneOf2) UnsetStartTrained()`

UnsetStartTrained ensures that no value is present for StartTrained, not even an explicit nil
### GetTooltipSections

`func (o *ItemOneOf2) GetTooltipSections() []UpgradeTooltipSection`

GetTooltipSections returns the TooltipSections field if non-nil, zero value otherwise.

### GetTooltipSectionsOk

`func (o *ItemOneOf2) GetTooltipSectionsOk() (*[]UpgradeTooltipSection, bool)`

GetTooltipSectionsOk returns a tuple with the TooltipSections field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipSections

`func (o *ItemOneOf2) SetTooltipSections(v []UpgradeTooltipSection)`

SetTooltipSections sets TooltipSections field to given value.

### HasTooltipSections

`func (o *ItemOneOf2) HasTooltipSections() bool`

HasTooltipSections returns a boolean if a field has been set.

### SetTooltipSectionsNil

`func (o *ItemOneOf2) SetTooltipSectionsNil(b bool)`

 SetTooltipSectionsNil sets the value for TooltipSections to be an explicit nil

### UnsetTooltipSections
`func (o *ItemOneOf2) UnsetTooltipSections()`

UnsetTooltipSections ensures that no value is present for TooltipSections, not even an explicit nil
### GetUpdateTime

`func (o *ItemOneOf2) GetUpdateTime() int64`

GetUpdateTime returns the UpdateTime field if non-nil, zero value otherwise.

### GetUpdateTimeOk

`func (o *ItemOneOf2) GetUpdateTimeOk() (*int64, bool)`

GetUpdateTimeOk returns a tuple with the UpdateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateTime

`func (o *ItemOneOf2) SetUpdateTime(v int64)`

SetUpdateTime sets UpdateTime field to given value.

### HasUpdateTime

`func (o *ItemOneOf2) HasUpdateTime() bool`

HasUpdateTime returns a boolean if a field has been set.

### SetUpdateTimeNil

`func (o *ItemOneOf2) SetUpdateTimeNil(b bool)`

 SetUpdateTimeNil sets the value for UpdateTime to be an explicit nil

### UnsetUpdateTime
`func (o *ItemOneOf2) UnsetUpdateTime()`

UnsetUpdateTime ensures that no value is present for UpdateTime, not even an explicit nil
### GetUpgrades

`func (o *ItemOneOf2) GetUpgrades() []RawAbilityUpgrade`

GetUpgrades returns the Upgrades field if non-nil, zero value otherwise.

### GetUpgradesOk

`func (o *ItemOneOf2) GetUpgradesOk() (*[]RawAbilityUpgrade, bool)`

GetUpgradesOk returns a tuple with the Upgrades field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpgrades

`func (o *ItemOneOf2) SetUpgrades(v []RawAbilityUpgrade)`

SetUpgrades sets Upgrades field to given value.

### HasUpgrades

`func (o *ItemOneOf2) HasUpgrades() bool`

HasUpgrades returns a boolean if a field has been set.

### SetUpgradesNil

`func (o *ItemOneOf2) SetUpgradesNil(b bool)`

 SetUpgradesNil sets the value for Upgrades to be an explicit nil

### UnsetUpgrades
`func (o *ItemOneOf2) UnsetUpgrades()`

UnsetUpgrades ensures that no value is present for Upgrades, not even an explicit nil
### GetWeaponInfo

`func (o *ItemOneOf2) GetWeaponInfo() RawItemWeaponInfoInner`

GetWeaponInfo returns the WeaponInfo field if non-nil, zero value otherwise.

### GetWeaponInfoOk

`func (o *ItemOneOf2) GetWeaponInfoOk() (*RawItemWeaponInfoInner, bool)`

GetWeaponInfoOk returns a tuple with the WeaponInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponInfo

`func (o *ItemOneOf2) SetWeaponInfo(v RawItemWeaponInfoInner)`

SetWeaponInfo sets WeaponInfo field to given value.

### HasWeaponInfo

`func (o *ItemOneOf2) HasWeaponInfo() bool`

HasWeaponInfo returns a boolean if a field has been set.

### SetWeaponInfoNil

`func (o *ItemOneOf2) SetWeaponInfoNil(b bool)`

 SetWeaponInfoNil sets the value for WeaponInfo to be an explicit nil

### UnsetWeaponInfo
`func (o *ItemOneOf2) UnsetWeaponInfo()`

UnsetWeaponInfo ensures that no value is present for WeaponInfo, not even an explicit nil
### GetType

`func (o *ItemOneOf2) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ItemOneOf2) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ItemOneOf2) SetType(v string)`

SetType sets Type field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


