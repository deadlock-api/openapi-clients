# RawAbilityV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClassName** | **string** |  | 
**StartTrained** | Pointer to **NullableBool** |  | [optional] 
**Image** | Pointer to **NullableString** |  | [optional] 
**UpdateTime** | Pointer to **NullableInt32** |  | [optional] 
**Properties** | Pointer to [**map[string]RawItemPropertyV2**](RawItemPropertyV2.md) |  | [optional] 
**WeaponInfo** | Pointer to [**NullableRawItemWeaponInfoV2**](RawItemWeaponInfoV2.md) |  | [optional] 
**CssClass** | Pointer to **NullableString** |  | [optional] 
**Type** | Pointer to **string** |  | [optional] [default to "ability"]
**BehaviourBits** | Pointer to **NullableString** |  | [optional] 
**Upgrades** | [**[]RawAbilityUpgradeV2**](RawAbilityUpgradeV2.md) |  | 
**AbilityType** | Pointer to [**NullableAbilityTypeV2**](AbilityTypeV2.md) |  | [optional] 
**BossDamageScale** | Pointer to **NullableFloat32** |  | [optional] 
**DependantAbilities** | Pointer to **[]string** |  | [optional] 
**Video** | Pointer to **NullableString** |  | [optional] 
**TooltipDetails** | Pointer to [**NullableRawAbilityV2TooltipDetails**](RawAbilityV2TooltipDetails.md) |  | [optional] 

## Methods

### NewRawAbilityV2

`func NewRawAbilityV2(className string, upgrades []RawAbilityUpgradeV2, ) *RawAbilityV2`

NewRawAbilityV2 instantiates a new RawAbilityV2 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRawAbilityV2WithDefaults

`func NewRawAbilityV2WithDefaults() *RawAbilityV2`

NewRawAbilityV2WithDefaults instantiates a new RawAbilityV2 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClassName

`func (o *RawAbilityV2) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *RawAbilityV2) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *RawAbilityV2) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetStartTrained

`func (o *RawAbilityV2) GetStartTrained() bool`

GetStartTrained returns the StartTrained field if non-nil, zero value otherwise.

### GetStartTrainedOk

`func (o *RawAbilityV2) GetStartTrainedOk() (*bool, bool)`

GetStartTrainedOk returns a tuple with the StartTrained field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTrained

`func (o *RawAbilityV2) SetStartTrained(v bool)`

SetStartTrained sets StartTrained field to given value.

### HasStartTrained

`func (o *RawAbilityV2) HasStartTrained() bool`

HasStartTrained returns a boolean if a field has been set.

### SetStartTrainedNil

`func (o *RawAbilityV2) SetStartTrainedNil(b bool)`

 SetStartTrainedNil sets the value for StartTrained to be an explicit nil

### UnsetStartTrained
`func (o *RawAbilityV2) UnsetStartTrained()`

UnsetStartTrained ensures that no value is present for StartTrained, not even an explicit nil
### GetImage

`func (o *RawAbilityV2) GetImage() string`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *RawAbilityV2) GetImageOk() (*string, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *RawAbilityV2) SetImage(v string)`

SetImage sets Image field to given value.

### HasImage

`func (o *RawAbilityV2) HasImage() bool`

HasImage returns a boolean if a field has been set.

### SetImageNil

`func (o *RawAbilityV2) SetImageNil(b bool)`

 SetImageNil sets the value for Image to be an explicit nil

### UnsetImage
`func (o *RawAbilityV2) UnsetImage()`

UnsetImage ensures that no value is present for Image, not even an explicit nil
### GetUpdateTime

`func (o *RawAbilityV2) GetUpdateTime() int32`

GetUpdateTime returns the UpdateTime field if non-nil, zero value otherwise.

### GetUpdateTimeOk

`func (o *RawAbilityV2) GetUpdateTimeOk() (*int32, bool)`

GetUpdateTimeOk returns a tuple with the UpdateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateTime

`func (o *RawAbilityV2) SetUpdateTime(v int32)`

SetUpdateTime sets UpdateTime field to given value.

### HasUpdateTime

`func (o *RawAbilityV2) HasUpdateTime() bool`

HasUpdateTime returns a boolean if a field has been set.

### SetUpdateTimeNil

`func (o *RawAbilityV2) SetUpdateTimeNil(b bool)`

 SetUpdateTimeNil sets the value for UpdateTime to be an explicit nil

### UnsetUpdateTime
`func (o *RawAbilityV2) UnsetUpdateTime()`

UnsetUpdateTime ensures that no value is present for UpdateTime, not even an explicit nil
### GetProperties

`func (o *RawAbilityV2) GetProperties() map[string]RawItemPropertyV2`

GetProperties returns the Properties field if non-nil, zero value otherwise.

### GetPropertiesOk

`func (o *RawAbilityV2) GetPropertiesOk() (*map[string]RawItemPropertyV2, bool)`

GetPropertiesOk returns a tuple with the Properties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperties

`func (o *RawAbilityV2) SetProperties(v map[string]RawItemPropertyV2)`

SetProperties sets Properties field to given value.

### HasProperties

`func (o *RawAbilityV2) HasProperties() bool`

HasProperties returns a boolean if a field has been set.

### SetPropertiesNil

`func (o *RawAbilityV2) SetPropertiesNil(b bool)`

 SetPropertiesNil sets the value for Properties to be an explicit nil

### UnsetProperties
`func (o *RawAbilityV2) UnsetProperties()`

UnsetProperties ensures that no value is present for Properties, not even an explicit nil
### GetWeaponInfo

`func (o *RawAbilityV2) GetWeaponInfo() RawItemWeaponInfoV2`

GetWeaponInfo returns the WeaponInfo field if non-nil, zero value otherwise.

### GetWeaponInfoOk

`func (o *RawAbilityV2) GetWeaponInfoOk() (*RawItemWeaponInfoV2, bool)`

GetWeaponInfoOk returns a tuple with the WeaponInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponInfo

`func (o *RawAbilityV2) SetWeaponInfo(v RawItemWeaponInfoV2)`

SetWeaponInfo sets WeaponInfo field to given value.

### HasWeaponInfo

`func (o *RawAbilityV2) HasWeaponInfo() bool`

HasWeaponInfo returns a boolean if a field has been set.

### SetWeaponInfoNil

`func (o *RawAbilityV2) SetWeaponInfoNil(b bool)`

 SetWeaponInfoNil sets the value for WeaponInfo to be an explicit nil

### UnsetWeaponInfo
`func (o *RawAbilityV2) UnsetWeaponInfo()`

UnsetWeaponInfo ensures that no value is present for WeaponInfo, not even an explicit nil
### GetCssClass

`func (o *RawAbilityV2) GetCssClass() string`

GetCssClass returns the CssClass field if non-nil, zero value otherwise.

### GetCssClassOk

`func (o *RawAbilityV2) GetCssClassOk() (*string, bool)`

GetCssClassOk returns a tuple with the CssClass field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCssClass

`func (o *RawAbilityV2) SetCssClass(v string)`

SetCssClass sets CssClass field to given value.

### HasCssClass

`func (o *RawAbilityV2) HasCssClass() bool`

HasCssClass returns a boolean if a field has been set.

### SetCssClassNil

`func (o *RawAbilityV2) SetCssClassNil(b bool)`

 SetCssClassNil sets the value for CssClass to be an explicit nil

### UnsetCssClass
`func (o *RawAbilityV2) UnsetCssClass()`

UnsetCssClass ensures that no value is present for CssClass, not even an explicit nil
### GetType

`func (o *RawAbilityV2) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *RawAbilityV2) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *RawAbilityV2) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *RawAbilityV2) HasType() bool`

HasType returns a boolean if a field has been set.

### GetBehaviourBits

`func (o *RawAbilityV2) GetBehaviourBits() string`

GetBehaviourBits returns the BehaviourBits field if non-nil, zero value otherwise.

### GetBehaviourBitsOk

`func (o *RawAbilityV2) GetBehaviourBitsOk() (*string, bool)`

GetBehaviourBitsOk returns a tuple with the BehaviourBits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBehaviourBits

`func (o *RawAbilityV2) SetBehaviourBits(v string)`

SetBehaviourBits sets BehaviourBits field to given value.

### HasBehaviourBits

`func (o *RawAbilityV2) HasBehaviourBits() bool`

HasBehaviourBits returns a boolean if a field has been set.

### SetBehaviourBitsNil

`func (o *RawAbilityV2) SetBehaviourBitsNil(b bool)`

 SetBehaviourBitsNil sets the value for BehaviourBits to be an explicit nil

### UnsetBehaviourBits
`func (o *RawAbilityV2) UnsetBehaviourBits()`

UnsetBehaviourBits ensures that no value is present for BehaviourBits, not even an explicit nil
### GetUpgrades

`func (o *RawAbilityV2) GetUpgrades() []RawAbilityUpgradeV2`

GetUpgrades returns the Upgrades field if non-nil, zero value otherwise.

### GetUpgradesOk

`func (o *RawAbilityV2) GetUpgradesOk() (*[]RawAbilityUpgradeV2, bool)`

GetUpgradesOk returns a tuple with the Upgrades field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpgrades

`func (o *RawAbilityV2) SetUpgrades(v []RawAbilityUpgradeV2)`

SetUpgrades sets Upgrades field to given value.


### GetAbilityType

`func (o *RawAbilityV2) GetAbilityType() AbilityTypeV2`

GetAbilityType returns the AbilityType field if non-nil, zero value otherwise.

### GetAbilityTypeOk

`func (o *RawAbilityV2) GetAbilityTypeOk() (*AbilityTypeV2, bool)`

GetAbilityTypeOk returns a tuple with the AbilityType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAbilityType

`func (o *RawAbilityV2) SetAbilityType(v AbilityTypeV2)`

SetAbilityType sets AbilityType field to given value.

### HasAbilityType

`func (o *RawAbilityV2) HasAbilityType() bool`

HasAbilityType returns a boolean if a field has been set.

### SetAbilityTypeNil

`func (o *RawAbilityV2) SetAbilityTypeNil(b bool)`

 SetAbilityTypeNil sets the value for AbilityType to be an explicit nil

### UnsetAbilityType
`func (o *RawAbilityV2) UnsetAbilityType()`

UnsetAbilityType ensures that no value is present for AbilityType, not even an explicit nil
### GetBossDamageScale

`func (o *RawAbilityV2) GetBossDamageScale() float32`

GetBossDamageScale returns the BossDamageScale field if non-nil, zero value otherwise.

### GetBossDamageScaleOk

`func (o *RawAbilityV2) GetBossDamageScaleOk() (*float32, bool)`

GetBossDamageScaleOk returns a tuple with the BossDamageScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBossDamageScale

`func (o *RawAbilityV2) SetBossDamageScale(v float32)`

SetBossDamageScale sets BossDamageScale field to given value.

### HasBossDamageScale

`func (o *RawAbilityV2) HasBossDamageScale() bool`

HasBossDamageScale returns a boolean if a field has been set.

### SetBossDamageScaleNil

`func (o *RawAbilityV2) SetBossDamageScaleNil(b bool)`

 SetBossDamageScaleNil sets the value for BossDamageScale to be an explicit nil

### UnsetBossDamageScale
`func (o *RawAbilityV2) UnsetBossDamageScale()`

UnsetBossDamageScale ensures that no value is present for BossDamageScale, not even an explicit nil
### GetDependantAbilities

`func (o *RawAbilityV2) GetDependantAbilities() []string`

GetDependantAbilities returns the DependantAbilities field if non-nil, zero value otherwise.

### GetDependantAbilitiesOk

`func (o *RawAbilityV2) GetDependantAbilitiesOk() (*[]string, bool)`

GetDependantAbilitiesOk returns a tuple with the DependantAbilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependantAbilities

`func (o *RawAbilityV2) SetDependantAbilities(v []string)`

SetDependantAbilities sets DependantAbilities field to given value.

### HasDependantAbilities

`func (o *RawAbilityV2) HasDependantAbilities() bool`

HasDependantAbilities returns a boolean if a field has been set.

### SetDependantAbilitiesNil

`func (o *RawAbilityV2) SetDependantAbilitiesNil(b bool)`

 SetDependantAbilitiesNil sets the value for DependantAbilities to be an explicit nil

### UnsetDependantAbilities
`func (o *RawAbilityV2) UnsetDependantAbilities()`

UnsetDependantAbilities ensures that no value is present for DependantAbilities, not even an explicit nil
### GetVideo

`func (o *RawAbilityV2) GetVideo() string`

GetVideo returns the Video field if non-nil, zero value otherwise.

### GetVideoOk

`func (o *RawAbilityV2) GetVideoOk() (*string, bool)`

GetVideoOk returns a tuple with the Video field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVideo

`func (o *RawAbilityV2) SetVideo(v string)`

SetVideo sets Video field to given value.

### HasVideo

`func (o *RawAbilityV2) HasVideo() bool`

HasVideo returns a boolean if a field has been set.

### SetVideoNil

`func (o *RawAbilityV2) SetVideoNil(b bool)`

 SetVideoNil sets the value for Video to be an explicit nil

### UnsetVideo
`func (o *RawAbilityV2) UnsetVideo()`

UnsetVideo ensures that no value is present for Video, not even an explicit nil
### GetTooltipDetails

`func (o *RawAbilityV2) GetTooltipDetails() RawAbilityV2TooltipDetails`

GetTooltipDetails returns the TooltipDetails field if non-nil, zero value otherwise.

### GetTooltipDetailsOk

`func (o *RawAbilityV2) GetTooltipDetailsOk() (*RawAbilityV2TooltipDetails, bool)`

GetTooltipDetailsOk returns a tuple with the TooltipDetails field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipDetails

`func (o *RawAbilityV2) SetTooltipDetails(v RawAbilityV2TooltipDetails)`

SetTooltipDetails sets TooltipDetails field to given value.

### HasTooltipDetails

`func (o *RawAbilityV2) HasTooltipDetails() bool`

HasTooltipDetails returns a boolean if a field has been set.

### SetTooltipDetailsNil

`func (o *RawAbilityV2) SetTooltipDetailsNil(b bool)`

 SetTooltipDetailsNil sets the value for TooltipDetails to be an explicit nil

### UnsetTooltipDetails
`func (o *RawAbilityV2) UnsetTooltipDetails()`

UnsetTooltipDetails ensures that no value is present for TooltipDetails, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


