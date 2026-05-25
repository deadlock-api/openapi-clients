# APIInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FetchedMatchesPerDay** | Pointer to **NullableInt64** | The number of matches fetched in the last 24 hours. | [optional] 
**TableSizes** | Pointer to [**map[string]TableSize**](TableSize.md) | The sizes of all tables in the database. | [optional] 
**UserIngestedMatchesLast24h** | Pointer to **NullableInt64** | The number of matches ingested in the last 24 hours. | [optional] 

## Methods

### NewAPIInfo

`func NewAPIInfo() *APIInfo`

NewAPIInfo instantiates a new APIInfo object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAPIInfoWithDefaults

`func NewAPIInfoWithDefaults() *APIInfo`

NewAPIInfoWithDefaults instantiates a new APIInfo object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFetchedMatchesPerDay

`func (o *APIInfo) GetFetchedMatchesPerDay() int64`

GetFetchedMatchesPerDay returns the FetchedMatchesPerDay field if non-nil, zero value otherwise.

### GetFetchedMatchesPerDayOk

`func (o *APIInfo) GetFetchedMatchesPerDayOk() (*int64, bool)`

GetFetchedMatchesPerDayOk returns a tuple with the FetchedMatchesPerDay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFetchedMatchesPerDay

`func (o *APIInfo) SetFetchedMatchesPerDay(v int64)`

SetFetchedMatchesPerDay sets FetchedMatchesPerDay field to given value.

### HasFetchedMatchesPerDay

`func (o *APIInfo) HasFetchedMatchesPerDay() bool`

HasFetchedMatchesPerDay returns a boolean if a field has been set.

### SetFetchedMatchesPerDayNil

`func (o *APIInfo) SetFetchedMatchesPerDayNil(b bool)`

 SetFetchedMatchesPerDayNil sets the value for FetchedMatchesPerDay to be an explicit nil

### UnsetFetchedMatchesPerDay
`func (o *APIInfo) UnsetFetchedMatchesPerDay()`

UnsetFetchedMatchesPerDay ensures that no value is present for FetchedMatchesPerDay, not even an explicit nil
### GetTableSizes

`func (o *APIInfo) GetTableSizes() map[string]TableSize`

GetTableSizes returns the TableSizes field if non-nil, zero value otherwise.

### GetTableSizesOk

`func (o *APIInfo) GetTableSizesOk() (*map[string]TableSize, bool)`

GetTableSizesOk returns a tuple with the TableSizes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTableSizes

`func (o *APIInfo) SetTableSizes(v map[string]TableSize)`

SetTableSizes sets TableSizes field to given value.

### HasTableSizes

`func (o *APIInfo) HasTableSizes() bool`

HasTableSizes returns a boolean if a field has been set.

### GetUserIngestedMatchesLast24h

`func (o *APIInfo) GetUserIngestedMatchesLast24h() int64`

GetUserIngestedMatchesLast24h returns the UserIngestedMatchesLast24h field if non-nil, zero value otherwise.

### GetUserIngestedMatchesLast24hOk

`func (o *APIInfo) GetUserIngestedMatchesLast24hOk() (*int64, bool)`

GetUserIngestedMatchesLast24hOk returns a tuple with the UserIngestedMatchesLast24h field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserIngestedMatchesLast24h

`func (o *APIInfo) SetUserIngestedMatchesLast24h(v int64)`

SetUserIngestedMatchesLast24h sets UserIngestedMatchesLast24h field to given value.

### HasUserIngestedMatchesLast24h

`func (o *APIInfo) HasUserIngestedMatchesLast24h() bool`

HasUserIngestedMatchesLast24h returns a boolean if a field has been set.

### SetUserIngestedMatchesLast24hNil

`func (o *APIInfo) SetUserIngestedMatchesLast24hNil(b bool)`

 SetUserIngestedMatchesLast24hNil sets the value for UserIngestedMatchesLast24h to be an explicit nil

### UnsetUserIngestedMatchesLast24h
`func (o *APIInfo) UnsetUserIngestedMatchesLast24h()`

UnsetUserIngestedMatchesLast24h ensures that no value is present for UserIngestedMatchesLast24h, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


