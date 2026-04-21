# deadlock_api_client.ServersApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingest**](ServersApi.md#ingest) | **POST** /v1/servers/metrics | Game Server Metric Ingest
[**list**](ServersApi.md#list) | **GET** /v1/servers | List Game Servers
[**status**](ServersApi.md#status) | **POST** /v1/servers/status | Game Server Status
[**steam_list**](ServersApi.md#steam_list) | **GET** /v1/servers/steam | List Steam Game Servers


# **ingest**
> ingest(metric_ingest_request)

Game Server Metric Ingest


Ingests a single metric event reported by a game server. The schema is intentionally
flexible: `metric_value` carries the primary numeric measurement and `metadata` holds
arbitrary key/value context that varies per game mode or metric. Optional `map` and
`game_mode_version` let callers segment leaderboards per map or per ruleset revision.
Requires a valid game server secret as a Bearer token.
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.metric_ingest_request import MetricIngestRequest
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
    metric_ingest_request = deadlock_api_client.MetricIngestRequest() # MetricIngestRequest | 

    try:
        # Game Server Metric Ingest
        api_instance.ingest(metric_ingest_request)
    except Exception as e:
        print("Exception when calling ServersApi->ingest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_ingest_request** | [**MetricIngestRequest**](MetricIngestRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Metric accepted for ingestion. |  -  |
**400** | Invalid request body. |  -  |
**401** | Invalid or missing game server secret. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **steam_list**
> List[SteamServer] steam_list()

List Steam Game Servers


Returns the list of Deadlock game servers registered with the Steam master server
(`IGameServersService/GetServerList`), filtered to Deadlock's appid.
    

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.steam_server import SteamServer
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
        # List Steam Game Servers
        api_response = api_instance.steam_list()
        print("The response of ServersApi->steam_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->steam_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SteamServer]**](SteamServer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** | Fetching the Steam server list failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

