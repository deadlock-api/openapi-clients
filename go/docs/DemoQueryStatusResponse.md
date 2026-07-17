# DemoQueryStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Error** | Pointer to **NullableString** | Failure reason, once &#x60;failed&#x60;. | [optional] 
**EstimatedWaitSeconds** | Pointer to **NullableInt64** | Rough seconds until the result is ready, while &#x60;queued&#x60; or &#x60;running&#x60;. | [optional] 
**Format** | [**OutputFormat**](OutputFormat.md) |  | 
**JobId** | **string** |  | 
**MatchId** | **int64** |  | 
**ResultUrl** | Pointer to **NullableString** | Public URL of the result artifact, once &#x60;done&#x60;. NDJSON results are zstd-compressed (&#x60;.ndjson.zst&#x60;); Parquet results are served as-is. | [optional] 
**Status** | [**JobStatus**](JobStatus.md) |  | 

## Methods

### NewDemoQueryStatusResponse

`func NewDemoQueryStatusResponse(format OutputFormat, jobId string, matchId int64, status JobStatus, ) *DemoQueryStatusResponse`

NewDemoQueryStatusResponse instantiates a new DemoQueryStatusResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDemoQueryStatusResponseWithDefaults

`func NewDemoQueryStatusResponseWithDefaults() *DemoQueryStatusResponse`

NewDemoQueryStatusResponseWithDefaults instantiates a new DemoQueryStatusResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetError

`func (o *DemoQueryStatusResponse) GetError() string`

GetError returns the Error field if non-nil, zero value otherwise.

### GetErrorOk

`func (o *DemoQueryStatusResponse) GetErrorOk() (*string, bool)`

GetErrorOk returns a tuple with the Error field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetError

`func (o *DemoQueryStatusResponse) SetError(v string)`

SetError sets Error field to given value.

### HasError

`func (o *DemoQueryStatusResponse) HasError() bool`

HasError returns a boolean if a field has been set.

### SetErrorNil

`func (o *DemoQueryStatusResponse) SetErrorNil(b bool)`

 SetErrorNil sets the value for Error to be an explicit nil

### UnsetError
`func (o *DemoQueryStatusResponse) UnsetError()`

UnsetError ensures that no value is present for Error, not even an explicit nil
### GetEstimatedWaitSeconds

`func (o *DemoQueryStatusResponse) GetEstimatedWaitSeconds() int64`

GetEstimatedWaitSeconds returns the EstimatedWaitSeconds field if non-nil, zero value otherwise.

### GetEstimatedWaitSecondsOk

`func (o *DemoQueryStatusResponse) GetEstimatedWaitSecondsOk() (*int64, bool)`

GetEstimatedWaitSecondsOk returns a tuple with the EstimatedWaitSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEstimatedWaitSeconds

`func (o *DemoQueryStatusResponse) SetEstimatedWaitSeconds(v int64)`

SetEstimatedWaitSeconds sets EstimatedWaitSeconds field to given value.

### HasEstimatedWaitSeconds

`func (o *DemoQueryStatusResponse) HasEstimatedWaitSeconds() bool`

HasEstimatedWaitSeconds returns a boolean if a field has been set.

### SetEstimatedWaitSecondsNil

`func (o *DemoQueryStatusResponse) SetEstimatedWaitSecondsNil(b bool)`

 SetEstimatedWaitSecondsNil sets the value for EstimatedWaitSeconds to be an explicit nil

### UnsetEstimatedWaitSeconds
`func (o *DemoQueryStatusResponse) UnsetEstimatedWaitSeconds()`

UnsetEstimatedWaitSeconds ensures that no value is present for EstimatedWaitSeconds, not even an explicit nil
### GetFormat

`func (o *DemoQueryStatusResponse) GetFormat() OutputFormat`

GetFormat returns the Format field if non-nil, zero value otherwise.

### GetFormatOk

`func (o *DemoQueryStatusResponse) GetFormatOk() (*OutputFormat, bool)`

GetFormatOk returns a tuple with the Format field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFormat

`func (o *DemoQueryStatusResponse) SetFormat(v OutputFormat)`

SetFormat sets Format field to given value.


### GetJobId

`func (o *DemoQueryStatusResponse) GetJobId() string`

GetJobId returns the JobId field if non-nil, zero value otherwise.

### GetJobIdOk

`func (o *DemoQueryStatusResponse) GetJobIdOk() (*string, bool)`

GetJobIdOk returns a tuple with the JobId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJobId

`func (o *DemoQueryStatusResponse) SetJobId(v string)`

SetJobId sets JobId field to given value.


### GetMatchId

`func (o *DemoQueryStatusResponse) GetMatchId() int64`

GetMatchId returns the MatchId field if non-nil, zero value otherwise.

### GetMatchIdOk

`func (o *DemoQueryStatusResponse) GetMatchIdOk() (*int64, bool)`

GetMatchIdOk returns a tuple with the MatchId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchId

`func (o *DemoQueryStatusResponse) SetMatchId(v int64)`

SetMatchId sets MatchId field to given value.


### GetResultUrl

`func (o *DemoQueryStatusResponse) GetResultUrl() string`

GetResultUrl returns the ResultUrl field if non-nil, zero value otherwise.

### GetResultUrlOk

`func (o *DemoQueryStatusResponse) GetResultUrlOk() (*string, bool)`

GetResultUrlOk returns a tuple with the ResultUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResultUrl

`func (o *DemoQueryStatusResponse) SetResultUrl(v string)`

SetResultUrl sets ResultUrl field to given value.

### HasResultUrl

`func (o *DemoQueryStatusResponse) HasResultUrl() bool`

HasResultUrl returns a boolean if a field has been set.

### SetResultUrlNil

`func (o *DemoQueryStatusResponse) SetResultUrlNil(b bool)`

 SetResultUrlNil sets the value for ResultUrl to be an explicit nil

### UnsetResultUrl
`func (o *DemoQueryStatusResponse) UnsetResultUrl()`

UnsetResultUrl ensures that no value is present for ResultUrl, not even an explicit nil
### GetStatus

`func (o *DemoQueryStatusResponse) GetStatus() JobStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *DemoQueryStatusResponse) GetStatusOk() (*JobStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *DemoQueryStatusResponse) SetStatus(v JobStatus)`

SetStatus sets Status field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


