# OpenAPI\Client\AnalyticsApi

Comprehensive game statistics and analysis endpoints. Provides detailed performance metrics for heroes, items, and players, including hero synergies, counters, and combinations. Features scoreboards for both heroes and players.

All URIs are relative to https://api.deadlock-api.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**abilityOrderStats()**](AnalyticsApi.md#abilityOrderStats) | **GET** /v1/analytics/ability-order-stats | Ability Order Stats |
| [**badgeDistribution()**](AnalyticsApi.md#badgeDistribution) | **GET** /v1/analytics/badge-distribution | Badge Distribution |
| [**buildItemStats()**](AnalyticsApi.md#buildItemStats) | **GET** /v1/analytics/build-item-stats | Build Item Stats |
| [**heroCombStats()**](AnalyticsApi.md#heroCombStats) | **GET** /v1/analytics/hero-comb-stats | Hero Comb Stats |
| [**heroCountersStats()**](AnalyticsApi.md#heroCountersStats) | **GET** /v1/analytics/hero-counter-stats | Hero Counter Stats |
| [**heroScoreboard()**](AnalyticsApi.md#heroScoreboard) | **GET** /v1/analytics/scoreboards/heroes | Hero Scoreboard |
| [**heroStats()**](AnalyticsApi.md#heroStats) | **GET** /v1/analytics/hero-stats | Hero Stats |
| [**heroSynergiesStats()**](AnalyticsApi.md#heroSynergiesStats) | **GET** /v1/analytics/hero-synergy-stats | Hero Synergy Stats |
| [**itemPermutationStats()**](AnalyticsApi.md#itemPermutationStats) | **GET** /v1/analytics/item-permutation-stats | Item Permutation Stats |
| [**itemStats()**](AnalyticsApi.md#itemStats) | **GET** /v1/analytics/item-stats | Item Stats |
| [**killDeathStats()**](AnalyticsApi.md#killDeathStats) | **GET** /v1/analytics/kill-death-stats | Kill Death Stats |
| [**playerPerformanceCurve()**](AnalyticsApi.md#playerPerformanceCurve) | **GET** /v1/analytics/player-performance-curve | Player Performance Curve |
| [**playerScoreboard()**](AnalyticsApi.md#playerScoreboard) | **GET** /v1/analytics/scoreboards/players | Player Scoreboard |
| [**playerStatsMetrics()**](AnalyticsApi.md#playerStatsMetrics) | **GET** /v1/analytics/player-stats/metrics | Player Stats Metrics |


## `abilityOrderStats()`

```php
abilityOrderStats($hero_id, $game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_ability_upgrades, $max_ability_upgrades, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $min_matches, $account_id, $account_ids): \OpenAPI\Client\Model\AnalyticsAbilityOrderStats[]
```

Ability Order Stats

Retrieves statistics for the ability order of a hero.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$hero_id = 56; // int | See more: <https://assets.deadlock-api.com/v2/heroes>
$game_mode = 'game_mode_example'; // string | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
$min_unix_timestamp = 1768867200; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$min_ability_upgrades = 56; // int | Filter players based on their minimum number of ability upgrades over the whole match.
$max_ability_upgrades = 56; // int | Filter players based on their maximum number of ability upgrades over the whole match.
$min_networth = 56; // int | Filter players based on their final net worth.
$max_networth = 56; // int | Filter players based on their final net worth.
$min_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$max_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.
$min_matches = 20; // int | The minimum number of matches played for an ability order to be included in the response.
$account_id = 56; // int | Filter for matches with a specific player account ID.
$account_ids = array(56); // int[] | Comma separated list of account ids to include

try {
    $result = $apiInstance->abilityOrderStats($hero_id, $game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_ability_upgrades, $max_ability_upgrades, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $min_matches, $account_id, $account_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->abilityOrderStats: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **hero_id** | **int**| See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | |
| **game_mode** | **string**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1768867200] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **min_ability_upgrades** | **int**| Filter players based on their minimum number of ability upgrades over the whole match. | [optional] |
| **max_ability_upgrades** | **int**| Filter players based on their maximum number of ability upgrades over the whole match. | [optional] |
| **min_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **max_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **min_matches** | **int**| The minimum number of matches played for an ability order to be included in the response. | [optional] [default to 20] |
| **account_id** | **int**| Filter for matches with a specific player account ID. | [optional] |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**\OpenAPI\Client\Model\AnalyticsAbilityOrderStats[]**](../Model/AnalyticsAbilityOrderStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `badgeDistribution()`

```php
badgeDistribution($game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $is_high_skill_range_parties, $is_low_pri_pool, $is_new_player_pool, $min_match_id, $max_match_id): \OpenAPI\Client\Model\BadgeDistribution[]
```

Badge Distribution

This endpoint returns the player badge distribution.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$game_mode = 'game_mode_example'; // string | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
$min_unix_timestamp = 1768867200; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$is_high_skill_range_parties = True; // bool | Filter matches based on whether they are in the high skill range.
$is_low_pri_pool = True; // bool | Filter matches based on whether they are in the low priority pool.
$is_new_player_pool = True; // bool | Filter matches based on whether they are in the new player pool.
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.

try {
    $result = $apiInstance->badgeDistribution($game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $is_high_skill_range_parties, $is_low_pri_pool, $is_new_player_pool, $min_match_id, $max_match_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->badgeDistribution: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **game_mode** | **string**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1768867200] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **is_high_skill_range_parties** | **bool**| Filter matches based on whether they are in the high skill range. | [optional] |
| **is_low_pri_pool** | **bool**| Filter matches based on whether they are in the low priority pool. | [optional] |
| **is_new_player_pool** | **bool**| Filter matches based on whether they are in the new player pool. | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |

### Return type

[**\OpenAPI\Client\Model\BadgeDistribution[]**](../Model/BadgeDistribution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `buildItemStats()`

```php
buildItemStats($hero_id, $min_last_updated_unix_timestamp, $max_last_updated_unix_timestamp): \OpenAPI\Client\Model\BuildItemStats[]
```

Build Item Stats

Retrieves item statistics from hero builds.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$hero_id = 56; // int | Filter builds based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
$min_last_updated_unix_timestamp = 1768867200; // int | Filter builds based on their last updated time (Unix timestamp). **Default:** 30 days ago.
$max_last_updated_unix_timestamp = 56; // int | Filter builds based on their last updated time (Unix timestamp).

try {
    $result = $apiInstance->buildItemStats($hero_id, $min_last_updated_unix_timestamp, $max_last_updated_unix_timestamp);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->buildItemStats: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **hero_id** | **int**| Filter builds based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **min_last_updated_unix_timestamp** | **int**| Filter builds based on their last updated time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1768867200] |
| **max_last_updated_unix_timestamp** | **int**| Filter builds based on their last updated time (Unix timestamp). | [optional] |

### Return type

[**\OpenAPI\Client\Model\BuildItemStats[]**](../Model/BuildItemStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `heroCombStats()`

```php
heroCombStats($game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $include_hero_ids, $exclude_hero_ids, $min_matches, $max_matches, $comb_size, $account_id, $account_ids): \OpenAPI\Client\Model\HeroCombStats[]
```

Hero Comb Stats

Retrieves overall statistics for each hero combination.  Results are cached for **1 hour**. The cache key is determined by the specific combination of filter parameters used in the query. Subsequent requests using the exact same filters within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$game_mode = 'game_mode_example'; // string | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
$min_unix_timestamp = 1768867200; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$min_networth = 56; // int | Filter players based on their final net worth.
$max_networth = 56; // int | Filter players based on their final net worth.
$min_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$max_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.
$include_hero_ids = array(56); // int[] | Comma separated list of hero ids to include. See more: <https://assets.deadlock-api.com/v2/heroes>
$exclude_hero_ids = array(56); // int[] | Comma separated list of hero ids to exclude. See more: <https://assets.deadlock-api.com/v2/heroes>
$min_matches = 20; // int | The minimum number of matches played for a hero combination to be included in the response.
$max_matches = 56; // int | The maximum number of matches played for a hero combination to be included in the response.
$comb_size = 6; // int | The combination size to return.
$account_id = 56; // int | Filter for matches with a specific player account ID.
$account_ids = array(56); // int[] | Comma separated list of account ids to include

try {
    $result = $apiInstance->heroCombStats($game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $include_hero_ids, $exclude_hero_ids, $min_matches, $max_matches, $comb_size, $account_id, $account_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->heroCombStats: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **game_mode** | **string**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1768867200] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **min_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **max_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **include_hero_ids** | [**int[]**](../Model/int.md)| Comma separated list of hero ids to include. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **exclude_hero_ids** | [**int[]**](../Model/int.md)| Comma separated list of hero ids to exclude. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **min_matches** | **int**| The minimum number of matches played for a hero combination to be included in the response. | [optional] [default to 20] |
| **max_matches** | **int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] |
| **comb_size** | **int**| The combination size to return. | [optional] [default to 6] |
| **account_id** | **int**| Filter for matches with a specific player account ID. | [optional] |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**\OpenAPI\Client\Model\HeroCombStats[]**](../Model/HeroCombStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `heroCountersStats()`

```php
heroCountersStats($game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_enemy_networth, $max_enemy_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $same_lane_filter, $min_matches, $max_matches, $account_id, $account_ids): \OpenAPI\Client\Model\HeroCounterStats[]
```

Hero Counter Stats

Retrieves hero-versus-hero matchup statistics based on historical match data.  This endpoint analyzes completed matches to calculate how often a specific hero (`hero_id`) wins against an enemy hero (`enemy_hero_id`) and the total number of times they have faced each other under the specified filter conditions.  Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$game_mode = 'game_mode_example'; // string | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
$min_unix_timestamp = 1768867200; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$min_networth = 56; // int | Filter players based on their final net worth.
$max_networth = 56; // int | Filter players based on their final net worth.
$min_enemy_networth = 56; // int | Filter enemy players based on their net worth.
$max_enemy_networth = 56; // int | Filter enemy players based on their net worth.
$min_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$max_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.
$same_lane_filter = true; // bool | When `true`, only considers matchups where both `hero_id` and `enemy_hero_id` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane.
$min_matches = 20; // int | The minimum number of matches played for a hero combination to be included in the response.
$max_matches = 56; // int | The maximum number of matches played for a hero combination to be included in the response.
$account_id = 56; // int | Filter for matches with a specific player account ID.
$account_ids = array(56); // int[] | Comma separated list of account ids to include

try {
    $result = $apiInstance->heroCountersStats($game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_enemy_networth, $max_enemy_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $same_lane_filter, $min_matches, $max_matches, $account_id, $account_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->heroCountersStats: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **game_mode** | **string**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1768867200] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **min_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **max_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **min_enemy_networth** | **int**| Filter enemy players based on their net worth. | [optional] |
| **max_enemy_networth** | **int**| Filter enemy players based on their net worth. | [optional] |
| **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **same_lane_filter** | **bool**| When &#x60;true&#x60;, only considers matchups where both &#x60;hero_id&#x60; and &#x60;enemy_hero_id&#x60; were assigned to the same lane (e.g., both Mid Lane). When &#x60;false&#x60;, considers all matchups regardless of assigned lane. | [optional] [default to true] |
| **min_matches** | **int**| The minimum number of matches played for a hero combination to be included in the response. | [optional] [default to 20] |
| **max_matches** | **int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] |
| **account_id** | **int**| Filter for matches with a specific player account ID. | [optional] |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**\OpenAPI\Client\Model\HeroCounterStats[]**](../Model/HeroCounterStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `heroScoreboard()`

```php
heroScoreboard($sort_by, $sort_direction, $game_mode, $min_matches, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $account_id, $account_ids): \OpenAPI\Client\Model\Entry[]
```

Hero Scoreboard

This endpoint returns the hero scoreboard.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$sort_by = 'sort_by_example'; // string | The field to sort by.
$sort_direction = 'sort_direction_example'; // string | The direction to sort heroes in.
$game_mode = 'game_mode_example'; // string | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
$min_matches = 56; // int | Filter by min number of matches played.
$min_unix_timestamp = 1768867200; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$min_networth = 56; // int | Filter players based on their final net worth.
$max_networth = 56; // int | Filter players based on their final net worth.
$min_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$max_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.
$account_id = 56; // int | Filter for matches with a specific player account ID.
$account_ids = array(56); // int[] | Comma separated list of account ids to include

try {
    $result = $apiInstance->heroScoreboard($sort_by, $sort_direction, $game_mode, $min_matches, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $account_id, $account_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->heroScoreboard: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **sort_by** | **string**| The field to sort by. | |
| **sort_direction** | **string**| The direction to sort heroes in. | [optional] |
| **game_mode** | **string**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] |
| **min_matches** | **int**| Filter by min number of matches played. | [optional] |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1768867200] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **min_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **max_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **account_id** | **int**| Filter for matches with a specific player account ID. | [optional] |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**\OpenAPI\Client\Model\Entry[]**](../Model/Entry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `heroStats()`

```php
heroStats($bucket, $game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $min_hero_matches, $max_hero_matches, $min_hero_matches_total, $max_hero_matches_total, $include_item_ids, $exclude_item_ids, $account_id, $account_ids): \OpenAPI\Client\Model\AnalyticsHeroStats[]
```

Hero Stats

Retrieves performance statistics for each hero based on historical match data.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$bucket = 'bucket_example'; // string | Bucket allows you to group the stats by a specific field.
$game_mode = 'game_mode_example'; // string | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
$min_unix_timestamp = 1768867200; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$min_networth = 56; // int | Filter players based on their final net worth.
$max_networth = 56; // int | Filter players based on their final net worth.
$min_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$max_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.
$min_hero_matches = 56; // int | Filter players based on the number of matches they have played with a specific hero within the filtered time range.
$max_hero_matches = 56; // int | Filter players based on the number of matches they have played with a specific hero within the filtered time range.
$min_hero_matches_total = 56; // int | Filter players based on the number of matches they have played with a specific hero in their entire history.
$max_hero_matches_total = 56; // int | Filter players based on the number of matches they have played with a specific hero in their entire history.
$include_item_ids = array(56); // int[] | Comma separated list of item ids to include (only players who have purchased these items). See more: <https://assets.deadlock-api.com/v2/items>
$exclude_item_ids = array(56); // int[] | Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://assets.deadlock-api.com/v2/items>
$account_id = 56; // int | Filter for matches with a specific player account ID.
$account_ids = array(56); // int[] | Comma separated list of account ids to include

try {
    $result = $apiInstance->heroStats($bucket, $game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $min_hero_matches, $max_hero_matches, $min_hero_matches_total, $max_hero_matches_total, $include_item_ids, $exclude_item_ids, $account_id, $account_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->heroStats: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **bucket** | **string**| Bucket allows you to group the stats by a specific field. | [optional] |
| **game_mode** | **string**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1768867200] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **min_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **max_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **min_hero_matches** | **int**| Filter players based on the number of matches they have played with a specific hero within the filtered time range. | [optional] |
| **max_hero_matches** | **int**| Filter players based on the number of matches they have played with a specific hero within the filtered time range. | [optional] |
| **min_hero_matches_total** | **int**| Filter players based on the number of matches they have played with a specific hero in their entire history. | [optional] |
| **max_hero_matches_total** | **int**| Filter players based on the number of matches they have played with a specific hero in their entire history. | [optional] |
| **include_item_ids** | [**int[]**](../Model/int.md)| Comma separated list of item ids to include (only players who have purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] |
| **exclude_item_ids** | [**int[]**](../Model/int.md)| Comma separated list of item ids to exclude (only players who have not purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] |
| **account_id** | **int**| Filter for matches with a specific player account ID. | [optional] |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**\OpenAPI\Client\Model\AnalyticsHeroStats[]**](../Model/AnalyticsHeroStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `heroSynergiesStats()`

```php
heroSynergiesStats($game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $same_lane_filter, $same_party_filter, $min_matches, $max_matches, $account_id, $account_ids): \OpenAPI\Client\Model\HeroSynergyStats[]
```

Hero Synergy Stats

Retrieves hero pair synergy statistics based on historical match data.  This endpoint analyzes completed matches to calculate how often a specific pair of heroes (`hero_id1` and `hero_id2`) won when playing *together on the same team*, and the total number of times they have played together under the specified filter conditions.  Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$game_mode = 'game_mode_example'; // string | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
$min_unix_timestamp = 1768867200; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$min_networth = 56; // int | Filter players based on their final net worth.
$max_networth = 56; // int | Filter players based on their final net worth.
$min_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$max_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.
$same_lane_filter = true; // bool | When `true`, only considers matchups where both `hero_id1` and `hero_id2` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane.
$same_party_filter = true; // bool | When `true`, only considers matchups where both `hero_id` and `hero_id2` were on the same party. When `false`, considers all matchups regardless of party affiliation.
$min_matches = 20; // int | The minimum number of matches played for a hero combination to be included in the response.
$max_matches = 56; // int | The maximum number of matches played for a hero combination to be included in the response.
$account_id = 56; // int | Filter for matches with a specific player account ID.
$account_ids = array(56); // int[] | Comma separated list of account ids to include

try {
    $result = $apiInstance->heroSynergiesStats($game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $same_lane_filter, $same_party_filter, $min_matches, $max_matches, $account_id, $account_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->heroSynergiesStats: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **game_mode** | **string**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1768867200] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **min_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **max_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **same_lane_filter** | **bool**| When &#x60;true&#x60;, only considers matchups where both &#x60;hero_id1&#x60; and &#x60;hero_id2&#x60; were assigned to the same lane (e.g., both Mid Lane). When &#x60;false&#x60;, considers all matchups regardless of assigned lane. | [optional] [default to true] |
| **same_party_filter** | **bool**| When &#x60;true&#x60;, only considers matchups where both &#x60;hero_id&#x60; and &#x60;hero_id2&#x60; were on the same party. When &#x60;false&#x60;, considers all matchups regardless of party affiliation. | [optional] [default to true] |
| **min_matches** | **int**| The minimum number of matches played for a hero combination to be included in the response. | [optional] [default to 20] |
| **max_matches** | **int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] |
| **account_id** | **int**| Filter for matches with a specific player account ID. | [optional] |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**\OpenAPI\Client\Model\HeroSynergyStats[]**](../Model/HeroSynergyStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `itemPermutationStats()`

```php
itemPermutationStats($item_ids, $comb_size, $game_mode, $hero_ids, $hero_id, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $account_id, $account_ids): \OpenAPI\Client\Model\ItemPermutationStats[]
```

Item Permutation Stats

Retrieves item permutation statistics based on historical match data.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$item_ids = array(56); // int[] | Comma separated list of item ids. See more: <https://assets.deadlock-api.com/v2/items>
$comb_size = 2; // int | The combination size to return.
$game_mode = 'game_mode_example'; // string | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
$hero_ids = 'hero_ids_example'; // string | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes>
$hero_id = 56; // int | Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
$min_unix_timestamp = 1768867200; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$min_networth = 56; // int | Filter players based on their final net worth.
$max_networth = 56; // int | Filter players based on their final net worth.
$min_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$max_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.
$account_id = 56; // int | Filter for matches with a specific player account ID.
$account_ids = array(56); // int[] | Comma separated list of account ids to include

try {
    $result = $apiInstance->itemPermutationStats($item_ids, $comb_size, $game_mode, $hero_ids, $hero_id, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $account_id, $account_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->itemPermutationStats: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **item_ids** | [**int[]**](../Model/int.md)| Comma separated list of item ids. See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] |
| **comb_size** | **int**| The combination size to return. | [optional] [default to 2] |
| **game_mode** | **string**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] |
| **hero_ids** | **string**| Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **hero_id** | **int**| Filter matches based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1768867200] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **min_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **max_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **account_id** | **int**| Filter for matches with a specific player account ID. | [optional] |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**\OpenAPI\Client\Model\ItemPermutationStats[]**](../Model/ItemPermutationStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `itemStats()`

```php
itemStats($bucket, $game_mode, $hero_ids, $hero_id, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $include_item_ids, $exclude_item_ids, $min_matches, $max_matches, $account_id, $account_ids, $min_bought_at_s, $max_bought_at_s): \OpenAPI\Client\Model\ItemStats[]
```

Item Stats

Retrieves item statistics based on historical match data.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$bucket = 'bucket_example'; // string | Bucket allows you to group the stats by a specific field.
$game_mode = 'game_mode_example'; // string | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
$hero_ids = 'hero_ids_example'; // string | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes>
$hero_id = 56; // int | Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
$min_unix_timestamp = 1768867200; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$min_networth = 56; // int | Filter players based on their final net worth.
$max_networth = 56; // int | Filter players based on their final net worth.
$min_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$max_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.
$include_item_ids = array(56); // int[] | Comma separated list of item ids to include. See more: <https://assets.deadlock-api.com/v2/items>
$exclude_item_ids = array(56); // int[] | Comma separated list of item ids to exclude. See more: <https://assets.deadlock-api.com/v2/items>
$min_matches = 20; // int | The minimum number of matches played for an item to be included in the response.
$max_matches = 56; // int | The maximum number of matches played for a hero combination to be included in the response.
$account_id = 56; // int | Filter for matches with a specific player account ID.
$account_ids = array(56); // int[] | Comma separated list of account ids to include
$min_bought_at_s = 56; // int | Filter items bought after this game time (seconds).
$max_bought_at_s = 56; // int | Filter items bought before this game time (seconds).

try {
    $result = $apiInstance->itemStats($bucket, $game_mode, $hero_ids, $hero_id, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $include_item_ids, $exclude_item_ids, $min_matches, $max_matches, $account_id, $account_ids, $min_bought_at_s, $max_bought_at_s);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->itemStats: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **bucket** | **string**| Bucket allows you to group the stats by a specific field. | [optional] |
| **game_mode** | **string**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] |
| **hero_ids** | **string**| Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **hero_id** | **int**| Filter matches based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1768867200] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **min_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **max_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **include_item_ids** | [**int[]**](../Model/int.md)| Comma separated list of item ids to include. See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] |
| **exclude_item_ids** | [**int[]**](../Model/int.md)| Comma separated list of item ids to exclude. See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] |
| **min_matches** | **int**| The minimum number of matches played for an item to be included in the response. | [optional] [default to 20] |
| **max_matches** | **int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] |
| **account_id** | **int**| Filter for matches with a specific player account ID. | [optional] |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids to include | [optional] |
| **min_bought_at_s** | **int**| Filter items bought after this game time (seconds). | [optional] |
| **max_bought_at_s** | **int**| Filter items bought before this game time (seconds). | [optional] |

### Return type

[**\OpenAPI\Client\Model\ItemStats[]**](../Model/ItemStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `killDeathStats()`

```php
killDeathStats($team, $game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $account_ids, $hero_ids, $min_networth, $max_networth, $is_high_skill_range_parties, $is_low_pri_pool, $is_new_player_pool, $min_match_id, $max_match_id, $min_average_badge, $max_average_badge, $min_kills_per_raster, $max_kills_per_raster, $min_deaths_per_raster, $max_deaths_per_raster, $min_game_time_s, $max_game_time_s): \OpenAPI\Client\Model\KillDeathStats[]
```

Kill Death Stats

This endpoint returns the kill-death statistics across a 100x100 pixel raster.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$team = 56; // int | Filter by team number.
$game_mode = 'game_mode_example'; // string | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
$min_unix_timestamp = 1768867200; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$account_ids = array(56); // int[] | Filter matches by account IDs of players that participated in the match.
$hero_ids = 'hero_ids_example'; // string | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes>
$min_networth = 56; // int | Filter players based on their final net worth.
$max_networth = 56; // int | Filter players based on their final net worth.
$is_high_skill_range_parties = True; // bool | Filter matches based on whether they are in the high skill range.
$is_low_pri_pool = True; // bool | Filter matches based on whether they are in the low priority pool.
$is_new_player_pool = True; // bool | Filter matches based on whether they are in the new player pool.
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.
$min_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$max_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$min_kills_per_raster = 56; // int | Filter Raster cells based on minimum kills.
$max_kills_per_raster = 56; // int | Filter Raster cells based on maximum kills.
$min_deaths_per_raster = 56; // int | Filter Raster cells based on minimum deaths.
$max_deaths_per_raster = 56; // int | Filter Raster cells based on maximum deaths.
$min_game_time_s = 56; // int | Filter kills based on their game time.
$max_game_time_s = 56; // int | Filter kills based on their game time.

try {
    $result = $apiInstance->killDeathStats($team, $game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $account_ids, $hero_ids, $min_networth, $max_networth, $is_high_skill_range_parties, $is_low_pri_pool, $is_new_player_pool, $min_match_id, $max_match_id, $min_average_badge, $max_average_badge, $min_kills_per_raster, $max_kills_per_raster, $min_deaths_per_raster, $max_deaths_per_raster, $min_game_time_s, $max_game_time_s);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->killDeathStats: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **team** | **int**| Filter by team number. | [optional] |
| **game_mode** | **string**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1768867200] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **account_ids** | [**int[]**](../Model/int.md)| Filter matches by account IDs of players that participated in the match. | [optional] |
| **hero_ids** | **string**| Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **min_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **max_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **is_high_skill_range_parties** | **bool**| Filter matches based on whether they are in the high skill range. | [optional] |
| **is_low_pri_pool** | **bool**| Filter matches based on whether they are in the low priority pool. | [optional] |
| **is_new_player_pool** | **bool**| Filter matches based on whether they are in the new player pool. | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **min_kills_per_raster** | **int**| Filter Raster cells based on minimum kills. | [optional] |
| **max_kills_per_raster** | **int**| Filter Raster cells based on maximum kills. | [optional] |
| **min_deaths_per_raster** | **int**| Filter Raster cells based on minimum deaths. | [optional] |
| **max_deaths_per_raster** | **int**| Filter Raster cells based on maximum deaths. | [optional] |
| **min_game_time_s** | **int**| Filter kills based on their game time. | [optional] |
| **max_game_time_s** | **int**| Filter kills based on their game time. | [optional] |

### Return type

[**\OpenAPI\Client\Model\KillDeathStats[]**](../Model/KillDeathStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `playerPerformanceCurve()`

```php
playerPerformanceCurve($resolution, $game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $hero_ids, $include_item_ids, $exclude_item_ids, $account_ids): \OpenAPI\Client\Model\PlayerPerformanceCurvePoint[]
```

Player Performance Curve

Retrieves player performance statistics (net worth, kills, deaths, assists) over time throughout matches.  Results are cached for **1 hour** based on the unique combination of query parameters provided.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$resolution = 10; // int | Resolution for relative game times in percent (0-100). **Default:** 10 (buckets of 10%). Set to **0** to use absolute game time (seconds).
$game_mode = 'game_mode_example'; // string | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
$min_unix_timestamp = 1768867200; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$min_networth = 56; // int | Filter players based on their final net worth.
$max_networth = 56; // int | Filter players based on their final net worth.
$min_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$max_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.
$hero_ids = 'hero_ids_example'; // string | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes>
$include_item_ids = array(56); // int[] | Comma separated list of item ids to include (only players who have purchased these items). See more: <https://assets.deadlock-api.com/v2/items>
$exclude_item_ids = array(56); // int[] | Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://assets.deadlock-api.com/v2/items>
$account_ids = array(56); // int[] | Comma separated list of account ids to include

try {
    $result = $apiInstance->playerPerformanceCurve($resolution, $game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $hero_ids, $include_item_ids, $exclude_item_ids, $account_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->playerPerformanceCurve: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **resolution** | **int**| Resolution for relative game times in percent (0-100). **Default:** 10 (buckets of 10%). Set to **0** to use absolute game time (seconds). | [optional] [default to 10] |
| **game_mode** | **string**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1768867200] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **min_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **max_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **hero_ids** | **string**| Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **include_item_ids** | [**int[]**](../Model/int.md)| Comma separated list of item ids to include (only players who have purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] |
| **exclude_item_ids** | [**int[]**](../Model/int.md)| Comma separated list of item ids to exclude (only players who have not purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**\OpenAPI\Client\Model\PlayerPerformanceCurvePoint[]**](../Model/PlayerPerformanceCurvePoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `playerScoreboard()`

```php
playerScoreboard($sort_by, $sort_direction, $game_mode, $hero_id, $min_matches, $max_matches, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $start, $limit, $account_ids): \OpenAPI\Client\Model\Entry[]
```

Player Scoreboard

This endpoint returns the player scoreboard.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$sort_by = 'sort_by_example'; // string | The field to sort by.
$sort_direction = 'sort_direction_example'; // string | The direction to sort players in.
$game_mode = 'game_mode_example'; // string | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
$hero_id = 56; // int | Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
$min_matches = 20; // int | The minimum number of matches played for a player to be included in the scoreboard.
$max_matches = 56; // int | The maximum number of matches played for a hero combination to be included in the response.
$min_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$min_networth = 56; // int | Filter players based on their final net worth.
$max_networth = 56; // int | Filter players based on their final net worth.
$min_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$max_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.
$start = 56; // int | The offset to start fetching players from.
$limit = 100; // int | The maximum number of players to fetch.
$account_ids = array(56); // int[] | Comma separated list of account ids to include

try {
    $result = $apiInstance->playerScoreboard($sort_by, $sort_direction, $game_mode, $hero_id, $min_matches, $max_matches, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $start, $limit, $account_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->playerScoreboard: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **sort_by** | **string**| The field to sort by. | |
| **sort_direction** | **string**| The direction to sort players in. | [optional] |
| **game_mode** | **string**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] |
| **hero_id** | **int**| Filter matches based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **min_matches** | **int**| The minimum number of matches played for a player to be included in the scoreboard. | [optional] [default to 20] |
| **max_matches** | **int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **min_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **max_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **start** | **int**| The offset to start fetching players from. | [optional] |
| **limit** | **int**| The maximum number of players to fetch. | [optional] [default to 100] |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**\OpenAPI\Client\Model\Entry[]**](../Model/Entry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `playerStatsMetrics()`

```php
playerStatsMetrics($hero_ids, $game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $max_matches, $include_item_ids, $exclude_item_ids, $account_ids): array<string,\OpenAPI\Client\Model\HashMapValue>
```

Player Stats Metrics

Returns comprehensive statistical analysis of player performance.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  > Note: Quantiles are calculated using the [DDSketch](https://www.vldb.org/pvldb/vol12/p2195-masson.pdf) algorithm, so they are not exact but have a maximum relative error of 0.01.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$hero_ids = 'hero_ids_example'; // string | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes>
$game_mode = 'game_mode_example'; // string | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`.
$min_unix_timestamp = 1768867200; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$min_networth = 56; // int | Filter players based on their final net worth.
$max_networth = 56; // int | Filter players based on their final net worth.
$min_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$max_average_badge = 56; // int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.
$max_matches = 56; // int | The maximum number of matches to analyze.
$include_item_ids = array(56); // int[] | Comma separated list of item ids to include (only players who have purchased these items). See more: <https://assets.deadlock-api.com/v2/items>
$exclude_item_ids = array(56); // int[] | Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://assets.deadlock-api.com/v2/items>
$account_ids = array(56); // int[] | Comma separated list of account ids to include

try {
    $result = $apiInstance->playerStatsMetrics($hero_ids, $game_mode, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $max_matches, $include_item_ids, $exclude_item_ids, $account_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->playerStatsMetrics: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **hero_ids** | **string**| Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] |
| **game_mode** | **string**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] |
| **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1768867200] |
| **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] |
| **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] |
| **min_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **max_networth** | **int**| Filter players based on their final net worth. | [optional] |
| **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] |
| **min_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_match_id** | **int**| Filter matches based on their ID. | [optional] |
| **max_matches** | **int**| The maximum number of matches to analyze. | [optional] |
| **include_item_ids** | [**int[]**](../Model/int.md)| Comma separated list of item ids to include (only players who have purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] |
| **exclude_item_ids** | [**int[]**](../Model/int.md)| Comma separated list of item ids to exclude (only players who have not purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] |
| **account_ids** | [**int[]**](../Model/int.md)| Comma separated list of account ids to include | [optional] |

### Return type

[**array<string,\OpenAPI\Client\Model\HashMapValue>**](../Model/HashMapValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
