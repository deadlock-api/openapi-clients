# \AnalyticsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ability_order_stats**](AnalyticsApi.md#ability_order_stats) | **GET** /v1/analytics/ability-order-stats | Ability Order Stats
[**badge_distribution**](AnalyticsApi.md#badge_distribution) | **GET** /v1/analytics/badge-distribution | Badge Distribution
[**build_item_stats**](AnalyticsApi.md#build_item_stats) | **GET** /v1/analytics/build-item-stats | Build Item Stats
[**hero_comb_stats**](AnalyticsApi.md#hero_comb_stats) | **GET** /v1/analytics/hero-comb-stats | Hero Comb Stats
[**hero_counters_stats**](AnalyticsApi.md#hero_counters_stats) | **GET** /v1/analytics/hero-counter-stats | Hero Counter Stats
[**hero_scoreboard**](AnalyticsApi.md#hero_scoreboard) | **GET** /v1/analytics/scoreboards/heroes | Hero Scoreboard
[**hero_stats**](AnalyticsApi.md#hero_stats) | **GET** /v1/analytics/hero-stats | Hero Stats
[**hero_synergies_stats**](AnalyticsApi.md#hero_synergies_stats) | **GET** /v1/analytics/hero-synergy-stats | Hero Synergy Stats
[**item_permutation_stats**](AnalyticsApi.md#item_permutation_stats) | **GET** /v1/analytics/item-permutation-stats | Item Permutation Stats
[**item_stats**](AnalyticsApi.md#item_stats) | **GET** /v1/analytics/item-stats | Item Stats
[**player_scoreboard**](AnalyticsApi.md#player_scoreboard) | **GET** /v1/analytics/scoreboards/players | Player Scoreboard
[**player_stats_metrics**](AnalyticsApi.md#player_stats_metrics) | **GET** /v1/analytics/player-stats/metrics | Player Stats Metrics



## ability_order_stats

> Vec<models::AnalyticsAbilityOrderStats> ability_order_stats(hero_id, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_ability_upgrades, max_ability_upgrades, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, min_matches, account_id, account_ids)
Ability Order Stats

 Retrieves statistics for the ability order of a hero.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hero_id** | **u32** | See more: <https://assets.deadlock-api.com/v2/heroes> | [required] |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1757980800]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_ability_upgrades** | Option<**u64**> | Filter players based on their minimum number of ability upgrades over the whole match. |  |
**max_ability_upgrades** | Option<**u64**> | Filter players based on their maximum number of ability upgrades over the whole match. |  |
**min_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**min_matches** | Option<**u32**> | The minimum number of matches played for an ability order to be included in the response. |  |[default to 20]
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](u32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::AnalyticsAbilityOrderStats>**](AnalyticsAbilityOrderStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## badge_distribution

> Vec<models::BadgeDistribution> badge_distribution(min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, is_high_skill_range_parties, is_low_pri_pool, is_new_player_pool, min_match_id, max_match_id)
Badge Distribution

 This endpoint returns the player badge distribution.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1757980800]
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

 Retrieves item statistics from hero builds.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hero_id** | Option<**u32**> | Filter builds based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> |  |
**min_last_updated_unix_timestamp** | Option<**i64**> | Filter builds based on their last updated time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1757980800]
**max_last_updated_unix_timestamp** | Option<**i64**> | Filter builds based on their last updated time (Unix timestamp). |  |

### Return type

[**Vec<models::BuildItemStats>**](BuildItemStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## hero_comb_stats

> Vec<models::HeroCombStats> hero_comb_stats(min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, include_hero_ids, exclude_hero_ids, min_matches, max_matches, comb_size, account_id, account_ids)
Hero Comb Stats

 Retrieves overall statistics for each hero combination.  Results are cached for **1 hour**. The cache key is determined by the specific combination of filter parameters used in the query. Subsequent requests using the exact same filters within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1757980800]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**include_hero_ids** | Option<[**Vec<u32>**](u32.md)> | Comma separated list of hero ids to include. See more: <https://assets.deadlock-api.com/v2/heroes> |  |
**exclude_hero_ids** | Option<[**Vec<u32>**](u32.md)> | Comma separated list of hero ids to exclude. See more: <https://assets.deadlock-api.com/v2/heroes> |  |
**min_matches** | Option<**u32**> | The minimum number of matches played for a hero combination to be included in the response. |  |[default to 20]
**max_matches** | Option<**u32**> | The maximum number of matches played for a hero combination to be included in the response. |  |
**comb_size** | Option<**u32**> | The combination size to return. |  |[default to 6]
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](u32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::HeroCombStats>**](HeroCombStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## hero_counters_stats

> Vec<models::HeroCounterStats> hero_counters_stats(min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_enemy_networth, max_enemy_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, same_lane_filter, min_matches, max_matches, account_id, account_ids)
Hero Counter Stats

 Retrieves hero-versus-hero matchup statistics based on historical match data.  This endpoint analyzes completed matches to calculate how often a specific hero (`hero_id`) wins against an enemy hero (`enemy_hero_id`) and the total number of times they have faced each other under the specified filter conditions.  Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1757980800]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**min_enemy_networth** | Option<**u64**> | Filter enemy players based on their net worth. |  |
**max_enemy_networth** | Option<**u64**> | Filter enemy players based on their net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**same_lane_filter** | Option<**bool**> | When `true`, only considers matchups where both `hero_id` and `enemy_hero_id` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane. |  |[default to true]
**min_matches** | Option<**u64**> | The minimum number of matches played for a hero combination to be included in the response. |  |[default to 20]
**max_matches** | Option<**u32**> | The maximum number of matches played for a hero combination to be included in the response. |  |
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](u32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::HeroCounterStats>**](HeroCounterStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## hero_scoreboard

> Vec<models::Entry> hero_scoreboard(sort_by, sort_direction, min_matches, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, account_id, account_ids)
Hero Scoreboard

 This endpoint returns the hero scoreboard.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**sort_by** | **String** | The field to sort by. | [required] |
**sort_direction** | Option<**String**> | The direction to sort heroes in. |  |
**min_matches** | Option<**u32**> | Filter by min number of matches played. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1757980800]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](u32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::Entry>**](Entry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## hero_stats

> Vec<models::AnalyticsHeroStats> hero_stats(bucket, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, min_hero_matches, max_hero_matches, min_hero_matches_total, max_hero_matches_total, include_item_ids, exclude_item_ids, account_id, account_ids)
Hero Stats

 Retrieves performance statistics for each hero based on historical match data.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**bucket** | Option<**String**> | Bucket allows you to group the stats by a specific field. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1757980800]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**min_hero_matches** | Option<**u64**> | Filter players based on the number of matches they have played with a specific hero within the filtered time range. |  |
**max_hero_matches** | Option<**u64**> | Filter players based on the number of matches they have played with a specific hero within the filtered time range. |  |
**min_hero_matches_total** | Option<**u64**> | Filter players based on the number of matches they have played with a specific hero in their entire history. |  |
**max_hero_matches_total** | Option<**u64**> | Filter players based on the number of matches they have played with a specific hero in their entire history. |  |
**include_item_ids** | Option<[**Vec<u32>**](u32.md)> | Comma separated list of item ids to include (only heroes who have purchased these items). See more: <https://assets.deadlock-api.com/v2/items> |  |
**exclude_item_ids** | Option<[**Vec<u32>**](u32.md)> | Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: <https://assets.deadlock-api.com/v2/items> |  |
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](u32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::AnalyticsHeroStats>**](AnalyticsHeroStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## hero_synergies_stats

> Vec<models::HeroSynergyStats> hero_synergies_stats(min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, same_lane_filter, same_party_filter, min_matches, max_matches, account_id, account_ids)
Hero Synergy Stats

 Retrieves hero pair synergy statistics based on historical match data.  This endpoint analyzes completed matches to calculate how often a specific pair of heroes (`hero_id1` and `hero_id2`) won when playing *together on the same team*, and the total number of times they have played together under the specified filter conditions.  Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1757980800]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**same_lane_filter** | Option<**bool**> | When `true`, only considers matchups where both `hero_id1` and `hero_id2` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane. |  |[default to true]
**same_party_filter** | Option<**bool**> | When `true`, only considers matchups where both `hero_id` and `hero_id2` were on the same party. When `false`, considers all matchups regardless of party affiliation. |  |[default to true]
**min_matches** | Option<**u64**> | The minimum number of matches played for a hero combination to be included in the response. |  |[default to 20]
**max_matches** | Option<**u32**> | The maximum number of matches played for a hero combination to be included in the response. |  |
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](u32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::HeroSynergyStats>**](HeroSynergyStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## item_permutation_stats

> Vec<models::ItemPermutationStats> item_permutation_stats(item_ids, comb_size, hero_ids, hero_id, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, account_id, account_ids)
Item Permutation Stats

 Retrieves item permutation statistics based on historical match data.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**item_ids** | Option<[**Vec<u32>**](u32.md)> | Comma separated list of item ids. See more: <https://assets.deadlock-api.com/v2/items> |  |
**comb_size** | Option<**u32**> | The combination size to return. |  |[default to 2]
**hero_ids** | Option<**String**> | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> |  |
**hero_id** | Option<**u32**> | Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1757980800]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](u32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::ItemPermutationStats>**](ItemPermutationStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## item_stats

> Vec<models::ItemStats> item_stats(bucket, hero_ids, hero_id, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, include_item_ids, exclude_item_ids, min_matches, max_matches, account_id, account_ids)
Item Stats

 Retrieves item statistics based on historical match data.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**bucket** | Option<**String**> | Bucket allows you to group the stats by a specific field. |  |
**hero_ids** | Option<**String**> | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> |  |
**hero_id** | Option<**u32**> | Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1757980800]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**include_item_ids** | Option<[**Vec<u32>**](u32.md)> | Comma separated list of item ids to include. See more: <https://assets.deadlock-api.com/v2/items> |  |
**exclude_item_ids** | Option<[**Vec<u32>**](u32.md)> | Comma separated list of item ids to exclude. See more: <https://assets.deadlock-api.com/v2/items> |  |
**min_matches** | Option<**u32**> | The minimum number of matches played for an item to be included in the response. |  |[default to 20]
**max_matches** | Option<**u32**> | The maximum number of matches played for a hero combination to be included in the response. |  |
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](u32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::ItemStats>**](ItemStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## player_scoreboard

> Vec<models::Entry> player_scoreboard(sort_by, sort_direction, hero_id, min_matches, max_matches, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, start, limit, account_ids)
Player Scoreboard

 This endpoint returns the player scoreboard.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**sort_by** | **String** | The field to sort by. | [required] |
**sort_direction** | Option<**String**> | The direction to sort players in. |  |
**hero_id** | Option<**u32**> | Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> |  |
**min_matches** | Option<**u32**> | The minimum number of matches played for a player to be included in the scoreboard. |  |[default to 20]
**max_matches** | Option<**u32**> | The maximum number of matches played for a hero combination to be included in the response. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**start** | Option<**u32**> | The offset to start fetching players from. |  |
**limit** | Option<**u32**> | The maximum number of players to fetch. |  |[default to 100]
**account_ids** | Option<[**Vec<u32>**](u32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::Entry>**](Entry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## player_stats_metrics

> std::collections::HashMap<String, models::HashMapValue> player_stats_metrics(hero_ids, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, max_matches, include_item_ids, exclude_item_ids, account_ids)
Player Stats Metrics

 Returns comprehensive statistical analysis of player performance.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  > Note: Quantiles are calculated using the [DDSketch](https://www.vldb.org/pvldb/vol12/p2195-masson.pdf) algorithm, so they are not exact but have a maximum relative error of 0.01.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hero_ids** | Option<**String**> | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1757980800]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_matches** | Option<**u32**> | The maximum number of matches to analyze. |  |
**include_item_ids** | Option<[**Vec<u32>**](u32.md)> | Comma separated list of item ids to include (only heroes who have purchased these items). See more: <https://assets.deadlock-api.com/v2/items> |  |
**exclude_item_ids** | Option<[**Vec<u32>**](u32.md)> | Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: <https://assets.deadlock-api.com/v2/items> |  |
**account_ids** | Option<[**Vec<u32>**](u32.md)> | Comma separated list of account ids to include |  |

### Return type

[**std::collections::HashMap<String, models::HashMapValue>**](HashMap_value.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

