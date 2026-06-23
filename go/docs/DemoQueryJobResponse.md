# DemoQueryJobResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**JobId** | **string** | Stable id of the job; poll &#x60;/demo/query/{job_id}&#x60; for status and the result URL. | 
**Status** | [**JobStatus**](JobStatus.md) |  | 

## Methods

### NewDemoQueryJobResponse

`func NewDemoQueryJobResponse(jobId string, status JobStatus, ) *DemoQueryJobResponse`

NewDemoQueryJobResponse instantiates a new DemoQueryJobResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDemoQueryJobResponseWithDefaults

`func NewDemoQueryJobResponseWithDefaults() *DemoQueryJobResponse`

NewDemoQueryJobResponseWithDefaults instantiates a new DemoQueryJobResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetJobId

`func (o *DemoQueryJobResponse) GetJobId() string`

GetJobId returns the JobId field if non-nil, zero value otherwise.

### GetJobIdOk

`func (o *DemoQueryJobResponse) GetJobIdOk() (*string, bool)`

GetJobIdOk returns a tuple with the JobId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJobId

`func (o *DemoQueryJobResponse) SetJobId(v string)`

SetJobId sets JobId field to given value.


### GetStatus

`func (o *DemoQueryJobResponse) GetStatus() JobStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *DemoQueryJobResponse) GetStatusOk() (*JobStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *DemoQueryJobResponse) SetStatus(v JobStatus)`

SetStatus sets Status field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


