# MMRApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**heroMmr**](MMRApi.md#heroMmr) | **GET** /v1/players/mmr/{hero_id} | Hero MMR
[**heroMmrHistory**](MMRApi.md#heroMmrHistory) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History
[**mmr**](MMRApi.md#mmr) | **GET** /v1/players/mmr | MMR
[**mmrHistory**](MMRApi.md#mmrHistory) | **GET** /v1/players/{account_id}/mmr-history | MMR History


<a id="heroMmr"></a>
# **heroMmr**
> kotlin.collections.List&lt;MMRHistory&gt; heroMmr(heroId, accountIds, maxMatchId)

Hero MMR

 Batch Player Hero MMR  Filters for the last 90 days if no &#x60;max_match_id&#x60; is provided. 

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = MMRApi()
val heroId : kotlin.Int = 56 // kotlin.Int | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>
val accountIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of account ids, Account IDs are in `SteamID3` format.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
try {
    val result : kotlin.collections.List<MMRHistory> = apiInstance.heroMmr(heroId, accountIds, maxMatchId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MMRApi#heroMmr")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MMRApi#heroMmr")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heroId** | **kotlin.Int**| The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; |
 **accountIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. |
 **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional]

### Return type

[**kotlin.collections.List&lt;MMRHistory&gt;**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="heroMmrHistory"></a>
# **heroMmrHistory**
> kotlin.collections.List&lt;MMRHistory&gt; heroMmrHistory(accountId, heroId)

Hero MMR History

Player Hero MMR History

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = MMRApi()
val accountId : kotlin.Int = 56 // kotlin.Int | The players `SteamID3`
val heroId : kotlin.Int = 56 // kotlin.Int | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>
try {
    val result : kotlin.collections.List<MMRHistory> = apiInstance.heroMmrHistory(accountId, heroId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MMRApi#heroMmrHistory")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MMRApi#heroMmrHistory")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **kotlin.Int**| The players &#x60;SteamID3&#x60; |
 **heroId** | **kotlin.Int**| The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; |

### Return type

[**kotlin.collections.List&lt;MMRHistory&gt;**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="mmr"></a>
# **mmr**
> kotlin.collections.List&lt;MMRHistory&gt; mmr(accountIds, maxMatchId)

MMR

 Batch Player MMR  Filters for the last 90 days if no &#x60;max_match_id&#x60; is provided. 

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = MMRApi()
val accountIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of account ids, Account IDs are in `SteamID3` format.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
try {
    val result : kotlin.collections.List<MMRHistory> = apiInstance.mmr(accountIds, maxMatchId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MMRApi#mmr")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MMRApi#mmr")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. |
 **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional]

### Return type

[**kotlin.collections.List&lt;MMRHistory&gt;**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="mmrHistory"></a>
# **mmrHistory**
> kotlin.collections.List&lt;MMRHistory&gt; mmrHistory(accountId)

MMR History

Player MMR History

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = MMRApi()
val accountId : kotlin.Int = 56 // kotlin.Int | The players `SteamID3`
try {
    val result : kotlin.collections.List<MMRHistory> = apiInstance.mmrHistory(accountId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MMRApi#mmrHistory")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MMRApi#mmrHistory")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **kotlin.Int**| The players &#x60;SteamID3&#x60; |

### Return type

[**kotlin.collections.List&lt;MMRHistory&gt;**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

