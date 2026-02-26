# RawApi

All URIs are relative to *https://assets.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getRawAccoladesRawAccoladesGet**](#getrawaccoladesrawaccoladesget) | **GET** /raw/accolades | Get Raw Accolades|
|[**getRawHeroesRawHeroesGet**](#getrawheroesrawheroesget) | **GET** /raw/heroes | Get Raw Heroes|
|[**getRawItemsRawItemsGet**](#getrawitemsrawitemsget) | **GET** /raw/items | Get Raw Items|

# **getRawAccoladesRawAccoladesGet**
> Array<RawAccoladeV2> getRawAccoladesRawAccoladesGet()


### Example

```typescript
import {
    RawApi,
    Configuration
} from 'assets_deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new RawApi(configuration);

let clientVersion: DeadlockAssetsApiRoutesValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getRawAccoladesRawAccoladesGet(
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**Array<RawAccoladeV2>**

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
> Array<RawHeroV2> getRawHeroesRawHeroesGet()


### Example

```typescript
import {
    RawApi,
    Configuration
} from 'assets_deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new RawApi(configuration);

let clientVersion: DeadlockAssetsApiRoutesValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getRawHeroesRawHeroesGet(
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**Array<RawHeroV2>**

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
> Array<ResponseGetRawItemsRawItemsGetInner> getRawItemsRawItemsGet()


### Example

```typescript
import {
    RawApi,
    Configuration
} from 'assets_deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new RawApi(configuration);

let clientVersion: DeadlockAssetsApiRoutesValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getRawItemsRawItemsGet(
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**Array<ResponseGetRawItemsRawItemsGetInner>**

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

