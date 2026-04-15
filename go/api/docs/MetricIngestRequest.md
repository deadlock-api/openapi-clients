# MetricIngestRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **int32** | Steam account id (&#x60;UInt32&#x60;) of the player this metric is about | 
**GameMode** | **string** | Game mode this metric applies to (e.g. \&quot;speedrun\&quot;) | 
**GameModeVersion** | Pointer to **NullableString** | Optional game-mode version tag (e.g. \&quot;v2\&quot;, \&quot;season3\&quot;) for versioning leaderboards | [optional] 
**Map** | Pointer to **NullableString** | Optional map identifier the metric was produced on | [optional] 
**Metadata** | Pointer to **map[string]string** | Free-form key/value metadata for game-mode-specific context | [optional] 
**MetricName** | **string** | Name of the metric (e.g. &#x60;run_time&#x60;) | 
**MetricValue** | **float64** | The primary numeric measurement for this metric | 
**Region** | **string** | Region the server is located in (e.g. \&quot;eu\&quot;, \&quot;na\&quot;) | 
**ServerId** | **string** | Unique identifier for the game server reporting the metric | 

## Methods

### NewMetricIngestRequest

`func NewMetricIngestRequest(accountId int32, gameMode string, metricName string, metricValue float64, region string, serverId string, ) *MetricIngestRequest`

NewMetricIngestRequest instantiates a new MetricIngestRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMetricIngestRequestWithDefaults

`func NewMetricIngestRequestWithDefaults() *MetricIngestRequest`

NewMetricIngestRequestWithDefaults instantiates a new MetricIngestRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccountId

`func (o *MetricIngestRequest) GetAccountId() int32`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *MetricIngestRequest) GetAccountIdOk() (*int32, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *MetricIngestRequest) SetAccountId(v int32)`

SetAccountId sets AccountId field to given value.


### GetGameMode

`func (o *MetricIngestRequest) GetGameMode() string`

GetGameMode returns the GameMode field if non-nil, zero value otherwise.

### GetGameModeOk

`func (o *MetricIngestRequest) GetGameModeOk() (*string, bool)`

GetGameModeOk returns a tuple with the GameMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGameMode

`func (o *MetricIngestRequest) SetGameMode(v string)`

SetGameMode sets GameMode field to given value.


### GetGameModeVersion

`func (o *MetricIngestRequest) GetGameModeVersion() string`

GetGameModeVersion returns the GameModeVersion field if non-nil, zero value otherwise.

### GetGameModeVersionOk

`func (o *MetricIngestRequest) GetGameModeVersionOk() (*string, bool)`

GetGameModeVersionOk returns a tuple with the GameModeVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGameModeVersion

`func (o *MetricIngestRequest) SetGameModeVersion(v string)`

SetGameModeVersion sets GameModeVersion field to given value.

### HasGameModeVersion

`func (o *MetricIngestRequest) HasGameModeVersion() bool`

HasGameModeVersion returns a boolean if a field has been set.

### SetGameModeVersionNil

`func (o *MetricIngestRequest) SetGameModeVersionNil(b bool)`

 SetGameModeVersionNil sets the value for GameModeVersion to be an explicit nil

### UnsetGameModeVersion
`func (o *MetricIngestRequest) UnsetGameModeVersion()`

UnsetGameModeVersion ensures that no value is present for GameModeVersion, not even an explicit nil
### GetMap

`func (o *MetricIngestRequest) GetMap() string`

GetMap returns the Map field if non-nil, zero value otherwise.

### GetMapOk

`func (o *MetricIngestRequest) GetMapOk() (*string, bool)`

GetMapOk returns a tuple with the Map field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMap

`func (o *MetricIngestRequest) SetMap(v string)`

SetMap sets Map field to given value.

### HasMap

`func (o *MetricIngestRequest) HasMap() bool`

HasMap returns a boolean if a field has been set.

### SetMapNil

`func (o *MetricIngestRequest) SetMapNil(b bool)`

 SetMapNil sets the value for Map to be an explicit nil

### UnsetMap
`func (o *MetricIngestRequest) UnsetMap()`

UnsetMap ensures that no value is present for Map, not even an explicit nil
### GetMetadata

`func (o *MetricIngestRequest) GetMetadata() map[string]string`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *MetricIngestRequest) GetMetadataOk() (*map[string]string, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *MetricIngestRequest) SetMetadata(v map[string]string)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *MetricIngestRequest) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### GetMetricName

`func (o *MetricIngestRequest) GetMetricName() string`

GetMetricName returns the MetricName field if non-nil, zero value otherwise.

### GetMetricNameOk

`func (o *MetricIngestRequest) GetMetricNameOk() (*string, bool)`

GetMetricNameOk returns a tuple with the MetricName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetricName

`func (o *MetricIngestRequest) SetMetricName(v string)`

SetMetricName sets MetricName field to given value.


### GetMetricValue

`func (o *MetricIngestRequest) GetMetricValue() float64`

GetMetricValue returns the MetricValue field if non-nil, zero value otherwise.

### GetMetricValueOk

`func (o *MetricIngestRequest) GetMetricValueOk() (*float64, bool)`

GetMetricValueOk returns a tuple with the MetricValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetricValue

`func (o *MetricIngestRequest) SetMetricValue(v float64)`

SetMetricValue sets MetricValue field to given value.


### GetRegion

`func (o *MetricIngestRequest) GetRegion() string`

GetRegion returns the Region field if non-nil, zero value otherwise.

### GetRegionOk

`func (o *MetricIngestRequest) GetRegionOk() (*string, bool)`

GetRegionOk returns a tuple with the Region field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegion

`func (o *MetricIngestRequest) SetRegion(v string)`

SetRegion sets Region field to given value.


### GetServerId

`func (o *MetricIngestRequest) GetServerId() string`

GetServerId returns the ServerId field if non-nil, zero value otherwise.

### GetServerIdOk

`func (o *MetricIngestRequest) GetServerIdOk() (*string, bool)`

GetServerIdOk returns a tuple with the ServerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetServerId

`func (o *MetricIngestRequest) SetServerId(v string)`

SetServerId sets ServerId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


