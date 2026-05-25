# Map

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Images** | [**MapImages**](MapImages.md) |  | 
**ObjectivePositions** | [**map[string]ObjectivePosition**](ObjectivePosition.md) |  | 
**Radius** | **int32** |  | 
**ZiplinePaths** | [**[]ZiplanePath**](ZiplanePath.md) |  | 

## Methods

### NewMap

`func NewMap(images MapImages, objectivePositions map[string]ObjectivePosition, radius int32, ziplinePaths []ZiplanePath, ) *Map`

NewMap instantiates a new Map object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMapWithDefaults

`func NewMapWithDefaults() *Map`

NewMapWithDefaults instantiates a new Map object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetImages

`func (o *Map) GetImages() MapImages`

GetImages returns the Images field if non-nil, zero value otherwise.

### GetImagesOk

`func (o *Map) GetImagesOk() (*MapImages, bool)`

GetImagesOk returns a tuple with the Images field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImages

`func (o *Map) SetImages(v MapImages)`

SetImages sets Images field to given value.


### GetObjectivePositions

`func (o *Map) GetObjectivePositions() map[string]ObjectivePosition`

GetObjectivePositions returns the ObjectivePositions field if non-nil, zero value otherwise.

### GetObjectivePositionsOk

`func (o *Map) GetObjectivePositionsOk() (*map[string]ObjectivePosition, bool)`

GetObjectivePositionsOk returns a tuple with the ObjectivePositions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectivePositions

`func (o *Map) SetObjectivePositions(v map[string]ObjectivePosition)`

SetObjectivePositions sets ObjectivePositions field to given value.


### GetRadius

`func (o *Map) GetRadius() int32`

GetRadius returns the Radius field if non-nil, zero value otherwise.

### GetRadiusOk

`func (o *Map) GetRadiusOk() (*int32, bool)`

GetRadiusOk returns a tuple with the Radius field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRadius

`func (o *Map) SetRadius(v int32)`

SetRadius sets Radius field to given value.


### GetZiplinePaths

`func (o *Map) GetZiplinePaths() []ZiplanePath`

GetZiplinePaths returns the ZiplinePaths field if non-nil, zero value otherwise.

### GetZiplinePathsOk

`func (o *Map) GetZiplinePathsOk() (*[]ZiplanePath, bool)`

GetZiplinePathsOk returns a tuple with the ZiplinePaths field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetZiplinePaths

`func (o *Map) SetZiplinePaths(v []ZiplanePath)`

SetZiplinePaths sets ZiplinePaths field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


