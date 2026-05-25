# deadlock_api_client.SteamApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**steam**](SteamApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile
[**steam_search**](SteamApi.md#steam_search) | **GET** /v1/players/steam-search | Steam Profile Search


# **steam**
> List[SteamProfile] steam(account_ids, refresh=refresh)

Batch Steam Profile


This endpoint returns Steam profiles of players.

Pass `refresh=true` to force a live refresh of the listed accounts from the
Steam Web API (`GetPlayerSummaries` + `GetFriendList`) before returning. The
refreshed rows are persisted to the `steam_profiles` table and returned in the
response with `last_updated` set to the current time. Refresh requests are
rate limited and capped at 100 account ids per call to stay inside the
shared Steam Web API key budget.

See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s (read path), 3req/min + 15req/h (refresh) |
| Key | - (read path), 10req/min + 60req/h (refresh) |
| Global | - (read path), 30req/min + 200req/h (refresh) |
    

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
    api_instance = deadlock_api_client.SteamApi(api_client)
    account_ids = [56] # List[int] | Comma separated list of account ids, Account IDs are in `SteamID3` format.
    refresh = True # bool | Refresh the listed profiles from the Steam Web API before returning. (optional)

    try:
        # Batch Steam Profile
        api_response = api_instance.steam(account_ids, refresh=refresh)
        print("The response of SteamApi->steam:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SteamApi->steam: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_ids** | [**List[int]**](int.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | 
 **refresh** | **bool**| Refresh the listed profiles from the Steam Web API before returning. | [optional] 

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
**429** | Rate limit exceeded (only enforced when refresh&#x3D;true). |  -  |
**500** | Failed to fetch steam profiles. |  -  |
**502** | Steam Web API call failed (only when refresh&#x3D;true). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **steam_search**
> List[SteamProfile] steam_search(search_query, limit=limit, min_matches_played_last_30d=min_matches_played_last_30d, min_last_team_avg_badge=min_last_team_avg_badge, matches_played_weight=matches_played_weight)

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
    api_instance = deadlock_api_client.SteamApi(api_client)
    search_query = 'search_query_example' # str | Search query for Steam profiles.
    limit = 100 # int | Maximum number of profiles to return. (optional) (default to 100)
    min_matches_played_last_30d = 5 # int | Only return profiles that have played at least this many matches in the last 30 days. Defaults to 5 to filter out inactive/empty profiles and keep search responsive. (optional) (default to 5)
    min_last_team_avg_badge = 0 # int | Only return profiles whose `last_team_avg_badge` is at least this value. Defaults to 0 (no filter). Profiles with no recorded badge are stored as 0 and are excluded when this is set above 0. (optional) (default to 0)
    matches_played_weight = 0.02 # float | Weight applied to `log1p(matches_played_last_30d)` when reranking candidates. The final score per profile is `jaro_winkler(personaname_lc, query) + weight * log1p(matches_played)`. Set to 0 to rank purely by string similarity; raise it to bias toward active/popular players. (optional) (default to 0.02)

    try:
        # Steam Profile Search
        api_response = api_instance.steam_search(search_query, limit=limit, min_matches_played_last_30d=min_matches_played_last_30d, min_last_team_avg_badge=min_last_team_avg_badge, matches_played_weight=matches_played_weight)
        print("The response of SteamApi->steam_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SteamApi->steam_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_query** | **str**| Search query for Steam profiles. | 
 **limit** | **int**| Maximum number of profiles to return. | [optional] [default to 100]
 **min_matches_played_last_30d** | **int**| Only return profiles that have played at least this many matches in the last 30 days. Defaults to 5 to filter out inactive/empty profiles and keep search responsive. | [optional] [default to 5]
 **min_last_team_avg_badge** | **int**| Only return profiles whose &#x60;last_team_avg_badge&#x60; is at least this value. Defaults to 0 (no filter). Profiles with no recorded badge are stored as 0 and are excluded when this is set above 0. | [optional] [default to 0]
 **matches_played_weight** | **float**| Weight applied to &#x60;log1p(matches_played_last_30d)&#x60; when reranking candidates. The final score per profile is &#x60;jaro_winkler(personaname_lc, query) + weight * log1p(matches_played)&#x60;. Set to 0 to rank purely by string similarity; raise it to bias toward active/popular players. | [optional] [default to 0.02]

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

