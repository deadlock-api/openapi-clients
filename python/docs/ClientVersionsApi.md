# deadlock_api_client.ClientVersionsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_client_versions**](ClientVersionsApi.md#list_client_versions) | **GET** /v1/assets/client-versions | List Client Versions


# **list_client_versions**
> List[int] list_client_versions()

List Client Versions

Returns all known Deadlock client/game versions for which versioned assets are available, sorted ascending (oldest first).

### Example


```python
import deadlock_api_client
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
    api_instance = deadlock_api_client.ClientVersionsApi(api_client)

    try:
        # List Client Versions
        api_response = api_instance.list_client_versions()
        print("The response of ClientVersionsApi->list_client_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientVersionsApi->list_client_versions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

