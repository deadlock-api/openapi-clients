# MapData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Images** | [**MapImages**](MapImages.md) |  | 
**ObjectivePositions** | [**map[string]ObjectivePosition**](ObjectivePosition.md) |  | 
**Radius** | **int32** |  | 
**ZiplinePaths** | [**[]ZiplanePath**](ZiplanePath.md) |  | 

## Methods

### NewMapData

`func NewMapData(images MapImages, objectivePositions map[string]ObjectivePosition, radius int32, ziplinePaths []ZiplanePath, ) *MapData`

NewMapData instantiates a new MapData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMapDataWithDefaults

`func NewMapDataWithDefaults() *MapData`

NewMapDataWithDefaults instantiates a new MapData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetImages

`func (o *MapData) GetImages() MapImages`

GetImages returns the Images field if non-nil, zero value otherwise.

### GetImagesOk

`func (o *MapData) GetImagesOk() (*MapImages, bool)`

GetImagesOk returns a tuple with the Images field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImages

`func (o *MapData) SetImages(v MapImages)`

SetImages sets Images field to given value.


### GetObjectivePositions

`func (o *MapData) GetObjectivePositions() map[string]ObjectivePosition`

GetObjectivePositions returns the ObjectivePositions field if non-nil, zero value otherwise.

### GetObjectivePositionsOk

`func (o *MapData) GetObjectivePositionsOk() (*map[string]ObjectivePosition, bool)`

GetObjectivePositionsOk returns a tuple with the ObjectivePositions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectivePositions

`func (o *MapData) SetObjectivePositions(v map[string]ObjectivePosition)`

SetObjectivePositions sets ObjectivePositions field to given value.


### GetRadius

`func (o *MapData) GetRadius() int32`

GetRadius returns the Radius field if non-nil, zero value otherwise.

### GetRadiusOk

`func (o *MapData) GetRadiusOk() (*int32, bool)`

GetRadiusOk returns a tuple with the Radius field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRadius

`func (o *MapData) SetRadius(v int32)`

SetRadius sets Radius field to given value.


### GetZiplinePaths

`func (o *MapData) GetZiplinePaths() []ZiplanePath`

GetZiplinePaths returns the ZiplinePaths field if non-nil, zero value otherwise.

### GetZiplinePathsOk

`func (o *MapData) GetZiplinePathsOk() (*[]ZiplanePath, bool)`

GetZiplinePathsOk returns a tuple with the ZiplinePaths field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetZiplinePaths

`func (o *MapData) SetZiplinePaths(v []ZiplanePath)`

SetZiplinePaths sets ZiplinePaths field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


