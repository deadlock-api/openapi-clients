# ServersApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**list**](#list) | **GET** /v1/servers | List Game Servers|
|[**status**](#status) | **POST** /v1/servers/status | Game Server Status|

# **list**
> ListServersResponse list()

Returns all currently active game servers.

### Example

```typescript
import {
    ServersApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new ServersApi(configuration);

const { status, data } = await apiInstance.list();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**ListServersResponse**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status**
> ServerStatusResponse status(serverStatusRequest)

 Reports the current status of a game server. Game servers must call this endpoint at least once every 30 seconds to remain active. Requires a valid game server secret as a Bearer token.     

### Example

```typescript
import {
    ServersApi,
    Configuration,
    ServerStatusRequest
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new ServersApi(configuration);

let serverStatusRequest: ServerStatusRequest; //

const { status, data } = await apiInstance.status(
    serverStatusRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **serverStatusRequest** | **ServerStatusRequest**|  | |


### Return type

**ServerStatusResponse**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**400** | Invalid request body. |  -  |
|**401** | Invalid or missing game server secret. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

