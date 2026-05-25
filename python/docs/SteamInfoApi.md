# deadlock_api_client.SteamInfoApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_steam_info**](SteamInfoApi.md#get_all_steam_info) | **GET** /v1/assets/steam-info/all | Get All Steam Infos
[**get_steam_info**](SteamInfoApi.md#get_steam_info) | **GET** /v1/assets/steam-info | Get Steam Info


# **get_all_steam_info**
> List[SteamInfo] get_all_steam_info()

Get All Steam Infos

Returns the `steam.inf` manifest for every known patch as a single array, newest version first. Replaces the legacy `/v1/steam-info/all` endpoint.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.steam_info import SteamInfo
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
    api_instance = deadlock_api_client.SteamInfoApi(api_client)

    try:
        # Get All Steam Infos
        api_response = api_instance.get_all_steam_info()
        print("The response of SteamInfoApi->get_all_steam_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SteamInfoApi->get_all_steam_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SteamInfo]**](SteamInfo.md)

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

# **get_steam_info**
> SteamInfo get_steam_info(client_version=client_version)

Get Steam Info

Returns the `steam.inf` manifest published with the patch (client/server version, app IDs, source revision, build timestamp).

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.steam_info import SteamInfo
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
    api_instance = deadlock_api_client.SteamInfoApi(api_client)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # Get Steam Info
        api_response = api_instance.get_steam_info(client_version=client_version)
        print("The response of SteamInfoApi->get_steam_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SteamInfoApi->get_steam_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**SteamInfo**](SteamInfo.md)

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

