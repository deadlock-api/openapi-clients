# MiscEntitiesApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getMiscEntity**](MiscEntitiesApi.md#getMiscEntity) | **GET** /v1/assets/misc-entities/{id_or_classname} | Get Misc Entity |
| [**listMiscEntities**](MiscEntitiesApi.md#listMiscEntities) | **GET** /v1/assets/misc-entities | List Misc Entities |


<a id="getMiscEntity"></a>
# **getMiscEntity**
> MiscEntity getMiscEntity(idOrClassname, language, clientVersion)

Get Misc Entity

Returns a single misc entity by numeric id or by &#x60;class_name&#x60; (case-insensitive).

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = MiscEntitiesApi()
val idOrClassname : kotlin.String = idOrClassname_example // kotlin.String | Misc entity id (`murmurhash2(class_name)`) or `class_name`
val language : kotlin.String = language_example // kotlin.String | Language code. Defaults to `english`.
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : MiscEntity = apiInstance.getMiscEntity(idOrClassname, language, clientVersion)
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
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **idOrClassname** | **kotlin.String**| Misc entity id (&#x60;murmurhash2(class_name)&#x60;) or &#x60;class_name&#x60; | |
| **language** | **kotlin.String**| Language code. Defaults to &#x60;english&#x60;. | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
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
> kotlin.collections.List&lt;MiscEntity&gt; listMiscEntities(language, clientVersion)

List Misc Entities

Returns the per-misc-entity metadata used by the game client, parsed from the patch&#39;s KV3 source files. Pickup labels (&#x60;name&#x60;) and permanent buff stat names (&#x60;buff_type_name&#x60;) are localized into the requested &#x60;language&#x60;; the raw tokens stay in &#x60;name_loc_string&#x60; / &#x60;buff_type_loc_string&#x60;.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = MiscEntitiesApi()
val language : kotlin.String = language_example // kotlin.String | Language code. Defaults to `english`.
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : kotlin.collections.List<MiscEntity> = apiInstance.listMiscEntities(language, clientVersion)
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
| **language** | **kotlin.String**| Language code. Defaults to &#x60;english&#x60;. | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**kotlin.collections.List&lt;MiscEntity&gt;**](MiscEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

