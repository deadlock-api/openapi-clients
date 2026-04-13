# PlayersApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**accountStats**](PlayersApi.md#accountStats) | **GET** /v1/players/{account_id}/account-stats | Account Stats |
| [**card**](PlayersApi.md#card) | **GET** /v1/players/{account_id}/card | Card |
| [**enemyStats**](PlayersApi.md#enemyStats) | **GET** /v1/players/{account_id}/enemy-stats | Enemy Stats |
| [**matchHistory**](PlayersApi.md#matchHistory) | **GET** /v1/players/{account_id}/match-history | Match History |
| [**mateStats**](PlayersApi.md#mateStats) | **GET** /v1/players/{account_id}/mate-stats | Mate Stats |
| [**playerHeroStats**](PlayersApi.md#playerHeroStats) | **GET** /v1/players/hero-stats | Hero Stats |
| [**rankPredict**](PlayersApi.md#rankPredict) | **GET** /v1/players/{account_id}/rank-predict | Rank Predict |


<a id="accountStats"></a>
# **accountStats**
> kotlin.collections.List&lt;PlayerAccountStats&gt; accountStats(accountId)

Account Stats

 This endpoint returns the player account stats for the given &#x60;account_id&#x60;.  !THIS IS A PATREON ONLY ENDPOINT!  You have to be friend with one of the bots to use this endpoint. On first use this endpoint will return an error with a list of invite links to add the bot as friend. From then on you can use this endpoint.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGcGetAccountStats - CMsgAccountStats  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 5req/min | | Key | 20req/min &amp; 800req/h | | Global | 200req/min |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = PlayersApi()
val accountId : kotlin.Int = 56 // kotlin.Int | The players `SteamID3`
try {
    val result : kotlin.collections.List<PlayerAccountStats> = apiInstance.accountStats(accountId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PlayersApi#accountStats")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PlayersApi#accountStats")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountId** | **kotlin.Int**| The players &#x60;SteamID3&#x60; | |

### Return type

[**kotlin.collections.List&lt;PlayerAccountStats&gt;**](PlayerAccountStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="card"></a>
# **card**
> kotlin.collections.List&lt;PlayerCard&gt; card(accountId)

Card

 This endpoint returns the player card for the given &#x60;account_id&#x60;.  !THIS IS A PATREON ONLY ENDPOINT!  You have to be friend with one of the bots to use this endpoint. On first use this endpoint will return an error with a list of invite links to add the bot as friend. From then on you can use this endpoint.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGcGetProfileCard - CMsgCitadelProfileCard  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 5req/min | | Key | 20req/min &amp; 800req/h | | Global | 200req/min |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = PlayersApi()
val accountId : kotlin.Int = 56 // kotlin.Int | The players `SteamID3`
try {
    val result : kotlin.collections.List<PlayerCard> = apiInstance.card(accountId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PlayersApi#card")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PlayersApi#card")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountId** | **kotlin.Int**| The players &#x60;SteamID3&#x60; | |

### Return type

[**kotlin.collections.List&lt;PlayerCard&gt;**](PlayerCard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
val gameMode : kotlin.String = gameMode_example // kotlin.String | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
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
| **gameMode** | **kotlin.String**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] [enum: normal, street_brawl, explore_n_y_c, internal] |
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
> kotlin.collections.List&lt;PlayerMatchHistoryEntry&gt; matchHistory(accountId, forceRefetch)

Match History

 This endpoint returns the player match history for the given &#x60;account_id&#x60;.  If the account is friends with one of our bots, the match history is a combination of the data from **Steam** and **ClickHouse**, so you always get the most up-to-date data and full history. If the account is not friends with a bot, only the stored match history from **ClickHouse** is returned.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGcGetMatchHistory - CMsgClientToGcGetMatchHistoryResponse  ### Rate Limits (only applies to bot friends): | Type | Limit | | ---- | ----- | | IP | 100req/s&lt;br&gt;Bot-Friend: 3req/h&lt;br&gt;With &#x60;force_refetch&#x3D;true&#x60;: 1req/h | | Key | -&lt;br&gt;Bot-Friend: 300req/h&lt;br&gt;With &#x60;force_refetch&#x3D;true&#x60;: 5req/h | | Global | -&lt;br&gt;Bot-Friend: 1500req/h&lt;br&gt;With &#x60;force_refetch&#x3D;true&#x60;: 10req/h |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = PlayersApi()
val accountId : kotlin.Int = 56 // kotlin.Int | The players `SteamID3`
val forceRefetch : kotlin.Boolean = true // kotlin.Boolean | Refetch the match history from Steam, even if it is already cached in `ClickHouse`. Only use this if you are sure that the data in `ClickHouse` is outdated. Enabling this flag results in a strict rate limit.
try {
    val result : kotlin.collections.List<PlayerMatchHistoryEntry> = apiInstance.matchHistory(accountId, forceRefetch)
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
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **forceRefetch** | **kotlin.Boolean**| Refetch the match history from Steam, even if it is already cached in &#x60;ClickHouse&#x60;. Only use this if you are sure that the data in &#x60;ClickHouse&#x60; is outdated. Enabling this flag results in a strict rate limit. | [optional] |

### Return type

[**kotlin.collections.List&lt;PlayerMatchHistoryEntry&gt;**](PlayerMatchHistoryEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="mateStats"></a>
# **mateStats**
> kotlin.collections.List&lt;MateStats&gt; mateStats(accountId, gameMode, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minMatchId, maxMatchId, minMatchesPlayed, maxMatchesPlayed)

Mate Stats

 This endpoint returns the mate stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = PlayersApi()
val accountId : kotlin.Int = 56 // kotlin.Int | The players `SteamID3`
val gameMode : kotlin.String = gameMode_example // kotlin.String | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val maxDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val minMatchesPlayed : kotlin.Long = 789 // kotlin.Long | Filter based on the number of matches played.
val maxMatchesPlayed : kotlin.Long = 789 // kotlin.Long | Filter based on the number of matches played.
try {
    val result : kotlin.collections.List<MateStats> = apiInstance.mateStats(accountId, gameMode, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minMatchId, maxMatchId, minMatchesPlayed, maxMatchesPlayed)
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
| **gameMode** | **kotlin.String**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] [enum: normal, street_brawl, explore_n_y_c, internal] |
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

[**kotlin.collections.List&lt;MateStats&gt;**](MateStats.md)

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
val gameMode : kotlin.String = gameMode_example // kotlin.String | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
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
| **gameMode** | **kotlin.String**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] [enum: normal, street_brawl, explore_n_y_c, internal] |
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

<a id="rankPredict"></a>
# **rankPredict**
> RankPredictResponse rankPredict(accountId)

Rank Predict

 Predicts a player&#39;s current rank badge from their last 30 ranked/unranked matches. Requires at least 30 eligible matches (Ranked or Unranked, Normal game mode) with valid badge data.  &gt; **This is an ML prediction and may be inaccurate.** The model has no access to the player&#39;s &gt; actual hidden MMR — it infers rank from match context signals only.  ### Model Accuracy (5-fold cross-validation)  | Metric | Value | |--------|-------| | R²     | 0.940 | | MAE    | 1.40 sub-ranks | | RMSE   | 2.22 sub-ranks | | Within ±1 sub-rank | 69.1% | | Within ±3 sub-ranks | 90.4% | | Within ±5 sub-ranks | 96.7% | | Within ±6 sub-ranks | 97.7% | | Within ±10 sub-ranks | 99.7% |  Accuracy by tier:  | Tier range | n | MAE | |------------|---|-----| | Low (1-4)  | 430 | 4.79 sub-ranks | | Mid (5-7)  | 1350 | 3.11 sub-ranks | | High (8-11)| 25020 | 1.25 sub-ranks |  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = PlayersApi()
val accountId : kotlin.Int = 56 // kotlin.Int | The players `SteamID3`
try {
    val result : RankPredictResponse = apiInstance.rankPredict(accountId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PlayersApi#rankPredict")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PlayersApi#rankPredict")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountId** | **kotlin.Int**| The players &#x60;SteamID3&#x60; | |

### Return type

[**RankPredictResponse**](RankPredictResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

