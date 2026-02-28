# ResponseGetRawItemsRawItemsGetInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClassName** | **string** |  | 
**StartTrained** | Pointer to **bool** |  | [optional] 
**Image** | Pointer to **string** |  | [optional] 
**UpdateTime** | Pointer to **int32** |  | [optional] 
**Properties** | Pointer to [**map[string]RawItemPropertyV2**](RawItemPropertyV2.md) |  | [optional] 
**WeaponInfo** | Pointer to [**RawItemWeaponInfoV2**](RawItemWeaponInfoV2.md) |  | [optional] 
**CssClass** | Pointer to **string** |  | [optional] 
**Type** | Pointer to **string** |  | [optional] [default to "ability"]
**GrantAmmoOnCast** | Pointer to **bool** |  | [optional] 
**BehaviourBits** | Pointer to **string** |  | [optional] 
**Upgrades** | [**[]RawAbilityUpgradeV2**](RawAbilityUpgradeV2.md) |  | 
**AbilityType** | Pointer to [**AbilityTypeV2**](AbilityTypeV2.md) |  | [optional] 
**BossDamageScale** | Pointer to **float32** |  | [optional] 
**DependantAbilities** | Pointer to **[]string** |  | [optional] 
**Video** | Pointer to **string** |  | [optional] 
**TooltipDetails** | Pointer to [**RawAbilityV2TooltipDetails**](RawAbilityV2TooltipDetails.md) |  | [optional] 
**DependentAbilities** | Pointer to [**map[string]AbilityV2DependentAbilitiesValue**](AbilityV2DependentAbilitiesValue.md) |  | [optional] 
**ShopImage** | Pointer to **string** |  | [optional] 
**ShopImageSmall** | Pointer to **string** |  | [optional] 
**ItemSlotType** | [**ItemSlotTypeV2**](ItemSlotTypeV2.md) |  | 
**ItemTier** | [**ItemTierV2**](ItemTierV2.md) |  | 
**Disabled** | Pointer to **bool** |  | [optional] 
**Activation** | Pointer to [**RawAbilityActivationV2**](RawAbilityActivationV2.md) |  | [optional] 
**Imbue** | Pointer to [**RawAbilityImbueV2**](RawAbilityImbueV2.md) |  | [optional] 
**ComponentItems** | Pointer to **[]string** |  | [optional] 
**TooltipSections** | Pointer to [**[]RawUpgradeTooltipSectionV2**](RawUpgradeTooltipSectionV2.md) |  | [optional] 

## Methods

### NewResponseGetRawItemsRawItemsGetInner

`func NewResponseGetRawItemsRawItemsGetInner(className string, upgrades []RawAbilityUpgradeV2, itemSlotType ItemSlotTypeV2, itemTier ItemTierV2, ) *ResponseGetRawItemsRawItemsGetInner`

NewResponseGetRawItemsRawItemsGetInner instantiates a new ResponseGetRawItemsRawItemsGetInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewResponseGetRawItemsRawItemsGetInnerWithDefaults

`func NewResponseGetRawItemsRawItemsGetInnerWithDefaults() *ResponseGetRawItemsRawItemsGetInner`

NewResponseGetRawItemsRawItemsGetInnerWithDefaults instantiates a new ResponseGetRawItemsRawItemsGetInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClassName

`func (o *ResponseGetRawItemsRawItemsGetInner) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *ResponseGetRawItemsRawItemsGetInner) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetStartTrained

`func (o *ResponseGetRawItemsRawItemsGetInner) GetStartTrained() bool`

GetStartTrained returns the StartTrained field if non-nil, zero value otherwise.

### GetStartTrainedOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetStartTrainedOk() (*bool, bool)`

GetStartTrainedOk returns a tuple with the StartTrained field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTrained

`func (o *ResponseGetRawItemsRawItemsGetInner) SetStartTrained(v bool)`

SetStartTrained sets StartTrained field to given value.

### HasStartTrained

`func (o *ResponseGetRawItemsRawItemsGetInner) HasStartTrained() bool`

HasStartTrained returns a boolean if a field has been set.

### GetImage

`func (o *ResponseGetRawItemsRawItemsGetInner) GetImage() string`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetImageOk() (*string, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *ResponseGetRawItemsRawItemsGetInner) SetImage(v string)`

SetImage sets Image field to given value.

### HasImage

`func (o *ResponseGetRawItemsRawItemsGetInner) HasImage() bool`

HasImage returns a boolean if a field has been set.

### GetUpdateTime

`func (o *ResponseGetRawItemsRawItemsGetInner) GetUpdateTime() int32`

GetUpdateTime returns the UpdateTime field if non-nil, zero value otherwise.

### GetUpdateTimeOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetUpdateTimeOk() (*int32, bool)`

GetUpdateTimeOk returns a tuple with the UpdateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateTime

`func (o *ResponseGetRawItemsRawItemsGetInner) SetUpdateTime(v int32)`

SetUpdateTime sets UpdateTime field to given value.

### HasUpdateTime

`func (o *ResponseGetRawItemsRawItemsGetInner) HasUpdateTime() bool`

HasUpdateTime returns a boolean if a field has been set.

### GetProperties

`func (o *ResponseGetRawItemsRawItemsGetInner) GetProperties() map[string]RawItemPropertyV2`

GetProperties returns the Properties field if non-nil, zero value otherwise.

### GetPropertiesOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetPropertiesOk() (*map[string]RawItemPropertyV2, bool)`

GetPropertiesOk returns a tuple with the Properties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperties

`func (o *ResponseGetRawItemsRawItemsGetInner) SetProperties(v map[string]RawItemPropertyV2)`

SetProperties sets Properties field to given value.

### HasProperties

`func (o *ResponseGetRawItemsRawItemsGetInner) HasProperties() bool`

HasProperties returns a boolean if a field has been set.

### GetWeaponInfo

`func (o *ResponseGetRawItemsRawItemsGetInner) GetWeaponInfo() RawItemWeaponInfoV2`

GetWeaponInfo returns the WeaponInfo field if non-nil, zero value otherwise.

### GetWeaponInfoOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetWeaponInfoOk() (*RawItemWeaponInfoV2, bool)`

GetWeaponInfoOk returns a tuple with the WeaponInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponInfo

`func (o *ResponseGetRawItemsRawItemsGetInner) SetWeaponInfo(v RawItemWeaponInfoV2)`

SetWeaponInfo sets WeaponInfo field to given value.

### HasWeaponInfo

`func (o *ResponseGetRawItemsRawItemsGetInner) HasWeaponInfo() bool`

HasWeaponInfo returns a boolean if a field has been set.

### GetCssClass

`func (o *ResponseGetRawItemsRawItemsGetInner) GetCssClass() string`

GetCssClass returns the CssClass field if non-nil, zero value otherwise.

### GetCssClassOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetCssClassOk() (*string, bool)`

GetCssClassOk returns a tuple with the CssClass field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCssClass

`func (o *ResponseGetRawItemsRawItemsGetInner) SetCssClass(v string)`

SetCssClass sets CssClass field to given value.

### HasCssClass

`func (o *ResponseGetRawItemsRawItemsGetInner) HasCssClass() bool`

HasCssClass returns a boolean if a field has been set.

### GetType

`func (o *ResponseGetRawItemsRawItemsGetInner) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ResponseGetRawItemsRawItemsGetInner) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *ResponseGetRawItemsRawItemsGetInner) HasType() bool`

HasType returns a boolean if a field has been set.

### GetGrantAmmoOnCast

`func (o *ResponseGetRawItemsRawItemsGetInner) GetGrantAmmoOnCast() bool`

GetGrantAmmoOnCast returns the GrantAmmoOnCast field if non-nil, zero value otherwise.

### GetGrantAmmoOnCastOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetGrantAmmoOnCastOk() (*bool, bool)`

GetGrantAmmoOnCastOk returns a tuple with the GrantAmmoOnCast field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGrantAmmoOnCast

`func (o *ResponseGetRawItemsRawItemsGetInner) SetGrantAmmoOnCast(v bool)`

SetGrantAmmoOnCast sets GrantAmmoOnCast field to given value.

### HasGrantAmmoOnCast

`func (o *ResponseGetRawItemsRawItemsGetInner) HasGrantAmmoOnCast() bool`

HasGrantAmmoOnCast returns a boolean if a field has been set.

### GetBehaviourBits

`func (o *ResponseGetRawItemsRawItemsGetInner) GetBehaviourBits() string`

GetBehaviourBits returns the BehaviourBits field if non-nil, zero value otherwise.

### GetBehaviourBitsOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetBehaviourBitsOk() (*string, bool)`

GetBehaviourBitsOk returns a tuple with the BehaviourBits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBehaviourBits

`func (o *ResponseGetRawItemsRawItemsGetInner) SetBehaviourBits(v string)`

SetBehaviourBits sets BehaviourBits field to given value.

### HasBehaviourBits

`func (o *ResponseGetRawItemsRawItemsGetInner) HasBehaviourBits() bool`

HasBehaviourBits returns a boolean if a field has been set.

### GetUpgrades

`func (o *ResponseGetRawItemsRawItemsGetInner) GetUpgrades() []RawAbilityUpgradeV2`

GetUpgrades returns the Upgrades field if non-nil, zero value otherwise.

### GetUpgradesOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetUpgradesOk() (*[]RawAbilityUpgradeV2, bool)`

GetUpgradesOk returns a tuple with the Upgrades field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpgrades

`func (o *ResponseGetRawItemsRawItemsGetInner) SetUpgrades(v []RawAbilityUpgradeV2)`

SetUpgrades sets Upgrades field to given value.


### GetAbilityType

`func (o *ResponseGetRawItemsRawItemsGetInner) GetAbilityType() AbilityTypeV2`

GetAbilityType returns the AbilityType field if non-nil, zero value otherwise.

### GetAbilityTypeOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetAbilityTypeOk() (*AbilityTypeV2, bool)`

GetAbilityTypeOk returns a tuple with the AbilityType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAbilityType

`func (o *ResponseGetRawItemsRawItemsGetInner) SetAbilityType(v AbilityTypeV2)`

SetAbilityType sets AbilityType field to given value.

### HasAbilityType

`func (o *ResponseGetRawItemsRawItemsGetInner) HasAbilityType() bool`

HasAbilityType returns a boolean if a field has been set.

### GetBossDamageScale

`func (o *ResponseGetRawItemsRawItemsGetInner) GetBossDamageScale() float32`

GetBossDamageScale returns the BossDamageScale field if non-nil, zero value otherwise.

### GetBossDamageScaleOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetBossDamageScaleOk() (*float32, bool)`

GetBossDamageScaleOk returns a tuple with the BossDamageScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBossDamageScale

`func (o *ResponseGetRawItemsRawItemsGetInner) SetBossDamageScale(v float32)`

SetBossDamageScale sets BossDamageScale field to given value.

### HasBossDamageScale

`func (o *ResponseGetRawItemsRawItemsGetInner) HasBossDamageScale() bool`

HasBossDamageScale returns a boolean if a field has been set.

### GetDependantAbilities

`func (o *ResponseGetRawItemsRawItemsGetInner) GetDependantAbilities() []string`

GetDependantAbilities returns the DependantAbilities field if non-nil, zero value otherwise.

### GetDependantAbilitiesOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetDependantAbilitiesOk() (*[]string, bool)`

GetDependantAbilitiesOk returns a tuple with the DependantAbilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependantAbilities

`func (o *ResponseGetRawItemsRawItemsGetInner) SetDependantAbilities(v []string)`

SetDependantAbilities sets DependantAbilities field to given value.

### HasDependantAbilities

`func (o *ResponseGetRawItemsRawItemsGetInner) HasDependantAbilities() bool`

HasDependantAbilities returns a boolean if a field has been set.

### GetVideo

`func (o *ResponseGetRawItemsRawItemsGetInner) GetVideo() string`

GetVideo returns the Video field if non-nil, zero value otherwise.

### GetVideoOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetVideoOk() (*string, bool)`

GetVideoOk returns a tuple with the Video field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVideo

`func (o *ResponseGetRawItemsRawItemsGetInner) SetVideo(v string)`

SetVideo sets Video field to given value.

### HasVideo

`func (o *ResponseGetRawItemsRawItemsGetInner) HasVideo() bool`

HasVideo returns a boolean if a field has been set.

### GetTooltipDetails

`func (o *ResponseGetRawItemsRawItemsGetInner) GetTooltipDetails() RawAbilityV2TooltipDetails`

GetTooltipDetails returns the TooltipDetails field if non-nil, zero value otherwise.

### GetTooltipDetailsOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetTooltipDetailsOk() (*RawAbilityV2TooltipDetails, bool)`

GetTooltipDetailsOk returns a tuple with the TooltipDetails field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipDetails

`func (o *ResponseGetRawItemsRawItemsGetInner) SetTooltipDetails(v RawAbilityV2TooltipDetails)`

SetTooltipDetails sets TooltipDetails field to given value.

### HasTooltipDetails

`func (o *ResponseGetRawItemsRawItemsGetInner) HasTooltipDetails() bool`

HasTooltipDetails returns a boolean if a field has been set.

### GetDependentAbilities

`func (o *ResponseGetRawItemsRawItemsGetInner) GetDependentAbilities() map[string]AbilityV2DependentAbilitiesValue`

GetDependentAbilities returns the DependentAbilities field if non-nil, zero value otherwise.

### GetDependentAbilitiesOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetDependentAbilitiesOk() (*map[string]AbilityV2DependentAbilitiesValue, bool)`

GetDependentAbilitiesOk returns a tuple with the DependentAbilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependentAbilities

`func (o *ResponseGetRawItemsRawItemsGetInner) SetDependentAbilities(v map[string]AbilityV2DependentAbilitiesValue)`

SetDependentAbilities sets DependentAbilities field to given value.

### HasDependentAbilities

`func (o *ResponseGetRawItemsRawItemsGetInner) HasDependentAbilities() bool`

HasDependentAbilities returns a boolean if a field has been set.

### GetShopImage

`func (o *ResponseGetRawItemsRawItemsGetInner) GetShopImage() string`

GetShopImage returns the ShopImage field if non-nil, zero value otherwise.

### GetShopImageOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetShopImageOk() (*string, bool)`

GetShopImageOk returns a tuple with the ShopImage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImage

`func (o *ResponseGetRawItemsRawItemsGetInner) SetShopImage(v string)`

SetShopImage sets ShopImage field to given value.

### HasShopImage

`func (o *ResponseGetRawItemsRawItemsGetInner) HasShopImage() bool`

HasShopImage returns a boolean if a field has been set.

### GetShopImageSmall

`func (o *ResponseGetRawItemsRawItemsGetInner) GetShopImageSmall() string`

GetShopImageSmall returns the ShopImageSmall field if non-nil, zero value otherwise.

### GetShopImageSmallOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetShopImageSmallOk() (*string, bool)`

GetShopImageSmallOk returns a tuple with the ShopImageSmall field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopImageSmall

`func (o *ResponseGetRawItemsRawItemsGetInner) SetShopImageSmall(v string)`

SetShopImageSmall sets ShopImageSmall field to given value.

### HasShopImageSmall

`func (o *ResponseGetRawItemsRawItemsGetInner) HasShopImageSmall() bool`

HasShopImageSmall returns a boolean if a field has been set.

### GetItemSlotType

`func (o *ResponseGetRawItemsRawItemsGetInner) GetItemSlotType() ItemSlotTypeV2`

GetItemSlotType returns the ItemSlotType field if non-nil, zero value otherwise.

### GetItemSlotTypeOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetItemSlotTypeOk() (*ItemSlotTypeV2, bool)`

GetItemSlotTypeOk returns a tuple with the ItemSlotType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemSlotType

`func (o *ResponseGetRawItemsRawItemsGetInner) SetItemSlotType(v ItemSlotTypeV2)`

SetItemSlotType sets ItemSlotType field to given value.


### GetItemTier

`func (o *ResponseGetRawItemsRawItemsGetInner) GetItemTier() ItemTierV2`

GetItemTier returns the ItemTier field if non-nil, zero value otherwise.

### GetItemTierOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetItemTierOk() (*ItemTierV2, bool)`

GetItemTierOk returns a tuple with the ItemTier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemTier

`func (o *ResponseGetRawItemsRawItemsGetInner) SetItemTier(v ItemTierV2)`

SetItemTier sets ItemTier field to given value.


### GetDisabled

`func (o *ResponseGetRawItemsRawItemsGetInner) GetDisabled() bool`

GetDisabled returns the Disabled field if non-nil, zero value otherwise.

### GetDisabledOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetDisabledOk() (*bool, bool)`

GetDisabledOk returns a tuple with the Disabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisabled

`func (o *ResponseGetRawItemsRawItemsGetInner) SetDisabled(v bool)`

SetDisabled sets Disabled field to given value.

### HasDisabled

`func (o *ResponseGetRawItemsRawItemsGetInner) HasDisabled() bool`

HasDisabled returns a boolean if a field has been set.

### GetActivation

`func (o *ResponseGetRawItemsRawItemsGetInner) GetActivation() RawAbilityActivationV2`

GetActivation returns the Activation field if non-nil, zero value otherwise.

### GetActivationOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetActivationOk() (*RawAbilityActivationV2, bool)`

GetActivationOk returns a tuple with the Activation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActivation

`func (o *ResponseGetRawItemsRawItemsGetInner) SetActivation(v RawAbilityActivationV2)`

SetActivation sets Activation field to given value.

### HasActivation

`func (o *ResponseGetRawItemsRawItemsGetInner) HasActivation() bool`

HasActivation returns a boolean if a field has been set.

### GetImbue

`func (o *ResponseGetRawItemsRawItemsGetInner) GetImbue() RawAbilityImbueV2`

GetImbue returns the Imbue field if non-nil, zero value otherwise.

### GetImbueOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetImbueOk() (*RawAbilityImbueV2, bool)`

GetImbueOk returns a tuple with the Imbue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImbue

`func (o *ResponseGetRawItemsRawItemsGetInner) SetImbue(v RawAbilityImbueV2)`

SetImbue sets Imbue field to given value.

### HasImbue

`func (o *ResponseGetRawItemsRawItemsGetInner) HasImbue() bool`

HasImbue returns a boolean if a field has been set.

### GetComponentItems

`func (o *ResponseGetRawItemsRawItemsGetInner) GetComponentItems() []string`

GetComponentItems returns the ComponentItems field if non-nil, zero value otherwise.

### GetComponentItemsOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetComponentItemsOk() (*[]string, bool)`

GetComponentItemsOk returns a tuple with the ComponentItems field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComponentItems

`func (o *ResponseGetRawItemsRawItemsGetInner) SetComponentItems(v []string)`

SetComponentItems sets ComponentItems field to given value.

### HasComponentItems

`func (o *ResponseGetRawItemsRawItemsGetInner) HasComponentItems() bool`

HasComponentItems returns a boolean if a field has been set.

### GetTooltipSections

`func (o *ResponseGetRawItemsRawItemsGetInner) GetTooltipSections() []RawUpgradeTooltipSectionV2`

GetTooltipSections returns the TooltipSections field if non-nil, zero value otherwise.

### GetTooltipSectionsOk

`func (o *ResponseGetRawItemsRawItemsGetInner) GetTooltipSectionsOk() (*[]RawUpgradeTooltipSectionV2, bool)`

GetTooltipSectionsOk returns a tuple with the TooltipSections field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTooltipSections

`func (o *ResponseGetRawItemsRawItemsGetInner) SetTooltipSections(v []RawUpgradeTooltipSectionV2)`

SetTooltipSections sets TooltipSections field to given value.

### HasTooltipSections

`func (o *ResponseGetRawItemsRawItemsGetInner) HasTooltipSections() bool`

HasTooltipSections returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


