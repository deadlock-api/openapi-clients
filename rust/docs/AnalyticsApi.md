# \AnalyticsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ability_max_first_stats**](AnalyticsApi.md#ability_max_first_stats) | **GET** /v1/analytics/ability-max-first-stats | Ability Max First Stats
[**ability_order_stats**](AnalyticsApi.md#ability_order_stats) | **GET** /v1/analytics/ability-order-stats | Ability Order Stats
[**ability_order_tree**](AnalyticsApi.md#ability_order_tree) | **GET** /v1/analytics/ability-order-tree | Ability Order Tree
[**badge_distribution**](AnalyticsApi.md#badge_distribution) | **GET** /v1/analytics/badge-distribution | Badge Distribution
[**buff_stats**](AnalyticsApi.md#buff_stats) | **GET** /v1/analytics/buff-stats | Buff Stats
[**build_item_stats**](AnalyticsApi.md#build_item_stats) | **GET** /v1/analytics/build-item-stats | Build Item Stats
[**game_stats**](AnalyticsApi.md#game_stats) | **GET** /v1/analytics/game-stats | Game Stats
[**hero_ban_stats**](AnalyticsApi.md#hero_ban_stats) | **GET** /v1/analytics/hero-ban-stats | Hero Ban Stats
[**hero_build_stats**](AnalyticsApi.md#hero_build_stats) | **GET** /v1/analytics/hero-build-stats/{hero_id} | Hero Build Stats
[**hero_comb_stats**](AnalyticsApi.md#hero_comb_stats) | **GET** /v1/analytics/hero-comb-stats | Hero Comb Stats
[**hero_counters_stats**](AnalyticsApi.md#hero_counters_stats) | **GET** /v1/analytics/hero-counter-stats | Hero Counter Stats
[**hero_scoreboard**](AnalyticsApi.md#hero_scoreboard) | **GET** /v1/analytics/scoreboards/heroes | Hero Scoreboard
[**hero_stats**](AnalyticsApi.md#hero_stats) | **GET** /v1/analytics/hero-stats | Hero Stats
[**hero_swap_stats**](AnalyticsApi.md#hero_swap_stats) | **GET** /v1/analytics/hero-swap-stats | Hero Swap Stats
[**hero_synergies_stats**](AnalyticsApi.md#hero_synergies_stats) | **GET** /v1/analytics/hero-synergy-stats | Hero Synergy Stats
[**item_flow_stats**](AnalyticsApi.md#item_flow_stats) | **GET** /v1/analytics/item-flow-stats | Item Flow Stats
[**item_permutation_stats**](AnalyticsApi.md#item_permutation_stats) | **GET** /v1/analytics/item-permutation-stats | Item Permutation Stats
[**item_stats**](AnalyticsApi.md#item_stats) | **GET** /v1/analytics/item-stats | Item Stats
[**kill_death_stats**](AnalyticsApi.md#kill_death_stats) | **GET** /v1/analytics/kill-death-stats | Kill Death Stats
[**lane_matchup_stats**](AnalyticsApi.md#lane_matchup_stats) | **GET** /v1/analytics/lane-matchup-stats | Lane Matchup Stats (Subject to Change)
[**lane_soul_curve**](AnalyticsApi.md#lane_soul_curve) | **GET** /v1/analytics/lane-soul-curve | Lane Soul Curve (Subject to Change)
[**player_performance_curve**](AnalyticsApi.md#player_performance_curve) | **GET** /v1/analytics/player-performance-curve | Player Performance Curve
[**player_scoreboard**](AnalyticsApi.md#player_scoreboard) | **GET** /v1/analytics/scoreboards/players | Player Scoreboard
[**player_stats_metrics**](AnalyticsApi.md#player_stats_metrics) | **GET** /v1/analytics/player-stats/metrics | Player Stats Metrics



## ability_max_first_stats

> Vec<models::AnalyticsAbilityMaxFirstStats> ability_max_first_stats(hero_id, game_mode, match_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_ability_upgrades, max_ability_upgrades, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, min_matches, account_id, account_ids, hero_build_id, include_item_ids, exclude_item_ids, ability_order_prefix, ability_unlock_order_prefix)
Ability Max First Stats

 Retrieves which ability the players of a hero max first: one row per ability, with every player whose upgrade order unlocks and upgrades it three times before any other ability, and one row (`ability_id` null) for the players who maxed none. Every player is in exactly one row, so the rows add up to all the hero's players, and `min_matches` never drops the null row. Unlike summing `/ability-order-tree` nodes, no player is lost to `min_matches` on a rare order.  In `street_brawl`, ability points come in blocks, and the upgrades within one block are sorted by ability id.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hero_id** | **u32** | See more: <https://api.deadlock-api.com/v1/assets/heroes> | [required] |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1790380800]
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
**min_matches** | Option<**u32**> | The minimum number of matches played for an ability order (on `/ability-order-tree`: an order prefix, on `/ability-max-first-stats`: an ability) to be included in the response. |  |[default to 10]
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |
**hero_build_id** | Option<**u64**> | Only players who started the match with this hero build selected. Matches without a processed demo record no build. See more: <https://api.deadlock-api.com/v1/analytics/hero-build-stats/{hero_id}> |  |
**include_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to include (only players who have purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**exclude_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**ability_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats> |  |
**ability_unlock_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |

### Return type

[**Vec<models::AnalyticsAbilityMaxFirstStats>**](AnalyticsAbilityMaxFirstStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## ability_order_stats

> Vec<models::AnalyticsAbilityOrderStats> ability_order_stats(hero_id, game_mode, match_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_ability_upgrades, max_ability_upgrades, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, min_matches, account_id, account_ids, hero_build_id, include_item_ids, exclude_item_ids, ability_order_prefix, ability_unlock_order_prefix)
Ability Order Stats

 Retrieves statistics for the ability order of a hero.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hero_id** | **u32** | See more: <https://api.deadlock-api.com/v1/assets/heroes> | [required] |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1790380800]
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
**min_matches** | Option<**u32**> | The minimum number of matches played for an ability order (on `/ability-order-tree`: an order prefix, on `/ability-max-first-stats`: an ability) to be included in the response. |  |[default to 10]
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |
**hero_build_id** | Option<**u64**> | Only players who started the match with this hero build selected. Matches without a processed demo record no build. See more: <https://api.deadlock-api.com/v1/analytics/hero-build-stats/{hero_id}> |  |
**include_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to include (only players who have purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**exclude_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**ability_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats> |  |
**ability_unlock_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |

### Return type

[**Vec<models::AnalyticsAbilityOrderStats>**](AnalyticsAbilityOrderStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## ability_order_tree

> Vec<models::AnalyticsAbilityOrderTreeNode> ability_order_tree(hero_id, game_mode, match_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_ability_upgrades, max_ability_upgrades, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, min_matches, account_id, account_ids, hero_build_id, include_item_ids, exclude_item_ids, ability_order_prefix, ability_unlock_order_prefix)
Ability Order Tree

 Retrieves the ability upgrade orders of a hero as a tree: one node per order prefix, with the stats of every player whose order starts with it. `min_matches` applies to each node, so a node counts all its players even when their full orders are rare (which `/ability-order-stats`, grouping by full order, leaves out). A node's parent is always present.  In `street_brawl`, ability points come in blocks, and the upgrades within one block are sorted by ability id.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hero_id** | **u32** | See more: <https://api.deadlock-api.com/v1/assets/heroes> | [required] |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1790380800]
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
**min_matches** | Option<**u32**> | The minimum number of matches played for an ability order (on `/ability-order-tree`: an order prefix, on `/ability-max-first-stats`: an ability) to be included in the response. |  |[default to 10]
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |
**hero_build_id** | Option<**u64**> | Only players who started the match with this hero build selected. Matches without a processed demo record no build. See more: <https://api.deadlock-api.com/v1/analytics/hero-build-stats/{hero_id}> |  |
**include_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to include (only players who have purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**exclude_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**ability_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats> |  |
**ability_unlock_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |

### Return type

[**Vec<models::AnalyticsAbilityOrderTreeNode>**](AnalyticsAbilityOrderTreeNode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## badge_distribution

> Vec<models::BadgeDistribution> badge_distribution(game_mode, match_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, is_high_skill_range_parties, is_low_pri_pool, is_new_player_pool, min_match_id, max_match_id)
Badge Distribution

 This endpoint returns the player badge distribution.  `total_matches` counts matches by their average badge, while `unique_players` counts players by the rank Valve reported at the end of their latest ranked match within the filtered range. Since only ranked matches carry a rank, `unique_players` ignores the `match_mode` filter and always looks at ranked matches.  Ranks exist only from the first ranked season on, so `min_unix_timestamp` is clamped to its start.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). Values below the start of the first ranked season (1785430800) are clamped to it. **Default:** 30 days ago. |  |[default to 1790380800]
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


## buff_stats

> Vec<models::AnalyticsBuffStats> buff_stats(game_mode, match_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_average_badge, max_average_badge, min_match_id, max_match_id, min_networth, max_networth, hero_ids, account_ids)
Buff Stats

 Retrieves pickup statistics per power-up buff type (e.g. `hp_permanent_pickup_lv2`): how often players pick each one up and, for matches since build 6712 (2026-09-29), when they pick it up and how much stat it grants.  Pickup counts cover every match. Pickup times and stat values are only recorded since build 6712, so `timed_matches`, `timed_pickups`, `total_stat_value` and the average times only cover those matches. Temporary power-ups have no timings.  Buff display names, value units and graph colors: <https://api.deadlock-api.com/v1/assets/misc-entities>  Results are cached for **1 hour** based on the unique combination of query parameters provided.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1790380800]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**min_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**hero_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of hero ids to include. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::AnalyticsBuffStats>**](AnalyticsBuffStats.md)

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
**min_last_updated_unix_timestamp** | Option<**i64**> | Filter builds based on their last updated time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1790380800]
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

> Vec<models::AnalyticsGameStats> game_stats(bucket, game_mode, match_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_average_badge, max_average_badge, min_match_id, max_match_id, min_networth, max_networth, hero_ids, include_item_ids, exclude_item_ids, ability_order_prefix, ability_unlock_order_prefix, account_ids)
Game Stats

 Retrieves aggregate game-level statistics.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**bucket** | Option<**String**> | Bucket allows you to group the stats by a specific field. |  |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1790380800]
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
**ability_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats> |  |
**ability_unlock_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
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

> Vec<models::HeroBanStats> hero_ban_stats(match_mode, bucket, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_average_badge, max_average_badge, min_match_id, max_match_id)
Hero Ban Stats

 Retrieves ban statistics for each hero based on historical match data from demo analysis.  Only matches with successfully extracted ban data are included. `matches` counts them per bucket, so a hero's ban rate is `bans / matches`. Matches where ban extraction failed (empty `banned_hero_ids`) are excluded entirely.  Results are cached for **1 hour** based on the combination of query parameters provided.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**bucket** | Option<**String**> | Bucket allows you to group the stats by a specific field. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. **Minimum:** March 1, 2026. |  |[default to 1790380800]
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

> Vec<models::HeroBuildStats> hero_build_stats(hero_id, match_mode, bucket, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_average_badge, max_average_badge, min_match_id, max_match_id, hero_build_id, include_performance, min_matches, account_id, account_ids, ability_order_prefix, ability_unlock_order_prefix)
Hero Build Stats

 Retrieves performance statistics for hero builds based on historical match data from demo analysis.  Only includes builds that exist in the hero builds database.  The `hero_build_id` is the first build the player had selected when the game started. It does not reflect any build changes made during the match.  Results are cached for **1 hour** based on the combination of query parameters provided.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hero_id** | **u32** | The hero ID to fetch build stats for. See more: <https://api.deadlock-api.com/v1/assets/heroes> | [required] |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**bucket** | Option<**String**> | Bucket allows you to group the stats by a specific field. `min_matches` applies to each build and bucket. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. **Minimum:** March 1, 2026. |  |[default to 1790380800]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**hero_build_id** | Option<**u64**> | Filter results for a specific hero build. |  |
**include_performance** | Option<**bool**> | Add the performance totals (kills, souls, damage, healing, accuracy, match length, average badge) to every build. They make the query read about three times as much data, so they are left out unless asked for. |  |
**min_matches** | Option<**u64**> | The minimum number of matches played for a build to be included in the response. |  |[default to 20]
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |
**ability_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats> |  |
**ability_unlock_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |

### Return type

[**Vec<models::HeroBuildStats>**](HeroBuildStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## hero_comb_stats

> Vec<models::HeroCombStats> hero_comb_stats(game_mode, match_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, include_hero_ids, exclude_hero_ids, include_enemy_hero_ids, exclude_enemy_hero_ids, min_matches, max_matches, comb_size, account_id, account_ids)
Hero Comb Stats

 Retrieves overall statistics for each hero combination.  Results are cached for **1 hour**. The cache key is determined by the specific combination of filter parameters used in the query. Subsequent requests using the exact same filters within this timeframe will receive the cached response.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1790380800]
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

> Vec<models::HeroCounterStats> hero_counters_stats(game_mode, match_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_enemy_networth, max_enemy_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, same_lane_filter, min_matches, max_matches, account_id, account_ids, hero_build_id)
Hero Counter Stats

 Retrieves hero-versus-hero matchup statistics based on historical match data.  This endpoint analyzes completed matches to calculate how often a specific hero (`hero_id`) wins against an enemy hero (`enemy_hero_id`) and the total number of times they have faced each other under the specified filter conditions.  Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1790380800]
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
**hero_build_id** | Option<**u64**> | Only matchups where `hero_id`'s player started the match with this hero build selected. Matches without a processed demo record no build. See more: <https://api.deadlock-api.com/v1/analytics/hero-build-stats/{hero_id}> |  |

### Return type

[**Vec<models::HeroCounterStats>**](HeroCounterStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## hero_scoreboard

> Vec<models::HeroEntry> hero_scoreboard(sort_by, sort_direction, game_mode, match_mode, min_matches, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, account_id, account_ids)
Hero Scoreboard

 This endpoint returns the hero scoreboard.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**sort_by** | **String** | The field to sort by. | [required] |
**sort_direction** | Option<**String**> | The direction to sort heroes in. |  |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**min_matches** | Option<**u32**> | Filter by min number of matches played. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1790380800]
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

> Vec<models::AnalyticsHeroStats> hero_stats(bucket, game_mode, match_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, min_hero_matches, max_hero_matches, min_hero_matches_total, max_hero_matches_total, include_item_ids, exclude_item_ids, ability_order_prefix, ability_unlock_order_prefix, account_id, account_ids)
Hero Stats

 Retrieves performance statistics for each hero based on historical match data.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**bucket** | Option<**String**> | Bucket allows you to group the stats by a specific field. |  |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1790380800]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**max_networth** | Option<**u64**> | Filter players based on their final net worth. |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**min_hero_matches** | Option<**u64**> | Filter players based on the number of matches they have played with a specific hero within the filtered time range (all durations, even with a duration filter). |  |
**max_hero_matches** | Option<**u64**> | Filter players based on the number of matches they have played with a specific hero within the filtered time range (all durations, even with a duration filter). |  |
**min_hero_matches_total** | Option<**u64**> | Filter players based on the number of matches they have played with a specific hero in their entire history, counting only matches of the selected `game_mode`. |  |
**max_hero_matches_total** | Option<**u64**> | Filter players based on the number of matches they have played with a specific hero in their entire history, counting only matches of the selected `game_mode`. |  |
**include_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to include (only players who have purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**exclude_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**ability_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats> |  |
**ability_unlock_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
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


## hero_swap_stats

> Vec<models::HeroSwapStats> hero_swap_stats(match_mode, bucket, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_average_badge, max_average_badge, min_match_id, max_match_id)
Hero Swap Stats

 Retrieves hero swap statistics for each hero based on historical match data from demo analysis.  A player swapped when the hero they had locked before the pre-game swap window (`pregame_hero_id`) differs from the hero they played. Only players whose pre-game hero was extracted from the demo are counted, so all fields share the same sample:  - **Swap-in rate:** `swapped_in / matches`, the share of this hero's players who swapped to it. - **Swap-in win rate:** `swapped_in_wins / swapped_in`. - **Swap-away rate:** `swapped_away / pregame_picks`, the share of players who had this hero locked and swapped away from it.  Results are cached for **1 hour** based on the combination of query parameters provided.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**bucket** | Option<**String**> | Bucket allows you to group the stats by a specific field. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. **Minimum:** March 1, 2026. |  |[default to 1790380800]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |

### Return type

[**Vec<models::HeroSwapStats>**](HeroSwapStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## hero_synergies_stats

> Vec<models::HeroSynergyStats> hero_synergies_stats(game_mode, match_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, same_lane_filter, min_matches, max_matches, account_id, account_ids)
Hero Synergy Stats

 Retrieves hero pair synergy statistics based on historical match data.  This endpoint analyzes completed matches to calculate how often a specific pair of heroes (`hero_id1` and `hero_id2`) won when playing *together on the same team*, and the total number of times they have played together under the specified filter conditions.  Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1790380800]
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

> models::ItemFlowStats item_flow_stats(phase_interval_s, phase_count, game_mode, match_mode, hero_ids, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, min_matches, account_ids, include_item_ids, exclude_item_ids, ability_order_prefix, ability_unlock_order_prefix, locked_item_ids, locked_columns)
Item Flow Stats

 Retrieves item build-flow statistics: per-phase item win/pick rates and the transitions between them.  Items are grouped into columns by the in-match phase they were bought in: fixed time phases (0-9m, 9-20m, 20-30m, 30m+) for `normal`, `phase_count` rounds for `street_brawl`. The response contains `nodes` (items aggregated within a phase) and `edges` (transitions between an item and items in the next phase). A locked build path can be supplied via `locked_item_ids` / `locked_columns` to restrict the population to players who bought those items in the given stage columns.  Each node also carries `adjusted_win_rate`: the item's win rate standardized to the stage's net-worth-at-buy distribution. Because players who are already ahead have more souls and buy items sooner, raw win rate is heavily confounded by wealth; the adjusted figure re-weights each item's win rate across net-worth buckets to the stage-wide distribution, isolating the item's contribution from the buyer's lead. It is still observational, not a controlled/causal estimate. `reached_per_column` gives the distinct baseline games that bought any upgrade in each column, so consumers can show how survivorship-selected (e.g. long-game-only) a late stage is; `reached_wins_per_column` counts the won ones among them, the win rate a build ending in that stage should be compared with. `summary_reached_per_column` and `summary_reached_wins_per_column` count the same over the locked build path's games, the win rate an item bought in that stage should be compared with.  Corrupted items (build 6712+, same item id as the normal item) are not counted as purchases; the normal item they replaced still is.  Results are cached for **1 hour** based on the unique combination of query parameters provided.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**phase_interval_s** | Option<**u32**> | Deprecated/unused. `normal` mode uses fixed phase boundaries (0-9m, 9-20m, 20-30m, 30m+) aligned to the stats time-series; `street_brawl` columns are rounds. |  |[default to 600]
**phase_count** | Option<**u32**> | Number of columns for `street_brawl` (rounds). Ignored for `normal`, which has fixed time phases. **Default:** 4. |  |[default to 4]
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**hero_ids** | Option<**String**> | Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1790380800]
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
**ability_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats> |  |
**ability_unlock_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
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

> Vec<models::ItemPermutationStats> item_permutation_stats(item_ids, comb_size, min_matches, max_matches, game_mode, match_mode, hero_ids, hero_id, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, account_id, account_ids, ability_order_prefix, ability_unlock_order_prefix, include_corrupted_items)
Item Permutation Stats

 Retrieves item permutation statistics based on historical match data.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids. See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**comb_size** | Option<**u32**> | The combination size to return. |  |[default to 2]
**min_matches** | Option<**u32**> | The minimum number of matches for an item combination to be included in the response. |  |[default to 20]
**max_matches** | Option<**u32**> | The maximum number of matches for an item combination to be included in the response. |  |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**hero_ids** | Option<**String**> | Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**hero_id** | Option<**u32**> | Filter matches based on the hero ID. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1790380800]
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
**ability_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats> |  |
**ability_unlock_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**include_corrupted_items** | Option<**bool**> | Count corrupted items (build 6712+: a T3/T4 upgrade the Broker swapped for a corrupted version with the same item id) as the normal item. **Default:** `false`, corrupted purchases are ignored. |  |[default to false]

### Return type

[**Vec<models::ItemPermutationStats>**](ItemPermutationStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## item_stats

> Vec<models::ItemStats> item_stats(bucket, game_mode, match_mode, hero_ids, hero_id, enemy_hero_ids, enemy_hero_ids_all_match, min_enemy_networth, max_enemy_networth, same_lane_filter, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, include_item_ids, exclude_item_ids, ability_order_prefix, ability_unlock_order_prefix, hero_build_id, min_matches, max_matches, account_id, account_ids, min_bought_at_s, max_bought_at_s, item_order, corrupted_items, include_corrupted_items, enhanced_items)
Item Stats

 Retrieves item statistics based on historical match data.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**bucket** | Option<**String**> | Bucket allows you to group the stats by a specific field. |  |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**hero_ids** | Option<**String**> | Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**hero_id** | Option<**u32**> | Filter matches based on the hero ID. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**enemy_hero_ids** | Option<**String**> | Filter to matches where one or more of these heroes were on the opposing team. Comma separated. When set, returns \"what items beat hero(es) X?\" stats. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**enemy_hero_ids_all_match** | Option<**bool**> | When `true`, requires *all* of the specified `enemy_hero_ids` to be on the same enemy team. When `false` (default), matches if *any* of the specified hero(es) are on the enemy team. Ignored when `enemy_hero_ids` is unset. |  |
**min_enemy_networth** | Option<**u64**> | Filter the specified enemy hero(es) by their final net worth. Ignored when `enemy_hero_ids` is unset. |  |
**max_enemy_networth** | Option<**u64**> | Filter the specified enemy hero(es) by their final net worth. Ignored when `enemy_hero_ids` is unset. |  |
**same_lane_filter** | Option<**bool**> | When `true`, only counts buyers in the same `assigned_lane` as one of the specified enemy heroes. Ignored when `enemy_hero_ids` is unset. **Default:** `false`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1790380800]
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
**ability_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats> |  |
**ability_unlock_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**hero_build_id** | Option<**u64**> | Only players who started the match with this hero build selected (the first build they had selected when the game started). Matches without a processed demo record no build. See more: <https://api.deadlock-api.com/v1/analytics/hero-build-stats/{hero_id}> |  |
**min_matches** | Option<**u32**> | The minimum number of matches played for an item to be included in the response. |  |[default to 20]
**max_matches** | Option<**u32**> | The maximum number of matches played for a hero combination to be included in the response. |  |
**account_id** | Option<**u32**> | Filter for matches with a specific player account ID. |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |
**min_bought_at_s** | Option<**u32**> | Filter items bought after this game time (seconds). |  |
**max_bought_at_s** | Option<**u32**> | Filter items bought before this game time (seconds). |  |
**item_order** | Option<[**Vec<String>**](String.md)> | Filter by purchase order. Each value is a comma-separated, ordered list of item ids (e.g. `1396247347,3977876567`). This is a *constraint*, not an inclusion filter: for each adjacent pair in the list, a match is excluded only when the player bought **both** items but bought the later one first. Builds missing either item are unaffected. Repeat the parameter for multiple independent orderings. See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**corrupted_items** | Option<**String**> | How to count corrupted items (build 6712+: a T3/T4 upgrade that the Broker swapped for a corrupted version with the same item id). `exclude`: only normal purchases. `include`: corrupted purchases count as the normal item. `only`: only corrupted purchases, so each row describes the corrupted variant of `item_id`. Compare it with the same request using `exclude`. Corrupted items only exist in matches from 2026-09-29 on, so `only` ignores earlier time and match-id bounds. `include` and `only` skip the pre-aggregated rollups, so those requests are slower. **Default:** `exclude`, or `include` if the deprecated `include_corrupted_items=true` is set. |  |
**include_corrupted_items** | Option<**bool**> | Deprecated alias of `corrupted_items=include`. `corrupted_items` takes precedence when both are set. |  |[default to false]
**enhanced_items** | Option<**String**> | How to count enhanced items (Street Brawl only: a draft pick that is the enhanced version of an upgrade, with the same item id). `include`: enhanced purchases count as the normal item. `exclude`: only normal purchases. `only`: only enhanced purchases, so each row describes the enhanced variant of `item_id`. Compare it with the same request using `exclude`. Matches before 2026-04-08 do not record which purchases were enhanced, so `exclude` and `only` ignore earlier time and match-id bounds. `exclude` and `only` require `game_mode=street_brawl` and skip the pre-aggregated rollups, so those requests are slower. **Default:** `include`. |  |

### Return type

[**Vec<models::ItemStats>**](ItemStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## kill_death_stats

> Vec<models::KillDeathStats> kill_death_stats(team, game_mode, match_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, account_ids, hero_ids, min_networth, max_networth, is_high_skill_range_parties, is_low_pri_pool, is_new_player_pool, min_match_id, max_match_id, min_average_badge, max_average_badge, min_kills_per_raster, max_kills_per_raster, min_deaths_per_raster, max_deaths_per_raster, min_game_time_s, max_game_time_s)
Kill Death Stats

 This endpoint returns the kill-death statistics across a 128x128 pixel raster.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**team** | Option<**u32**> | Filter by team number. |  |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1790380800]
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


## lane_matchup_stats

> Vec<models::LaneMatchupStats> lane_matchup_stats(game_mode, match_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_average_badge, max_average_badge, min_match_id, max_match_id, sample_time_s, assigned_lanes, hero_ids, enemy_hero_ids, stats, group_by, min_matches, max_matches, account_ids)
Lane Matchup Stats (Subject to Change)

 > **⚠️ Subject to change:** This endpoint is newly added and not yet stable. Its parameters, response fields and semantics may change or be removed without notice.  Retrieves duo-versus-duo lane statistics: how a pair of heroes sharing a lane performed against the pair of heroes they laned against.  Win rate covers the whole match. Everything else is read at `sample_time_s` (900 by default, the last sample before the game's recording cadence coarsens) off the matchups that lasted that long, counted by `sample_matches`. Souls are always reported, in `net_worth_diff`; pass `stats` for any other per-tick stat the game records — kills, denies, player damage, healing, level and so on — each as the duo's own combined value *and* as its lead over the enemy duo.  Only lanes where *both* sides fielded exactly two players are counted, and each lane contributes one row per side, so every matchup appears twice with the two sides swapped.  `group_by` chooses what a row stands for. The default groups all three dimensions, giving one row per duo-versus-duo matchup per lane. Dropping `enemy_hero_ids` gives a duo's record across every opponent, dropping `hero_ids` gives what a duo is up against, and dropping `assigned_lane` merges the lanes. Folded dimensions come back as `0` / an empty array.  Pass `hero_ids` and `enemy_hero_ids` to scope the response to the duos you care about. Without them the full duo-versus-duo matrix is computed, which is a considerably more expensive query.  Results are cached for **1 hour**. The cache key is determined by the specific combination of filter parameters used in the query. Subsequent requests using the exact same filters within this timeframe will receive the cached response.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1790380800]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**sample_time_s** | Option<**u32**> | Seconds into the match the stat readings are taken at. **Default:** 900. Matchups whose match ended earlier are still counted in `wins` and `matches_played`, but contribute no reading; `sample_matches` reports how many did. |  |[default to 900]
**assigned_lanes** | Option<**String**> | Comma separated list of `assigned_lane` values to restrict the response to. See the `lane_info` array of <https://api.deadlock-api.com/v1/assets/generic-data>. |  |
**hero_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of hero ids the *ally* duo has to be drawn from, or a single hero id the *ally* duo has to include. Omit to return every duo. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**enemy_hero_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of hero ids the *enemy* duo has to be drawn from, or a single hero id the *enemy* duo has to include. Omit to return every duo. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**stats** | Option<**String**> | Comma separated list of extra per-tick stats to report, at most 8. **Default:** none. |  |
**group_by** | Option<**String**> | Comma separated list of dimensions to group by. Valid values: `assigned_lane`, `hero_ids`, `enemy_hero_ids`. **Default:** all three. |  |
**min_matches** | Option<**u64**> | The minimum number of lane matchups behind a row for it to be included in the response. |  |[default to 20]
**max_matches** | Option<**u64**> | The maximum number of lane matchups behind a row for it to be included in the response. |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::LaneMatchupStats>**](LaneMatchupStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## lane_soul_curve

> Vec<models::LaneSoulCurve> lane_soul_curve(game_mode, match_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_average_badge, max_average_badge, min_match_id, max_match_id, min_time_s, max_time_s, assigned_lanes, hero_ids, enemy_hero_ids, stats, group_by, min_matches, max_matches, account_ids)
Lane Soul Curve (Subject to Change)

 > **⚠️ Subject to change:** This endpoint is newly added and not yet stable. Its parameters, response fields and semantics may change or be removed without notice.  Retrieves how a duo's lead over the duo they laned against develops over the course of the match.  The curve is not interpolated: it carries exactly the samples the game records, which are every 180 seconds up to the 15 minute mark and every 300 seconds after that. It runs from `min_time_s` (180 by default) to `max_time_s`, which is open by default, so a matchup is followed until its matches end. `sample_matches` reports how many matchups were still running at each point, and thins out towards the end of the curve.  Only lanes where *both* sides fielded exactly two players are counted, and each lane contributes one row per side, so every matchup appears twice with the two sides swapped.  Souls are always reported, in `net_worth_diff`. Pass `stats` for curves of any other per-tick stat the game records — kills, denies, player damage, healing, level and so on — each as the duo's own combined value *and* as its lead over the enemy duo.  `group_by` chooses what a row stands for. The default groups all three dimensions, giving one row per duo-versus-duo matchup per lane. Dropping `enemy_hero_ids` gives a duo's curve across every opponent, dropping `hero_ids` gives what a duo is up against, and dropping `assigned_lane` merges the lanes. Folded dimensions come back as `0` / an empty array.  Pass `hero_ids` and `enemy_hero_ids` to scope the response to the duos you care about. Without them the full duo-versus-duo matrix is computed, which is a considerably more expensive query.  Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1790380800]
**max_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). |  |
**min_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**max_duration_s** | Option<**u64**> | Filter matches based on their duration in seconds (up to 7000s). |  |
**min_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**max_average_badge** | Option<**u32**> | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> |  |
**min_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**max_match_id** | Option<**u64**> | Filter matches based on their ID. |  |
**min_time_s** | Option<**u32**> | Earliest sample to return, in seconds into the match. **Default:** 180. |  |[default to 180]
**max_time_s** | Option<**u32**> | Latest sample to return, in seconds into the match. Omit to follow every matchup to the end of its match. |  |
**assigned_lanes** | Option<**String**> | Comma separated list of `assigned_lane` values to restrict the response to. See the `lane_info` array of <https://api.deadlock-api.com/v1/assets/generic-data>. |  |
**hero_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of hero ids the *ally* duo has to be drawn from, or a single hero id the *ally* duo has to include. Omit to return every duo. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**enemy_hero_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of hero ids the *enemy* duo has to be drawn from, or a single hero id the *enemy* duo has to include. Omit to return every duo. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**stats** | Option<**String**> | Comma separated list of extra per-tick stats to return curves for, at most 8. **Default:** none. |  |
**group_by** | Option<**String**> | Comma separated list of dimensions to group by. Valid values: `assigned_lane`, `hero_ids`, `enemy_hero_ids`. **Default:** all three. |  |
**min_matches** | Option<**u64**> | The minimum number of lane matchups behind a row for it to be included in the response. |  |[default to 20]
**max_matches** | Option<**u64**> | The maximum number of lane matchups behind a row for it to be included in the response. |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |

### Return type

[**Vec<models::LaneSoulCurve>**](LaneSoulCurve.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## player_performance_curve

> Vec<models::PlayerPerformanceCurvePoint> player_performance_curve(resolution, game_mode, match_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, hero_ids, hero_build_id, include_item_ids, exclude_item_ids, ability_order_prefix, ability_unlock_order_prefix, account_ids)
Player Performance Curve

 Retrieves player performance statistics (net worth, kills, deaths, assists, souls per source, damage and kills per target, healing, barriers and self damage) over time throughout matches.  Results are cached for **1 hour** based on the unique combination of query parameters provided.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**resolution** | Option<**u32**> | Resolution for relative game times in percent (0-100). **Default:** 10 (buckets of 10%). Set to **0** to use absolute game time (seconds). |  |[default to 10]
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1790380800]
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
**hero_build_id** | Option<**u64**> | Only players who started the match with this hero build selected. Matches without a processed demo record no build. See more: <https://api.deadlock-api.com/v1/analytics/hero-build-stats/{hero_id}> |  |
**include_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to include (only players who have purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**exclude_item_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items> |  |
**ability_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats> |  |
**ability_unlock_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
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

> Vec<models::PlayerEntry> player_scoreboard(sort_by, sort_direction, game_mode, match_mode, hero_id, hero_build_id, min_matches, max_matches, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, start, limit, account_ids)
Player Scoreboard

 This endpoint returns the player scoreboard.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**sort_by** | **String** | The field to sort by. | [required] |
**sort_direction** | Option<**String**> | The direction to sort players in. |  |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**hero_id** | Option<**u32**> | Filter matches based on the hero ID. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**hero_build_id** | Option<**u64**> | Only matches the player started with this hero build selected. Matches without a processed demo record no build. See more: <https://api.deadlock-api.com/v1/analytics/hero-build-stats/{hero_id}> |  |
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
**start** | Option<**u32**> | The rank to start fetching players from (1-based, like `rank`). |  |
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

> std::collections::HashMap<String, models::HashMapValue> player_stats_metrics(hero_ids, game_mode, match_mode, min_unix_timestamp, max_unix_timestamp, min_duration_s, max_duration_s, min_networth, max_networth, min_average_badge, max_average_badge, min_match_id, max_match_id, max_matches, include_item_ids, exclude_item_ids, ability_order_prefix, ability_unlock_order_prefix, account_ids, include_buff_metrics)
Player Stats Metrics

 Returns comprehensive statistical analysis of player performance.  `avg`, `std` and the percentiles describe the distribution over single matches: each player's row in each matching match is one value, so players with more matches weigh more. With `account_ids` it is the distribution of those players' matches. The percentiles rank a single match, not a player: a player's average over many matches spreads much narrower than single matches do, so read against these percentiles it looks less extreme than it is among players.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  > Note: Quantiles are calculated using the [DDSketch](https://www.vldb.org/pvldb/vol12/p2195-masson.pdf) algorithm, so they are not exact but have a maximum relative error of 0.01.  ### Rate Limits: > The rate limits below are **shared across all analytics endpoints**.  | Type | Limit | | ---- | ----- | | IP | 200req/min | | Key | 400req/min | | Global | 2000req/min |     

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**hero_ids** | Option<**String**> | Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**game_mode** | Option<**String**> | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. |  |
**match_mode** | Option<**String**> | Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`. |  |
**min_unix_timestamp** | Option<**i64**> | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. |  |[default to 1790380800]
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
**ability_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats> |  |
**ability_unlock_order_prefix** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes> |  |
**account_ids** | Option<[**Vec<u32>**](U32.md)> | Comma separated list of account ids to include |  |
**include_buff_metrics** | Option<**bool**> | Also return the permanent buff (power-up) pickup metrics `permanent_buffs`, `permanent_buffs_per_min` and `first_permanent_buff_time_s`. Off by default because the buff columns are not in the per-hero projection, which roughly doubles the cost of hero-filtered requests. `first_permanent_buff_time_s` only covers matches since build 6712 (2026-09-29), which record pickup times; its values are `null` when the filter matches none of them. |  |[default to false]

### Return type

[**std::collections::HashMap<String, models::HashMapValue>**](HashMap_value.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

