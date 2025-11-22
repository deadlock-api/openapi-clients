# MiniMapOffsets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EntityClass** | **string** |  | 
**Offset2d** | **[]float32** |  | 
**LaneIndex** | Pointer to **NullableInt32** |  | [optional] 

## Methods

### NewMiniMapOffsets

`func NewMiniMapOffsets(entityClass string, offset2d []float32, ) *MiniMapOffsets`

NewMiniMapOffsets instantiates a new MiniMapOffsets object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMiniMapOffsetsWithDefaults

`func NewMiniMapOffsetsWithDefaults() *MiniMapOffsets`

NewMiniMapOffsetsWithDefaults instantiates a new MiniMapOffsets object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEntityClass

`func (o *MiniMapOffsets) GetEntityClass() string`

GetEntityClass returns the EntityClass field if non-nil, zero value otherwise.

### GetEntityClassOk

`func (o *MiniMapOffsets) GetEntityClassOk() (*string, bool)`

GetEntityClassOk returns a tuple with the EntityClass field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEntityClass

`func (o *MiniMapOffsets) SetEntityClass(v string)`

SetEntityClass sets EntityClass field to given value.


### GetOffset2d

`func (o *MiniMapOffsets) GetOffset2d() []float32`

GetOffset2d returns the Offset2d field if non-nil, zero value otherwise.

### GetOffset2dOk

`func (o *MiniMapOffsets) GetOffset2dOk() (*[]float32, bool)`

GetOffset2dOk returns a tuple with the Offset2d field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset2d

`func (o *MiniMapOffsets) SetOffset2d(v []float32)`

SetOffset2d sets Offset2d field to given value.


### GetLaneIndex

`func (o *MiniMapOffsets) GetLaneIndex() int32`

GetLaneIndex returns the LaneIndex field if non-nil, zero value otherwise.

### GetLaneIndexOk

`func (o *MiniMapOffsets) GetLaneIndexOk() (*int32, bool)`

GetLaneIndexOk returns a tuple with the LaneIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLaneIndex

`func (o *MiniMapOffsets) SetLaneIndex(v int32)`

SetLaneIndex sets LaneIndex field to given value.

### HasLaneIndex

`func (o *MiniMapOffsets) HasLaneIndex() bool`

HasLaneIndex returns a boolean if a field has been set.

### SetLaneIndexNil

`func (o *MiniMapOffsets) SetLaneIndexNil(b bool)`

 SetLaneIndexNil sets the value for LaneIndex to be an explicit nil

### UnsetLaneIndex
`func (o *MiniMapOffsets) UnsetLaneIndex()`

UnsetLaneIndex ensures that no value is present for LaneIndex, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


