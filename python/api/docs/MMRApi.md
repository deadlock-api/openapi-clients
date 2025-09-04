# deadlock-api-client.MMRApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hero_mmr**](MMRApi.md#hero_mmr) | **GET** /v1/players/mmr/{hero_id} | Hero MMR
[**hero_mmr_history**](MMRApi.md#hero_mmr_history) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History
[**mmr**](MMRApi.md#mmr) | **GET** /v1/players/mmr | MMR
[**mmr_history**](MMRApi.md#mmr_history) | **GET** /v1/players/{account_id}/mmr-history | MMR History


# **hero_mmr**
> List[MMRHistory] hero_mmr(account_ids, hero_id, max_match_id=max_match_id)

Hero MMR

Batch Player Hero MMR

### Example


```python
import deadlock-api-client
from deadlock-api-client.models.mmr_history import MMRHistory
from deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock-api-client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock-api-client.MMRApi(api_client)
    account_ids = [56] # List[int] | Comma separated list of account ids, Account IDs are in `SteamID3` format.
    hero_id = 56 # int | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>
    max_match_id = 56 # int | Filter matches based on their ID. (optional)

    try:
        # Hero MMR
        api_response = api_instance.hero_mmr(account_ids, hero_id, max_match_id=max_match_id)
        print("The response of MMRApi->hero_mmr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MMRApi->hero_mmr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_ids** | [**List[int]**](int.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | 
 **hero_id** | **int**| The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 

### Return type

[**List[MMRHistory]**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hero MMR |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch hero mmr |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hero_mmr_history**
> List[MMRHistory] hero_mmr_history(account_id, hero_id, start=start, limit=limit)

Hero MMR History

Player Hero MMR History

### Example


```python
import deadlock-api-client
from deadlock-api-client.models.mmr_history import MMRHistory
from deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock-api-client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock-api-client.MMRApi(api_client)
    account_id = 56 # int | The players `SteamID3`
    hero_id = 56 # int | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>
    start = 56 # int | The index of the first match to return. (optional)
    limit = 100 # int | The maximum number of matches to return. (optional) (default to 100)

    try:
        # Hero MMR History
        api_response = api_instance.hero_mmr_history(account_id, hero_id, start=start, limit=limit)
        print("The response of MMRApi->hero_mmr_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MMRApi->hero_mmr_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The players &#x60;SteamID3&#x60; | 
 **hero_id** | **int**| The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
 **start** | **int**| The index of the first match to return. | [optional] 
 **limit** | **int**| The maximum number of matches to return. | [optional] [default to 100]

### Return type

[**List[MMRHistory]**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hero MMR History |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch hero mmr history |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mmr**
> List[MMRHistory] mmr(account_ids, max_match_id=max_match_id)

MMR

Batch Player MMR

### Example


```python
import deadlock-api-client
from deadlock-api-client.models.mmr_history import MMRHistory
from deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock-api-client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock-api-client.MMRApi(api_client)
    account_ids = [56] # List[int] | Comma separated list of account ids, Account IDs are in `SteamID3` format.
    max_match_id = 56 # int | Filter matches based on their ID. (optional)

    try:
        # MMR
        api_response = api_instance.mmr(account_ids, max_match_id=max_match_id)
        print("The response of MMRApi->mmr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MMRApi->mmr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_ids** | [**List[int]**](int.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 

### Return type

[**List[MMRHistory]**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MMR |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch mmr |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mmr_history**
> List[MMRHistory] mmr_history(account_id, start=start, limit=limit)

MMR History

Player MMR History

### Example


```python
import deadlock-api-client
from deadlock-api-client.models.mmr_history import MMRHistory
from deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock-api-client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock-api-client.MMRApi(api_client)
    account_id = 56 # int | The players `SteamID3`
    start = 56 # int | The index of the first match to return. (optional)
    limit = 100 # int | The maximum number of matches to return. (optional) (default to 100)

    try:
        # MMR History
        api_response = api_instance.mmr_history(account_id, start=start, limit=limit)
        print("The response of MMRApi->mmr_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MMRApi->mmr_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The players &#x60;SteamID3&#x60; | 
 **start** | **int**| The index of the first match to return. | [optional] 
 **limit** | **int**| The maximum number of matches to return. | [optional] [default to 100]

### Return type

[**List[MMRHistory]**](MMRHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MMR History |  -  |
**400** | Provided parameters are invalid. |  -  |
**500** | Failed to fetch mmr history |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

