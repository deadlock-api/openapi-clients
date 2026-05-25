# NPCUnitsApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getNpcUnit**](#getnpcunit) | **GET** /v1/assets/npc-units/{id_or_classname} | Get NPC Unit|
|[**listNpcUnits**](#listnpcunits) | **GET** /v1/assets/npc-units | List NPC Units|

# **getNpcUnit**
> NpcUnit getNpcUnit()

Returns a single NPC unit by numeric id or by `class_name` (case-insensitive).

### Example

```typescript
import {
    NPCUnitsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new NPCUnitsApi(configuration);

let idOrClassname: string; //NPC unit id (`murmurhash2(class_name)`) or `class_name` (default to undefined)
let clientVersion: number; //Client/game version (e.g. `6518`). Defaults to the latest known version. (optional) (default to undefined)

const { status, data } = await apiInstance.getNpcUnit(
    idOrClassname,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **idOrClassname** | [**string**] | NPC unit id (&#x60;murmurhash2(class_name)&#x60;) or &#x60;class_name&#x60; | defaults to undefined|
| **clientVersion** | [**number**] | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | (optional) defaults to undefined|


### Return type

**NpcUnit**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**404** | Unknown NPC unit id/class_name or client_version |  -  |
|**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listNpcUnits**
> Array<NpcUnit> listNpcUnits()

Returns the per-NPC-unit metadata used by the game client, parsed from the patch\'s KV3 source files.

### Example

```typescript
import {
    NPCUnitsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new NPCUnitsApi(configuration);

let clientVersion: number; //Client/game version (e.g. `6518`). Defaults to the latest known version. (optional) (default to undefined)

const { status, data } = await apiInstance.listNpcUnits(
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientVersion** | [**number**] | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | (optional) defaults to undefined|


### Return type

**Array<NpcUnit>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**404** | Requested client_version is not available |  -  |
|**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

