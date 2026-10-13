# deadlock_api_client.ConvarsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_convar**](ConvarsApi.md#get_convar) | **GET** /v1/assets/convars/{name} | Get Convar
[**list_convars**](ConvarsApi.md#list_convars) | **GET** /v1/assets/convars | List Convars


# **get_convar**
> Convar get_convar(name, client_version=client_version)

Get Convar

Returns a single console variable by name (case-insensitive).

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.convar import Convar
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
    api_instance = deadlock_api_client.ConvarsApi(api_client)
    name = 'name_example' # str | Convar name, e.g. `citadel_corrupted_item_shop_restock_interval`
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # Get Convar
        api_response = api_instance.get_convar(name, client_version=client_version)
        print("The response of ConvarsApi->get_convar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConvarsApi->get_convar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Convar name, e.g. &#x60;citadel_corrupted_item_shop_restock_interval&#x60; | 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**Convar**](Convar.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Unknown convar or client_version, or no convars data for that version |  -  |
**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_convars**
> Dict[str, Convar] list_convars(client_version=client_version)

List Convars

Returns every console variable registered by the patch's `client.dll` and `server.dll`, keyed by name, with its type, compiled-in default value, `FCVAR_*` flags and help text. These are the defaults the binaries ship with; servers and game modes can override them at runtime.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.convar import Convar
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
    api_instance = deadlock_api_client.ConvarsApi(api_client)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # List Convars
        api_response = api_instance.list_convars(client_version=client_version)
        print("The response of ConvarsApi->list_convars:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConvarsApi->list_convars: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**Dict[str, Convar]**](Convar.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Requested client_version is not available, or it has no convars data (extracted from build 6774 on) |  -  |
**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

