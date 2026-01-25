# PlayersApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**enemyStats**](PlayersApi.md#enemyStats) | **GET** /v1/players/{account_id}/enemy-stats | Enemy Stats |
| [**matchHistory**](PlayersApi.md#matchHistory) | **GET** /v1/players/{account_id}/match-history | Match History |
| [**mateStats**](PlayersApi.md#mateStats) | **GET** /v1/players/{account_id}/mate-stats | Mate Stats |
| [**partyStats**](PlayersApi.md#partyStats) | **GET** /v1/players/{account_id}/party-stats | Party Stats |
| [**playerHeroStats**](PlayersApi.md#playerHeroStats) | **GET** /v1/players/hero-stats | Hero Stats |
| [**steam**](PlayersApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile |
| [**steamSearch**](PlayersApi.md#steamSearch) | **GET** /v1/players/steam-search | Steam Profile Search |


<a id="enemyStats"></a>
# **enemyStats**
> kotlin.collections.List&lt;EnemyStats&gt; enemyStats(accountId, gameMode, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minMatchId, maxMatchId, minMatchesPlayed, maxMatchesPlayed)

Enemy Stats

 This endpoint returns the enemy stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = PlayersApi()
val accountId : kotlin.Int = 56 // kotlin.Int | The players `SteamID3`
val gameMode : kotlin.String = gameMode_example // kotlin.String | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. If not specified, both are included.
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val maxDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val minMatchesPlayed : kotlin.Long = 789 // kotlin.Long | Filter based on the number of matches played.
val maxMatchesPlayed : kotlin.Long = 789 // kotlin.Long | Filter based on the number of matches played.
try {
    val result : kotlin.collections.List<EnemyStats> = apiInstance.enemyStats(accountId, gameMode, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minMatchId, maxMatchId, minMatchesPlayed, maxMatchesPlayed)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PlayersApi#enemyStats")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PlayersApi#enemyStats")
    e.printStackTrace()
}
```

### Parameters
| **accountId** | **kotlin.Int**| The players &#x60;SteamID3&#x60; | |
| **gameMode** | **kotlin.String**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. If not specified, both are included. | [optional] [enum: normal, street_brawl] |
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **minDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **maxDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **minMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **minMatchesPlayed** | **kotlin.Long**| Filter based on the number of matches played. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **maxMatchesPlayed** | **kotlin.Long**| Filter based on the number of matches played. | [optional] |

### Return type

[**kotlin.collections.List&lt;EnemyStats&gt;**](EnemyStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="matchHistory"></a>
# **matchHistory**
> kotlin.collections.List&lt;PlayerMatchHistoryEntry&gt; matchHistory(accountId, forceRefetch, onlyStoredHistory)

Match History

 This endpoint returns the player match history for the given &#x60;account_id&#x60;.  The player match history is a combination of the data from **Steam** and **ClickHouse**, so you always get the most up-to-date data and full history.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGcGetMatchHistory - CMsgClientToGcGetMatchHistoryResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 5req/min&lt;br&gt;With &#x60;only_stored_history&#x3D;true&#x60;: 100req/s&lt;br&gt;With &#x60;force_refetch&#x3D;true&#x60;: 5req/h | | Key | 50req/min &amp; 1000req/h&lt;br&gt;With &#x60;only_stored_history&#x3D;true&#x60;: -&lt;br&gt;With &#x60;force_refetch&#x3D;true&#x60;: 5req/h | | Global | 2000req/h&lt;br&gt;With &#x60;only_stored_history&#x3D;true&#x60;: -&lt;br&gt;With &#x60;force_refetch&#x3D;true&#x60;: 10req/h |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = PlayersApi()
val accountId : kotlin.Int = 56 // kotlin.Int | The players `SteamID3`
val forceRefetch : kotlin.Boolean = true // kotlin.Boolean | Refetch the match history from Steam, even if it is already cached in `ClickHouse`. Only use this if you are sure that the data in `ClickHouse` is outdated. Enabling this flag results in a strict rate limit.
val onlyStoredHistory : kotlin.Boolean = true // kotlin.Boolean | Return only the already stored match history from `ClickHouse`. There is no rate limit for this option, so if you need a lot of data, you can use this option. This option is not compatible with `force_refetch`.
try {
    val result : kotlin.collections.List<PlayerMatchHistoryEntry> = apiInstance.matchHistory(accountId, forceRefetch, onlyStoredHistory)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PlayersApi#matchHistory")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PlayersApi#matchHistory")
    e.printStackTrace()
}
```

### Parameters
| **accountId** | **kotlin.Int**| The players &#x60;SteamID3&#x60; | |
| **forceRefetch** | **kotlin.Boolean**| Refetch the match history from Steam, even if it is already cached in &#x60;ClickHouse&#x60;. Only use this if you are sure that the data in &#x60;ClickHouse&#x60; is outdated. Enabling this flag results in a strict rate limit. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **onlyStoredHistory** | **kotlin.Boolean**| Return only the already stored match history from &#x60;ClickHouse&#x60;. There is no rate limit for this option, so if you need a lot of data, you can use this option. This option is not compatible with &#x60;force_refetch&#x60;. | [optional] |

### Return type

[**kotlin.collections.List&lt;PlayerMatchHistoryEntry&gt;**](PlayerMatchHistoryEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="mateStats"></a>
# **mateStats**
> kotlin.collections.List&lt;MateStats&gt; mateStats(accountId, gameMode, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minMatchId, maxMatchId, minMatchesPlayed, maxMatchesPlayed, sameParty)

Mate Stats

 This endpoint returns the mate stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = PlayersApi()
val accountId : kotlin.Int = 56 // kotlin.Int | The players `SteamID3`
val gameMode : kotlin.String = gameMode_example // kotlin.String | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. If not specified, both are included.
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val maxDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val minMatchesPlayed : kotlin.Long = 789 // kotlin.Long | Filter based on the number of matches played.
val maxMatchesPlayed : kotlin.Long = 789 // kotlin.Long | Filter based on the number of matches played.
val sameParty : kotlin.Boolean = true // kotlin.Boolean | Filter based on whether the mates were on the same party. **Careful:** this will require us to use the match metadata, which can have missing matches.
try {
    val result : kotlin.collections.List<MateStats> = apiInstance.mateStats(accountId, gameMode, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minMatchId, maxMatchId, minMatchesPlayed, maxMatchesPlayed, sameParty)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PlayersApi#mateStats")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PlayersApi#mateStats")
    e.printStackTrace()
}
```

### Parameters
| **accountId** | **kotlin.Int**| The players &#x60;SteamID3&#x60; | |
| **gameMode** | **kotlin.String**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. If not specified, both are included. | [optional] [enum: normal, street_brawl] |
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **minDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **maxDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **minMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **minMatchesPlayed** | **kotlin.Long**| Filter based on the number of matches played. | [optional] |
| **maxMatchesPlayed** | **kotlin.Long**| Filter based on the number of matches played. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **sameParty** | **kotlin.Boolean**| Filter based on whether the mates were on the same party. **Careful:** this will require us to use the match metadata, which can have missing matches. | [optional] [default to true] |

### Return type

[**kotlin.collections.List&lt;MateStats&gt;**](MateStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="partyStats"></a>
# **partyStats**
> kotlin.collections.List&lt;PartyStats&gt; partyStats(accountId, gameMode, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minMatchId, maxMatchId)

Party Stats

 This endpoint returns the party stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = PlayersApi()
val accountId : kotlin.Int = 56 // kotlin.Int | The players `SteamID3`
val gameMode : kotlin.String = gameMode_example // kotlin.String | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. If not specified, both are included.
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val maxDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
try {
    val result : kotlin.collections.List<PartyStats> = apiInstance.partyStats(accountId, gameMode, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minMatchId, maxMatchId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PlayersApi#partyStats")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PlayersApi#partyStats")
    e.printStackTrace()
}
```

### Parameters
| **accountId** | **kotlin.Int**| The players &#x60;SteamID3&#x60; | |
| **gameMode** | **kotlin.String**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. If not specified, both are included. | [optional] [enum: normal, street_brawl] |
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **minDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **maxDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **minMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |

### Return type

[**kotlin.collections.List&lt;PartyStats&gt;**](PartyStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="playerHeroStats"></a>
# **playerHeroStats**
> kotlin.collections.List&lt;HeroStats&gt; playerHeroStats(accountIds, gameMode, heroIds, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId)

Hero Stats

 This endpoint returns statistics for each hero played by a given player account.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = PlayersApi()
val accountIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of account ids, Account IDs are in `SteamID3` format.
val gameMode : kotlin.String = gameMode_example // kotlin.String | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. If not specified, both are included.
val heroIds : kotlin.String = heroIds_example // kotlin.String | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes>
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val maxDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val minNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their final net worth.
val maxNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their final net worth.
val minAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val maxAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
try {
    val result : kotlin.collections.List<HeroStats> = apiInstance.playerHeroStats(accountIds, gameMode, heroIds, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PlayersApi#playerHeroStats")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PlayersApi#playerHeroStats")
    e.printStackTrace()
}
```

### Parameters
| **accountIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | |
| **gameMode** | **kotlin.String**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. If not specified, both are included. | [optional] [enum: normal, street_brawl] |
| **heroIds** | **kotlin.String**| Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **minDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **maxDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **minNetworth** | **kotlin.Long**| Filter players based on their final net worth. | [optional] |
| **maxNetworth** | **kotlin.Long**| Filter players based on their final net worth. | [optional] |
| **minAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **maxAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **minMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |

### Return type

[**kotlin.collections.List&lt;HeroStats&gt;**](HeroStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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

val apiInstance = PlayersApi()
val accountIds : kotlin.collections.List<kotlin.Long> =  // kotlin.collections.List<kotlin.Long> | Comma separated list of account ids, Account IDs are in `SteamID3` format.
try {
    val result : kotlin.collections.List<SteamProfile> = apiInstance.steam(accountIds)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PlayersApi#steam")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PlayersApi#steam")
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

val apiInstance = PlayersApi()
val searchQuery : kotlin.String = searchQuery_example // kotlin.String | Search query for Steam profiles.
try {
    val result : kotlin.collections.List<SteamProfile> = apiInstance.steamSearch(searchQuery)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PlayersApi#steamSearch")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PlayersApi#steamSearch")
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

