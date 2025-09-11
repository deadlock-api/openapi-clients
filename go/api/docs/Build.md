# Build

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**HeroBuild** | [**BuildHero**](BuildHero.md) |  | 
**NumFavorites** | Pointer to **NullableInt32** |  | [optional] 
**NumIgnores** | Pointer to **NullableInt32** |  | [optional] 
**NumReports** | Pointer to **NullableInt32** |  | [optional] 
**NumWeeklyFavorites** | Pointer to **NullableInt32** |  | [optional] 
**RollupCategory** | Pointer to **NullableInt32** |  | [optional] 

## Methods

### NewBuild

`func NewBuild(heroBuild BuildHero, ) *Build`

NewBuild instantiates a new Build object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBuildWithDefaults

`func NewBuildWithDefaults() *Build`

NewBuildWithDefaults instantiates a new Build object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetHeroBuild

`func (o *Build) GetHeroBuild() BuildHero`

GetHeroBuild returns the HeroBuild field if non-nil, zero value otherwise.

### GetHeroBuildOk

`func (o *Build) GetHeroBuildOk() (*BuildHero, bool)`

GetHeroBuildOk returns a tuple with the HeroBuild field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroBuild

`func (o *Build) SetHeroBuild(v BuildHero)`

SetHeroBuild sets HeroBuild field to given value.


### GetNumFavorites

`func (o *Build) GetNumFavorites() int32`

GetNumFavorites returns the NumFavorites field if non-nil, zero value otherwise.

### GetNumFavoritesOk

`func (o *Build) GetNumFavoritesOk() (*int32, bool)`

GetNumFavoritesOk returns a tuple with the NumFavorites field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNumFavorites

`func (o *Build) SetNumFavorites(v int32)`

SetNumFavorites sets NumFavorites field to given value.

### HasNumFavorites

`func (o *Build) HasNumFavorites() bool`

HasNumFavorites returns a boolean if a field has been set.

### SetNumFavoritesNil

`func (o *Build) SetNumFavoritesNil(b bool)`

 SetNumFavoritesNil sets the value for NumFavorites to be an explicit nil

### UnsetNumFavorites
`func (o *Build) UnsetNumFavorites()`

UnsetNumFavorites ensures that no value is present for NumFavorites, not even an explicit nil
### GetNumIgnores

`func (o *Build) GetNumIgnores() int32`

GetNumIgnores returns the NumIgnores field if non-nil, zero value otherwise.

### GetNumIgnoresOk

`func (o *Build) GetNumIgnoresOk() (*int32, bool)`

GetNumIgnoresOk returns a tuple with the NumIgnores field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNumIgnores

`func (o *Build) SetNumIgnores(v int32)`

SetNumIgnores sets NumIgnores field to given value.

### HasNumIgnores

`func (o *Build) HasNumIgnores() bool`

HasNumIgnores returns a boolean if a field has been set.

### SetNumIgnoresNil

`func (o *Build) SetNumIgnoresNil(b bool)`

 SetNumIgnoresNil sets the value for NumIgnores to be an explicit nil

### UnsetNumIgnores
`func (o *Build) UnsetNumIgnores()`

UnsetNumIgnores ensures that no value is present for NumIgnores, not even an explicit nil
### GetNumReports

`func (o *Build) GetNumReports() int32`

GetNumReports returns the NumReports field if non-nil, zero value otherwise.

### GetNumReportsOk

`func (o *Build) GetNumReportsOk() (*int32, bool)`

GetNumReportsOk returns a tuple with the NumReports field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNumReports

`func (o *Build) SetNumReports(v int32)`

SetNumReports sets NumReports field to given value.

### HasNumReports

`func (o *Build) HasNumReports() bool`

HasNumReports returns a boolean if a field has been set.

### SetNumReportsNil

`func (o *Build) SetNumReportsNil(b bool)`

 SetNumReportsNil sets the value for NumReports to be an explicit nil

### UnsetNumReports
`func (o *Build) UnsetNumReports()`

UnsetNumReports ensures that no value is present for NumReports, not even an explicit nil
### GetNumWeeklyFavorites

`func (o *Build) GetNumWeeklyFavorites() int32`

GetNumWeeklyFavorites returns the NumWeeklyFavorites field if non-nil, zero value otherwise.

### GetNumWeeklyFavoritesOk

`func (o *Build) GetNumWeeklyFavoritesOk() (*int32, bool)`

GetNumWeeklyFavoritesOk returns a tuple with the NumWeeklyFavorites field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNumWeeklyFavorites

`func (o *Build) SetNumWeeklyFavorites(v int32)`

SetNumWeeklyFavorites sets NumWeeklyFavorites field to given value.

### HasNumWeeklyFavorites

`func (o *Build) HasNumWeeklyFavorites() bool`

HasNumWeeklyFavorites returns a boolean if a field has been set.

### SetNumWeeklyFavoritesNil

`func (o *Build) SetNumWeeklyFavoritesNil(b bool)`

 SetNumWeeklyFavoritesNil sets the value for NumWeeklyFavorites to be an explicit nil

### UnsetNumWeeklyFavorites
`func (o *Build) UnsetNumWeeklyFavorites()`

UnsetNumWeeklyFavorites ensures that no value is present for NumWeeklyFavorites, not even an explicit nil
### GetRollupCategory

`func (o *Build) GetRollupCategory() int32`

GetRollupCategory returns the RollupCategory field if non-nil, zero value otherwise.

### GetRollupCategoryOk

`func (o *Build) GetRollupCategoryOk() (*int32, bool)`

GetRollupCategoryOk returns a tuple with the RollupCategory field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRollupCategory

`func (o *Build) SetRollupCategory(v int32)`

SetRollupCategory sets RollupCategory field to given value.

### HasRollupCategory

`func (o *Build) HasRollupCategory() bool`

HasRollupCategory returns a boolean if a field has been set.

### SetRollupCategoryNil

`func (o *Build) SetRollupCategoryNil(b bool)`

 SetRollupCategoryNil sets the value for RollupCategory to be an explicit nil

### UnsetRollupCategory
`func (o *Build) UnsetRollupCategory()`

UnsetRollupCategory ensures that no value is present for RollupCategory, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


