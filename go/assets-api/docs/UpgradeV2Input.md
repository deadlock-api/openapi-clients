# UpgradeV2Input

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
**Properties** | Pointer to [**map[string]UpgradePropertyV2Input**](UpgradePropertyV2Input.md) |  | [optional] 
**WeaponInfo** | Pointer to [**NullableRawItemWeaponInfoV2Input**](RawItemWeaponInfoV2Input.md) |  | [optional] 
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
**TooltipSections** | Pointer to [**[]UpgradeTooltipSectionV2Input**](UpgradeTooltipSectionV2Input.md) |  | [optional] 

## Methods

### NewUpgradeV2Input

`func NewUpgradeV2Input(id int32, className string, name string, itemSlotType ItemSlotTypeV2, itemTier ItemTierV2, activation RawAbilityActivationV2, ) *UpgradeV2Input`

NewUpgradeV2Input instantiates a new UpgradeV2Input object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpgradeV2InputWithDefaults

`func NewUpgradeV2InputWithDefaults() *UpgradeV2Input`

NewUpgradeV2InputWithDefaults instantiates a new UpgradeV2Input object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *UpgradeV2Input) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *UpgradeV2Input) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *UpgradeV2Input) SetId(v int32)`

SetId sets Id field to given value.


### GetClassName

`func (o *UpgradeV2Input) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *UpgradeV2Input) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *UpgradeV2Input) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetName

`func (o *UpgradeV2Input) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *UpgradeV2Input) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *UpgradeV2Input) SetName(v string)`

SetName sets Name field to given value.


### GetStartTrained

`func (o *UpgradeV2Input) GetStartTrained() bool`

GetStartTrained returns the StartTrained field if non-nil, zero value otherwise.

### GetStartTrainedOk

`func (o *UpgradeV2Input) GetStartTrainedOk() (*bool, bool)`

GetStartTrainedOk returns a tuple with the StartTrained field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTrained

`func (o *UpgradeV2Input) SetStartTrained(v bool)`

SetStartTrained sets StartTrained field to given value.

### HasStartTrained

`func (o *UpgradeV2Input) HasStartTrained() bool`

HasStartTrained returns a boolean if a field has been set.

### SetStartTrainedNil

`func (o *UpgradeV2Input) SetStartTrainedNil(b bool)`

 SetStartTrainedNil sets the value for StartTrained to be an explicit nil

### UnsetStartTrained
`func (o *UpgradeV2Input) UnsetStartTrained()`

UnsetStartTrained ensures that no value is present for StartTrained, not even an explicit nil
### GetImage

`func (o *UpgradeV2Input) GetImage() string`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *UpgradeV2Input) GetImageOk() (*string, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *UpgradeV2Input) SetImage(v string)`

SetImage sets Image field to given value.

### HasImage

`func (o *UpgradeV2Input) HasImage() bool`

HasImage returns a boolean if a field has been set.

### SetImageNil

`func (o *UpgradeV2Input) SetImageNil(b bool)`

 SetImageNil sets the value for Image to be an explicit nil

### UnsetImage
`func (o *UpgradeV2Input) UnsetImage()`

UnsetImage ensures that no value is present for Image, not even an explicit nil
### GetImageWebp

`func (o *UpgradeV2Input) GetImageWebp() string`

GetImageWebp returns the ImageWebp field if non-nil, zero value otherwise.

### GetImageWebpOk

`func (o *UpgradeV2Input) GetImageWebpOk() (*string, bool)`

GetImageWebpOk returns a tuple with the ImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImageWebp

`func (o *UpgradeV2Input) SetImageWebp(v string)`

SetImageWebp sets ImageWebp field to given value.

### HasImageWebp

`func (o *UpgradeV2Input) HasImageWebp() bool`

HasImageWebp returns a boolean if a field has been set.

### SetImageWebpNil

`func (o *UpgradeV2Input) SetImageWebpNil(b bool)`

 SetImageWebpNil sets the value for ImageWebp to be an explicit nil

### UnsetImageWebp
`func (o *UpgradeV2Input) UnsetImageWebp()`

UnsetImageWebp ensures that no value is present for ImageWebp, not even an explicit nil
### GetHero

`func (o *UpgradeV2Input) GetHero() int32`

GetHero returns the Hero field if non-nil, zero value otherwise.

### GetHeroOk

`func (o *UpgradeV2Input) GetHeroOk() (*int32, bool)`

GetHeroOk returns a tuple with the Hero field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHero

`func (o *UpgradeV2Input) SetHero(v int32)`

SetHero sets Hero field to given value.

### HasHero

`func (o *UpgradeV2Input) HasHero() bool`

HasHero returns a boolean if a field has been set.

### SetHeroNil

`func (o *UpgradeV2Input) SetHeroNil(b bool)`

 SetHeroNil sets the value for Hero to be an explicit nil

### UnsetHero
`func (o *UpgradeV2Input) UnsetHero()`

UnsetHero ensures that no value is present for Hero, not even an explicit nil
### GetHeroes

`func (o *UpgradeV2Input) GetHeroes() []int32`

GetHeroes returns the Heroes field if non-nil, zero value otherwise.

### GetHeroesOk

`func (o *UpgradeV2Input) GetHeroesOk() (*[]int32, bool)`

GetHeroesOk returns a tuple with the Heroes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroes

`func (o *UpgradeV2Input) SetHeroes(v []int32)`

SetHeroes sets Heroes field to given value.

### HasHeroes

`func (o *UpgradeV2Input) HasHeroes() bool`

HasHeroes returns a boolean if a field has been set.

### SetHeroesNil

`func (o *UpgradeV2Input) SetHeroesNil(b bool)`

 SetHeroesNil sets the value for Heroes to be an explicit nil

### UnsetHeroes
`func (o *UpgradeV2Input) UnsetHeroes()`

UnsetHeroes ensures that no value is present for Heroes, not even an explicit nil
### GetUpdateTime

`func (o *UpgradeV2Input) GetUpdateTime() int32`

GetUpdateTime returns the UpdateTime field if non-nil, zero value otherwise.

### GetUpdateTimeOk

`func (o *UpgradeV2Input) GetUpdateTimeOk() (*int32, bool)`

GetUpdateTimeOk returns a tuple with the UpdateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateTime

`func (o *UpgradeV2Input) SetUpdateTime(v int32)`

SetUpdateTime sets UpdateTime field to given value.

### HasUpdateTime

`func (o *UpgradeV2Input) HasUpdateTime() bool`

HasUpdateTime returns a boolean if a field has been set.

### SetUpdateTimeNil

`func (o *UpgradeV2Input) SetUpdateTimeNil(b bool)`

 SetUpdateTimeNil sets the value for UpdateTime to be an explicit nil

### UnsetUpdateTime
`func (o *UpgradeV2Input) UnsetUpdateTime()`

UnsetUpdateTime ensures that no value is present for UpdateTime, not even an explicit nil
### GetProperties

`func (o *UpgradeV2Input) GetProperties() map[string]UpgradePropertyV2Input`

GetProperties returns the Properties field if non-nil, zero value otherwise.

### GetPropertiesOk

`func (o *UpgradeV2Input) GetPropertiesOk() (*map[string]UpgradePropertyV2Input, bool)`

GetPropertiesOk returns a tuple with the Properties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperties

`func (o *UpgradeV2Input) SetProperties(v map[string]UpgradePropertyV2Input)`

SetProperties sets Properties field to given value.

### HasProperties

`func (o *UpgradeV2Input) HasProperties() bool`

HasProperties returns a boolean if a field has been set.

### SetPropertiesNil

`func (o *UpgradeV2Input) SetPropertiesNil(b bool)`

 SetPropertiesNil sets the value for Properties to be an explicit nil

### UnsetProperties
`func (o *UpgradeV2Input) UnsetProperties()`

UnsetProperties ensures that no value is present for Properties, not even an explicit nil
### GetWeaponInfo

`func (o *UpgradeV2Input) GetWeaponInfo() RawItemWeaponInfoV2Input`

GetWeaponInfo returns the WeaponInfo field if non-nil, zero value otherwise.

### GetWeaponInfoOk

`func (o *UpgradeV2Input) GetWeaponInfoOk() (*RawItemWeaponInfoV2Input, bool)`

GetWeaponInfoOk returns a tuple with the WeaponInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponInfo

`func (o *UpgradeV2Input) SetWeaponInfo(v RawItemWeaponInfoV2Input)`

SetWeaponInfo sets WeaponInfo field to given value.

### HasWeaponInfo

`func (o *UpgradeV2Input) HasWeaponInfo() bool`

HasWeaponInfo returns a boolean if a field has been set.

### SetWeaponInfoNil

`func (o *UpgradeV2Input) SetWeaponInfoNil(b bool)`

 SetWeaponInfoNil sets the value for WeaponInfo to be an explicit nil

### UnsetWeaponInfo
`func (o *UpgradeV2Input) UnsetWeaponInfo()`

UnsetWeaponInfo ensures that no value is present for WeaponInfo, not even an explicit nil
### GetType

`func (o *UpgradeV2Input) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *UpgradeV2Input) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *UpgradeV2Input) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *UpgradeV2Input) HasType() bool`

HasType returns a boolean if a field has been set.

### GetShopImage

`func (o *UpgradeV2Input) GetShopImage() string`

GetShopImage returns the ShopImage field if non-nil, zero value otherwise.

### GetShopImageOk

`func (o *UpgradeV2Input) GetShopImageOk() (*string, bool)`

GetShopImageOk returns a tuple with the ShopImage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImage

`func (o *UpgradeV2Input) SetShopImage(v string)`

SetShopImage sets ShopImage field to given value.

### HasShopImage

`func (o *UpgradeV2Input) HasShopImage() bool`

HasShopImage returns a boolean if a field has been set.

### SetShopImageNil

`func (o *UpgradeV2Input) SetShopImageNil(b bool)`

 SetShopImageNil sets the value for ShopImage to be an explicit nil

### UnsetShopImage
`func (o *UpgradeV2Input) UnsetShopImage()`

UnsetShopImage ensures that no value is present for ShopImage, not even an explicit nil
### GetShopImageWebp

`func (o *UpgradeV2Input) GetShopImageWebp() string`

GetShopImageWebp returns the ShopImageWebp field if non-nil, zero value otherwise.

### GetShopImageWebpOk

`func (o *UpgradeV2Input) GetShopImageWebpOk() (*string, bool)`

GetShopImageWebpOk returns a tuple with the ShopImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageWebp

`func (o *UpgradeV2Input) SetShopImageWebp(v string)`

SetShopImageWebp sets ShopImageWebp field to given value.

### HasShopImageWebp

`func (o *UpgradeV2Input) HasShopImageWebp() bool`

HasShopImageWebp returns a boolean if a field has been set.

### SetShopImageWebpNil

`func (o *UpgradeV2Input) SetShopImageWebpNil(b bool)`

 SetShopImageWebpNil sets the value for ShopImageWebp to be an explicit nil

### UnsetShopImageWebp
`func (o *UpgradeV2Input) UnsetShopImageWebp()`

UnsetShopImageWebp ensures that no value is present for ShopImageWebp, not even an explicit nil
### GetShopImageSmall

`func (o *UpgradeV2Input) GetShopImageSmall() string`

GetShopImageSmall returns the ShopImageSmall field if non-nil, zero value otherwise.

### GetShopImageSmallOk

`func (o *UpgradeV2Input) GetShopImageSmallOk() (*string, bool)`

GetShopImageSmallOk returns a tuple with the ShopImageSmall field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageSmall

`func (o *UpgradeV2Input) SetShopImageSmall(v string)`

SetShopImageSmall sets ShopImageSmall field to given value.

### HasShopImageSmall

`func (o *UpgradeV2Input) HasShopImageSmall() bool`

HasShopImageSmall returns a boolean if a field has been set.

### SetShopImageSmallNil

`func (o *UpgradeV2Input) SetShopImageSmallNil(b bool)`

 SetShopImageSmallNil sets the value for ShopImageSmall to be an explicit nil

### UnsetShopImageSmall
`func (o *UpgradeV2Input) UnsetShopImageSmall()`

UnsetShopImageSmall ensures that no value is present for ShopImageSmall, not even an explicit nil
### GetShopImageSmallWebp

`func (o *UpgradeV2Input) GetShopImageSmallWebp() string`

GetShopImageSmallWebp returns the ShopImageSmallWebp field if non-nil, zero value otherwise.

### GetShopImageSmallWebpOk

`func (o *UpgradeV2Input) GetShopImageSmallWebpOk() (*string, bool)`

GetShopImageSmallWebpOk returns a tuple with the ShopImageSmallWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageSmallWebp

`func (o *UpgradeV2Input) SetShopImageSmallWebp(v string)`

SetShopImageSmallWebp sets ShopImageSmallWebp field to given value.

### HasShopImageSmallWebp

`func (o *UpgradeV2Input) HasShopImageSmallWebp() bool`

HasShopImageSmallWebp returns a boolean if a field has been set.

### SetShopImageSmallWebpNil

`func (o *UpgradeV2Input) SetShopImageSmallWebpNil(b bool)`

 SetShopImageSmallWebpNil sets the value for ShopImageSmallWebp to be an explicit nil

### UnsetShopImageSmallWebp
`func (o *UpgradeV2Input) UnsetShopImageSmallWebp()`

UnsetShopImageSmallWebp ensures that no value is present for ShopImageSmallWebp, not even an explicit nil
### GetItemSlotType

`func (o *UpgradeV2Input) GetItemSlotType() ItemSlotTypeV2`

GetItemSlotType returns the ItemSlotType field if non-nil, zero value otherwise.

### GetItemSlotTypeOk

`func (o *UpgradeV2Input) GetItemSlotTypeOk() (*ItemSlotTypeV2, bool)`

GetItemSlotTypeOk returns a tuple with the ItemSlotType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemSlotType

`func (o *UpgradeV2Input) SetItemSlotType(v ItemSlotTypeV2)`

SetItemSlotType sets ItemSlotType field to given value.


### GetItemTier

`func (o *UpgradeV2Input) GetItemTier() ItemTierV2`

GetItemTier returns the ItemTier field if non-nil, zero value otherwise.

### GetItemTierOk

`func (o *UpgradeV2Input) GetItemTierOk() (*ItemTierV2, bool)`

GetItemTierOk returns a tuple with the ItemTier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemTier

`func (o *UpgradeV2Input) SetItemTier(v ItemTierV2)`

SetItemTier sets ItemTier field to given value.


### GetDisabled

`func (o *UpgradeV2Input) GetDisabled() bool`

GetDisabled returns the Disabled field if non-nil, zero value otherwise.

### GetDisabledOk

`func (o *UpgradeV2Input) GetDisabledOk() (*bool, bool)`

GetDisabledOk returns a tuple with the Disabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisabled

`func (o *UpgradeV2Input) SetDisabled(v bool)`

SetDisabled sets Disabled field to given value.

### HasDisabled

`func (o *UpgradeV2Input) HasDisabled() bool`

HasDisabled returns a boolean if a field has been set.

### SetDisabledNil

`func (o *UpgradeV2Input) SetDisabledNil(b bool)`

 SetDisabledNil sets the value for Disabled to be an explicit nil

### UnsetDisabled
`func (o *UpgradeV2Input) UnsetDisabled()`

UnsetDisabled ensures that no value is present for Disabled, not even an explicit nil
### GetDescription

`func (o *UpgradeV2Input) GetDescription() UpgradeDescriptionV2`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *UpgradeV2Input) GetDescriptionOk() (*UpgradeDescriptionV2, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *UpgradeV2Input) SetDescription(v UpgradeDescriptionV2)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *UpgradeV2Input) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *UpgradeV2Input) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *UpgradeV2Input) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetActivation

`func (o *UpgradeV2Input) GetActivation() RawAbilityActivationV2`

GetActivation returns the Activation field if non-nil, zero value otherwise.

### GetActivationOk

`func (o *UpgradeV2Input) GetActivationOk() (*RawAbilityActivationV2, bool)`

GetActivationOk returns a tuple with the Activation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActivation

`func (o *UpgradeV2Input) SetActivation(v RawAbilityActivationV2)`

SetActivation sets Activation field to given value.


### GetImbue

`func (o *UpgradeV2Input) GetImbue() RawAbilityImbueV2`

GetImbue returns the Imbue field if non-nil, zero value otherwise.

### GetImbueOk

`func (o *UpgradeV2Input) GetImbueOk() (*RawAbilityImbueV2, bool)`

GetImbueOk returns a tuple with the Imbue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImbue

`func (o *UpgradeV2Input) SetImbue(v RawAbilityImbueV2)`

SetImbue sets Imbue field to given value.

### HasImbue

`func (o *UpgradeV2Input) HasImbue() bool`

HasImbue returns a boolean if a field has been set.

### SetImbueNil

`func (o *UpgradeV2Input) SetImbueNil(b bool)`

 SetImbueNil sets the value for Imbue to be an explicit nil

### UnsetImbue
`func (o *UpgradeV2Input) UnsetImbue()`

UnsetImbue ensures that no value is present for Imbue, not even an explicit nil
### GetComponentItems

`func (o *UpgradeV2Input) GetComponentItems() []string`

GetComponentItems returns the ComponentItems field if non-nil, zero value otherwise.

### GetComponentItemsOk

`func (o *UpgradeV2Input) GetComponentItemsOk() (*[]string, bool)`

GetComponentItemsOk returns a tuple with the ComponentItems field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComponentItems

`func (o *UpgradeV2Input) SetComponentItems(v []string)`

SetComponentItems sets ComponentItems field to given value.

### HasComponentItems

`func (o *UpgradeV2Input) HasComponentItems() bool`

HasComponentItems returns a boolean if a field has been set.

### SetComponentItemsNil

`func (o *UpgradeV2Input) SetComponentItemsNil(b bool)`

 SetComponentItemsNil sets the value for ComponentItems to be an explicit nil

### UnsetComponentItems
`func (o *UpgradeV2Input) UnsetComponentItems()`

UnsetComponentItems ensures that no value is present for ComponentItems, not even an explicit nil
### GetTooltipSections

`func (o *UpgradeV2Input) GetTooltipSections() []UpgradeTooltipSectionV2Input`

GetTooltipSections returns the TooltipSections field if non-nil, zero value otherwise.

### GetTooltipSectionsOk

`func (o *UpgradeV2Input) GetTooltipSectionsOk() (*[]UpgradeTooltipSectionV2Input, bool)`

GetTooltipSectionsOk returns a tuple with the TooltipSections field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipSections

`func (o *UpgradeV2Input) SetTooltipSections(v []UpgradeTooltipSectionV2Input)`

SetTooltipSections sets TooltipSections field to given value.

### HasTooltipSections

`func (o *UpgradeV2Input) HasTooltipSections() bool`

HasTooltipSections returns a boolean if a field has been set.

### SetTooltipSectionsNil

`func (o *UpgradeV2Input) SetTooltipSectionsNil(b bool)`

 SetTooltipSectionsNil sets the value for TooltipSections to be an explicit nil

### UnsetTooltipSections
`func (o *UpgradeV2Input) UnsetTooltipSections()`

UnsetTooltipSections ensures that no value is present for TooltipSections, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


