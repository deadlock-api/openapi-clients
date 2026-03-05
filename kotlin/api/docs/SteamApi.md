# SteamApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**steam**](SteamApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile |
| [**steamSearch**](SteamApi.md#steamSearch) | **GET** /v1/players/steam-search | Steam Profile Search |


<a id="steam"></a>
# **steam**
> kotlin.collections.List&lt;SteamProfile&gt; steam(accountIds)

Batch Steam Profile

 This endpoint returns Steam profiles of players.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = SteamApi()
val accountIds : kotlin.collections.List<kotlin.Long> =  // kotlin.collections.List<kotlin.Long> | Comma separated list of account ids, Account IDs are in `SteamID3` format.
try {
    val result : kotlin.collections.List<SteamProfile> = apiInstance.steam(accountIds)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling SteamApi#steam")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling SteamApi#steam")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountIds** | [**kotlin.collections.List&lt;kotlin.Long&gt;**](kotlin.Long.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | |

### Return type

[**kotlin.collections.List&lt;SteamProfile&gt;**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="steamSearch"></a>
# **steamSearch**
> kotlin.collections.List&lt;SteamProfile&gt; steamSearch(searchQuery)

Steam Profile Search

 This endpoint lets you search for Steam profiles by account_id or personaname.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = SteamApi()
val searchQuery : kotlin.String = searchQuery_example // kotlin.String | Search query for Steam profiles.
try {
    val result : kotlin.collections.List<SteamProfile> = apiInstance.steamSearch(searchQuery)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling SteamApi#steamSearch")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling SteamApi#steamSearch")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **searchQuery** | **kotlin.String**| Search query for Steam profiles. | |

### Return type

[**kotlin.collections.List&lt;SteamProfile&gt;**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

