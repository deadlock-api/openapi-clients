# deadlock-api-client.MMRApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hero_mmr**](MMRApi.md#hero_mmr) | **GET** /v1/players/mmr/distribution/{hero_id} | Hero MMR Distribution
[**hero_mmr_0**](MMRApi.md#hero_mmr_0) | **GET** /v1/players/mmr/{hero_id} | Batch Hero MMR
[**hero_mmr_history**](MMRApi.md#hero_mmr_history) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History
[**mmr**](MMRApi.md#mmr) | **GET** /v1/players/mmr | Batch MMR
[**mmr_0**](MMRApi.md#mmr_0) | **GET** /v1/players/mmr/distribution | MMR Distribution
[**mmr_history**](MMRApi.md#mmr_history) | **GET** /v1/players/{account_id}/mmr-history | MMR History


# **hero_mmr**
> List[DistributionEntry] hero_mmr(hero_id, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, is_high_skill_range_parties=is_high_skill_range_parties, is_low_pri_pool=is_low_pri_pool, is_new_player_pool=is_new_player_pool, min_match_id=min_match_id, max_match_id=max_match_id)

Hero MMR Distribution


Player Hero MMR Distribution


### Example


```python
import deadlock-api-client
from deadlock-api-client.models.distribution_entry import DistributionEntry
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
    hero_id = 56 # int | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>
    min_unix_timestamp = 1759795200 # int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1759795200)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    is_high_skill_range_parties = True # bool | Filter matches based on whether they are in the high skill range. (optional)
    is_low_pri_pool = True # bool | Filter matches based on whether they are in the low priority pool. (optional)
    is_new_player_pool = True # bool | Filter matches based on whether they are in the new player pool. (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)

    try:
        # Hero MMR Distribution
        api_response = api_instance.hero_mmr(hero_id, min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, is_high_skill_range_parties=is_high_skill_range_parties, is_low_pri_pool=is_low_pri_pool, is_new_player_pool=is_new_player_pool, min_match_id=min_match_id, max_match_id=max_match_id)
        print("The response of MMRApi->hero_mmr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MMRApi->hero_mmr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_id** | **int**| The hero ID to fetch the MMR history for. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1759795200]
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **is_high_skill_range_parties** | **bool**| Filter matches based on whether they are in the high skill range. | [optional] 
 **is_low_pri_pool** | **bool**| Filter matches based on whether they are in the low priority pool. | [optional] 
 **is_new_player_pool** | **bool**| Filter matches based on whether they are in the new player pool. | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 

### Return type

[**List[DistributionEntry]**](DistributionEntry.md)

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

# **hero_mmr_0**
> List[MMRHistory] hero_mmr_0(account_ids, hero_id, max_match_id=max_match_id)

Batch Hero MMR


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
        # Batch Hero MMR
        api_response = api_instance.hero_mmr_0(account_ids, hero_id, max_match_id=max_match_id)
        print("The response of MMRApi->hero_mmr_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MMRApi->hero_mmr_0: %s\n" % e)
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
> List[MMRHistory] hero_mmr_history(account_id, hero_id)

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

    try:
        # Hero MMR History
        api_response = api_instance.hero_mmr_history(account_id, hero_id)
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

Batch MMR


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
        # Batch MMR
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

# **mmr_0**
> List[DistributionEntry] mmr_0(min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, is_high_skill_range_parties=is_high_skill_range_parties, is_low_pri_pool=is_low_pri_pool, is_new_player_pool=is_new_player_pool, min_match_id=min_match_id, max_match_id=max_match_id)

MMR Distribution


Player MMR Distribution


### Example


```python
import deadlock-api-client
from deadlock-api-client.models.distribution_entry import DistributionEntry
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
    min_unix_timestamp = 1759795200 # int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. (optional) (default to 1759795200)
    max_unix_timestamp = 56 # int | Filter matches based on their start time (Unix timestamp). (optional)
    min_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    max_duration_s = 56 # int | Filter matches based on their duration in seconds (up to 7000s). (optional)
    is_high_skill_range_parties = True # bool | Filter matches based on whether they are in the high skill range. (optional)
    is_low_pri_pool = True # bool | Filter matches based on whether they are in the low priority pool. (optional)
    is_new_player_pool = True # bool | Filter matches based on whether they are in the new player pool. (optional)
    min_match_id = 56 # int | Filter matches based on their ID. (optional)
    max_match_id = 56 # int | Filter matches based on their ID. (optional)

    try:
        # MMR Distribution
        api_response = api_instance.mmr_0(min_unix_timestamp=min_unix_timestamp, max_unix_timestamp=max_unix_timestamp, min_duration_s=min_duration_s, max_duration_s=max_duration_s, is_high_skill_range_parties=is_high_skill_range_parties, is_low_pri_pool=is_low_pri_pool, is_new_player_pool=is_new_player_pool, min_match_id=min_match_id, max_match_id=max_match_id)
        print("The response of MMRApi->mmr_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MMRApi->mmr_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. | [optional] [default to 1759795200]
 **max_unix_timestamp** | **int**| Filter matches based on their start time (Unix timestamp). | [optional] 
 **min_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **max_duration_s** | **int**| Filter matches based on their duration in seconds (up to 7000s). | [optional] 
 **is_high_skill_range_parties** | **bool**| Filter matches based on whether they are in the high skill range. | [optional] 
 **is_low_pri_pool** | **bool**| Filter matches based on whether they are in the low priority pool. | [optional] 
 **is_new_player_pool** | **bool**| Filter matches based on whether they are in the new player pool. | [optional] 
 **min_match_id** | **int**| Filter matches based on their ID. | [optional] 
 **max_match_id** | **int**| Filter matches based on their ID. | [optional] 

### Return type

[**List[DistributionEntry]**](DistributionEntry.md)

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
> List[MMRHistory] mmr_history(account_id)

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

    try:
        # MMR History
        api_response = api_instance.mmr_history(account_id)
        print("The response of MMRApi->mmr_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MMRApi->mmr_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The players &#x60;SteamID3&#x60; | 

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

