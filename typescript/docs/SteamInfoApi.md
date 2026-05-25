# SteamInfoApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getAllSteamInfo**](#getallsteaminfo) | **GET** /v1/assets/steam-info/all | Get All Steam Infos|
|[**getSteamInfo**](#getsteaminfo) | **GET** /v1/assets/steam-info | Get Steam Info|

# **getAllSteamInfo**
> Array<SteamInfo> getAllSteamInfo()

Returns the `steam.inf` manifest for every known patch as a single array, newest version first. Replaces the legacy `/v1/steam-info/all` endpoint.

### Example

```typescript
import {
    SteamInfoApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new SteamInfoApi(configuration);

const { status, data } = await apiInstance.getAllSteamInfo();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Array<SteamInfo>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getSteamInfo**
> SteamInfo getSteamInfo()

Returns the `steam.inf` manifest published with the patch (client/server version, app IDs, source revision, build timestamp).

### Example

```typescript
import {
    SteamInfoApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new SteamInfoApi(configuration);

let clientVersion: number; //Client/game version (e.g. `6518`). Defaults to the latest known version. (optional) (default to undefined)

const { status, data } = await apiInstance.getSteamInfo(
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientVersion** | [**number**] | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | (optional) defaults to undefined|


### Return type

**SteamInfo**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**404** | Requested client_version is not available |  -  |
|**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

