# NeutralCamp

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Icon** | **string** | Minimap icon URL. | 
**Kind** | [**NeutralCampKind**](NeutralCampKind.md) |  | 
**LeftRelative** | **float64** | Position on the minimap, as fractions of its width/height. | 
**Name** | **string** | Camp entity name from the map (e.g. &#x60;theater_lobby_camp&#x60;). | 
**Position** | **[]float64** | World position &#x60;[x, y, z]&#x60;, same space as the zip-line splines. | 
**TopRelative** | **float64** |  | 

## Methods

### NewNeutralCamp

`func NewNeutralCamp(icon string, kind NeutralCampKind, leftRelative float64, name string, position []float64, topRelative float64, ) *NeutralCamp`

NewNeutralCamp instantiates a new NeutralCamp object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNeutralCampWithDefaults

`func NewNeutralCampWithDefaults() *NeutralCamp`

NewNeutralCampWithDefaults instantiates a new NeutralCamp object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIcon

`func (o *NeutralCamp) GetIcon() string`

GetIcon returns the Icon field if non-nil, zero value otherwise.

### GetIconOk

`func (o *NeutralCamp) GetIconOk() (*string, bool)`

GetIconOk returns a tuple with the Icon field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIcon

`func (o *NeutralCamp) SetIcon(v string)`

SetIcon sets Icon field to given value.


### GetKind

`func (o *NeutralCamp) GetKind() NeutralCampKind`

GetKind returns the Kind field if non-nil, zero value otherwise.

### GetKindOk

`func (o *NeutralCamp) GetKindOk() (*NeutralCampKind, bool)`

GetKindOk returns a tuple with the Kind field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKind

`func (o *NeutralCamp) SetKind(v NeutralCampKind)`

SetKind sets Kind field to given value.


### GetLeftRelative

`func (o *NeutralCamp) GetLeftRelative() float64`

GetLeftRelative returns the LeftRelative field if non-nil, zero value otherwise.

### GetLeftRelativeOk

`func (o *NeutralCamp) GetLeftRelativeOk() (*float64, bool)`

GetLeftRelativeOk returns a tuple with the LeftRelative field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLeftRelative

`func (o *NeutralCamp) SetLeftRelative(v float64)`

SetLeftRelative sets LeftRelative field to given value.


### GetName

`func (o *NeutralCamp) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *NeutralCamp) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *NeutralCamp) SetName(v string)`

SetName sets Name field to given value.


### GetPosition

`func (o *NeutralCamp) GetPosition() []float64`

GetPosition returns the Position field if non-nil, zero value otherwise.

### GetPositionOk

`func (o *NeutralCamp) GetPositionOk() (*[]float64, bool)`

GetPositionOk returns a tuple with the Position field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPosition

`func (o *NeutralCamp) SetPosition(v []float64)`

SetPosition sets Position field to given value.


### GetTopRelative

`func (o *NeutralCamp) GetTopRelative() float64`

GetTopRelative returns the TopRelative field if non-nil, zero value otherwise.

### GetTopRelativeOk

`func (o *NeutralCamp) GetTopRelativeOk() (*float64, bool)`

GetTopRelativeOk returns a tuple with the TopRelative field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopRelative

`func (o *NeutralCamp) SetTopRelative(v float64)`

SetTopRelative sets TopRelative field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


