# ResponseGetItemV2ItemsIdOrClassNameGet

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

### NewResponseGetItemV2ItemsIdOrClassNameGet

`func NewResponseGetItemV2ItemsIdOrClassNameGet(id int32, className string, name string, description UpgradeDescriptionV2, itemSlotType ItemSlotTypeV2, itemTier ItemTierV2, activation RawAbilityActivationV2, isActiveItem bool, shopable bool, cost int32, ) *ResponseGetItemV2ItemsIdOrClassNameGet`

NewResponseGetItemV2ItemsIdOrClassNameGet instantiates a new ResponseGetItemV2ItemsIdOrClassNameGet object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewResponseGetItemV2ItemsIdOrClassNameGetWithDefaults

`func NewResponseGetItemV2ItemsIdOrClassNameGetWithDefaults() *ResponseGetItemV2ItemsIdOrClassNameGet`

NewResponseGetItemV2ItemsIdOrClassNameGetWithDefaults instantiates a new ResponseGetItemV2ItemsIdOrClassNameGet object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetId(v int32)`

SetId sets Id field to given value.


### GetClassName

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetName

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetName(v string)`

SetName sets Name field to given value.


### GetStartTrained

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetStartTrained() bool`

GetStartTrained returns the StartTrained field if non-nil, zero value otherwise.

### GetStartTrainedOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetStartTrainedOk() (*bool, bool)`

GetStartTrainedOk returns a tuple with the StartTrained field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTrained

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetStartTrained(v bool)`

SetStartTrained sets StartTrained field to given value.

### HasStartTrained

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasStartTrained() bool`

HasStartTrained returns a boolean if a field has been set.

### GetImage

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetImage() string`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetImageOk() (*string, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetImage(v string)`

SetImage sets Image field to given value.

### HasImage

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasImage() bool`

HasImage returns a boolean if a field has been set.

### GetImageWebp

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetImageWebp() string`

GetImageWebp returns the ImageWebp field if non-nil, zero value otherwise.

### GetImageWebpOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetImageWebpOk() (*string, bool)`

GetImageWebpOk returns a tuple with the ImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImageWebp

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetImageWebp(v string)`

SetImageWebp sets ImageWebp field to given value.

### HasImageWebp

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasImageWebp() bool`

HasImageWebp returns a boolean if a field has been set.

### GetHero

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetHero() int32`

GetHero returns the Hero field if non-nil, zero value otherwise.

### GetHeroOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetHeroOk() (*int32, bool)`

GetHeroOk returns a tuple with the Hero field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHero

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetHero(v int32)`

SetHero sets Hero field to given value.

### HasHero

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasHero() bool`

HasHero returns a boolean if a field has been set.

### GetHeroes

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetHeroes() []int32`

GetHeroes returns the Heroes field if non-nil, zero value otherwise.

### GetHeroesOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetHeroesOk() (*[]int32, bool)`

GetHeroesOk returns a tuple with the Heroes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroes

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetHeroes(v []int32)`

SetHeroes sets Heroes field to given value.

### HasHeroes

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasHeroes() bool`

HasHeroes returns a boolean if a field has been set.

### GetUpdateTime

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetUpdateTime() int32`

GetUpdateTime returns the UpdateTime field if non-nil, zero value otherwise.

### GetUpdateTimeOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetUpdateTimeOk() (*int32, bool)`

GetUpdateTimeOk returns a tuple with the UpdateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateTime

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetUpdateTime(v int32)`

SetUpdateTime sets UpdateTime field to given value.

### HasUpdateTime

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasUpdateTime() bool`

HasUpdateTime returns a boolean if a field has been set.

### GetProperties

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetProperties() map[string]UpgradePropertyV2`

GetProperties returns the Properties field if non-nil, zero value otherwise.

### GetPropertiesOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetPropertiesOk() (*map[string]UpgradePropertyV2, bool)`

GetPropertiesOk returns a tuple with the Properties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperties

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetProperties(v map[string]UpgradePropertyV2)`

SetProperties sets Properties field to given value.

### HasProperties

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasProperties() bool`

HasProperties returns a boolean if a field has been set.

### GetWeaponInfo

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetWeaponInfo() RawItemWeaponInfoV2`

GetWeaponInfo returns the WeaponInfo field if non-nil, zero value otherwise.

### GetWeaponInfoOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetWeaponInfoOk() (*RawItemWeaponInfoV2, bool)`

GetWeaponInfoOk returns a tuple with the WeaponInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponInfo

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetWeaponInfo(v RawItemWeaponInfoV2)`

SetWeaponInfo sets WeaponInfo field to given value.

### HasWeaponInfo

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasWeaponInfo() bool`

HasWeaponInfo returns a boolean if a field has been set.

### GetType

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasType() bool`

HasType returns a boolean if a field has been set.

### GetGrantAmmoOnCast

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetGrantAmmoOnCast() bool`

GetGrantAmmoOnCast returns the GrantAmmoOnCast field if non-nil, zero value otherwise.

### GetGrantAmmoOnCastOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetGrantAmmoOnCastOk() (*bool, bool)`

GetGrantAmmoOnCastOk returns a tuple with the GrantAmmoOnCast field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGrantAmmoOnCast

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetGrantAmmoOnCast(v bool)`

SetGrantAmmoOnCast sets GrantAmmoOnCast field to given value.

### HasGrantAmmoOnCast

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasGrantAmmoOnCast() bool`

HasGrantAmmoOnCast returns a boolean if a field has been set.

### GetBehaviours

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetBehaviours() []string`

GetBehaviours returns the Behaviours field if non-nil, zero value otherwise.

### GetBehavioursOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetBehavioursOk() (*[]string, bool)`

GetBehavioursOk returns a tuple with the Behaviours field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBehaviours

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetBehaviours(v []string)`

SetBehaviours sets Behaviours field to given value.

### HasBehaviours

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasBehaviours() bool`

HasBehaviours returns a boolean if a field has been set.

### GetDescription

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetDescription() UpgradeDescriptionV2`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetDescriptionOk() (*UpgradeDescriptionV2, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetDescription(v UpgradeDescriptionV2)`

SetDescription sets Description field to given value.


### GetTooltipDetails

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetTooltipDetails() AbilityTooltipDetailsV2`

GetTooltipDetails returns the TooltipDetails field if non-nil, zero value otherwise.

### GetTooltipDetailsOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetTooltipDetailsOk() (*AbilityTooltipDetailsV2, bool)`

GetTooltipDetailsOk returns a tuple with the TooltipDetails field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipDetails

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetTooltipDetails(v AbilityTooltipDetailsV2)`

SetTooltipDetails sets TooltipDetails field to given value.

### HasTooltipDetails

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasTooltipDetails() bool`

HasTooltipDetails returns a boolean if a field has been set.

### GetUpgrades

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetUpgrades() []RawAbilityUpgradeV2`

GetUpgrades returns the Upgrades field if non-nil, zero value otherwise.

### GetUpgradesOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetUpgradesOk() (*[]RawAbilityUpgradeV2, bool)`

GetUpgradesOk returns a tuple with the Upgrades field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpgrades

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetUpgrades(v []RawAbilityUpgradeV2)`

SetUpgrades sets Upgrades field to given value.

### HasUpgrades

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasUpgrades() bool`

HasUpgrades returns a boolean if a field has been set.

### GetAbilityType

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetAbilityType() AbilityTypeV2`

GetAbilityType returns the AbilityType field if non-nil, zero value otherwise.

### GetAbilityTypeOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetAbilityTypeOk() (*AbilityTypeV2, bool)`

GetAbilityTypeOk returns a tuple with the AbilityType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAbilityType

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetAbilityType(v AbilityTypeV2)`

SetAbilityType sets AbilityType field to given value.

### HasAbilityType

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasAbilityType() bool`

HasAbilityType returns a boolean if a field has been set.

### GetBossDamageScale

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetBossDamageScale() float32`

GetBossDamageScale returns the BossDamageScale field if non-nil, zero value otherwise.

### GetBossDamageScaleOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetBossDamageScaleOk() (*float32, bool)`

GetBossDamageScaleOk returns a tuple with the BossDamageScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBossDamageScale

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetBossDamageScale(v float32)`

SetBossDamageScale sets BossDamageScale field to given value.

### HasBossDamageScale

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasBossDamageScale() bool`

HasBossDamageScale returns a boolean if a field has been set.

### GetDependantAbilities

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetDependantAbilities() []string`

GetDependantAbilities returns the DependantAbilities field if non-nil, zero value otherwise.

### GetDependantAbilitiesOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetDependantAbilitiesOk() (*[]string, bool)`

GetDependantAbilitiesOk returns a tuple with the DependantAbilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependantAbilities

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetDependantAbilities(v []string)`

SetDependantAbilities sets DependantAbilities field to given value.

### HasDependantAbilities

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasDependantAbilities() bool`

HasDependantAbilities returns a boolean if a field has been set.

### GetVideos

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetVideos() AbilityVideosV2`

GetVideos returns the Videos field if non-nil, zero value otherwise.

### GetVideosOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetVideosOk() (*AbilityVideosV2, bool)`

GetVideosOk returns a tuple with the Videos field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVideos

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetVideos(v AbilityVideosV2)`

SetVideos sets Videos field to given value.

### HasVideos

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasVideos() bool`

HasVideos returns a boolean if a field has been set.

### GetDependentAbilities

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetDependentAbilities() map[string]DependantAbilities`

GetDependentAbilities returns the DependentAbilities field if non-nil, zero value otherwise.

### GetDependentAbilitiesOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetDependentAbilitiesOk() (*map[string]DependantAbilities, bool)`

GetDependentAbilitiesOk returns a tuple with the DependentAbilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependentAbilities

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetDependentAbilities(v map[string]DependantAbilities)`

SetDependentAbilities sets DependentAbilities field to given value.

### HasDependentAbilities

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasDependentAbilities() bool`

HasDependentAbilities returns a boolean if a field has been set.

### GetShopImage

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetShopImage() string`

GetShopImage returns the ShopImage field if non-nil, zero value otherwise.

### GetShopImageOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetShopImageOk() (*string, bool)`

GetShopImageOk returns a tuple with the ShopImage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImage

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetShopImage(v string)`

SetShopImage sets ShopImage field to given value.

### HasShopImage

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasShopImage() bool`

HasShopImage returns a boolean if a field has been set.

### GetShopImageWebp

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetShopImageWebp() string`

GetShopImageWebp returns the ShopImageWebp field if non-nil, zero value otherwise.

### GetShopImageWebpOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetShopImageWebpOk() (*string, bool)`

GetShopImageWebpOk returns a tuple with the ShopImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageWebp

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetShopImageWebp(v string)`

SetShopImageWebp sets ShopImageWebp field to given value.

### HasShopImageWebp

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasShopImageWebp() bool`

HasShopImageWebp returns a boolean if a field has been set.

### GetShopImageSmall

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetShopImageSmall() string`

GetShopImageSmall returns the ShopImageSmall field if non-nil, zero value otherwise.

### GetShopImageSmallOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetShopImageSmallOk() (*string, bool)`

GetShopImageSmallOk returns a tuple with the ShopImageSmall field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageSmall

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetShopImageSmall(v string)`

SetShopImageSmall sets ShopImageSmall field to given value.

### HasShopImageSmall

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasShopImageSmall() bool`

HasShopImageSmall returns a boolean if a field has been set.

### GetShopImageSmallWebp

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetShopImageSmallWebp() string`

GetShopImageSmallWebp returns the ShopImageSmallWebp field if non-nil, zero value otherwise.

### GetShopImageSmallWebpOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetShopImageSmallWebpOk() (*string, bool)`

GetShopImageSmallWebpOk returns a tuple with the ShopImageSmallWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageSmallWebp

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetShopImageSmallWebp(v string)`

SetShopImageSmallWebp sets ShopImageSmallWebp field to given value.

### HasShopImageSmallWebp

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasShopImageSmallWebp() bool`

HasShopImageSmallWebp returns a boolean if a field has been set.

### GetItemSlotType

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetItemSlotType() ItemSlotTypeV2`

GetItemSlotType returns the ItemSlotType field if non-nil, zero value otherwise.

### GetItemSlotTypeOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetItemSlotTypeOk() (*ItemSlotTypeV2, bool)`

GetItemSlotTypeOk returns a tuple with the ItemSlotType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemSlotType

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetItemSlotType(v ItemSlotTypeV2)`

SetItemSlotType sets ItemSlotType field to given value.


### GetItemTier

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetItemTier() ItemTierV2`

GetItemTier returns the ItemTier field if non-nil, zero value otherwise.

### GetItemTierOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetItemTierOk() (*ItemTierV2, bool)`

GetItemTierOk returns a tuple with the ItemTier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemTier

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetItemTier(v ItemTierV2)`

SetItemTier sets ItemTier field to given value.


### GetDisabled

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetDisabled() bool`

GetDisabled returns the Disabled field if non-nil, zero value otherwise.

### GetDisabledOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetDisabledOk() (*bool, bool)`

GetDisabledOk returns a tuple with the Disabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisabled

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetDisabled(v bool)`

SetDisabled sets Disabled field to given value.

### HasDisabled

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasDisabled() bool`

HasDisabled returns a boolean if a field has been set.

### GetActivation

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetActivation() RawAbilityActivationV2`

GetActivation returns the Activation field if non-nil, zero value otherwise.

### GetActivationOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetActivationOk() (*RawAbilityActivationV2, bool)`

GetActivationOk returns a tuple with the Activation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActivation

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetActivation(v RawAbilityActivationV2)`

SetActivation sets Activation field to given value.


### GetImbue

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetImbue() RawAbilityImbueV2`

GetImbue returns the Imbue field if non-nil, zero value otherwise.

### GetImbueOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetImbueOk() (*RawAbilityImbueV2, bool)`

GetImbueOk returns a tuple with the Imbue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImbue

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetImbue(v RawAbilityImbueV2)`

SetImbue sets Imbue field to given value.

### HasImbue

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasImbue() bool`

HasImbue returns a boolean if a field has been set.

### GetComponentItems

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetComponentItems() []string`

GetComponentItems returns the ComponentItems field if non-nil, zero value otherwise.

### GetComponentItemsOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetComponentItemsOk() (*[]string, bool)`

GetComponentItemsOk returns a tuple with the ComponentItems field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComponentItems

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetComponentItems(v []string)`

SetComponentItems sets ComponentItems field to given value.

### HasComponentItems

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasComponentItems() bool`

HasComponentItems returns a boolean if a field has been set.

### GetTooltipSections

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetTooltipSections() []UpgradeTooltipSectionV2`

GetTooltipSections returns the TooltipSections field if non-nil, zero value otherwise.

### GetTooltipSectionsOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetTooltipSectionsOk() (*[]UpgradeTooltipSectionV2, bool)`

GetTooltipSectionsOk returns a tuple with the TooltipSections field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipSections

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetTooltipSections(v []UpgradeTooltipSectionV2)`

SetTooltipSections sets TooltipSections field to given value.

### HasTooltipSections

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) HasTooltipSections() bool`

HasTooltipSections returns a boolean if a field has been set.

### GetIsActiveItem

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetIsActiveItem() bool`

GetIsActiveItem returns the IsActiveItem field if non-nil, zero value otherwise.

### GetIsActiveItemOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetIsActiveItemOk() (*bool, bool)`

GetIsActiveItemOk returns a tuple with the IsActiveItem field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsActiveItem

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetIsActiveItem(v bool)`

SetIsActiveItem sets IsActiveItem field to given value.


### GetShopable

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetShopable() bool`

GetShopable returns the Shopable field if non-nil, zero value otherwise.

### GetShopableOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetShopableOk() (*bool, bool)`

GetShopableOk returns a tuple with the Shopable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopable

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetShopable(v bool)`

SetShopable sets Shopable field to given value.


### GetCost

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetCost() int32`

GetCost returns the Cost field if non-nil, zero value otherwise.

### GetCostOk

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) GetCostOk() (*int32, bool)`

GetCostOk returns a tuple with the Cost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCost

`func (o *ResponseGetItemV2ItemsIdOrClassNameGet) SetCost(v int32)`

SetCost sets Cost field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


