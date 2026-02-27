# AbilityV2

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
**Properties** | Pointer to [**map[string]ItemPropertyV2**](ItemPropertyV2.md) |  | [optional] 
**WeaponInfo** | Pointer to [**NullableRawItemWeaponInfoV2**](RawItemWeaponInfoV2.md) |  | [optional] 
**Type** | Pointer to **string** |  | [optional] [default to "ability"]
**GrantAmmoOnCast** | Pointer to **NullableBool** |  | [optional] 
**Behaviours** | Pointer to **[]string** |  | [optional] 
**Description** | [**AbilityDescriptionV2**](AbilityDescriptionV2.md) |  | 
**TooltipDetails** | Pointer to [**NullableAbilityTooltipDetailsV2**](AbilityTooltipDetailsV2.md) |  | [optional] 
**Upgrades** | Pointer to [**[]RawAbilityUpgradeV2**](RawAbilityUpgradeV2.md) |  | [optional] 
**AbilityType** | Pointer to [**NullableAbilityTypeV2**](AbilityTypeV2.md) |  | [optional] 
**BossDamageScale** | Pointer to **NullableFloat32** |  | [optional] 
**DependantAbilities** | Pointer to **[]string** |  | [optional] 
**Videos** | Pointer to [**NullableAbilityVideosV2**](AbilityVideosV2.md) |  | [optional] 
**DependentAbilities** | Pointer to [**map[string]DependantAbilities**](DependantAbilities.md) |  | [optional] 

## Methods

### NewAbilityV2

`func NewAbilityV2(id int32, className string, name string, description AbilityDescriptionV2, ) *AbilityV2`

NewAbilityV2 instantiates a new AbilityV2 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAbilityV2WithDefaults

`func NewAbilityV2WithDefaults() *AbilityV2`

NewAbilityV2WithDefaults instantiates a new AbilityV2 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *AbilityV2) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *AbilityV2) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *AbilityV2) SetId(v int32)`

SetId sets Id field to given value.


### GetClassName

`func (o *AbilityV2) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *AbilityV2) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *AbilityV2) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetName

`func (o *AbilityV2) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *AbilityV2) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *AbilityV2) SetName(v string)`

SetName sets Name field to given value.


### GetStartTrained

`func (o *AbilityV2) GetStartTrained() bool`

GetStartTrained returns the StartTrained field if non-nil, zero value otherwise.

### GetStartTrainedOk

`func (o *AbilityV2) GetStartTrainedOk() (*bool, bool)`

GetStartTrainedOk returns a tuple with the StartTrained field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTrained

`func (o *AbilityV2) SetStartTrained(v bool)`

SetStartTrained sets StartTrained field to given value.

### HasStartTrained

`func (o *AbilityV2) HasStartTrained() bool`

HasStartTrained returns a boolean if a field has been set.

### SetStartTrainedNil

`func (o *AbilityV2) SetStartTrainedNil(b bool)`

 SetStartTrainedNil sets the value for StartTrained to be an explicit nil

### UnsetStartTrained
`func (o *AbilityV2) UnsetStartTrained()`

UnsetStartTrained ensures that no value is present for StartTrained, not even an explicit nil
### GetImage

`func (o *AbilityV2) GetImage() string`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *AbilityV2) GetImageOk() (*string, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *AbilityV2) SetImage(v string)`

SetImage sets Image field to given value.

### HasImage

`func (o *AbilityV2) HasImage() bool`

HasImage returns a boolean if a field has been set.

### SetImageNil

`func (o *AbilityV2) SetImageNil(b bool)`

 SetImageNil sets the value for Image to be an explicit nil

### UnsetImage
`func (o *AbilityV2) UnsetImage()`

UnsetImage ensures that no value is present for Image, not even an explicit nil
### GetImageWebp

`func (o *AbilityV2) GetImageWebp() string`

GetImageWebp returns the ImageWebp field if non-nil, zero value otherwise.

### GetImageWebpOk

`func (o *AbilityV2) GetImageWebpOk() (*string, bool)`

GetImageWebpOk returns a tuple with the ImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImageWebp

`func (o *AbilityV2) SetImageWebp(v string)`

SetImageWebp sets ImageWebp field to given value.

### HasImageWebp

`func (o *AbilityV2) HasImageWebp() bool`

HasImageWebp returns a boolean if a field has been set.

### SetImageWebpNil

`func (o *AbilityV2) SetImageWebpNil(b bool)`

 SetImageWebpNil sets the value for ImageWebp to be an explicit nil

### UnsetImageWebp
`func (o *AbilityV2) UnsetImageWebp()`

UnsetImageWebp ensures that no value is present for ImageWebp, not even an explicit nil
### GetHero

`func (o *AbilityV2) GetHero() int32`

GetHero returns the Hero field if non-nil, zero value otherwise.

### GetHeroOk

`func (o *AbilityV2) GetHeroOk() (*int32, bool)`

GetHeroOk returns a tuple with the Hero field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHero

`func (o *AbilityV2) SetHero(v int32)`

SetHero sets Hero field to given value.

### HasHero

`func (o *AbilityV2) HasHero() bool`

HasHero returns a boolean if a field has been set.

### SetHeroNil

`func (o *AbilityV2) SetHeroNil(b bool)`

 SetHeroNil sets the value for Hero to be an explicit nil

### UnsetHero
`func (o *AbilityV2) UnsetHero()`

UnsetHero ensures that no value is present for Hero, not even an explicit nil
### GetHeroes

`func (o *AbilityV2) GetHeroes() []int32`

GetHeroes returns the Heroes field if non-nil, zero value otherwise.

### GetHeroesOk

`func (o *AbilityV2) GetHeroesOk() (*[]int32, bool)`

GetHeroesOk returns a tuple with the Heroes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroes

`func (o *AbilityV2) SetHeroes(v []int32)`

SetHeroes sets Heroes field to given value.

### HasHeroes

`func (o *AbilityV2) HasHeroes() bool`

HasHeroes returns a boolean if a field has been set.

### SetHeroesNil

`func (o *AbilityV2) SetHeroesNil(b bool)`

 SetHeroesNil sets the value for Heroes to be an explicit nil

### UnsetHeroes
`func (o *AbilityV2) UnsetHeroes()`

UnsetHeroes ensures that no value is present for Heroes, not even an explicit nil
### GetUpdateTime

`func (o *AbilityV2) GetUpdateTime() int32`

GetUpdateTime returns the UpdateTime field if non-nil, zero value otherwise.

### GetUpdateTimeOk

`func (o *AbilityV2) GetUpdateTimeOk() (*int32, bool)`

GetUpdateTimeOk returns a tuple with the UpdateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateTime

`func (o *AbilityV2) SetUpdateTime(v int32)`

SetUpdateTime sets UpdateTime field to given value.

### HasUpdateTime

`func (o *AbilityV2) HasUpdateTime() bool`

HasUpdateTime returns a boolean if a field has been set.

### SetUpdateTimeNil

`func (o *AbilityV2) SetUpdateTimeNil(b bool)`

 SetUpdateTimeNil sets the value for UpdateTime to be an explicit nil

### UnsetUpdateTime
`func (o *AbilityV2) UnsetUpdateTime()`

UnsetUpdateTime ensures that no value is present for UpdateTime, not even an explicit nil
### GetProperties

`func (o *AbilityV2) GetProperties() map[string]ItemPropertyV2`

GetProperties returns the Properties field if non-nil, zero value otherwise.

### GetPropertiesOk

`func (o *AbilityV2) GetPropertiesOk() (*map[string]ItemPropertyV2, bool)`

GetPropertiesOk returns a tuple with the Properties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperties

`func (o *AbilityV2) SetProperties(v map[string]ItemPropertyV2)`

SetProperties sets Properties field to given value.

### HasProperties

`func (o *AbilityV2) HasProperties() bool`

HasProperties returns a boolean if a field has been set.

### SetPropertiesNil

`func (o *AbilityV2) SetPropertiesNil(b bool)`

 SetPropertiesNil sets the value for Properties to be an explicit nil

### UnsetProperties
`func (o *AbilityV2) UnsetProperties()`

UnsetProperties ensures that no value is present for Properties, not even an explicit nil
### GetWeaponInfo

`func (o *AbilityV2) GetWeaponInfo() RawItemWeaponInfoV2`

GetWeaponInfo returns the WeaponInfo field if non-nil, zero value otherwise.

### GetWeaponInfoOk

`func (o *AbilityV2) GetWeaponInfoOk() (*RawItemWeaponInfoV2, bool)`

GetWeaponInfoOk returns a tuple with the WeaponInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponInfo

`func (o *AbilityV2) SetWeaponInfo(v RawItemWeaponInfoV2)`

SetWeaponInfo sets WeaponInfo field to given value.

### HasWeaponInfo

`func (o *AbilityV2) HasWeaponInfo() bool`

HasWeaponInfo returns a boolean if a field has been set.

### SetWeaponInfoNil

`func (o *AbilityV2) SetWeaponInfoNil(b bool)`

 SetWeaponInfoNil sets the value for WeaponInfo to be an explicit nil

### UnsetWeaponInfo
`func (o *AbilityV2) UnsetWeaponInfo()`

UnsetWeaponInfo ensures that no value is present for WeaponInfo, not even an explicit nil
### GetType

`func (o *AbilityV2) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *AbilityV2) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *AbilityV2) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *AbilityV2) HasType() bool`

HasType returns a boolean if a field has been set.

### GetGrantAmmoOnCast

`func (o *AbilityV2) GetGrantAmmoOnCast() bool`

GetGrantAmmoOnCast returns the GrantAmmoOnCast field if non-nil, zero value otherwise.

### GetGrantAmmoOnCastOk

`func (o *AbilityV2) GetGrantAmmoOnCastOk() (*bool, bool)`

GetGrantAmmoOnCastOk returns a tuple with the GrantAmmoOnCast field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGrantAmmoOnCast

`func (o *AbilityV2) SetGrantAmmoOnCast(v bool)`

SetGrantAmmoOnCast sets GrantAmmoOnCast field to given value.

### HasGrantAmmoOnCast

`func (o *AbilityV2) HasGrantAmmoOnCast() bool`

HasGrantAmmoOnCast returns a boolean if a field has been set.

### SetGrantAmmoOnCastNil

`func (o *AbilityV2) SetGrantAmmoOnCastNil(b bool)`

 SetGrantAmmoOnCastNil sets the value for GrantAmmoOnCast to be an explicit nil

### UnsetGrantAmmoOnCast
`func (o *AbilityV2) UnsetGrantAmmoOnCast()`

UnsetGrantAmmoOnCast ensures that no value is present for GrantAmmoOnCast, not even an explicit nil
### GetBehaviours

`func (o *AbilityV2) GetBehaviours() []string`

GetBehaviours returns the Behaviours field if non-nil, zero value otherwise.

### GetBehavioursOk

`func (o *AbilityV2) GetBehavioursOk() (*[]string, bool)`

GetBehavioursOk returns a tuple with the Behaviours field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBehaviours

`func (o *AbilityV2) SetBehaviours(v []string)`

SetBehaviours sets Behaviours field to given value.

### HasBehaviours

`func (o *AbilityV2) HasBehaviours() bool`

HasBehaviours returns a boolean if a field has been set.

### SetBehavioursNil

`func (o *AbilityV2) SetBehavioursNil(b bool)`

 SetBehavioursNil sets the value for Behaviours to be an explicit nil

### UnsetBehaviours
`func (o *AbilityV2) UnsetBehaviours()`

UnsetBehaviours ensures that no value is present for Behaviours, not even an explicit nil
### GetDescription

`func (o *AbilityV2) GetDescription() AbilityDescriptionV2`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *AbilityV2) GetDescriptionOk() (*AbilityDescriptionV2, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *AbilityV2) SetDescription(v AbilityDescriptionV2)`

SetDescription sets Description field to given value.


### GetTooltipDetails

`func (o *AbilityV2) GetTooltipDetails() AbilityTooltipDetailsV2`

GetTooltipDetails returns the TooltipDetails field if non-nil, zero value otherwise.

### GetTooltipDetailsOk

`func (o *AbilityV2) GetTooltipDetailsOk() (*AbilityTooltipDetailsV2, bool)`

GetTooltipDetailsOk returns a tuple with the TooltipDetails field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipDetails

`func (o *AbilityV2) SetTooltipDetails(v AbilityTooltipDetailsV2)`

SetTooltipDetails sets TooltipDetails field to given value.

### HasTooltipDetails

`func (o *AbilityV2) HasTooltipDetails() bool`

HasTooltipDetails returns a boolean if a field has been set.

### SetTooltipDetailsNil

`func (o *AbilityV2) SetTooltipDetailsNil(b bool)`

 SetTooltipDetailsNil sets the value for TooltipDetails to be an explicit nil

### UnsetTooltipDetails
`func (o *AbilityV2) UnsetTooltipDetails()`

UnsetTooltipDetails ensures that no value is present for TooltipDetails, not even an explicit nil
### GetUpgrades

`func (o *AbilityV2) GetUpgrades() []RawAbilityUpgradeV2`

GetUpgrades returns the Upgrades field if non-nil, zero value otherwise.

### GetUpgradesOk

`func (o *AbilityV2) GetUpgradesOk() (*[]RawAbilityUpgradeV2, bool)`

GetUpgradesOk returns a tuple with the Upgrades field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpgrades

`func (o *AbilityV2) SetUpgrades(v []RawAbilityUpgradeV2)`

SetUpgrades sets Upgrades field to given value.

### HasUpgrades

`func (o *AbilityV2) HasUpgrades() bool`

HasUpgrades returns a boolean if a field has been set.

### SetUpgradesNil

`func (o *AbilityV2) SetUpgradesNil(b bool)`

 SetUpgradesNil sets the value for Upgrades to be an explicit nil

### UnsetUpgrades
`func (o *AbilityV2) UnsetUpgrades()`

UnsetUpgrades ensures that no value is present for Upgrades, not even an explicit nil
### GetAbilityType

`func (o *AbilityV2) GetAbilityType() AbilityTypeV2`

GetAbilityType returns the AbilityType field if non-nil, zero value otherwise.

### GetAbilityTypeOk

`func (o *AbilityV2) GetAbilityTypeOk() (*AbilityTypeV2, bool)`

GetAbilityTypeOk returns a tuple with the AbilityType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAbilityType

`func (o *AbilityV2) SetAbilityType(v AbilityTypeV2)`

SetAbilityType sets AbilityType field to given value.

### HasAbilityType

`func (o *AbilityV2) HasAbilityType() bool`

HasAbilityType returns a boolean if a field has been set.

### SetAbilityTypeNil

`func (o *AbilityV2) SetAbilityTypeNil(b bool)`

 SetAbilityTypeNil sets the value for AbilityType to be an explicit nil

### UnsetAbilityType
`func (o *AbilityV2) UnsetAbilityType()`

UnsetAbilityType ensures that no value is present for AbilityType, not even an explicit nil
### GetBossDamageScale

`func (o *AbilityV2) GetBossDamageScale() float32`

GetBossDamageScale returns the BossDamageScale field if non-nil, zero value otherwise.

### GetBossDamageScaleOk

`func (o *AbilityV2) GetBossDamageScaleOk() (*float32, bool)`

GetBossDamageScaleOk returns a tuple with the BossDamageScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBossDamageScale

`func (o *AbilityV2) SetBossDamageScale(v float32)`

SetBossDamageScale sets BossDamageScale field to given value.

### HasBossDamageScale

`func (o *AbilityV2) HasBossDamageScale() bool`

HasBossDamageScale returns a boolean if a field has been set.

### SetBossDamageScaleNil

`func (o *AbilityV2) SetBossDamageScaleNil(b bool)`

 SetBossDamageScaleNil sets the value for BossDamageScale to be an explicit nil

### UnsetBossDamageScale
`func (o *AbilityV2) UnsetBossDamageScale()`

UnsetBossDamageScale ensures that no value is present for BossDamageScale, not even an explicit nil
### GetDependantAbilities

`func (o *AbilityV2) GetDependantAbilities() []string`

GetDependantAbilities returns the DependantAbilities field if non-nil, zero value otherwise.

### GetDependantAbilitiesOk

`func (o *AbilityV2) GetDependantAbilitiesOk() (*[]string, bool)`

GetDependantAbilitiesOk returns a tuple with the DependantAbilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependantAbilities

`func (o *AbilityV2) SetDependantAbilities(v []string)`

SetDependantAbilities sets DependantAbilities field to given value.

### HasDependantAbilities

`func (o *AbilityV2) HasDependantAbilities() bool`

HasDependantAbilities returns a boolean if a field has been set.

### SetDependantAbilitiesNil

`func (o *AbilityV2) SetDependantAbilitiesNil(b bool)`

 SetDependantAbilitiesNil sets the value for DependantAbilities to be an explicit nil

### UnsetDependantAbilities
`func (o *AbilityV2) UnsetDependantAbilities()`

UnsetDependantAbilities ensures that no value is present for DependantAbilities, not even an explicit nil
### GetVideos

`func (o *AbilityV2) GetVideos() AbilityVideosV2`

GetVideos returns the Videos field if non-nil, zero value otherwise.

### GetVideosOk

`func (o *AbilityV2) GetVideosOk() (*AbilityVideosV2, bool)`

GetVideosOk returns a tuple with the Videos field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVideos

`func (o *AbilityV2) SetVideos(v AbilityVideosV2)`

SetVideos sets Videos field to given value.

### HasVideos

`func (o *AbilityV2) HasVideos() bool`

HasVideos returns a boolean if a field has been set.

### SetVideosNil

`func (o *AbilityV2) SetVideosNil(b bool)`

 SetVideosNil sets the value for Videos to be an explicit nil

### UnsetVideos
`func (o *AbilityV2) UnsetVideos()`

UnsetVideos ensures that no value is present for Videos, not even an explicit nil
### GetDependentAbilities

`func (o *AbilityV2) GetDependentAbilities() map[string]DependantAbilities`

GetDependentAbilities returns the DependentAbilities field if non-nil, zero value otherwise.

### GetDependentAbilitiesOk

`func (o *AbilityV2) GetDependentAbilitiesOk() (*map[string]DependantAbilities, bool)`

GetDependentAbilitiesOk returns a tuple with the DependentAbilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependentAbilities

`func (o *AbilityV2) SetDependentAbilities(v map[string]DependantAbilities)`

SetDependentAbilities sets DependentAbilities field to given value.

### HasDependentAbilities

`func (o *AbilityV2) HasDependentAbilities() bool`

HasDependentAbilities returns a boolean if a field has been set.

### SetDependentAbilitiesNil

`func (o *AbilityV2) SetDependentAbilitiesNil(b bool)`

 SetDependentAbilitiesNil sets the value for DependentAbilities to be an explicit nil

### UnsetDependentAbilities
`func (o *AbilityV2) UnsetDependentAbilities()`

UnsetDependentAbilities ensures that no value is present for DependentAbilities, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


