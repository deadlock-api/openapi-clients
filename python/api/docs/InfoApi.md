# deadlock-api-client.InfoApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check**](InfoApi.md#health_check) | **GET** /v1/info/health | Health Check
[**info**](InfoApi.md#info) | **GET** /v1/info | API Info


# **health_check**
> Status health_check()

Health Check

 Checks the health of the services.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example


```python
import deadlock-api-client
from deadlock-api-client.models.status import Status
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
    api_instance = deadlock-api-client.InfoApi(api_client)

    try:
        # Health Check
        api_response = api_instance.health_check()
        print("The response of InfoApi->health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->health_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info**
> APIInfo info()

API Info

 Returns information about the API.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example


```python
import deadlock-api-client
from deadlock-api-client.models.api_info import APIInfo
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
    api_instance = deadlock-api-client.InfoApi(api_client)

    try:
        # API Info
        api_response = api_instance.info()
        print("The response of InfoApi->info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**APIInfo**](APIInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

