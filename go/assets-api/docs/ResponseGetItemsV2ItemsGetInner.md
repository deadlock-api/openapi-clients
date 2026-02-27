# ResponseGetItemsV2ItemsGetInner

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
**Properties** | Pointer to [**map[string]UpgradePropertyV2**](UpgradePropertyV2.md) |  | [optional] 
**WeaponInfo** | Pointer to [**RawItemWeaponInfoV2**](RawItemWeaponInfoV2.md) |  | [optional] 
**Type** | Pointer to **string** |  | [optional] [default to "ability"]
**GrantAmmoOnCast** | Pointer to **bool** |  | [optional] 
**Behaviours** | Pointer to **[]string** |  | [optional] 
**Description** | [**UpgradeDescriptionV2**](UpgradeDescriptionV2.md) |  | 
**TooltipDetails** | Pointer to [**AbilityTooltipDetailsV2**](AbilityTooltipDetailsV2.md) |  | [optional] 
**Upgrades** | Pointer to [**[]RawAbilityUpgradeV2**](RawAbilityUpgradeV2.md) |  | [optional] 
**AbilityType** | Pointer to [**AbilityTypeV2**](AbilityTypeV2.md) |  | [optional] 
**BossDamageScale** | Pointer to **float32** |  | [optional] 
**DependantAbilities** | Pointer to **[]string** |  | [optional] 
**Videos** | Pointer to [**AbilityVideosV2**](AbilityVideosV2.md) |  | [optional] 
**DependentAbilities** | Pointer to [**map[string]DependantAbilities**](DependantAbilities.md) |  | [optional] 
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
**TooltipSections** | Pointer to [**[]UpgradeTooltipSectionV2**](UpgradeTooltipSectionV2.md) |  | [optional] 
**IsActiveItem** | **bool** |  | [readonly] 
**Shopable** | **bool** |  | [readonly] 
**Cost** | **int32** |  | [readonly] 

## Methods

### NewResponseGetItemsV2ItemsGetInner

`func NewResponseGetItemsV2ItemsGetInner(id int32, className string, name string, description UpgradeDescriptionV2, itemSlotType ItemSlotTypeV2, itemTier ItemTierV2, activation RawAbilityActivationV2, isActiveItem bool, shopable bool, cost int32, ) *ResponseGetItemsV2ItemsGetInner`

NewResponseGetItemsV2ItemsGetInner instantiates a new ResponseGetItemsV2ItemsGetInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewResponseGetItemsV2ItemsGetInnerWithDefaults

`func NewResponseGetItemsV2ItemsGetInnerWithDefaults() *ResponseGetItemsV2ItemsGetInner`

NewResponseGetItemsV2ItemsGetInnerWithDefaults instantiates a new ResponseGetItemsV2ItemsGetInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ResponseGetItemsV2ItemsGetInner) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ResponseGetItemsV2ItemsGetInner) SetId(v int32)`

SetId sets Id field to given value.


### GetClassName

`func (o *ResponseGetItemsV2ItemsGetInner) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *ResponseGetItemsV2ItemsGetInner) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetName

`func (o *ResponseGetItemsV2ItemsGetInner) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ResponseGetItemsV2ItemsGetInner) SetName(v string)`

SetName sets Name field to given value.


### GetStartTrained

`func (o *ResponseGetItemsV2ItemsGetInner) GetStartTrained() bool`

GetStartTrained returns the StartTrained field if non-nil, zero value otherwise.

### GetStartTrainedOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetStartTrainedOk() (*bool, bool)`

GetStartTrainedOk returns a tuple with the StartTrained field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTrained

`func (o *ResponseGetItemsV2ItemsGetInner) SetStartTrained(v bool)`

SetStartTrained sets StartTrained field to given value.

### HasStartTrained

`func (o *ResponseGetItemsV2ItemsGetInner) HasStartTrained() bool`

HasStartTrained returns a boolean if a field has been set.

### GetImage

`func (o *ResponseGetItemsV2ItemsGetInner) GetImage() string`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetImageOk() (*string, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *ResponseGetItemsV2ItemsGetInner) SetImage(v string)`

SetImage sets Image field to given value.

### HasImage

`func (o *ResponseGetItemsV2ItemsGetInner) HasImage() bool`

HasImage returns a boolean if a field has been set.

### GetImageWebp

`func (o *ResponseGetItemsV2ItemsGetInner) GetImageWebp() string`

GetImageWebp returns the ImageWebp field if non-nil, zero value otherwise.

### GetImageWebpOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetImageWebpOk() (*string, bool)`

GetImageWebpOk returns a tuple with the ImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImageWebp

`func (o *ResponseGetItemsV2ItemsGetInner) SetImageWebp(v string)`

SetImageWebp sets ImageWebp field to given value.

### HasImageWebp

`func (o *ResponseGetItemsV2ItemsGetInner) HasImageWebp() bool`

HasImageWebp returns a boolean if a field has been set.

### GetHero

`func (o *ResponseGetItemsV2ItemsGetInner) GetHero() int32`

GetHero returns the Hero field if non-nil, zero value otherwise.

### GetHeroOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetHeroOk() (*int32, bool)`

GetHeroOk returns a tuple with the Hero field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHero

`func (o *ResponseGetItemsV2ItemsGetInner) SetHero(v int32)`

SetHero sets Hero field to given value.

### HasHero

`func (o *ResponseGetItemsV2ItemsGetInner) HasHero() bool`

HasHero returns a boolean if a field has been set.

### GetHeroes

`func (o *ResponseGetItemsV2ItemsGetInner) GetHeroes() []int32`

GetHeroes returns the Heroes field if non-nil, zero value otherwise.

### GetHeroesOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetHeroesOk() (*[]int32, bool)`

GetHeroesOk returns a tuple with the Heroes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroes

`func (o *ResponseGetItemsV2ItemsGetInner) SetHeroes(v []int32)`

SetHeroes sets Heroes field to given value.

### HasHeroes

`func (o *ResponseGetItemsV2ItemsGetInner) HasHeroes() bool`

HasHeroes returns a boolean if a field has been set.

### GetUpdateTime

`func (o *ResponseGetItemsV2ItemsGetInner) GetUpdateTime() int32`

GetUpdateTime returns the UpdateTime field if non-nil, zero value otherwise.

### GetUpdateTimeOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetUpdateTimeOk() (*int32, bool)`

GetUpdateTimeOk returns a tuple with the UpdateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateTime

`func (o *ResponseGetItemsV2ItemsGetInner) SetUpdateTime(v int32)`

SetUpdateTime sets UpdateTime field to given value.

### HasUpdateTime

`func (o *ResponseGetItemsV2ItemsGetInner) HasUpdateTime() bool`

HasUpdateTime returns a boolean if a field has been set.

### GetProperties

`func (o *ResponseGetItemsV2ItemsGetInner) GetProperties() map[string]UpgradePropertyV2`

GetProperties returns the Properties field if non-nil, zero value otherwise.

### GetPropertiesOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetPropertiesOk() (*map[string]UpgradePropertyV2, bool)`

GetPropertiesOk returns a tuple with the Properties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperties

`func (o *ResponseGetItemsV2ItemsGetInner) SetProperties(v map[string]UpgradePropertyV2)`

SetProperties sets Properties field to given value.

### HasProperties

`func (o *ResponseGetItemsV2ItemsGetInner) HasProperties() bool`

HasProperties returns a boolean if a field has been set.

### GetWeaponInfo

`func (o *ResponseGetItemsV2ItemsGetInner) GetWeaponInfo() RawItemWeaponInfoV2`

GetWeaponInfo returns the WeaponInfo field if non-nil, zero value otherwise.

### GetWeaponInfoOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetWeaponInfoOk() (*RawItemWeaponInfoV2, bool)`

GetWeaponInfoOk returns a tuple with the WeaponInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponInfo

`func (o *ResponseGetItemsV2ItemsGetInner) SetWeaponInfo(v RawItemWeaponInfoV2)`

SetWeaponInfo sets WeaponInfo field to given value.

### HasWeaponInfo

`func (o *ResponseGetItemsV2ItemsGetInner) HasWeaponInfo() bool`

HasWeaponInfo returns a boolean if a field has been set.

### GetType

`func (o *ResponseGetItemsV2ItemsGetInner) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ResponseGetItemsV2ItemsGetInner) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *ResponseGetItemsV2ItemsGetInner) HasType() bool`

HasType returns a boolean if a field has been set.

### GetGrantAmmoOnCast

`func (o *ResponseGetItemsV2ItemsGetInner) GetGrantAmmoOnCast() bool`

GetGrantAmmoOnCast returns the GrantAmmoOnCast field if non-nil, zero value otherwise.

### GetGrantAmmoOnCastOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetGrantAmmoOnCastOk() (*bool, bool)`

GetGrantAmmoOnCastOk returns a tuple with the GrantAmmoOnCast field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGrantAmmoOnCast

`func (o *ResponseGetItemsV2ItemsGetInner) SetGrantAmmoOnCast(v bool)`

SetGrantAmmoOnCast sets GrantAmmoOnCast field to given value.

### HasGrantAmmoOnCast

`func (o *ResponseGetItemsV2ItemsGetInner) HasGrantAmmoOnCast() bool`

HasGrantAmmoOnCast returns a boolean if a field has been set.

### GetBehaviours

`func (o *ResponseGetItemsV2ItemsGetInner) GetBehaviours() []string`

GetBehaviours returns the Behaviours field if non-nil, zero value otherwise.

### GetBehavioursOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetBehavioursOk() (*[]string, bool)`

GetBehavioursOk returns a tuple with the Behaviours field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBehaviours

`func (o *ResponseGetItemsV2ItemsGetInner) SetBehaviours(v []string)`

SetBehaviours sets Behaviours field to given value.

### HasBehaviours

`func (o *ResponseGetItemsV2ItemsGetInner) HasBehaviours() bool`

HasBehaviours returns a boolean if a field has been set.

### GetDescription

`func (o *ResponseGetItemsV2ItemsGetInner) GetDescription() UpgradeDescriptionV2`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetDescriptionOk() (*UpgradeDescriptionV2, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ResponseGetItemsV2ItemsGetInner) SetDescription(v UpgradeDescriptionV2)`

SetDescription sets Description field to given value.


### GetTooltipDetails

`func (o *ResponseGetItemsV2ItemsGetInner) GetTooltipDetails() AbilityTooltipDetailsV2`

GetTooltipDetails returns the TooltipDetails field if non-nil, zero value otherwise.

### GetTooltipDetailsOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetTooltipDetailsOk() (*AbilityTooltipDetailsV2, bool)`

GetTooltipDetailsOk returns a tuple with the TooltipDetails field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipDetails

`func (o *ResponseGetItemsV2ItemsGetInner) SetTooltipDetails(v AbilityTooltipDetailsV2)`

SetTooltipDetails sets TooltipDetails field to given value.

### HasTooltipDetails

`func (o *ResponseGetItemsV2ItemsGetInner) HasTooltipDetails() bool`

HasTooltipDetails returns a boolean if a field has been set.

### GetUpgrades

`func (o *ResponseGetItemsV2ItemsGetInner) GetUpgrades() []RawAbilityUpgradeV2`

GetUpgrades returns the Upgrades field if non-nil, zero value otherwise.

### GetUpgradesOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetUpgradesOk() (*[]RawAbilityUpgradeV2, bool)`

GetUpgradesOk returns a tuple with the Upgrades field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpgrades

`func (o *ResponseGetItemsV2ItemsGetInner) SetUpgrades(v []RawAbilityUpgradeV2)`

SetUpgrades sets Upgrades field to given value.

### HasUpgrades

`func (o *ResponseGetItemsV2ItemsGetInner) HasUpgrades() bool`

HasUpgrades returns a boolean if a field has been set.

### GetAbilityType

`func (o *ResponseGetItemsV2ItemsGetInner) GetAbilityType() AbilityTypeV2`

GetAbilityType returns the AbilityType field if non-nil, zero value otherwise.

### GetAbilityTypeOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetAbilityTypeOk() (*AbilityTypeV2, bool)`

GetAbilityTypeOk returns a tuple with the AbilityType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAbilityType

`func (o *ResponseGetItemsV2ItemsGetInner) SetAbilityType(v AbilityTypeV2)`

SetAbilityType sets AbilityType field to given value.

### HasAbilityType

`func (o *ResponseGetItemsV2ItemsGetInner) HasAbilityType() bool`

HasAbilityType returns a boolean if a field has been set.

### GetBossDamageScale

`func (o *ResponseGetItemsV2ItemsGetInner) GetBossDamageScale() float32`

GetBossDamageScale returns the BossDamageScale field if non-nil, zero value otherwise.

### GetBossDamageScaleOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetBossDamageScaleOk() (*float32, bool)`

GetBossDamageScaleOk returns a tuple with the BossDamageScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBossDamageScale

`func (o *ResponseGetItemsV2ItemsGetInner) SetBossDamageScale(v float32)`

SetBossDamageScale sets BossDamageScale field to given value.

### HasBossDamageScale

`func (o *ResponseGetItemsV2ItemsGetInner) HasBossDamageScale() bool`

HasBossDamageScale returns a boolean if a field has been set.

### GetDependantAbilities

`func (o *ResponseGetItemsV2ItemsGetInner) GetDependantAbilities() []string`

GetDependantAbilities returns the DependantAbilities field if non-nil, zero value otherwise.

### GetDependantAbilitiesOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetDependantAbilitiesOk() (*[]string, bool)`

GetDependantAbilitiesOk returns a tuple with the DependantAbilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependantAbilities

`func (o *ResponseGetItemsV2ItemsGetInner) SetDependantAbilities(v []string)`

SetDependantAbilities sets DependantAbilities field to given value.

### HasDependantAbilities

`func (o *ResponseGetItemsV2ItemsGetInner) HasDependantAbilities() bool`

HasDependantAbilities returns a boolean if a field has been set.

### GetVideos

`func (o *ResponseGetItemsV2ItemsGetInner) GetVideos() AbilityVideosV2`

GetVideos returns the Videos field if non-nil, zero value otherwise.

### GetVideosOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetVideosOk() (*AbilityVideosV2, bool)`

GetVideosOk returns a tuple with the Videos field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVideos

`func (o *ResponseGetItemsV2ItemsGetInner) SetVideos(v AbilityVideosV2)`

SetVideos sets Videos field to given value.

### HasVideos

`func (o *ResponseGetItemsV2ItemsGetInner) HasVideos() bool`

HasVideos returns a boolean if a field has been set.

### GetDependentAbilities

`func (o *ResponseGetItemsV2ItemsGetInner) GetDependentAbilities() map[string]DependantAbilities`

GetDependentAbilities returns the DependentAbilities field if non-nil, zero value otherwise.

### GetDependentAbilitiesOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetDependentAbilitiesOk() (*map[string]DependantAbilities, bool)`

GetDependentAbilitiesOk returns a tuple with the DependentAbilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependentAbilities

`func (o *ResponseGetItemsV2ItemsGetInner) SetDependentAbilities(v map[string]DependantAbilities)`

SetDependentAbilities sets DependentAbilities field to given value.

### HasDependentAbilities

`func (o *ResponseGetItemsV2ItemsGetInner) HasDependentAbilities() bool`

HasDependentAbilities returns a boolean if a field has been set.

### GetShopImage

`func (o *ResponseGetItemsV2ItemsGetInner) GetShopImage() string`

GetShopImage returns the ShopImage field if non-nil, zero value otherwise.

### GetShopImageOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetShopImageOk() (*string, bool)`

GetShopImageOk returns a tuple with the ShopImage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImage

`func (o *ResponseGetItemsV2ItemsGetInner) SetShopImage(v string)`

SetShopImage sets ShopImage field to given value.

### HasShopImage

`func (o *ResponseGetItemsV2ItemsGetInner) HasShopImage() bool`

HasShopImage returns a boolean if a field has been set.

### GetShopImageWebp

`func (o *ResponseGetItemsV2ItemsGetInner) GetShopImageWebp() string`

GetShopImageWebp returns the ShopImageWebp field if non-nil, zero value otherwise.

### GetShopImageWebpOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetShopImageWebpOk() (*string, bool)`

GetShopImageWebpOk returns a tuple with the ShopImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageWebp

`func (o *ResponseGetItemsV2ItemsGetInner) SetShopImageWebp(v string)`

SetShopImageWebp sets ShopImageWebp field to given value.

### HasShopImageWebp

`func (o *ResponseGetItemsV2ItemsGetInner) HasShopImageWebp() bool`

HasShopImageWebp returns a boolean if a field has been set.

### GetShopImageSmall

`func (o *ResponseGetItemsV2ItemsGetInner) GetShopImageSmall() string`

GetShopImageSmall returns the ShopImageSmall field if non-nil, zero value otherwise.

### GetShopImageSmallOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetShopImageSmallOk() (*string, bool)`

GetShopImageSmallOk returns a tuple with the ShopImageSmall field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageSmall

`func (o *ResponseGetItemsV2ItemsGetInner) SetShopImageSmall(v string)`

SetShopImageSmall sets ShopImageSmall field to given value.

### HasShopImageSmall

`func (o *ResponseGetItemsV2ItemsGetInner) HasShopImageSmall() bool`

HasShopImageSmall returns a boolean if a field has been set.

### GetShopImageSmallWebp

`func (o *ResponseGetItemsV2ItemsGetInner) GetShopImageSmallWebp() string`

GetShopImageSmallWebp returns the ShopImageSmallWebp field if non-nil, zero value otherwise.

### GetShopImageSmallWebpOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetShopImageSmallWebpOk() (*string, bool)`

GetShopImageSmallWebpOk returns a tuple with the ShopImageSmallWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageSmallWebp

`func (o *ResponseGetItemsV2ItemsGetInner) SetShopImageSmallWebp(v string)`

SetShopImageSmallWebp sets ShopImageSmallWebp field to given value.

### HasShopImageSmallWebp

`func (o *ResponseGetItemsV2ItemsGetInner) HasShopImageSmallWebp() bool`

HasShopImageSmallWebp returns a boolean if a field has been set.

### GetItemSlotType

`func (o *ResponseGetItemsV2ItemsGetInner) GetItemSlotType() ItemSlotTypeV2`

GetItemSlotType returns the ItemSlotType field if non-nil, zero value otherwise.

### GetItemSlotTypeOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetItemSlotTypeOk() (*ItemSlotTypeV2, bool)`

GetItemSlotTypeOk returns a tuple with the ItemSlotType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemSlotType

`func (o *ResponseGetItemsV2ItemsGetInner) SetItemSlotType(v ItemSlotTypeV2)`

SetItemSlotType sets ItemSlotType field to given value.


### GetItemTier

`func (o *ResponseGetItemsV2ItemsGetInner) GetItemTier() ItemTierV2`

GetItemTier returns the ItemTier field if non-nil, zero value otherwise.

### GetItemTierOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetItemTierOk() (*ItemTierV2, bool)`

GetItemTierOk returns a tuple with the ItemTier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemTier

`func (o *ResponseGetItemsV2ItemsGetInner) SetItemTier(v ItemTierV2)`

SetItemTier sets ItemTier field to given value.


### GetDisabled

`func (o *ResponseGetItemsV2ItemsGetInner) GetDisabled() bool`

GetDisabled returns the Disabled field if non-nil, zero value otherwise.

### GetDisabledOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetDisabledOk() (*bool, bool)`

GetDisabledOk returns a tuple with the Disabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisabled

`func (o *ResponseGetItemsV2ItemsGetInner) SetDisabled(v bool)`

SetDisabled sets Disabled field to given value.

### HasDisabled

`func (o *ResponseGetItemsV2ItemsGetInner) HasDisabled() bool`

HasDisabled returns a boolean if a field has been set.

### GetActivation

`func (o *ResponseGetItemsV2ItemsGetInner) GetActivation() RawAbilityActivationV2`

GetActivation returns the Activation field if non-nil, zero value otherwise.

### GetActivationOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetActivationOk() (*RawAbilityActivationV2, bool)`

GetActivationOk returns a tuple with the Activation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActivation

`func (o *ResponseGetItemsV2ItemsGetInner) SetActivation(v RawAbilityActivationV2)`

SetActivation sets Activation field to given value.


### GetImbue

`func (o *ResponseGetItemsV2ItemsGetInner) GetImbue() RawAbilityImbueV2`

GetImbue returns the Imbue field if non-nil, zero value otherwise.

### GetImbueOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetImbueOk() (*RawAbilityImbueV2, bool)`

GetImbueOk returns a tuple with the Imbue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImbue

`func (o *ResponseGetItemsV2ItemsGetInner) SetImbue(v RawAbilityImbueV2)`

SetImbue sets Imbue field to given value.

### HasImbue

`func (o *ResponseGetItemsV2ItemsGetInner) HasImbue() bool`

HasImbue returns a boolean if a field has been set.

### GetComponentItems

`func (o *ResponseGetItemsV2ItemsGetInner) GetComponentItems() []string`

GetComponentItems returns the ComponentItems field if non-nil, zero value otherwise.

### GetComponentItemsOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetComponentItemsOk() (*[]string, bool)`

GetComponentItemsOk returns a tuple with the ComponentItems field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComponentItems

`func (o *ResponseGetItemsV2ItemsGetInner) SetComponentItems(v []string)`

SetComponentItems sets ComponentItems field to given value.

### HasComponentItems

`func (o *ResponseGetItemsV2ItemsGetInner) HasComponentItems() bool`

HasComponentItems returns a boolean if a field has been set.

### GetTooltipSections

`func (o *ResponseGetItemsV2ItemsGetInner) GetTooltipSections() []UpgradeTooltipSectionV2`

GetTooltipSections returns the TooltipSections field if non-nil, zero value otherwise.

### GetTooltipSectionsOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetTooltipSectionsOk() (*[]UpgradeTooltipSectionV2, bool)`

GetTooltipSectionsOk returns a tuple with the TooltipSections field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipSections

`func (o *ResponseGetItemsV2ItemsGetInner) SetTooltipSections(v []UpgradeTooltipSectionV2)`

SetTooltipSections sets TooltipSections field to given value.

### HasTooltipSections

`func (o *ResponseGetItemsV2ItemsGetInner) HasTooltipSections() bool`

HasTooltipSections returns a boolean if a field has been set.

### GetIsActiveItem

`func (o *ResponseGetItemsV2ItemsGetInner) GetIsActiveItem() bool`

GetIsActiveItem returns the IsActiveItem field if non-nil, zero value otherwise.

### GetIsActiveItemOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetIsActiveItemOk() (*bool, bool)`

GetIsActiveItemOk returns a tuple with the IsActiveItem field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsActiveItem

`func (o *ResponseGetItemsV2ItemsGetInner) SetIsActiveItem(v bool)`

SetIsActiveItem sets IsActiveItem field to given value.


### GetShopable

`func (o *ResponseGetItemsV2ItemsGetInner) GetShopable() bool`

GetShopable returns the Shopable field if non-nil, zero value otherwise.

### GetShopableOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetShopableOk() (*bool, bool)`

GetShopableOk returns a tuple with the Shopable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopable

`func (o *ResponseGetItemsV2ItemsGetInner) SetShopable(v bool)`

SetShopable sets Shopable field to given value.


### GetCost

`func (o *ResponseGetItemsV2ItemsGetInner) GetCost() int32`

GetCost returns the Cost field if non-nil, zero value otherwise.

### GetCostOk

`func (o *ResponseGetItemsV2ItemsGetInner) GetCostOk() (*int32, bool)`

GetCostOk returns a tuple with the Cost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCost

`func (o *ResponseGetItemsV2ItemsGetInner) SetCost(v int32)`

SetCost sets Cost field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


