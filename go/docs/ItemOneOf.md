# ItemOneOf

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AbilityType** | Pointer to [**NullableAbilityType**](AbilityType.md) |  | [optional] 
**Behaviours** | Pointer to **[]string** |  | [optional] 
**BossDamageScale** | Pointer to **NullableFloat64** |  | [optional] 
**ClassName** | **string** |  | 
**DependantAbilities** | Pointer to **[]string** |  | [optional] 
**DependentAbilities** | Pointer to [**map[string]DependantAbilities**](DependantAbilities.md) | Abilities this one depends on. Entries whose ability has no data are left out. | [optional] 
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
**UpdateTime** | Pointer to **NullableInt64** |  | [optional] 
**Upgrades** | Pointer to [**[]RawAbilityUpgrade**](RawAbilityUpgrade.md) |  | [optional] 
**Videos** | Pointer to [**NullableAbilityVideos**](AbilityVideos.md) |  | [optional] 
**WeaponInfo** | Pointer to [**NullableRawItemWeaponInfoInner**](RawItemWeaponInfoInner.md) |  | [optional] 
**Type** | **string** |  | 

## Methods

### NewItemOneOf

`func NewItemOneOf(className string, description AbilityDescription, id int32, name string, type_ string, ) *ItemOneOf`

NewItemOneOf instantiates a new ItemOneOf object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewItemOneOfWithDefaults

`func NewItemOneOfWithDefaults() *ItemOneOf`

NewItemOneOfWithDefaults instantiates a new ItemOneOf object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAbilityType

`func (o *ItemOneOf) GetAbilityType() AbilityType`

GetAbilityType returns the AbilityType field if non-nil, zero value otherwise.

### GetAbilityTypeOk

`func (o *ItemOneOf) GetAbilityTypeOk() (*AbilityType, bool)`

GetAbilityTypeOk returns a tuple with the AbilityType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAbilityType

`func (o *ItemOneOf) SetAbilityType(v AbilityType)`

SetAbilityType sets AbilityType field to given value.

### HasAbilityType

`func (o *ItemOneOf) HasAbilityType() bool`

HasAbilityType returns a boolean if a field has been set.

### SetAbilityTypeNil

`func (o *ItemOneOf) SetAbilityTypeNil(b bool)`

 SetAbilityTypeNil sets the value for AbilityType to be an explicit nil

### UnsetAbilityType
`func (o *ItemOneOf) UnsetAbilityType()`

UnsetAbilityType ensures that no value is present for AbilityType, not even an explicit nil
### GetBehaviours

`func (o *ItemOneOf) GetBehaviours() []string`

GetBehaviours returns the Behaviours field if non-nil, zero value otherwise.

### GetBehavioursOk

`func (o *ItemOneOf) GetBehavioursOk() (*[]string, bool)`

GetBehavioursOk returns a tuple with the Behaviours field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBehaviours

`func (o *ItemOneOf) SetBehaviours(v []string)`

SetBehaviours sets Behaviours field to given value.

### HasBehaviours

`func (o *ItemOneOf) HasBehaviours() bool`

HasBehaviours returns a boolean if a field has been set.

### SetBehavioursNil

`func (o *ItemOneOf) SetBehavioursNil(b bool)`

 SetBehavioursNil sets the value for Behaviours to be an explicit nil

### UnsetBehaviours
`func (o *ItemOneOf) UnsetBehaviours()`

UnsetBehaviours ensures that no value is present for Behaviours, not even an explicit nil
### GetBossDamageScale

`func (o *ItemOneOf) GetBossDamageScale() float64`

GetBossDamageScale returns the BossDamageScale field if non-nil, zero value otherwise.

### GetBossDamageScaleOk

`func (o *ItemOneOf) GetBossDamageScaleOk() (*float64, bool)`

GetBossDamageScaleOk returns a tuple with the BossDamageScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBossDamageScale

`func (o *ItemOneOf) SetBossDamageScale(v float64)`

SetBossDamageScale sets BossDamageScale field to given value.

### HasBossDamageScale

`func (o *ItemOneOf) HasBossDamageScale() bool`

HasBossDamageScale returns a boolean if a field has been set.

### SetBossDamageScaleNil

`func (o *ItemOneOf) SetBossDamageScaleNil(b bool)`

 SetBossDamageScaleNil sets the value for BossDamageScale to be an explicit nil

### UnsetBossDamageScale
`func (o *ItemOneOf) UnsetBossDamageScale()`

UnsetBossDamageScale ensures that no value is present for BossDamageScale, not even an explicit nil
### GetClassName

`func (o *ItemOneOf) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *ItemOneOf) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *ItemOneOf) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetDependantAbilities

`func (o *ItemOneOf) GetDependantAbilities() []string`

GetDependantAbilities returns the DependantAbilities field if non-nil, zero value otherwise.

### GetDependantAbilitiesOk

`func (o *ItemOneOf) GetDependantAbilitiesOk() (*[]string, bool)`

GetDependantAbilitiesOk returns a tuple with the DependantAbilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependantAbilities

`func (o *ItemOneOf) SetDependantAbilities(v []string)`

SetDependantAbilities sets DependantAbilities field to given value.

### HasDependantAbilities

`func (o *ItemOneOf) HasDependantAbilities() bool`

HasDependantAbilities returns a boolean if a field has been set.

### SetDependantAbilitiesNil

`func (o *ItemOneOf) SetDependantAbilitiesNil(b bool)`

 SetDependantAbilitiesNil sets the value for DependantAbilities to be an explicit nil

### UnsetDependantAbilities
`func (o *ItemOneOf) UnsetDependantAbilities()`

UnsetDependantAbilities ensures that no value is present for DependantAbilities, not even an explicit nil
### GetDependentAbilities

`func (o *ItemOneOf) GetDependentAbilities() map[string]DependantAbilities`

GetDependentAbilities returns the DependentAbilities field if non-nil, zero value otherwise.

### GetDependentAbilitiesOk

`func (o *ItemOneOf) GetDependentAbilitiesOk() (*map[string]DependantAbilities, bool)`

GetDependentAbilitiesOk returns a tuple with the DependentAbilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependentAbilities

`func (o *ItemOneOf) SetDependentAbilities(v map[string]DependantAbilities)`

SetDependentAbilities sets DependentAbilities field to given value.

### HasDependentAbilities

`func (o *ItemOneOf) HasDependentAbilities() bool`

HasDependentAbilities returns a boolean if a field has been set.

### SetDependentAbilitiesNil

`func (o *ItemOneOf) SetDependentAbilitiesNil(b bool)`

 SetDependentAbilitiesNil sets the value for DependentAbilities to be an explicit nil

### UnsetDependentAbilities
`func (o *ItemOneOf) UnsetDependentAbilities()`

UnsetDependentAbilities ensures that no value is present for DependentAbilities, not even an explicit nil
### GetDescription

`func (o *ItemOneOf) GetDescription() AbilityDescription`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ItemOneOf) GetDescriptionOk() (*AbilityDescription, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ItemOneOf) SetDescription(v AbilityDescription)`

SetDescription sets Description field to given value.


### GetGrantAmmoOnCast

`func (o *ItemOneOf) GetGrantAmmoOnCast() bool`

GetGrantAmmoOnCast returns the GrantAmmoOnCast field if non-nil, zero value otherwise.

### GetGrantAmmoOnCastOk

`func (o *ItemOneOf) GetGrantAmmoOnCastOk() (*bool, bool)`

GetGrantAmmoOnCastOk returns a tuple with the GrantAmmoOnCast field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGrantAmmoOnCast

`func (o *ItemOneOf) SetGrantAmmoOnCast(v bool)`

SetGrantAmmoOnCast sets GrantAmmoOnCast field to given value.

### HasGrantAmmoOnCast

`func (o *ItemOneOf) HasGrantAmmoOnCast() bool`

HasGrantAmmoOnCast returns a boolean if a field has been set.

### SetGrantAmmoOnCastNil

`func (o *ItemOneOf) SetGrantAmmoOnCastNil(b bool)`

 SetGrantAmmoOnCastNil sets the value for GrantAmmoOnCast to be an explicit nil

### UnsetGrantAmmoOnCast
`func (o *ItemOneOf) UnsetGrantAmmoOnCast()`

UnsetGrantAmmoOnCast ensures that no value is present for GrantAmmoOnCast, not even an explicit nil
### GetHero

`func (o *ItemOneOf) GetHero() int32`

GetHero returns the Hero field if non-nil, zero value otherwise.

### GetHeroOk

`func (o *ItemOneOf) GetHeroOk() (*int32, bool)`

GetHeroOk returns a tuple with the Hero field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHero

`func (o *ItemOneOf) SetHero(v int32)`

SetHero sets Hero field to given value.

### HasHero

`func (o *ItemOneOf) HasHero() bool`

HasHero returns a boolean if a field has been set.

### SetHeroNil

`func (o *ItemOneOf) SetHeroNil(b bool)`

 SetHeroNil sets the value for Hero to be an explicit nil

### UnsetHero
`func (o *ItemOneOf) UnsetHero()`

UnsetHero ensures that no value is present for Hero, not even an explicit nil
### GetHeroes

`func (o *ItemOneOf) GetHeroes() []int32`

GetHeroes returns the Heroes field if non-nil, zero value otherwise.

### GetHeroesOk

`func (o *ItemOneOf) GetHeroesOk() (*[]int32, bool)`

GetHeroesOk returns a tuple with the Heroes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroes

`func (o *ItemOneOf) SetHeroes(v []int32)`

SetHeroes sets Heroes field to given value.

### HasHeroes

`func (o *ItemOneOf) HasHeroes() bool`

HasHeroes returns a boolean if a field has been set.

### SetHeroesNil

`func (o *ItemOneOf) SetHeroesNil(b bool)`

 SetHeroesNil sets the value for Heroes to be an explicit nil

### UnsetHeroes
`func (o *ItemOneOf) UnsetHeroes()`

UnsetHeroes ensures that no value is present for Heroes, not even an explicit nil
### GetId

`func (o *ItemOneOf) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ItemOneOf) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ItemOneOf) SetId(v int32)`

SetId sets Id field to given value.


### GetImage

`func (o *ItemOneOf) GetImage() string`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *ItemOneOf) GetImageOk() (*string, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *ItemOneOf) SetImage(v string)`

SetImage sets Image field to given value.

### HasImage

`func (o *ItemOneOf) HasImage() bool`

HasImage returns a boolean if a field has been set.

### SetImageNil

`func (o *ItemOneOf) SetImageNil(b bool)`

 SetImageNil sets the value for Image to be an explicit nil

### UnsetImage
`func (o *ItemOneOf) UnsetImage()`

UnsetImage ensures that no value is present for Image, not even an explicit nil
### GetImageWebp

`func (o *ItemOneOf) GetImageWebp() string`

GetImageWebp returns the ImageWebp field if non-nil, zero value otherwise.

### GetImageWebpOk

`func (o *ItemOneOf) GetImageWebpOk() (*string, bool)`

GetImageWebpOk returns a tuple with the ImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImageWebp

`func (o *ItemOneOf) SetImageWebp(v string)`

SetImageWebp sets ImageWebp field to given value.

### HasImageWebp

`func (o *ItemOneOf) HasImageWebp() bool`

HasImageWebp returns a boolean if a field has been set.

### SetImageWebpNil

`func (o *ItemOneOf) SetImageWebpNil(b bool)`

 SetImageWebpNil sets the value for ImageWebp to be an explicit nil

### UnsetImageWebp
`func (o *ItemOneOf) UnsetImageWebp()`

UnsetImageWebp ensures that no value is present for ImageWebp, not even an explicit nil
### GetName

`func (o *ItemOneOf) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ItemOneOf) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ItemOneOf) SetName(v string)`

SetName sets Name field to given value.


### GetProperties

`func (o *ItemOneOf) GetProperties() map[string]ItemProperty`

GetProperties returns the Properties field if non-nil, zero value otherwise.

### GetPropertiesOk

`func (o *ItemOneOf) GetPropertiesOk() (*map[string]ItemProperty, bool)`

GetPropertiesOk returns a tuple with the Properties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperties

`func (o *ItemOneOf) SetProperties(v map[string]ItemProperty)`

SetProperties sets Properties field to given value.

### HasProperties

`func (o *ItemOneOf) HasProperties() bool`

HasProperties returns a boolean if a field has been set.

### SetPropertiesNil

`func (o *ItemOneOf) SetPropertiesNil(b bool)`

 SetPropertiesNil sets the value for Properties to be an explicit nil

### UnsetProperties
`func (o *ItemOneOf) UnsetProperties()`

UnsetProperties ensures that no value is present for Properties, not even an explicit nil
### GetStartTrained

`func (o *ItemOneOf) GetStartTrained() bool`

GetStartTrained returns the StartTrained field if non-nil, zero value otherwise.

### GetStartTrainedOk

`func (o *ItemOneOf) GetStartTrainedOk() (*bool, bool)`

GetStartTrainedOk returns a tuple with the StartTrained field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTrained

`func (o *ItemOneOf) SetStartTrained(v bool)`

SetStartTrained sets StartTrained field to given value.

### HasStartTrained

`func (o *ItemOneOf) HasStartTrained() bool`

HasStartTrained returns a boolean if a field has been set.

### SetStartTrainedNil

`func (o *ItemOneOf) SetStartTrainedNil(b bool)`

 SetStartTrainedNil sets the value for StartTrained to be an explicit nil

### UnsetStartTrained
`func (o *ItemOneOf) UnsetStartTrained()`

UnsetStartTrained ensures that no value is present for StartTrained, not even an explicit nil
### GetTooltipDetails

`func (o *ItemOneOf) GetTooltipDetails() AbilityTooltipDetails`

GetTooltipDetails returns the TooltipDetails field if non-nil, zero value otherwise.

### GetTooltipDetailsOk

`func (o *ItemOneOf) GetTooltipDetailsOk() (*AbilityTooltipDetails, bool)`

GetTooltipDetailsOk returns a tuple with the TooltipDetails field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipDetails

`func (o *ItemOneOf) SetTooltipDetails(v AbilityTooltipDetails)`

SetTooltipDetails sets TooltipDetails field to given value.

### HasTooltipDetails

`func (o *ItemOneOf) HasTooltipDetails() bool`

HasTooltipDetails returns a boolean if a field has been set.

### SetTooltipDetailsNil

`func (o *ItemOneOf) SetTooltipDetailsNil(b bool)`

 SetTooltipDetailsNil sets the value for TooltipDetails to be an explicit nil

### UnsetTooltipDetails
`func (o *ItemOneOf) UnsetTooltipDetails()`

UnsetTooltipDetails ensures that no value is present for TooltipDetails, not even an explicit nil
### GetUpdateTime

`func (o *ItemOneOf) GetUpdateTime() int64`

GetUpdateTime returns the UpdateTime field if non-nil, zero value otherwise.

### GetUpdateTimeOk

`func (o *ItemOneOf) GetUpdateTimeOk() (*int64, bool)`

GetUpdateTimeOk returns a tuple with the UpdateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateTime

`func (o *ItemOneOf) SetUpdateTime(v int64)`

SetUpdateTime sets UpdateTime field to given value.

### HasUpdateTime

`func (o *ItemOneOf) HasUpdateTime() bool`

HasUpdateTime returns a boolean if a field has been set.

### SetUpdateTimeNil

`func (o *ItemOneOf) SetUpdateTimeNil(b bool)`

 SetUpdateTimeNil sets the value for UpdateTime to be an explicit nil

### UnsetUpdateTime
`func (o *ItemOneOf) UnsetUpdateTime()`

UnsetUpdateTime ensures that no value is present for UpdateTime, not even an explicit nil
### GetUpgrades

`func (o *ItemOneOf) GetUpgrades() []RawAbilityUpgrade`

GetUpgrades returns the Upgrades field if non-nil, zero value otherwise.

### GetUpgradesOk

`func (o *ItemOneOf) GetUpgradesOk() (*[]RawAbilityUpgrade, bool)`

GetUpgradesOk returns a tuple with the Upgrades field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpgrades

`func (o *ItemOneOf) SetUpgrades(v []RawAbilityUpgrade)`

SetUpgrades sets Upgrades field to given value.

### HasUpgrades

`func (o *ItemOneOf) HasUpgrades() bool`

HasUpgrades returns a boolean if a field has been set.

### SetUpgradesNil

`func (o *ItemOneOf) SetUpgradesNil(b bool)`

 SetUpgradesNil sets the value for Upgrades to be an explicit nil

### UnsetUpgrades
`func (o *ItemOneOf) UnsetUpgrades()`

UnsetUpgrades ensures that no value is present for Upgrades, not even an explicit nil
### GetVideos

`func (o *ItemOneOf) GetVideos() AbilityVideos`

GetVideos returns the Videos field if non-nil, zero value otherwise.

### GetVideosOk

`func (o *ItemOneOf) GetVideosOk() (*AbilityVideos, bool)`

GetVideosOk returns a tuple with the Videos field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVideos

`func (o *ItemOneOf) SetVideos(v AbilityVideos)`

SetVideos sets Videos field to given value.

### HasVideos

`func (o *ItemOneOf) HasVideos() bool`

HasVideos returns a boolean if a field has been set.

### SetVideosNil

`func (o *ItemOneOf) SetVideosNil(b bool)`

 SetVideosNil sets the value for Videos to be an explicit nil

### UnsetVideos
`func (o *ItemOneOf) UnsetVideos()`

UnsetVideos ensures that no value is present for Videos, not even an explicit nil
### GetWeaponInfo

`func (o *ItemOneOf) GetWeaponInfo() RawItemWeaponInfoInner`

GetWeaponInfo returns the WeaponInfo field if non-nil, zero value otherwise.

### GetWeaponInfoOk

`func (o *ItemOneOf) GetWeaponInfoOk() (*RawItemWeaponInfoInner, bool)`

GetWeaponInfoOk returns a tuple with the WeaponInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponInfo

`func (o *ItemOneOf) SetWeaponInfo(v RawItemWeaponInfoInner)`

SetWeaponInfo sets WeaponInfo field to given value.

### HasWeaponInfo

`func (o *ItemOneOf) HasWeaponInfo() bool`

HasWeaponInfo returns a boolean if a field has been set.

### SetWeaponInfoNil

`func (o *ItemOneOf) SetWeaponInfoNil(b bool)`

 SetWeaponInfoNil sets the value for WeaponInfo to be an explicit nil

### UnsetWeaponInfo
`func (o *ItemOneOf) UnsetWeaponInfo()`

UnsetWeaponInfo ensures that no value is present for WeaponInfo, not even an explicit nil
### GetType

`func (o *ItemOneOf) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ItemOneOf) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ItemOneOf) SetType(v string)`

SetType sets Type field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


