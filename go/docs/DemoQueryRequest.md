# DemoQueryRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Format** | Pointer to [**OutputFormat**](OutputFormat.md) | Output format of the result artifact. | [optional] 
**MatchId** | **int64** | Match whose demo to query. | 
**Query** | **string** | SQL query to run over the demo&#39;s entity/event tables (see &#x60;/demo/schema&#x60;). | 

## Methods

### NewDemoQueryRequest

`func NewDemoQueryRequest(matchId int64, query string, ) *DemoQueryRequest`

NewDemoQueryRequest instantiates a new DemoQueryRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDemoQueryRequestWithDefaults

`func NewDemoQueryRequestWithDefaults() *DemoQueryRequest`

NewDemoQueryRequestWithDefaults instantiates a new DemoQueryRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFormat

`func (o *DemoQueryRequest) GetFormat() OutputFormat`

GetFormat returns the Format field if non-nil, zero value otherwise.

### GetFormatOk

`func (o *DemoQueryRequest) GetFormatOk() (*OutputFormat, bool)`

GetFormatOk returns a tuple with the Format field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFormat

`func (o *DemoQueryRequest) SetFormat(v OutputFormat)`

SetFormat sets Format field to given value.

### HasFormat

`func (o *DemoQueryRequest) HasFormat() bool`

HasFormat returns a boolean if a field has been set.

### GetMatchId

`func (o *DemoQueryRequest) GetMatchId() int64`

GetMatchId returns the MatchId field if non-nil, zero value otherwise.

### GetMatchIdOk

`func (o *DemoQueryRequest) GetMatchIdOk() (*int64, bool)`

GetMatchIdOk returns a tuple with the MatchId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchId

`func (o *DemoQueryRequest) SetMatchId(v int64)`

SetMatchId sets MatchId field to given value.


### GetQuery

`func (o *DemoQueryRequest) GetQuery() string`

GetQuery returns the Query field if non-nil, zero value otherwise.

### GetQueryOk

`func (o *DemoQueryRequest) GetQueryOk() (*string, bool)`

GetQueryOk returns a tuple with the Query field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQuery

`func (o *DemoQueryRequest) SetQuery(v string)`

SetQuery sets Query field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


