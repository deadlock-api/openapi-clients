# RankedSeasonsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listRankedSeasons**](RankedSeasonsApi.md#listRankedSeasons) | **GET** /v1/assets/ranked-seasons | List Ranked Seasons |


<a id="listRankedSeasons"></a>
# **listRankedSeasons**
> kotlin.collections.List&lt;RankedSeason&gt; listRankedSeasons(language, clientVersion)

List Ranked Seasons

Returns the ranked season definitions used by the game client, parsed from the patch&#39;s KV3 source files. Each season carries its eligibility requirements and the intervals it runs for, as unix timestamps in seconds.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = RankedSeasonsApi()
val language : kotlin.String = language_example // kotlin.String | Language code. Defaults to `english`.
val clientVersion : kotlin.Int = 56 // kotlin.Int | Client/game version (e.g. `6518`). Defaults to the latest known version.
try {
    val result : kotlin.collections.List<RankedSeason> = apiInstance.listRankedSeasons(language, clientVersion)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RankedSeasonsApi#listRankedSeasons")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RankedSeasonsApi#listRankedSeasons")
    e.printStackTrace()
}
```

### Parameters
| **language** | **kotlin.String**| Language code. Defaults to &#x60;english&#x60;. | [optional] [enum: brazilian, bulgarian, czech, danish, dutch, english, finnish, french, german, greek, hungarian, indonesian, italian, japanese, koreana, latam, norwegian, polish, portuguese, romanian, russian, schinese, spanish, swedish, tchinese, thai, turkish, ukrainian, vietnamese] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clientVersion** | **kotlin.Int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] |

### Return type

[**kotlin.collections.List&lt;RankedSeason&gt;**](RankedSeason.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

