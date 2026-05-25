# AccoladesApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getAccolade**](AccoladesApi.md#getAccolade) | **GET** /v1/assets/accolades/{accolade_id} | Get Accolade |
| [**getAccoladeByName**](AccoladesApi.md#getAccoladeByName) | **GET** /v1/assets/accolades/by-name/{name} | Get Accolade By Name |
| [**listAccolades**](AccoladesApi.md#listAccolades) | **GET** /v1/assets/accolades | List Accolades |


<a id="getAccolade"></a>
# **getAccolade**
> Accolade getAccolade(accoladeId, language, clientVersion)

Get Accolade

Returns a single accolade by id.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = AccoladesApi()
val accoladeId : kotlin.Int = 56 // kotlin.Int | Accolade id (`m_unAccoladeID`)
val language : kotlin.String = language_example // kotlin.String | Language code. Defaults to `english`.
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : Accolade = apiInstance.getAccolade(accoladeId, language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AccoladesApi#getAccolade")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AccoladesApi#getAccolade")
    e.printStackTrace()
}
```

### Parameters
| **accoladeId** | **kotlin.Int**| Accolade id (&#x60;m_unAccoladeID&#x60;) | |
| **language** | **kotlin.String**| Language code. Defaults to &#x60;english&#x60;. | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**Accolade**](Accolade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getAccoladeByName"></a>
# **getAccoladeByName**
> Accolade getAccoladeByName(name, language, clientVersion)

Get Accolade By Name

Returns a single accolade by &#x60;class_name&#x60; or &#x60;tracked_stat_name&#x60; (case-insensitive).

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = AccoladesApi()
val name : kotlin.String = name_example // kotlin.String | Accolade `class_name` (e.g. `kills`) or `tracked_stat_name`
val language : kotlin.String = language_example // kotlin.String | Language code. Defaults to `english`.
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : Accolade = apiInstance.getAccoladeByName(name, language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AccoladesApi#getAccoladeByName")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AccoladesApi#getAccoladeByName")
    e.printStackTrace()
}
```

### Parameters
| **name** | **kotlin.String**| Accolade &#x60;class_name&#x60; (e.g. &#x60;kills&#x60;) or &#x60;tracked_stat_name&#x60; | |
| **language** | **kotlin.String**| Language code. Defaults to &#x60;english&#x60;. | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**Accolade**](Accolade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="listAccolades"></a>
# **listAccolades**
> kotlin.collections.List&lt;Accolade&gt; listAccolades(language, clientVersion)

List Accolades

Returns the per-accolade metadata used by the game client, parsed from the patch&#39;s KV3 source files.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = AccoladesApi()
val language : kotlin.String = language_example // kotlin.String | Language code. Defaults to `english`.
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : kotlin.collections.List<Accolade> = apiInstance.listAccolades(language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AccoladesApi#listAccolades")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AccoladesApi#listAccolades")
    e.printStackTrace()
}
```

### Parameters
| **language** | **kotlin.String**| Language code. Defaults to &#x60;english&#x60;. | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**kotlin.collections.List&lt;Accolade&gt;**](Accolade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

