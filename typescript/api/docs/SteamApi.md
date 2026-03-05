# SteamApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**steam**](#steam) | **GET** /v1/players/steam | Batch Steam Profile|
|[**steamSearch**](#steamsearch) | **GET** /v1/players/steam-search | Steam Profile Search|

# **steam**
> Array<SteamProfile> steam()

 This endpoint returns Steam profiles of players.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    SteamApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new SteamApi(configuration);

let accountIds: Array<number>; //Comma separated list of account ids, Account IDs are in `SteamID3` format. (default to undefined)

const { status, data } = await apiInstance.steam(
    accountIds
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountIds** | **Array&lt;number&gt;** | Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | defaults to undefined|


### Return type

**Array<SteamProfile>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Steam Profiles |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**404** | No Steam profile found. |  -  |
|**500** | Failed to fetch steam profiles. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **steamSearch**
> Array<SteamProfile> steamSearch()

 This endpoint lets you search for Steam profiles by account_id or personaname.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    SteamApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new SteamApi(configuration);

let searchQuery: string; //Search query for Steam profiles. (default to undefined)

const { status, data } = await apiInstance.steamSearch(
    searchQuery
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **searchQuery** | [**string**] | Search query for Steam profiles. | defaults to undefined|


### Return type

**Array<SteamProfile>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Steam Profile Search |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**404** | No Steam profiles found. |  -  |
|**500** | Failed to fetch steam profiles. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

