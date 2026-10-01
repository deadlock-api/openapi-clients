# MapEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Kind** | Pointer to **NullableString** | Variant within the category, e.g. &#x60;wooden_crate&#x60; or &#x60;secret&#x60; (shops). | [optional] 
**LeftRelative** | Pointer to **float64** | Position on the minimap, as fractions of its width/height. | [optional] 
**Position** | **[]float64** | World position &#x60;[x, y, z]&#x60;, same space as the zip-line splines. Brush triggers (ropes, pads, veils, ...) are placed at their entity origin. | 
**Target** | Pointer to **[]float64** | World position &#x60;[x, y, z]&#x60; the entity sends you to: the teleporter exit or the bounce pad landing spot. | [optional] 
**Team** | Pointer to **NullableInt32** | Owning team (0 or 1); absent for neutral entities. | [optional] 
**TopRelative** | Pointer to **float64** |  | [optional] 

## Methods

### NewMapEntity

`func NewMapEntity(position []float64, ) *MapEntity`

NewMapEntity instantiates a new MapEntity object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMapEntityWithDefaults

`func NewMapEntityWithDefaults() *MapEntity`

NewMapEntityWithDefaults instantiates a new MapEntity object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetKind

`func (o *MapEntity) GetKind() string`

GetKind returns the Kind field if non-nil, zero value otherwise.

### GetKindOk

`func (o *MapEntity) GetKindOk() (*string, bool)`

GetKindOk returns a tuple with the Kind field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKind

`func (o *MapEntity) SetKind(v string)`

SetKind sets Kind field to given value.

### HasKind

`func (o *MapEntity) HasKind() bool`

HasKind returns a boolean if a field has been set.

### SetKindNil

`func (o *MapEntity) SetKindNil(b bool)`

 SetKindNil sets the value for Kind to be an explicit nil

### UnsetKind
`func (o *MapEntity) UnsetKind()`

UnsetKind ensures that no value is present for Kind, not even an explicit nil
### GetLeftRelative

`func (o *MapEntity) GetLeftRelative() float64`

GetLeftRelative returns the LeftRelative field if non-nil, zero value otherwise.

### GetLeftRelativeOk

`func (o *MapEntity) GetLeftRelativeOk() (*float64, bool)`

GetLeftRelativeOk returns a tuple with the LeftRelative field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLeftRelative

`func (o *MapEntity) SetLeftRelative(v float64)`

SetLeftRelative sets LeftRelative field to given value.

### HasLeftRelative

`func (o *MapEntity) HasLeftRelative() bool`

HasLeftRelative returns a boolean if a field has been set.

### GetPosition

`func (o *MapEntity) GetPosition() []float64`

GetPosition returns the Position field if non-nil, zero value otherwise.

### GetPositionOk

`func (o *MapEntity) GetPositionOk() (*[]float64, bool)`

GetPositionOk returns a tuple with the Position field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPosition

`func (o *MapEntity) SetPosition(v []float64)`

SetPosition sets Position field to given value.


### GetTarget

`func (o *MapEntity) GetTarget() []float64`

GetTarget returns the Target field if non-nil, zero value otherwise.

### GetTargetOk

`func (o *MapEntity) GetTargetOk() (*[]float64, bool)`

GetTargetOk returns a tuple with the Target field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTarget

`func (o *MapEntity) SetTarget(v []float64)`

SetTarget sets Target field to given value.

### HasTarget

`func (o *MapEntity) HasTarget() bool`

HasTarget returns a boolean if a field has been set.

### SetTargetNil

`func (o *MapEntity) SetTargetNil(b bool)`

 SetTargetNil sets the value for Target to be an explicit nil

### UnsetTarget
`func (o *MapEntity) UnsetTarget()`

UnsetTarget ensures that no value is present for Target, not even an explicit nil
### GetTeam

`func (o *MapEntity) GetTeam() int32`

GetTeam returns the Team field if non-nil, zero value otherwise.

### GetTeamOk

`func (o *MapEntity) GetTeamOk() (*int32, bool)`

GetTeamOk returns a tuple with the Team field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTeam

`func (o *MapEntity) SetTeam(v int32)`

SetTeam sets Team field to given value.

### HasTeam

`func (o *MapEntity) HasTeam() bool`

HasTeam returns a boolean if a field has been set.

### SetTeamNil

`func (o *MapEntity) SetTeamNil(b bool)`

 SetTeamNil sets the value for Team to be an explicit nil

### UnsetTeam
`func (o *MapEntity) UnsetTeam()`

UnsetTeam ensures that no value is present for Team, not even an explicit nil
### GetTopRelative

`func (o *MapEntity) GetTopRelative() float64`

GetTopRelative returns the TopRelative field if non-nil, zero value otherwise.

### GetTopRelativeOk

`func (o *MapEntity) GetTopRelativeOk() (*float64, bool)`

GetTopRelativeOk returns a tuple with the TopRelative field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopRelative

`func (o *MapEntity) SetTopRelative(v float64)`

SetTopRelative sets TopRelative field to given value.

### HasTopRelative

`func (o *MapEntity) HasTopRelative() bool`

HasTopRelative returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


