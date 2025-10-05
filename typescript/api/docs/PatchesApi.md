# PatchesApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**bigPatchDays**](#bigpatchdays) | **GET** /v1/patches/big-days | Big Days|
|[**feed**](#feed) | **GET** /v1/patches | Notes|

# **bigPatchDays**
> Array<string> bigPatchDays()

 Returns a list of dates where Deadlock\'s \"big\" patch days were, usually bi-weekly. The exact date is the time when the announcement forum post was published.  This list is manually maintained, and so new patch dates may be delayed by a few hours.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    PatchesApi,
    Configuration
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new PatchesApi(configuration);

const { status, data } = await apiInstance.bigPatchDays();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Array<string>**

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

# **feed**
> Array<Patch> feed()

 Returns the parsed result of the RSS Feed from the official Forum.  RSS-Feed: https://forums.playdeadlock.com/forums/changelog.10/index.rss  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    PatchesApi,
    Configuration
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new PatchesApi(configuration);

const { status, data } = await apiInstance.feed();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Array<Patch>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**500** | Fetching or parsing the RSS-Feed failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

