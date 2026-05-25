# Weapon

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClassName** | **string** |  | 
**CrosshairCssClass** | Pointer to **NullableString** |  | [optional] 
**CustomCrosshairSettings** | Pointer to [**NullableRawCustomCrosshairSettings**](RawCustomCrosshairSettings.md) |  | [optional] 
**Hero** | Pointer to **NullableInt32** |  | [optional] 
**Heroes** | Pointer to **[]int32** |  | [optional] 
**Id** | **int32** |  | 
**Image** | Pointer to **NullableString** |  | [optional] 
**ImageWebp** | Pointer to **NullableString** |  | [optional] 
**Name** | **string** |  | 
**Properties** | Pointer to [**map[string]ItemProperty**](ItemProperty.md) |  | [optional] 
**StartTrained** | Pointer to **NullableBool** |  | [optional] 
**Type** | [**ItemType**](ItemType.md) |  | 
**UpdateTime** | Pointer to **NullableInt64** |  | [optional] 
**UseCustomCrosshairSettings** | Pointer to **NullableBool** |  | [optional] 
**WeaponInfo** | Pointer to [**NullableWeaponInfo**](WeaponInfo.md) |  | [optional] 

## Methods

### NewWeapon

`func NewWeapon(className string, id int32, name string, type_ ItemType, ) *Weapon`

NewWeapon instantiates a new Weapon object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWeaponWithDefaults

`func NewWeaponWithDefaults() *Weapon`

NewWeaponWithDefaults instantiates a new Weapon object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClassName

`func (o *Weapon) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *Weapon) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *Weapon) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetCrosshairCssClass

`func (o *Weapon) GetCrosshairCssClass() string`

GetCrosshairCssClass returns the CrosshairCssClass field if non-nil, zero value otherwise.

### GetCrosshairCssClassOk

`func (o *Weapon) GetCrosshairCssClassOk() (*string, bool)`

GetCrosshairCssClassOk returns a tuple with the CrosshairCssClass field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrosshairCssClass

`func (o *Weapon) SetCrosshairCssClass(v string)`

SetCrosshairCssClass sets CrosshairCssClass field to given value.

### HasCrosshairCssClass

`func (o *Weapon) HasCrosshairCssClass() bool`

HasCrosshairCssClass returns a boolean if a field has been set.

### SetCrosshairCssClassNil

`func (o *Weapon) SetCrosshairCssClassNil(b bool)`

 SetCrosshairCssClassNil sets the value for CrosshairCssClass to be an explicit nil

### UnsetCrosshairCssClass
`func (o *Weapon) UnsetCrosshairCssClass()`

UnsetCrosshairCssClass ensures that no value is present for CrosshairCssClass, not even an explicit nil
### GetCustomCrosshairSettings

`func (o *Weapon) GetCustomCrosshairSettings() RawCustomCrosshairSettings`

GetCustomCrosshairSettings returns the CustomCrosshairSettings field if non-nil, zero value otherwise.

### GetCustomCrosshairSettingsOk

`func (o *Weapon) GetCustomCrosshairSettingsOk() (*RawCustomCrosshairSettings, bool)`

GetCustomCrosshairSettingsOk returns a tuple with the CustomCrosshairSettings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomCrosshairSettings

`func (o *Weapon) SetCustomCrosshairSettings(v RawCustomCrosshairSettings)`

SetCustomCrosshairSettings sets CustomCrosshairSettings field to given value.

### HasCustomCrosshairSettings

`func (o *Weapon) HasCustomCrosshairSettings() bool`

HasCustomCrosshairSettings returns a boolean if a field has been set.

### SetCustomCrosshairSettingsNil

`func (o *Weapon) SetCustomCrosshairSettingsNil(b bool)`

 SetCustomCrosshairSettingsNil sets the value for CustomCrosshairSettings to be an explicit nil

### UnsetCustomCrosshairSettings
`func (o *Weapon) UnsetCustomCrosshairSettings()`

UnsetCustomCrosshairSettings ensures that no value is present for CustomCrosshairSettings, not even an explicit nil
### GetHero

`func (o *Weapon) GetHero() int32`

GetHero returns the Hero field if non-nil, zero value otherwise.

### GetHeroOk

`func (o *Weapon) GetHeroOk() (*int32, bool)`

GetHeroOk returns a tuple with the Hero field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHero

`func (o *Weapon) SetHero(v int32)`

SetHero sets Hero field to given value.

### HasHero

`func (o *Weapon) HasHero() bool`

HasHero returns a boolean if a field has been set.

### SetHeroNil

`func (o *Weapon) SetHeroNil(b bool)`

 SetHeroNil sets the value for Hero to be an explicit nil

### UnsetHero
`func (o *Weapon) UnsetHero()`

UnsetHero ensures that no value is present for Hero, not even an explicit nil
### GetHeroes

`func (o *Weapon) GetHeroes() []int32`

GetHeroes returns the Heroes field if non-nil, zero value otherwise.

### GetHeroesOk

`func (o *Weapon) GetHeroesOk() (*[]int32, bool)`

GetHeroesOk returns a tuple with the Heroes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroes

`func (o *Weapon) SetHeroes(v []int32)`

SetHeroes sets Heroes field to given value.

### HasHeroes

`func (o *Weapon) HasHeroes() bool`

HasHeroes returns a boolean if a field has been set.

### SetHeroesNil

`func (o *Weapon) SetHeroesNil(b bool)`

 SetHeroesNil sets the value for Heroes to be an explicit nil

### UnsetHeroes
`func (o *Weapon) UnsetHeroes()`

UnsetHeroes ensures that no value is present for Heroes, not even an explicit nil
### GetId

`func (o *Weapon) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Weapon) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Weapon) SetId(v int32)`

SetId sets Id field to given value.


### GetImage

`func (o *Weapon) GetImage() string`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *Weapon) GetImageOk() (*string, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *Weapon) SetImage(v string)`

SetImage sets Image field to given value.

### HasImage

`func (o *Weapon) HasImage() bool`

HasImage returns a boolean if a field has been set.

### SetImageNil

`func (o *Weapon) SetImageNil(b bool)`

 SetImageNil sets the value for Image to be an explicit nil

### UnsetImage
`func (o *Weapon) UnsetImage()`

UnsetImage ensures that no value is present for Image, not even an explicit nil
### GetImageWebp

`func (o *Weapon) GetImageWebp() string`

GetImageWebp returns the ImageWebp field if non-nil, zero value otherwise.

### GetImageWebpOk

`func (o *Weapon) GetImageWebpOk() (*string, bool)`

GetImageWebpOk returns a tuple with the ImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImageWebp

`func (o *Weapon) SetImageWebp(v string)`

SetImageWebp sets ImageWebp field to given value.

### HasImageWebp

`func (o *Weapon) HasImageWebp() bool`

HasImageWebp returns a boolean if a field has been set.

### SetImageWebpNil

`func (o *Weapon) SetImageWebpNil(b bool)`

 SetImageWebpNil sets the value for ImageWebp to be an explicit nil

### UnsetImageWebp
`func (o *Weapon) UnsetImageWebp()`

UnsetImageWebp ensures that no value is present for ImageWebp, not even an explicit nil
### GetName

`func (o *Weapon) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Weapon) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Weapon) SetName(v string)`

SetName sets Name field to given value.


### GetProperties

`func (o *Weapon) GetProperties() map[string]ItemProperty`

GetProperties returns the Properties field if non-nil, zero value otherwise.

### GetPropertiesOk

`func (o *Weapon) GetPropertiesOk() (*map[string]ItemProperty, bool)`

GetPropertiesOk returns a tuple with the Properties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperties

`func (o *Weapon) SetProperties(v map[string]ItemProperty)`

SetProperties sets Properties field to given value.

### HasProperties

`func (o *Weapon) HasProperties() bool`

HasProperties returns a boolean if a field has been set.

### GetStartTrained

`func (o *Weapon) GetStartTrained() bool`

GetStartTrained returns the StartTrained field if non-nil, zero value otherwise.

### GetStartTrainedOk

`func (o *Weapon) GetStartTrainedOk() (*bool, bool)`

GetStartTrainedOk returns a tuple with the StartTrained field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTrained

`func (o *Weapon) SetStartTrained(v bool)`

SetStartTrained sets StartTrained field to given value.

### HasStartTrained

`func (o *Weapon) HasStartTrained() bool`

HasStartTrained returns a boolean if a field has been set.

### SetStartTrainedNil

`func (o *Weapon) SetStartTrainedNil(b bool)`

 SetStartTrainedNil sets the value for StartTrained to be an explicit nil

### UnsetStartTrained
`func (o *Weapon) UnsetStartTrained()`

UnsetStartTrained ensures that no value is present for StartTrained, not even an explicit nil
### GetType

`func (o *Weapon) GetType() ItemType`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Weapon) GetTypeOk() (*ItemType, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Weapon) SetType(v ItemType)`

SetType sets Type field to given value.


### GetUpdateTime

`func (o *Weapon) GetUpdateTime() int64`

GetUpdateTime returns the UpdateTime field if non-nil, zero value otherwise.

### GetUpdateTimeOk

`func (o *Weapon) GetUpdateTimeOk() (*int64, bool)`

GetUpdateTimeOk returns a tuple with the UpdateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateTime

`func (o *Weapon) SetUpdateTime(v int64)`

SetUpdateTime sets UpdateTime field to given value.

### HasUpdateTime

`func (o *Weapon) HasUpdateTime() bool`

HasUpdateTime returns a boolean if a field has been set.

### SetUpdateTimeNil

`func (o *Weapon) SetUpdateTimeNil(b bool)`

 SetUpdateTimeNil sets the value for UpdateTime to be an explicit nil

### UnsetUpdateTime
`func (o *Weapon) UnsetUpdateTime()`

UnsetUpdateTime ensures that no value is present for UpdateTime, not even an explicit nil
### GetUseCustomCrosshairSettings

`func (o *Weapon) GetUseCustomCrosshairSettings() bool`

GetUseCustomCrosshairSettings returns the UseCustomCrosshairSettings field if non-nil, zero value otherwise.

### GetUseCustomCrosshairSettingsOk

`func (o *Weapon) GetUseCustomCrosshairSettingsOk() (*bool, bool)`

GetUseCustomCrosshairSettingsOk returns a tuple with the UseCustomCrosshairSettings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUseCustomCrosshairSettings

`func (o *Weapon) SetUseCustomCrosshairSettings(v bool)`

SetUseCustomCrosshairSettings sets UseCustomCrosshairSettings field to given value.

### HasUseCustomCrosshairSettings

`func (o *Weapon) HasUseCustomCrosshairSettings() bool`

HasUseCustomCrosshairSettings returns a boolean if a field has been set.

### SetUseCustomCrosshairSettingsNil

`func (o *Weapon) SetUseCustomCrosshairSettingsNil(b bool)`

 SetUseCustomCrosshairSettingsNil sets the value for UseCustomCrosshairSettings to be an explicit nil

### UnsetUseCustomCrosshairSettings
`func (o *Weapon) UnsetUseCustomCrosshairSettings()`

UnsetUseCustomCrosshairSettings ensures that no value is present for UseCustomCrosshairSettings, not even an explicit nil
### GetWeaponInfo

`func (o *Weapon) GetWeaponInfo() WeaponInfo`

GetWeaponInfo returns the WeaponInfo field if non-nil, zero value otherwise.

### GetWeaponInfoOk

`func (o *Weapon) GetWeaponInfoOk() (*WeaponInfo, bool)`

GetWeaponInfoOk returns a tuple with the WeaponInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponInfo

`func (o *Weapon) SetWeaponInfo(v WeaponInfo)`

SetWeaponInfo sets WeaponInfo field to given value.

### HasWeaponInfo

`func (o *Weapon) HasWeaponInfo() bool`

HasWeaponInfo returns a boolean if a field has been set.

### SetWeaponInfoNil

`func (o *Weapon) SetWeaponInfoNil(b bool)`

 SetWeaponInfoNil sets the value for WeaponInfo to be an explicit nil

### UnsetWeaponInfo
`func (o *Weapon) UnsetWeaponInfo()`

UnsetWeaponInfo ensures that no value is present for WeaponInfo, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


