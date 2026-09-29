# ModifiersApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getModifier**](ModifiersApi.md#getModifier) | **GET** /v1/assets/modifiers/{id_or_classname} | Get Modifier |
| [**listModifiers**](ModifiersApi.md#listModifiers) | **GET** /v1/assets/modifiers | List Modifiers |


<a id="getModifier"></a>
# **getModifier**
> Modifier getModifier(idOrClassname, clientVersion)

Get Modifier

Returns a single modifier by numeric id or by &#x60;class_name&#x60; (case-insensitive).

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = ModifiersApi()
val idOrClassname : kotlin.String = idOrClassname_example // kotlin.String | Modifier id (`murmurhash2(class_name)`) or `class_name`
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : Modifier = apiInstance.getModifier(idOrClassname, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ModifiersApi#getModifier")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ModifiersApi#getModifier")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **idOrClassname** | **kotlin.String**| Modifier id (&#x60;murmurhash2(class_name)&#x60;) or &#x60;class_name&#x60; | |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**Modifier**](Modifier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="listModifiers"></a>
# **listModifiers**
> kotlin.collections.List&lt;Modifier&gt; listModifiers(clientVersion)

List Modifiers

Returns modifier definitions parsed from the patch&#39;s &#x60;modifiers.vdata&#x60; KV3 source file, including the neutral (\&quot;Haunt\&quot;) abilities referenced by NPC units&#39; &#x60;neutral_abilities&#x60; / &#x60;neutral_melee&#x60; (&#x60;citadel_neutral_*&#x60;). Each entry exposes its class and numeric properties; nested properties use dotted paths.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = ModifiersApi()
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : kotlin.collections.List<Modifier> = apiInstance.listModifiers(clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ModifiersApi#listModifiers")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ModifiersApi#listModifiers")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**kotlin.collections.List&lt;Modifier&gt;**](Modifier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

