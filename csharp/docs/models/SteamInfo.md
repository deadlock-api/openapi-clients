# DeadlockApiClient.Model.SteamInfo
Per-patch Steam manifest as served by the public assets API.  Field order is load-bearing — it sets the JSON key order, which matches the legacy Python endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AppId** | **int** |  | 
**ClientVersion** | **int** |  | 
**ProductName** | **string** |  | 
**ServerAppId** | **int** |  | 
**ServerVersion** | **int** |  | 
**SourceRevision** | **long** |  | 
**ToolsAppId** | **int** |  | 
**VersionDate** | **string** |  | 
**VersionDatetime** | **string** | &#x60;version_date&#x60; + &#x60;version_time&#x60; combined into a naive ISO-8601 string (&#x60;YYYY-MM-DDTHH:MM:SS&#x60;, no timezone) — matches the Python output. | 
**VersionTime** | **string** |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

