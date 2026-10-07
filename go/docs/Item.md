# Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AbilityType** | Pointer to [**NullableAbilityType**](AbilityType.md) |  | [optional] 
**Behaviours** | Pointer to **[]string** |  | [optional] 
**BossDamageScale** | Pointer to **NullableFloat64** |  | [optional] 
**ClassName** | **string** |  | 
**DependantAbilities** | Pointer to **[]string** |  | [optional] 
**DependentAbilities** | Pointer to [**map[string]DependantAbilities**](DependantAbilities.md) |  | [optional] 
**Description** | [**NullableUpgradeDescription**](UpgradeDescription.md) |  | 
**GrantAmmoOnCast** | Pointer to **NullableBool** |  | [optional] 
**Hero** | Pointer to **NullableInt32** |  | [optional] 
**Heroes** | Pointer to **[]int32** |  | [optional] 
**Id** | **int32** |  | 
**Image** | Pointer to **NullableString** |  | [optional] 
**ImageWebp** | Pointer to **NullableString** |  | [optional] 
**Name** | **string** |  | 
**Properties** | Pointer to [**map[string]UpgradeProperty**](UpgradeProperty.md) |  | [optional] 
**StartTrained** | Pointer to **NullableBool** |  | [optional] 
**TooltipDetails** | Pointer to [**NullableAbilityTooltipDetails**](AbilityTooltipDetails.md) |  | [optional] 
**Type** | [**ItemType**](ItemType.md) |  | 
**UpdateTime** | Pointer to **NullableInt64** |  | [optional] 
**Upgrades** | Pointer to [**[]RawAbilityUpgrade**](RawAbilityUpgrade.md) |  | [optional] 
**Videos** | Pointer to [**NullableAbilityVideos**](AbilityVideos.md) |  | [optional] 
**WeaponInfo** | Pointer to [**NullableRawItemWeaponInfoInner**](RawItemWeaponInfoInner.md) |  | [optional] 
**CrosshairCssClass** | Pointer to **NullableString** |  | [optional] 
**CustomCrosshairSettings** | Pointer to [**NullableRawCustomCrosshairSettings**](RawCustomCrosshairSettings.md) |  | [optional] 
**UseCustomCrosshairSettings** | Pointer to **NullableBool** |  | [optional] 
**Activation** | [**AbilityActivation**](AbilityActivation.md) |  | 
**ComponentItems** | Pointer to **[]string** |  | [optional] 
**CorruptedInfo** | Pointer to [**NullableCorruptedItemInfo**](CorruptedItemInfo.md) | Present on upgrades the Broker can corrupt (build 6711+). | [optional] 
**Cost** | Pointer to **NullableInt32** |  | [optional] 
**DisableItemTarget** | Pointer to **NullableString** |  | [optional] 
**Disabled** | Pointer to **NullableBool** |  | [optional] 
**DisabledShopFilters** | Pointer to **[]string** | Shop filters (&#x60;snake_case&#x60; &#x60;EShopFilter*&#x60; names) this item is hidden from even though its stats would match them. | [optional] 
**Imbue** | Pointer to [**NullableAbilityImbue**](AbilityImbue.md) |  | [optional] 
**IsActiveItem** | **bool** |  | 
**ItemSlotType** | [**ItemSlotType**](ItemSlotType.md) |  | 
**ItemTier** | **int32** |  | 
**ShopFilters** | Pointer to **[]string** | Extra shop filters (&#x60;snake_case&#x60; &#x60;EShopFilter*&#x60; names, e.g. &#x60;status_grounded&#x60;) this item shows up under, beyond those derived from its stats. | [optional] 
**ShopImage** | Pointer to **NullableString** |  | [optional] 
**ShopImageSmall** | Pointer to **NullableString** |  | [optional] 
**ShopImageSmallWebp** | Pointer to **NullableString** |  | [optional] 
**ShopImageWebp** | Pointer to **NullableString** |  | [optional] 
**ShopVersion** | Pointer to **NullableInt64** |  | [optional] 
**Shopable** | **bool** |  | 
**TooltipSections** | Pointer to [**[]UpgradeTooltipSection**](UpgradeTooltipSection.md) |  | [optional] 

## Methods

### NewItem

`func NewItem(className string, description NullableUpgradeDescription, id int32, name string, type_ ItemType, activation AbilityActivation, isActiveItem bool, itemSlotType ItemSlotType, itemTier int32, shopable bool, ) *Item`

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

### SetAbilityTypeNil

`func (o *Item) SetAbilityTypeNil(b bool)`

 SetAbilityTypeNil sets the value for AbilityType to be an explicit nil

### UnsetAbilityType
`func (o *Item) UnsetAbilityType()`

UnsetAbilityType ensures that no value is present for AbilityType, not even an explicit nil
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

### SetBehavioursNil

`func (o *Item) SetBehavioursNil(b bool)`

 SetBehavioursNil sets the value for Behaviours to be an explicit nil

### UnsetBehaviours
`func (o *Item) UnsetBehaviours()`

UnsetBehaviours ensures that no value is present for Behaviours, not even an explicit nil
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

### SetBossDamageScaleNil

`func (o *Item) SetBossDamageScaleNil(b bool)`

 SetBossDamageScaleNil sets the value for BossDamageScale to be an explicit nil

### UnsetBossDamageScale
`func (o *Item) UnsetBossDamageScale()`

UnsetBossDamageScale ensures that no value is present for BossDamageScale, not even an explicit nil
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

### SetDependantAbilitiesNil

`func (o *Item) SetDependantAbilitiesNil(b bool)`

 SetDependantAbilitiesNil sets the value for DependantAbilities to be an explicit nil

### UnsetDependantAbilities
`func (o *Item) UnsetDependantAbilities()`

UnsetDependantAbilities ensures that no value is present for DependantAbilities, not even an explicit nil
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

### SetDependentAbilitiesNil

`func (o *Item) SetDependentAbilitiesNil(b bool)`

 SetDependentAbilitiesNil sets the value for DependentAbilities to be an explicit nil

### UnsetDependentAbilities
`func (o *Item) UnsetDependentAbilities()`

UnsetDependentAbilities ensures that no value is present for DependentAbilities, not even an explicit nil
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


### SetDescriptionNil

`func (o *Item) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *Item) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
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

### SetGrantAmmoOnCastNil

`func (o *Item) SetGrantAmmoOnCastNil(b bool)`

 SetGrantAmmoOnCastNil sets the value for GrantAmmoOnCast to be an explicit nil

### UnsetGrantAmmoOnCast
`func (o *Item) UnsetGrantAmmoOnCast()`

UnsetGrantAmmoOnCast ensures that no value is present for GrantAmmoOnCast, not even an explicit nil
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

### SetHeroNil

`func (o *Item) SetHeroNil(b bool)`

 SetHeroNil sets the value for Hero to be an explicit nil

### UnsetHero
`func (o *Item) UnsetHero()`

UnsetHero ensures that no value is present for Hero, not even an explicit nil
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

### SetHeroesNil

`func (o *Item) SetHeroesNil(b bool)`

 SetHeroesNil sets the value for Heroes to be an explicit nil

### UnsetHeroes
`func (o *Item) UnsetHeroes()`

UnsetHeroes ensures that no value is present for Heroes, not even an explicit nil
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

### SetImageNil

`func (o *Item) SetImageNil(b bool)`

 SetImageNil sets the value for Image to be an explicit nil

### UnsetImage
`func (o *Item) UnsetImage()`

UnsetImage ensures that no value is present for Image, not even an explicit nil
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

### SetImageWebpNil

`func (o *Item) SetImageWebpNil(b bool)`

 SetImageWebpNil sets the value for ImageWebp to be an explicit nil

### UnsetImageWebp
`func (o *Item) UnsetImageWebp()`

UnsetImageWebp ensures that no value is present for ImageWebp, not even an explicit nil
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

### SetPropertiesNil

`func (o *Item) SetPropertiesNil(b bool)`

 SetPropertiesNil sets the value for Properties to be an explicit nil

### UnsetProperties
`func (o *Item) UnsetProperties()`

UnsetProperties ensures that no value is present for Properties, not even an explicit nil
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

### SetStartTrainedNil

`func (o *Item) SetStartTrainedNil(b bool)`

 SetStartTrainedNil sets the value for StartTrained to be an explicit nil

### UnsetStartTrained
`func (o *Item) UnsetStartTrained()`

UnsetStartTrained ensures that no value is present for StartTrained, not even an explicit nil
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

### SetTooltipDetailsNil

`func (o *Item) SetTooltipDetailsNil(b bool)`

 SetTooltipDetailsNil sets the value for TooltipDetails to be an explicit nil

### UnsetTooltipDetails
`func (o *Item) UnsetTooltipDetails()`

UnsetTooltipDetails ensures that no value is present for TooltipDetails, not even an explicit nil
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

### SetUpdateTimeNil

`func (o *Item) SetUpdateTimeNil(b bool)`

 SetUpdateTimeNil sets the value for UpdateTime to be an explicit nil

### UnsetUpdateTime
`func (o *Item) UnsetUpdateTime()`

UnsetUpdateTime ensures that no value is present for UpdateTime, not even an explicit nil
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

### SetUpgradesNil

`func (o *Item) SetUpgradesNil(b bool)`

 SetUpgradesNil sets the value for Upgrades to be an explicit nil

### UnsetUpgrades
`func (o *Item) UnsetUpgrades()`

UnsetUpgrades ensures that no value is present for Upgrades, not even an explicit nil
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

### SetVideosNil

`func (o *Item) SetVideosNil(b bool)`

 SetVideosNil sets the value for Videos to be an explicit nil

### UnsetVideos
`func (o *Item) UnsetVideos()`

UnsetVideos ensures that no value is present for Videos, not even an explicit nil
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

### SetWeaponInfoNil

`func (o *Item) SetWeaponInfoNil(b bool)`

 SetWeaponInfoNil sets the value for WeaponInfo to be an explicit nil

### UnsetWeaponInfo
`func (o *Item) UnsetWeaponInfo()`

UnsetWeaponInfo ensures that no value is present for WeaponInfo, not even an explicit nil
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

### SetCrosshairCssClassNil

`func (o *Item) SetCrosshairCssClassNil(b bool)`

 SetCrosshairCssClassNil sets the value for CrosshairCssClass to be an explicit nil

### UnsetCrosshairCssClass
`func (o *Item) UnsetCrosshairCssClass()`

UnsetCrosshairCssClass ensures that no value is present for CrosshairCssClass, not even an explicit nil
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

### SetCustomCrosshairSettingsNil

`func (o *Item) SetCustomCrosshairSettingsNil(b bool)`

 SetCustomCrosshairSettingsNil sets the value for CustomCrosshairSettings to be an explicit nil

### UnsetCustomCrosshairSettings
`func (o *Item) UnsetCustomCrosshairSettings()`

UnsetCustomCrosshairSettings ensures that no value is present for CustomCrosshairSettings, not even an explicit nil
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

### SetUseCustomCrosshairSettingsNil

`func (o *Item) SetUseCustomCrosshairSettingsNil(b bool)`

 SetUseCustomCrosshairSettingsNil sets the value for UseCustomCrosshairSettings to be an explicit nil

### UnsetUseCustomCrosshairSettings
`func (o *Item) UnsetUseCustomCrosshairSettings()`

UnsetUseCustomCrosshairSettings ensures that no value is present for UseCustomCrosshairSettings, not even an explicit nil
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

### SetComponentItemsNil

`func (o *Item) SetComponentItemsNil(b bool)`

 SetComponentItemsNil sets the value for ComponentItems to be an explicit nil

### UnsetComponentItems
`func (o *Item) UnsetComponentItems()`

UnsetComponentItems ensures that no value is present for ComponentItems, not even an explicit nil
### GetCorruptedInfo

`func (o *Item) GetCorruptedInfo() CorruptedItemInfo`

GetCorruptedInfo returns the CorruptedInfo field if non-nil, zero value otherwise.

### GetCorruptedInfoOk

`func (o *Item) GetCorruptedInfoOk() (*CorruptedItemInfo, bool)`

GetCorruptedInfoOk returns a tuple with the CorruptedInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCorruptedInfo

`func (o *Item) SetCorruptedInfo(v CorruptedItemInfo)`

SetCorruptedInfo sets CorruptedInfo field to given value.

### HasCorruptedInfo

`func (o *Item) HasCorruptedInfo() bool`

HasCorruptedInfo returns a boolean if a field has been set.

### SetCorruptedInfoNil

`func (o *Item) SetCorruptedInfoNil(b bool)`

 SetCorruptedInfoNil sets the value for CorruptedInfo to be an explicit nil

### UnsetCorruptedInfo
`func (o *Item) UnsetCorruptedInfo()`

UnsetCorruptedInfo ensures that no value is present for CorruptedInfo, not even an explicit nil
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

### SetCostNil

`func (o *Item) SetCostNil(b bool)`

 SetCostNil sets the value for Cost to be an explicit nil

### UnsetCost
`func (o *Item) UnsetCost()`

UnsetCost ensures that no value is present for Cost, not even an explicit nil
### GetDisableItemTarget

`func (o *Item) GetDisableItemTarget() string`

GetDisableItemTarget returns the DisableItemTarget field if non-nil, zero value otherwise.

### GetDisableItemTargetOk

`func (o *Item) GetDisableItemTargetOk() (*string, bool)`

GetDisableItemTargetOk returns a tuple with the DisableItemTarget field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisableItemTarget

`func (o *Item) SetDisableItemTarget(v string)`

SetDisableItemTarget sets DisableItemTarget field to given value.

### HasDisableItemTarget

`func (o *Item) HasDisableItemTarget() bool`

HasDisableItemTarget returns a boolean if a field has been set.

### SetDisableItemTargetNil

`func (o *Item) SetDisableItemTargetNil(b bool)`

 SetDisableItemTargetNil sets the value for DisableItemTarget to be an explicit nil

### UnsetDisableItemTarget
`func (o *Item) UnsetDisableItemTarget()`

UnsetDisableItemTarget ensures that no value is present for DisableItemTarget, not even an explicit nil
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

### SetDisabledNil

`func (o *Item) SetDisabledNil(b bool)`

 SetDisabledNil sets the value for Disabled to be an explicit nil

### UnsetDisabled
`func (o *Item) UnsetDisabled()`

UnsetDisabled ensures that no value is present for Disabled, not even an explicit nil
### GetDisabledShopFilters

`func (o *Item) GetDisabledShopFilters() []string`

GetDisabledShopFilters returns the DisabledShopFilters field if non-nil, zero value otherwise.

### GetDisabledShopFiltersOk

`func (o *Item) GetDisabledShopFiltersOk() (*[]string, bool)`

GetDisabledShopFiltersOk returns a tuple with the DisabledShopFilters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisabledShopFilters

`func (o *Item) SetDisabledShopFilters(v []string)`

SetDisabledShopFilters sets DisabledShopFilters field to given value.

### HasDisabledShopFilters

`func (o *Item) HasDisabledShopFilters() bool`

HasDisabledShopFilters returns a boolean if a field has been set.

### SetDisabledShopFiltersNil

`func (o *Item) SetDisabledShopFiltersNil(b bool)`

 SetDisabledShopFiltersNil sets the value for DisabledShopFilters to be an explicit nil

### UnsetDisabledShopFilters
`func (o *Item) UnsetDisabledShopFilters()`

UnsetDisabledShopFilters ensures that no value is present for DisabledShopFilters, not even an explicit nil
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

### SetImbueNil

`func (o *Item) SetImbueNil(b bool)`

 SetImbueNil sets the value for Imbue to be an explicit nil

### UnsetImbue
`func (o *Item) UnsetImbue()`

UnsetImbue ensures that no value is present for Imbue, not even an explicit nil
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


### GetShopFilters

`func (o *Item) GetShopFilters() []string`

GetShopFilters returns the ShopFilters field if non-nil, zero value otherwise.

### GetShopFiltersOk

`func (o *Item) GetShopFiltersOk() (*[]string, bool)`

GetShopFiltersOk returns a tuple with the ShopFilters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopFilters

`func (o *Item) SetShopFilters(v []string)`

SetShopFilters sets ShopFilters field to given value.

### HasShopFilters

`func (o *Item) HasShopFilters() bool`

HasShopFilters returns a boolean if a field has been set.

### SetShopFiltersNil

`func (o *Item) SetShopFiltersNil(b bool)`

 SetShopFiltersNil sets the value for ShopFilters to be an explicit nil

### UnsetShopFilters
`func (o *Item) UnsetShopFilters()`

UnsetShopFilters ensures that no value is present for ShopFilters, not even an explicit nil
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

### SetShopImageNil

`func (o *Item) SetShopImageNil(b bool)`

 SetShopImageNil sets the value for ShopImage to be an explicit nil

### UnsetShopImage
`func (o *Item) UnsetShopImage()`

UnsetShopImage ensures that no value is present for ShopImage, not even an explicit nil
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

### SetShopImageSmallNil

`func (o *Item) SetShopImageSmallNil(b bool)`

 SetShopImageSmallNil sets the value for ShopImageSmall to be an explicit nil

### UnsetShopImageSmall
`func (o *Item) UnsetShopImageSmall()`

UnsetShopImageSmall ensures that no value is present for ShopImageSmall, not even an explicit nil
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

### SetShopImageSmallWebpNil

`func (o *Item) SetShopImageSmallWebpNil(b bool)`

 SetShopImageSmallWebpNil sets the value for ShopImageSmallWebp to be an explicit nil

### UnsetShopImageSmallWebp
`func (o *Item) UnsetShopImageSmallWebp()`

UnsetShopImageSmallWebp ensures that no value is present for ShopImageSmallWebp, not even an explicit nil
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

### SetShopImageWebpNil

`func (o *Item) SetShopImageWebpNil(b bool)`

 SetShopImageWebpNil sets the value for ShopImageWebp to be an explicit nil

### UnsetShopImageWebp
`func (o *Item) UnsetShopImageWebp()`

UnsetShopImageWebp ensures that no value is present for ShopImageWebp, not even an explicit nil
### GetShopVersion

`func (o *Item) GetShopVersion() int64`

GetShopVersion returns the ShopVersion field if non-nil, zero value otherwise.

### GetShopVersionOk

`func (o *Item) GetShopVersionOk() (*int64, bool)`

GetShopVersionOk returns a tuple with the ShopVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopVersion

`func (o *Item) SetShopVersion(v int64)`

SetShopVersion sets ShopVersion field to given value.

### HasShopVersion

`func (o *Item) HasShopVersion() bool`

HasShopVersion returns a boolean if a field has been set.

### SetShopVersionNil

`func (o *Item) SetShopVersionNil(b bool)`

 SetShopVersionNil sets the value for ShopVersion to be an explicit nil

### UnsetShopVersion
`func (o *Item) UnsetShopVersion()`

UnsetShopVersion ensures that no value is present for ShopVersion, not even an explicit nil
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

### SetTooltipSectionsNil

`func (o *Item) SetTooltipSectionsNil(b bool)`

 SetTooltipSectionsNil sets the value for TooltipSections to be an explicit nil

### UnsetTooltipSections
`func (o *Item) UnsetTooltipSections()`

UnsetTooltipSections ensures that no value is present for TooltipSections, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


