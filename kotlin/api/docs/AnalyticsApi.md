# AnalyticsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**abilityOrderStats**](AnalyticsApi.md#abilityOrderStats) | **GET** /v1/analytics/ability-order-stats | Ability Order Stats |
| [**badgeDistribution**](AnalyticsApi.md#badgeDistribution) | **GET** /v1/analytics/badge-distribution | Badge Distribution |
| [**buildItemStats**](AnalyticsApi.md#buildItemStats) | **GET** /v1/analytics/build-item-stats | Build Item Stats |
| [**heroCombStats**](AnalyticsApi.md#heroCombStats) | **GET** /v1/analytics/hero-comb-stats | Hero Comb Stats |
| [**heroCountersStats**](AnalyticsApi.md#heroCountersStats) | **GET** /v1/analytics/hero-counter-stats | Hero Counter Stats |
| [**heroScoreboard**](AnalyticsApi.md#heroScoreboard) | **GET** /v1/analytics/scoreboards/heroes | Hero Scoreboard |
| [**heroStats**](AnalyticsApi.md#heroStats) | **GET** /v1/analytics/hero-stats | Hero Stats |
| [**heroSynergiesStats**](AnalyticsApi.md#heroSynergiesStats) | **GET** /v1/analytics/hero-synergy-stats | Hero Synergy Stats |
| [**itemPermutationStats**](AnalyticsApi.md#itemPermutationStats) | **GET** /v1/analytics/item-permutation-stats | Item Permutation Stats |
| [**itemStats**](AnalyticsApi.md#itemStats) | **GET** /v1/analytics/item-stats | Item Stats |
| [**playerScoreboard**](AnalyticsApi.md#playerScoreboard) | **GET** /v1/analytics/scoreboards/players | Player Scoreboard |
| [**playerStatsMetrics**](AnalyticsApi.md#playerStatsMetrics) | **GET** /v1/analytics/player-stats/metrics | Player Stats Metrics |


<a id="abilityOrderStats"></a>
# **abilityOrderStats**
> kotlin.collections.List&lt;AnalyticsAbilityOrderStats&gt; abilityOrderStats(heroId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minAbilityUpgrades, maxAbilityUpgrades, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, minMatches, accountId, accountIds)

Ability Order Stats

 Retrieves statistics for the ability order of a hero.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = AnalyticsApi()
val heroId : kotlin.Int = 56 // kotlin.Int | See more: <https://assets.deadlock-api.com/v2/heroes>
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val maxDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val minAbilityUpgrades : kotlin.Long = 789 // kotlin.Long | Filter players based on their minimum number of ability upgrades over the whole match.
val maxAbilityUpgrades : kotlin.Long = 789 // kotlin.Long | Filter players based on their maximum number of ability upgrades over the whole match.
val minNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val maxNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val minAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val maxAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val minMatches : kotlin.Int = 56 // kotlin.Int | The minimum number of matches played for an ability order to be included in the response.
val accountId : kotlin.Int = 56 // kotlin.Int | Filter for matches with a specific player account ID.
val accountIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of account ids to include
try {
    val result : kotlin.collections.List<AnalyticsAbilityOrderStats> = apiInstance.abilityOrderStats(heroId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minAbilityUpgrades, maxAbilityUpgrades, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, minMatches, accountId, accountIds)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AnalyticsApi#abilityOrderStats")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AnalyticsApi#abilityOrderStats")
    e.printStackTrace()
}
```

### Parameters
| **heroId** | **kotlin.Int**| See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | |
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1757030400L] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **minDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **maxDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **minAbilityUpgrades** | **kotlin.Long**| Filter players based on their minimum number of ability upgrades over the whole match. | [optional] |
| **maxAbilityUpgrades** | **kotlin.Long**| Filter players based on their maximum number of ability upgrades over the whole match. | [optional] |
| **minNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **maxNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **minAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **maxAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **minMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **minMatches** | **kotlin.Int**| The minimum number of matches played for an ability order to be included in the response. | [optional] [default to 20] |
| **accountId** | **kotlin.Int**| Filter for matches with a specific player account ID. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**kotlin.collections.List&lt;AnalyticsAbilityOrderStats&gt;**](AnalyticsAbilityOrderStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="badgeDistribution"></a>
# **badgeDistribution**
> kotlin.collections.List&lt;BadgeDistribution&gt; badgeDistribution(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, minMatchId, maxMatchId)

Badge Distribution

 This endpoint returns the player badge distribution.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = AnalyticsApi()
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
    val result : kotlin.collections.List<BadgeDistribution> = apiInstance.badgeDistribution(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, minMatchId, maxMatchId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AnalyticsApi#badgeDistribution")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AnalyticsApi#badgeDistribution")
    e.printStackTrace()
}
```

### Parameters
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1757030400L] |
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

[**kotlin.collections.List&lt;BadgeDistribution&gt;**](BadgeDistribution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="buildItemStats"></a>
# **buildItemStats**
> kotlin.collections.List&lt;BuildItemStats&gt; buildItemStats(heroId, minLastUpdatedUnixTimestamp, maxLastUpdatedUnixTimestamp)

Build Item Stats

 Retrieves item statistics from hero builds.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = AnalyticsApi()
val heroId : kotlin.Int = 56 // kotlin.Int | Filter builds based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
val minLastUpdatedUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter builds based on their last updated time (Unix timestamp). **Default:** 30 days ago.
val maxLastUpdatedUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter builds based on their last updated time (Unix timestamp).
try {
    val result : kotlin.collections.List<BuildItemStats> = apiInstance.buildItemStats(heroId, minLastUpdatedUnixTimestamp, maxLastUpdatedUnixTimestamp)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AnalyticsApi#buildItemStats")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AnalyticsApi#buildItemStats")
    e.printStackTrace()
}
```

### Parameters
| **heroId** | **kotlin.Int**| Filter builds based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **minLastUpdatedUnixTimestamp** | **kotlin.Long**| Filter builds based on their last updated time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1757030400L] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **maxLastUpdatedUnixTimestamp** | **kotlin.Long**| Filter builds based on their last updated time (Unix timestamp). | [optional] |

### Return type

[**kotlin.collections.List&lt;BuildItemStats&gt;**](BuildItemStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="heroCombStats"></a>
# **heroCombStats**
> kotlin.collections.List&lt;HeroCombStats&gt; heroCombStats(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, includeHeroIds, excludeHeroIds, minMatches, maxMatches, combSize, accountId, accountIds)

Hero Comb Stats

 Retrieves overall statistics for each hero combination.  Results are cached for **1 hour**. The cache key is determined by the specific combination of filter parameters used in the query. Subsequent requests using the exact same filters within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = AnalyticsApi()
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val maxDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val minNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val maxNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val minAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val maxAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val includeHeroIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of hero ids to include. See more: <https://assets.deadlock-api.com/v2/heroes>
val excludeHeroIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of hero ids to exclude. See more: <https://assets.deadlock-api.com/v2/heroes>
val minMatches : kotlin.Int = 56 // kotlin.Int | The minimum number of matches played for a hero combination to be included in the response.
val maxMatches : kotlin.Int = 56 // kotlin.Int | The maximum number of matches played for a hero combination to be included in the response.
val combSize : kotlin.Int = 56 // kotlin.Int | The combination size to return.
val accountId : kotlin.Int = 56 // kotlin.Int | Filter for matches with a specific player account ID.
val accountIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of account ids to include
try {
    val result : kotlin.collections.List<HeroCombStats> = apiInstance.heroCombStats(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, includeHeroIds, excludeHeroIds, minMatches, maxMatches, combSize, accountId, accountIds)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AnalyticsApi#heroCombStats")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AnalyticsApi#heroCombStats")
    e.printStackTrace()
}
```

### Parameters
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1757030400L] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **minDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **maxDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **minNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **maxNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **minAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **maxAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **minMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **includeHeroIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of hero ids to include. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **excludeHeroIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of hero ids to exclude. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **minMatches** | **kotlin.Int**| The minimum number of matches played for a hero combination to be included in the response. | [optional] [default to 20] |
| **maxMatches** | **kotlin.Int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] |
| **combSize** | **kotlin.Int**| The combination size to return. | [optional] [default to 6] |
| **accountId** | **kotlin.Int**| Filter for matches with a specific player account ID. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**kotlin.collections.List&lt;HeroCombStats&gt;**](HeroCombStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="heroCountersStats"></a>
# **heroCountersStats**
> kotlin.collections.List&lt;HeroCounterStats&gt; heroCountersStats(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minEnemyNetworth, maxEnemyNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, sameLaneFilter, minMatches, maxMatches, accountId, accountIds)

Hero Counter Stats

 Retrieves hero-versus-hero matchup statistics based on historical match data.  This endpoint analyzes completed matches to calculate how often a specific hero (&#x60;hero_id&#x60;) wins against an enemy hero (&#x60;enemy_hero_id&#x60;) and the total number of times they have faced each other under the specified filter conditions.  Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = AnalyticsApi()
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val maxDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val minNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val maxNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val minEnemyNetworth : kotlin.Long = 789 // kotlin.Long | Filter enemy players based on their net worth.
val maxEnemyNetworth : kotlin.Long = 789 // kotlin.Long | Filter enemy players based on their net worth.
val minAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val maxAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val sameLaneFilter : kotlin.Boolean = true // kotlin.Boolean | When `true`, only considers matchups where both `hero_id` and `enemy_hero_id` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane.
val minMatches : kotlin.Long = 789 // kotlin.Long | The minimum number of matches played for a hero combination to be included in the response.
val maxMatches : kotlin.Int = 56 // kotlin.Int | The maximum number of matches played for a hero combination to be included in the response.
val accountId : kotlin.Int = 56 // kotlin.Int | Filter for matches with a specific player account ID.
val accountIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of account ids to include
try {
    val result : kotlin.collections.List<HeroCounterStats> = apiInstance.heroCountersStats(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minEnemyNetworth, maxEnemyNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, sameLaneFilter, minMatches, maxMatches, accountId, accountIds)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AnalyticsApi#heroCountersStats")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AnalyticsApi#heroCountersStats")
    e.printStackTrace()
}
```

### Parameters
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1757030400L] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **minDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **maxDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **minNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **maxNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **minEnemyNetworth** | **kotlin.Long**| Filter enemy players based on their net worth. | [optional] |
| **maxEnemyNetworth** | **kotlin.Long**| Filter enemy players based on their net worth. | [optional] |
| **minAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **maxAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **minMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **sameLaneFilter** | **kotlin.Boolean**| When &#x60;true&#x60;, only considers matchups where both &#x60;hero_id&#x60; and &#x60;enemy_hero_id&#x60; were assigned to the same lane (e.g., both Mid Lane). When &#x60;false&#x60;, considers all matchups regardless of assigned lane. | [optional] [default to true] |
| **minMatches** | **kotlin.Long**| The minimum number of matches played for a hero combination to be included in the response. | [optional] [default to 20L] |
| **maxMatches** | **kotlin.Int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] |
| **accountId** | **kotlin.Int**| Filter for matches with a specific player account ID. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**kotlin.collections.List&lt;HeroCounterStats&gt;**](HeroCounterStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="heroScoreboard"></a>
# **heroScoreboard**
> kotlin.collections.List&lt;Entry&gt; heroScoreboard(sortBy, sortDirection, minMatches, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, accountId, accountIds)

Hero Scoreboard

 This endpoint returns the hero scoreboard.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = AnalyticsApi()
val sortBy : kotlin.String = sortBy_example // kotlin.String | The field to sort by.
val sortDirection : kotlin.String = sortDirection_example // kotlin.String | The direction to sort heroes in.
val minMatches : kotlin.Int = 56 // kotlin.Int | Filter by min number of matches played.
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val maxDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val minNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val maxNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val minAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val maxAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val accountId : kotlin.Int = 56 // kotlin.Int | Filter for matches with a specific player account ID.
val accountIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of account ids to include
try {
    val result : kotlin.collections.List<Entry> = apiInstance.heroScoreboard(sortBy, sortDirection, minMatches, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, accountId, accountIds)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AnalyticsApi#heroScoreboard")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AnalyticsApi#heroScoreboard")
    e.printStackTrace()
}
```

### Parameters
| **sortBy** | **kotlin.String**| The field to sort by. | [enum: matches, wins, losses, winrate, max_kills_per_match, avg_kills_per_match, kills, max_deaths_per_match, avg_deaths_per_match, deaths, max_damage_taken_per_match, avg_damage_taken_per_match, damage_taken, max_assists_per_match, avg_assists_per_match, assists, max_net_worth_per_match, avg_net_worth_per_match, net_worth, max_last_hits_per_match, avg_last_hits_per_match, last_hits, max_denies_per_match, avg_denies_per_match, denies, max_player_level_per_match, avg_player_level_per_match, player_level, max_creep_kills_per_match, avg_creep_kills_per_match, creep_kills, max_neutral_kills_per_match, avg_neutral_kills_per_match, neutral_kills, max_creep_damage_per_match, avg_creep_damage_per_match, creep_damage, max_player_damage_per_match, avg_player_damage_per_match, player_damage, max_neutral_damage_per_match, avg_neutral_damage_per_match, neutral_damage, max_boss_damage_per_match, avg_boss_damage_per_match, boss_damage, max_max_health_per_match, avg_max_health_per_match, max_health, max_shots_hit_per_match, avg_shots_hit_per_match, shots_hit, max_shots_missed_per_match, avg_shots_missed_per_match, shots_missed, max_hero_bullets_hit_per_match, avg_hero_bullets_hit_per_match, hero_bullets_hit, max_hero_bullets_hit_crit_per_match, avg_hero_bullets_hit_crit_per_match, hero_bullets_hit_crit] |
| **sortDirection** | **kotlin.String**| The direction to sort heroes in. | [optional] [enum: desc, asc] |
| **minMatches** | **kotlin.Int**| Filter by min number of matches played. | [optional] |
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1757030400L] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **minDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **maxDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **minNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **maxNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **minAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **maxAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **minMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **accountId** | **kotlin.Int**| Filter for matches with a specific player account ID. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**kotlin.collections.List&lt;Entry&gt;**](Entry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="heroStats"></a>
# **heroStats**
> kotlin.collections.List&lt;AnalyticsHeroStats&gt; heroStats(bucket, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, minHeroMatches, maxHeroMatches, includeItemIds, excludeItemIds, accountId, accountIds)

Hero Stats

 Retrieves performance statistics for each hero based on historical match data.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = AnalyticsApi()
val bucket : kotlin.String = bucket_example // kotlin.String | Bucket allows you to group the stats by a specific field.
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val maxDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val minNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val maxNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val minAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val maxAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val minHeroMatches : kotlin.Long = 789 // kotlin.Long | Filter players based on the number of matches they have played with a specific hero.
val maxHeroMatches : kotlin.Long = 789 // kotlin.Long | Filter players based on the number of matches they have played with a specific hero.
val includeItemIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of item ids to include (only heroes who have purchased these items). See more: <https://assets.deadlock-api.com/v2/items>
val excludeItemIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: <https://assets.deadlock-api.com/v2/items>
val accountId : kotlin.Int = 56 // kotlin.Int | Filter for matches with a specific player account ID.
val accountIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of account ids to include
try {
    val result : kotlin.collections.List<AnalyticsHeroStats> = apiInstance.heroStats(bucket, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, minHeroMatches, maxHeroMatches, includeItemIds, excludeItemIds, accountId, accountIds)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AnalyticsApi#heroStats")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AnalyticsApi#heroStats")
    e.printStackTrace()
}
```

### Parameters
| **bucket** | **kotlin.String**| Bucket allows you to group the stats by a specific field. | [optional] [enum: no_bucket, start_time_hour, start_time_day, start_time_week, start_time_month] |
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1757030400L] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **minDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **maxDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **minNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **maxNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **minAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **maxAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **minMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **minHeroMatches** | **kotlin.Long**| Filter players based on the number of matches they have played with a specific hero. | [optional] |
| **maxHeroMatches** | **kotlin.Long**| Filter players based on the number of matches they have played with a specific hero. | [optional] |
| **includeItemIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of item ids to include (only heroes who have purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] |
| **excludeItemIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] |
| **accountId** | **kotlin.Int**| Filter for matches with a specific player account ID. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**kotlin.collections.List&lt;AnalyticsHeroStats&gt;**](AnalyticsHeroStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="heroSynergiesStats"></a>
# **heroSynergiesStats**
> kotlin.collections.List&lt;HeroSynergyStats&gt; heroSynergiesStats(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, sameLaneFilter, samePartyFilter, minMatches, maxMatches, accountId, accountIds)

Hero Synergy Stats

 Retrieves hero pair synergy statistics based on historical match data.  This endpoint analyzes completed matches to calculate how often a specific pair of heroes (&#x60;hero_id1&#x60; and &#x60;hero_id2&#x60;) won when playing *together on the same team*, and the total number of times they have played together under the specified filter conditions.  Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = AnalyticsApi()
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val maxDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val minNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val maxNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val minAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val maxAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val sameLaneFilter : kotlin.Boolean = true // kotlin.Boolean | When `true`, only considers matchups where both `hero_id1` and `hero_id2` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane.
val samePartyFilter : kotlin.Boolean = true // kotlin.Boolean | When `true`, only considers matchups where both `hero_id` and `hero_id2` were on the same party. When `false`, considers all matchups regardless of party affiliation.
val minMatches : kotlin.Long = 789 // kotlin.Long | The minimum number of matches played for a hero combination to be included in the response.
val maxMatches : kotlin.Int = 56 // kotlin.Int | The maximum number of matches played for a hero combination to be included in the response.
val accountId : kotlin.Int = 56 // kotlin.Int | Filter for matches with a specific player account ID.
val accountIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of account ids to include
try {
    val result : kotlin.collections.List<HeroSynergyStats> = apiInstance.heroSynergiesStats(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, sameLaneFilter, samePartyFilter, minMatches, maxMatches, accountId, accountIds)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AnalyticsApi#heroSynergiesStats")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AnalyticsApi#heroSynergiesStats")
    e.printStackTrace()
}
```

### Parameters
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1757030400L] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **minDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **maxDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **minNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **maxNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **minAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **maxAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **minMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **sameLaneFilter** | **kotlin.Boolean**| When &#x60;true&#x60;, only considers matchups where both &#x60;hero_id1&#x60; and &#x60;hero_id2&#x60; were assigned to the same lane (e.g., both Mid Lane). When &#x60;false&#x60;, considers all matchups regardless of assigned lane. | [optional] [default to true] |
| **samePartyFilter** | **kotlin.Boolean**| When &#x60;true&#x60;, only considers matchups where both &#x60;hero_id&#x60; and &#x60;hero_id2&#x60; were on the same party. When &#x60;false&#x60;, considers all matchups regardless of party affiliation. | [optional] [default to true] |
| **minMatches** | **kotlin.Long**| The minimum number of matches played for a hero combination to be included in the response. | [optional] [default to 20L] |
| **maxMatches** | **kotlin.Int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] |
| **accountId** | **kotlin.Int**| Filter for matches with a specific player account ID. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**kotlin.collections.List&lt;HeroSynergyStats&gt;**](HeroSynergyStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="itemPermutationStats"></a>
# **itemPermutationStats**
> kotlin.collections.List&lt;ItemPermutationStats&gt; itemPermutationStats(itemIds, combSize, heroIds, heroId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, accountId, accountIds)

Item Permutation Stats

 Retrieves item permutation statistics based on historical match data.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = AnalyticsApi()
val itemIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of item ids. See more: <https://assets.deadlock-api.com/v2/items>
val combSize : kotlin.Int = 56 // kotlin.Int | The combination size to return.
val heroIds : kotlin.String = heroIds_example // kotlin.String | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes>
val heroId : kotlin.Int = 56 // kotlin.Int | Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val maxDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val minNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val maxNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val minAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val maxAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val accountId : kotlin.Int = 56 // kotlin.Int | Filter for matches with a specific player account ID.
val accountIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of account ids to include
try {
    val result : kotlin.collections.List<ItemPermutationStats> = apiInstance.itemPermutationStats(itemIds, combSize, heroIds, heroId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, accountId, accountIds)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AnalyticsApi#itemPermutationStats")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AnalyticsApi#itemPermutationStats")
    e.printStackTrace()
}
```

### Parameters
| **itemIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of item ids. See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] |
| **combSize** | **kotlin.Int**| The combination size to return. | [optional] [default to 2] |
| **heroIds** | **kotlin.String**| Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **heroId** | **kotlin.Int**| Filter matches based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1757030400L] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **minDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **maxDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **minNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **maxNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **minAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **maxAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **minMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **accountId** | **kotlin.Int**| Filter for matches with a specific player account ID. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**kotlin.collections.List&lt;ItemPermutationStats&gt;**](ItemPermutationStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="itemStats"></a>
# **itemStats**
> kotlin.collections.List&lt;ItemStats&gt; itemStats(bucket, heroIds, heroId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, includeItemIds, excludeItemIds, minMatches, maxMatches, accountId, accountIds)

Item Stats

 Retrieves item statistics based on historical match data.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = AnalyticsApi()
val bucket : kotlin.String = bucket_example // kotlin.String | Bucket allows you to group the stats by a specific field.
val heroIds : kotlin.String = heroIds_example // kotlin.String | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes>
val heroId : kotlin.Int = 56 // kotlin.Int | Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val maxDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val minNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val maxNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val minAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val maxAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val includeItemIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of item ids to include. See more: <https://assets.deadlock-api.com/v2/items>
val excludeItemIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of item ids to exclude. See more: <https://assets.deadlock-api.com/v2/items>
val minMatches : kotlin.Int = 56 // kotlin.Int | The minimum number of matches played for an item to be included in the response.
val maxMatches : kotlin.Int = 56 // kotlin.Int | The maximum number of matches played for a hero combination to be included in the response.
val accountId : kotlin.Int = 56 // kotlin.Int | Filter for matches with a specific player account ID.
val accountIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of account ids to include
try {
    val result : kotlin.collections.List<ItemStats> = apiInstance.itemStats(bucket, heroIds, heroId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, includeItemIds, excludeItemIds, minMatches, maxMatches, accountId, accountIds)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AnalyticsApi#itemStats")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AnalyticsApi#itemStats")
    e.printStackTrace()
}
```

### Parameters
| **bucket** | **kotlin.String**| Bucket allows you to group the stats by a specific field. | [optional] [enum: no_bucket, hero, team, start_time_hour, start_time_day, start_time_week, start_time_month, game_time_min, game_time_normalized_percentage, net_worth_by_1000, net_worth_by_2000, net_worth_by_3000, net_worth_by_5000, net_worth_by_10000] |
| **heroIds** | **kotlin.String**| Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **heroId** | **kotlin.Int**| Filter matches based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1757030400L] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **minDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **maxDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **minNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **maxNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **minAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **maxAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **minMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **includeItemIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of item ids to include. See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] |
| **excludeItemIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of item ids to exclude. See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] |
| **minMatches** | **kotlin.Int**| The minimum number of matches played for an item to be included in the response. | [optional] [default to 20] |
| **maxMatches** | **kotlin.Int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] |
| **accountId** | **kotlin.Int**| Filter for matches with a specific player account ID. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**kotlin.collections.List&lt;ItemStats&gt;**](ItemStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="playerScoreboard"></a>
# **playerScoreboard**
> kotlin.collections.List&lt;Entry&gt; playerScoreboard(sortBy, sortDirection, heroId, minMatches, maxMatches, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, start, limit, accountIds)

Player Scoreboard

 This endpoint returns the player scoreboard.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = AnalyticsApi()
val sortBy : kotlin.String = sortBy_example // kotlin.String | The field to sort by.
val sortDirection : kotlin.String = sortDirection_example // kotlin.String | The direction to sort players in.
val heroId : kotlin.Int = 56 // kotlin.Int | Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
val minMatches : kotlin.Int = 56 // kotlin.Int | The minimum number of matches played for a player to be included in the scoreboard.
val maxMatches : kotlin.Int = 56 // kotlin.Int | The maximum number of matches played for a hero combination to be included in the response.
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val maxDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val minNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val maxNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val minAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val maxAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val start : kotlin.Int = 56 // kotlin.Int | The offset to start fetching players from.
val limit : kotlin.Int = 56 // kotlin.Int | The maximum number of players to fetch.
val accountIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of account ids to include
try {
    val result : kotlin.collections.List<Entry> = apiInstance.playerScoreboard(sortBy, sortDirection, heroId, minMatches, maxMatches, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, start, limit, accountIds)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AnalyticsApi#playerScoreboard")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AnalyticsApi#playerScoreboard")
    e.printStackTrace()
}
```

### Parameters
| **sortBy** | **kotlin.String**| The field to sort by. | [enum: matches, wins, losses, winrate, max_kills_per_match, avg_kills_per_match, kills, max_deaths_per_match, avg_deaths_per_match, deaths, max_damage_taken_per_match, avg_damage_taken_per_match, damage_taken, max_assists_per_match, avg_assists_per_match, assists, max_net_worth_per_match, avg_net_worth_per_match, net_worth, max_last_hits_per_match, avg_last_hits_per_match, last_hits, max_denies_per_match, avg_denies_per_match, denies, max_player_level_per_match, avg_player_level_per_match, player_level, max_creep_kills_per_match, avg_creep_kills_per_match, creep_kills, max_neutral_kills_per_match, avg_neutral_kills_per_match, neutral_kills, max_creep_damage_per_match, avg_creep_damage_per_match, creep_damage, max_player_damage_per_match, avg_player_damage_per_match, player_damage, max_neutral_damage_per_match, avg_neutral_damage_per_match, neutral_damage, max_boss_damage_per_match, avg_boss_damage_per_match, boss_damage, max_max_health_per_match, avg_max_health_per_match, max_health, max_shots_hit_per_match, avg_shots_hit_per_match, shots_hit, max_shots_missed_per_match, avg_shots_missed_per_match, shots_missed, max_hero_bullets_hit_per_match, avg_hero_bullets_hit_per_match, hero_bullets_hit, max_hero_bullets_hit_crit_per_match, avg_hero_bullets_hit_crit_per_match, hero_bullets_hit_crit] |
| **sortDirection** | **kotlin.String**| The direction to sort players in. | [optional] [enum: desc, asc] |
| **heroId** | **kotlin.Int**| Filter matches based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **minMatches** | **kotlin.Int**| The minimum number of matches played for a player to be included in the scoreboard. | [optional] [default to 20] |
| **maxMatches** | **kotlin.Int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] |
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **minDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **maxDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **minNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **maxNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **minAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **maxAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **minMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **start** | **kotlin.Int**| The offset to start fetching players from. | [optional] |
| **limit** | **kotlin.Int**| The maximum number of players to fetch. | [optional] [default to 100] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**kotlin.collections.List&lt;Entry&gt;**](Entry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="playerStatsMetrics"></a>
# **playerStatsMetrics**
> kotlin.collections.Map&lt;kotlin.String, HashMapValue&gt; playerStatsMetrics(heroIds, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, maxMatches, includeItemIds, excludeItemIds, accountIds)

Player Stats Metrics

 Returns comprehensive statistical analysis of player performance.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  &gt; Note: Quantiles are calculated using the [DDSketch](https://www.vldb.org/pvldb/vol12/p2195-masson.pdf) algorithm, so they are not exact but have a maximum relative error of 0.01.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = AnalyticsApi()
val heroIds : kotlin.String = heroIds_example // kotlin.String | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes>
val minUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
val maxUnixTimestamp : kotlin.Long = 789 // kotlin.Long | Filter matches based on their start time (Unix timestamp).
val minDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val maxDurationS : kotlin.Long = 789 // kotlin.Long | Filter matches based on their duration in seconds (up to 7000s).
val minNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val maxNetworth : kotlin.Long = 789 // kotlin.Long | Filter players based on their net worth.
val minAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val maxAverageBadge : kotlin.Int = 56 // kotlin.Int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
val minMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatchId : kotlin.Long = 789 // kotlin.Long | Filter matches based on their ID.
val maxMatches : kotlin.Int = 56 // kotlin.Int | The maximum number of matches to analyze.
val includeItemIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of item ids to include (only heroes who have purchased these items). See more: <https://assets.deadlock-api.com/v2/items>
val excludeItemIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: <https://assets.deadlock-api.com/v2/items>
val accountIds : kotlin.collections.List<kotlin.Int> =  // kotlin.collections.List<kotlin.Int> | Comma separated list of account ids to include
try {
    val result : kotlin.collections.Map<kotlin.String, HashMapValue> = apiInstance.playerStatsMetrics(heroIds, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, maxMatches, includeItemIds, excludeItemIds, accountIds)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AnalyticsApi#playerStatsMetrics")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AnalyticsApi#playerStatsMetrics")
    e.printStackTrace()
}
```

### Parameters
| **heroIds** | **kotlin.String**| Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **minUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1757030400L] |
| **maxUnixTimestamp** | **kotlin.Long**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **minDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **maxDurationS** | **kotlin.Long**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **minNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **maxNetworth** | **kotlin.Long**| Filter players based on their net worth. | [optional] |
| **minAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **maxAverageBadge** | **kotlin.Int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **minMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **maxMatchId** | **kotlin.Long**| Filter matches based on their ID. | [optional] |
| **maxMatches** | **kotlin.Int**| The maximum number of matches to analyze. | [optional] |
| **includeItemIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of item ids to include (only heroes who have purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] |
| **excludeItemIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountIds** | [**kotlin.collections.List&lt;kotlin.Int&gt;**](kotlin.Int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**kotlin.collections.Map&lt;kotlin.String, HashMapValue&gt;**](HashMapValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

