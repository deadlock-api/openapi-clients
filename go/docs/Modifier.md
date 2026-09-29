# Modifier

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Base** | Pointer to **NullableString** | Entry this one inherits from (&#x60;_base&#x60;). | [optional] 
**Class** | Pointer to **NullableString** | Engine class (&#x60;_class&#x60;), e.g. &#x60;citadel_neutral_laser_beam&#x60;. | [optional] 
**ClassName** | **string** |  | 
**Folder** | Pointer to **NullableString** | Editor folder (&#x60;_editor.folder_name&#x60;), e.g. &#x60;Neutral Ability&#x60;. | [optional] 
**Id** | **int32** |  | 
**Properties** | **map[string]float64** | Numeric properties keyed by their source name. Nested properties use a dotted path (&#x60;m_GroundAuraModifier.m_modifierProvidedByAura.m_flDPS&#x60;, &#x60;subclass:&#x60; wrappers are skipped); &#x60;m_vecScriptValues&#x60; entries are keyed by their &#x60;m_eModifierValue&#x60; (&#x60;MODIFIER_VALUE_GRAVITY_SCALE&#x60;). | 

## Methods

### NewModifier

`func NewModifier(className string, id int32, properties map[string]float64, ) *Modifier`

NewModifier instantiates a new Modifier object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewModifierWithDefaults

`func NewModifierWithDefaults() *Modifier`

NewModifierWithDefaults instantiates a new Modifier object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBase

`func (o *Modifier) GetBase() string`

GetBase returns the Base field if non-nil, zero value otherwise.

### GetBaseOk

`func (o *Modifier) GetBaseOk() (*string, bool)`

GetBaseOk returns a tuple with the Base field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBase

`func (o *Modifier) SetBase(v string)`

SetBase sets Base field to given value.

### HasBase

`func (o *Modifier) HasBase() bool`

HasBase returns a boolean if a field has been set.

### SetBaseNil

`func (o *Modifier) SetBaseNil(b bool)`

 SetBaseNil sets the value for Base to be an explicit nil

### UnsetBase
`func (o *Modifier) UnsetBase()`

UnsetBase ensures that no value is present for Base, not even an explicit nil
### GetClass

`func (o *Modifier) GetClass() string`

GetClass returns the Class field if non-nil, zero value otherwise.

### GetClassOk

`func (o *Modifier) GetClassOk() (*string, bool)`

GetClassOk returns a tuple with the Class field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClass

`func (o *Modifier) SetClass(v string)`

SetClass sets Class field to given value.

### HasClass

`func (o *Modifier) HasClass() bool`

HasClass returns a boolean if a field has been set.

### SetClassNil

`func (o *Modifier) SetClassNil(b bool)`

 SetClassNil sets the value for Class to be an explicit nil

### UnsetClass
`func (o *Modifier) UnsetClass()`

UnsetClass ensures that no value is present for Class, not even an explicit nil
### GetClassName

`func (o *Modifier) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *Modifier) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *Modifier) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetFolder

`func (o *Modifier) GetFolder() string`

GetFolder returns the Folder field if non-nil, zero value otherwise.

### GetFolderOk

`func (o *Modifier) GetFolderOk() (*string, bool)`

GetFolderOk returns a tuple with the Folder field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFolder

`func (o *Modifier) SetFolder(v string)`

SetFolder sets Folder field to given value.

### HasFolder

`func (o *Modifier) HasFolder() bool`

HasFolder returns a boolean if a field has been set.

### SetFolderNil

`func (o *Modifier) SetFolderNil(b bool)`

 SetFolderNil sets the value for Folder to be an explicit nil

### UnsetFolder
`func (o *Modifier) UnsetFolder()`

UnsetFolder ensures that no value is present for Folder, not even an explicit nil
### GetId

`func (o *Modifier) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Modifier) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Modifier) SetId(v int32)`

SetId sets Id field to given value.


### GetProperties

`func (o *Modifier) GetProperties() map[string]float64`

GetProperties returns the Properties field if non-nil, zero value otherwise.

### GetPropertiesOk

`func (o *Modifier) GetPropertiesOk() (*map[string]float64, bool)`

GetPropertiesOk returns a tuple with the Properties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperties

`func (o *Modifier) SetProperties(v map[string]float64)`

SetProperties sets Properties field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


