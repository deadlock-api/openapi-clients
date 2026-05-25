# DeadlockApiClient.Api.LootTablesApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**ListLootTables**](LootTablesApi.md#listloottables) | **GET** /v1/assets/loot-tables | List Loot Tables |

<a id="listloottables"></a>
# **ListLootTables**
> Dictionary&lt;string, LootTable&gt; ListLootTables (int clientVersion = null)

List Loot Tables

Returns the per-table loot definitions used by the game client, parsed from the patch's KV3 source files. Keyed by table `class_name`.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **clientVersion** | **int** | Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional]  |

### Return type

[**Dictionary&lt;string, LootTable&gt;**](LootTable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Requested client_version is not available |  -  |
| **500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

