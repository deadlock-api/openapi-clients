# SteamInfoV1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClientVersion** | **int32** |  | 
**ServerVersion** | **int32** |  | 
**ProductName** | **string** |  | 
**AppId** | **int32** |  | 
**ServerAppId** | **int32** |  | 
**ToolsAppId** | **int32** |  | 
**SourceRevision** | **int32** |  | 
**VersionDate** | **string** |  | 
**VersionTime** | **string** |  | 
**VersionDatetime** | **time.Time** |  | [readonly] 

## Methods

### NewSteamInfoV1

`func NewSteamInfoV1(clientVersion int32, serverVersion int32, productName string, appId int32, serverAppId int32, toolsAppId int32, sourceRevision int32, versionDate string, versionTime string, versionDatetime time.Time, ) *SteamInfoV1`

NewSteamInfoV1 instantiates a new SteamInfoV1 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSteamInfoV1WithDefaults

`func NewSteamInfoV1WithDefaults() *SteamInfoV1`

NewSteamInfoV1WithDefaults instantiates a new SteamInfoV1 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClientVersion

`func (o *SteamInfoV1) GetClientVersion() int32`

GetClientVersion returns the ClientVersion field if non-nil, zero value otherwise.

### GetClientVersionOk

`func (o *SteamInfoV1) GetClientVersionOk() (*int32, bool)`

GetClientVersionOk returns a tuple with the ClientVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientVersion

`func (o *SteamInfoV1) SetClientVersion(v int32)`

SetClientVersion sets ClientVersion field to given value.


### GetServerVersion

`func (o *SteamInfoV1) GetServerVersion() int32`

GetServerVersion returns the ServerVersion field if non-nil, zero value otherwise.

### GetServerVersionOk

`func (o *SteamInfoV1) GetServerVersionOk() (*int32, bool)`

GetServerVersionOk returns a tuple with the ServerVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetServerVersion

`func (o *SteamInfoV1) SetServerVersion(v int32)`

SetServerVersion sets ServerVersion field to given value.


### GetProductName

`func (o *SteamInfoV1) GetProductName() string`

GetProductName returns the ProductName field if non-nil, zero value otherwise.

### GetProductNameOk

`func (o *SteamInfoV1) GetProductNameOk() (*string, bool)`

GetProductNameOk returns a tuple with the ProductName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProductName

`func (o *SteamInfoV1) SetProductName(v string)`

SetProductName sets ProductName field to given value.


### GetAppId

`func (o *SteamInfoV1) GetAppId() int32`

GetAppId returns the AppId field if non-nil, zero value otherwise.

### GetAppIdOk

`func (o *SteamInfoV1) GetAppIdOk() (*int32, bool)`

GetAppIdOk returns a tuple with the AppId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAppId

`func (o *SteamInfoV1) SetAppId(v int32)`

SetAppId sets AppId field to given value.


### GetServerAppId

`func (o *SteamInfoV1) GetServerAppId() int32`

GetServerAppId returns the ServerAppId field if non-nil, zero value otherwise.

### GetServerAppIdOk

`func (o *SteamInfoV1) GetServerAppIdOk() (*int32, bool)`

GetServerAppIdOk returns a tuple with the ServerAppId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetServerAppId

`func (o *SteamInfoV1) SetServerAppId(v int32)`

SetServerAppId sets ServerAppId field to given value.


### GetToolsAppId

`func (o *SteamInfoV1) GetToolsAppId() int32`

GetToolsAppId returns the ToolsAppId field if non-nil, zero value otherwise.

### GetToolsAppIdOk

`func (o *SteamInfoV1) GetToolsAppIdOk() (*int32, bool)`

GetToolsAppIdOk returns a tuple with the ToolsAppId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolsAppId

`func (o *SteamInfoV1) SetToolsAppId(v int32)`

SetToolsAppId sets ToolsAppId field to given value.


### GetSourceRevision

`func (o *SteamInfoV1) GetSourceRevision() int32`

GetSourceRevision returns the SourceRevision field if non-nil, zero value otherwise.

### GetSourceRevisionOk

`func (o *SteamInfoV1) GetSourceRevisionOk() (*int32, bool)`

GetSourceRevisionOk returns a tuple with the SourceRevision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceRevision

`func (o *SteamInfoV1) SetSourceRevision(v int32)`

SetSourceRevision sets SourceRevision field to given value.


### GetVersionDate

`func (o *SteamInfoV1) GetVersionDate() string`

GetVersionDate returns the VersionDate field if non-nil, zero value otherwise.

### GetVersionDateOk

`func (o *SteamInfoV1) GetVersionDateOk() (*string, bool)`

GetVersionDateOk returns a tuple with the VersionDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersionDate

`func (o *SteamInfoV1) SetVersionDate(v string)`

SetVersionDate sets VersionDate field to given value.


### GetVersionTime

`func (o *SteamInfoV1) GetVersionTime() string`

GetVersionTime returns the VersionTime field if non-nil, zero value otherwise.

### GetVersionTimeOk

`func (o *SteamInfoV1) GetVersionTimeOk() (*string, bool)`

GetVersionTimeOk returns a tuple with the VersionTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersionTime

`func (o *SteamInfoV1) SetVersionTime(v string)`

SetVersionTime sets VersionTime field to given value.


### GetVersionDatetime

`func (o *SteamInfoV1) GetVersionDatetime() time.Time`

GetVersionDatetime returns the VersionDatetime field if non-nil, zero value otherwise.

### GetVersionDatetimeOk

`func (o *SteamInfoV1) GetVersionDatetimeOk() (*time.Time, bool)`

GetVersionDatetimeOk returns a tuple with the VersionDatetime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersionDatetime

`func (o *SteamInfoV1) SetVersionDatetime(v time.Time)`

SetVersionDatetime sets VersionDatetime field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


