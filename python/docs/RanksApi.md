# deadlock_api_client.RanksApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rank**](RanksApi.md#get_rank) | **GET** /v1/assets/ranks/{tier} | Get Rank
[**list_ranks**](RanksApi.md#list_ranks) | **GET** /v1/assets/ranks | List Ranks


# **get_rank**
> Rank get_rank(tier, language=language, client_version=client_version)

Get Rank

Returns a single rank by tier index.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.rank import Rank
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
    api_instance = deadlock_api_client.RanksApi(api_client)
    tier = 56 # int | Rank tier (0-11)
    language = 'language_example' # str | Language code. Defaults to `english`. (optional)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # Get Rank
        api_response = api_instance.get_rank(tier, language=language, client_version=client_version)
        print("The response of RanksApi->get_rank:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RanksApi->get_rank: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tier** | **int**| Rank tier (0-11) | 
 **language** | **str**| Language code. Defaults to &#x60;english&#x60;. | [optional] 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**Rank**](Rank.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Unknown tier or client_version |  -  |
**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ranks**
> List[Rank] list_ranks(language=language, client_version=client_version)

List Ranks

Returns the 12 player ranks (tier, localized name, badge image URLs, hex color).

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.rank import Rank
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
    api_instance = deadlock_api_client.RanksApi(api_client)
    language = 'language_example' # str | Language code. Defaults to `english`. (optional)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # List Ranks
        api_response = api_instance.list_ranks(language=language, client_version=client_version)
        print("The response of RanksApi->list_ranks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RanksApi->list_ranks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Language code. Defaults to &#x60;english&#x60;. | [optional] 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**List[Rank]**](Rank.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Requested client_version is not available |  -  |
**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

