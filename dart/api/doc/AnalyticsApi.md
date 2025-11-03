# deadlock-api-client.api.AnalyticsApi

## Load the API package
```dart
import 'package:deadlock-api-client/api.dart';
```

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abilityOrderStats**](AnalyticsApi.md#abilityorderstats) | **GET** /v1/analytics/ability-order-stats | Ability Order Stats
[**badgeDistribution**](AnalyticsApi.md#badgedistribution) | **GET** /v1/analytics/badge-distribution | Badge Distribution
[**buildItemStats**](AnalyticsApi.md#builditemstats) | **GET** /v1/analytics/build-item-stats | Build Item Stats
[**heroCombStats**](AnalyticsApi.md#herocombstats) | **GET** /v1/analytics/hero-comb-stats | Hero Comb Stats
[**heroCountersStats**](AnalyticsApi.md#herocountersstats) | **GET** /v1/analytics/hero-counter-stats | Hero Counter Stats
[**heroScoreboard**](AnalyticsApi.md#heroscoreboard) | **GET** /v1/analytics/scoreboards/heroes | Hero Scoreboard
[**heroStats**](AnalyticsApi.md#herostats) | **GET** /v1/analytics/hero-stats | Hero Stats
[**heroSynergiesStats**](AnalyticsApi.md#herosynergiesstats) | **GET** /v1/analytics/hero-synergy-stats | Hero Synergy Stats
[**itemPermutationStats**](AnalyticsApi.md#itempermutationstats) | **GET** /v1/analytics/item-permutation-stats | Item Permutation Stats
[**itemStats**](AnalyticsApi.md#itemstats) | **GET** /v1/analytics/item-stats | Item Stats
[**playerScoreboard**](AnalyticsApi.md#playerscoreboard) | **GET** /v1/analytics/scoreboards/players | Player Scoreboard
[**playerStatsMetrics**](AnalyticsApi.md#playerstatsmetrics) | **GET** /v1/analytics/player-stats/metrics | Player Stats Metrics


# **abilityOrderStats**
> List<AnalyticsAbilityOrderStats> abilityOrderStats(heroId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minAbilityUpgrades, maxAbilityUpgrades, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, minMatches, accountId, accountIds)

Ability Order Stats

 Retrieves statistics for the ability order of a hero.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = AnalyticsApi();
final heroId = 56; // int | See more: <https://assets.deadlock-api.com/v2/heroes>
final minUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
final maxUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final minDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final maxDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final minAbilityUpgrades = 789; // int | Filter players based on their minimum number of ability upgrades over the whole match.
final maxAbilityUpgrades = 789; // int | Filter players based on their maximum number of ability upgrades over the whole match.
final minNetworth = 789; // int | Filter players based on their net worth.
final maxNetworth = 789; // int | Filter players based on their net worth.
final minAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final maxAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final minMatchId = 789; // int | Filter matches based on their ID.
final maxMatchId = 789; // int | Filter matches based on their ID.
final minMatches = 56; // int | The minimum number of matches played for an ability order to be included in the response.
final accountId = 56; // int | Filter for matches with a specific player account ID.
final accountIds = []; // List<int> | Comma separated list of account ids to include

try {
    final result = api_instance.abilityOrderStats(heroId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minAbilityUpgrades, maxAbilityUpgrades, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, minMatches, accountId, accountIds);
    print(result);
} catch (e) {
    print('Exception when calling AnalyticsApi->abilityOrderStats: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heroId** | **int**| See more: <https://assets.deadlock-api.com/v2/heroes> | 
 **minUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1759449600]
 **maxUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **minDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **maxDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **minAbilityUpgrades** | **int**| Filter players based on their minimum number of ability upgrades over the whole match. | [optional] 
 **maxAbilityUpgrades** | **int**| Filter players based on their maximum number of ability upgrades over the whole match. | [optional] 
 **minNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **maxNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **minAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **maxAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **minMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **minMatches** | **int**| The minimum number of matches played for an ability order to be included in the response. | [optional] [default to 20]
 **accountId** | **int**| Filter for matches with a specific player account ID. | [optional] 
 **accountIds** | [**List<int>**](int.md)| Comma separated list of account ids to include | [optional] [default to const []]

### Return type

[**List<AnalyticsAbilityOrderStats>**](AnalyticsAbilityOrderStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **badgeDistribution**
> List<BadgeDistribution> badgeDistribution(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, minMatchId, maxMatchId)

Badge Distribution

 This endpoint returns the player badge distribution.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = AnalyticsApi();
final minUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
final maxUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final minDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final maxDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final isHighSkillRangeParties = true; // bool | Filter matches based on whether they are in the high skill range.
final isLowPriPool = true; // bool | Filter matches based on whether they are in the low priority pool.
final isNewPlayerPool = true; // bool | Filter matches based on whether they are in the new player pool.
final minMatchId = 789; // int | Filter matches based on their ID.
final maxMatchId = 789; // int | Filter matches based on their ID.

try {
    final result = api_instance.badgeDistribution(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, isHighSkillRangeParties, isLowPriPool, isNewPlayerPool, minMatchId, maxMatchId);
    print(result);
} catch (e) {
    print('Exception when calling AnalyticsApi->badgeDistribution: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1759449600]
 **maxUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **minDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **maxDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **isHighSkillRangeParties** | **bool**| Filter matches based on whether they are in the high skill range. | [optional] 
 **isLowPriPool** | **bool**| Filter matches based on whether they are in the low priority pool. | [optional] 
 **isNewPlayerPool** | **bool**| Filter matches based on whether they are in the new player pool. | [optional] 
 **minMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 

### Return type

[**List<BadgeDistribution>**](BadgeDistribution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buildItemStats**
> List<BuildItemStats> buildItemStats(heroId, minLastUpdatedUnixTimestamp, maxLastUpdatedUnixTimestamp)

Build Item Stats

 Retrieves item statistics from hero builds.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = AnalyticsApi();
final heroId = 56; // int | Filter builds based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
final minLastUpdatedUnixTimestamp = 789; // int | Filter builds based on their last updated time (Unix timestamp). **Default:** 30 days ago.
final maxLastUpdatedUnixTimestamp = 789; // int | Filter builds based on their last updated time (Unix timestamp).

try {
    final result = api_instance.buildItemStats(heroId, minLastUpdatedUnixTimestamp, maxLastUpdatedUnixTimestamp);
    print(result);
} catch (e) {
    print('Exception when calling AnalyticsApi->buildItemStats: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heroId** | **int**| Filter builds based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> | [optional] 
 **minLastUpdatedUnixTimestamp** | **int**| Filter builds based on their last updated time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1759449600]
 **maxLastUpdatedUnixTimestamp** | **int**| Filter builds based on their last updated time (Unix timestamp). | [optional] 

### Return type

[**List<BuildItemStats>**](BuildItemStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroCombStats**
> List<HeroCombStats> heroCombStats(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, includeHeroIds, excludeHeroIds, minMatches, maxMatches, combSize, accountId, accountIds)

Hero Comb Stats

 Retrieves overall statistics for each hero combination.  Results are cached for **1 hour**. The cache key is determined by the specific combination of filter parameters used in the query. Subsequent requests using the exact same filters within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = AnalyticsApi();
final minUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
final maxUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final minDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final maxDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final minNetworth = 789; // int | Filter players based on their net worth.
final maxNetworth = 789; // int | Filter players based on their net worth.
final minAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final maxAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final minMatchId = 789; // int | Filter matches based on their ID.
final maxMatchId = 789; // int | Filter matches based on their ID.
final includeHeroIds = []; // List<int> | Comma separated list of hero ids to include. See more: <https://assets.deadlock-api.com/v2/heroes>
final excludeHeroIds = []; // List<int> | Comma separated list of hero ids to exclude. See more: <https://assets.deadlock-api.com/v2/heroes>
final minMatches = 56; // int | The minimum number of matches played for a hero combination to be included in the response.
final maxMatches = 56; // int | The maximum number of matches played for a hero combination to be included in the response.
final combSize = 56; // int | The combination size to return.
final accountId = 56; // int | Filter for matches with a specific player account ID.
final accountIds = []; // List<int> | Comma separated list of account ids to include

try {
    final result = api_instance.heroCombStats(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, includeHeroIds, excludeHeroIds, minMatches, maxMatches, combSize, accountId, accountIds);
    print(result);
} catch (e) {
    print('Exception when calling AnalyticsApi->heroCombStats: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1759449600]
 **maxUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **minDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **maxDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **minNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **maxNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **minAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **maxAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **minMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **includeHeroIds** | [**List<int>**](int.md)| Comma separated list of hero ids to include. See more: <https://assets.deadlock-api.com/v2/heroes> | [optional] [default to const []]
 **excludeHeroIds** | [**List<int>**](int.md)| Comma separated list of hero ids to exclude. See more: <https://assets.deadlock-api.com/v2/heroes> | [optional] [default to const []]
 **minMatches** | **int**| The minimum number of matches played for a hero combination to be included in the response. | [optional] [default to 20]
 **maxMatches** | **int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] 
 **combSize** | **int**| The combination size to return. | [optional] [default to 6]
 **accountId** | **int**| Filter for matches with a specific player account ID. | [optional] 
 **accountIds** | [**List<int>**](int.md)| Comma separated list of account ids to include | [optional] [default to const []]

### Return type

[**List<HeroCombStats>**](HeroCombStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroCountersStats**
> List<HeroCounterStats> heroCountersStats(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minEnemyNetworth, maxEnemyNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, sameLaneFilter, minMatches, maxMatches, accountId, accountIds)

Hero Counter Stats

 Retrieves hero-versus-hero matchup statistics based on historical match data.  This endpoint analyzes completed matches to calculate how often a specific hero (`hero_id`) wins against an enemy hero (`enemy_hero_id`) and the total number of times they have faced each other under the specified filter conditions.  Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = AnalyticsApi();
final minUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
final maxUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final minDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final maxDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final minNetworth = 789; // int | Filter players based on their net worth.
final maxNetworth = 789; // int | Filter players based on their net worth.
final minEnemyNetworth = 789; // int | Filter enemy players based on their net worth.
final maxEnemyNetworth = 789; // int | Filter enemy players based on their net worth.
final minAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final maxAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final minMatchId = 789; // int | Filter matches based on their ID.
final maxMatchId = 789; // int | Filter matches based on their ID.
final sameLaneFilter = true; // bool | When `true`, only considers matchups where both `hero_id` and `enemy_hero_id` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane.
final minMatches = 789; // int | The minimum number of matches played for a hero combination to be included in the response.
final maxMatches = 56; // int | The maximum number of matches played for a hero combination to be included in the response.
final accountId = 56; // int | Filter for matches with a specific player account ID.
final accountIds = []; // List<int> | Comma separated list of account ids to include

try {
    final result = api_instance.heroCountersStats(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minEnemyNetworth, maxEnemyNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, sameLaneFilter, minMatches, maxMatches, accountId, accountIds);
    print(result);
} catch (e) {
    print('Exception when calling AnalyticsApi->heroCountersStats: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1759449600]
 **maxUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **minDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **maxDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **minNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **maxNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **minEnemyNetworth** | **int**| Filter enemy players based on their net worth. | [optional] 
 **maxEnemyNetworth** | **int**| Filter enemy players based on their net worth. | [optional] 
 **minAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **maxAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **minMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **sameLaneFilter** | **bool**| When `true`, only considers matchups where both `hero_id` and `enemy_hero_id` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane. | [optional] [default to true]
 **minMatches** | **int**| The minimum number of matches played for a hero combination to be included in the response. | [optional] [default to 20]
 **maxMatches** | **int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] 
 **accountId** | **int**| Filter for matches with a specific player account ID. | [optional] 
 **accountIds** | [**List<int>**](int.md)| Comma separated list of account ids to include | [optional] [default to const []]

### Return type

[**List<HeroCounterStats>**](HeroCounterStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroScoreboard**
> List<Entry> heroScoreboard(sortBy, sortDirection, minMatches, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, accountId, accountIds)

Hero Scoreboard

 This endpoint returns the hero scoreboard.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = AnalyticsApi();
final sortBy = sortBy_example; // String | The field to sort by.
final sortDirection = sortDirection_example; // String | The direction to sort heroes in.
final minMatches = 56; // int | Filter by min number of matches played.
final minUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
final maxUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final minDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final maxDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final minNetworth = 789; // int | Filter players based on their net worth.
final maxNetworth = 789; // int | Filter players based on their net worth.
final minAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final maxAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final minMatchId = 789; // int | Filter matches based on their ID.
final maxMatchId = 789; // int | Filter matches based on their ID.
final accountId = 56; // int | Filter for matches with a specific player account ID.
final accountIds = []; // List<int> | Comma separated list of account ids to include

try {
    final result = api_instance.heroScoreboard(sortBy, sortDirection, minMatches, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, accountId, accountIds);
    print(result);
} catch (e) {
    print('Exception when calling AnalyticsApi->heroScoreboard: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortBy** | **String**| The field to sort by. | 
 **sortDirection** | **String**| The direction to sort heroes in. | [optional] 
 **minMatches** | **int**| Filter by min number of matches played. | [optional] 
 **minUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1759449600]
 **maxUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **minDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **maxDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **minNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **maxNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **minAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **maxAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **minMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **accountId** | **int**| Filter for matches with a specific player account ID. | [optional] 
 **accountIds** | [**List<int>**](int.md)| Comma separated list of account ids to include | [optional] [default to const []]

### Return type

[**List<Entry>**](Entry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroStats**
> List<AnalyticsHeroStats> heroStats(bucket, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, minHeroMatches, maxHeroMatches, minHeroMatchesTotal, maxHeroMatchesTotal, includeItemIds, excludeItemIds, accountId, accountIds)

Hero Stats

 Retrieves performance statistics for each hero based on historical match data.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = AnalyticsApi();
final bucket = bucket_example; // String | Bucket allows you to group the stats by a specific field.
final minUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
final maxUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final minDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final maxDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final minNetworth = 789; // int | Filter players based on their net worth.
final maxNetworth = 789; // int | Filter players based on their net worth.
final minAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final maxAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final minMatchId = 789; // int | Filter matches based on their ID.
final maxMatchId = 789; // int | Filter matches based on their ID.
final minHeroMatches = 789; // int | Filter players based on the number of matches they have played with a specific hero within the filtered time range.
final maxHeroMatches = 789; // int | Filter players based on the number of matches they have played with a specific hero within the filtered time range.
final minHeroMatchesTotal = 789; // int | Filter players based on the number of matches they have played with a specific hero in their entire history.
final maxHeroMatchesTotal = 789; // int | Filter players based on the number of matches they have played with a specific hero in their entire history.
final includeItemIds = []; // List<int> | Comma separated list of item ids to include (only heroes who have purchased these items). See more: <https://assets.deadlock-api.com/v2/items>
final excludeItemIds = []; // List<int> | Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: <https://assets.deadlock-api.com/v2/items>
final accountId = 56; // int | Filter for matches with a specific player account ID.
final accountIds = []; // List<int> | Comma separated list of account ids to include

try {
    final result = api_instance.heroStats(bucket, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, minHeroMatches, maxHeroMatches, minHeroMatchesTotal, maxHeroMatchesTotal, includeItemIds, excludeItemIds, accountId, accountIds);
    print(result);
} catch (e) {
    print('Exception when calling AnalyticsApi->heroStats: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **String**| Bucket allows you to group the stats by a specific field. | [optional] 
 **minUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1759449600]
 **maxUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **minDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **maxDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **minNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **maxNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **minAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **maxAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **minMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **minHeroMatches** | **int**| Filter players based on the number of matches they have played with a specific hero within the filtered time range. | [optional] 
 **maxHeroMatches** | **int**| Filter players based on the number of matches they have played with a specific hero within the filtered time range. | [optional] 
 **minHeroMatchesTotal** | **int**| Filter players based on the number of matches they have played with a specific hero in their entire history. | [optional] 
 **maxHeroMatchesTotal** | **int**| Filter players based on the number of matches they have played with a specific hero in their entire history. | [optional] 
 **includeItemIds** | [**List<int>**](int.md)| Comma separated list of item ids to include (only heroes who have purchased these items). See more: <https://assets.deadlock-api.com/v2/items> | [optional] [default to const []]
 **excludeItemIds** | [**List<int>**](int.md)| Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: <https://assets.deadlock-api.com/v2/items> | [optional] [default to const []]
 **accountId** | **int**| Filter for matches with a specific player account ID. | [optional] 
 **accountIds** | [**List<int>**](int.md)| Comma separated list of account ids to include | [optional] [default to const []]

### Return type

[**List<AnalyticsHeroStats>**](AnalyticsHeroStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroSynergiesStats**
> List<HeroSynergyStats> heroSynergiesStats(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, sameLaneFilter, samePartyFilter, minMatches, maxMatches, accountId, accountIds)

Hero Synergy Stats

 Retrieves hero pair synergy statistics based on historical match data.  This endpoint analyzes completed matches to calculate how often a specific pair of heroes (`hero_id1` and `hero_id2`) won when playing *together on the same team*, and the total number of times they have played together under the specified filter conditions.  Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = AnalyticsApi();
final minUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
final maxUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final minDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final maxDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final minNetworth = 789; // int | Filter players based on their net worth.
final maxNetworth = 789; // int | Filter players based on their net worth.
final minAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final maxAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final minMatchId = 789; // int | Filter matches based on their ID.
final maxMatchId = 789; // int | Filter matches based on their ID.
final sameLaneFilter = true; // bool | When `true`, only considers matchups where both `hero_id1` and `hero_id2` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane.
final samePartyFilter = true; // bool | When `true`, only considers matchups where both `hero_id` and `hero_id2` were on the same party. When `false`, considers all matchups regardless of party affiliation.
final minMatches = 789; // int | The minimum number of matches played for a hero combination to be included in the response.
final maxMatches = 56; // int | The maximum number of matches played for a hero combination to be included in the response.
final accountId = 56; // int | Filter for matches with a specific player account ID.
final accountIds = []; // List<int> | Comma separated list of account ids to include

try {
    final result = api_instance.heroSynergiesStats(minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, sameLaneFilter, samePartyFilter, minMatches, maxMatches, accountId, accountIds);
    print(result);
} catch (e) {
    print('Exception when calling AnalyticsApi->heroSynergiesStats: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1759449600]
 **maxUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **minDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **maxDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **minNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **maxNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **minAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **maxAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **minMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **sameLaneFilter** | **bool**| When `true`, only considers matchups where both `hero_id1` and `hero_id2` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane. | [optional] [default to true]
 **samePartyFilter** | **bool**| When `true`, only considers matchups where both `hero_id` and `hero_id2` were on the same party. When `false`, considers all matchups regardless of party affiliation. | [optional] [default to true]
 **minMatches** | **int**| The minimum number of matches played for a hero combination to be included in the response. | [optional] [default to 20]
 **maxMatches** | **int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] 
 **accountId** | **int**| Filter for matches with a specific player account ID. | [optional] 
 **accountIds** | [**List<int>**](int.md)| Comma separated list of account ids to include | [optional] [default to const []]

### Return type

[**List<HeroSynergyStats>**](HeroSynergyStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **itemPermutationStats**
> List<ItemPermutationStats> itemPermutationStats(itemIds, combSize, heroIds, heroId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, accountId, accountIds)

Item Permutation Stats

 Retrieves item permutation statistics based on historical match data.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = AnalyticsApi();
final itemIds = []; // List<int> | Comma separated list of item ids. See more: <https://assets.deadlock-api.com/v2/items>
final combSize = 56; // int | The combination size to return.
final heroIds = heroIds_example; // String | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes>
final heroId = 56; // int | Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
final minUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
final maxUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final minDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final maxDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final minNetworth = 789; // int | Filter players based on their net worth.
final maxNetworth = 789; // int | Filter players based on their net worth.
final minAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final maxAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final minMatchId = 789; // int | Filter matches based on their ID.
final maxMatchId = 789; // int | Filter matches based on their ID.
final accountId = 56; // int | Filter for matches with a specific player account ID.
final accountIds = []; // List<int> | Comma separated list of account ids to include

try {
    final result = api_instance.itemPermutationStats(itemIds, combSize, heroIds, heroId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, accountId, accountIds);
    print(result);
} catch (e) {
    print('Exception when calling AnalyticsApi->itemPermutationStats: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemIds** | [**List<int>**](int.md)| Comma separated list of item ids. See more: <https://assets.deadlock-api.com/v2/items> | [optional] [default to const []]
 **combSize** | **int**| The combination size to return. | [optional] [default to 2]
 **heroIds** | **String**| Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> | [optional] 
 **heroId** | **int**| Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> | [optional] 
 **minUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1759449600]
 **maxUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **minDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **maxDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **minNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **maxNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **minAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **maxAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **minMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **accountId** | **int**| Filter for matches with a specific player account ID. | [optional] 
 **accountIds** | [**List<int>**](int.md)| Comma separated list of account ids to include | [optional] [default to const []]

### Return type

[**List<ItemPermutationStats>**](ItemPermutationStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **itemStats**
> List<ItemStats> itemStats(bucket, heroIds, heroId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, includeItemIds, excludeItemIds, minMatches, maxMatches, accountId, accountIds)

Item Stats

 Retrieves item statistics based on historical match data.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = AnalyticsApi();
final bucket = bucket_example; // String | Bucket allows you to group the stats by a specific field.
final heroIds = heroIds_example; // String | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes>
final heroId = 56; // int | Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
final minUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
final maxUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final minDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final maxDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final minNetworth = 789; // int | Filter players based on their net worth.
final maxNetworth = 789; // int | Filter players based on their net worth.
final minAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final maxAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final minMatchId = 789; // int | Filter matches based on their ID.
final maxMatchId = 789; // int | Filter matches based on their ID.
final includeItemIds = []; // List<int> | Comma separated list of item ids to include. See more: <https://assets.deadlock-api.com/v2/items>
final excludeItemIds = []; // List<int> | Comma separated list of item ids to exclude. See more: <https://assets.deadlock-api.com/v2/items>
final minMatches = 56; // int | The minimum number of matches played for an item to be included in the response.
final maxMatches = 56; // int | The maximum number of matches played for a hero combination to be included in the response.
final accountId = 56; // int | Filter for matches with a specific player account ID.
final accountIds = []; // List<int> | Comma separated list of account ids to include

try {
    final result = api_instance.itemStats(bucket, heroIds, heroId, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, includeItemIds, excludeItemIds, minMatches, maxMatches, accountId, accountIds);
    print(result);
} catch (e) {
    print('Exception when calling AnalyticsApi->itemStats: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **String**| Bucket allows you to group the stats by a specific field. | [optional] 
 **heroIds** | **String**| Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> | [optional] 
 **heroId** | **int**| Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> | [optional] 
 **minUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1759449600]
 **maxUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **minDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **maxDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **minNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **maxNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **minAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **maxAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **minMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **includeItemIds** | [**List<int>**](int.md)| Comma separated list of item ids to include. See more: <https://assets.deadlock-api.com/v2/items> | [optional] [default to const []]
 **excludeItemIds** | [**List<int>**](int.md)| Comma separated list of item ids to exclude. See more: <https://assets.deadlock-api.com/v2/items> | [optional] [default to const []]
 **minMatches** | **int**| The minimum number of matches played for an item to be included in the response. | [optional] [default to 20]
 **maxMatches** | **int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] 
 **accountId** | **int**| Filter for matches with a specific player account ID. | [optional] 
 **accountIds** | [**List<int>**](int.md)| Comma separated list of account ids to include | [optional] [default to const []]

### Return type

[**List<ItemStats>**](ItemStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playerScoreboard**
> List<Entry> playerScoreboard(sortBy, sortDirection, heroId, minMatches, maxMatches, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, start, limit, accountIds)

Player Scoreboard

 This endpoint returns the player scoreboard.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = AnalyticsApi();
final sortBy = sortBy_example; // String | The field to sort by.
final sortDirection = sortDirection_example; // String | The direction to sort players in.
final heroId = 56; // int | Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
final minMatches = 56; // int | The minimum number of matches played for a player to be included in the scoreboard.
final maxMatches = 56; // int | The maximum number of matches played for a hero combination to be included in the response.
final minUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final maxUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final minDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final maxDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final minNetworth = 789; // int | Filter players based on their net worth.
final maxNetworth = 789; // int | Filter players based on their net worth.
final minAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final maxAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final minMatchId = 789; // int | Filter matches based on their ID.
final maxMatchId = 789; // int | Filter matches based on their ID.
final start = 56; // int | The offset to start fetching players from.
final limit = 56; // int | The maximum number of players to fetch.
final accountIds = []; // List<int> | Comma separated list of account ids to include

try {
    final result = api_instance.playerScoreboard(sortBy, sortDirection, heroId, minMatches, maxMatches, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, start, limit, accountIds);
    print(result);
} catch (e) {
    print('Exception when calling AnalyticsApi->playerScoreboard: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortBy** | **String**| The field to sort by. | 
 **sortDirection** | **String**| The direction to sort players in. | [optional] 
 **heroId** | **int**| Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> | [optional] 
 **minMatches** | **int**| The minimum number of matches played for a player to be included in the scoreboard. | [optional] [default to 20]
 **maxMatches** | **int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] 
 **minUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **maxUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **minDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **maxDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **minNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **maxNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **minAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **maxAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **minMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **start** | **int**| The offset to start fetching players from. | [optional] 
 **limit** | **int**| The maximum number of players to fetch. | [optional] [default to 100]
 **accountIds** | [**List<int>**](int.md)| Comma separated list of account ids to include | [optional] [default to const []]

### Return type

[**List<Entry>**](Entry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playerStatsMetrics**
> Map<String, HashMapValue> playerStatsMetrics(heroIds, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, maxMatches, includeItemIds, excludeItemIds, accountIds)

Player Stats Metrics

 Returns comprehensive statistical analysis of player performance.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  > Note: Quantiles are calculated using the [DDSketch](https://www.vldb.org/pvldb/vol12/p2195-masson.pdf) algorithm, so they are not exact but have a maximum relative error of 0.01.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = AnalyticsApi();
final heroIds = heroIds_example; // String | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes>
final minUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
final maxUnixTimestamp = 789; // int | Filter matches based on their start time (Unix timestamp).
final minDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final maxDurationS = 789; // int | Filter matches based on their duration in seconds (up to 7000s).
final minNetworth = 789; // int | Filter players based on their net worth.
final maxNetworth = 789; // int | Filter players based on their net worth.
final minAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final maxAverageBadge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
final minMatchId = 789; // int | Filter matches based on their ID.
final maxMatchId = 789; // int | Filter matches based on their ID.
final maxMatches = 56; // int | The maximum number of matches to analyze.
final includeItemIds = []; // List<int> | Comma separated list of item ids to include (only heroes who have purchased these items). See more: <https://assets.deadlock-api.com/v2/items>
final excludeItemIds = []; // List<int> | Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: <https://assets.deadlock-api.com/v2/items>
final accountIds = []; // List<int> | Comma separated list of account ids to include

try {
    final result = api_instance.playerStatsMetrics(heroIds, minUnixTimestamp, maxUnixTimestamp, minDurationS, maxDurationS, minNetworth, maxNetworth, minAverageBadge, maxAverageBadge, minMatchId, maxMatchId, maxMatches, includeItemIds, excludeItemIds, accountIds);
    print(result);
} catch (e) {
    print('Exception when calling AnalyticsApi->playerStatsMetrics: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heroIds** | **String**| Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> | [optional] 
 **minUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1759449600]
 **maxUnixTimestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **minDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **maxDurationS** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **minNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **maxNetworth** | **int**| Filter players based on their net worth. | [optional] 
 **minAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **maxAverageBadge** | **int**| Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
 **minMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **maxMatchId** | **int**| Filter matches based on their ID. | [optional] 
 **maxMatches** | **int**| The maximum number of matches to analyze. | [optional] 
 **includeItemIds** | [**List<int>**](int.md)| Comma separated list of item ids to include (only heroes who have purchased these items). See more: <https://assets.deadlock-api.com/v2/items> | [optional] [default to const []]
 **excludeItemIds** | [**List<int>**](int.md)| Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: <https://assets.deadlock-api.com/v2/items> | [optional] [default to const []]
 **accountIds** | [**List<int>**](int.md)| Comma separated list of account ids to include | [optional] [default to const []]

### Return type

[**Map<String, HashMapValue>**](HashMapValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

