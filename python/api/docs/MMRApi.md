# openapi_client.MMRApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hero_mmr**](MMRApi.md#hero_mmr) | **GET** /v1/players/mmr/{hero_id} | Hero MMR
[**hero_mmr_history**](MMRApi.md#hero_mmr_history) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History
[**mmr**](MMRApi.md#mmr) | **GET** /v1/players/mmr | MMR
[**mmr_history**](MMRApi.md#mmr_history) | **GET** /v1/players/{account_id}/mmr-history | MMR History


# **hero_mmr**
> List[MMRHistory] hero_mmr(account_ids, hero_id)

Hero MMR

Batch Player Hero MMR

### Example


```python
import openapi_client
from openapi_client.models.mmr_history import MMRHistory
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MMRApi(api_client)
    account_ids = [56] # List[int] | Comma separated list of account ids, Account IDs are in `SteamID3` format.
    hero_id = 56 # int | The hero ID to fetch the MMR history for. See more: <https://assets.deadlock-api.com/v2/heroes>

    try:
        # Hero MMR
        api_response = api_instance.hero_mmr(account_ids, hero_id)
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
import openapi_client
from openapi_client.models.mmr_history import MMRHistory
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MMRApi(api_client)
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
> List[MMRHistory] mmr(account_ids)

MMR

Batch Player MMR

### Example


```python
import openapi_client
from openapi_client.models.mmr_history import MMRHistory
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MMRApi(api_client)
    account_ids = [56] # List[int] | Comma separated list of account ids, Account IDs are in `SteamID3` format.

    try:
        # MMR
        api_response = api_instance.mmr(account_ids)
        print("The response of MMRApi->mmr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MMRApi->mmr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_ids** | [**List[int]**](int.md)| Comma separated list of account ids, Account IDs are in &#x60;SteamID3&#x60; format. | 

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
> List[MMRHistory] mmr_history(account_id)

MMR History

Player MMR History

### Example


```python
import openapi_client
from openapi_client.models.mmr_history import MMRHistory
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MMRApi(api_client)
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

