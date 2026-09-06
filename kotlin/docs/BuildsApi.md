# BuildsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**fetchBuildLive**](BuildsApi.md#fetchBuildLive) | **GET** /v1/builds/{hero_id}/{build_id} | Fetch Live |
| [**fetchBuildsByAuthorLive**](BuildsApi.md#fetchBuildsByAuthorLive) | **GET** /v1/builds/by-author/{account_id} | Fetch Live by Author |
| [**searchBuilds**](BuildsApi.md#searchBuilds) | **GET** /v1/builds | Search |


<a id="fetchBuildLive"></a>
# **fetchBuildLive**
> Build fetchBuildLive(heroId, buildId, forceRefetch)

Fetch Live

 Returns a single build. If the build is already in our database it is served from there, otherwise it is fetched live from the Deadlock Game Coordinator and stored in the database.  Set &#x60;force_refetch&#x3D;true&#x60; to always fetch from the Game Coordinator, e.g. to pick up a newer version.  Rate limits only apply when the build is fetched from the Game Coordinator.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGCFindHeroBuilds - CMsgClientToGCFindHeroBuildsResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 20req/min | | Key | 100req/min | | Global | 500req/min |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = BuildsApi()
val heroId : kotlin.Int = 56 // kotlin.Int | The hero ID of the build. See more: <https://api.deadlock-api.com/v1/assets/heroes>
val buildId : kotlin.Int = 56 // kotlin.Int | The build ID to fetch.
val forceRefetch : kotlin.Boolean = true // kotlin.Boolean | Fetch the build from the Game Coordinator even if it is already in the database.
try {
    val result : Build = apiInstance.fetchBuildLive(heroId, buildId, forceRefetch)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling BuildsApi#fetchBuildLive")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling BuildsApi#fetchBuildLive")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **heroId** | **kotlin.Int**| The hero ID of the build. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | |
| **buildId** | **kotlin.Int**| The build ID to fetch. | |
| **forceRefetch** | **kotlin.Boolean**| Fetch the build from the Game Coordinator even if it is already in the database. | [optional] |

### Return type

[**Build**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="fetchBuildsByAuthorLive"></a>
# **fetchBuildsByAuthorLive**
> kotlin.collections.List&lt;Build&gt; fetchBuildsByAuthorLive(accountId)

Fetch Live by Author

 Fetches all builds of an author directly from the Deadlock Game Coordinator and stores them in the database.  Unlike the search endpoint, this does not rely on builds already being in our database, so it can be used to look up builds that have not been crawled yet. Every fetched build is upserted into the database.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGCFindHeroBuilds - CMsgClientToGCFindHeroBuildsResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 20req/min | | Key | 100req/min | | Global | 500req/min |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = BuildsApi()
val accountId : kotlin.Int = 56 // kotlin.Int | The players `SteamID3`
try {
    val result : kotlin.collections.List<Build> = apiInstance.fetchBuildsByAuthorLive(accountId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling BuildsApi#fetchBuildsByAuthorLive")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling BuildsApi#fetchBuildsByAuthorLive")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountId** | **kotlin.Int**| The players &#x60;SteamID3&#x60; | |

### Return type

[**kotlin.collections.List&lt;Build&gt;**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="searchBuilds"></a>
# **searchBuilds**
> kotlin.collections.List&lt;Build&gt; searchBuilds(minUnixTimestamp, maxUnixTimestamp, minPublishedUnixTimestamp, maxPublishedUnixTimestamp, sortBy, start, limit, sortDirection, searchName, searchDescription, onlyLatest, language, buildLanguage, buildId, version, heroId, tag, rollupCategory, authorId)

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
val buildLanguage : kotlin.String = buildLanguage_example // kotlin.String | Filter builds by language.
val buildId : kotlin.Int = 56 // kotlin.Int | Filter builds by ID.
val version : kotlin.Int = 56 // kotlin.Int | Filter builds by version.
val heroId : kotlin.Int = 56 // kotlin.Int | Filter builds by hero ID. See more: <https://api.deadlock-api.com/v1/assets/heroes>
val tag : kotlin.Int = 56 // kotlin.Int | Filter builds by tag.
val rollupCategory : kotlin.Int = 56 // kotlin.Int | Filter builds by rollup category.
val authorId : kotlin.Int = 56 // kotlin.Int | The author's `SteamID3`
try {
    val result : kotlin.collections.List<Build> = apiInstance.searchBuilds(minUnixTimestamp, maxUnixTimestamp, minPublishedUnixTimestamp, maxPublishedUnixTimestamp, sortBy, start, limit, sortDirection, searchName, searchDescription, onlyLatest, language, buildLanguage, buildId, version, heroId, tag, rollupCategory, authorId)
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
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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
| **buildLanguage** | **kotlin.String**| Filter builds by language. | [optional] [enum: English, German, French, Italian, Korean, SpanishSpain, ChineseSimplified, Russian, Thai, Japanese, PortuguesePortugal, Polish, Czech, Turkish, PortugueseBrazil, Ukrainian, SpanishLatinAmerica, Vietnamese] |
| **buildId** | **kotlin.Int**| Filter builds by ID. | [optional] |
| **version** | **kotlin.Int**| Filter builds by version. | [optional] |
| **heroId** | **kotlin.Int**| Filter builds by hero ID. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [optional] |
| **tag** | **kotlin.Int**| Filter builds by tag. | [optional] |
| **rollupCategory** | **kotlin.Int**| Filter builds by rollup category. | [optional] |
| **authorId** | **kotlin.Int**| The author&#39;s &#x60;SteamID3&#x60; | [optional] |

### Return type

[**kotlin.collections.List&lt;Build&gt;**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

