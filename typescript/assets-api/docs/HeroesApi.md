# HeroesApi

All URIs are relative to *https://assets.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getHeroByNameV2HeroesByNameNameGet**](#getherobynamev2heroesbynamenameget) | **GET** /v2/heroes/by-name/{name} | Get Hero By Name|
|[**getHeroV2HeroesIdGet**](#getherov2heroesidget) | **GET** /v2/heroes/{id} | Get Hero|
|[**getHeroesV2HeroesGet**](#getheroesv2heroesget) | **GET** /v2/heroes | Get Heroes|

# **getHeroByNameV2HeroesByNameNameGet**
> HeroV2 getHeroByNameV2HeroesByNameNameGet()


### Example

```typescript
import {
    HeroesApi,
    Configuration
} from 'assets-deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new HeroesApi(configuration);

let name: string; // (default to undefined)
let language: Language; // (optional) (default to undefined)
let clientVersion: ValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getHeroByNameV2HeroesByNameNameGet(
    name,
    language,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **name** | [**string**] |  | defaults to undefined|
| **language** | **Language** |  | (optional) defaults to undefined|
| **clientVersion** | **ValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**HeroV2**

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

# **getHeroV2HeroesIdGet**
> HeroV2 getHeroV2HeroesIdGet()


### Example

```typescript
import {
    HeroesApi,
    Configuration
} from 'assets-deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new HeroesApi(configuration);

let id: number; // (default to undefined)
let language: Language; // (optional) (default to undefined)
let clientVersion: ValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getHeroV2HeroesIdGet(
    id,
    language,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|
| **language** | **Language** |  | (optional) defaults to undefined|
| **clientVersion** | **ValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**HeroV2**

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

# **getHeroesV2HeroesGet**
> Array<HeroV2> getHeroesV2HeroesGet()


### Example

```typescript
import {
    HeroesApi,
    Configuration
} from 'assets-deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new HeroesApi(configuration);

let language: Language; // (optional) (default to undefined)
let clientVersion: ValidClientVersions; // (optional) (default to undefined)
let onlyActive: boolean; // (optional) (default to undefined)

const { status, data } = await apiInstance.getHeroesV2HeroesGet(
    language,
    clientVersion,
    onlyActive
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language** | **Language** |  | (optional) defaults to undefined|
| **clientVersion** | **ValidClientVersions** |  | (optional) defaults to undefined|
| **onlyActive** | [**boolean**] |  | (optional) defaults to undefined|


### Return type

**Array<HeroV2>**

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

