# Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AbilityType** | Pointer to [**AbilityType**](AbilityType.md) |  | [optional] 
**Behaviours** | Pointer to **[]string** |  | [optional] 
**BossDamageScale** | Pointer to **float64** |  | [optional] 
**ClassName** | **string** |  | 
**DependantAbilities** | Pointer to **[]string** |  | [optional] 
**DependentAbilities** | Pointer to [**map[string]DependantAbilities**](DependantAbilities.md) |  | [optional] 
**Description** | [**UpgradeDescription**](UpgradeDescription.md) |  | 
**GrantAmmoOnCast** | Pointer to **bool** |  | [optional] 
**Hero** | Pointer to **int32** |  | [optional] 
**Heroes** | Pointer to **[]int32** |  | [optional] 
**Id** | **int32** |  | 
**Image** | Pointer to **string** |  | [optional] 
**ImageWebp** | Pointer to **string** |  | [optional] 
**Name** | **string** |  | 
**Properties** | Pointer to [**map[string]UpgradeProperty**](UpgradeProperty.md) |  | [optional] 
**StartTrained** | Pointer to **bool** |  | [optional] 
**TooltipDetails** | Pointer to [**AbilityTooltipDetails**](AbilityTooltipDetails.md) |  | [optional] 
**Type** | [**ItemType**](ItemType.md) |  | 
**UpdateTime** | Pointer to **int64** |  | [optional] 
**Upgrades** | Pointer to [**[]RawAbilityUpgrade**](RawAbilityUpgrade.md) |  | [optional] 
**Videos** | Pointer to [**AbilityVideos**](AbilityVideos.md) |  | [optional] 
**WeaponInfo** | Pointer to [**RawItemWeaponInfoInner**](RawItemWeaponInfoInner.md) |  | [optional] 
**CrosshairCssClass** | Pointer to **string** |  | [optional] 
**CustomCrosshairSettings** | Pointer to [**RawCustomCrosshairSettings**](RawCustomCrosshairSettings.md) |  | [optional] 
**UseCustomCrosshairSettings** | Pointer to **bool** |  | [optional] 
**Activation** | [**AbilityActivation**](AbilityActivation.md) |  | 
**ComponentItems** | Pointer to **[]string** |  | [optional] 
**Cost** | Pointer to **int32** |  | [optional] 
**Disabled** | Pointer to **bool** |  | [optional] 
**Imbue** | Pointer to [**AbilityImbue**](AbilityImbue.md) |  | [optional] 
**IsActiveItem** | **bool** |  | 
**ItemSlotType** | [**ItemSlotType**](ItemSlotType.md) |  | 
**ItemTier** | **int32** |  | 
**ShopImage** | Pointer to **string** |  | [optional] 
**ShopImageSmall** | Pointer to **string** |  | [optional] 
**ShopImageSmallWebp** | Pointer to **string** |  | [optional] 
**ShopImageWebp** | Pointer to **string** |  | [optional] 
**Shopable** | **bool** |  | 
**TooltipSections** | Pointer to [**[]UpgradeTooltipSection**](UpgradeTooltipSection.md) |  | [optional] 

## Methods

### NewItem

`func NewItem(className string, description UpgradeDescription, id int32, name string, type_ ItemType, activation AbilityActivation, isActiveItem bool, itemSlotType ItemSlotType, itemTier int32, shopable bool, ) *Item`

NewItem instantiates a new Item object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewItemWithDefaults

`func NewItemWithDefaults() *Item`

NewItemWithDefaults instantiates a new Item object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAbilityType

`func (o *Item) GetAbilityType() AbilityType`

GetAbilityType returns the AbilityType field if non-nil, zero value otherwise.

### GetAbilityTypeOk

`func (o *Item) GetAbilityTypeOk() (*AbilityType, bool)`

GetAbilityTypeOk returns a tuple with the AbilityType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAbilityType

`func (o *Item) SetAbilityType(v AbilityType)`

SetAbilityType sets AbilityType field to given value.

### HasAbilityType

`func (o *Item) HasAbilityType() bool`

HasAbilityType returns a boolean if a field has been set.

### GetBehaviours

`func (o *Item) GetBehaviours() []string`

GetBehaviours returns the Behaviours field if non-nil, zero value otherwise.

### GetBehavioursOk

`func (o *Item) GetBehavioursOk() (*[]string, bool)`

GetBehavioursOk returns a tuple with the Behaviours field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBehaviours

`func (o *Item) SetBehaviours(v []string)`

SetBehaviours sets Behaviours field to given value.

### HasBehaviours

`func (o *Item) HasBehaviours() bool`

HasBehaviours returns a boolean if a field has been set.

### GetBossDamageScale

`func (o *Item) GetBossDamageScale() float64`

GetBossDamageScale returns the BossDamageScale field if non-nil, zero value otherwise.

### GetBossDamageScaleOk

`func (o *Item) GetBossDamageScaleOk() (*float64, bool)`

GetBossDamageScaleOk returns a tuple with the BossDamageScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBossDamageScale

`func (o *Item) SetBossDamageScale(v float64)`

SetBossDamageScale sets BossDamageScale field to given value.

### HasBossDamageScale

`func (o *Item) HasBossDamageScale() bool`

HasBossDamageScale returns a boolean if a field has been set.

### GetClassName

`func (o *Item) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *Item) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *Item) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetDependantAbilities

`func (o *Item) GetDependantAbilities() []string`

GetDependantAbilities returns the DependantAbilities field if non-nil, zero value otherwise.

### GetDependantAbilitiesOk

`func (o *Item) GetDependantAbilitiesOk() (*[]string, bool)`

GetDependantAbilitiesOk returns a tuple with the DependantAbilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependantAbilities

`func (o *Item) SetDependantAbilities(v []string)`

SetDependantAbilities sets DependantAbilities field to given value.

### HasDependantAbilities

`func (o *Item) HasDependantAbilities() bool`

HasDependantAbilities returns a boolean if a field has been set.

### GetDependentAbilities

`func (o *Item) GetDependentAbilities() map[string]DependantAbilities`

GetDependentAbilities returns the DependentAbilities field if non-nil, zero value otherwise.

### GetDependentAbilitiesOk

`func (o *Item) GetDependentAbilitiesOk() (*map[string]DependantAbilities, bool)`

GetDependentAbilitiesOk returns a tuple with the DependentAbilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependentAbilities

`func (o *Item) SetDependentAbilities(v map[string]DependantAbilities)`

SetDependentAbilities sets DependentAbilities field to given value.

### HasDependentAbilities

`func (o *Item) HasDependentAbilities() bool`

HasDependentAbilities returns a boolean if a field has been set.

### GetDescription

`func (o *Item) GetDescription() UpgradeDescription`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Item) GetDescriptionOk() (*UpgradeDescription, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Item) SetDescription(v UpgradeDescription)`

SetDescription sets Description field to given value.


### GetGrantAmmoOnCast

`func (o *Item) GetGrantAmmoOnCast() bool`

GetGrantAmmoOnCast returns the GrantAmmoOnCast field if non-nil, zero value otherwise.

### GetGrantAmmoOnCastOk

`func (o *Item) GetGrantAmmoOnCastOk() (*bool, bool)`

GetGrantAmmoOnCastOk returns a tuple with the GrantAmmoOnCast field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGrantAmmoOnCast

`func (o *Item) SetGrantAmmoOnCast(v bool)`

SetGrantAmmoOnCast sets GrantAmmoOnCast field to given value.

### HasGrantAmmoOnCast

`func (o *Item) HasGrantAmmoOnCast() bool`

HasGrantAmmoOnCast returns a boolean if a field has been set.

### GetHero

`func (o *Item) GetHero() int32`

GetHero returns the Hero field if non-nil, zero value otherwise.

### GetHeroOk

`func (o *Item) GetHeroOk() (*int32, bool)`

GetHeroOk returns a tuple with the Hero field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHero

`func (o *Item) SetHero(v int32)`

SetHero sets Hero field to given value.

### HasHero

`func (o *Item) HasHero() bool`

HasHero returns a boolean if a field has been set.

### GetHeroes

`func (o *Item) GetHeroes() []int32`

GetHeroes returns the Heroes field if non-nil, zero value otherwise.

### GetHeroesOk

`func (o *Item) GetHeroesOk() (*[]int32, bool)`

GetHeroesOk returns a tuple with the Heroes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroes

`func (o *Item) SetHeroes(v []int32)`

SetHeroes sets Heroes field to given value.

### HasHeroes

`func (o *Item) HasHeroes() bool`

HasHeroes returns a boolean if a field has been set.

### GetId

`func (o *Item) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Item) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Item) SetId(v int32)`

SetId sets Id field to given value.


### GetImage

`func (o *Item) GetImage() string`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *Item) GetImageOk() (*string, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *Item) SetImage(v string)`

SetImage sets Image field to given value.

### HasImage

`func (o *Item) HasImage() bool`

HasImage returns a boolean if a field has been set.

### GetImageWebp

`func (o *Item) GetImageWebp() string`

GetImageWebp returns the ImageWebp field if non-nil, zero value otherwise.

### GetImageWebpOk

`func (o *Item) GetImageWebpOk() (*string, bool)`

GetImageWebpOk returns a tuple with the ImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImageWebp

`func (o *Item) SetImageWebp(v string)`

SetImageWebp sets ImageWebp field to given value.

### HasImageWebp

`func (o *Item) HasImageWebp() bool`

HasImageWebp returns a boolean if a field has been set.

### GetName

`func (o *Item) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Item) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Item) SetName(v string)`

SetName sets Name field to given value.


### GetProperties

`func (o *Item) GetProperties() map[string]UpgradeProperty`

GetProperties returns the Properties field if non-nil, zero value otherwise.

### GetPropertiesOk

`func (o *Item) GetPropertiesOk() (*map[string]UpgradeProperty, bool)`

GetPropertiesOk returns a tuple with the Properties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperties

`func (o *Item) SetProperties(v map[string]UpgradeProperty)`

SetProperties sets Properties field to given value.

### HasProperties

`func (o *Item) HasProperties() bool`

HasProperties returns a boolean if a field has been set.

### GetStartTrained

`func (o *Item) GetStartTrained() bool`

GetStartTrained returns the StartTrained field if non-nil, zero value otherwise.

### GetStartTrainedOk

`func (o *Item) GetStartTrainedOk() (*bool, bool)`

GetStartTrainedOk returns a tuple with the StartTrained field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTrained

`func (o *Item) SetStartTrained(v bool)`

SetStartTrained sets StartTrained field to given value.

### HasStartTrained

`func (o *Item) HasStartTrained() bool`

HasStartTrained returns a boolean if a field has been set.

### GetTooltipDetails

`func (o *Item) GetTooltipDetails() AbilityTooltipDetails`

GetTooltipDetails returns the TooltipDetails field if non-nil, zero value otherwise.

### GetTooltipDetailsOk

`func (o *Item) GetTooltipDetailsOk() (*AbilityTooltipDetails, bool)`

GetTooltipDetailsOk returns a tuple with the TooltipDetails field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipDetails

`func (o *Item) SetTooltipDetails(v AbilityTooltipDetails)`

SetTooltipDetails sets TooltipDetails field to given value.

### HasTooltipDetails

`func (o *Item) HasTooltipDetails() bool`

HasTooltipDetails returns a boolean if a field has been set.

### GetType

`func (o *Item) GetType() ItemType`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Item) GetTypeOk() (*ItemType, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Item) SetType(v ItemType)`

SetType sets Type field to given value.


### GetUpdateTime

`func (o *Item) GetUpdateTime() int64`

GetUpdateTime returns the UpdateTime field if non-nil, zero value otherwise.

### GetUpdateTimeOk

`func (o *Item) GetUpdateTimeOk() (*int64, bool)`

GetUpdateTimeOk returns a tuple with the UpdateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateTime

`func (o *Item) SetUpdateTime(v int64)`

SetUpdateTime sets UpdateTime field to given value.

### HasUpdateTime

`func (o *Item) HasUpdateTime() bool`

HasUpdateTime returns a boolean if a field has been set.

### GetUpgrades

`func (o *Item) GetUpgrades() []RawAbilityUpgrade`

GetUpgrades returns the Upgrades field if non-nil, zero value otherwise.

### GetUpgradesOk

`func (o *Item) GetUpgradesOk() (*[]RawAbilityUpgrade, bool)`

GetUpgradesOk returns a tuple with the Upgrades field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpgrades

`func (o *Item) SetUpgrades(v []RawAbilityUpgrade)`

SetUpgrades sets Upgrades field to given value.

### HasUpgrades

`func (o *Item) HasUpgrades() bool`

HasUpgrades returns a boolean if a field has been set.

### GetVideos

`func (o *Item) GetVideos() AbilityVideos`

GetVideos returns the Videos field if non-nil, zero value otherwise.

### GetVideosOk

`func (o *Item) GetVideosOk() (*AbilityVideos, bool)`

GetVideosOk returns a tuple with the Videos field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVideos

`func (o *Item) SetVideos(v AbilityVideos)`

SetVideos sets Videos field to given value.

### HasVideos

`func (o *Item) HasVideos() bool`

HasVideos returns a boolean if a field has been set.

### GetWeaponInfo

`func (o *Item) GetWeaponInfo() RawItemWeaponInfoInner`

GetWeaponInfo returns the WeaponInfo field if non-nil, zero value otherwise.

### GetWeaponInfoOk

`func (o *Item) GetWeaponInfoOk() (*RawItemWeaponInfoInner, bool)`

GetWeaponInfoOk returns a tuple with the WeaponInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponInfo

`func (o *Item) SetWeaponInfo(v RawItemWeaponInfoInner)`

SetWeaponInfo sets WeaponInfo field to given value.

### HasWeaponInfo

`func (o *Item) HasWeaponInfo() bool`

HasWeaponInfo returns a boolean if a field has been set.

### GetCrosshairCssClass

`func (o *Item) GetCrosshairCssClass() string`

GetCrosshairCssClass returns the CrosshairCssClass field if non-nil, zero value otherwise.

### GetCrosshairCssClassOk

`func (o *Item) GetCrosshairCssClassOk() (*string, bool)`

GetCrosshairCssClassOk returns a tuple with the CrosshairCssClass field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrosshairCssClass

`func (o *Item) SetCrosshairCssClass(v string)`

SetCrosshairCssClass sets CrosshairCssClass field to given value.

### HasCrosshairCssClass

`func (o *Item) HasCrosshairCssClass() bool`

HasCrosshairCssClass returns a boolean if a field has been set.

### GetCustomCrosshairSettings

`func (o *Item) GetCustomCrosshairSettings() RawCustomCrosshairSettings`

GetCustomCrosshairSettings returns the CustomCrosshairSettings field if non-nil, zero value otherwise.

### GetCustomCrosshairSettingsOk

`func (o *Item) GetCustomCrosshairSettingsOk() (*RawCustomCrosshairSettings, bool)`

GetCustomCrosshairSettingsOk returns a tuple with the CustomCrosshairSettings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomCrosshairSettings

`func (o *Item) SetCustomCrosshairSettings(v RawCustomCrosshairSettings)`

SetCustomCrosshairSettings sets CustomCrosshairSettings field to given value.

### HasCustomCrosshairSettings

`func (o *Item) HasCustomCrosshairSettings() bool`

HasCustomCrosshairSettings returns a boolean if a field has been set.

### GetUseCustomCrosshairSettings

`func (o *Item) GetUseCustomCrosshairSettings() bool`

GetUseCustomCrosshairSettings returns the UseCustomCrosshairSettings field if non-nil, zero value otherwise.

### GetUseCustomCrosshairSettingsOk

`func (o *Item) GetUseCustomCrosshairSettingsOk() (*bool, bool)`

GetUseCustomCrosshairSettingsOk returns a tuple with the UseCustomCrosshairSettings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUseCustomCrosshairSettings

`func (o *Item) SetUseCustomCrosshairSettings(v bool)`

SetUseCustomCrosshairSettings sets UseCustomCrosshairSettings field to given value.

### HasUseCustomCrosshairSettings

`func (o *Item) HasUseCustomCrosshairSettings() bool`

HasUseCustomCrosshairSettings returns a boolean if a field has been set.

### GetActivation

`func (o *Item) GetActivation() AbilityActivation`

GetActivation returns the Activation field if non-nil, zero value otherwise.

### GetActivationOk

`func (o *Item) GetActivationOk() (*AbilityActivation, bool)`

GetActivationOk returns a tuple with the Activation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActivation

`func (o *Item) SetActivation(v AbilityActivation)`

SetActivation sets Activation field to given value.


### GetComponentItems

`func (o *Item) GetComponentItems() []string`

GetComponentItems returns the ComponentItems field if non-nil, zero value otherwise.

### GetComponentItemsOk

`func (o *Item) GetComponentItemsOk() (*[]string, bool)`

GetComponentItemsOk returns a tuple with the ComponentItems field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComponentItems

`func (o *Item) SetComponentItems(v []string)`

SetComponentItems sets ComponentItems field to given value.

### HasComponentItems

`func (o *Item) HasComponentItems() bool`

HasComponentItems returns a boolean if a field has been set.

### GetCost

`func (o *Item) GetCost() int32`

GetCost returns the Cost field if non-nil, zero value otherwise.

### GetCostOk

`func (o *Item) GetCostOk() (*int32, bool)`

GetCostOk returns a tuple with the Cost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCost

`func (o *Item) SetCost(v int32)`

SetCost sets Cost field to given value.

### HasCost

`func (o *Item) HasCost() bool`

HasCost returns a boolean if a field has been set.

### GetDisabled

`func (o *Item) GetDisabled() bool`

GetDisabled returns the Disabled field if non-nil, zero value otherwise.

### GetDisabledOk

`func (o *Item) GetDisabledOk() (*bool, bool)`

GetDisabledOk returns a tuple with the Disabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisabled

`func (o *Item) SetDisabled(v bool)`

SetDisabled sets Disabled field to given value.

### HasDisabled

`func (o *Item) HasDisabled() bool`

HasDisabled returns a boolean if a field has been set.

### GetImbue

`func (o *Item) GetImbue() AbilityImbue`

GetImbue returns the Imbue field if non-nil, zero value otherwise.

### GetImbueOk

`func (o *Item) GetImbueOk() (*AbilityImbue, bool)`

GetImbueOk returns a tuple with the Imbue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImbue

`func (o *Item) SetImbue(v AbilityImbue)`

SetImbue sets Imbue field to given value.

### HasImbue

`func (o *Item) HasImbue() bool`

HasImbue returns a boolean if a field has been set.

### GetIsActiveItem

`func (o *Item) GetIsActiveItem() bool`

GetIsActiveItem returns the IsActiveItem field if non-nil, zero value otherwise.

### GetIsActiveItemOk

`func (o *Item) GetIsActiveItemOk() (*bool, bool)`

GetIsActiveItemOk returns a tuple with the IsActiveItem field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsActiveItem

`func (o *Item) SetIsActiveItem(v bool)`

SetIsActiveItem sets IsActiveItem field to given value.


### GetItemSlotType

`func (o *Item) GetItemSlotType() ItemSlotType`

GetItemSlotType returns the ItemSlotType field if non-nil, zero value otherwise.

### GetItemSlotTypeOk

`func (o *Item) GetItemSlotTypeOk() (*ItemSlotType, bool)`

GetItemSlotTypeOk returns a tuple with the ItemSlotType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemSlotType

`func (o *Item) SetItemSlotType(v ItemSlotType)`

SetItemSlotType sets ItemSlotType field to given value.


### GetItemTier

`func (o *Item) GetItemTier() int32`

GetItemTier returns the ItemTier field if non-nil, zero value otherwise.

### GetItemTierOk

`func (o *Item) GetItemTierOk() (*int32, bool)`

GetItemTierOk returns a tuple with the ItemTier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemTier

`func (o *Item) SetItemTier(v int32)`

SetItemTier sets ItemTier field to given value.


### GetShopImage

`func (o *Item) GetShopImage() string`

GetShopImage returns the ShopImage field if non-nil, zero value otherwise.

### GetShopImageOk

`func (o *Item) GetShopImageOk() (*string, bool)`

GetShopImageOk returns a tuple with the ShopImage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImage

`func (o *Item) SetShopImage(v string)`

SetShopImage sets ShopImage field to given value.

### HasShopImage

`func (o *Item) HasShopImage() bool`

HasShopImage returns a boolean if a field has been set.

### GetShopImageSmall

`func (o *Item) GetShopImageSmall() string`

GetShopImageSmall returns the ShopImageSmall field if non-nil, zero value otherwise.

### GetShopImageSmallOk

`func (o *Item) GetShopImageSmallOk() (*string, bool)`

GetShopImageSmallOk returns a tuple with the ShopImageSmall field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageSmall

`func (o *Item) SetShopImageSmall(v string)`

SetShopImageSmall sets ShopImageSmall field to given value.

### HasShopImageSmall

`func (o *Item) HasShopImageSmall() bool`

HasShopImageSmall returns a boolean if a field has been set.

### GetShopImageSmallWebp

`func (o *Item) GetShopImageSmallWebp() string`

GetShopImageSmallWebp returns the ShopImageSmallWebp field if non-nil, zero value otherwise.

### GetShopImageSmallWebpOk

`func (o *Item) GetShopImageSmallWebpOk() (*string, bool)`

GetShopImageSmallWebpOk returns a tuple with the ShopImageSmallWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageSmallWebp

`func (o *Item) SetShopImageSmallWebp(v string)`

SetShopImageSmallWebp sets ShopImageSmallWebp field to given value.

### HasShopImageSmallWebp

`func (o *Item) HasShopImageSmallWebp() bool`

HasShopImageSmallWebp returns a boolean if a field has been set.

### GetShopImageWebp

`func (o *Item) GetShopImageWebp() string`

GetShopImageWebp returns the ShopImageWebp field if non-nil, zero value otherwise.

### GetShopImageWebpOk

`func (o *Item) GetShopImageWebpOk() (*string, bool)`

GetShopImageWebpOk returns a tuple with the ShopImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageWebp

`func (o *Item) SetShopImageWebp(v string)`

SetShopImageWebp sets ShopImageWebp field to given value.

### HasShopImageWebp

`func (o *Item) HasShopImageWebp() bool`

HasShopImageWebp returns a boolean if a field has been set.

### GetShopable

`func (o *Item) GetShopable() bool`

GetShopable returns the Shopable field if non-nil, zero value otherwise.

### GetShopableOk

`func (o *Item) GetShopableOk() (*bool, bool)`

GetShopableOk returns a tuple with the Shopable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopable

`func (o *Item) SetShopable(v bool)`

SetShopable sets Shopable field to given value.


### GetTooltipSections

`func (o *Item) GetTooltipSections() []UpgradeTooltipSection`

GetTooltipSections returns the TooltipSections field if non-nil, zero value otherwise.

### GetTooltipSectionsOk

`func (o *Item) GetTooltipSectionsOk() (*[]UpgradeTooltipSection, bool)`

GetTooltipSectionsOk returns a tuple with the TooltipSections field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipSections

`func (o *Item) SetTooltipSections(v []UpgradeTooltipSection)`

SetTooltipSections sets TooltipSections field to given value.

### HasTooltipSections

`func (o *Item) HasTooltipSections() bool`

HasTooltipSections returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


