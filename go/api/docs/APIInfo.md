# APIInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FetchedMatchesPerDay** | Pointer to **NullableInt64** | The number of matches fetched in the last 24 hours. | [optional] 
**MissedMatches** | Pointer to **NullableInt64** | The number of matches that have not been fetched. | [optional] 
**TableSizes** | Pointer to [**map[string]TableSize**](TableSize.md) | The sizes of all tables in the database. | [optional] 

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
### GetMissedMatches

`func (o *APIInfo) GetMissedMatches() int64`

GetMissedMatches returns the MissedMatches field if non-nil, zero value otherwise.

### GetMissedMatchesOk

`func (o *APIInfo) GetMissedMatchesOk() (*int64, bool)`

GetMissedMatchesOk returns a tuple with the MissedMatches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMissedMatches

`func (o *APIInfo) SetMissedMatches(v int64)`

SetMissedMatches sets MissedMatches field to given value.

### HasMissedMatches

`func (o *APIInfo) HasMissedMatches() bool`

HasMissedMatches returns a boolean if a field has been set.

### SetMissedMatchesNil

`func (o *APIInfo) SetMissedMatchesNil(b bool)`

 SetMissedMatchesNil sets the value for MissedMatches to be an explicit nil

### UnsetMissedMatches
`func (o *APIInfo) UnsetMissedMatches()`

UnsetMissedMatches ensures that no value is present for MissedMatches, not even an explicit nil
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


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


