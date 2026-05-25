# NPCUnitsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getNpcUnit**](NPCUnitsApi.md#getNpcUnit) | **GET** /v1/assets/npc-units/{id_or_classname} | Get NPC Unit |
| [**listNpcUnits**](NPCUnitsApi.md#listNpcUnits) | **GET** /v1/assets/npc-units | List NPC Units |


<a id="getNpcUnit"></a>
# **getNpcUnit**
> NpcUnit getNpcUnit(idOrClassname, clientVersion)

Get NPC Unit

Returns a single NPC unit by numeric id or by &#x60;class_name&#x60; (case-insensitive).

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = NPCUnitsApi()
val idOrClassname : kotlin.String = idOrClassname_example // kotlin.String | NPC unit id (`murmurhash2(class_name)`) or `class_name`
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : NpcUnit = apiInstance.getNpcUnit(idOrClassname, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling NPCUnitsApi#getNpcUnit")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling NPCUnitsApi#getNpcUnit")
    e.printStackTrace()
}
```

### Parameters
| **idOrClassname** | **kotlin.String**| NPC unit id (&#x60;murmurhash2(class_name)&#x60;) or &#x60;class_name&#x60; | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**NpcUnit**](NpcUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="listNpcUnits"></a>
# **listNpcUnits**
> kotlin.collections.List&lt;NpcUnit&gt; listNpcUnits(clientVersion)

List NPC Units

Returns the per-NPC-unit metadata used by the game client, parsed from the patch&#39;s KV3 source files.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = NPCUnitsApi()
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : kotlin.collections.List<NpcUnit> = apiInstance.listNpcUnits(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling NPCUnitsApi#listNpcUnits")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling NPCUnitsApi#listNpcUnits")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**kotlin.collections.List&lt;NpcUnit&gt;**](NpcUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

