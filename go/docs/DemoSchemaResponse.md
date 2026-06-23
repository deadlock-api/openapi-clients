# DemoSchemaResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DemoUrl** | **string** |  | 
**MatchId** | **int64** |  | 
**Tables** | [**[]TableSchemaResponse**](TableSchemaResponse.md) |  | 

## Methods

### NewDemoSchemaResponse

`func NewDemoSchemaResponse(demoUrl string, matchId int64, tables []TableSchemaResponse, ) *DemoSchemaResponse`

NewDemoSchemaResponse instantiates a new DemoSchemaResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDemoSchemaResponseWithDefaults

`func NewDemoSchemaResponseWithDefaults() *DemoSchemaResponse`

NewDemoSchemaResponseWithDefaults instantiates a new DemoSchemaResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDemoUrl

`func (o *DemoSchemaResponse) GetDemoUrl() string`

GetDemoUrl returns the DemoUrl field if non-nil, zero value otherwise.

### GetDemoUrlOk

`func (o *DemoSchemaResponse) GetDemoUrlOk() (*string, bool)`

GetDemoUrlOk returns a tuple with the DemoUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDemoUrl

`func (o *DemoSchemaResponse) SetDemoUrl(v string)`

SetDemoUrl sets DemoUrl field to given value.


### GetMatchId

`func (o *DemoSchemaResponse) GetMatchId() int64`

GetMatchId returns the MatchId field if non-nil, zero value otherwise.

### GetMatchIdOk

`func (o *DemoSchemaResponse) GetMatchIdOk() (*int64, bool)`

GetMatchIdOk returns a tuple with the MatchId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchId

`func (o *DemoSchemaResponse) SetMatchId(v int64)`

SetMatchId sets MatchId field to given value.


### GetTables

`func (o *DemoSchemaResponse) GetTables() []TableSchemaResponse`

GetTables returns the Tables field if non-nil, zero value otherwise.

### GetTablesOk

`func (o *DemoSchemaResponse) GetTablesOk() (*[]TableSchemaResponse, bool)`

GetTablesOk returns a tuple with the Tables field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTables

`func (o *DemoSchemaResponse) SetTables(v []TableSchemaResponse)`

SetTables sets Tables field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


