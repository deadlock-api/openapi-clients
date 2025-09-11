# MatchesApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**activeMatches**](MatchesApi.md#activeMatches) | **GET** /v1/matches/active | Active |
| [**activeMatchesRaw**](MatchesApi.md#activeMatchesRaw) | **GET** /v1/matches/active/raw | Active as Protobuf |
| [**badgeDistribution**](MatchesApi.md#badgeDistribution) | **GET** /v1/matches/badge-distribution | Badge Distribution |
| [**bulkMetadata**](MatchesApi.md#bulkMetadata) | **GET** /v1/matches/metadata | Bulk Metadata |
| [**metadata**](MatchesApi.md#metadata) | **GET** /v1/matches/{match_id}/metadata | Metadata |
| [**metadataRaw**](MatchesApi.md#metadataRaw) | **GET** /v1/matches/{match_id}/metadata/raw | Metadata as Protobuf |
| [**recentlyFetched**](MatchesApi.md#recentlyFetched) | **GET** /v1/matches/recently-fetched | Recently Fetched |
| [**salts**](MatchesApi.md#salts) | **GET** /v1/matches/{match_id}/salts | Salts |
| [**url**](MatchesApi.md#url) | **GET** /v1/matches/{match_id}/live/url | Live Broadcast URL |


<a id="activeMatches"></a>
# **activeMatches**
> kotlin.collections.List&lt;ActiveMatch&gt; activeMatches(accountId, accountIds)

Active

 Returns active matches that are currently being played.  Fetched from the watch tab in game, which is limited to the **top 200 matches**.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = MatchesApi()
val accountId : kotlin.Int = 56 // kotlin.Int | The account ID to filter active matches by (`SteamID3`)
val accountIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of account ids to include
try {
    val result : kotlin.collections.List<ActiveMatch> = apiInstance.activeMatches(accountId, accountIds)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MatchesApi#activeMatches")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MatchesApi#activeMatches")
    e.printStackTrace()
}
```

### Parameters
| **accountId** | **kotlin.Int**| The account ID to filter active matches by (&#x60;SteamID3&#x60;) | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**kotlin.collections.List&lt;ActiveMatch&gt;**](ActiveMatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="activeMatchesRaw"></a>
# **activeMatchesRaw**
> kotlin.collections.List&lt;kotlin.Int&gt; activeMatchesRaw()

Active as Protobuf

 Returns active matches that are currently being played, serialized as protobuf message.  Fetched from the watch tab in game, which is limited to the **top 200 matches**.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetActiveMatchesResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = MatchesApi()
try {
    val result : kotlin.collections.List<kotlin.Int> = apiInstance.activeMatchesRaw()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MatchesApi#activeMatchesRaw")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MatchesApi#activeMatchesRaw")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**kotlin.collections.List&lt;kotlin.Int&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

<a id="badgeDistribution"></a>
# **badgeDistribution**
> kotlin.collections.List&lt;BadgeDistribution&gt; badgeDistribution(minUnixTimestamp, maxUnixTimestamp, minMatchId, maxMatchId)

Badge Distribution

 This endpoint returns the player badge distribution.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = MatchesApi()
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
try {
    val result : kotlin.collections.List<BadgeDistribution> = apiInstance.badgeDistribution(minUnixTimestamp, maxUnixTimestamp, minMatchId, maxMatchId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MatchesApi#badgeDistribution")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MatchesApi#badgeDistribution")
    e.printStackTrace()
}
```

### Parameters
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **minMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |

### Return type

[**kotlin.collections.List&lt;BadgeDistribution&gt;**](BadgeDistribution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="bulkMetadata"></a>
# **bulkMetadata**
> kotlin.collections.List&lt;kotlin.Int&gt; bulkMetadata(includeInfo, includeObjectives, includeMidBoss, includePlayerInfo, includePlayerItems, includePlayerStats, includePlayerDeathDetails, matchIds, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, accountIds, orderBy, orderDirection, limit)

Bulk Metadata

 This endpoints lets you fetch multiple match metadata at once. The response is a JSON array of match metadata.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 4req/s | | Key | - | | Global | 10req/s |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = MatchesApi()
val includeInfo : kotlin.Boolean = true // kotlin.Boolean | Include match info in the response.
val includeObjectives : kotlin.Boolean = true // kotlin.Boolean | Include objectives in the response.
val includeMidBoss : kotlin.Boolean = true // kotlin.Boolean | Include midboss in the response.
val includePlayerInfo : kotlin.Boolean = true // kotlin.Boolean | Include player info in the response.
val includePlayerItems : kotlin.Boolean = true // kotlin.Boolean | Include player items in the response.
val includePlayerStats : kotlin.Boolean = true // kotlin.Boolean | Include player stats in the response.
val includePlayerDeathDetails : kotlin.Boolean = true // kotlin.Boolean | Include player death details in the response.
val matchIds : kotlin.collections.List<kotlin.Long> =  // kotlin.collections.List<kotlin.Long> | Comma separated list of match ids, limited by `limit`
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val maxDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val minAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val maxAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val isHighSkillRangeParties : kotlin.Boolean = true // kotlin.Boolean | Filter matches based on whether they are in the high skill range.
val isLowPriPool : kotlin.Boolean = true // kotlin.Boolean | Filter matches based on whether they are in the low priority pool.
val isNewPlayerPool : kotlin.Boolean = true // kotlin.Boolean | Filter matches based on whether they are in the new player pool.
val accountIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Filter matches by account IDs of players that participated in the match.
val orderBy : kotlin.String = orderBy_example // kotlin.String | The field to order the results by.
val orderDirection : kotlin.String = orderDirection_example // kotlin.String | The direction to order the results by.
val limit : kotlin.Int = 56 // kotlin.Int | The maximum number of matches to return.
try {
    val result : kotlin.collections.List<kotlin.Int> = apiInstance.bulkMetadata(includeInfo, includeObjectives, includeMidBoss, includePlayerInfo, includePlayerItems, includePlayerStats, includePlayerDeathDetails, matchIds, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, accountIds, orderBy, orderDirection, limit)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MatchesApi#bulkMetadata")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MatchesApi#bulkMetadata")
    e.printStackTrace()
}
```

### Parameters
| **includeInfo** | **kotlin.Boolean**| Include match info in the response. | [optional] [default to true] |
| **includeObjectives** | **kotlin.Boolean**| Include objectives in the response. | [optional] |
| **includeMidBoss** | **kotlin.Boolean**| Include midboss in the response. | [optional] |
| **includePlayerInfo** | **kotlin.Boolean**| Include player info in the response. | [optional] |
| **includePlayerItems** | **kotlin.Boolean**| Include player items in the response. | [optional] |
| **includePlayerStats** | **kotlin.Boolean**| Include player stats in the response. | [optional] |
| **includePlayerDeathDetails** | **kotlin.Boolean**| Include player death details in the response. | [optional] |
| **matchIds** | [**kotlin.collections.List&lt;kotlin.Long&gt;**](kotlin.Long.md)| Comma separated list of match ids, limited by &#x60;limit&#x60; | [optional] |
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **minDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **maxDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **minAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **maxAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **minMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **isHighSkillRangeParties** | **kotlin.Boolean**| Filter matches based on whether they are in the high skill range. | [optional] |
| **isLowPriPool** | **kotlin.Boolean**| Filter matches based on whether they are in the low priority pool. | [optional] |
| **isNewPlayerPool** | **kotlin.Boolean**| Filter matches based on whether they are in the new player pool. | [optional] |
| **accountIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Filter matches by account IDs of players that participated in the match. | [optional] |
| **orderBy** | **kotlin.String**| The field to order the results by. | [optional] [enum: match_id, start_time] |
| **orderDirection** | **kotlin.String**| The direction to order the results by. | [optional] [enum: desc, asc] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **kotlin.Int**| The maximum number of matches to return. | [optional] [default to 1000] |

### Return type

**kotlin.collections.List&lt;kotlin.Int&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

<a id="metadata"></a>
# **metadata**
> metadata(matchId, isCustom)

Metadata

 This endpoint returns the match metadata for the given &#x60;match_id&#x60; parsed into JSON.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From Cache: 100req/s&lt;br&gt;From S3: 100req/10s&lt;br&gt;From Steam: 10req/30mins | | Key | From Cache: 100req/s&lt;br&gt;From S3: 100req/s&lt;br&gt;From Steam: 10req/min | | Global | From Cache: 100req/s&lt;br&gt;From S3: 700req/s&lt;br&gt;From Steam: 10req/10s |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = MatchesApi()
val matchId : kotlin.Long = 789 // kotlin.Long | The match ID
val isCustom : kotlin.Boolean = true // kotlin.Boolean | 
try {
    apiInstance.metadata(matchId, isCustom)
} catch (e: ClientException) {
    println("4xx response calling MatchesApi#metadata")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MatchesApi#metadata")
    e.printStackTrace()
}
```

### Parameters
| **matchId** | **kotlin.Long**| The match ID | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **isCustom** | **kotlin.Boolean**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a id="metadataRaw"></a>
# **metadataRaw**
> kotlin.collections.List&lt;kotlin.Int&gt; metadataRaw(matchId, isCustom)

Metadata as Protobuf

 This endpoints returns the raw .meta.bz2 file for the given &#x60;match_id&#x60;.  You have to decompress it and decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From Cache: 100req/s&lt;br&gt;From S3: 100req/10s&lt;br&gt;From Steam: 10req/30mins | | Key | From Cache: 100req/s&lt;br&gt;From S3: 100req/s&lt;br&gt;From Steam: 10req/min | | Global | From Cache: 100req/s&lt;br&gt;From S3: 700req/s&lt;br&gt;From Steam: 10req/10s |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = MatchesApi()
val matchId : kotlin.Long = 789 // kotlin.Long | The match ID
val isCustom : kotlin.Boolean = true // kotlin.Boolean | 
try {
    val result : kotlin.collections.List<kotlin.Int> = apiInstance.metadataRaw(matchId, isCustom)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MatchesApi#metadataRaw")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MatchesApi#metadataRaw")
    e.printStackTrace()
}
```

### Parameters
| **matchId** | **kotlin.Long**| The match ID | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **isCustom** | **kotlin.Boolean**|  | [optional] |

### Return type

**kotlin.collections.List&lt;kotlin.Int&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

<a id="recentlyFetched"></a>
# **recentlyFetched**
> kotlin.collections.List&lt;ClickhouseMatchInfo&gt; recentlyFetched()

Recently Fetched

 This endpoint returns a list of match ids that have been fetched within the last 10 minutes.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = MatchesApi()
try {
    val result : kotlin.collections.List<ClickhouseMatchInfo> = apiInstance.recentlyFetched()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MatchesApi#recentlyFetched")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MatchesApi#recentlyFetched")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;ClickhouseMatchInfo&gt;**](ClickhouseMatchInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="salts"></a>
# **salts**
> MatchSaltsResponse salts(matchId)

Salts

 This endpoints returns salts that can be used to fetch metadata and demofile for a match.  **Note:** We currently fetch many matches without salts, so for these matches we do not have salts stored.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From DB: 100req/s&lt;br&gt;From Steam: 10req/30mins | | Key | From DB: -&lt;br&gt;From Steam: 10req/min | | Global | From DB: -&lt;br&gt;From Steam: 10req/10s |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = MatchesApi()
val matchId : kotlin.Long = 789 // kotlin.Long | The match ID
try {
    val result : MatchSaltsResponse = apiInstance.salts(matchId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MatchesApi#salts")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MatchesApi#salts")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **matchId** | **kotlin.Long**| The match ID | |

### Return type

[**MatchSaltsResponse**](MatchSaltsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="url"></a>
# **url**
> MatchSpectateResponse url(matchId)

Live Broadcast URL

 This endpoints spectates a match and returns the live URL to be used in any demofile broadcast parser.  Example Parsers: - [Demofile-Net](https://github.com/saul/demofile-net) - [Haste](https://github.com/blukai/haste/)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 10req/30mins | | Key | 60req/min | | Global | 100req/10s |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = MatchesApi()
val matchId : kotlin.Long = 789 // kotlin.Long | The match ID
try {
    val result : MatchSpectateResponse = apiInstance.url(matchId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MatchesApi#url")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MatchesApi#url")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **matchId** | **kotlin.Long**| The match ID | |

### Return type

[**MatchSpectateResponse**](MatchSpectateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

