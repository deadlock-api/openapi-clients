# NPCUnitsApi

All URIs are relative to *https://assets.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getNpcUnitV2NpcUnitsIdOrClassNameGet**](#getnpcunitv2npcunitsidorclassnameget) | **GET** /v2/npc-units/{id_or_class_name} | Get Npc Unit|
|[**getNpcUnitsV2NpcUnitsGet**](#getnpcunitsv2npcunitsget) | **GET** /v2/npc-units | Get Npc Units|

# **getNpcUnitV2NpcUnitsIdOrClassNameGet**
> NPCUnitV2 getNpcUnitV2NpcUnitsIdOrClassNameGet()


### Example

```typescript
import {
    NPCUnitsApi,
    Configuration
} from 'assets-deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new NPCUnitsApi(configuration);

let idOrClassName: string; // (default to undefined)
let clientVersion: DeadlockAssetsApiRoutesRawValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getNpcUnitV2NpcUnitsIdOrClassNameGet(
    idOrClassName,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **idOrClassName** | [**string**] |  | defaults to undefined|
| **clientVersion** | **DeadlockAssetsApiRoutesRawValidClientVersions** |  | (optional) defaults to undefined|


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

# **getNpcUnitsV2NpcUnitsGet**
> Array<NPCUnitV2> getNpcUnitsV2NpcUnitsGet()


### Example

```typescript
import {
    NPCUnitsApi,
    Configuration
} from 'assets-deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new NPCUnitsApi(configuration);

let clientVersion: DeadlockAssetsApiRoutesRawValidClientVersions; // (optional) (default to undefined)

const { status, data } = await apiInstance.getNpcUnitsV2NpcUnitsGet(
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientVersion** | **DeadlockAssetsApiRoutesRawValidClientVersions** |  | (optional) defaults to undefined|


### Return type

**Array<NPCUnitV2>**

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

