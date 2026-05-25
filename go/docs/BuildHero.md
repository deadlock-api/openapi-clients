# BuildHero

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthorAccountId** | **int32** |  | 
**Description** | Pointer to **NullableString** |  | [optional] 
**Details** | [**BuildHeroDetails**](BuildHeroDetails.md) |  | 
**DevelopmentBuild** | Pointer to **NullableBool** |  | [optional] 
**HeroBuildId** | **int32** |  | 
**HeroId** | **int32** | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**Language** | **int32** |  | 
**LastUpdatedTimestamp** | Pointer to **NullableInt64** |  | [optional] 
**Name** | **string** |  | 
**OriginBuildId** | **int32** |  | 
**PublishTimestamp** | Pointer to **NullableInt64** |  | [optional] 
**Tags** | Pointer to **[]int32** |  | [optional] 
**Version** | **int32** |  | 

## Methods

### NewBuildHero

`func NewBuildHero(authorAccountId int32, details BuildHeroDetails, heroBuildId int32, heroId int32, language int32, name string, originBuildId int32, version int32, ) *BuildHero`

NewBuildHero instantiates a new BuildHero object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBuildHeroWithDefaults

`func NewBuildHeroWithDefaults() *BuildHero`

NewBuildHeroWithDefaults instantiates a new BuildHero object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuthorAccountId

`func (o *BuildHero) GetAuthorAccountId() int32`

GetAuthorAccountId returns the AuthorAccountId field if non-nil, zero value otherwise.

### GetAuthorAccountIdOk

`func (o *BuildHero) GetAuthorAccountIdOk() (*int32, bool)`

GetAuthorAccountIdOk returns a tuple with the AuthorAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorAccountId

`func (o *BuildHero) SetAuthorAccountId(v int32)`

SetAuthorAccountId sets AuthorAccountId field to given value.


### GetDescription

`func (o *BuildHero) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *BuildHero) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *BuildHero) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *BuildHero) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *BuildHero) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *BuildHero) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetDetails

`func (o *BuildHero) GetDetails() BuildHeroDetails`

GetDetails returns the Details field if non-nil, zero value otherwise.

### GetDetailsOk

`func (o *BuildHero) GetDetailsOk() (*BuildHeroDetails, bool)`

GetDetailsOk returns a tuple with the Details field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDetails

`func (o *BuildHero) SetDetails(v BuildHeroDetails)`

SetDetails sets Details field to given value.


### GetDevelopmentBuild

`func (o *BuildHero) GetDevelopmentBuild() bool`

GetDevelopmentBuild returns the DevelopmentBuild field if non-nil, zero value otherwise.

### GetDevelopmentBuildOk

`func (o *BuildHero) GetDevelopmentBuildOk() (*bool, bool)`

GetDevelopmentBuildOk returns a tuple with the DevelopmentBuild field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDevelopmentBuild

`func (o *BuildHero) SetDevelopmentBuild(v bool)`

SetDevelopmentBuild sets DevelopmentBuild field to given value.

### HasDevelopmentBuild

`func (o *BuildHero) HasDevelopmentBuild() bool`

HasDevelopmentBuild returns a boolean if a field has been set.

### SetDevelopmentBuildNil

`func (o *BuildHero) SetDevelopmentBuildNil(b bool)`

 SetDevelopmentBuildNil sets the value for DevelopmentBuild to be an explicit nil

### UnsetDevelopmentBuild
`func (o *BuildHero) UnsetDevelopmentBuild()`

UnsetDevelopmentBuild ensures that no value is present for DevelopmentBuild, not even an explicit nil
### GetHeroBuildId

`func (o *BuildHero) GetHeroBuildId() int32`

GetHeroBuildId returns the HeroBuildId field if non-nil, zero value otherwise.

### GetHeroBuildIdOk

`func (o *BuildHero) GetHeroBuildIdOk() (*int32, bool)`

GetHeroBuildIdOk returns a tuple with the HeroBuildId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroBuildId

`func (o *BuildHero) SetHeroBuildId(v int32)`

SetHeroBuildId sets HeroBuildId field to given value.


### GetHeroId

`func (o *BuildHero) GetHeroId() int32`

GetHeroId returns the HeroId field if non-nil, zero value otherwise.

### GetHeroIdOk

`func (o *BuildHero) GetHeroIdOk() (*int32, bool)`

GetHeroIdOk returns a tuple with the HeroId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroId

`func (o *BuildHero) SetHeroId(v int32)`

SetHeroId sets HeroId field to given value.


### GetLanguage

`func (o *BuildHero) GetLanguage() int32`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *BuildHero) GetLanguageOk() (*int32, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *BuildHero) SetLanguage(v int32)`

SetLanguage sets Language field to given value.


### GetLastUpdatedTimestamp

`func (o *BuildHero) GetLastUpdatedTimestamp() int64`

GetLastUpdatedTimestamp returns the LastUpdatedTimestamp field if non-nil, zero value otherwise.

### GetLastUpdatedTimestampOk

`func (o *BuildHero) GetLastUpdatedTimestampOk() (*int64, bool)`

GetLastUpdatedTimestampOk returns a tuple with the LastUpdatedTimestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastUpdatedTimestamp

`func (o *BuildHero) SetLastUpdatedTimestamp(v int64)`

SetLastUpdatedTimestamp sets LastUpdatedTimestamp field to given value.

### HasLastUpdatedTimestamp

`func (o *BuildHero) HasLastUpdatedTimestamp() bool`

HasLastUpdatedTimestamp returns a boolean if a field has been set.

### SetLastUpdatedTimestampNil

`func (o *BuildHero) SetLastUpdatedTimestampNil(b bool)`

 SetLastUpdatedTimestampNil sets the value for LastUpdatedTimestamp to be an explicit nil

### UnsetLastUpdatedTimestamp
`func (o *BuildHero) UnsetLastUpdatedTimestamp()`

UnsetLastUpdatedTimestamp ensures that no value is present for LastUpdatedTimestamp, not even an explicit nil
### GetName

`func (o *BuildHero) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *BuildHero) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *BuildHero) SetName(v string)`

SetName sets Name field to given value.


### GetOriginBuildId

`func (o *BuildHero) GetOriginBuildId() int32`

GetOriginBuildId returns the OriginBuildId field if non-nil, zero value otherwise.

### GetOriginBuildIdOk

`func (o *BuildHero) GetOriginBuildIdOk() (*int32, bool)`

GetOriginBuildIdOk returns a tuple with the OriginBuildId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOriginBuildId

`func (o *BuildHero) SetOriginBuildId(v int32)`

SetOriginBuildId sets OriginBuildId field to given value.


### GetPublishTimestamp

`func (o *BuildHero) GetPublishTimestamp() int64`

GetPublishTimestamp returns the PublishTimestamp field if non-nil, zero value otherwise.

### GetPublishTimestampOk

`func (o *BuildHero) GetPublishTimestampOk() (*int64, bool)`

GetPublishTimestampOk returns a tuple with the PublishTimestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublishTimestamp

`func (o *BuildHero) SetPublishTimestamp(v int64)`

SetPublishTimestamp sets PublishTimestamp field to given value.

### HasPublishTimestamp

`func (o *BuildHero) HasPublishTimestamp() bool`

HasPublishTimestamp returns a boolean if a field has been set.

### SetPublishTimestampNil

`func (o *BuildHero) SetPublishTimestampNil(b bool)`

 SetPublishTimestampNil sets the value for PublishTimestamp to be an explicit nil

### UnsetPublishTimestamp
`func (o *BuildHero) UnsetPublishTimestamp()`

UnsetPublishTimestamp ensures that no value is present for PublishTimestamp, not even an explicit nil
### GetTags

`func (o *BuildHero) GetTags() []int32`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *BuildHero) GetTagsOk() (*[]int32, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTags

`func (o *BuildHero) SetTags(v []int32)`

SetTags sets Tags field to given value.

### HasTags

`func (o *BuildHero) HasTags() bool`

HasTags returns a boolean if a field has been set.

### GetVersion

`func (o *BuildHero) GetVersion() int32`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *BuildHero) GetVersionOk() (*int32, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *BuildHero) SetVersion(v int32)`

SetVersion sets Version field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


