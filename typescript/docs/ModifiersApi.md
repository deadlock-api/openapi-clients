# ModifiersApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getModifier**](#getmodifier) | **GET** /v1/assets/modifiers/{id_or_classname} | Get Modifier|
|[**listModifiers**](#listmodifiers) | **GET** /v1/assets/modifiers | List Modifiers|

# **getModifier**
> Modifier getModifier()

Returns a single modifier by numeric id or by `class_name` (case-insensitive).

### Example

```typescript
import {
    ModifiersApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new ModifiersApi(configuration);

let idOrClassname: string; //Modifier id (`murmurhash2(class_name)`) or `class_name` (default to undefined)
let clientVersion: number; //Client/game version (e.g. `6518`). Defaults to the latest known version. (optional) (default to undefined)

const { status, data } = await apiInstance.getModifier(
    idOrClassname,
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **idOrClassname** | [**string**] | Modifier id (&#x60;murmurhash2(class_name)&#x60;) or &#x60;class_name&#x60; | defaults to undefined|
| **clientVersion** | [**number**] | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | (optional) defaults to undefined|


### Return type

**Modifier**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**404** | Unknown modifier id/class_name or client_version, or no modifiers data for that version |  -  |
|**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listModifiers**
> Array<Modifier> listModifiers()

Returns modifier definitions parsed from the patch\'s `modifiers.vdata` KV3 source file, including the neutral (\"Haunt\") abilities referenced by NPC units\' `neutral_abilities` / `neutral_melee` (`citadel_neutral_*`). Each entry exposes its class and numeric properties; nested properties use dotted paths.

### Example

```typescript
import {
    ModifiersApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new ModifiersApi(configuration);

let clientVersion: number; //Client/game version (e.g. `6518`). Defaults to the latest known version. (optional) (default to undefined)

const { status, data } = await apiInstance.listModifiers(
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientVersion** | [**number**] | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | (optional) defaults to undefined|


### Return type

**Array<Modifier>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**404** | Requested client_version is not available, or it has no modifiers data (published from build 6712 on) |  -  |
|**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

