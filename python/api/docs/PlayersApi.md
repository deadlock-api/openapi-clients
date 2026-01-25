# deadlock_api_client.PlayersApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enemy_stats**](PlayersApi.md#enemy_stats) | **GET** /v1/players/{account_id}/enemy-stats | Enemy Stats
[**match_history**](PlayersApi.md#match_history) | **GET** /v1/players/{account_id}/match-history | Match History
[**mate_stats**](PlayersApi.md#mate_stats) | **GET** /v1/players/{account_id}/mate-stats | Mate Stats
[**party_stats**](PlayersApi.md#party_stats) | **GET** /v1/players/{account_id}/party-stats | Party Stats
[**player_hero_stats**](PlayersApi.md#player_hero_stats) | **GET** /v1/players/hero-stats | Hero Stats
[**steam**](PlayersApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile
[**steam_search**](PlayersApi.md#steam_search) | **GET** /v1/players/steam-search | Steam Profile Search


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
    game_mode = 'game_mode_example' # str | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. If not specified, both are included. (optional)
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
 **game_mode** | **str**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. If not specified, both are included. | [optional] 
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
| IP | 5req/min<br>With `only_stored_history=true`: 100req/s<br>With `force_refetch=true`: 5req/h |
| Key | 50req/min & 1000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 5req/h |
| Global | 2000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 10req/h |
    

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
**429** | Rate limit exceeded |  -  |
**500** | Fetching player match history failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mate_stats**
> List[MateStats] mate_stats(account_id, game_mode=game_mode, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_match_id=min_match_id, max_match_id=max_match_id, min_matches_played=min_matches_played, max_matches_played=max_matches_played, same_party=same_party)

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
    game_mode = 'game_mode_example' # str | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. If not specified, both are included. (optional)
    min_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)
    min_matches_played = 56 # int | Filter based on the number of matches played. (optional)
    max_matches_played = 56 # int | Filter based on the number of matches played. (optional)
    same_party = True # bool | Filter based on whether the mates were on the same party. **Careful:** this will require us to use the match metadata, which can have missing matches. (optional) (default to True)

    try:
        # Mate Stats
        api_response = api_instance.mate_stats(account_id, game_mode=game_mode, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_match_id=min_match_id, max_match_id=max_match_id, min_matches_played=min_matches_played, max_matches_played=max_matches_played, same_party=same_party)
        print("The response of PlayersApi->mate_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->mate_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The players &#x60;SteamID3&#x60; | 
 **game_mode** | **str**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. If not specified, both are included. | [optional] 
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **min_matches_played** | **int**| Filter based on the number of matches played. | [optional] 
 **max_matches_played** | **int**| Filter based on the number of matches played. | [optional] 
 **same_party** | **bool**| Filter based on whether the mates were on the same party. **Careful:** this will require us to use the match metadata, which can have missing matches. | [optional] [default to True]

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

# **party_stats**
> List[PartyStats] party_stats(account_id, game_mode=game_mode, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_match_id=min_match_id, max_match_id=max_match_id)

Party Stats


This endpoint returns the party stats.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.party_stats import PartyStats
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
    game_mode = 'game_mode_example' # str | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. If not specified, both are included. (optional)
    min_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)

    try:
        # Party Stats
        api_response = api_instance.party_stats(account_id, game_mode=game_mode, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, min_match_id=min_match_id, max_match_id=max_match_id)
        print("The response of PlayersApi->party_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->party_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The players &#x60;SteamID3&#x60; | 
 **game_mode** | **str**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. If not specified, both are included. | [optional] 
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 

### Return type

[**List[PartyStats]**](PartyStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Party Stats |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch party stats |  -  |

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
    game_mode = 'game_mode_example' # str | Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. If not specified, both are included. (optional)
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
 **game_mode** | **str**| Filter matches based on their game mode. Valid values: &#x60;normal&#x60;, &#x60;street_brawl&#x60;. If not specified, both are included. | [optional] 
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

# **steam**
> List[SteamProfile] steam(account_ids)

Batch Steam Profile


This endpoint returns Steam profiles of players.

See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.steam_profile import SteamProfile
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

    try:
        # Batch Steam Profile
        api_response = api_instance.steam(account_ids)
        print("The response of PlayersApi->steam:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->steam: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_ids** | [**List[int]**](int.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | 

### Return type

[**List[SteamProfile]**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Steam Profiles |  -  |
**400** | Provided parameters are invalid. |  -  |
**404** | No Steam profile found. |  -  |
**500** | Failed to fetch steam profiles. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **steam_search**
> List[SteamProfile] steam_search(search_query)

Steam Profile Search


This endpoint lets you search for Steam profiles by account_id or personaname.

See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.steam_profile import SteamProfile
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
    search_query = 'search_query_example' # str | Search query for Steam profiles.

    try:
        # Steam Profile Search
        api_response = api_instance.steam_search(search_query)
        print("The response of PlayersApi->steam_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->steam_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_query** | **str**| Search query for Steam profiles. | 

### Return type

[**List[SteamProfile]**](SteamProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Steam Profile Search |  -  |
**400** | Provided parameters are invalid. |  -  |
**404** | No Steam profiles found. |  -  |
**500** | Failed to fetch steam profiles. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

