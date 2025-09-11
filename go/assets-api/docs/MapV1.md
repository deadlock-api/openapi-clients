# MapV1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Radius** | Pointer to **int32** | The radius of the map. | [optional] [default to 10752]
**Images** | [**MapImagesV1**](MapImagesV1.md) | The images of the map. | 
**ObjectivePositions** | [**ObjectivePositionsV1**](ObjectivePositionsV1.md) |  | [readonly] 
**ZiplinePaths** | [**[]ZiplanePathV1**](ZiplanePathV1.md) | The ziplane paths of the map. Each path is a list of P0, P1, and P2 points, describing the cubic spline. | 

## Methods

### NewMapV1

`func NewMapV1(images MapImagesV1, objectivePositions ObjectivePositionsV1, ziplinePaths []ZiplanePathV1, ) *MapV1`

NewMapV1 instantiates a new MapV1 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMapV1WithDefaults

`func NewMapV1WithDefaults() *MapV1`

NewMapV1WithDefaults instantiates a new MapV1 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRadius

`func (o *MapV1) GetRadius() int32`

GetRadius returns the Radius field if non-nil, zero value otherwise.

### GetRadiusOk

`func (o *MapV1) GetRadiusOk() (*int32, bool)`

GetRadiusOk returns a tuple with the Radius field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRadius

`func (o *MapV1) SetRadius(v int32)`

SetRadius sets Radius field to given value.

### HasRadius

`func (o *MapV1) HasRadius() bool`

HasRadius returns a boolean if a field has been set.

### GetImages

`func (o *MapV1) GetImages() MapImagesV1`

GetImages returns the Images field if non-nil, zero value otherwise.

### GetImagesOk

`func (o *MapV1) GetImagesOk() (*MapImagesV1, bool)`

GetImagesOk returns a tuple with the Images field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImages

`func (o *MapV1) SetImages(v MapImagesV1)`

SetImages sets Images field to given value.


### GetObjectivePositions

`func (o *MapV1) GetObjectivePositions() ObjectivePositionsV1`

GetObjectivePositions returns the ObjectivePositions field if non-nil, zero value otherwise.

### GetObjectivePositionsOk

`func (o *MapV1) GetObjectivePositionsOk() (*ObjectivePositionsV1, bool)`

GetObjectivePositionsOk returns a tuple with the ObjectivePositions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectivePositions

`func (o *MapV1) SetObjectivePositions(v ObjectivePositionsV1)`

SetObjectivePositions sets ObjectivePositions field to given value.


### GetZiplinePaths

`func (o *MapV1) GetZiplinePaths() []ZiplanePathV1`

GetZiplinePaths returns the ZiplinePaths field if non-nil, zero value otherwise.

### GetZiplinePathsOk

`func (o *MapV1) GetZiplinePathsOk() (*[]ZiplanePathV1, bool)`

GetZiplinePathsOk returns a tuple with the ZiplinePaths field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetZiplinePaths

`func (o *MapV1) SetZiplinePaths(v []ZiplanePathV1)`

SetZiplinePaths sets ZiplinePaths field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


