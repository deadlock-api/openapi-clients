# RanksApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getRank**](RanksApi.md#getRank) | **GET** /v1/assets/ranks/{tier} | Get Rank |
| [**listRanks**](RanksApi.md#listRanks) | **GET** /v1/assets/ranks | List Ranks |


<a id="getRank"></a>
# **getRank**
> Rank getRank(tier, language, clientVersion)

Get Rank

Returns a single rank by tier index.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = RanksApi()
val tier : kotlin.Int = 56 // kotlin.Int | Rank tier (0-11)
val language : kotlin.String = language_example // kotlin.String | Language code. Defaults to `english`.
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : Rank = apiInstance.getRank(tier, language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RanksApi#getRank")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RanksApi#getRank")
    e.printStackTrace()
}
```

### Parameters
| **tier** | **kotlin.Int**| Rank tier (0-11) | |
| **language** | **kotlin.String**| Language code. Defaults to &#x60;english&#x60;. | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**Rank**](Rank.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="listRanks"></a>
# **listRanks**
> kotlin.collections.List&lt;Rank&gt; listRanks(language, clientVersion)

List Ranks

Returns the 12 player ranks (tier, localized name, badge image URLs, hex color).

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = RanksApi()
val language : kotlin.String = language_example // kotlin.String | Language code. Defaults to `english`.
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : kotlin.collections.List<Rank> = apiInstance.listRanks(language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RanksApi#listRanks")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RanksApi#listRanks")
    e.printStackTrace()
}
```

### Parameters
| **language** | **kotlin.String**| Language code. Defaults to &#x60;english&#x60;. | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**kotlin.collections.List&lt;Rank&gt;**](Rank.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

