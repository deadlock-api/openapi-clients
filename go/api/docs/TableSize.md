# TableSize

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DataCompressedBytes** | Pointer to **NullableInt64** | Compressed size of the table in bytes. | [optional] 
**DataUncompressedBytes** | Pointer to **NullableInt64** | Uncompressed size of the table in bytes. | [optional] 
**IsView** | **bool** | Whether the table is a view. | 
**Rows** | Pointer to **NullableInt64** | Number of rows in the table. | [optional] 

## Methods

### NewTableSize

`func NewTableSize(isView bool, ) *TableSize`

NewTableSize instantiates a new TableSize object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTableSizeWithDefaults

`func NewTableSizeWithDefaults() *TableSize`

NewTableSizeWithDefaults instantiates a new TableSize object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDataCompressedBytes

`func (o *TableSize) GetDataCompressedBytes() int64`

GetDataCompressedBytes returns the DataCompressedBytes field if non-nil, zero value otherwise.

### GetDataCompressedBytesOk

`func (o *TableSize) GetDataCompressedBytesOk() (*int64, bool)`

GetDataCompressedBytesOk returns a tuple with the DataCompressedBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDataCompressedBytes

`func (o *TableSize) SetDataCompressedBytes(v int64)`

SetDataCompressedBytes sets DataCompressedBytes field to given value.

### HasDataCompressedBytes

`func (o *TableSize) HasDataCompressedBytes() bool`

HasDataCompressedBytes returns a boolean if a field has been set.

### SetDataCompressedBytesNil

`func (o *TableSize) SetDataCompressedBytesNil(b bool)`

 SetDataCompressedBytesNil sets the value for DataCompressedBytes to be an explicit nil

### UnsetDataCompressedBytes
`func (o *TableSize) UnsetDataCompressedBytes()`

UnsetDataCompressedBytes ensures that no value is present for DataCompressedBytes, not even an explicit nil
### GetDataUncompressedBytes

`func (o *TableSize) GetDataUncompressedBytes() int64`

GetDataUncompressedBytes returns the DataUncompressedBytes field if non-nil, zero value otherwise.

### GetDataUncompressedBytesOk

`func (o *TableSize) GetDataUncompressedBytesOk() (*int64, bool)`

GetDataUncompressedBytesOk returns a tuple with the DataUncompressedBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDataUncompressedBytes

`func (o *TableSize) SetDataUncompressedBytes(v int64)`

SetDataUncompressedBytes sets DataUncompressedBytes field to given value.

### HasDataUncompressedBytes

`func (o *TableSize) HasDataUncompressedBytes() bool`

HasDataUncompressedBytes returns a boolean if a field has been set.

### SetDataUncompressedBytesNil

`func (o *TableSize) SetDataUncompressedBytesNil(b bool)`

 SetDataUncompressedBytesNil sets the value for DataUncompressedBytes to be an explicit nil

### UnsetDataUncompressedBytes
`func (o *TableSize) UnsetDataUncompressedBytes()`

UnsetDataUncompressedBytes ensures that no value is present for DataUncompressedBytes, not even an explicit nil
### GetIsView

`func (o *TableSize) GetIsView() bool`

GetIsView returns the IsView field if non-nil, zero value otherwise.

### GetIsViewOk

`func (o *TableSize) GetIsViewOk() (*bool, bool)`

GetIsViewOk returns a tuple with the IsView field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsView

`func (o *TableSize) SetIsView(v bool)`

SetIsView sets IsView field to given value.


### GetRows

`func (o *TableSize) GetRows() int64`

GetRows returns the Rows field if non-nil, zero value otherwise.

### GetRowsOk

`func (o *TableSize) GetRowsOk() (*int64, bool)`

GetRowsOk returns a tuple with the Rows field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRows

`func (o *TableSize) SetRows(v int64)`

SetRows sets Rows field to given value.

### HasRows

`func (o *TableSize) HasRows() bool`

HasRows returns a boolean if a field has been set.

### SetRowsNil

`func (o *TableSize) SetRowsNil(b bool)`

 SetRowsNil sets the value for Rows to be an explicit nil

### UnsetRows
`func (o *TableSize) UnsetRows()`

UnsetRows ensures that no value is present for Rows, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


