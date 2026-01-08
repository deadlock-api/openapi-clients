# AccoladesApi

All URIs are relative to *https://assets.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getAccoladeByNameV2AccoladesByNameNameGet**](#getaccoladebynamev2accoladesbynamenameget) | **GET** /v2/accolades/by-name/{name} | Get Accolade By Name|
|[**getAccoladeV2AccoladesIdGet**](#getaccoladev2accoladesidget) | **GET** /v2/accolades/{id} | Get Accolade|
|[**getAccoladesV2AccoladesGet**](#getaccoladesv2accoladesget) | **GET** /v2/accolades | Get Accolades|

# **getAccoladeByNameV2AccoladesByNameNameGet**
> AccoladeV2 getAccoladeByNameV2AccoladesByNameNameGet()


### Example

```typescript
import {
    AccoladesApi,
    Configuration
} from 'assets_deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AccoladesApi(configuration);

let name: string; // (default to undefined)
let language: Language; // (optional) (default to undefined)
let clientVersion: DeadlockAssetsApiRoutesValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getAccoladeByNameV2AccoladesByNameNameGet(
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
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**AccoladeV2**

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

# **getAccoladeV2AccoladesIdGet**
> AccoladeV2 getAccoladeV2AccoladesIdGet()


### Example

```typescript
import {
    AccoladesApi,
    Configuration
} from 'assets_deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AccoladesApi(configuration);

let id: number; // (default to undefined)
let language: Language; // (optional) (default to undefined)
let clientVersion: DeadlockAssetsApiRoutesValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getAccoladeV2AccoladesIdGet(
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
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**AccoladeV2**

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

# **getAccoladesV2AccoladesGet**
> Array<AccoladeV2> getAccoladesV2AccoladesGet()


### Example

```typescript
import {
    AccoladesApi,
    Configuration
} from 'assets_deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new AccoladesApi(configuration);

let language: Language; // (optional) (default to undefined)
let clientVersion: DeadlockAssetsApiRoutesValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getAccoladesV2AccoladesGet(
    language,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language** | **Language** |  | (optional) defaults to undefined|
| **clientVersion** | **DeadlockAssetsApiRoutesValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**Array<AccoladeV2>**

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

