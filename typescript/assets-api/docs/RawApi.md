# RawApi

All URIs are relative to *https://assets.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getGenericDataRawGenericDataGet**](#getgenericdatarawgenericdataget) | **GET** /raw/generic_data | Get Generic Data|
|[**getRawHeroesRawHeroesGet**](#getrawheroesrawheroesget) | **GET** /raw/heroes | Get Raw Heroes|
|[**getRawItemsRawItemsGet**](#getrawitemsrawitemsget) | **GET** /raw/items | Get Raw Items|

# **getGenericDataRawGenericDataGet**
> any getGenericDataRawGenericDataGet()


### Example

```typescript
import {
    RawApi,
    Configuration
} from 'assets-deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new RawApi(configuration);

let clientVersion: DeadlockAssetsApiRoutesV1ValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getGenericDataRawGenericDataGet(
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientVersion** | **DeadlockAssetsApiRoutesV1ValidClientVersions** |  | (optional) defaults to undefined|


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

# **getRawHeroesRawHeroesGet**
> any getRawHeroesRawHeroesGet()


### Example

```typescript
import {
    RawApi,
    Configuration
} from 'assets-deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new RawApi(configuration);

let clientVersion: DeadlockAssetsApiRoutesV1ValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getRawHeroesRawHeroesGet(
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientVersion** | **DeadlockAssetsApiRoutesV1ValidClientVersions** |  | (optional) defaults to undefined|


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

# **getRawItemsRawItemsGet**
> any getRawItemsRawItemsGet()


### Example

```typescript
import {
    RawApi,
    Configuration
} from 'assets-deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new RawApi(configuration);

let clientVersion: DeadlockAssetsApiRoutesV1ValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getRawItemsRawItemsGet(
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientVersion** | **DeadlockAssetsApiRoutesV1ValidClientVersions** |  | (optional) defaults to undefined|


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

