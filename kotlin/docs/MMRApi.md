# MMRApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**heroMmr**](MMRApi.md#heroMmr) | **GET** /v1/players/mmr/{hero_id} | Batch Hero MMR (Deprecated) |
| [**heroMmrDistribution**](MMRApi.md#heroMmrDistribution) | **GET** /v1/players/mmr/distribution/{hero_id} | Hero MMR Distribution (Deprecated) |
| [**heroMmrHistory**](MMRApi.md#heroMmrHistory) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History (Deprecated) |
| [**mmr**](MMRApi.md#mmr) | **GET** /v1/players/mmr | Batch MMR (Deprecated) |
| [**mmrDistribution**](MMRApi.md#mmrDistribution) | **GET** /v1/players/mmr/distribution | MMR Distribution (Deprecated) |
| [**mmrHistory**](MMRApi.md#mmrHistory) | **GET** /v1/players/{account_id}/mmr-history | MMR History (Deprecated) |


<a id="heroMmr"></a>
# **heroMmr**
> kotlin.collections.List&lt;MMRHistory&gt; heroMmr(heroId, accountIds, maxMatchId)

Batch Hero MMR (Deprecated)

 Deprecated. Valve reports a single account-wide rank, not a per-hero one, so this returns each player&#39;s rank on their latest ranked match played on that hero.  Use &#x60;/v1/players/{account_id}/rank&#x60; instead. 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = MMRApi()
val heroId : kotlin.Int = 56 // kotlin.Int | The hero ID to fetch the MMR history for. See more: <https://api.deadlock-api.com/v1/assets/heroes>
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
| **heroId** | **kotlin.Int**| The hero ID to fetch the MMR history for. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | |
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

<a id="heroMmrDistribution"></a>
# **heroMmrDistribution**
> kotlin.collections.List&lt;DistributionEntry&gt; heroMmrDistribution(heroId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, minMatchId, maxMatchId)

Hero MMR Distribution (Deprecated)

 Deprecated. Valve reports a single account-wide rank, not a per-hero one, so this counts players by the rank they had on their latest ranked match played on that hero.  Use &#x60;/v1/analytics/badge-distribution&#x60; instead. 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = MMRApi()
val heroId : kotlin.Int = 56 // kotlin.Int | The hero ID to fetch the MMR history for. See more: <https://api.deadlock-api.com/v1/assets/heroes>
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
    val result : kotlin.collections.List<DistributionEntry> = apiInstance.heroMmrDistribution(heroId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, minMatchId, maxMatchId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MMRApi#heroMmrDistribution")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MMRApi#heroMmrDistribution")
    e.printStackTrace()
}
```

### Parameters
| **heroId** | **kotlin.Int**| The hero ID to fetch the MMR history for. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | |
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1783036800L] |
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

Hero MMR History (Deprecated)

 Deprecated. Valve reports a single account-wide rank, not a per-hero one, so this returns the player&#39;s rank at the start of each ranked match they played on that hero.  Use the &#x60;ranked_display_badge&#x60; and &#x60;ranked_delta&#x60; fields of &#x60;/v1/players/{account_id}/match-history&#x60; instead. 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = MMRApi()
val accountId : kotlin.Int = 56 // kotlin.Int | The players `SteamID3`
val heroId : kotlin.Int = 56 // kotlin.Int | The hero ID to fetch the MMR history for. See more: <https://api.deadlock-api.com/v1/assets/heroes>
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
| **heroId** | **kotlin.Int**| The hero ID to fetch the MMR history for. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | |

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

Batch MMR (Deprecated)

 Deprecated. The MMR estimate is gone, this now returns the rank Valve reported for each player on their latest ranked match. Players without a ranked match carrying a rank are left out.  Use &#x60;/v1/players/{account_id}/rank&#x60; instead. 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

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

<a id="mmrDistribution"></a>
# **mmrDistribution**
> kotlin.collections.List&lt;DistributionEntry&gt; mmrDistribution(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, minMatchId, maxMatchId)

MMR Distribution (Deprecated)

 Deprecated. The MMR estimate is gone, this now counts players by the rank Valve reported on their latest ranked match within the filtered range.  Use &#x60;/v1/analytics/badge-distribution&#x60; instead. 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

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
    val result : kotlin.collections.List<DistributionEntry> = apiInstance.mmrDistribution(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, minMatchId, maxMatchId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MMRApi#mmrDistribution")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MMRApi#mmrDistribution")
    e.printStackTrace()
}
```

### Parameters
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1783036800L] |
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

<a id="mmrHistory"></a>
# **mmrHistory**
> kotlin.collections.List&lt;MMRHistory&gt; mmrHistory(accountId)

MMR History (Deprecated)

 Deprecated. The MMR estimate is gone, this now returns one entry per ranked match with the rank Valve reported for the player at the start of that match.  Use the &#x60;ranked_display_badge&#x60; and &#x60;ranked_delta&#x60; fields of &#x60;/v1/players/{account_id}/match-history&#x60; instead. 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

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

