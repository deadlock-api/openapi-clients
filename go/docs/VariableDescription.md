# VariableDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Category** | [**VariableCategory**](VariableCategory.md) | The category of the variable. | 
**DefaultLabel** | Pointer to **NullableString** | The default label for the variable. | [optional] 
**Description** | **string** | The description of the variable. | 
**ExtraArgs** | **[]string** | Extra arguments that can be passed to the variable. | 
**Name** | **string** | The name of the variable. | 

## Methods

### NewVariableDescription

`func NewVariableDescription(category VariableCategory, description string, extraArgs []string, name string, ) *VariableDescription`

NewVariableDescription instantiates a new VariableDescription object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewVariableDescriptionWithDefaults

`func NewVariableDescriptionWithDefaults() *VariableDescription`

NewVariableDescriptionWithDefaults instantiates a new VariableDescription object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCategory

`func (o *VariableDescription) GetCategory() VariableCategory`

GetCategory returns the Category field if non-nil, zero value otherwise.

### GetCategoryOk

`func (o *VariableDescription) GetCategoryOk() (*VariableCategory, bool)`

GetCategoryOk returns a tuple with the Category field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategory

`func (o *VariableDescription) SetCategory(v VariableCategory)`

SetCategory sets Category field to given value.


### GetDefaultLabel

`func (o *VariableDescription) GetDefaultLabel() string`

GetDefaultLabel returns the DefaultLabel field if non-nil, zero value otherwise.

### GetDefaultLabelOk

`func (o *VariableDescription) GetDefaultLabelOk() (*string, bool)`

GetDefaultLabelOk returns a tuple with the DefaultLabel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultLabel

`func (o *VariableDescription) SetDefaultLabel(v string)`

SetDefaultLabel sets DefaultLabel field to given value.

### HasDefaultLabel

`func (o *VariableDescription) HasDefaultLabel() bool`

HasDefaultLabel returns a boolean if a field has been set.

### SetDefaultLabelNil

`func (o *VariableDescription) SetDefaultLabelNil(b bool)`

 SetDefaultLabelNil sets the value for DefaultLabel to be an explicit nil

### UnsetDefaultLabel
`func (o *VariableDescription) UnsetDefaultLabel()`

UnsetDefaultLabel ensures that no value is present for DefaultLabel, not even an explicit nil
### GetDescription

`func (o *VariableDescription) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *VariableDescription) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *VariableDescription) SetDescription(v string)`

SetDescription sets Description field to given value.


### GetExtraArgs

`func (o *VariableDescription) GetExtraArgs() []string`

GetExtraArgs returns the ExtraArgs field if non-nil, zero value otherwise.

### GetExtraArgsOk

`func (o *VariableDescription) GetExtraArgsOk() (*[]string, bool)`

GetExtraArgsOk returns a tuple with the ExtraArgs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExtraArgs

`func (o *VariableDescription) SetExtraArgs(v []string)`

SetExtraArgs sets ExtraArgs field to given value.


### GetName

`func (o *VariableDescription) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *VariableDescription) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *VariableDescription) SetName(v string)`

SetName sets Name field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


