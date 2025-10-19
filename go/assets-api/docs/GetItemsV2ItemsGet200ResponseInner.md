# GetItemsV2ItemsGet200ResponseInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** |  | 
**ClassName** | **string** |  | 
**Name** | **string** |  | 
**StartTrained** | Pointer to **bool** |  | [optional] 
**Image** | Pointer to **string** |  | [optional] 
**ImageWebp** | Pointer to **string** |  | [optional] 
**Hero** | Pointer to **int32** |  | [optional] 
**Heroes** | Pointer to **[]int32** |  | [optional] 
**UpdateTime** | Pointer to **int32** |  | [optional] 
**Properties** | Pointer to [**map[string]UpgradePropertyV2Output**](UpgradePropertyV2Output.md) |  | [optional] 
**WeaponInfo** | Pointer to [**RawItemWeaponInfoV2Output**](RawItemWeaponInfoV2Output.md) |  | [optional] 
**Type** | Pointer to **string** |  | [optional] [default to "ability"]
**Behaviours** | Pointer to **[]string** |  | [optional] 
**Description** | [**UpgradeDescriptionV2**](UpgradeDescriptionV2.md) |  | 
**TooltipDetails** | Pointer to [**AbilityTooltipDetailsV2Output**](AbilityTooltipDetailsV2Output.md) |  | [optional] 
**Upgrades** | Pointer to [**[]RawAbilityUpgradeV2Output**](RawAbilityUpgradeV2Output.md) |  | [optional] 
**AbilityType** | Pointer to [**AbilityTypeV2**](AbilityTypeV2.md) |  | [optional] 
**BossDamageScale** | Pointer to **float32** |  | [optional] 
**DependantAbilities** | Pointer to **[]string** |  | [optional] 
**Videos** | Pointer to [**AbilityVideosV2**](AbilityVideosV2.md) |  | [optional] 
**ShopImage** | Pointer to **string** |  | [optional] 
**ShopImageWebp** | Pointer to **string** |  | [optional] 
**ShopImageSmall** | Pointer to **string** |  | [optional] 
**ShopImageSmallWebp** | Pointer to **string** |  | [optional] 
**ItemSlotType** | [**ItemSlotTypeV2**](ItemSlotTypeV2.md) |  | 
**ItemTier** | [**ItemTierV2**](ItemTierV2.md) |  | 
**Disabled** | Pointer to **bool** |  | [optional] 
**Activation** | [**RawAbilityActivationV2**](RawAbilityActivationV2.md) |  | 
**Imbue** | Pointer to [**RawAbilityImbueV2**](RawAbilityImbueV2.md) |  | [optional] 
**ComponentItems** | Pointer to **[]string** |  | [optional] 
**TooltipSections** | Pointer to [**[]UpgradeTooltipSectionV2Output**](UpgradeTooltipSectionV2Output.md) |  | [optional] 
**IsActiveItem** | **bool** |  | [readonly] 
**Shopable** | **bool** |  | [readonly] 
**Cost** | **int32** |  | [readonly] 

## Methods

### NewGetItemsV2ItemsGet200ResponseInner

`func NewGetItemsV2ItemsGet200ResponseInner(id int32, className string, name string, description UpgradeDescriptionV2, itemSlotType ItemSlotTypeV2, itemTier ItemTierV2, activation RawAbilityActivationV2, isActiveItem bool, shopable bool, cost int32, ) *GetItemsV2ItemsGet200ResponseInner`

NewGetItemsV2ItemsGet200ResponseInner instantiates a new GetItemsV2ItemsGet200ResponseInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetItemsV2ItemsGet200ResponseInnerWithDefaults

`func NewGetItemsV2ItemsGet200ResponseInnerWithDefaults() *GetItemsV2ItemsGet200ResponseInner`

NewGetItemsV2ItemsGet200ResponseInnerWithDefaults instantiates a new GetItemsV2ItemsGet200ResponseInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *GetItemsV2ItemsGet200ResponseInner) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *GetItemsV2ItemsGet200ResponseInner) SetId(v int32)`

SetId sets Id field to given value.


### GetClassName

`func (o *GetItemsV2ItemsGet200ResponseInner) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *GetItemsV2ItemsGet200ResponseInner) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetName

`func (o *GetItemsV2ItemsGet200ResponseInner) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *GetItemsV2ItemsGet200ResponseInner) SetName(v string)`

SetName sets Name field to given value.


### GetStartTrained

`func (o *GetItemsV2ItemsGet200ResponseInner) GetStartTrained() bool`

GetStartTrained returns the StartTrained field if non-nil, zero value otherwise.

### GetStartTrainedOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetStartTrainedOk() (*bool, bool)`

GetStartTrainedOk returns a tuple with the StartTrained field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTrained

`func (o *GetItemsV2ItemsGet200ResponseInner) SetStartTrained(v bool)`

SetStartTrained sets StartTrained field to given value.

### HasStartTrained

`func (o *GetItemsV2ItemsGet200ResponseInner) HasStartTrained() bool`

HasStartTrained returns a boolean if a field has been set.

### GetImage

`func (o *GetItemsV2ItemsGet200ResponseInner) GetImage() string`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetImageOk() (*string, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *GetItemsV2ItemsGet200ResponseInner) SetImage(v string)`

SetImage sets Image field to given value.

### HasImage

`func (o *GetItemsV2ItemsGet200ResponseInner) HasImage() bool`

HasImage returns a boolean if a field has been set.

### GetImageWebp

`func (o *GetItemsV2ItemsGet200ResponseInner) GetImageWebp() string`

GetImageWebp returns the ImageWebp field if non-nil, zero value otherwise.

### GetImageWebpOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetImageWebpOk() (*string, bool)`

GetImageWebpOk returns a tuple with the ImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImageWebp

`func (o *GetItemsV2ItemsGet200ResponseInner) SetImageWebp(v string)`

SetImageWebp sets ImageWebp field to given value.

### HasImageWebp

`func (o *GetItemsV2ItemsGet200ResponseInner) HasImageWebp() bool`

HasImageWebp returns a boolean if a field has been set.

### GetHero

`func (o *GetItemsV2ItemsGet200ResponseInner) GetHero() int32`

GetHero returns the Hero field if non-nil, zero value otherwise.

### GetHeroOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetHeroOk() (*int32, bool)`

GetHeroOk returns a tuple with the Hero field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHero

`func (o *GetItemsV2ItemsGet200ResponseInner) SetHero(v int32)`

SetHero sets Hero field to given value.

### HasHero

`func (o *GetItemsV2ItemsGet200ResponseInner) HasHero() bool`

HasHero returns a boolean if a field has been set.

### GetHeroes

`func (o *GetItemsV2ItemsGet200ResponseInner) GetHeroes() []int32`

GetHeroes returns the Heroes field if non-nil, zero value otherwise.

### GetHeroesOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetHeroesOk() (*[]int32, bool)`

GetHeroesOk returns a tuple with the Heroes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroes

`func (o *GetItemsV2ItemsGet200ResponseInner) SetHeroes(v []int32)`

SetHeroes sets Heroes field to given value.

### HasHeroes

`func (o *GetItemsV2ItemsGet200ResponseInner) HasHeroes() bool`

HasHeroes returns a boolean if a field has been set.

### GetUpdateTime

`func (o *GetItemsV2ItemsGet200ResponseInner) GetUpdateTime() int32`

GetUpdateTime returns the UpdateTime field if non-nil, zero value otherwise.

### GetUpdateTimeOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetUpdateTimeOk() (*int32, bool)`

GetUpdateTimeOk returns a tuple with the UpdateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateTime

`func (o *GetItemsV2ItemsGet200ResponseInner) SetUpdateTime(v int32)`

SetUpdateTime sets UpdateTime field to given value.

### HasUpdateTime

`func (o *GetItemsV2ItemsGet200ResponseInner) HasUpdateTime() bool`

HasUpdateTime returns a boolean if a field has been set.

### GetProperties

`func (o *GetItemsV2ItemsGet200ResponseInner) GetProperties() map[string]UpgradePropertyV2Output`

GetProperties returns the Properties field if non-nil, zero value otherwise.

### GetPropertiesOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetPropertiesOk() (*map[string]UpgradePropertyV2Output, bool)`

GetPropertiesOk returns a tuple with the Properties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperties

`func (o *GetItemsV2ItemsGet200ResponseInner) SetProperties(v map[string]UpgradePropertyV2Output)`

SetProperties sets Properties field to given value.

### HasProperties

`func (o *GetItemsV2ItemsGet200ResponseInner) HasProperties() bool`

HasProperties returns a boolean if a field has been set.

### GetWeaponInfo

`func (o *GetItemsV2ItemsGet200ResponseInner) GetWeaponInfo() RawItemWeaponInfoV2Output`

GetWeaponInfo returns the WeaponInfo field if non-nil, zero value otherwise.

### GetWeaponInfoOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetWeaponInfoOk() (*RawItemWeaponInfoV2Output, bool)`

GetWeaponInfoOk returns a tuple with the WeaponInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponInfo

`func (o *GetItemsV2ItemsGet200ResponseInner) SetWeaponInfo(v RawItemWeaponInfoV2Output)`

SetWeaponInfo sets WeaponInfo field to given value.

### HasWeaponInfo

`func (o *GetItemsV2ItemsGet200ResponseInner) HasWeaponInfo() bool`

HasWeaponInfo returns a boolean if a field has been set.

### GetType

`func (o *GetItemsV2ItemsGet200ResponseInner) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *GetItemsV2ItemsGet200ResponseInner) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *GetItemsV2ItemsGet200ResponseInner) HasType() bool`

HasType returns a boolean if a field has been set.

### GetBehaviours

`func (o *GetItemsV2ItemsGet200ResponseInner) GetBehaviours() []string`

GetBehaviours returns the Behaviours field if non-nil, zero value otherwise.

### GetBehavioursOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetBehavioursOk() (*[]string, bool)`

GetBehavioursOk returns a tuple with the Behaviours field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBehaviours

`func (o *GetItemsV2ItemsGet200ResponseInner) SetBehaviours(v []string)`

SetBehaviours sets Behaviours field to given value.

### HasBehaviours

`func (o *GetItemsV2ItemsGet200ResponseInner) HasBehaviours() bool`

HasBehaviours returns a boolean if a field has been set.

### GetDescription

`func (o *GetItemsV2ItemsGet200ResponseInner) GetDescription() UpgradeDescriptionV2`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetDescriptionOk() (*UpgradeDescriptionV2, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *GetItemsV2ItemsGet200ResponseInner) SetDescription(v UpgradeDescriptionV2)`

SetDescription sets Description field to given value.


### GetTooltipDetails

`func (o *GetItemsV2ItemsGet200ResponseInner) GetTooltipDetails() AbilityTooltipDetailsV2Output`

GetTooltipDetails returns the TooltipDetails field if non-nil, zero value otherwise.

### GetTooltipDetailsOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetTooltipDetailsOk() (*AbilityTooltipDetailsV2Output, bool)`

GetTooltipDetailsOk returns a tuple with the TooltipDetails field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipDetails

`func (o *GetItemsV2ItemsGet200ResponseInner) SetTooltipDetails(v AbilityTooltipDetailsV2Output)`

SetTooltipDetails sets TooltipDetails field to given value.

### HasTooltipDetails

`func (o *GetItemsV2ItemsGet200ResponseInner) HasTooltipDetails() bool`

HasTooltipDetails returns a boolean if a field has been set.

### GetUpgrades

`func (o *GetItemsV2ItemsGet200ResponseInner) GetUpgrades() []RawAbilityUpgradeV2Output`

GetUpgrades returns the Upgrades field if non-nil, zero value otherwise.

### GetUpgradesOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetUpgradesOk() (*[]RawAbilityUpgradeV2Output, bool)`

GetUpgradesOk returns a tuple with the Upgrades field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpgrades

`func (o *GetItemsV2ItemsGet200ResponseInner) SetUpgrades(v []RawAbilityUpgradeV2Output)`

SetUpgrades sets Upgrades field to given value.

### HasUpgrades

`func (o *GetItemsV2ItemsGet200ResponseInner) HasUpgrades() bool`

HasUpgrades returns a boolean if a field has been set.

### GetAbilityType

`func (o *GetItemsV2ItemsGet200ResponseInner) GetAbilityType() AbilityTypeV2`

GetAbilityType returns the AbilityType field if non-nil, zero value otherwise.

### GetAbilityTypeOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetAbilityTypeOk() (*AbilityTypeV2, bool)`

GetAbilityTypeOk returns a tuple with the AbilityType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAbilityType

`func (o *GetItemsV2ItemsGet200ResponseInner) SetAbilityType(v AbilityTypeV2)`

SetAbilityType sets AbilityType field to given value.

### HasAbilityType

`func (o *GetItemsV2ItemsGet200ResponseInner) HasAbilityType() bool`

HasAbilityType returns a boolean if a field has been set.

### GetBossDamageScale

`func (o *GetItemsV2ItemsGet200ResponseInner) GetBossDamageScale() float32`

GetBossDamageScale returns the BossDamageScale field if non-nil, zero value otherwise.

### GetBossDamageScaleOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetBossDamageScaleOk() (*float32, bool)`

GetBossDamageScaleOk returns a tuple with the BossDamageScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBossDamageScale

`func (o *GetItemsV2ItemsGet200ResponseInner) SetBossDamageScale(v float32)`

SetBossDamageScale sets BossDamageScale field to given value.

### HasBossDamageScale

`func (o *GetItemsV2ItemsGet200ResponseInner) HasBossDamageScale() bool`

HasBossDamageScale returns a boolean if a field has been set.

### GetDependantAbilities

`func (o *GetItemsV2ItemsGet200ResponseInner) GetDependantAbilities() []string`

GetDependantAbilities returns the DependantAbilities field if non-nil, zero value otherwise.

### GetDependantAbilitiesOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetDependantAbilitiesOk() (*[]string, bool)`

GetDependantAbilitiesOk returns a tuple with the DependantAbilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependantAbilities

`func (o *GetItemsV2ItemsGet200ResponseInner) SetDependantAbilities(v []string)`

SetDependantAbilities sets DependantAbilities field to given value.

### HasDependantAbilities

`func (o *GetItemsV2ItemsGet200ResponseInner) HasDependantAbilities() bool`

HasDependantAbilities returns a boolean if a field has been set.

### GetVideos

`func (o *GetItemsV2ItemsGet200ResponseInner) GetVideos() AbilityVideosV2`

GetVideos returns the Videos field if non-nil, zero value otherwise.

### GetVideosOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetVideosOk() (*AbilityVideosV2, bool)`

GetVideosOk returns a tuple with the Videos field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVideos

`func (o *GetItemsV2ItemsGet200ResponseInner) SetVideos(v AbilityVideosV2)`

SetVideos sets Videos field to given value.

### HasVideos

`func (o *GetItemsV2ItemsGet200ResponseInner) HasVideos() bool`

HasVideos returns a boolean if a field has been set.

### GetShopImage

`func (o *GetItemsV2ItemsGet200ResponseInner) GetShopImage() string`

GetShopImage returns the ShopImage field if non-nil, zero value otherwise.

### GetShopImageOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetShopImageOk() (*string, bool)`

GetShopImageOk returns a tuple with the ShopImage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImage

`func (o *GetItemsV2ItemsGet200ResponseInner) SetShopImage(v string)`

SetShopImage sets ShopImage field to given value.

### HasShopImage

`func (o *GetItemsV2ItemsGet200ResponseInner) HasShopImage() bool`

HasShopImage returns a boolean if a field has been set.

### GetShopImageWebp

`func (o *GetItemsV2ItemsGet200ResponseInner) GetShopImageWebp() string`

GetShopImageWebp returns the ShopImageWebp field if non-nil, zero value otherwise.

### GetShopImageWebpOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetShopImageWebpOk() (*string, bool)`

GetShopImageWebpOk returns a tuple with the ShopImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageWebp

`func (o *GetItemsV2ItemsGet200ResponseInner) SetShopImageWebp(v string)`

SetShopImageWebp sets ShopImageWebp field to given value.

### HasShopImageWebp

`func (o *GetItemsV2ItemsGet200ResponseInner) HasShopImageWebp() bool`

HasShopImageWebp returns a boolean if a field has been set.

### GetShopImageSmall

`func (o *GetItemsV2ItemsGet200ResponseInner) GetShopImageSmall() string`

GetShopImageSmall returns the ShopImageSmall field if non-nil, zero value otherwise.

### GetShopImageSmallOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetShopImageSmallOk() (*string, bool)`

GetShopImageSmallOk returns a tuple with the ShopImageSmall field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageSmall

`func (o *GetItemsV2ItemsGet200ResponseInner) SetShopImageSmall(v string)`

SetShopImageSmall sets ShopImageSmall field to given value.

### HasShopImageSmall

`func (o *GetItemsV2ItemsGet200ResponseInner) HasShopImageSmall() bool`

HasShopImageSmall returns a boolean if a field has been set.

### GetShopImageSmallWebp

`func (o *GetItemsV2ItemsGet200ResponseInner) GetShopImageSmallWebp() string`

GetShopImageSmallWebp returns the ShopImageSmallWebp field if non-nil, zero value otherwise.

### GetShopImageSmallWebpOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetShopImageSmallWebpOk() (*string, bool)`

GetShopImageSmallWebpOk returns a tuple with the ShopImageSmallWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageSmallWebp

`func (o *GetItemsV2ItemsGet200ResponseInner) SetShopImageSmallWebp(v string)`

SetShopImageSmallWebp sets ShopImageSmallWebp field to given value.

### HasShopImageSmallWebp

`func (o *GetItemsV2ItemsGet200ResponseInner) HasShopImageSmallWebp() bool`

HasShopImageSmallWebp returns a boolean if a field has been set.

### GetItemSlotType

`func (o *GetItemsV2ItemsGet200ResponseInner) GetItemSlotType() ItemSlotTypeV2`

GetItemSlotType returns the ItemSlotType field if non-nil, zero value otherwise.

### GetItemSlotTypeOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetItemSlotTypeOk() (*ItemSlotTypeV2, bool)`

GetItemSlotTypeOk returns a tuple with the ItemSlotType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemSlotType

`func (o *GetItemsV2ItemsGet200ResponseInner) SetItemSlotType(v ItemSlotTypeV2)`

SetItemSlotType sets ItemSlotType field to given value.


### GetItemTier

`func (o *GetItemsV2ItemsGet200ResponseInner) GetItemTier() ItemTierV2`

GetItemTier returns the ItemTier field if non-nil, zero value otherwise.

### GetItemTierOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetItemTierOk() (*ItemTierV2, bool)`

GetItemTierOk returns a tuple with the ItemTier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemTier

`func (o *GetItemsV2ItemsGet200ResponseInner) SetItemTier(v ItemTierV2)`

SetItemTier sets ItemTier field to given value.


### GetDisabled

`func (o *GetItemsV2ItemsGet200ResponseInner) GetDisabled() bool`

GetDisabled returns the Disabled field if non-nil, zero value otherwise.

### GetDisabledOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetDisabledOk() (*bool, bool)`

GetDisabledOk returns a tuple with the Disabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisabled

`func (o *GetItemsV2ItemsGet200ResponseInner) SetDisabled(v bool)`

SetDisabled sets Disabled field to given value.

### HasDisabled

`func (o *GetItemsV2ItemsGet200ResponseInner) HasDisabled() bool`

HasDisabled returns a boolean if a field has been set.

### GetActivation

`func (o *GetItemsV2ItemsGet200ResponseInner) GetActivation() RawAbilityActivationV2`

GetActivation returns the Activation field if non-nil, zero value otherwise.

### GetActivationOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetActivationOk() (*RawAbilityActivationV2, bool)`

GetActivationOk returns a tuple with the Activation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActivation

`func (o *GetItemsV2ItemsGet200ResponseInner) SetActivation(v RawAbilityActivationV2)`

SetActivation sets Activation field to given value.


### GetImbue

`func (o *GetItemsV2ItemsGet200ResponseInner) GetImbue() RawAbilityImbueV2`

GetImbue returns the Imbue field if non-nil, zero value otherwise.

### GetImbueOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetImbueOk() (*RawAbilityImbueV2, bool)`

GetImbueOk returns a tuple with the Imbue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImbue

`func (o *GetItemsV2ItemsGet200ResponseInner) SetImbue(v RawAbilityImbueV2)`

SetImbue sets Imbue field to given value.

### HasImbue

`func (o *GetItemsV2ItemsGet200ResponseInner) HasImbue() bool`

HasImbue returns a boolean if a field has been set.

### GetComponentItems

`func (o *GetItemsV2ItemsGet200ResponseInner) GetComponentItems() []string`

GetComponentItems returns the ComponentItems field if non-nil, zero value otherwise.

### GetComponentItemsOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetComponentItemsOk() (*[]string, bool)`

GetComponentItemsOk returns a tuple with the ComponentItems field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComponentItems

`func (o *GetItemsV2ItemsGet200ResponseInner) SetComponentItems(v []string)`

SetComponentItems sets ComponentItems field to given value.

### HasComponentItems

`func (o *GetItemsV2ItemsGet200ResponseInner) HasComponentItems() bool`

HasComponentItems returns a boolean if a field has been set.

### GetTooltipSections

`func (o *GetItemsV2ItemsGet200ResponseInner) GetTooltipSections() []UpgradeTooltipSectionV2Output`

GetTooltipSections returns the TooltipSections field if non-nil, zero value otherwise.

### GetTooltipSectionsOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetTooltipSectionsOk() (*[]UpgradeTooltipSectionV2Output, bool)`

GetTooltipSectionsOk returns a tuple with the TooltipSections field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipSections

`func (o *GetItemsV2ItemsGet200ResponseInner) SetTooltipSections(v []UpgradeTooltipSectionV2Output)`

SetTooltipSections sets TooltipSections field to given value.

### HasTooltipSections

`func (o *GetItemsV2ItemsGet200ResponseInner) HasTooltipSections() bool`

HasTooltipSections returns a boolean if a field has been set.

### GetIsActiveItem

`func (o *GetItemsV2ItemsGet200ResponseInner) GetIsActiveItem() bool`

GetIsActiveItem returns the IsActiveItem field if non-nil, zero value otherwise.

### GetIsActiveItemOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetIsActiveItemOk() (*bool, bool)`

GetIsActiveItemOk returns a tuple with the IsActiveItem field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsActiveItem

`func (o *GetItemsV2ItemsGet200ResponseInner) SetIsActiveItem(v bool)`

SetIsActiveItem sets IsActiveItem field to given value.


### GetShopable

`func (o *GetItemsV2ItemsGet200ResponseInner) GetShopable() bool`

GetShopable returns the Shopable field if non-nil, zero value otherwise.

### GetShopableOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetShopableOk() (*bool, bool)`

GetShopableOk returns a tuple with the Shopable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopable

`func (o *GetItemsV2ItemsGet200ResponseInner) SetShopable(v bool)`

SetShopable sets Shopable field to given value.


### GetCost

`func (o *GetItemsV2ItemsGet200ResponseInner) GetCost() int32`

GetCost returns the Cost field if non-nil, zero value otherwise.

### GetCostOk

`func (o *GetItemsV2ItemsGet200ResponseInner) GetCostOk() (*int32, bool)`

GetCostOk returns a tuple with the Cost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCost

`func (o *GetItemsV2ItemsGet200ResponseInner) SetCost(v int32)`

SetCost sets Cost field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


