# deadlock-api-client.PatchesApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**big_patch_days**](PatchesApi.md#big_patch_days) | **GET** /v1/patches/big-days | Big Days
[**feed**](PatchesApi.md#feed) | **GET** /v1/patches | Notes


# **big_patch_days**
> List[str] big_patch_days()

Big Days

 Returns a list of dates where Deadlock's \"big\" patch days were, usually bi-weekly. The exact date is the time when the announcement forum post was published.  This list is manually maintained, and so new patch dates may be delayed by a few hours.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example


```python
import deadlock-api-client
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
    api_instance = deadlock-api-client.PatchesApi(api_client)

    try:
        # Big Days
        api_response = api_instance.big_patch_days()
        print("The response of PatchesApi->big_patch_days:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatchesApi->big_patch_days: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feed**
> List[Patch] feed()

Notes

 Returns the parsed result of the RSS Feed from the official Forum.  RSS-Feed: https://forums.playdeadlock.com/forums/changelog.10/index.rss  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example


```python
import deadlock-api-client
from deadlock-api-client.models.patch import Patch
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
    api_instance = deadlock-api-client.PatchesApi(api_client)

    try:
        # Notes
        api_response = api_instance.feed()
        print("The response of PatchesApi->feed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatchesApi->feed: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Patch]**](Patch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** | Fetching or parsing the RSS-Feed failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

