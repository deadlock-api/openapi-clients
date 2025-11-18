# MiscEntitiesApi

All URIs are relative to *https://assets.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getMiscEntitiesV2MiscEntitiesGet**](#getmiscentitiesv2miscentitiesget) | **GET** /v2/misc-entities | Get Misc Entities|
|[**getMiscEntityV2MiscEntitiesIdOrClassNameGet**](#getmiscentityv2miscentitiesidorclassnameget) | **GET** /v2/misc-entities/{id_or_class_name} | Get Misc Entity|

# **getMiscEntitiesV2MiscEntitiesGet**
> Array<MiscV2> getMiscEntitiesV2MiscEntitiesGet()


### Example

```typescript
import {
    MiscEntitiesApi,
    Configuration
} from 'assets-deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new MiscEntitiesApi(configuration);

let clientVersion: DeadlockAssetsApiRoutesV2ValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getMiscEntitiesV2MiscEntitiesGet(
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientVersion** | **DeadlockAssetsApiRoutesV2ValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**Array<MiscV2>**

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

# **getMiscEntityV2MiscEntitiesIdOrClassNameGet**
> NPCUnitV2 getMiscEntityV2MiscEntitiesIdOrClassNameGet()


### Example

```typescript
import {
    MiscEntitiesApi,
    Configuration
} from 'assets-deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new MiscEntitiesApi(configuration);

let idOrClassName: string; // (default to undefined)
let clientVersion: DeadlockAssetsApiRoutesV2ValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getMiscEntityV2MiscEntitiesIdOrClassNameGet(
    idOrClassName,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **idOrClassName** | [**string**] |  | defaults to undefined|
| **clientVersion** | **DeadlockAssetsApiRoutesV2ValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**NPCUnitV2**

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

