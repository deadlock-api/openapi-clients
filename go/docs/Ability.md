# Ability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AbilityType** | Pointer to [**NullableAbilityType**](AbilityType.md) |  | [optional] 
**Behaviours** | Pointer to **[]string** |  | [optional] 
**BossDamageScale** | Pointer to **NullableFloat64** |  | [optional] 
**ClassName** | **string** |  | 
**DependantAbilities** | Pointer to **[]string** |  | [optional] 
**DependentAbilities** | Pointer to [**map[string]DependantAbilities**](DependantAbilities.md) |  | [optional] 
**Description** | [**AbilityDescription**](AbilityDescription.md) |  | 
**GrantAmmoOnCast** | Pointer to **NullableBool** |  | [optional] 
**Hero** | Pointer to **NullableInt32** |  | [optional] 
**Heroes** | Pointer to **[]int32** |  | [optional] 
**Id** | **int32** |  | 
**Image** | Pointer to **NullableString** |  | [optional] 
**ImageWebp** | Pointer to **NullableString** |  | [optional] 
**Name** | **string** |  | 
**Properties** | Pointer to [**map[string]ItemProperty**](ItemProperty.md) |  | [optional] 
**StartTrained** | Pointer to **NullableBool** |  | [optional] 
**TooltipDetails** | Pointer to [**NullableAbilityTooltipDetails**](AbilityTooltipDetails.md) |  | [optional] 
**Type** | [**ItemType**](ItemType.md) |  | 
**UpdateTime** | Pointer to **NullableInt64** |  | [optional] 
**Upgrades** | Pointer to [**[]RawAbilityUpgrade**](RawAbilityUpgrade.md) |  | [optional] 
**Videos** | Pointer to [**NullableAbilityVideos**](AbilityVideos.md) |  | [optional] 
**WeaponInfo** | Pointer to [**NullableRawItemWeaponInfoInner**](RawItemWeaponInfoInner.md) |  | [optional] 

## Methods

### NewAbility

`func NewAbility(className string, description AbilityDescription, id int32, name string, type_ ItemType, ) *Ability`

NewAbility instantiates a new Ability object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAbilityWithDefaults

`func NewAbilityWithDefaults() *Ability`

NewAbilityWithDefaults instantiates a new Ability object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAbilityType

`func (o *Ability) GetAbilityType() AbilityType`

GetAbilityType returns the AbilityType field if non-nil, zero value otherwise.

### GetAbilityTypeOk

`func (o *Ability) GetAbilityTypeOk() (*AbilityType, bool)`

GetAbilityTypeOk returns a tuple with the AbilityType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAbilityType

`func (o *Ability) SetAbilityType(v AbilityType)`

SetAbilityType sets AbilityType field to given value.

### HasAbilityType

`func (o *Ability) HasAbilityType() bool`

HasAbilityType returns a boolean if a field has been set.

### SetAbilityTypeNil

`func (o *Ability) SetAbilityTypeNil(b bool)`

 SetAbilityTypeNil sets the value for AbilityType to be an explicit nil

### UnsetAbilityType
`func (o *Ability) UnsetAbilityType()`

UnsetAbilityType ensures that no value is present for AbilityType, not even an explicit nil
### GetBehaviours

`func (o *Ability) GetBehaviours() []string`

GetBehaviours returns the Behaviours field if non-nil, zero value otherwise.

### GetBehavioursOk

`func (o *Ability) GetBehavioursOk() (*[]string, bool)`

GetBehavioursOk returns a tuple with the Behaviours field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBehaviours

`func (o *Ability) SetBehaviours(v []string)`

SetBehaviours sets Behaviours field to given value.

### HasBehaviours

`func (o *Ability) HasBehaviours() bool`

HasBehaviours returns a boolean if a field has been set.

### SetBehavioursNil

`func (o *Ability) SetBehavioursNil(b bool)`

 SetBehavioursNil sets the value for Behaviours to be an explicit nil

### UnsetBehaviours
`func (o *Ability) UnsetBehaviours()`

UnsetBehaviours ensures that no value is present for Behaviours, not even an explicit nil
### GetBossDamageScale

`func (o *Ability) GetBossDamageScale() float64`

GetBossDamageScale returns the BossDamageScale field if non-nil, zero value otherwise.

### GetBossDamageScaleOk

`func (o *Ability) GetBossDamageScaleOk() (*float64, bool)`

GetBossDamageScaleOk returns a tuple with the BossDamageScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBossDamageScale

`func (o *Ability) SetBossDamageScale(v float64)`

SetBossDamageScale sets BossDamageScale field to given value.

### HasBossDamageScale

`func (o *Ability) HasBossDamageScale() bool`

HasBossDamageScale returns a boolean if a field has been set.

### SetBossDamageScaleNil

`func (o *Ability) SetBossDamageScaleNil(b bool)`

 SetBossDamageScaleNil sets the value for BossDamageScale to be an explicit nil

### UnsetBossDamageScale
`func (o *Ability) UnsetBossDamageScale()`

UnsetBossDamageScale ensures that no value is present for BossDamageScale, not even an explicit nil
### GetClassName

`func (o *Ability) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *Ability) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *Ability) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetDependantAbilities

`func (o *Ability) GetDependantAbilities() []string`

GetDependantAbilities returns the DependantAbilities field if non-nil, zero value otherwise.

### GetDependantAbilitiesOk

`func (o *Ability) GetDependantAbilitiesOk() (*[]string, bool)`

GetDependantAbilitiesOk returns a tuple with the DependantAbilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependantAbilities

`func (o *Ability) SetDependantAbilities(v []string)`

SetDependantAbilities sets DependantAbilities field to given value.

### HasDependantAbilities

`func (o *Ability) HasDependantAbilities() bool`

HasDependantAbilities returns a boolean if a field has been set.

### SetDependantAbilitiesNil

`func (o *Ability) SetDependantAbilitiesNil(b bool)`

 SetDependantAbilitiesNil sets the value for DependantAbilities to be an explicit nil

### UnsetDependantAbilities
`func (o *Ability) UnsetDependantAbilities()`

UnsetDependantAbilities ensures that no value is present for DependantAbilities, not even an explicit nil
### GetDependentAbilities

`func (o *Ability) GetDependentAbilities() map[string]DependantAbilities`

GetDependentAbilities returns the DependentAbilities field if non-nil, zero value otherwise.

### GetDependentAbilitiesOk

`func (o *Ability) GetDependentAbilitiesOk() (*map[string]DependantAbilities, bool)`

GetDependentAbilitiesOk returns a tuple with the DependentAbilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependentAbilities

`func (o *Ability) SetDependentAbilities(v map[string]DependantAbilities)`

SetDependentAbilities sets DependentAbilities field to given value.

### HasDependentAbilities

`func (o *Ability) HasDependentAbilities() bool`

HasDependentAbilities returns a boolean if a field has been set.

### GetDescription

`func (o *Ability) GetDescription() AbilityDescription`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Ability) GetDescriptionOk() (*AbilityDescription, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Ability) SetDescription(v AbilityDescription)`

SetDescription sets Description field to given value.


### GetGrantAmmoOnCast

`func (o *Ability) GetGrantAmmoOnCast() bool`

GetGrantAmmoOnCast returns the GrantAmmoOnCast field if non-nil, zero value otherwise.

### GetGrantAmmoOnCastOk

`func (o *Ability) GetGrantAmmoOnCastOk() (*bool, bool)`

GetGrantAmmoOnCastOk returns a tuple with the GrantAmmoOnCast field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGrantAmmoOnCast

`func (o *Ability) SetGrantAmmoOnCast(v bool)`

SetGrantAmmoOnCast sets GrantAmmoOnCast field to given value.

### HasGrantAmmoOnCast

`func (o *Ability) HasGrantAmmoOnCast() bool`

HasGrantAmmoOnCast returns a boolean if a field has been set.

### SetGrantAmmoOnCastNil

`func (o *Ability) SetGrantAmmoOnCastNil(b bool)`

 SetGrantAmmoOnCastNil sets the value for GrantAmmoOnCast to be an explicit nil

### UnsetGrantAmmoOnCast
`func (o *Ability) UnsetGrantAmmoOnCast()`

UnsetGrantAmmoOnCast ensures that no value is present for GrantAmmoOnCast, not even an explicit nil
### GetHero

`func (o *Ability) GetHero() int32`

GetHero returns the Hero field if non-nil, zero value otherwise.

### GetHeroOk

`func (o *Ability) GetHeroOk() (*int32, bool)`

GetHeroOk returns a tuple with the Hero field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHero

`func (o *Ability) SetHero(v int32)`

SetHero sets Hero field to given value.

### HasHero

`func (o *Ability) HasHero() bool`

HasHero returns a boolean if a field has been set.

### SetHeroNil

`func (o *Ability) SetHeroNil(b bool)`

 SetHeroNil sets the value for Hero to be an explicit nil

### UnsetHero
`func (o *Ability) UnsetHero()`

UnsetHero ensures that no value is present for Hero, not even an explicit nil
### GetHeroes

`func (o *Ability) GetHeroes() []int32`

GetHeroes returns the Heroes field if non-nil, zero value otherwise.

### GetHeroesOk

`func (o *Ability) GetHeroesOk() (*[]int32, bool)`

GetHeroesOk returns a tuple with the Heroes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroes

`func (o *Ability) SetHeroes(v []int32)`

SetHeroes sets Heroes field to given value.

### HasHeroes

`func (o *Ability) HasHeroes() bool`

HasHeroes returns a boolean if a field has been set.

### SetHeroesNil

`func (o *Ability) SetHeroesNil(b bool)`

 SetHeroesNil sets the value for Heroes to be an explicit nil

### UnsetHeroes
`func (o *Ability) UnsetHeroes()`

UnsetHeroes ensures that no value is present for Heroes, not even an explicit nil
### GetId

`func (o *Ability) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Ability) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Ability) SetId(v int32)`

SetId sets Id field to given value.


### GetImage

`func (o *Ability) GetImage() string`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *Ability) GetImageOk() (*string, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *Ability) SetImage(v string)`

SetImage sets Image field to given value.

### HasImage

`func (o *Ability) HasImage() bool`

HasImage returns a boolean if a field has been set.

### SetImageNil

`func (o *Ability) SetImageNil(b bool)`

 SetImageNil sets the value for Image to be an explicit nil

### UnsetImage
`func (o *Ability) UnsetImage()`

UnsetImage ensures that no value is present for Image, not even an explicit nil
### GetImageWebp

`func (o *Ability) GetImageWebp() string`

GetImageWebp returns the ImageWebp field if non-nil, zero value otherwise.

### GetImageWebpOk

`func (o *Ability) GetImageWebpOk() (*string, bool)`

GetImageWebpOk returns a tuple with the ImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImageWebp

`func (o *Ability) SetImageWebp(v string)`

SetImageWebp sets ImageWebp field to given value.

### HasImageWebp

`func (o *Ability) HasImageWebp() bool`

HasImageWebp returns a boolean if a field has been set.

### SetImageWebpNil

`func (o *Ability) SetImageWebpNil(b bool)`

 SetImageWebpNil sets the value for ImageWebp to be an explicit nil

### UnsetImageWebp
`func (o *Ability) UnsetImageWebp()`

UnsetImageWebp ensures that no value is present for ImageWebp, not even an explicit nil
### GetName

`func (o *Ability) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Ability) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Ability) SetName(v string)`

SetName sets Name field to given value.


### GetProperties

`func (o *Ability) GetProperties() map[string]ItemProperty`

GetProperties returns the Properties field if non-nil, zero value otherwise.

### GetPropertiesOk

`func (o *Ability) GetPropertiesOk() (*map[string]ItemProperty, bool)`

GetPropertiesOk returns a tuple with the Properties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperties

`func (o *Ability) SetProperties(v map[string]ItemProperty)`

SetProperties sets Properties field to given value.

### HasProperties

`func (o *Ability) HasProperties() bool`

HasProperties returns a boolean if a field has been set.

### GetStartTrained

`func (o *Ability) GetStartTrained() bool`

GetStartTrained returns the StartTrained field if non-nil, zero value otherwise.

### GetStartTrainedOk

`func (o *Ability) GetStartTrainedOk() (*bool, bool)`

GetStartTrainedOk returns a tuple with the StartTrained field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTrained

`func (o *Ability) SetStartTrained(v bool)`

SetStartTrained sets StartTrained field to given value.

### HasStartTrained

`func (o *Ability) HasStartTrained() bool`

HasStartTrained returns a boolean if a field has been set.

### SetStartTrainedNil

`func (o *Ability) SetStartTrainedNil(b bool)`

 SetStartTrainedNil sets the value for StartTrained to be an explicit nil

### UnsetStartTrained
`func (o *Ability) UnsetStartTrained()`

UnsetStartTrained ensures that no value is present for StartTrained, not even an explicit nil
### GetTooltipDetails

`func (o *Ability) GetTooltipDetails() AbilityTooltipDetails`

GetTooltipDetails returns the TooltipDetails field if non-nil, zero value otherwise.

### GetTooltipDetailsOk

`func (o *Ability) GetTooltipDetailsOk() (*AbilityTooltipDetails, bool)`

GetTooltipDetailsOk returns a tuple with the TooltipDetails field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipDetails

`func (o *Ability) SetTooltipDetails(v AbilityTooltipDetails)`

SetTooltipDetails sets TooltipDetails field to given value.

### HasTooltipDetails

`func (o *Ability) HasTooltipDetails() bool`

HasTooltipDetails returns a boolean if a field has been set.

### SetTooltipDetailsNil

`func (o *Ability) SetTooltipDetailsNil(b bool)`

 SetTooltipDetailsNil sets the value for TooltipDetails to be an explicit nil

### UnsetTooltipDetails
`func (o *Ability) UnsetTooltipDetails()`

UnsetTooltipDetails ensures that no value is present for TooltipDetails, not even an explicit nil
### GetType

`func (o *Ability) GetType() ItemType`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Ability) GetTypeOk() (*ItemType, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Ability) SetType(v ItemType)`

SetType sets Type field to given value.


### GetUpdateTime

`func (o *Ability) GetUpdateTime() int64`

GetUpdateTime returns the UpdateTime field if non-nil, zero value otherwise.

### GetUpdateTimeOk

`func (o *Ability) GetUpdateTimeOk() (*int64, bool)`

GetUpdateTimeOk returns a tuple with the UpdateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateTime

`func (o *Ability) SetUpdateTime(v int64)`

SetUpdateTime sets UpdateTime field to given value.

### HasUpdateTime

`func (o *Ability) HasUpdateTime() bool`

HasUpdateTime returns a boolean if a field has been set.

### SetUpdateTimeNil

`func (o *Ability) SetUpdateTimeNil(b bool)`

 SetUpdateTimeNil sets the value for UpdateTime to be an explicit nil

### UnsetUpdateTime
`func (o *Ability) UnsetUpdateTime()`

UnsetUpdateTime ensures that no value is present for UpdateTime, not even an explicit nil
### GetUpgrades

`func (o *Ability) GetUpgrades() []RawAbilityUpgrade`

GetUpgrades returns the Upgrades field if non-nil, zero value otherwise.

### GetUpgradesOk

`func (o *Ability) GetUpgradesOk() (*[]RawAbilityUpgrade, bool)`

GetUpgradesOk returns a tuple with the Upgrades field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpgrades

`func (o *Ability) SetUpgrades(v []RawAbilityUpgrade)`

SetUpgrades sets Upgrades field to given value.

### HasUpgrades

`func (o *Ability) HasUpgrades() bool`

HasUpgrades returns a boolean if a field has been set.

### SetUpgradesNil

`func (o *Ability) SetUpgradesNil(b bool)`

 SetUpgradesNil sets the value for Upgrades to be an explicit nil

### UnsetUpgrades
`func (o *Ability) UnsetUpgrades()`

UnsetUpgrades ensures that no value is present for Upgrades, not even an explicit nil
### GetVideos

`func (o *Ability) GetVideos() AbilityVideos`

GetVideos returns the Videos field if non-nil, zero value otherwise.

### GetVideosOk

`func (o *Ability) GetVideosOk() (*AbilityVideos, bool)`

GetVideosOk returns a tuple with the Videos field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVideos

`func (o *Ability) SetVideos(v AbilityVideos)`

SetVideos sets Videos field to given value.

### HasVideos

`func (o *Ability) HasVideos() bool`

HasVideos returns a boolean if a field has been set.

### SetVideosNil

`func (o *Ability) SetVideosNil(b bool)`

 SetVideosNil sets the value for Videos to be an explicit nil

### UnsetVideos
`func (o *Ability) UnsetVideos()`

UnsetVideos ensures that no value is present for Videos, not even an explicit nil
### GetWeaponInfo

`func (o *Ability) GetWeaponInfo() RawItemWeaponInfoInner`

GetWeaponInfo returns the WeaponInfo field if non-nil, zero value otherwise.

### GetWeaponInfoOk

`func (o *Ability) GetWeaponInfoOk() (*RawItemWeaponInfoInner, bool)`

GetWeaponInfoOk returns a tuple with the WeaponInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponInfo

`func (o *Ability) SetWeaponInfo(v RawItemWeaponInfoInner)`

SetWeaponInfo sets WeaponInfo field to given value.

### HasWeaponInfo

`func (o *Ability) HasWeaponInfo() bool`

HasWeaponInfo returns a boolean if a field has been set.

### SetWeaponInfoNil

`func (o *Ability) SetWeaponInfoNil(b bool)`

 SetWeaponInfoNil sets the value for WeaponInfo to be an explicit nil

### UnsetWeaponInfo
`func (o *Ability) UnsetWeaponInfo()`

UnsetWeaponInfo ensures that no value is present for WeaponInfo, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


