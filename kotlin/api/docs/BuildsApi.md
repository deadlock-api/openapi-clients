# BuildsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**searchBuilds**](BuildsApi.md#searchBuilds) | **GET** /v1/builds | Search |


<a id="searchBuilds"></a>
# **searchBuilds**
> kotlin.collections.List&lt;Build&gt; searchBuilds(minUnixTimestamp, maxUnixTimestamp, minPublishedUnixTimestamp, maxPublishedUnixTimestamp, sortBy, start, limit, sortDirection, searchName, searchDescription, onlyLatest, language, buildId, version, heroId, tag, rollupCategory, authorId)

Search

 Search for builds based on various criteria.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = BuildsApi()
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter builds based on their `last_updated` time (Unix timestamp).
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter builds based on their `last_updated` time (Unix timestamp).
val minPublishedUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter builds based on their published time (Unix timestamp).
val maxPublishedUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter builds based on their published time (Unix timestamp).
val sortBy : kotlin.String = sortBy_example // kotlin.String | The field to sort the builds by.
val start : kotlin.Int = 56 // kotlin.Int | The index of the first build to return.
val limit : kotlin.Int = 56 // kotlin.Int | The maximum number of builds to return.
val sortDirection : kotlin.String = sortDirection_example // kotlin.String | The direction to sort the builds in.
val searchName : kotlin.String = searchName_example // kotlin.String | Search for builds with a name containing this string.
val searchDescription : kotlin.String = searchDescription_example // kotlin.String | Search for builds with a description containing this string.
val onlyLatest : kotlin.Boolean = true // kotlin.Boolean | Only return the latest version of each build.
val language : kotlin.Int = 56 // kotlin.Int | Filter builds by language.
val buildId : kotlin.Int = 56 // kotlin.Int | Filter builds by ID.
val version : kotlin.Int = 56 // kotlin.Int | Filter builds by version.
val heroId : kotlin.Int = 56 // kotlin.Int | Filter builds by hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
val tag : kotlin.Int = 56 // kotlin.Int | Filter builds by tag.
val rollupCategory : kotlin.Int = 56 // kotlin.Int | Filter builds by rollup category.
val authorId : kotlin.Int = 56 // kotlin.Int | The author's `SteamID3`
try {
    val result : kotlin.collections.List<Build> = apiInstance.searchBuilds(minUnixTimestamp, maxUnixTimestamp, minPublishedUnixTimestamp, maxPublishedUnixTimestamp, sortBy, start, limit, sortDirection, searchName, searchDescription, onlyLatest, language, buildId, version, heroId, tag, rollupCategory, authorId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling BuildsApi#searchBuilds")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling BuildsApi#searchBuilds")
    e.printStackTrace()
}
```

### Parameters
| **minUnixTimestamp** | **kotlin.Long**| Filter builds based on their &#x60;last_updated&#x60; time (Unix timestamp). | [optional] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter builds based on their &#x60;last_updated&#x60; time (Unix timestamp). | [optional] |
| **minPublishedUnixTimestamp** | **kotlin.Long**| Filter builds based on their published time (Unix timestamp). | [optional] |
| **maxPublishedUnixTimestamp** | **kotlin.Long**| Filter builds based on their published time (Unix timestamp). | [optional] |
| **sortBy** | **kotlin.String**| The field to sort the builds by. | [optional] [enum: weekly_favorites, favorites, ignores, reports, updated_at, published_at, version] |
| **start** | **kotlin.Int**| The index of the first build to return. | [optional] |
| **limit** | **kotlin.Int**| The maximum number of builds to return. | [optional] [default to 100] |
| **sortDirection** | **kotlin.String**| The direction to sort the builds in. | [optional] [enum: desc, asc] |
| **searchName** | **kotlin.String**| Search for builds with a name containing this string. | [optional] |
| **searchDescription** | **kotlin.String**| Search for builds with a description containing this string. | [optional] |
| **onlyLatest** | **kotlin.Boolean**| Only return the latest version of each build. | [optional] |
| **language** | **kotlin.Int**| Filter builds by language. | [optional] |
| **buildId** | **kotlin.Int**| Filter builds by ID. | [optional] |
| **version** | **kotlin.Int**| Filter builds by version. | [optional] |
| **heroId** | **kotlin.Int**| Filter builds by hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **tag** | **kotlin.Int**| Filter builds by tag. | [optional] |
| **rollupCategory** | **kotlin.Int**| Filter builds by rollup category. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **authorId** | **kotlin.Int**| The author&#39;s &#x60;SteamID3&#x60; | [optional] |

### Return type

[**kotlin.collections.List&lt;Build&gt;**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

