# deadlock_api_client.RankedSeasonsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_ranked_seasons**](RankedSeasonsApi.md#list_ranked_seasons) | **GET** /v1/assets/ranked-seasons | List Ranked Seasons


# **list_ranked_seasons**
> List[RankedSeason] list_ranked_seasons(language=language, client_version=client_version)

List Ranked Seasons

Returns the ranked season definitions used by the game client, parsed from the patch's KV3 source files. Each season carries its eligibility requirements and the intervals it runs for, as unix timestamps in seconds.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.ranked_season import RankedSeason
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
    api_instance = deadlock_api_client.RankedSeasonsApi(api_client)
    language = 'language_example' # str | Language code. Defaults to `english`. (optional)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # List Ranked Seasons
        api_response = api_instance.list_ranked_seasons(language=language, client_version=client_version)
        print("The response of RankedSeasonsApi->list_ranked_seasons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RankedSeasonsApi->list_ranked_seasons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Language code. Defaults to &#x60;english&#x60;. | [optional] 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**List[RankedSeason]**](RankedSeason.md)

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

