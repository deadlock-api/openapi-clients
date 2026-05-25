# ClientVersionsApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**listClientVersions**](#listclientversions) | **GET** /v1/assets/client-versions | List Client Versions|

# **listClientVersions**
> Array<number> listClientVersions()

Returns all known Deadlock client/game versions for which versioned assets are available, sorted ascending (oldest first).

### Example

```typescript
import {
    ClientVersionsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new ClientVersionsApi(configuration);

const { status, data } = await apiInstance.listClientVersions();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Array<number>**

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

