# MiscEntitiesApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getMiscEntity**](MiscEntitiesApi.md#getMiscEntity) | **GET** /v1/assets/misc-entities/{id_or_classname} | Get Misc Entity |
| [**listMiscEntities**](MiscEntitiesApi.md#listMiscEntities) | **GET** /v1/assets/misc-entities | List Misc Entities |


<a id="getMiscEntity"></a>
# **getMiscEntity**
> MiscEntity getMiscEntity(idOrClassname, clientVersion)

Get Misc Entity

Returns a single misc entity by numeric id or by &#x60;class_name&#x60; (case-insensitive).

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = MiscEntitiesApi()
val idOrClassname : kotlin.String = idOrClassname_example // kotlin.String | Misc entity id (`murmurhash2(class_name)`) or `class_name`
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : MiscEntity = apiInstance.getMiscEntity(idOrClassname, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MiscEntitiesApi#getMiscEntity")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MiscEntitiesApi#getMiscEntity")
    e.printStackTrace()
}
```

### Parameters
| **idOrClassname** | **kotlin.String**| Misc entity id (&#x60;murmurhash2(class_name)&#x60;) or &#x60;class_name&#x60; | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**MiscEntity**](MiscEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="listMiscEntities"></a>
# **listMiscEntities**
> kotlin.collections.List&lt;MiscEntity&gt; listMiscEntities(clientVersion)

List Misc Entities

Returns the per-misc-entity metadata used by the game client, parsed from the patch&#39;s KV3 source files.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = MiscEntitiesApi()
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : kotlin.collections.List<MiscEntity> = apiInstance.listMiscEntities(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MiscEntitiesApi#listMiscEntities")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MiscEntitiesApi#listMiscEntities")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**kotlin.collections.List&lt;MiscEntity&gt;**](MiscEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

