# TableSchemaRow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Comment** | Pointer to **NullableString** |  | [optional] 
**Name** | **string** |  | 
**Type** | **string** |  | 

## Methods

### NewTableSchemaRow

`func NewTableSchemaRow(name string, type_ string, ) *TableSchemaRow`

NewTableSchemaRow instantiates a new TableSchemaRow object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTableSchemaRowWithDefaults

`func NewTableSchemaRowWithDefaults() *TableSchemaRow`

NewTableSchemaRowWithDefaults instantiates a new TableSchemaRow object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetComment

`func (o *TableSchemaRow) GetComment() string`

GetComment returns the Comment field if non-nil, zero value otherwise.

### GetCommentOk

`func (o *TableSchemaRow) GetCommentOk() (*string, bool)`

GetCommentOk returns a tuple with the Comment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComment

`func (o *TableSchemaRow) SetComment(v string)`

SetComment sets Comment field to given value.

### HasComment

`func (o *TableSchemaRow) HasComment() bool`

HasComment returns a boolean if a field has been set.

### SetCommentNil

`func (o *TableSchemaRow) SetCommentNil(b bool)`

 SetCommentNil sets the value for Comment to be an explicit nil

### UnsetComment
`func (o *TableSchemaRow) UnsetComment()`

UnsetComment ensures that no value is present for Comment, not even an explicit nil
### GetName

`func (o *TableSchemaRow) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *TableSchemaRow) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *TableSchemaRow) SetName(v string)`

SetName sets Name field to given value.


### GetType

`func (o *TableSchemaRow) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *TableSchemaRow) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *TableSchemaRow) SetType(v string)`

SetType sets Type field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


