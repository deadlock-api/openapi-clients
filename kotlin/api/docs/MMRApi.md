# MMRApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**heroMmr**](MMRApi.md#heroMmr) | **GET** /v1/players/mmr/distribution/{hero_id} | Hero MMR Distribution |
| [**heroMmrHistory**](MMRApi.md#heroMmrHistory) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History |
| [**heroMmr_0**](MMRApi.md#heroMmr_0) | **GET** /v1/players/mmr/{hero_id} | Batch Hero MMR |
| [**mmr**](MMRApi.md#mmr) | **GET** /v1/players/mmr | Batch MMR |
| [**mmrHistory**](MMRApi.md#mmrHistory) | **GET** /v1/players/{account_id}/mmr-history | MMR History |
| [**mmr_0**](MMRApi.md#mmr_0) | **GET** /v1/players/mmr/distribution | MMR Distribution |


<a id="heroMmr"></a>
# **heroMmr**
> kotlin.collections.List&lt;DistributionEntry&gt; heroMmr(heroId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, minMatchId, maxMatchId)

Hero MMR Distribution

 Player Hero MMR Distribution 

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = MMRApi()
val heroId : kotlin.Int = 56 // kotlin.Int | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val maxDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val isHighSkillRangeParties : kotlin.Boolean = true // kotlin.Boolean | Filter matches based on whether they are in the high skill range.
val isLowPriPool : kotlin.Boolean = true // kotlin.Boolean | Filter matches based on whether they are in the low priority pool.
val isNewPlayerPool : kotlin.Boolean = true // kotlin.Boolean | Filter matches based on whether they are in the new player pool.
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
try {
    val result : kotlin.collections.List<DistributionEntry> = apiInstance.heroMmr(heroId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, minMatchId, maxMatchId)
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
| **heroId** | **kotlin.Int**| The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | |
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1759104000L] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **minDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **maxDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **isHighSkillRangeParties** | **kotlin.Boolean**| Filter matches based on whether they are in the high skill range. | [optional] |
| **isLowPriPool** | **kotlin.Boolean**| Filter matches based on whether they are in the low priority pool. | [optional] |
| **isNewPlayerPool** | **kotlin.Boolean**| Filter matches based on whether they are in the new player pool. | [optional] |
| **minMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |

### Return type

[**kotlin.collections.List&lt;DistributionEntry&gt;**](DistributionEntry.md)

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
| **accountId** | **kotlin.Int**| The players &#x60;SteamID3&#x60; | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **heroId** | **kotlin.Int**| The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | |

### Return type

[**kotlin.collections.List&lt;MMRHistory&gt;**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="heroMmr_0"></a>
# **heroMmr_0**
> kotlin.collections.List&lt;MMRHistory&gt; heroMmr_0(heroId, accountIds, maxMatchId)

Batch Hero MMR

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
    val result : kotlin.collections.List<MMRHistory> = apiInstance.heroMmr_0(heroId, accountIds, maxMatchId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MMRApi#heroMmr_0")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MMRApi#heroMmr_0")
    e.printStackTrace()
}
```

### Parameters
| **heroId** | **kotlin.Int**| The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | |
| **accountIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |

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

Batch MMR

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
| **accountIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |

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
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountId** | **kotlin.Int**| The players &#x60;SteamID3&#x60; | |

### Return type

[**kotlin.collections.List&lt;MMRHistory&gt;**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="mmr_0"></a>
# **mmr_0**
> kotlin.collections.List&lt;DistributionEntry&gt; mmr_0(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, minMatchId, maxMatchId)

MMR Distribution

 Player MMR Distribution 

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = MMRApi()
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val maxDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val isHighSkillRangeParties : kotlin.Boolean = true // kotlin.Boolean | Filter matches based on whether they are in the high skill range.
val isLowPriPool : kotlin.Boolean = true // kotlin.Boolean | Filter matches based on whether they are in the low priority pool.
val isNewPlayerPool : kotlin.Boolean = true // kotlin.Boolean | Filter matches based on whether they are in the new player pool.
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
try {
    val result : kotlin.collections.List<DistributionEntry> = apiInstance.mmr_0(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, minMatchId, maxMatchId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MMRApi#mmr_0")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MMRApi#mmr_0")
    e.printStackTrace()
}
```

### Parameters
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1759104000L] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **minDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **maxDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **isHighSkillRangeParties** | **kotlin.Boolean**| Filter matches based on whether they are in the high skill range. | [optional] |
| **isLowPriPool** | **kotlin.Boolean**| Filter matches based on whether they are in the low priority pool. | [optional] |
| **isNewPlayerPool** | **kotlin.Boolean**| Filter matches based on whether they are in the new player pool. | [optional] |
| **minMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |

### Return type

[**kotlin.collections.List&lt;DistributionEntry&gt;**](DistributionEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

