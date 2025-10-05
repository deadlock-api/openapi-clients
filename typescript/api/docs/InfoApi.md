# InfoApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**healthCheck**](#healthcheck) | **GET** /v1/info/health | Health Check|
|[**info**](#info) | **GET** /v1/info | API Info|

# **healthCheck**
> Status healthCheck()

 Checks the health of the services.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    InfoApi,
    Configuration
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new InfoApi(configuration);

const { status, data } = await apiInstance.healthCheck();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Status**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info**
> APIInfo info()

 Returns information about the API.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    InfoApi,
    Configuration
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new InfoApi(configuration);

const { status, data } = await apiInstance.info();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**APIInfo**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

