# LootTablesApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**listLootTables**](#listloottables) | **GET** /v1/assets/loot-tables | List Loot Tables|

# **listLootTables**
> { [key: string]: LootTable; } listLootTables()

Returns the per-table loot definitions used by the game client, parsed from the patch\'s KV3 source files. Keyed by table `class_name`.

### Example

```typescript
import {
    LootTablesApi,
    Configuration
} from 'deadlock_api_client';

const configuration = new Configuration();
const apiInstance = new LootTablesApi(configuration);

let clientVersion: number; //Client/game version (e.g. `6518`). Defaults to the latest known version. (optional) (default to undefined)

const { status, data } = await apiInstance.listLootTables(
    clientVersion
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientVersion** | [**number**] | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | (optional) defaults to undefined|


### Return type

**{ [key: string]: LootTable; }**

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

