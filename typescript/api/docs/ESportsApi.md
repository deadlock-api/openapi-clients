# ESportsApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**ingestMatch**](#ingestmatch) | **POST** /v1/esports/ingest/match | Ingest|
|[**matches**](#matches) | **GET** /v1/esports/matches | List Matches|

# **ingestMatch**
> ingestMatch(eSportsMatch)

 To use this Endpoint you need to have special permissions. Please contact us if you organize E-Sports Matches and want to ingest them to us.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 1000req/h | | Key | - | | Global | 10000req/h |     

### Example

```typescript
import {
    ESportsApi,
    Configuration,
    ESportsMatch
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new ESportsApi(configuration);

let eSportsMatch: ESportsMatch; //

const { status, data } = await apiInstance.ingestMatch(
    eSportsMatch
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **eSportsMatch** | **ESportsMatch**|  | |


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Ingest failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matches**
> Array<ESportsMatch> matches()

 ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    ESportsApi,
    Configuration
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new ESportsApi(configuration);

const { status, data } = await apiInstance.matches();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Array<ESportsMatch>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**400** | Provided parameters are invalid. |  -  |
|**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

