# LootTablesApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listLootTables**](LootTablesApi.md#listLootTables) | **GET** /v1/assets/loot-tables | List Loot Tables |


<a id="listLootTables"></a>
# **listLootTables**
> kotlin.collections.Map&lt;kotlin.String, LootTable&gt; listLootTables(clientVersion)

List Loot Tables

Returns the per-table loot definitions used by the game client, parsed from the patch&#39;s KV3 source files. Keyed by table &#x60;class_name&#x60;.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = LootTablesApi()
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : kotlin.collections.Map<kotlin.String, LootTable> = apiInstance.listLootTables(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling LootTablesApi#listLootTables")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling LootTablesApi#listLootTables")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**kotlin.collections.Map&lt;kotlin.String, LootTable&gt;**](LootTable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

