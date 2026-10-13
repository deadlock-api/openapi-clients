# ConvarsApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getConvar**](#getconvar) | **GET** /v1/assets/convars/{name} | Get Convar|
|[**listConvars**](#listconvars) | **GET** /v1/assets/convars | List Convars|

# **getConvar**
> Convar getConvar()

Returns a single console variable by name (case-insensitive).

### Example

```typescript
import {
    ConvarsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new ConvarsApi(configuration);

let name: string; //Convar name, e.g. `citadel_corrupted_item_shop_restock_interval` (default to undefined)
let clientVersion: number; //Client/game version (e.g. `6518`). Defaults to the latest known version. (optional) (default to undefined)

const { status, data } = await apiInstance.getConvar(
    name,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **name** | [**string**] | Convar name, e.g. &#x60;citadel_corrupted_item_shop_restock_interval&#x60; | defaults to undefined|
| **clientVersion** | [**number**] | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | (optional) defaults to undefined|


### Return type

**Convar**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**404** | Unknown convar or client_version, or no convars data for that version |  -  |
|**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listConvars**
> { [key: string]: Convar; } listConvars()

Returns every console variable registered by the patch\'s `client.dll` and `server.dll`, keyed by name, with its type, compiled-in default value, `FCVAR_*` flags and help text. These are the defaults the binaries ship with; servers and game modes can override them at runtime.

### Example

```typescript
import {
    ConvarsApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new ConvarsApi(configuration);

let clientVersion: number; //Client/game version (e.g. `6518`). Defaults to the latest known version. (optional) (default to undefined)

const { status, data } = await apiInstance.listConvars(
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientVersion** | [**number**] | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | (optional) defaults to undefined|


### Return type

**{ [key: string]: Convar; }**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**404** | Requested client_version is not available, or it has no convars data (extracted from build 6774 on) |  -  |
|**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

