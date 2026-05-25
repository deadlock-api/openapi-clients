# AssetsBucketApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**fonts**](#fonts) | **GET** /v1/assets/fonts | Fonts Index|
|[**icons**](#icons) | **GET** /v1/assets/icons | Icons Index|
|[**images**](#images) | **GET** /v1/assets/images | Images Index|
|[**sounds**](#sounds) | **GET** /v1/assets/sounds | Sounds Index|

# **fonts**
> any fonts()

Nested file-tree of all hosted fonts, mapping each name to its public CDN URL.

### Example

```typescript
import {
    AssetsBucketApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AssetsBucketApi(configuration);

const { status, data } = await apiInstance.fonts();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**any**

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

# **icons**
> any icons()

Nested file-tree of all hosted icons, mapping each name to its public CDN URL.

### Example

```typescript
import {
    AssetsBucketApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AssetsBucketApi(configuration);

const { status, data } = await apiInstance.icons();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**any**

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

# **images**
> any images()

Nested file-tree of all hosted images, mapping each name to its public CDN URL.

### Example

```typescript
import {
    AssetsBucketApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AssetsBucketApi(configuration);

const { status, data } = await apiInstance.images();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**any**

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

# **sounds**
> any sounds()

Nested file-tree of all hosted sounds, mapping each name to its public CDN URL.

### Example

```typescript
import {
    AssetsBucketApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AssetsBucketApi(configuration);

const { status, data } = await apiInstance.sounds();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**any**

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

