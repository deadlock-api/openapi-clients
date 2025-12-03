# deadlock_api_client.AnalyticsApi

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
[**kill_death_stats**](AnalyticsApi.md#kill_death_stats) | **GET** /v1/analytics/kill-death-stats | Kill Death Stats
[**player_scoreboard**](AnalyticsApi.md#player_scoreboard) | **GET** /v1/analytics/scoreboards/players | Player Scoreboard
[**player_stats_metrics**](AnalyticsApi.md#player_stats_metrics) | **GET** /v1/analytics/player-stats/metrics | Player Stats Metrics


# **ability_order_stats**
> List[AnalyticsAbilityOrderStats] ability_order_stats(hero_id, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_ability_upgrades=min_ability_upgrades, max_ability_upgrades=max_ability_upgrades, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, min_matches=min_matches, account_id=account_id, account_ids=account_ids)

Ability Order Stats


Retrieves statistics for the ability order of a hero.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.analytics_ability_order_stats import AnalyticsAbilityOrderStats
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.AnalyticsApi(api_client)
    hero_id = 56 # int | See more: <https://assets.deadlock-api.com/v2/heroes>
    min_unix_timestamp = 1762041600 # int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1762041600)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    min_ability_upgrades = 56 # int | Filter players based on their minimum number of ability upgrades over the whole match. (optional)
    max_ability_upgrades = 56 # int | Filter players based on their maximum number of ability upgrades over the whole match. (optional)
    min_networth = 56 # int | Filter players based on their net worth. (optional)
    max_networth = 56 # int | Filter players based on their net worth. (optional)
    min_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    max_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)
    min_matches = 20 # int | The minimum number of matches played for an ability order to be included in the response. (optional) (default to 20)
    account_id = 56 # int | Filter for matches with a specific player account ID. (optional)
    account_ids = [56] # List[int] | Comma separated list of account ids to include (optional)

    try:
        # Ability Order Stats
        api_response = api_instance.ability_order_stats(hero_id, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_ability_upgrades=min_ability_upgrades, max_ability_upgrades=max_ability_upgrades, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, min_matches=min_matches, account_id=account_id, account_ids=account_ids)
        print("The response of AnalyticsApi->ability_order_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->ability_order_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_id** | **int**| See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1762041600]
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **min_ability_upgrades** | **int**| Filter players based on their minimum number of ability upgrades over the whole match. | [optional] 
 **max_ability_upgrades** | **int**| Filter players based on their maximum number of ability upgrades over the whole match. | [optional] 
 **min_networth** | **int**| Filter players based on their net worth. | [optional] 
 **max_networth** | **int**| Filter players based on their net worth. | [optional] 
 **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **min_matches** | **int**| The minimum number of matches played for an ability order to be included in the response. | [optional] [default to 20]
 **account_id** | **int**| Filter for matches with a specific player account ID. | [optional] 
 **account_ids** | [**List[int]**](int.md)| Comma separated list of account ids to include | [optional] 

### Return type

[**List[AnalyticsAbilityOrderStats]**](AnalyticsAbilityOrderStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ability Order Stats |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch ability order stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **badge_distribution**
> List[BadgeDistribution] badge_distribution(min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, is_high_skill_range_parties=is_high_skill_range_parties, is_low_pri_pool=is_low_pri_pool, is_new_player_pool=is_new_player_pool, min_match_id=min_match_id, max_match_id=max_match_id)

Badge Distribution


This endpoint returns the player badge distribution.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.badge_distribution import BadgeDistribution
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.AnalyticsApi(api_client)
    min_unix_timestamp = 1762041600 # int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1762041600)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    is_high_skill_range_parties = True # bool | Filter matches based on whether they are in the high skill range. (optional)
    is_low_pri_pool = True # bool | Filter matches based on whether they are in the low priority pool. (optional)
    is_new_player_pool = True # bool | Filter matches based on whether they are in the new player pool. (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)

    try:
        # Badge Distribution
        api_response = api_instance.badge_distribution(min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, is_high_skill_range_parties=is_high_skill_range_parties, is_low_pri_pool=is_low_pri_pool, is_new_player_pool=is_new_player_pool, min_match_id=min_match_id, max_match_id=max_match_id)
        print("The response of AnalyticsApi->badge_distribution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->badge_distribution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1762041600]
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **is_high_skill_range_parties** | **bool**| Filter matches based on whether they are in the high skill range. | [optional] 
 **is_low_pri_pool** | **bool**| Filter matches based on whether they are in the low priority pool. | [optional] 
 **is_new_player_pool** | **bool**| Filter matches based on whether they are in the new player pool. | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 

### Return type

[**List[BadgeDistribution]**](BadgeDistribution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Badge Distribution |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch badge distribution |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **build_item_stats**
> List[BuildItemStats] build_item_stats(hero_id=hero_id, min_last_updated_unix_timestamp=min_last_updated_unix_timestamp, max_last_updated_unix_timestamp=max_last_updated_unix_timestamp)

Build Item Stats


Retrieves item statistics from hero builds.

Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.build_item_stats import BuildItemStats
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.AnalyticsApi(api_client)
    hero_id = 56 # int | Filter builds based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
    min_last_updated_unix_timestamp = 1762041600 # int | Filter builds based on their last updated time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1762041600)
    max_last_updated_unix_timestamp = 56 # int | Filter builds based on their last updated time (Unix timestamp). (optional)

    try:
        # Build Item Stats
        api_response = api_instance.build_item_stats(hero_id=hero_id, min_last_updated_unix_timestamp=min_last_updated_unix_timestamp, max_last_updated_unix_timestamp=max_last_updated_unix_timestamp)
        print("The response of AnalyticsApi->build_item_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->build_item_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_id** | **int**| Filter builds based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] 
 **min_last_updated_unix_timestamp** | **int**| Filter builds based on their last updated time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1762041600]
 **max_last_updated_unix_timestamp** | **int**| Filter builds based on their last updated time (Unix timestamp). | [optional] 

### Return type

[**List[BuildItemStats]**](BuildItemStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Build Item Stats |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch build item stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hero_comb_stats**
> List[HeroCombStats] hero_comb_stats(min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, include_hero_ids=include_hero_ids, exclude_hero_ids=exclude_hero_ids, min_matches=min_matches, max_matches=max_matches, comb_size=comb_size, account_id=account_id, account_ids=account_ids)

Hero Comb Stats


Retrieves overall statistics for each hero combination.

Results are cached for **1 hour**. The cache key is determined by the specific combination of filter parameters used in the query. Subsequent requests using the exact same filters within this timeframe will receive the cached response.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.hero_comb_stats import HeroCombStats
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.AnalyticsApi(api_client)
    min_unix_timestamp = 1762041600 # int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1762041600)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    min_networth = 56 # int | Filter players based on their net worth. (optional)
    max_networth = 56 # int | Filter players based on their net worth. (optional)
    min_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    max_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)
    include_hero_ids = [56] # List[int] | Comma separated list of hero ids to include. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
    exclude_hero_ids = [56] # List[int] | Comma separated list of hero ids to exclude. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
    min_matches = 20 # int | The minimum number of matches played for a hero combination to be included in the response. (optional) (default to 20)
    max_matches = 56 # int | The maximum number of matches played for a hero combination to be included in the response. (optional)
    comb_size = 6 # int | The combination size to return. (optional) (default to 6)
    account_id = 56 # int | Filter for matches with a specific player account ID. (optional)
    account_ids = [56] # List[int] | Comma separated list of account ids to include (optional)

    try:
        # Hero Comb Stats
        api_response = api_instance.hero_comb_stats(min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, include_hero_ids=include_hero_ids, exclude_hero_ids=exclude_hero_ids, min_matches=min_matches, max_matches=max_matches, comb_size=comb_size, account_id=account_id, account_ids=account_ids)
        print("The response of AnalyticsApi->hero_comb_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->hero_comb_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1762041600]
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **min_networth** | **int**| Filter players based on their net worth. | [optional] 
 **max_networth** | **int**| Filter players based on their net worth. | [optional] 
 **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **include_hero_ids** | [**List[int]**](int.md)| Comma separated list of hero ids to include. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] 
 **exclude_hero_ids** | [**List[int]**](int.md)| Comma separated list of hero ids to exclude. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] 
 **min_matches** | **int**| The minimum number of matches played for a hero combination to be included in the response. | [optional] [default to 20]
 **max_matches** | **int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] 
 **comb_size** | **int**| The combination size to return. | [optional] [default to 6]
 **account_id** | **int**| Filter for matches with a specific player account ID. | [optional] 
 **account_ids** | [**List[int]**](int.md)| Comma separated list of account ids to include | [optional] 

### Return type

[**List[HeroCombStats]**](HeroCombStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hero Comb Stats |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch hero comb stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hero_counters_stats**
> List[HeroCounterStats] hero_counters_stats(min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_enemy_networth=min_enemy_networth, max_enemy_networth=max_enemy_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, same_lane_filter=same_lane_filter, min_matches=min_matches, max_matches=max_matches, account_id=account_id, account_ids=account_ids)

Hero Counter Stats


Retrieves hero-versus-hero matchup statistics based on historical match data.

This endpoint analyzes completed matches to calculate how often a specific hero (`hero_id`) wins against an enemy hero (`enemy_hero_id`) and the total number of times they have faced each other under the specified filter conditions.

Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.hero_counter_stats import HeroCounterStats
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.AnalyticsApi(api_client)
    min_unix_timestamp = 1762041600 # int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1762041600)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    min_networth = 56 # int | Filter players based on their net worth. (optional)
    max_networth = 56 # int | Filter players based on their net worth. (optional)
    min_enemy_networth = 56 # int | Filter enemy players based on their net worth. (optional)
    max_enemy_networth = 56 # int | Filter enemy players based on their net worth. (optional)
    min_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    max_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)
    same_lane_filter = True # bool | When `true`, only considers matchups where both `hero_id` and `enemy_hero_id` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane. (optional) (default to True)
    min_matches = 20 # int | The minimum number of matches played for a hero combination to be included in the response. (optional) (default to 20)
    max_matches = 56 # int | The maximum number of matches played for a hero combination to be included in the response. (optional)
    account_id = 56 # int | Filter for matches with a specific player account ID. (optional)
    account_ids = [56] # List[int] | Comma separated list of account ids to include (optional)

    try:
        # Hero Counter Stats
        api_response = api_instance.hero_counters_stats(min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_enemy_networth=min_enemy_networth, max_enemy_networth=max_enemy_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, same_lane_filter=same_lane_filter, min_matches=min_matches, max_matches=max_matches, account_id=account_id, account_ids=account_ids)
        print("The response of AnalyticsApi->hero_counters_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->hero_counters_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1762041600]
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **min_networth** | **int**| Filter players based on their net worth. | [optional] 
 **max_networth** | **int**| Filter players based on their net worth. | [optional] 
 **min_enemy_networth** | **int**| Filter enemy players based on their net worth. | [optional] 
 **max_enemy_networth** | **int**| Filter enemy players based on their net worth. | [optional] 
 **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **same_lane_filter** | **bool**| When &#x60;true&#x60;, only considers matchups where both &#x60;hero_id&#x60; and &#x60;enemy_hero_id&#x60; were assigned to the same lane (e.g., both Mid Lane). When &#x60;false&#x60;, considers all matchups regardless of assigned lane. | [optional] [default to True]
 **min_matches** | **int**| The minimum number of matches played for a hero combination to be included in the response. | [optional] [default to 20]
 **max_matches** | **int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] 
 **account_id** | **int**| Filter for matches with a specific player account ID. | [optional] 
 **account_ids** | [**List[int]**](int.md)| Comma separated list of account ids to include | [optional] 

### Return type

[**List[HeroCounterStats]**](HeroCounterStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hero Counter Stats |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch hero counter stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hero_scoreboard**
> List[Entry] hero_scoreboard(sort_by, sort_direction=sort_direction, min_matches=min_matches, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, account_id=account_id, account_ids=account_ids)

Hero Scoreboard


This endpoint returns the hero scoreboard.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.entry import Entry
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.AnalyticsApi(api_client)
    sort_by = 'sort_by_example' # str | The field to sort by.
    sort_direction = 'sort_direction_example' # str | The direction to sort heroes in. (optional)
    min_matches = 56 # int | Filter by min number of matches played. (optional)
    min_unix_timestamp = 1762041600 # int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1762041600)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    min_networth = 56 # int | Filter players based on their net worth. (optional)
    max_networth = 56 # int | Filter players based on their net worth. (optional)
    min_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    max_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)
    account_id = 56 # int | Filter for matches with a specific player account ID. (optional)
    account_ids = [56] # List[int] | Comma separated list of account ids to include (optional)

    try:
        # Hero Scoreboard
        api_response = api_instance.hero_scoreboard(sort_by, sort_direction=sort_direction, min_matches=min_matches, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, account_id=account_id, account_ids=account_ids)
        print("The response of AnalyticsApi->hero_scoreboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->hero_scoreboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | **str**| The field to sort by. | 
 **sort_direction** | **str**| The direction to sort heroes in. | [optional] 
 **min_matches** | **int**| Filter by min number of matches played. | [optional] 
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1762041600]
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **min_networth** | **int**| Filter players based on their net worth. | [optional] 
 **max_networth** | **int**| Filter players based on their net worth. | [optional] 
 **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **account_id** | **int**| Filter for matches with a specific player account ID. | [optional] 
 **account_ids** | [**List[int]**](int.md)| Comma separated list of account ids to include | [optional] 

### Return type

[**List[Entry]**](Entry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hero Scoreboard |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch hero scoreboard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hero_stats**
> List[AnalyticsHeroStats] hero_stats(bucket=bucket, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, min_hero_matches=min_hero_matches, max_hero_matches=max_hero_matches, min_hero_matches_total=min_hero_matches_total, max_hero_matches_total=max_hero_matches_total, include_item_ids=include_item_ids, exclude_item_ids=exclude_item_ids, account_id=account_id, account_ids=account_ids)

Hero Stats


Retrieves performance statistics for each hero based on historical match data.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.analytics_hero_stats import AnalyticsHeroStats
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.AnalyticsApi(api_client)
    bucket = 'bucket_example' # str | Bucket allows you to group the stats by a specific field. (optional)
    min_unix_timestamp = 1762041600 # int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1762041600)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    min_networth = 56 # int | Filter players based on their net worth. (optional)
    max_networth = 56 # int | Filter players based on their net worth. (optional)
    min_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    max_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)
    min_hero_matches = 56 # int | Filter players based on the number of matches they have played with a specific hero within the filtered time range. (optional)
    max_hero_matches = 56 # int | Filter players based on the number of matches they have played with a specific hero within the filtered time range. (optional)
    min_hero_matches_total = 56 # int | Filter players based on the number of matches they have played with a specific hero in their entire history. (optional)
    max_hero_matches_total = 56 # int | Filter players based on the number of matches they have played with a specific hero in their entire history. (optional)
    include_item_ids = [56] # List[int] | Comma separated list of item ids to include (only heroes who have purchased these items). See more: <https://assets.deadlock-api.com/v2/items> (optional)
    exclude_item_ids = [56] # List[int] | Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: <https://assets.deadlock-api.com/v2/items> (optional)
    account_id = 56 # int | Filter for matches with a specific player account ID. (optional)
    account_ids = [56] # List[int] | Comma separated list of account ids to include (optional)

    try:
        # Hero Stats
        api_response = api_instance.hero_stats(bucket=bucket, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, min_hero_matches=min_hero_matches, max_hero_matches=max_hero_matches, min_hero_matches_total=min_hero_matches_total, max_hero_matches_total=max_hero_matches_total, include_item_ids=include_item_ids, exclude_item_ids=exclude_item_ids, account_id=account_id, account_ids=account_ids)
        print("The response of AnalyticsApi->hero_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->hero_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket allows you to group the stats by a specific field. | [optional] 
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1762041600]
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **min_networth** | **int**| Filter players based on their net worth. | [optional] 
 **max_networth** | **int**| Filter players based on their net worth. | [optional] 
 **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **min_hero_matches** | **int**| Filter players based on the number of matches they have played with a specific hero within the filtered time range. | [optional] 
 **max_hero_matches** | **int**| Filter players based on the number of matches they have played with a specific hero within the filtered time range. | [optional] 
 **min_hero_matches_total** | **int**| Filter players based on the number of matches they have played with a specific hero in their entire history. | [optional] 
 **max_hero_matches_total** | **int**| Filter players based on the number of matches they have played with a specific hero in their entire history. | [optional] 
 **include_item_ids** | [**List[int]**](int.md)| Comma separated list of item ids to include (only heroes who have purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] 
 **exclude_item_ids** | [**List[int]**](int.md)| Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] 
 **account_id** | **int**| Filter for matches with a specific player account ID. | [optional] 
 **account_ids** | [**List[int]**](int.md)| Comma separated list of account ids to include | [optional] 

### Return type

[**List[AnalyticsHeroStats]**](AnalyticsHeroStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hero Stats |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch hero stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hero_synergies_stats**
> List[HeroSynergyStats] hero_synergies_stats(min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, same_lane_filter=same_lane_filter, same_party_filter=same_party_filter, min_matches=min_matches, max_matches=max_matches, account_id=account_id, account_ids=account_ids)

Hero Synergy Stats


Retrieves hero pair synergy statistics based on historical match data.

This endpoint analyzes completed matches to calculate how often a specific pair of heroes (`hero_id1` and `hero_id2`) won when playing *together on the same team*, and the total number of times they have played together under the specified filter conditions.

Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.hero_synergy_stats import HeroSynergyStats
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.AnalyticsApi(api_client)
    min_unix_timestamp = 1762041600 # int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1762041600)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    min_networth = 56 # int | Filter players based on their net worth. (optional)
    max_networth = 56 # int | Filter players based on their net worth. (optional)
    min_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    max_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)
    same_lane_filter = True # bool | When `true`, only considers matchups where both `hero_id1` and `hero_id2` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane. (optional) (default to True)
    same_party_filter = True # bool | When `true`, only considers matchups where both `hero_id` and `hero_id2` were on the same party. When `false`, considers all matchups regardless of party affiliation. (optional) (default to True)
    min_matches = 20 # int | The minimum number of matches played for a hero combination to be included in the response. (optional) (default to 20)
    max_matches = 56 # int | The maximum number of matches played for a hero combination to be included in the response. (optional)
    account_id = 56 # int | Filter for matches with a specific player account ID. (optional)
    account_ids = [56] # List[int] | Comma separated list of account ids to include (optional)

    try:
        # Hero Synergy Stats
        api_response = api_instance.hero_synergies_stats(min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, same_lane_filter=same_lane_filter, same_party_filter=same_party_filter, min_matches=min_matches, max_matches=max_matches, account_id=account_id, account_ids=account_ids)
        print("The response of AnalyticsApi->hero_synergies_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->hero_synergies_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1762041600]
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **min_networth** | **int**| Filter players based on their net worth. | [optional] 
 **max_networth** | **int**| Filter players based on their net worth. | [optional] 
 **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **same_lane_filter** | **bool**| When &#x60;true&#x60;, only considers matchups where both &#x60;hero_id1&#x60; and &#x60;hero_id2&#x60; were assigned to the same lane (e.g., both Mid Lane). When &#x60;false&#x60;, considers all matchups regardless of assigned lane. | [optional] [default to True]
 **same_party_filter** | **bool**| When &#x60;true&#x60;, only considers matchups where both &#x60;hero_id&#x60; and &#x60;hero_id2&#x60; were on the same party. When &#x60;false&#x60;, considers all matchups regardless of party affiliation. | [optional] [default to True]
 **min_matches** | **int**| The minimum number of matches played for a hero combination to be included in the response. | [optional] [default to 20]
 **max_matches** | **int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] 
 **account_id** | **int**| Filter for matches with a specific player account ID. | [optional] 
 **account_ids** | [**List[int]**](int.md)| Comma separated list of account ids to include | [optional] 

### Return type

[**List[HeroSynergyStats]**](HeroSynergyStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hero Synergy Stats |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch hero synergy stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_permutation_stats**
> List[ItemPermutationStats] item_permutation_stats(item_ids=item_ids, comb_size=comb_size, hero_ids=hero_ids, hero_id=hero_id, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, account_id=account_id, account_ids=account_ids)

Item Permutation Stats


Retrieves item permutation statistics based on historical match data.

Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.item_permutation_stats import ItemPermutationStats
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.AnalyticsApi(api_client)
    item_ids = [56] # List[int] | Comma separated list of item ids. See more: <https://assets.deadlock-api.com/v2/items> (optional)
    comb_size = 2 # int | The combination size to return. (optional) (default to 2)
    hero_ids = 'hero_ids_example' # str | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
    hero_id = 56 # int | Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
    min_unix_timestamp = 1762041600 # int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1762041600)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    min_networth = 56 # int | Filter players based on their net worth. (optional)
    max_networth = 56 # int | Filter players based on their net worth. (optional)
    min_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    max_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)
    account_id = 56 # int | Filter for matches with a specific player account ID. (optional)
    account_ids = [56] # List[int] | Comma separated list of account ids to include (optional)

    try:
        # Item Permutation Stats
        api_response = api_instance.item_permutation_stats(item_ids=item_ids, comb_size=comb_size, hero_ids=hero_ids, hero_id=hero_id, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, account_id=account_id, account_ids=account_ids)
        print("The response of AnalyticsApi->item_permutation_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->item_permutation_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_ids** | [**List[int]**](int.md)| Comma separated list of item ids. See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] 
 **comb_size** | **int**| The combination size to return. | [optional] [default to 2]
 **hero_ids** | **str**| Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] 
 **hero_id** | **int**| Filter matches based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] 
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1762041600]
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **min_networth** | **int**| Filter players based on their net worth. | [optional] 
 **max_networth** | **int**| Filter players based on their net worth. | [optional] 
 **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **account_id** | **int**| Filter for matches with a specific player account ID. | [optional] 
 **account_ids** | [**List[int]**](int.md)| Comma separated list of account ids to include | [optional] 

### Return type

[**List[ItemPermutationStats]**](ItemPermutationStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Item Stats |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch item stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_stats**
> List[ItemStats] item_stats(bucket=bucket, hero_ids=hero_ids, hero_id=hero_id, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, include_item_ids=include_item_ids, exclude_item_ids=exclude_item_ids, min_matches=min_matches, max_matches=max_matches, account_id=account_id, account_ids=account_ids, min_bought_at_s=min_bought_at_s, max_bought_at_s=max_bought_at_s)

Item Stats


Retrieves item statistics based on historical match data.

Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.item_stats import ItemStats
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.AnalyticsApi(api_client)
    bucket = 'bucket_example' # str | Bucket allows you to group the stats by a specific field. (optional)
    hero_ids = 'hero_ids_example' # str | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
    hero_id = 56 # int | Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
    min_unix_timestamp = 1762041600 # int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1762041600)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    min_networth = 56 # int | Filter players based on their net worth. (optional)
    max_networth = 56 # int | Filter players based on their net worth. (optional)
    min_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    max_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)
    include_item_ids = [56] # List[int] | Comma separated list of item ids to include. See more: <https://assets.deadlock-api.com/v2/items> (optional)
    exclude_item_ids = [56] # List[int] | Comma separated list of item ids to exclude. See more: <https://assets.deadlock-api.com/v2/items> (optional)
    min_matches = 20 # int | The minimum number of matches played for an item to be included in the response. (optional) (default to 20)
    max_matches = 56 # int | The maximum number of matches played for a hero combination to be included in the response. (optional)
    account_id = 56 # int | Filter for matches with a specific player account ID. (optional)
    account_ids = [56] # List[int] | Comma separated list of account ids to include (optional)
    min_bought_at_s = 56 # int | Filter items bought after this game time (seconds). (optional)
    max_bought_at_s = 56 # int | Filter items bought before this game time (seconds). (optional)

    try:
        # Item Stats
        api_response = api_instance.item_stats(bucket=bucket, hero_ids=hero_ids, hero_id=hero_id, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, include_item_ids=include_item_ids, exclude_item_ids=exclude_item_ids, min_matches=min_matches, max_matches=max_matches, account_id=account_id, account_ids=account_ids, min_bought_at_s=min_bought_at_s, max_bought_at_s=max_bought_at_s)
        print("The response of AnalyticsApi->item_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->item_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket allows you to group the stats by a specific field. | [optional] 
 **hero_ids** | **str**| Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] 
 **hero_id** | **int**| Filter matches based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] 
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1762041600]
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **min_networth** | **int**| Filter players based on their net worth. | [optional] 
 **max_networth** | **int**| Filter players based on their net worth. | [optional] 
 **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **include_item_ids** | [**List[int]**](int.md)| Comma separated list of item ids to include. See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] 
 **exclude_item_ids** | [**List[int]**](int.md)| Comma separated list of item ids to exclude. See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] 
 **min_matches** | **int**| The minimum number of matches played for an item to be included in the response. | [optional] [default to 20]
 **max_matches** | **int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] 
 **account_id** | **int**| Filter for matches with a specific player account ID. | [optional] 
 **account_ids** | [**List[int]**](int.md)| Comma separated list of account ids to include | [optional] 
 **min_bought_at_s** | **int**| Filter items bought after this game time (seconds). | [optional] 
 **max_bought_at_s** | **int**| Filter items bought before this game time (seconds). | [optional] 

### Return type

[**List[ItemStats]**](ItemStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Item Stats |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch item stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kill_death_stats**
> List[KillDeathStats] kill_death_stats(team=team, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, account_ids=account_ids, hero_ids=hero_ids, min_networth=min_networth, max_networth=max_networth, is_high_skill_range_parties=is_high_skill_range_parties, is_low_pri_pool=is_low_pri_pool, is_new_player_pool=is_new_player_pool, min_match_id=min_match_id, max_match_id=max_match_id, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_kills_per_raster=min_kills_per_raster, max_kills_per_raster=max_kills_per_raster, min_deaths_per_raster=min_deaths_per_raster, max_deaths_per_raster=max_deaths_per_raster, min_game_time_s=min_game_time_s, max_game_time_s=max_game_time_s)

Kill Death Stats


This endpoint returns the kill-death statistics across a 100x100 pixel raster.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.kill_death_stats import KillDeathStats
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.AnalyticsApi(api_client)
    team = 56 # int | Filter by team number. (optional)
    min_unix_timestamp = 1762041600 # int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1762041600)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    account_ids = [56] # List[int] | Filter matches by account IDs of players that participated in the match. (optional)
    hero_ids = 'hero_ids_example' # str | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
    min_networth = 56 # int | Filter players based on their net worth. (optional)
    max_networth = 56 # int | Filter players based on their net worth. (optional)
    is_high_skill_range_parties = True # bool | Filter matches based on whether they are in the high skill range. (optional)
    is_low_pri_pool = True # bool | Filter matches based on whether they are in the low priority pool. (optional)
    is_new_player_pool = True # bool | Filter matches based on whether they are in the new player pool. (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)
    min_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    max_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    min_kills_per_raster = 56 # int | Filter Raster cells based on minimum kills. (optional)
    max_kills_per_raster = 56 # int | Filter Raster cells based on maximum kills. (optional)
    min_deaths_per_raster = 56 # int | Filter Raster cells based on minimum deaths. (optional)
    max_deaths_per_raster = 56 # int | Filter Raster cells based on maximum deaths. (optional)
    min_game_time_s = 56 # int | Filter kills based on their game time. (optional)
    max_game_time_s = 56 # int | Filter kills based on their game time. (optional)

    try:
        # Kill Death Stats
        api_response = api_instance.kill_death_stats(team=team, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, account_ids=account_ids, hero_ids=hero_ids, min_networth=min_networth, max_networth=max_networth, is_high_skill_range_parties=is_high_skill_range_parties, is_low_pri_pool=is_low_pri_pool, is_new_player_pool=is_new_player_pool, min_match_id=min_match_id, max_match_id=max_match_id, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_kills_per_raster=min_kills_per_raster, max_kills_per_raster=max_kills_per_raster, min_deaths_per_raster=min_deaths_per_raster, max_deaths_per_raster=max_deaths_per_raster, min_game_time_s=min_game_time_s, max_game_time_s=max_game_time_s)
        print("The response of AnalyticsApi->kill_death_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->kill_death_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team** | **int**| Filter by team number. | [optional] 
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1762041600]
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **account_ids** | [**List[int]**](int.md)| Filter matches by account IDs of players that participated in the match. | [optional] 
 **hero_ids** | **str**| Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] 
 **min_networth** | **int**| Filter players based on their net worth. | [optional] 
 **max_networth** | **int**| Filter players based on their net worth. | [optional] 
 **is_high_skill_range_parties** | **bool**| Filter matches based on whether they are in the high skill range. | [optional] 
 **is_low_pri_pool** | **bool**| Filter matches based on whether they are in the low priority pool. | [optional] 
 **is_new_player_pool** | **bool**| Filter matches based on whether they are in the new player pool. | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **min_kills_per_raster** | **int**| Filter Raster cells based on minimum kills. | [optional] 
 **max_kills_per_raster** | **int**| Filter Raster cells based on maximum kills. | [optional] 
 **min_deaths_per_raster** | **int**| Filter Raster cells based on minimum deaths. | [optional] 
 **max_deaths_per_raster** | **int**| Filter Raster cells based on maximum deaths. | [optional] 
 **min_game_time_s** | **int**| Filter kills based on their game time. | [optional] 
 **max_game_time_s** | **int**| Filter kills based on their game time. | [optional] 

### Return type

[**List[KillDeathStats]**](KillDeathStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kill Death Stats |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch kill death stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_scoreboard**
> List[Entry] player_scoreboard(sort_by, sort_direction=sort_direction, hero_id=hero_id, min_matches=min_matches, max_matches=max_matches, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, start=start, limit=limit, account_ids=account_ids)

Player Scoreboard


This endpoint returns the player scoreboard.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.entry import Entry
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.AnalyticsApi(api_client)
    sort_by = 'sort_by_example' # str | The field to sort by.
    sort_direction = 'sort_direction_example' # str | The direction to sort players in. (optional)
    hero_id = 56 # int | Filter matches based on the hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
    min_matches = 20 # int | The minimum number of matches played for a player to be included in the scoreboard. (optional) (default to 20)
    max_matches = 56 # int | The maximum number of matches played for a hero combination to be included in the response. (optional)
    min_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    min_networth = 56 # int | Filter players based on their net worth. (optional)
    max_networth = 56 # int | Filter players based on their net worth. (optional)
    min_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    max_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)
    start = 56 # int | The offset to start fetching players from. (optional)
    limit = 100 # int | The maximum number of players to fetch. (optional) (default to 100)
    account_ids = [56] # List[int] | Comma separated list of account ids to include (optional)

    try:
        # Player Scoreboard
        api_response = api_instance.player_scoreboard(sort_by, sort_direction=sort_direction, hero_id=hero_id, min_matches=min_matches, max_matches=max_matches, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, start=start, limit=limit, account_ids=account_ids)
        print("The response of AnalyticsApi->player_scoreboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->player_scoreboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | **str**| The field to sort by. | 
 **sort_direction** | **str**| The direction to sort players in. | [optional] 
 **hero_id** | **int**| Filter matches based on the hero ID. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] 
 **min_matches** | **int**| The minimum number of matches played for a player to be included in the scoreboard. | [optional] [default to 20]
 **max_matches** | **int**| The maximum number of matches played for a hero combination to be included in the response. | [optional] 
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **min_networth** | **int**| Filter players based on their net worth. | [optional] 
 **max_networth** | **int**| Filter players based on their net worth. | [optional] 
 **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **start** | **int**| The offset to start fetching players from. | [optional] 
 **limit** | **int**| The maximum number of players to fetch. | [optional] [default to 100]
 **account_ids** | [**List[int]**](int.md)| Comma separated list of account ids to include | [optional] 

### Return type

[**List[Entry]**](Entry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Player Scoreboard |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch player scoreboard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_stats_metrics**
> Dict[str, HashMapValue] player_stats_metrics(hero_ids=hero_ids, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, max_matches=max_matches, include_item_ids=include_item_ids, exclude_item_ids=exclude_item_ids, account_ids=account_ids)

Player Stats Metrics


Returns comprehensive statistical analysis of player performance.

Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.

> Note: Quantiles are calculated using the [DDSketch](https://www.vldb.org/pvldb/vol12/p2195-masson.pdf) algorithm, so they are not exact but have a maximum relative error of 0.01.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.hash_map_value import HashMapValue
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.AnalyticsApi(api_client)
    hero_ids = 'hero_ids_example' # str | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
    min_unix_timestamp = 1762041600 # int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1762041600)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    min_networth = 56 # int | Filter players based on their net worth. (optional)
    max_networth = 56 # int | Filter players based on their net worth. (optional)
    min_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    max_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_matches = 56 # int | The maximum number of matches to analyze. (optional)
    include_item_ids = [56] # List[int] | Comma separated list of item ids to include (only heroes who have purchased these items). See more: <https://assets.deadlock-api.com/v2/items> (optional)
    exclude_item_ids = [56] # List[int] | Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: <https://assets.deadlock-api.com/v2/items> (optional)
    account_ids = [56] # List[int] | Comma separated list of account ids to include (optional)

    try:
        # Player Stats Metrics
        api_response = api_instance.player_stats_metrics(hero_ids=hero_ids, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id, max_matches=max_matches, include_item_ids=include_item_ids, exclude_item_ids=exclude_item_ids, account_ids=account_ids)
        print("The response of AnalyticsApi->player_stats_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->player_stats_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_ids** | **str**| Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] 
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1762041600]
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **min_networth** | **int**| Filter players based on their net worth. | [optional] 
 **max_networth** | **int**| Filter players based on their net worth. | [optional] 
 **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_matches** | **int**| The maximum number of matches to analyze. | [optional] 
 **include_item_ids** | [**List[int]**](int.md)| Comma separated list of item ids to include (only heroes who have purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] 
 **exclude_item_ids** | [**List[int]**](int.md)| Comma separated list of item ids to exclude (only heroes who have not purchased these items). See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | [optional] 
 **account_ids** | [**List[int]**](int.md)| Comma separated list of account ids to include | [optional] 

### Return type

[**Dict[str, HashMapValue]**](HashMapValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hero Stats |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch player stats metrics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

