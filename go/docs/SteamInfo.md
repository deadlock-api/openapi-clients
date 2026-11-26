# SteamInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AppId** | **int64** |  | 
**ClientVersion** | **int64** |  | 
**ProductName** | **string** |  | 
**ServerAppId** | **int64** |  | 
**ServerVersion** | **int64** |  | 
**SourceRevision** | **int64** |  | 
**ToolsAppId** | **int64** |  | 
**VersionDate** | **string** |  | 
**VersionDatetime** | **string** | &#x60;version_date&#x60; + &#x60;version_time&#x60; combined into a naive ISO-8601 string (&#x60;YYYY-MM-DDTHH:MM:SS&#x60;, no timezone). | 
**VersionTime** | **string** |  | 

## Methods

### NewSteamInfo

`func NewSteamInfo(appId int64, clientVersion int64, productName string, serverAppId int64, serverVersion int64, sourceRevision int64, toolsAppId int64, versionDate string, versionDatetime string, versionTime string, ) *SteamInfo`

NewSteamInfo instantiates a new SteamInfo object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSteamInfoWithDefaults

`func NewSteamInfoWithDefaults() *SteamInfo`

NewSteamInfoWithDefaults instantiates a new SteamInfo object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAppId

`func (o *SteamInfo) GetAppId() int64`

GetAppId returns the AppId field if non-nil, zero value otherwise.

### GetAppIdOk

`func (o *SteamInfo) GetAppIdOk() (*int64, bool)`

GetAppIdOk returns a tuple with the AppId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAppId

`func (o *SteamInfo) SetAppId(v int64)`

SetAppId sets AppId field to given value.


### GetClientVersion

`func (o *SteamInfo) GetClientVersion() int64`

GetClientVersion returns the ClientVersion field if non-nil, zero value otherwise.

### GetClientVersionOk

`func (o *SteamInfo) GetClientVersionOk() (*int64, bool)`

GetClientVersionOk returns a tuple with the ClientVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientVersion

`func (o *SteamInfo) SetClientVersion(v int64)`

SetClientVersion sets ClientVersion field to given value.


### GetProductName

`func (o *SteamInfo) GetProductName() string`

GetProductName returns the ProductName field if non-nil, zero value otherwise.

### GetProductNameOk

`func (o *SteamInfo) GetProductNameOk() (*string, bool)`

GetProductNameOk returns a tuple with the ProductName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProductName

`func (o *SteamInfo) SetProductName(v string)`

SetProductName sets ProductName field to given value.


### GetServerAppId

`func (o *SteamInfo) GetServerAppId() int64`

GetServerAppId returns the ServerAppId field if non-nil, zero value otherwise.

### GetServerAppIdOk

`func (o *SteamInfo) GetServerAppIdOk() (*int64, bool)`

GetServerAppIdOk returns a tuple with the ServerAppId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetServerAppId

`func (o *SteamInfo) SetServerAppId(v int64)`

SetServerAppId sets ServerAppId field to given value.


### GetServerVersion

`func (o *SteamInfo) GetServerVersion() int64`

GetServerVersion returns the ServerVersion field if non-nil, zero value otherwise.

### GetServerVersionOk

`func (o *SteamInfo) GetServerVersionOk() (*int64, bool)`

GetServerVersionOk returns a tuple with the ServerVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetServerVersion

`func (o *SteamInfo) SetServerVersion(v int64)`

SetServerVersion sets ServerVersion field to given value.


### GetSourceRevision

`func (o *SteamInfo) GetSourceRevision() int64`

GetSourceRevision returns the SourceRevision field if non-nil, zero value otherwise.

### GetSourceRevisionOk

`func (o *SteamInfo) GetSourceRevisionOk() (*int64, bool)`

GetSourceRevisionOk returns a tuple with the SourceRevision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceRevision

`func (o *SteamInfo) SetSourceRevision(v int64)`

SetSourceRevision sets SourceRevision field to given value.


### GetToolsAppId

`func (o *SteamInfo) GetToolsAppId() int64`

GetToolsAppId returns the ToolsAppId field if non-nil, zero value otherwise.

### GetToolsAppIdOk

`func (o *SteamInfo) GetToolsAppIdOk() (*int64, bool)`

GetToolsAppIdOk returns a tuple with the ToolsAppId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolsAppId

`func (o *SteamInfo) SetToolsAppId(v int64)`

SetToolsAppId sets ToolsAppId field to given value.


### GetVersionDate

`func (o *SteamInfo) GetVersionDate() string`

GetVersionDate returns the VersionDate field if non-nil, zero value otherwise.

### GetVersionDateOk

`func (o *SteamInfo) GetVersionDateOk() (*string, bool)`

GetVersionDateOk returns a tuple with the VersionDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersionDate

`func (o *SteamInfo) SetVersionDate(v string)`

SetVersionDate sets VersionDate field to given value.


### GetVersionDatetime

`func (o *SteamInfo) GetVersionDatetime() string`

GetVersionDatetime returns the VersionDatetime field if non-nil, zero value otherwise.

### GetVersionDatetimeOk

`func (o *SteamInfo) GetVersionDatetimeOk() (*string, bool)`

GetVersionDatetimeOk returns a tuple with the VersionDatetime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersionDatetime

`func (o *SteamInfo) SetVersionDatetime(v string)`

SetVersionDatetime sets VersionDatetime field to given value.


### GetVersionTime

`func (o *SteamInfo) GetVersionTime() string`

GetVersionTime returns the VersionTime field if non-nil, zero value otherwise.

### GetVersionTimeOk

`func (o *SteamInfo) GetVersionTimeOk() (*string, bool)`

GetVersionTimeOk returns a tuple with the VersionTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersionTime

`func (o *SteamInfo) SetVersionTime(v string)`

SetVersionTime sets VersionTime field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


