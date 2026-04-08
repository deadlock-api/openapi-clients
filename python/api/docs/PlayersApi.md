# deadlock_api_client.PlayersApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_stats**](PlayersApi.md#account_stats) | **GET** /v1/players/{account_id}/account-stats | Account Stats
[**card**](PlayersApi.md#card) | **GET** /v1/players/{account_id}/card | Card
[**enemy_stats**](PlayersApi.md#enemy_stats) | **GET** /v1/players/{account_id}/enemy-stats | Enemy Stats
[**match_history**](PlayersApi.md#match_history) | **GET** /v1/players/{account_id}/match-history | Match History
[**mate_stats**](PlayersApi.md#mate_stats) | **GET** /v1/players/{account_id}/mate-stats | Mate Stats
[**player_hero_stats**](PlayersApi.md#player_hero_stats) | **GET** /v1/players/hero-stats | Hero Stats
[**rank_predict**](PlayersApi.md#rank_predict) | **GET** /v1/players/{account_id}/rank-predict | Rank Predict


# **account_stats**
> List[PlayerAccountStats] account_stats(account_id)

Account Stats


This endpoint returns the player account stats for the given `account_id`.

!THIS IS A PATREON ONLY ENDPOINT!

You have to be friend with one of the bots to use this endpoint.
On first use this endpoint will return an error with a list of invite links to add the bot as friend.
From then on you can use this endpoint.

Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

Relevant Protobuf Messages:
- CMsgClientToGcGetAccountStats
- CMsgAccountStats

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 5req/min |
| Key | 20req/min & 800req/h |
| Global | 200req/min |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.player_account_stats import PlayerAccountStats
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
    api_instance = deadlock_api_client.PlayersApi(api_client)
    account_id = 56 # int | The players `SteamID3`

    try:
        # Account Stats
        api_response = api_instance.account_stats(account_id)
        print("The response of PlayersApi->account_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->account_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The players &#x60;SteamID3&#x60; | 

### Return type

[**List[PlayerAccountStats]**](PlayerAccountStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Provided parameters are invalid. |  -  |
**403** | Account is not a Patreon subscriber or not prioritized. |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Fetching account stats failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **card**
> List[PlayerCard] card(account_id)

Card


This endpoint returns the player card for the given `account_id`.

!THIS IS A PATREON ONLY ENDPOINT!

You have to be friend with one of the bots to use this endpoint.
On first use this endpoint will return an error with a list of invite links to add the bot as friend.
From then on you can use this endpoint.

Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

Relevant Protobuf Messages:
- CMsgClientToGcGetProfileCard
- CMsgCitadelProfileCard

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 5req/min |
| Key | 20req/min & 800req/h |
| Global | 200req/min |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.player_card import PlayerCard
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
    api_instance = deadlock_api_client.PlayersApi(api_client)
    account_id = 56 # int | The players `SteamID3`

    try:
        # Card
        api_response = api_instance.card(account_id)
        print("The response of PlayersApi->card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The players &#x60;SteamID3&#x60; | 

### Return type

[**List[PlayerCard]**](PlayerCard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Provided parameters are invalid. |  -  |
**403** | Account is not a Patreon subscriber or not prioritized. |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Fetching card failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enemy_stats**
> List[EnemyStats] enemy_stats(account_id, game_mode=game_mode, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_match_id=min_match_id, max_match_id=max_match_id, min_matches_played=min_matches_played, max_matches_played=max_matches_played)

Enemy Stats


This endpoint returns the enemy stats.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.enemy_stats import EnemyStats
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
    api_instance = deadlock_api_client.PlayersApi(api_client)
    account_id = 56 # int | The players `SteamID3`
    game_mode = 'game_mode_example' # str | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. (optional)
    min_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)
    min_matches_played = 56 # int | Filter based on the number of matches played. (optional)
    max_matches_played = 56 # int | Filter based on the number of matches played. (optional)

    try:
        # Enemy Stats
        api_response = api_instance.enemy_stats(account_id, game_mode=game_mode, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_match_id=min_match_id, max_match_id=max_match_id, min_matches_played=min_matches_played, max_matches_played=max_matches_played)
        print("The response of PlayersApi->enemy_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->enemy_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The players &#x60;SteamID3&#x60; | 
 **game_mode** | **str**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] 
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **min_matches_played** | **int**| Filter based on the number of matches played. | [optional] 
 **max_matches_played** | **int**| Filter based on the number of matches played. | [optional] 

### Return type

[**List[EnemyStats]**](EnemyStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Enemy Stats |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch enemy stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_history**
> List[PlayerMatchHistoryEntry] match_history(account_id, force_refetch=force_refetch, only_stored_history=only_stored_history)

Match History


This endpoint returns the player match history for the given `account_id`.

The player match history is a combination of the data from **Steam** and **ClickHouse**, so you always get the most up-to-date data and full history.

Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

Relevant Protobuf Messages:
- CMsgClientToGcGetMatchHistory
- CMsgClientToGcGetMatchHistoryResponse

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 3req/h<br>With `only_stored_history=true`: 100req/s<br>With `force_refetch=true`: 1req/h |
| Key | 300req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 5req/h |
| Global | 1500req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 10req/h |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.player_match_history_entry import PlayerMatchHistoryEntry
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
    api_instance = deadlock_api_client.PlayersApi(api_client)
    account_id = 56 # int | The players `SteamID3`
    force_refetch = True # bool | Refetch the match history from Steam, even if it is already cached in `ClickHouse`. Only use this if you are sure that the data in `ClickHouse` is outdated. Enabling this flag results in a strict rate limit. (optional)
    only_stored_history = True # bool | Return only the already stored match history from `ClickHouse`. There is no rate limit for this option, so if you need a lot of data, you can use this option. This option is not compatible with `force_refetch`. (optional)

    try:
        # Match History
        api_response = api_instance.match_history(account_id, force_refetch=force_refetch, only_stored_history=only_stored_history)
        print("The response of PlayersApi->match_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->match_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The players &#x60;SteamID3&#x60; | 
 **force_refetch** | **bool**| Refetch the match history from Steam, even if it is already cached in &#x60;ClickHouse&#x60;. Only use this if you are sure that the data in &#x60;ClickHouse&#x60; is outdated. Enabling this flag results in a strict rate limit. | [optional] 
 **only_stored_history** | **bool**| Return only the already stored match history from &#x60;ClickHouse&#x60;. There is no rate limit for this option, so if you need a lot of data, you can use this option. This option is not compatible with &#x60;force_refetch&#x60;. | [optional] 

### Return type

[**List[PlayerMatchHistoryEntry]**](PlayerMatchHistoryEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Provided parameters are invalid. |  -  |
**429** | Rate limit exceeded. Returns stored match history from ClickHouse as a fallback. When &#x60;force_refetch&#x3D;true&#x60;, returns an error instead. |  -  |
**500** | Fetching player match history failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mate_stats**
> List[MateStats] mate_stats(account_id, game_mode=game_mode, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_match_id=min_match_id, max_match_id=max_match_id, min_matches_played=min_matches_played, max_matches_played=max_matches_played)

Mate Stats


This endpoint returns the mate stats.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.mate_stats import MateStats
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
    api_instance = deadlock_api_client.PlayersApi(api_client)
    account_id = 56 # int | The players `SteamID3`
    game_mode = 'game_mode_example' # str | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. (optional)
    min_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)
    min_matches_played = 56 # int | Filter based on the number of matches played. (optional)
    max_matches_played = 56 # int | Filter based on the number of matches played. (optional)

    try:
        # Mate Stats
        api_response = api_instance.mate_stats(account_id, game_mode=game_mode, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_match_id=min_match_id, max_match_id=max_match_id, min_matches_played=min_matches_played, max_matches_played=max_matches_played)
        print("The response of PlayersApi->mate_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->mate_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The players &#x60;SteamID3&#x60; | 
 **game_mode** | **str**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] 
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **min_matches_played** | **int**| Filter based on the number of matches played. | [optional] 
 **max_matches_played** | **int**| Filter based on the number of matches played. | [optional] 

### Return type

[**List[MateStats]**](MateStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mate Stats |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch mate stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_hero_stats**
> List[HeroStats] player_hero_stats(account_ids, game_mode=game_mode, hero_ids=hero_ids, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id)

Hero Stats


This endpoint returns statistics for each hero played by a given player account.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.hero_stats import HeroStats
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
    api_instance = deadlock_api_client.PlayersApi(api_client)
    account_ids = [56] # List[int] | Comma separated list of account ids, Account IDs are in `SteamID3` format.
    game_mode = 'game_mode_example' # str | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`. (optional)
    hero_ids = 'hero_ids_example' # str | Filter matches based on the hero IDs. See more: <https://assets.deadlock-api.com/v2/heroes> (optional)
    min_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    min_networth = 56 # int | Filter players based on their final net worth. (optional)
    max_networth = 56 # int | Filter players based on their final net worth. (optional)
    min_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    max_average_badge = 56 # int | Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks> (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)

    try:
        # Hero Stats
        api_response = api_instance.player_hero_stats(account_ids, game_mode=game_mode, hero_ids=hero_ids, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_networth=min_networth, max_networth=max_networth, min_average_badge=min_average_badge, max_average_badge=max_average_badge, min_match_id=min_match_id, max_match_id=max_match_id)
        print("The response of PlayersApi->player_hero_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->player_hero_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_ids** | [**List[int]**](int.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | 
 **game_mode** | **str**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. **Default:** &#x60;normal&#x60;. | [optional] 
 **hero_ids** | **str**| Filter matches based on the hero IDs. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] 
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **min_networth** | **int**| Filter players based on their final net worth. | [optional] 
 **max_networth** | **int**| Filter players based on their final net worth. | [optional] 
 **min_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **max_average_badge** | **int**| Filter matches based on the average badge level (tier &#x3D; first digits, subtier &#x3D; last digit) of *both* teams involved. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 

### Return type

[**List[HeroStats]**](HeroStats.md)

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

# **rank_predict**
> RankPredictResponse rank_predict(account_id)

Rank Predict


Predicts a player's current rank badge from their last 30 ranked/unranked matches.
Requires at least 30 eligible matches (Ranked or Unranked, Normal game mode) with valid badge data.

> **This is an ML prediction and may be inaccurate.** The model has no access to the player's
> actual hidden MMR — it infers rank from match context signals only.

### Model Accuracy (5-fold cross-validation)

| Metric | Value |
|--------|-------|
| R²     | 0.940 |
| MAE    | 1.40 sub-ranks |
| RMSE   | 2.22 sub-ranks |
| Within ±1 sub-rank | 69.1% |
| Within ±3 sub-ranks | 90.4% |
| Within ±5 sub-ranks | 96.7% |
| Within ±6 sub-ranks | 97.7% |
| Within ±10 sub-ranks | 99.7% |

Accuracy by tier:

| Tier range | n | MAE |
|------------|---|-----|
| Low (1-4)  | 430 | 4.79 sub-ranks |
| Mid (5-7)  | 1350 | 3.11 sub-ranks |
| High (8-11)| 25020 | 1.25 sub-ranks |

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |


### Example


```python
import deadlock_api_client
from deadlock_api_client.models.rank_predict_response import RankPredictResponse
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
    api_instance = deadlock_api_client.PlayersApi(api_client)
    account_id = 56 # int | The players `SteamID3`

    try:
        # Rank Predict
        api_response = api_instance.rank_predict(account_id)
        print("The response of PlayersApi->rank_predict:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->rank_predict: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The players &#x60;SteamID3&#x60; | 

### Return type

[**RankPredictResponse**](RankPredictResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid account ID |  -  |
**403** | User is protected or endpoint unavailable |  -  |
**422** | Not enough recent ranked matches (need 30) |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Prediction failed |  -  |
**503** | Rank prediction model not loaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

