# ItemOneOf1

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
**UpdateTime** | Pointer to **NullableInt64** |  | [optional] 
**UseCustomCrosshairSettings** | Pointer to **NullableBool** |  | [optional] 
**WeaponInfo** | Pointer to [**NullableWeaponInfo**](WeaponInfo.md) |  | [optional] 
**Type** | **string** |  | 

## Methods

### NewItemOneOf1

`func NewItemOneOf1(className string, id int32, name string, type_ string, ) *ItemOneOf1`

NewItemOneOf1 instantiates a new ItemOneOf1 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewItemOneOf1WithDefaults

`func NewItemOneOf1WithDefaults() *ItemOneOf1`

NewItemOneOf1WithDefaults instantiates a new ItemOneOf1 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClassName

`func (o *ItemOneOf1) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *ItemOneOf1) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *ItemOneOf1) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetCrosshairCssClass

`func (o *ItemOneOf1) GetCrosshairCssClass() string`

GetCrosshairCssClass returns the CrosshairCssClass field if non-nil, zero value otherwise.

### GetCrosshairCssClassOk

`func (o *ItemOneOf1) GetCrosshairCssClassOk() (*string, bool)`

GetCrosshairCssClassOk returns a tuple with the CrosshairCssClass field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrosshairCssClass

`func (o *ItemOneOf1) SetCrosshairCssClass(v string)`

SetCrosshairCssClass sets CrosshairCssClass field to given value.

### HasCrosshairCssClass

`func (o *ItemOneOf1) HasCrosshairCssClass() bool`

HasCrosshairCssClass returns a boolean if a field has been set.

### SetCrosshairCssClassNil

`func (o *ItemOneOf1) SetCrosshairCssClassNil(b bool)`

 SetCrosshairCssClassNil sets the value for CrosshairCssClass to be an explicit nil

### UnsetCrosshairCssClass
`func (o *ItemOneOf1) UnsetCrosshairCssClass()`

UnsetCrosshairCssClass ensures that no value is present for CrosshairCssClass, not even an explicit nil
### GetCustomCrosshairSettings

`func (o *ItemOneOf1) GetCustomCrosshairSettings() RawCustomCrosshairSettings`

GetCustomCrosshairSettings returns the CustomCrosshairSettings field if non-nil, zero value otherwise.

### GetCustomCrosshairSettingsOk

`func (o *ItemOneOf1) GetCustomCrosshairSettingsOk() (*RawCustomCrosshairSettings, bool)`

GetCustomCrosshairSettingsOk returns a tuple with the CustomCrosshairSettings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomCrosshairSettings

`func (o *ItemOneOf1) SetCustomCrosshairSettings(v RawCustomCrosshairSettings)`

SetCustomCrosshairSettings sets CustomCrosshairSettings field to given value.

### HasCustomCrosshairSettings

`func (o *ItemOneOf1) HasCustomCrosshairSettings() bool`

HasCustomCrosshairSettings returns a boolean if a field has been set.

### SetCustomCrosshairSettingsNil

`func (o *ItemOneOf1) SetCustomCrosshairSettingsNil(b bool)`

 SetCustomCrosshairSettingsNil sets the value for CustomCrosshairSettings to be an explicit nil

### UnsetCustomCrosshairSettings
`func (o *ItemOneOf1) UnsetCustomCrosshairSettings()`

UnsetCustomCrosshairSettings ensures that no value is present for CustomCrosshairSettings, not even an explicit nil
### GetHero

`func (o *ItemOneOf1) GetHero() int32`

GetHero returns the Hero field if non-nil, zero value otherwise.

### GetHeroOk

`func (o *ItemOneOf1) GetHeroOk() (*int32, bool)`

GetHeroOk returns a tuple with the Hero field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHero

`func (o *ItemOneOf1) SetHero(v int32)`

SetHero sets Hero field to given value.

### HasHero

`func (o *ItemOneOf1) HasHero() bool`

HasHero returns a boolean if a field has been set.

### SetHeroNil

`func (o *ItemOneOf1) SetHeroNil(b bool)`

 SetHeroNil sets the value for Hero to be an explicit nil

### UnsetHero
`func (o *ItemOneOf1) UnsetHero()`

UnsetHero ensures that no value is present for Hero, not even an explicit nil
### GetHeroes

`func (o *ItemOneOf1) GetHeroes() []int32`

GetHeroes returns the Heroes field if non-nil, zero value otherwise.

### GetHeroesOk

`func (o *ItemOneOf1) GetHeroesOk() (*[]int32, bool)`

GetHeroesOk returns a tuple with the Heroes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroes

`func (o *ItemOneOf1) SetHeroes(v []int32)`

SetHeroes sets Heroes field to given value.

### HasHeroes

`func (o *ItemOneOf1) HasHeroes() bool`

HasHeroes returns a boolean if a field has been set.

### SetHeroesNil

`func (o *ItemOneOf1) SetHeroesNil(b bool)`

 SetHeroesNil sets the value for Heroes to be an explicit nil

### UnsetHeroes
`func (o *ItemOneOf1) UnsetHeroes()`

UnsetHeroes ensures that no value is present for Heroes, not even an explicit nil
### GetId

`func (o *ItemOneOf1) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ItemOneOf1) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ItemOneOf1) SetId(v int32)`

SetId sets Id field to given value.


### GetImage

`func (o *ItemOneOf1) GetImage() string`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *ItemOneOf1) GetImageOk() (*string, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *ItemOneOf1) SetImage(v string)`

SetImage sets Image field to given value.

### HasImage

`func (o *ItemOneOf1) HasImage() bool`

HasImage returns a boolean if a field has been set.

### SetImageNil

`func (o *ItemOneOf1) SetImageNil(b bool)`

 SetImageNil sets the value for Image to be an explicit nil

### UnsetImage
`func (o *ItemOneOf1) UnsetImage()`

UnsetImage ensures that no value is present for Image, not even an explicit nil
### GetImageWebp

`func (o *ItemOneOf1) GetImageWebp() string`

GetImageWebp returns the ImageWebp field if non-nil, zero value otherwise.

### GetImageWebpOk

`func (o *ItemOneOf1) GetImageWebpOk() (*string, bool)`

GetImageWebpOk returns a tuple with the ImageWebp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImageWebp

`func (o *ItemOneOf1) SetImageWebp(v string)`

SetImageWebp sets ImageWebp field to given value.

### HasImageWebp

`func (o *ItemOneOf1) HasImageWebp() bool`

HasImageWebp returns a boolean if a field has been set.

### SetImageWebpNil

`func (o *ItemOneOf1) SetImageWebpNil(b bool)`

 SetImageWebpNil sets the value for ImageWebp to be an explicit nil

### UnsetImageWebp
`func (o *ItemOneOf1) UnsetImageWebp()`

UnsetImageWebp ensures that no value is present for ImageWebp, not even an explicit nil
### GetName

`func (o *ItemOneOf1) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ItemOneOf1) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ItemOneOf1) SetName(v string)`

SetName sets Name field to given value.


### GetProperties

`func (o *ItemOneOf1) GetProperties() map[string]ItemProperty`

GetProperties returns the Properties field if non-nil, zero value otherwise.

### GetPropertiesOk

`func (o *ItemOneOf1) GetPropertiesOk() (*map[string]ItemProperty, bool)`

GetPropertiesOk returns a tuple with the Properties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperties

`func (o *ItemOneOf1) SetProperties(v map[string]ItemProperty)`

SetProperties sets Properties field to given value.

### HasProperties

`func (o *ItemOneOf1) HasProperties() bool`

HasProperties returns a boolean if a field has been set.

### SetPropertiesNil

`func (o *ItemOneOf1) SetPropertiesNil(b bool)`

 SetPropertiesNil sets the value for Properties to be an explicit nil

### UnsetProperties
`func (o *ItemOneOf1) UnsetProperties()`

UnsetProperties ensures that no value is present for Properties, not even an explicit nil
### GetStartTrained

`func (o *ItemOneOf1) GetStartTrained() bool`

GetStartTrained returns the StartTrained field if non-nil, zero value otherwise.

### GetStartTrainedOk

`func (o *ItemOneOf1) GetStartTrainedOk() (*bool, bool)`

GetStartTrainedOk returns a tuple with the StartTrained field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTrained

`func (o *ItemOneOf1) SetStartTrained(v bool)`

SetStartTrained sets StartTrained field to given value.

### HasStartTrained

`func (o *ItemOneOf1) HasStartTrained() bool`

HasStartTrained returns a boolean if a field has been set.

### SetStartTrainedNil

`func (o *ItemOneOf1) SetStartTrainedNil(b bool)`

 SetStartTrainedNil sets the value for StartTrained to be an explicit nil

### UnsetStartTrained
`func (o *ItemOneOf1) UnsetStartTrained()`

UnsetStartTrained ensures that no value is present for StartTrained, not even an explicit nil
### GetUpdateTime

`func (o *ItemOneOf1) GetUpdateTime() int64`

GetUpdateTime returns the UpdateTime field if non-nil, zero value otherwise.

### GetUpdateTimeOk

`func (o *ItemOneOf1) GetUpdateTimeOk() (*int64, bool)`

GetUpdateTimeOk returns a tuple with the UpdateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateTime

`func (o *ItemOneOf1) SetUpdateTime(v int64)`

SetUpdateTime sets UpdateTime field to given value.

### HasUpdateTime

`func (o *ItemOneOf1) HasUpdateTime() bool`

HasUpdateTime returns a boolean if a field has been set.

### SetUpdateTimeNil

`func (o *ItemOneOf1) SetUpdateTimeNil(b bool)`

 SetUpdateTimeNil sets the value for UpdateTime to be an explicit nil

### UnsetUpdateTime
`func (o *ItemOneOf1) UnsetUpdateTime()`

UnsetUpdateTime ensures that no value is present for UpdateTime, not even an explicit nil
### GetUseCustomCrosshairSettings

`func (o *ItemOneOf1) GetUseCustomCrosshairSettings() bool`

GetUseCustomCrosshairSettings returns the UseCustomCrosshairSettings field if non-nil, zero value otherwise.

### GetUseCustomCrosshairSettingsOk

`func (o *ItemOneOf1) GetUseCustomCrosshairSettingsOk() (*bool, bool)`

GetUseCustomCrosshairSettingsOk returns a tuple with the UseCustomCrosshairSettings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUseCustomCrosshairSettings

`func (o *ItemOneOf1) SetUseCustomCrosshairSettings(v bool)`

SetUseCustomCrosshairSettings sets UseCustomCrosshairSettings field to given value.

### HasUseCustomCrosshairSettings

`func (o *ItemOneOf1) HasUseCustomCrosshairSettings() bool`

HasUseCustomCrosshairSettings returns a boolean if a field has been set.

### SetUseCustomCrosshairSettingsNil

`func (o *ItemOneOf1) SetUseCustomCrosshairSettingsNil(b bool)`

 SetUseCustomCrosshairSettingsNil sets the value for UseCustomCrosshairSettings to be an explicit nil

### UnsetUseCustomCrosshairSettings
`func (o *ItemOneOf1) UnsetUseCustomCrosshairSettings()`

UnsetUseCustomCrosshairSettings ensures that no value is present for UseCustomCrosshairSettings, not even an explicit nil
### GetWeaponInfo

`func (o *ItemOneOf1) GetWeaponInfo() WeaponInfo`

GetWeaponInfo returns the WeaponInfo field if non-nil, zero value otherwise.

### GetWeaponInfoOk

`func (o *ItemOneOf1) GetWeaponInfoOk() (*WeaponInfo, bool)`

GetWeaponInfoOk returns a tuple with the WeaponInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponInfo

`func (o *ItemOneOf1) SetWeaponInfo(v WeaponInfo)`

SetWeaponInfo sets WeaponInfo field to given value.

### HasWeaponInfo

`func (o *ItemOneOf1) HasWeaponInfo() bool`

HasWeaponInfo returns a boolean if a field has been set.

### SetWeaponInfoNil

`func (o *ItemOneOf1) SetWeaponInfoNil(b bool)`

 SetWeaponInfoNil sets the value for WeaponInfo to be an explicit nil

### UnsetWeaponInfo
`func (o *ItemOneOf1) UnsetWeaponInfo()`

UnsetWeaponInfo ensures that no value is present for WeaponInfo, not even an explicit nil
### GetType

`func (o *ItemOneOf1) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ItemOneOf1) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ItemOneOf1) SetType(v string)`

SetType sets Type field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


