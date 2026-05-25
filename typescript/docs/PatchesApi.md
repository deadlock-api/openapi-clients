# PatchesApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**bigPatchDays**](#bigpatchdays) | **GET** /v1/patches/big-days | Big Days|
|[**feed**](#feed) | **GET** /v1/patches | Notes|
|[**feed_0**](#feed_0) | **GET** /v2/patches | Notes|

# **bigPatchDays**
> Array<string> bigPatchDays()

 Returns a list of dates where Deadlock\'s \"big\" patch days were, usually bi-weekly. The exact date is the time when the announcement forum post was published.  This list is manually maintained, and so new patch dates may be delayed by a few hours.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    PatchesApi,
    Configuration
} from 'deadlock_api_client';

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

 **Deprecated:** Use `/v2/patches` instead, which returns a unified feed combining the Forum changelog and the Steam news feed.  Returns the parsed result of the RSS Feed from the official Forum.  RSS-Feed: https://forums.playdeadlock.com/forums/changelog.10/index.rss  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    PatchesApi,
    Configuration
} from 'deadlock_api_client';

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

# **feed_0**
> Array<FeedItem> feed_0()

 Returns a unified feed combining patch notes from the official Forum changelog and the Steam news feed.  Each entry is tagged with a `source` field (`forum` or `steam`).  - Forum RSS: https://forums.playdeadlock.com/forums/changelog.10/index.rss - Steam News RSS: https://store.steampowered.com/feeds/news/app/1422450/  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example

```typescript
import {
    PatchesApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new PatchesApi(configuration);

const { status, data } = await apiInstance.feed_0();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Array<FeedItem>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**500** | Fetching or parsing one of the RSS feeds failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

