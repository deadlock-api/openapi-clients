# IngestStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **int64** |  | 
**Active** | **bool** | Whether the ingest tool uploaded a salt for this account within the window that was then verified. | 
**LastUploadAt** | Pointer to **NullableInt64** | Unix timestamp of the most recent verified upload within the window. | [optional] 
**WindowDays** | **int64** | The window, in days, an upload must fall in to count. | 

## Methods

### NewIngestStatusResponse

`func NewIngestStatusResponse(accountId int64, active bool, windowDays int64, ) *IngestStatusResponse`

NewIngestStatusResponse instantiates a new IngestStatusResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewIngestStatusResponseWithDefaults

`func NewIngestStatusResponseWithDefaults() *IngestStatusResponse`

NewIngestStatusResponseWithDefaults instantiates a new IngestStatusResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccountId

`func (o *IngestStatusResponse) GetAccountId() int64`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *IngestStatusResponse) GetAccountIdOk() (*int64, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *IngestStatusResponse) SetAccountId(v int64)`

SetAccountId sets AccountId field to given value.


### GetActive

`func (o *IngestStatusResponse) GetActive() bool`

GetActive returns the Active field if non-nil, zero value otherwise.

### GetActiveOk

`func (o *IngestStatusResponse) GetActiveOk() (*bool, bool)`

GetActiveOk returns a tuple with the Active field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActive

`func (o *IngestStatusResponse) SetActive(v bool)`

SetActive sets Active field to given value.


### GetLastUploadAt

`func (o *IngestStatusResponse) GetLastUploadAt() int64`

GetLastUploadAt returns the LastUploadAt field if non-nil, zero value otherwise.

### GetLastUploadAtOk

`func (o *IngestStatusResponse) GetLastUploadAtOk() (*int64, bool)`

GetLastUploadAtOk returns a tuple with the LastUploadAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastUploadAt

`func (o *IngestStatusResponse) SetLastUploadAt(v int64)`

SetLastUploadAt sets LastUploadAt field to given value.

### HasLastUploadAt

`func (o *IngestStatusResponse) HasLastUploadAt() bool`

HasLastUploadAt returns a boolean if a field has been set.

### SetLastUploadAtNil

`func (o *IngestStatusResponse) SetLastUploadAtNil(b bool)`

 SetLastUploadAtNil sets the value for LastUploadAt to be an explicit nil

### UnsetLastUploadAt
`func (o *IngestStatusResponse) UnsetLastUploadAt()`

UnsetLastUploadAt ensures that no value is present for LastUploadAt, not even an explicit nil
### GetWindowDays

`func (o *IngestStatusResponse) GetWindowDays() int64`

GetWindowDays returns the WindowDays field if non-nil, zero value otherwise.

### GetWindowDaysOk

`func (o *IngestStatusResponse) GetWindowDaysOk() (*int64, bool)`

GetWindowDaysOk returns a tuple with the WindowDays field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWindowDays

`func (o *IngestStatusResponse) SetWindowDays(v int64)`

SetWindowDays sets WindowDays field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


