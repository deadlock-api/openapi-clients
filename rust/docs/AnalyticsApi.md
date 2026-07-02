# \AnalyticsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ability_order_stats**](AnalyticsApi.md#ability_order_stats) | **GET** /v1/analytics/ability-order-stats | Ability Order Stats
[**badge_distribution**](AnalyticsApi.md#badge_distribution) | **GET** /v1/analytics/badge-distribution | Badge Distribution
[**build_item_stats**](AnalyticsApi.md#build_item_stats) | **GET** /v1/analytics/build-item-stats | Build Item Stats
[**game_stats**](AnalyticsApi.md#game_stats) | **GET** /v1/analytics/game-stats | Game Stats
[**hero_ban_stats**](AnalyticsApi.md#hero_ban_stats) | **GET** /v1/analytics/hero-ban-stats | Hero Ban Stats
[**hero_build_stats**](AnalyticsApi.md#hero_build_stats) | **GET** /v1/analytics/hero-build-stats/{hero_id} | Hero Build Stats
[**hero_comb_stats**](AnalyticsApi.md#hero_comb_stats) | **GET** /v1/analytics/hero-comb-stats | Hero Comb Stats
[**hero_counters_stats**](AnalyticsApi.md#hero_counters_stats) | **GET** /v1/analytics/hero-counter-stats | Hero Counter Stats
[**hero_scoreboard**](AnalyticsApi.md#hero_scoreboard) | **GET** /v1/analytics/scoreboards/heroes | Hero Scoreboard
[**hero_stats**](AnalyticsApi.md#hero_stats) | **GET** /v1/analytics/hero-stats | Hero Stats
[**hero_synergies_stats**](AnalyticsApi.md#hero_synergies_stats) | **GET** /v1/analytics/hero-synergy-stats | Hero Synergy Stats
[**item_flow_stats**](AnalyticsApi.md#item_flow_stats) | **GET** /v1/analytics/item-flow-stats | Item Flow Stats
[**item_permutation_stats**](AnalyticsApi.md#item_permutation_stats) | **GET** /v1/analytics/item-permutation-stats | Item Permutation Stats
[**item_stats**](AnalyticsApi.md#item_stats) | **GET** /v1/analytics/item-stats | Item Stats
[**kill_death_stats**](AnalyticsApi.md#kill_death_stats) | **GET** /v1/analytics/kill-death-stats | Kill Death Stats
[**player_performance_curve**](AnalyticsApi.md#player_performance_curve) | **GET** /v1/analytics/player-performance-curve | Player Performance Curve
[**player_scoreboard**](AnalyticsApi.md#player_scoreboard) | **GET** /v1/analytics/scoreboards/players | Player Scoreboard
[**player_stats_metrics**](AnalyticsApi.md#player_stats_metrics) | **GET** /v1/analytics/player-stats/metrics | Player Stats Metrics



## ability_order_stats

> Vec<models::AnalyticsAbilityOrderStats> ability_order_stats(hero_id, game_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_ability_upgrades, max_ability_upgrades, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, min_matches, account_id, account_ids, include_item_ids, exclude_item_ids)
Ability Order Stats

 Retrieves statistics for the ability order of a hero.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hero_id** | **u32** | See more: <https://api.deadlock-api.com/v1/assets/heroes> | [required] |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1780272000]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_ability_upgrades** | Option<**u64**> | Filter players based on their minimum number of ability upgrades over the whole match. |  |
**max_ability_upgrades** | Option<**u64**> | Filter players based on their maximum number of ability upgrades over the whole match. |  |
**min_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**min_matches** | Option<**u32**> | The minimum number of matches played for an ability order to be included in the response. |  |[default to 20]
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |
**include_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to include (only players who have purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**exclude_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |

### Return type

[**Vec<models::AnalyticsAbilityOrderStats>**](AnalyticsAbilityOrderStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## badge_distribution

> Vec<models::BadgeDistribution> badge_distribution(game_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, is_high_skill_range_parties, is_low_pri_pool, is_new_player_pool, min_match_id, max_match_id)
Badge Distribution

 This endpoint returns the player badge distribution.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1780272000]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**is_high_skill_range_parties** | Option<**bool**> | Filter matches based on whether they are in the high skill range. |  |
**is_low_pri_pool** | Option<**bool**> | Filter matches based on whether they are in the low priority pool. |  |
**is_new_player_pool** | Option<**bool**> | Filter matches based on whether they are in the new player pool. |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |

### Return type

[**Vec<models::BadgeDistribution>**](BadgeDistribution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## build_item_stats

> Vec<models::BuildItemStats> build_item_stats(hero_id, min_last_updated_unix_timestamp, max_last_updated_unix_timestamp)
Build Item Stats

 Retrieves item statistics from hero builds.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hero_id** | Option<**u32**> | Filter builds based on the hero ID. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**min_last_updated_unix_timestamp** | Option<**i64**> | Filter builds based on their last updated time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1780272000]
**max_last_updated_unix_timestamp** | Option<**i64**> | Filter builds based on their last updated time (Unix timestamp). |  |

### Return type

[**Vec<models::BuildItemStats>**](BuildItemStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## game_stats

> Vec<models::AnalyticsGameStats> game_stats(bucket, game_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_average_badge, max_average_badge, min_match_id, max_match_id, min_networth, max_networth, hero_ids, include_item_ids, exclude_item_ids, account_ids)
Game Stats

 Retrieves aggregate game-level statistics.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**bucket** | Option<**String**> | Bucket allows you to group the stats by a specific field. |  |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1780272000]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> Only works for `game_modes` with badge data (e.g. `normal`, not `street_brawl`). |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> Only works for `game_modes` with badge data (e.g. `normal`, not `street_brawl`). |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**min_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**hero_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of hero ids to include. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**include_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to include (only players who have purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**exclude_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::AnalyticsGameStats>**](AnalyticsGameStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## hero_ban_stats

> Vec<models::HeroBanStats> hero_ban_stats(bucket, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_average_badge, max_average_badge, min_match_id, max_match_id)
Hero Ban Stats

 Retrieves ban statistics for each hero based on historical match data from demo analysis.  Only matches with successfully extracted ban data are included. Matches where ban extraction failed (empty `banned_hero_ids`) are excluded entirely.  Results are cached for **1 hour** based on the combination of query parameters provided.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**bucket** | Option<**String**> | Bucket allows you to group the stats by a specific field. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. **Minimum:** March 1, 2026. |  |[default to 1780272000]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |

### Return type

[**Vec<models::HeroBanStats>**](HeroBanStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## hero_build_stats

> Vec<models::HeroBuildStats> hero_build_stats(hero_id, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_average_badge, max_average_badge, min_match_id, max_match_id, hero_build_id, min_matches, account_id, account_ids)
Hero Build Stats

 Retrieves performance statistics for hero builds based on historical match data from demo analysis.  Only includes builds that exist in the hero builds database.  The `hero_build_id` is the first build the player had selected when the game started. It does not reflect any build changes made during the match.  Results are cached for **1 hour** based on the combination of query parameters provided.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hero_id** | **u32** | The hero ID to fetch build stats for. See more: <https://api.deadlock-api.com/v1/assets/heroes> | [required] |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. **Minimum:** March 1, 2026. |  |[default to 1780272000]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**hero_build_id** | Option<**u64**> | Filter results for a specific hero build. |  |
**min_matches** | Option<**u64**> | The minimum number of matches played for a build to be included in the response. |  |[default to 20]
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::HeroBuildStats>**](HeroBuildStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## hero_comb_stats

> Vec<models::HeroCombStats> hero_comb_stats(game_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, include_hero_ids, exclude_hero_ids, include_enemy_hero_ids, exclude_enemy_hero_ids, min_matches, max_matches, comb_size, account_id, account_ids)
Hero Comb Stats

 Retrieves overall statistics for each hero combination.  Results are cached for **1 hour**. The cache key is determined by the specific combination of filter parameters used in the query. Subsequent requests using the exact same filters within this timeframe will receive the cached response.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1780272000]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**include_hero_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of hero ids to include. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**exclude_hero_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of hero ids to exclude. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**include_enemy_hero_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of enemy hero ids to include. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**exclude_enemy_hero_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of enemy hero ids to exclude. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**min_matches** | Option<**u32**> | The minimum number of matches played for a hero combination to be included in the response. |  |[default to 20]
**max_matches** | Option<**u32**> | The maximum number of matches played for a hero combination to be included in the response. |  |
**comb_size** | Option<**u32**> | The combination size to return. |  |[default to 6]
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::HeroCombStats>**](HeroCombStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## hero_counters_stats

> Vec<models::HeroCounterStats> hero_counters_stats(game_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_enemy_networth, max_enemy_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, same_lane_filter, min_matches, max_matches, account_id, account_ids)
Hero Counter Stats

 Retrieves hero-versus-hero matchup statistics based on historical match data.  This endpoint analyzes completed matches to calculate how often a specific hero (`hero_id`) wins against an enemy hero (`enemy_hero_id`) and the total number of times they have faced each other under the specified filter conditions.  Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1780272000]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**min_enemy_networth** | Option<**u64**> | Filter enemy players based on their net worth. |  |
**max_enemy_networth** | Option<**u64**> | Filter enemy players based on their net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**same_lane_filter** | Option<**bool**> | When `true`, only considers matchups where both `hero_id` and `enemy_hero_id` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane. |  |[default to true]
**min_matches** | Option<**u64**> | The minimum number of matches played for a hero combination to be included in the response. |  |[default to 20]
**max_matches** | Option<**u32**> | The maximum number of matches played for a hero combination to be included in the response. |  |
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::HeroCounterStats>**](HeroCounterStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## hero_scoreboard

> Vec<models::HeroEntry> hero_scoreboard(sort_by, sort_direction, game_mode, min_matches, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, account_id, account_ids)
Hero Scoreboard

 This endpoint returns the hero scoreboard.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**sort_by** | **String** | The field to sort by. | [required] |
**sort_direction** | Option<**String**> | The direction to sort heroes in. |  |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**min_matches** | Option<**u32**> | Filter by min number of matches played. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1780272000]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::HeroEntry>**](HeroEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## hero_stats

> Vec<models::AnalyticsHeroStats> hero_stats(bucket, game_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, min_hero_matches, max_hero_matches, min_hero_matches_total, max_hero_matches_total, include_item_ids, exclude_item_ids, account_id, account_ids)
Hero Stats

 Retrieves performance statistics for each hero based on historical match data.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**bucket** | Option<**String**> | Bucket allows you to group the stats by a specific field. |  |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1780272000]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**min_hero_matches** | Option<**u64**> | Filter players based on the number of matches they have played with a specific hero within the filtered time range. |  |
**max_hero_matches** | Option<**u64**> | Filter players based on the number of matches they have played with a specific hero within the filtered time range. |  |
**min_hero_matches_total** | Option<**u64**> | Filter players based on the number of matches they have played with a specific hero in their entire history. |  |
**max_hero_matches_total** | Option<**u64**> | Filter players based on the number of matches they have played with a specific hero in their entire history. |  |
**include_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to include (only players who have purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**exclude_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::AnalyticsHeroStats>**](AnalyticsHeroStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## hero_synergies_stats

> Vec<models::HeroSynergyStats> hero_synergies_stats(game_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, same_lane_filter, min_matches, max_matches, account_id, account_ids)
Hero Synergy Stats

 Retrieves hero pair synergy statistics based on historical match data.  This endpoint analyzes completed matches to calculate how often a specific pair of heroes (`hero_id1` and `hero_id2`) won when playing *together on the same team*, and the total number of times they have played together under the specified filter conditions.  Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1780272000]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**same_lane_filter** | Option<**bool**> | When `true`, only considers matchups where both `hero_id1` and `hero_id2` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane. |  |[default to true]
**min_matches** | Option<**u64**> | The minimum number of matches played for a hero combination to be included in the response. |  |[default to 20]
**max_matches** | Option<**u32**> | The maximum number of matches played for a hero combination to be included in the response. |  |
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::HeroSynergyStats>**](HeroSynergyStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## item_flow_stats

> models::ItemFlowStats item_flow_stats(phase_interval_s, phase_count, game_mode, hero_ids, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, min_matches, account_ids, include_item_ids, exclude_item_ids, locked_item_ids, locked_columns)
Item Flow Stats

 Retrieves item build-flow statistics: per-phase item win/pick rates and the transitions between them.  Items are grouped into columns by the in-match phase they were bought in (controlled by `phase_interval_s` and `phase_count`). The response contains `nodes` (items aggregated within a phase) and `edges` (transitions between an item and items in the next phase). A locked build path can be supplied via `locked_item_ids` / `locked_columns` to restrict the population to players who bought those items in the given stage columns.  Each node also carries `adjusted_win_rate`: the item's win rate standardized to the stage's net-worth-at-buy distribution. Because players who are already ahead have more souls and buy items sooner, raw win rate is heavily confounded by wealth; the adjusted figure re-weights each item's win rate across net-worth buckets to the stage-wide distribution, isolating the item's contribution from the buyer's lead. It is still observational, not a controlled/causal estimate. `reached_per_column` gives the distinct baseline games that bought any upgrade in each column, so consumers can show how survivorship-selected (e.g. long-game-only) a late stage is.  Results are cached for **1 hour** based on the unique combination of query parameters provided.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**phase_interval_s** | Option<**u32**> | Deprecated/unused. `normal` mode uses fixed phase boundaries (0-9m, 9-20m, 20-30m, 30m+) aligned to the stats time-series; `street_brawl` columns are rounds. |  |[default to 600]
**phase_count** | Option<**u32**> | Number of columns for `street_brawl` (rounds). Ignored for `normal`, which has fixed time phases. **Default:** 4. |  |[default to 4]
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**hero_ids** | Option<**String**> | Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1780272000]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**min_matches** | Option<**u32**> | The minimum number of matches for a node or edge to be included in the response. |  |[default to 20]
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |
**include_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to include (only players who have purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**exclude_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**locked_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids forming a \"locked\" build path. Pairs positionally with `locked_columns`: the i-th item must have been bought in the i-th `locked_columns` stage. See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**locked_columns** | Option<[**Vec<u32>**](U32.md)> | Comma separated 0-based stage column indices for each `locked_item_ids` entry (time phase for `normal`, round for `street_brawl`). Must have the same length as `locked_item_ids`. |  |

### Return type

[**models::ItemFlowStats**](ItemFlowStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## item_permutation_stats

> Vec<models::ItemPermutationStats> item_permutation_stats(item_ids, comb_size, game_mode, hero_ids, hero_id, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, account_id, account_ids)
Item Permutation Stats

 Retrieves item permutation statistics based on historical match data.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids. See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**comb_size** | Option<**u32**> | The combination size to return. |  |[default to 2]
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**hero_ids** | Option<**String**> | Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**hero_id** | Option<**u32**> | Filter matches based on the hero ID. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1780272000]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::ItemPermutationStats>**](ItemPermutationStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## item_stats

> Vec<models::ItemStats> item_stats(bucket, game_mode, hero_ids, hero_id, enemy_hero_ids, enemy_hero_ids_all_match, min_enemy_networth, max_enemy_networth, same_lane_filter, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, include_item_ids, exclude_item_ids, min_matches, max_matches, account_id, account_ids, min_bought_at_s, max_bought_at_s, item_order)
Item Stats

 Retrieves item statistics based on historical match data.  Results are cached for **6 hours** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**bucket** | Option<**String**> | Bucket allows you to group the stats by a specific field. |  |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**hero_ids** | Option<**String**> | Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**hero_id** | Option<**u32**> | Filter matches based on the hero ID. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**enemy_hero_ids** | Option<**String**> | Filter to matches where one or more of these heroes were on the opposing team. Comma separated. When set, returns \"what items beat hero(es) X?\" stats. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**enemy_hero_ids_all_match** | Option<**bool**> | When `true`, requires *all* of the specified `enemy_hero_ids` to be on the same enemy team. When `false` (default), matches if *any* of the specified hero(es) are on the enemy team. Ignored when `enemy_hero_ids` is unset. |  |
**min_enemy_networth** | Option<**u64**> | Filter the specified enemy hero(es) by their final net worth. Ignored when `enemy_hero_ids` is unset. |  |
**max_enemy_networth** | Option<**u64**> | Filter the specified enemy hero(es) by their final net worth. Ignored when `enemy_hero_ids` is unset. |  |
**same_lane_filter** | Option<**bool**> | When `true`, only counts buyers in the same `assigned_lane` as one of the specified enemy heroes. Ignored when `enemy_hero_ids` is unset. **Default:** `false`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1780272000]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**include_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to include. See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**exclude_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to exclude. See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**min_matches** | Option<**u32**> | The minimum number of matches played for an item to be included in the response. |  |[default to 20]
**max_matches** | Option<**u32**> | The maximum number of matches played for a hero combination to be included in the response. |  |
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |
**min_bought_at_s** | Option<**u32**> | Filter items bought after this game time (seconds). |  |
**max_bought_at_s** | Option<**u32**> | Filter items bought before this game time (seconds). |  |
**item_order** | Option<[**Vec<String>**](String.md)> | Filter by purchase order. Each value is a comma-separated, ordered list of item ids (e.g. `1396247347,3977876567`). This is a *constraint*, not an inclusion filter: for each adjacent pair in the list, a match is excluded only when the player bought **both** items but bought the later one first. Builds missing either item are unaffected. Repeat the parameter for multiple independent orderings. See more: <https://api.deadlock-api.com/v1/assets/items> |  |

### Return type

[**Vec<models::ItemStats>**](ItemStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## kill_death_stats

> Vec<models::KillDeathStats> kill_death_stats(team, game_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, account_ids, hero_ids, min_networth, max_networth, is_high_skill_range_parties, is_low_pri_pool, is_new_player_pool, min_match_id, max_match_id, min_average_badge, max_average_badge, min_kills_per_raster, max_kills_per_raster, min_deaths_per_raster, max_deaths_per_raster, min_game_time_s, max_game_time_s)
Kill Death Stats

 This endpoint returns the kill-death statistics across a 128x128 pixel raster.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**team** | Option<**u32**> | Filter by team number. |  |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1780272000]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Filter matches by account IDs of players that participated in the match. |  |
**hero_ids** | Option<**String**> | Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**min_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**is_high_skill_range_parties** | Option<**bool**> | Filter matches based on whether they are in the high skill range. |  |
**is_low_pri_pool** | Option<**bool**> | Filter matches based on whether they are in the low priority pool. |  |
**is_new_player_pool** | Option<**bool**> | Filter matches based on whether they are in the new player pool. |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_kills_per_raster** | Option<**u32**> | Filter Raster cells based on minimum kills. |  |
**max_kills_per_raster** | Option<**u32**> | Filter Raster cells based on maximum kills. |  |
**min_deaths_per_raster** | Option<**u32**> | Filter Raster cells based on minimum deaths. |  |
**max_deaths_per_raster** | Option<**u32**> | Filter Raster cells based on maximum deaths. |  |
**min_game_time_s** | Option<**u32**> | Filter kills based on their game time. |  |
**max_game_time_s** | Option<**u32**> | Filter kills based on their game time. |  |

### Return type

[**Vec<models::KillDeathStats>**](KillDeathStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## player_performance_curve

> Vec<models::PlayerPerformanceCurvePoint> player_performance_curve(resolution, game_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, hero_ids, include_item_ids, exclude_item_ids, account_ids)
Player Performance Curve

 Retrieves player performance statistics (net worth, kills, deaths, assists) over time throughout matches.  Results are cached for **1 hour** based on the unique combination of query parameters provided.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**resolution** | Option<**u32**> | Resolution for relative game times in percent (0-100). **Default:** 10 (buckets of 10%). Set to **0** to use absolute game time (seconds). |  |[default to 10]
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1780272000]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**hero_ids** | Option<**String**> | Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**include_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to include (only players who have purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**exclude_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::PlayerPerformanceCurvePoint>**](PlayerPerformanceCurvePoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## player_scoreboard

> Vec<models::PlayerEntry> player_scoreboard(sort_by, sort_direction, game_mode, hero_id, min_matches, max_matches, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, start, limit, account_ids)
Player Scoreboard

 This endpoint returns the player scoreboard.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**sort_by** | **String** | The field to sort by. | [required] |
**sort_direction** | Option<**String**> | The direction to sort players in. |  |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**hero_id** | Option<**u32**> | Filter matches based on the hero ID. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**min_matches** | Option<**u32**> | The minimum number of matches played for a player to be included in the scoreboard. |  |[default to 20]
**max_matches** | Option<**u32**> | The maximum number of matches played for a hero combination to be included in the response. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**start** | Option<**u32**> | The offset to start fetching players from. |  |
**limit** | Option<**u32**> | The maximum number of players to fetch. |  |[default to 100]
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::PlayerEntry>**](PlayerEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## player_stats_metrics

> std::collections::HashMap<String, models::HashMapValue> player_stats_metrics(hero_ids, game_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, max_matches, include_item_ids, exclude_item_ids, account_ids)
Player Stats Metrics

 Returns comprehensive statistical analysis of player performance.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  > Note: Quantiles are calculated using the [DDSketch](https://www.vldb.org/pvldb/vol12/p2195-masson.pdf) algorithm, so they are not exact but have a maximum relative error of 0.01.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hero_ids** | Option<**String**> | Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1780272000]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_matches** | Option<**u32**> | The maximum number of matches to analyze. |  |
**include_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to include (only players who have purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**exclude_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |

### Return type

[**std::collections::HashMap<String, models::HashMapValue>**](HashMap_value.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

