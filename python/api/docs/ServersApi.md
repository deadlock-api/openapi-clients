# deadlock_api_client.ServersApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](ServersApi.md#list) | **GET** /v1/servers | List Game Servers
[**status**](ServersApi.md#status) | **POST** /v1/servers/status | Game Server Status


# **list**
> ListServersResponse list()

List Game Servers

Returns all currently active game servers.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.list_servers_response import ListServersResponse
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
    api_instance = deadlock_api_client.ServersApi(api_client)

    try:
        # List Game Servers
        api_response = api_instance.list()
        print("The response of ServersApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListServersResponse**](ListServersResponse.md)

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

# **status**
> ServerStatusResponse status(server_status_request)

Game Server Status


Reports the current status of a game server.
Game servers must call this endpoint at least once every 30 seconds to remain active.
Requires a valid game server secret as a Bearer token.
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.server_status_request import ServerStatusRequest
from deadlock_api_client.models.server_status_response import ServerStatusResponse
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
    api_instance = deadlock_api_client.ServersApi(api_client)
    server_status_request = deadlock_api_client.ServerStatusRequest() # ServerStatusRequest | 

    try:
        # Game Server Status
        api_response = api_instance.status(server_status_request)
        print("The response of ServersApi->status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_status_request** | [**ServerStatusRequest**](ServerStatusRequest.md)|  | 

### Return type

[**ServerStatusResponse**](ServerStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid request body. |  -  |
**401** | Invalid or missing game server secret. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

