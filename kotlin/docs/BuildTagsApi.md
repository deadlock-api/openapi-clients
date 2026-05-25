# BuildTagsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getBuildTag**](BuildTagsApi.md#getBuildTag) | **GET** /v1/assets/build-tags/{build_tag_id} | Get Build Tag |
| [**getBuildTagByName**](BuildTagsApi.md#getBuildTagByName) | **GET** /v1/assets/build-tags/by-name/{name} | Get Build Tag By Name |
| [**listBuildTags**](BuildTagsApi.md#listBuildTags) | **GET** /v1/assets/build-tags | List Build Tags |


<a id="getBuildTag"></a>
# **getBuildTag**
> BuildTag getBuildTag(buildTagId, language, clientVersion)

Get Build Tag

Returns a single build tag by id.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = BuildTagsApi()
val buildTagId : kotlin.Int = 56 // kotlin.Int | Build tag id (murmurhash2 of `class_name`)
val language : kotlin.String = language_example // kotlin.String | Language code. Defaults to `english`.
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : BuildTag = apiInstance.getBuildTag(buildTagId, language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling BuildTagsApi#getBuildTag")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling BuildTagsApi#getBuildTag")
    e.printStackTrace()
}
```

### Parameters
| **buildTagId** | **kotlin.Int**| Build tag id (murmurhash2 of &#x60;class_name&#x60;) | |
| **language** | **kotlin.String**| Language code. Defaults to &#x60;english&#x60;. | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**BuildTag**](BuildTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getBuildTagByName"></a>
# **getBuildTagByName**
> BuildTag getBuildTagByName(name, language, clientVersion)

Get Build Tag By Name

Returns a single build tag by &#x60;class_name&#x60; (case-insensitive).

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = BuildTagsApi()
val name : kotlin.String = name_example // kotlin.String | Build tag `class_name` (e.g. `citadel_build_tag_weapon`)
val language : kotlin.String = language_example // kotlin.String | Language code. Defaults to `english`.
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : BuildTag = apiInstance.getBuildTagByName(name, language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling BuildTagsApi#getBuildTagByName")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling BuildTagsApi#getBuildTagByName")
    e.printStackTrace()
}
```

### Parameters
| **name** | **kotlin.String**| Build tag &#x60;class_name&#x60; (e.g. &#x60;citadel_build_tag_weapon&#x60;) | |
| **language** | **kotlin.String**| Language code. Defaults to &#x60;english&#x60;. | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**BuildTag**](BuildTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="listBuildTags"></a>
# **listBuildTags**
> kotlin.collections.List&lt;BuildTag&gt; listBuildTags(language, clientVersion)

List Build Tags

Returns the build tag taxonomy used by the game client, derived from per-version localization keys.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = BuildTagsApi()
val language : kotlin.String = language_example // kotlin.String | Language code. Defaults to `english`.
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : kotlin.collections.List<BuildTag> = apiInstance.listBuildTags(language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling BuildTagsApi#listBuildTags")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling BuildTagsApi#listBuildTags")
    e.printStackTrace()
}
```

### Parameters
| **language** | **kotlin.String**| Language code. Defaults to &#x60;english&#x60;. | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**kotlin.collections.List&lt;BuildTag&gt;**](BuildTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

