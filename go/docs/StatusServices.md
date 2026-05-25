# StatusServices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Clickhouse** | **bool** | Whether Clickhouse is reachable. | 
**Postgres** | **bool** | Whether Postgres is reachable. | 
**Redis** | **bool** | Whether Redis is reachable. | 

## Methods

### NewStatusServices

`func NewStatusServices(clickhouse bool, postgres bool, redis bool, ) *StatusServices`

NewStatusServices instantiates a new StatusServices object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStatusServicesWithDefaults

`func NewStatusServicesWithDefaults() *StatusServices`

NewStatusServicesWithDefaults instantiates a new StatusServices object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClickhouse

`func (o *StatusServices) GetClickhouse() bool`

GetClickhouse returns the Clickhouse field if non-nil, zero value otherwise.

### GetClickhouseOk

`func (o *StatusServices) GetClickhouseOk() (*bool, bool)`

GetClickhouseOk returns a tuple with the Clickhouse field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClickhouse

`func (o *StatusServices) SetClickhouse(v bool)`

SetClickhouse sets Clickhouse field to given value.


### GetPostgres

`func (o *StatusServices) GetPostgres() bool`

GetPostgres returns the Postgres field if non-nil, zero value otherwise.

### GetPostgresOk

`func (o *StatusServices) GetPostgresOk() (*bool, bool)`

GetPostgresOk returns a tuple with the Postgres field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostgres

`func (o *StatusServices) SetPostgres(v bool)`

SetPostgres sets Postgres field to given value.


### GetRedis

`func (o *StatusServices) GetRedis() bool`

GetRedis returns the Redis field if non-nil, zero value otherwise.

### GetRedisOk

`func (o *StatusServices) GetRedisOk() (*bool, bool)`

GetRedisOk returns a tuple with the Redis field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRedis

`func (o *StatusServices) SetRedis(v bool)`

SetRedis sets Redis field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


