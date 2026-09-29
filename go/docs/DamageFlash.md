# DamageFlash

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BulletDamage** | [**FlashData**](FlashData.md) |  | 
**CritDamage** | [**FlashData**](FlashData.md) |  | 
**GenericDamage** | Pointer to [**NullableFlashData**](FlashData.md) | Build 6711+. | [optional] 
**HealingDamage** | [**FlashData**](FlashData.md) |  | 
**MeleeDamage** | [**FlashData**](FlashData.md) |  | 
**TechDamage** | [**FlashData**](FlashData.md) |  | 

## Methods

### NewDamageFlash

`func NewDamageFlash(bulletDamage FlashData, critDamage FlashData, healingDamage FlashData, meleeDamage FlashData, techDamage FlashData, ) *DamageFlash`

NewDamageFlash instantiates a new DamageFlash object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDamageFlashWithDefaults

`func NewDamageFlashWithDefaults() *DamageFlash`

NewDamageFlashWithDefaults instantiates a new DamageFlash object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBulletDamage

`func (o *DamageFlash) GetBulletDamage() FlashData`

GetBulletDamage returns the BulletDamage field if non-nil, zero value otherwise.

### GetBulletDamageOk

`func (o *DamageFlash) GetBulletDamageOk() (*FlashData, bool)`

GetBulletDamageOk returns a tuple with the BulletDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBulletDamage

`func (o *DamageFlash) SetBulletDamage(v FlashData)`

SetBulletDamage sets BulletDamage field to given value.


### GetCritDamage

`func (o *DamageFlash) GetCritDamage() FlashData`

GetCritDamage returns the CritDamage field if non-nil, zero value otherwise.

### GetCritDamageOk

`func (o *DamageFlash) GetCritDamageOk() (*FlashData, bool)`

GetCritDamageOk returns a tuple with the CritDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCritDamage

`func (o *DamageFlash) SetCritDamage(v FlashData)`

SetCritDamage sets CritDamage field to given value.


### GetGenericDamage

`func (o *DamageFlash) GetGenericDamage() FlashData`

GetGenericDamage returns the GenericDamage field if non-nil, zero value otherwise.

### GetGenericDamageOk

`func (o *DamageFlash) GetGenericDamageOk() (*FlashData, bool)`

GetGenericDamageOk returns a tuple with the GenericDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGenericDamage

`func (o *DamageFlash) SetGenericDamage(v FlashData)`

SetGenericDamage sets GenericDamage field to given value.

### HasGenericDamage

`func (o *DamageFlash) HasGenericDamage() bool`

HasGenericDamage returns a boolean if a field has been set.

### SetGenericDamageNil

`func (o *DamageFlash) SetGenericDamageNil(b bool)`

 SetGenericDamageNil sets the value for GenericDamage to be an explicit nil

### UnsetGenericDamage
`func (o *DamageFlash) UnsetGenericDamage()`

UnsetGenericDamage ensures that no value is present for GenericDamage, not even an explicit nil
### GetHealingDamage

`func (o *DamageFlash) GetHealingDamage() FlashData`

GetHealingDamage returns the HealingDamage field if non-nil, zero value otherwise.

### GetHealingDamageOk

`func (o *DamageFlash) GetHealingDamageOk() (*FlashData, bool)`

GetHealingDamageOk returns a tuple with the HealingDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHealingDamage

`func (o *DamageFlash) SetHealingDamage(v FlashData)`

SetHealingDamage sets HealingDamage field to given value.


### GetMeleeDamage

`func (o *DamageFlash) GetMeleeDamage() FlashData`

GetMeleeDamage returns the MeleeDamage field if non-nil, zero value otherwise.

### GetMeleeDamageOk

`func (o *DamageFlash) GetMeleeDamageOk() (*FlashData, bool)`

GetMeleeDamageOk returns a tuple with the MeleeDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeleeDamage

`func (o *DamageFlash) SetMeleeDamage(v FlashData)`

SetMeleeDamage sets MeleeDamage field to given value.


### GetTechDamage

`func (o *DamageFlash) GetTechDamage() FlashData`

GetTechDamage returns the TechDamage field if non-nil, zero value otherwise.

### GetTechDamageOk

`func (o *DamageFlash) GetTechDamageOk() (*FlashData, bool)`

GetTechDamageOk returns a tuple with the TechDamage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTechDamage

`func (o *DamageFlash) SetTechDamage(v FlashData)`

SetTechDamage sets TechDamage field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


