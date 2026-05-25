# MiscEntitiesApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getMiscEntity**](#getmiscentity) | **GET** /v1/assets/misc-entities/{id_or_classname} | Get Misc Entity|
|[**listMiscEntities**](#listmiscentities) | **GET** /v1/assets/misc-entities | List Misc Entities|

# **getMiscEntity**
> MiscEntity getMiscEntity()

Returns a single misc entity by numeric id or by `class_name` (case-insensitive).

### Example

```typescript
import {
    MiscEntitiesApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new MiscEntitiesApi(configuration);

let idOrClassname: string; //Misc entity id (`murmurhash2(class_name)`) or `class_name` (default to undefined)
let clientVersion: number; //Client/game version (e.g. `6518`). Defaults to the latest known version. (optional) (default to undefined)

const { status, data } = await apiInstance.getMiscEntity(
    idOrClassname,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **idOrClassname** | [**string**] | Misc entity id (&#x60;murmurhash2(class_name)&#x60;) or &#x60;class_name&#x60; | defaults to undefined|
| **clientVersion** | [**number**] | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | (optional) defaults to undefined|


### Return type

**MiscEntity**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**404** | Unknown misc entity id/class_name or client_version |  -  |
|**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listMiscEntities**
> Array<MiscEntity> listMiscEntities()

Returns the per-misc-entity metadata used by the game client, parsed from the patch\'s KV3 source files.

### Example

```typescript
import {
    MiscEntitiesApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new MiscEntitiesApi(configuration);

let clientVersion: number; //Client/game version (e.g. `6518`). Defaults to the latest known version. (optional) (default to undefined)

const { status, data } = await apiInstance.listMiscEntities(
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientVersion** | [**number**] | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | (optional) defaults to undefined|


### Return type

**Array<MiscEntity>**

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

