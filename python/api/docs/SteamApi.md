# deadlock_api_client.SteamApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**steam**](SteamApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile
[**steam_search**](SteamApi.md#steam_search) | **GET** /v1/players/steam-search | Steam Profile Search


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
    api_instance = deadlock_api_client.SteamApi(api_client)
    account_ids = [56] # List[int] | Comma separated list of account ids, Account IDs are in `SteamID3` format.

    try:
        # Batch Steam Profile
        api_response = api_instance.steam(account_ids)
        print("The response of SteamApi->steam:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SteamApi->steam: %s\n" % e)
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
    api_instance = deadlock_api_client.SteamApi(api_client)
    search_query = 'search_query_example' # str | Search query for Steam profiles.

    try:
        # Steam Profile Search
        api_response = api_instance.steam_search(search_query)
        print("The response of SteamApi->steam_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SteamApi->steam_search: %s\n" % e)
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

