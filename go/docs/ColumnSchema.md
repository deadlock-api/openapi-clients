# ColumnSchema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DataType** | **string** | Arrow data type, rendered as its canonical textual form (e.g. &#x60;Int32&#x60;, &#x60;Utf8&#x60;). | 
**Name** | **string** |  | 
**Nullable** | **bool** |  | 

## Methods

### NewColumnSchema

`func NewColumnSchema(dataType string, name string, nullable bool, ) *ColumnSchema`

NewColumnSchema instantiates a new ColumnSchema object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewColumnSchemaWithDefaults

`func NewColumnSchemaWithDefaults() *ColumnSchema`

NewColumnSchemaWithDefaults instantiates a new ColumnSchema object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDataType

`func (o *ColumnSchema) GetDataType() string`

GetDataType returns the DataType field if non-nil, zero value otherwise.

### GetDataTypeOk

`func (o *ColumnSchema) GetDataTypeOk() (*string, bool)`

GetDataTypeOk returns a tuple with the DataType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDataType

`func (o *ColumnSchema) SetDataType(v string)`

SetDataType sets DataType field to given value.


### GetName

`func (o *ColumnSchema) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ColumnSchema) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ColumnSchema) SetName(v string)`

SetName sets Name field to given value.


### GetNullable

`func (o *ColumnSchema) GetNullable() bool`

GetNullable returns the Nullable field if non-nil, zero value otherwise.

### GetNullableOk

`func (o *ColumnSchema) GetNullableOk() (*bool, bool)`

GetNullableOk returns a tuple with the Nullable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNullable

`func (o *ColumnSchema) SetNullable(v bool)`

SetNullable sets Nullable field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


