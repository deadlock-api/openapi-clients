# TableSchemaResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Columns** | [**[]ColumnSchema**](ColumnSchema.md) |  | 
**Kind** | **string** | &#x60;entity&#x60; for tables discovered from the demo&#39;s send-tables, &#x60;event&#x60; for the event tables common to every demo. | 
**Name** | **string** |  | 

## Methods

### NewTableSchemaResponse

`func NewTableSchemaResponse(columns []ColumnSchema, kind string, name string, ) *TableSchemaResponse`

NewTableSchemaResponse instantiates a new TableSchemaResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTableSchemaResponseWithDefaults

`func NewTableSchemaResponseWithDefaults() *TableSchemaResponse`

NewTableSchemaResponseWithDefaults instantiates a new TableSchemaResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetColumns

`func (o *TableSchemaResponse) GetColumns() []ColumnSchema`

GetColumns returns the Columns field if non-nil, zero value otherwise.

### GetColumnsOk

`func (o *TableSchemaResponse) GetColumnsOk() (*[]ColumnSchema, bool)`

GetColumnsOk returns a tuple with the Columns field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColumns

`func (o *TableSchemaResponse) SetColumns(v []ColumnSchema)`

SetColumns sets Columns field to given value.


### GetKind

`func (o *TableSchemaResponse) GetKind() string`

GetKind returns the Kind field if non-nil, zero value otherwise.

### GetKindOk

`func (o *TableSchemaResponse) GetKindOk() (*string, bool)`

GetKindOk returns a tuple with the Kind field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKind

`func (o *TableSchemaResponse) SetKind(v string)`

SetKind sets Kind field to given value.


### GetName

`func (o *TableSchemaResponse) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *TableSchemaResponse) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *TableSchemaResponse) SetName(v string)`

SetName sets Name field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


