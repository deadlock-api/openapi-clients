# BuildHeroDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AbilityOrder** | Pointer to [**NullableBuildHeroDetailsAbilityOrder**](BuildHeroDetailsAbilityOrder.md) |  | [optional] 
**ModCategories** | [**[]BuildHeroDetailsCategory**](BuildHeroDetailsCategory.md) |  | 

## Methods

### NewBuildHeroDetails

`func NewBuildHeroDetails(modCategories []BuildHeroDetailsCategory, ) *BuildHeroDetails`

NewBuildHeroDetails instantiates a new BuildHeroDetails object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBuildHeroDetailsWithDefaults

`func NewBuildHeroDetailsWithDefaults() *BuildHeroDetails`

NewBuildHeroDetailsWithDefaults instantiates a new BuildHeroDetails object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAbilityOrder

`func (o *BuildHeroDetails) GetAbilityOrder() BuildHeroDetailsAbilityOrder`

GetAbilityOrder returns the AbilityOrder field if non-nil, zero value otherwise.

### GetAbilityOrderOk

`func (o *BuildHeroDetails) GetAbilityOrderOk() (*BuildHeroDetailsAbilityOrder, bool)`

GetAbilityOrderOk returns a tuple with the AbilityOrder field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAbilityOrder

`func (o *BuildHeroDetails) SetAbilityOrder(v BuildHeroDetailsAbilityOrder)`

SetAbilityOrder sets AbilityOrder field to given value.

### HasAbilityOrder

`func (o *BuildHeroDetails) HasAbilityOrder() bool`

HasAbilityOrder returns a boolean if a field has been set.

### SetAbilityOrderNil

`func (o *BuildHeroDetails) SetAbilityOrderNil(b bool)`

 SetAbilityOrderNil sets the value for AbilityOrder to be an explicit nil

### UnsetAbilityOrder
`func (o *BuildHeroDetails) UnsetAbilityOrder()`

UnsetAbilityOrder ensures that no value is present for AbilityOrder, not even an explicit nil
### GetModCategories

`func (o *BuildHeroDetails) GetModCategories() []BuildHeroDetailsCategory`

GetModCategories returns the ModCategories field if non-nil, zero value otherwise.

### GetModCategoriesOk

`func (o *BuildHeroDetails) GetModCategoriesOk() (*[]BuildHeroDetailsCategory, bool)`

GetModCategoriesOk returns a tuple with the ModCategories field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModCategories

`func (o *BuildHeroDetails) SetModCategories(v []BuildHeroDetailsCategory)`

SetModCategories sets ModCategories field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


