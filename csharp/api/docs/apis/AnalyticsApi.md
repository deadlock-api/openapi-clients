# DeadlockApiClient.Api.AnalyticsApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**AbilityOrderStats**](AnalyticsApi.md#abilityorderstats) | **GET** /v1/analytics/ability-order-stats | Ability Order Stats |
| [**BadgeDistribution**](AnalyticsApi.md#badgedistribution) | **GET** /v1/analytics/badge-distribution | Badge Distribution |
| [**BuildItemStats**](AnalyticsApi.md#builditemstats) | **GET** /v1/analytics/build-item-stats | Build Item Stats |
| [**HeroCombStats**](AnalyticsApi.md#herocombstats) | **GET** /v1/analytics/hero-comb-stats | Hero Comb Stats |
| [**HeroCountersStats**](AnalyticsApi.md#herocountersstats) | **GET** /v1/analytics/hero-counter-stats | Hero Counter Stats |
| [**HeroScoreboard**](AnalyticsApi.md#heroscoreboard) | **GET** /v1/analytics/scoreboards/heroes | Hero Scoreboard |
| [**HeroStats**](AnalyticsApi.md#herostats) | **GET** /v1/analytics/hero-stats | Hero Stats |
| [**HeroSynergiesStats**](AnalyticsApi.md#herosynergiesstats) | **GET** /v1/analytics/hero-synergy-stats | Hero Synergy Stats |
| [**ItemPermutationStats**](AnalyticsApi.md#itempermutationstats) | **GET** /v1/analytics/item-permutation-stats | Item Permutation Stats |
| [**ItemStats**](AnalyticsApi.md#itemstats) | **GET** /v1/analytics/item-stats | Item Stats |
| [**KillDeathStats**](AnalyticsApi.md#killdeathstats) | **GET** /v1/analytics/kill-death-stats | Kill Death Stats |
| [**PlayerPerformanceCurve**](AnalyticsApi.md#playerperformancecurve) | **GET** /v1/analytics/player-performance-curve | Player Performance Curve |
| [**PlayerScoreboard**](AnalyticsApi.md#playerscoreboard) | **GET** /v1/analytics/scoreboards/players | Player Scoreboard |
| [**PlayerStatsMetrics**](AnalyticsApi.md#playerstatsmetrics) | **GET** /v1/analytics/player-stats/metrics | Player Stats Metrics |

<a id="abilityorderstats"></a>
# **AbilityOrderStats**
> List&lt;AnalyticsAbilityOrderStats&gt; AbilityOrderStats (int heroId, string gameMode = null, long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, long minAbilityUpgrades = null, long maxAbilityUpgrades = null, long minNetworth = null, long maxNetworth = null, int minAverageBadge = null, int maxAverageBadge = null, long minMatchId = null, long maxMatchId = null, int minMatches = null, int accountId = null, List<int> accountIds = null)

Ability Order Stats

 Retrieves statistics for the ability order of a hero.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **heroId** | **int** | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; |  |
| **gameMode** | **string** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional]  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1767139200] |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **minAbilityUpgrades** | **long** | Filter players based on their minimum number of ability upgrades over the whole match. | [optional]  |
| **maxAbilityUpgrades** | **long** | Filter players based on their maximum number of ability upgrades over the whole match. | [optional]  |
| **minNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **maxNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **minAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **maxAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **minMatches** | **int** | The minimum number of matches played for an ability order to be included in the response. | [optional] [default to 20] |
| **accountId** | **int** | Filter for matches with a specific player account ID. | [optional]  |
| **accountIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of account ids to include | [optional]  |

### Return type

[**List&lt;AnalyticsAbilityOrderStats&gt;**](AnalyticsAbilityOrderStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ability Order Stats |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch ability order stats |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="badgedistribution"></a>
# **BadgeDistribution**
> List&lt;BadgeDistribution&gt; BadgeDistribution (string gameMode = null, long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, bool isHighSkillRangeParties = null, bool isLowPriPool = null, bool isNewPlayerPool = null, long minMatchId = null, long maxMatchId = null)

Badge Distribution

 This endpoint returns the player badge distribution.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **gameMode** | **string** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional]  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1767139200] |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **isHighSkillRangeParties** | **bool** | Filter matches based on whether they are in the high skill range. | [optional]  |
| **isLowPriPool** | **bool** | Filter matches based on whether they are in the low priority pool. | [optional]  |
| **isNewPlayerPool** | **bool** | Filter matches based on whether they are in the new player pool. | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |

### Return type

[**List&lt;BadgeDistribution&gt;**](BadgeDistribution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Badge Distribution |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch badge distribution |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="builditemstats"></a>
# **BuildItemStats**
> List&lt;BuildItemStats&gt; BuildItemStats (int heroId = null, long minLastUpdatedUnixTimestamp = null, long maxLastUpdatedUnixTimestamp = null)

Build Item Stats

 Retrieves item statistics from hero builds.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **heroId** | **int** | Filter builds based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional]  |
| **minLastUpdatedUnixTimestamp** | **long** | Filter builds based on their last updated time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1767139200] |
| **maxLastUpdatedUnixTimestamp** | **long** | Filter builds based on their last updated time (Unix timestamp). | [optional]  |

### Return type

[**List&lt;BuildItemStats&gt;**](BuildItemStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Build Item Stats |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch build item stats |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="herocombstats"></a>
# **HeroCombStats**
> List&lt;HeroCombStats&gt; HeroCombStats (string gameMode = null, long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, long minNetworth = null, long maxNetworth = null, int minAverageBadge = null, int maxAverageBadge = null, long minMatchId = null, long maxMatchId = null, List<int> includeHeroIds = null, List<int> excludeHeroIds = null, int minMatches = null, int maxMatches = null, int combSize = null, int accountId = null, List<int> accountIds = null)

Hero Comb Stats

 Retrieves overall statistics for each hero combination.  Results are cached for **1 hour**. The cache key is determined by the specific combination of filter parameters used in the query. Subsequent requests using the exact same filters within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **gameMode** | **string** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional]  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1767139200] |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **minNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **maxNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **minAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **maxAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **includeHeroIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of hero ids to include. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional]  |
| **excludeHeroIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of hero ids to exclude. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional]  |
| **minMatches** | **int** | The minimum number of matches played for a hero combination to be included in the response. | [optional] [default to 20] |
| **maxMatches** | **int** | The maximum number of matches played for a hero combination to be included in the response. | [optional]  |
| **combSize** | **int** | The combination size to return. | [optional] [default to 6] |
| **accountId** | **int** | Filter for matches with a specific player account ID. | [optional]  |
| **accountIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of account ids to include | [optional]  |

### Return type

[**List&lt;HeroCombStats&gt;**](HeroCombStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Hero Comb Stats |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch hero comb stats |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="herocountersstats"></a>
# **HeroCountersStats**
> List&lt;HeroCounterStats&gt; HeroCountersStats (string gameMode = null, long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, long minNetworth = null, long maxNetworth = null, long minEnemyNetworth = null, long maxEnemyNetworth = null, int minAverageBadge = null, int maxAverageBadge = null, long minMatchId = null, long maxMatchId = null, bool sameLaneFilter = null, long minMatches = null, int maxMatches = null, int accountId = null, List<int> accountIds = null)

Hero Counter Stats

 Retrieves hero-versus-hero matchup statistics based on historical match data.  This endpoint analyzes completed matches to calculate how often a specific hero (`hero_id`) wins against an enemy hero (`enemy_hero_id`) and the total number of times they have faced each other under the specified filter conditions.  Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **gameMode** | **string** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional]  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1767139200] |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **minNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **maxNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **minEnemyNetworth** | **long** | Filter enemy players based on their net worth. | [optional]  |
| **maxEnemyNetworth** | **long** | Filter enemy players based on their net worth. | [optional]  |
| **minAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **maxAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **sameLaneFilter** | **bool** | When &#x60;true&#x60;, only considers matchups where both &#x60;hero_id&#x60; and &#x60;enemy_hero_id&#x60; were assigned to the same lane (e.g., both Mid Lane). When &#x60;false&#x60;, considers all matchups regardless of assigned lane. | [optional] [default to true] |
| **minMatches** | **long** | The minimum number of matches played for a hero combination to be included in the response. | [optional] [default to 20] |
| **maxMatches** | **int** | The maximum number of matches played for a hero combination to be included in the response. | [optional]  |
| **accountId** | **int** | Filter for matches with a specific player account ID. | [optional]  |
| **accountIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of account ids to include | [optional]  |

### Return type

[**List&lt;HeroCounterStats&gt;**](HeroCounterStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Hero Counter Stats |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch hero counter stats |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="heroscoreboard"></a>
# **HeroScoreboard**
> List&lt;Entry&gt; HeroScoreboard (string sortBy, string sortDirection = null, string gameMode = null, int minMatches = null, long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, long minNetworth = null, long maxNetworth = null, int minAverageBadge = null, int maxAverageBadge = null, long minMatchId = null, long maxMatchId = null, int accountId = null, List<int> accountIds = null)

Hero Scoreboard

 This endpoint returns the hero scoreboard.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **sortBy** | **string** | The field to sort by. |  |
| **sortDirection** | **string** | The direction to sort heroes in. | [optional]  |
| **gameMode** | **string** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional]  |
| **minMatches** | **int** | Filter by min number of matches played. | [optional]  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1767139200] |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **minNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **maxNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **minAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **maxAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **accountId** | **int** | Filter for matches with a specific player account ID. | [optional]  |
| **accountIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of account ids to include | [optional]  |

### Return type

[**List&lt;Entry&gt;**](Entry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Hero Scoreboard |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch hero scoreboard |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="herostats"></a>
# **HeroStats**
> List&lt;AnalyticsHeroStats&gt; HeroStats (string bucket = null, string gameMode = null, long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, long minNetworth = null, long maxNetworth = null, int minAverageBadge = null, int maxAverageBadge = null, long minMatchId = null, long maxMatchId = null, long minHeroMatches = null, long maxHeroMatches = null, long minHeroMatchesTotal = null, long maxHeroMatchesTotal = null, List<int> includeItemIds = null, List<int> excludeItemIds = null, int accountId = null, List<int> accountIds = null)

Hero Stats

 Retrieves performance statistics for each hero based on historical match data.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **bucket** | **string** | Bucket allows you to group the stats by a specific field. | [optional]  |
| **gameMode** | **string** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional]  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1767139200] |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **minNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **maxNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **minAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **maxAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **minHeroMatches** | **long** | Filter players based on the number of matches they have played with a specific hero within the filtered time range. | [optional]  |
| **maxHeroMatches** | **long** | Filter players based on the number of matches they have played with a specific hero within the filtered time range. | [optional]  |
| **minHeroMatchesTotal** | **long** | Filter players based on the number of matches they have played with a specific hero in their entire history. | [optional]  |
| **maxHeroMatchesTotal** | **long** | Filter players based on the number of matches they have played with a specific hero in their entire history. | [optional]  |
| **includeItemIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of item ids to include (only players who have purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional]  |
| **excludeItemIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of item ids to exclude (only players who have not purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional]  |
| **accountId** | **int** | Filter for matches with a specific player account ID. | [optional]  |
| **accountIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of account ids to include | [optional]  |

### Return type

[**List&lt;AnalyticsHeroStats&gt;**](AnalyticsHeroStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Hero Stats |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch hero stats |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="herosynergiesstats"></a>
# **HeroSynergiesStats**
> List&lt;HeroSynergyStats&gt; HeroSynergiesStats (string gameMode = null, long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, long minNetworth = null, long maxNetworth = null, int minAverageBadge = null, int maxAverageBadge = null, long minMatchId = null, long maxMatchId = null, bool sameLaneFilter = null, bool samePartyFilter = null, long minMatches = null, int maxMatches = null, int accountId = null, List<int> accountIds = null)

Hero Synergy Stats

 Retrieves hero pair synergy statistics based on historical match data.  This endpoint analyzes completed matches to calculate how often a specific pair of heroes (`hero_id1` and `hero_id2`) won when playing *together on the same team*, and the total number of times they have played together under the specified filter conditions.  Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **gameMode** | **string** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional]  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1767139200] |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **minNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **maxNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **minAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **maxAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **sameLaneFilter** | **bool** | When &#x60;true&#x60;, only considers matchups where both &#x60;hero_id1&#x60; and &#x60;hero_id2&#x60; were assigned to the same lane (e.g., both Mid Lane). When &#x60;false&#x60;, considers all matchups regardless of assigned lane. | [optional] [default to true] |
| **samePartyFilter** | **bool** | When &#x60;true&#x60;, only considers matchups where both &#x60;hero_id&#x60; and &#x60;hero_id2&#x60; were on the same party. When &#x60;false&#x60;, considers all matchups regardless of party affiliation. | [optional] [default to true] |
| **minMatches** | **long** | The minimum number of matches played for a hero combination to be included in the response. | [optional] [default to 20] |
| **maxMatches** | **int** | The maximum number of matches played for a hero combination to be included in the response. | [optional]  |
| **accountId** | **int** | Filter for matches with a specific player account ID. | [optional]  |
| **accountIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of account ids to include | [optional]  |

### Return type

[**List&lt;HeroSynergyStats&gt;**](HeroSynergyStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Hero Synergy Stats |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch hero synergy stats |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="itempermutationstats"></a>
# **ItemPermutationStats**
> List&lt;ItemPermutationStats&gt; ItemPermutationStats (List<int> itemIds = null, int combSize = null, string gameMode = null, string heroIds = null, int heroId = null, long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, long minNetworth = null, long maxNetworth = null, int minAverageBadge = null, int maxAverageBadge = null, long minMatchId = null, long maxMatchId = null, int accountId = null, List<int> accountIds = null)

Item Permutation Stats

 Retrieves item permutation statistics based on historical match data.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **itemIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of item ids. See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional]  |
| **combSize** | **int** | The combination size to return. | [optional] [default to 2] |
| **gameMode** | **string** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional]  |
| **heroIds** | **string** | Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional]  |
| **heroId** | **int** | Filter matches based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional]  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1767139200] |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **minNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **maxNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **minAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **maxAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **accountId** | **int** | Filter for matches with a specific player account ID. | [optional]  |
| **accountIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of account ids to include | [optional]  |

### Return type

[**List&lt;ItemPermutationStats&gt;**](ItemPermutationStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Item Stats |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch item stats |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="itemstats"></a>
# **ItemStats**
> List&lt;ItemStats&gt; ItemStats (string bucket = null, string gameMode = null, string heroIds = null, int heroId = null, long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, long minNetworth = null, long maxNetworth = null, int minAverageBadge = null, int maxAverageBadge = null, long minMatchId = null, long maxMatchId = null, List<int> includeItemIds = null, List<int> excludeItemIds = null, int minMatches = null, int maxMatches = null, int accountId = null, List<int> accountIds = null, int minBoughtAtS = null, int maxBoughtAtS = null)

Item Stats

 Retrieves item statistics based on historical match data.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **bucket** | **string** | Bucket allows you to group the stats by a specific field. | [optional]  |
| **gameMode** | **string** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional]  |
| **heroIds** | **string** | Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional]  |
| **heroId** | **int** | Filter matches based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional]  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1767139200] |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **minNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **maxNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **minAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **maxAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **includeItemIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of item ids to include. See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional]  |
| **excludeItemIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of item ids to exclude. See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional]  |
| **minMatches** | **int** | The minimum number of matches played for an item to be included in the response. | [optional] [default to 20] |
| **maxMatches** | **int** | The maximum number of matches played for a hero combination to be included in the response. | [optional]  |
| **accountId** | **int** | Filter for matches with a specific player account ID. | [optional]  |
| **accountIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of account ids to include | [optional]  |
| **minBoughtAtS** | **int** | Filter items bought after this game time (seconds). | [optional]  |
| **maxBoughtAtS** | **int** | Filter items bought before this game time (seconds). | [optional]  |

### Return type

[**List&lt;ItemStats&gt;**](ItemStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Item Stats |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch item stats |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="killdeathstats"></a>
# **KillDeathStats**
> List&lt;KillDeathStats&gt; KillDeathStats (int team = null, string gameMode = null, long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, List<int> accountIds = null, string heroIds = null, long minNetworth = null, long maxNetworth = null, bool isHighSkillRangeParties = null, bool isLowPriPool = null, bool isNewPlayerPool = null, long minMatchId = null, long maxMatchId = null, int minAverageBadge = null, int maxAverageBadge = null, int minKillsPerRaster = null, int maxKillsPerRaster = null, int minDeathsPerRaster = null, int maxDeathsPerRaster = null, int minGameTimeS = null, int maxGameTimeS = null)

Kill Death Stats

 This endpoint returns the kill-death statistics across a 100x100 pixel raster.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **team** | **int** | Filter by team number. | [optional]  |
| **gameMode** | **string** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional]  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1767139200] |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **accountIds** | [**List&lt;int&gt;**](int.md) | Filter matches by account IDs of players that participated in the match. | [optional]  |
| **heroIds** | **string** | Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional]  |
| **minNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **maxNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **isHighSkillRangeParties** | **bool** | Filter matches based on whether they are in the high skill range. | [optional]  |
| **isLowPriPool** | **bool** | Filter matches based on whether they are in the low priority pool. | [optional]  |
| **isNewPlayerPool** | **bool** | Filter matches based on whether they are in the new player pool. | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **minAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **maxAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **minKillsPerRaster** | **int** | Filter Raster cells based on minimum kills. | [optional]  |
| **maxKillsPerRaster** | **int** | Filter Raster cells based on maximum kills. | [optional]  |
| **minDeathsPerRaster** | **int** | Filter Raster cells based on minimum deaths. | [optional]  |
| **maxDeathsPerRaster** | **int** | Filter Raster cells based on maximum deaths. | [optional]  |
| **minGameTimeS** | **int** | Filter kills based on their game time. | [optional]  |
| **maxGameTimeS** | **int** | Filter kills based on their game time. | [optional]  |

### Return type

[**List&lt;KillDeathStats&gt;**](KillDeathStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Kill Death Stats |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch kill death stats |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="playerperformancecurve"></a>
# **PlayerPerformanceCurve**
> List&lt;PlayerPerformanceCurvePoint&gt; PlayerPerformanceCurve (int resolution = null, string gameMode = null, long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, long minNetworth = null, long maxNetworth = null, int minAverageBadge = null, int maxAverageBadge = null, long minMatchId = null, long maxMatchId = null, string heroIds = null, List<int> includeItemIds = null, List<int> excludeItemIds = null, List<int> accountIds = null)

Player Performance Curve

 Retrieves player performance statistics (net worth, kills, deaths, assists) over time throughout matches.  Results are cached for **1 hour** based on the unique combination of query parameters provided.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **resolution** | **int** | Resolution for relative game times in percent (0-100). **Default:** 10 (buckets of 10%). Set to **0** to use absolute game time (seconds). | [optional] [default to 10] |
| **gameMode** | **string** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional]  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1767139200] |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **minNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **maxNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **minAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **maxAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **heroIds** | **string** | Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional]  |
| **includeItemIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of item ids to include (only players who have purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional]  |
| **excludeItemIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of item ids to exclude (only players who have not purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional]  |
| **accountIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of account ids to include | [optional]  |

### Return type

[**List&lt;PlayerPerformanceCurvePoint&gt;**](PlayerPerformanceCurvePoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Player Performance Curve |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch player performance curve |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="playerscoreboard"></a>
# **PlayerScoreboard**
> List&lt;Entry&gt; PlayerScoreboard (string sortBy, string sortDirection = null, string gameMode = null, int heroId = null, int minMatches = null, int maxMatches = null, long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, long minNetworth = null, long maxNetworth = null, int minAverageBadge = null, int maxAverageBadge = null, long minMatchId = null, long maxMatchId = null, int start = null, int limit = null, List<int> accountIds = null)

Player Scoreboard

 This endpoint returns the player scoreboard.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **sortBy** | **string** | The field to sort by. |  |
| **sortDirection** | **string** | The direction to sort players in. | [optional]  |
| **gameMode** | **string** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional]  |
| **heroId** | **int** | Filter matches based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional]  |
| **minMatches** | **int** | The minimum number of matches played for a player to be included in the scoreboard. | [optional] [default to 20] |
| **maxMatches** | **int** | The maximum number of matches played for a hero combination to be included in the response. | [optional]  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **minNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **maxNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **minAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **maxAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **start** | **int** | The offset to start fetching players from. | [optional]  |
| **limit** | **int** | The maximum number of players to fetch. | [optional] [default to 100] |
| **accountIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of account ids to include | [optional]  |

### Return type

[**List&lt;Entry&gt;**](Entry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Player Scoreboard |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch player scoreboard |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="playerstatsmetrics"></a>
# **PlayerStatsMetrics**
> Dictionary&lt;string, HashMapValue&gt; PlayerStatsMetrics (string heroIds = null, string gameMode = null, long minUnixTimestamp = null, long maxUnixTimestamp = null, long minDurationS = null, long maxDurationS = null, long minNetworth = null, long maxNetworth = null, int minAverageBadge = null, int maxAverageBadge = null, long minMatchId = null, long maxMatchId = null, int maxMatches = null, List<int> includeItemIds = null, List<int> excludeItemIds = null, List<int> accountIds = null)

Player Stats Metrics

 Returns comprehensive statistical analysis of player performance.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  > Note: Quantiles are calculated using the [DDSketch](https://www.vldb.org/pvldb/vol12/p2195-masson.pdf) algorithm, so they are not exact but have a maximum relative error of 0.01.  ### Rate Limits: | Type | Limit | | - -- - | - -- -- | | IP | 100req/s | | Key | - | | Global | - |     


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **heroIds** | **string** | Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional]  |
| **gameMode** | **string** | Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional]  |
| **minUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1767139200] |
| **maxUnixTimestamp** | **long** | Filter matches based on their start time (Unix timestamp). | [optional]  |
| **minDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **maxDurationS** | **long** | Filter matches based on their duration in seconds (up to 7000s). | [optional]  |
| **minNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **maxNetworth** | **long** | Filter players based on their final net worth. | [optional]  |
| **minAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **maxAverageBadge** | **int** | Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]  |
| **minMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatchId** | **long** | Filter matches based on their ID. | [optional]  |
| **maxMatches** | **int** | The maximum number of matches to analyze. | [optional]  |
| **includeItemIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of item ids to include (only players who have purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional]  |
| **excludeItemIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of item ids to exclude (only players who have not purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional]  |
| **accountIds** | [**List&lt;int&gt;**](int.md) | Comma separated list of account ids to include | [optional]  |

### Return type

[**Dictionary&lt;string, HashMapValue&gt;**](HashMapValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Hero Stats |  -  |
| **400** | Provided parameters are invalid. |  -  |
| **500** | Failed to fetch player stats metrics |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

