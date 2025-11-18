# DefaultApi

All URIs are relative to *https://assets.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getBuildTagsV2BuildTagsGet**](#getbuildtagsv2buildtagsget) | **GET** /v2/build-tags | Get Build Tags|
|[**getClientVersionsV2ClientVersionsGet**](#getclientversionsv2clientversionsget) | **GET** /v2/client-versions | Get Client Versions|
|[**getColorsV1ColorsGet**](#getcolorsv1colorsget) | **GET** /v1/colors | Get Colors|
|[**getIconsV1IconsGet**](#geticonsv1iconsget) | **GET** /v1/icons | Get Icons|
|[**getMapV1MapGet**](#getmapv1mapget) | **GET** /v1/map | Get Map|
|[**getRanksV2RanksGet**](#getranksv2ranksget) | **GET** /v2/ranks | Get Ranks|
|[**getSoundsV1SoundsGet**](#getsoundsv1soundsget) | **GET** /v1/sounds | Get Sounds|
|[**getSteamInfoV1SteamInfoGet**](#getsteaminfov1steaminfoget) | **GET** /v1/steam-info | Get Steam Info|

# **getBuildTagsV2BuildTagsGet**
> Array<BuildTagV2> getBuildTagsV2BuildTagsGet()


### Example

```typescript
import {
    DefaultApi,
    Configuration
} from 'assets-deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new DefaultApi(configuration);

let language: Language; // (optional) (default to undefined)
let clientVersion: DeadlockAssetsApiRoutesV2ValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getBuildTagsV2BuildTagsGet(
    language,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language** | **Language** |  | (optional) defaults to undefined|
| **clientVersion** | **DeadlockAssetsApiRoutesV2ValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**Array<BuildTagV2>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getClientVersionsV2ClientVersionsGet**
> Array<number> getClientVersionsV2ClientVersionsGet()


### Example

```typescript
import {
    DefaultApi,
    Configuration
} from 'assets-deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new DefaultApi(configuration);

const { status, data } = await apiInstance.getClientVersionsV2ClientVersionsGet();
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
|**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getColorsV1ColorsGet**
> { [key: string]: ColorV1; } getColorsV1ColorsGet()


### Example

```typescript
import {
    DefaultApi,
    Configuration
} from 'assets-deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new DefaultApi(configuration);

let clientVersion: DeadlockAssetsApiRoutesV2ValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getColorsV1ColorsGet(
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientVersion** | **DeadlockAssetsApiRoutesV2ValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**{ [key: string]: ColorV1; }**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getIconsV1IconsGet**
> { [key: string]: string; } getIconsV1IconsGet()


### Example

```typescript
import {
    DefaultApi,
    Configuration
} from 'assets-deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new DefaultApi(configuration);

let clientVersion: DeadlockAssetsApiRoutesV2ValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getIconsV1IconsGet(
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientVersion** | **DeadlockAssetsApiRoutesV2ValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**{ [key: string]: string; }**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getMapV1MapGet**
> MapV1 getMapV1MapGet()


### Example

```typescript
import {
    DefaultApi,
    Configuration
} from 'assets-deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new DefaultApi(configuration);

let clientVersion: DeadlockAssetsApiRoutesV2ValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getMapV1MapGet(
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientVersion** | **DeadlockAssetsApiRoutesV2ValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**MapV1**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getRanksV2RanksGet**
> Array<RankV2> getRanksV2RanksGet()


### Example

```typescript
import {
    DefaultApi,
    Configuration
} from 'assets-deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new DefaultApi(configuration);

let language: Language; // (optional) (default to undefined)
let clientVersion: DeadlockAssetsApiRoutesV2ValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getRanksV2RanksGet(
    language,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language** | **Language** |  | (optional) defaults to undefined|
| **clientVersion** | **DeadlockAssetsApiRoutesV2ValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**Array<RankV2>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getSoundsV1SoundsGet**
> { [key: string]: any; } getSoundsV1SoundsGet()


### Example

```typescript
import {
    DefaultApi,
    Configuration
} from 'assets-deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new DefaultApi(configuration);

let clientVersion: DeadlockAssetsApiRoutesV2ValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getSoundsV1SoundsGet(
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientVersion** | **DeadlockAssetsApiRoutesV2ValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**{ [key: string]: any; }**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getSteamInfoV1SteamInfoGet**
> any getSteamInfoV1SteamInfoGet()


### Example

```typescript
import {
    DefaultApi,
    Configuration
} from 'assets-deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new DefaultApi(configuration);

let clientVersion: DeadlockAssetsApiRoutesV2ValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getSteamInfoV1SteamInfoGet(
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientVersion** | **DeadlockAssetsApiRoutesV2ValidClientVersions** |  | (optional) defaults to undefined|


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
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

