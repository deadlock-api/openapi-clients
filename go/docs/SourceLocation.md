# SourceLocation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Chain** | Pointer to **[]string** |  | [optional] 
**Column** | **int32** |  | 
**Component** | Pointer to **NullableString** |  | [optional] 
**File** | **string** |  | 
**Line** | **int32** |  | 

## Methods

### NewSourceLocation

`func NewSourceLocation(column int32, file string, line int32, ) *SourceLocation`

NewSourceLocation instantiates a new SourceLocation object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSourceLocationWithDefaults

`func NewSourceLocationWithDefaults() *SourceLocation`

NewSourceLocationWithDefaults instantiates a new SourceLocation object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetChain

`func (o *SourceLocation) GetChain() []string`

GetChain returns the Chain field if non-nil, zero value otherwise.

### GetChainOk

`func (o *SourceLocation) GetChainOk() (*[]string, bool)`

GetChainOk returns a tuple with the Chain field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChain

`func (o *SourceLocation) SetChain(v []string)`

SetChain sets Chain field to given value.

### HasChain

`func (o *SourceLocation) HasChain() bool`

HasChain returns a boolean if a field has been set.

### GetColumn

`func (o *SourceLocation) GetColumn() int32`

GetColumn returns the Column field if non-nil, zero value otherwise.

### GetColumnOk

`func (o *SourceLocation) GetColumnOk() (*int32, bool)`

GetColumnOk returns a tuple with the Column field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColumn

`func (o *SourceLocation) SetColumn(v int32)`

SetColumn sets Column field to given value.


### GetComponent

`func (o *SourceLocation) GetComponent() string`

GetComponent returns the Component field if non-nil, zero value otherwise.

### GetComponentOk

`func (o *SourceLocation) GetComponentOk() (*string, bool)`

GetComponentOk returns a tuple with the Component field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComponent

`func (o *SourceLocation) SetComponent(v string)`

SetComponent sets Component field to given value.

### HasComponent

`func (o *SourceLocation) HasComponent() bool`

HasComponent returns a boolean if a field has been set.

### SetComponentNil

`func (o *SourceLocation) SetComponentNil(b bool)`

 SetComponentNil sets the value for Component to be an explicit nil

### UnsetComponent
`func (o *SourceLocation) UnsetComponent()`

UnsetComponent ensures that no value is present for Component, not even an explicit nil
### GetFile

`func (o *SourceLocation) GetFile() string`

GetFile returns the File field if non-nil, zero value otherwise.

### GetFileOk

`func (o *SourceLocation) GetFileOk() (*string, bool)`

GetFileOk returns a tuple with the File field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFile

`func (o *SourceLocation) SetFile(v string)`

SetFile sets File field to given value.


### GetLine

`func (o *SourceLocation) GetLine() int32`

GetLine returns the Line field if non-nil, zero value otherwise.

### GetLineOk

`func (o *SourceLocation) GetLineOk() (*int32, bool)`

GetLineOk returns a tuple with the Line field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLine

`func (o *SourceLocation) SetLine(v int32)`

SetLine sets Line field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


