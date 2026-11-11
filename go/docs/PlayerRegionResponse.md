# PlayerRegionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **int32** |  | 
**History** | [**[]PlayerClusterMonth**](PlayerClusterMonth.md) | Matches per month and server cluster, newest month first. | 
**Region** | Pointer to **NullableString** | The region the player played most matches in during their latest month with a known region. &#x60;null&#x60; if none of their matches has a known region. | [optional] 
**RegionMonth** | Pointer to **NullableInt32** | Unix timestamp of the month &#x60;region&#x60; was taken from. | [optional] 

## Methods

### NewPlayerRegionResponse

`func NewPlayerRegionResponse(accountId int32, history []PlayerClusterMonth, ) *PlayerRegionResponse`

NewPlayerRegionResponse instantiates a new PlayerRegionResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPlayerRegionResponseWithDefaults

`func NewPlayerRegionResponseWithDefaults() *PlayerRegionResponse`

NewPlayerRegionResponseWithDefaults instantiates a new PlayerRegionResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccountId

`func (o *PlayerRegionResponse) GetAccountId() int32`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *PlayerRegionResponse) GetAccountIdOk() (*int32, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *PlayerRegionResponse) SetAccountId(v int32)`

SetAccountId sets AccountId field to given value.


### GetHistory

`func (o *PlayerRegionResponse) GetHistory() []PlayerClusterMonth`

GetHistory returns the History field if non-nil, zero value otherwise.

### GetHistoryOk

`func (o *PlayerRegionResponse) GetHistoryOk() (*[]PlayerClusterMonth, bool)`

GetHistoryOk returns a tuple with the History field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHistory

`func (o *PlayerRegionResponse) SetHistory(v []PlayerClusterMonth)`

SetHistory sets History field to given value.


### GetRegion

`func (o *PlayerRegionResponse) GetRegion() string`

GetRegion returns the Region field if non-nil, zero value otherwise.

### GetRegionOk

`func (o *PlayerRegionResponse) GetRegionOk() (*string, bool)`

GetRegionOk returns a tuple with the Region field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegion

`func (o *PlayerRegionResponse) SetRegion(v string)`

SetRegion sets Region field to given value.

### HasRegion

`func (o *PlayerRegionResponse) HasRegion() bool`

HasRegion returns a boolean if a field has been set.

### SetRegionNil

`func (o *PlayerRegionResponse) SetRegionNil(b bool)`

 SetRegionNil sets the value for Region to be an explicit nil

### UnsetRegion
`func (o *PlayerRegionResponse) UnsetRegion()`

UnsetRegion ensures that no value is present for Region, not even an explicit nil
### GetRegionMonth

`func (o *PlayerRegionResponse) GetRegionMonth() int32`

GetRegionMonth returns the RegionMonth field if non-nil, zero value otherwise.

### GetRegionMonthOk

`func (o *PlayerRegionResponse) GetRegionMonthOk() (*int32, bool)`

GetRegionMonthOk returns a tuple with the RegionMonth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegionMonth

`func (o *PlayerRegionResponse) SetRegionMonth(v int32)`

SetRegionMonth sets RegionMonth field to given value.

### HasRegionMonth

`func (o *PlayerRegionResponse) HasRegionMonth() bool`

HasRegionMonth returns a boolean if a field has been set.

### SetRegionMonthNil

`func (o *PlayerRegionResponse) SetRegionMonthNil(b bool)`

 SetRegionMonthNil sets the value for RegionMonth to be an explicit nil

### UnsetRegionMonth
`func (o *PlayerRegionResponse) UnsetRegionMonth()`

UnsetRegionMonth ensures that no value is present for RegionMonth, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


