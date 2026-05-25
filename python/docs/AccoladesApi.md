# deadlock_api_client.AccoladesApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accolade**](AccoladesApi.md#get_accolade) | **GET** /v1/assets/accolades/{accolade_id} | Get Accolade
[**get_accolade_by_name**](AccoladesApi.md#get_accolade_by_name) | **GET** /v1/assets/accolades/by-name/{name} | Get Accolade By Name
[**list_accolades**](AccoladesApi.md#list_accolades) | **GET** /v1/assets/accolades | List Accolades


# **get_accolade**
> Accolade get_accolade(accolade_id, language=language, client_version=client_version)

Get Accolade

Returns a single accolade by id.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.accolade import Accolade
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
    api_instance = deadlock_api_client.AccoladesApi(api_client)
    accolade_id = 56 # int | Accolade id (`m_unAccoladeID`)
    language = 'language_example' # str | Language code. Defaults to `english`. (optional)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # Get Accolade
        api_response = api_instance.get_accolade(accolade_id, language=language, client_version=client_version)
        print("The response of AccoladesApi->get_accolade:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccoladesApi->get_accolade: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accolade_id** | **int**| Accolade id (&#x60;m_unAccoladeID&#x60;) | 
 **language** | **str**| Language code. Defaults to &#x60;english&#x60;. | [optional] 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**Accolade**](Accolade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Unknown accolade id or client_version |  -  |
**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accolade_by_name**
> Accolade get_accolade_by_name(name, language=language, client_version=client_version)

Get Accolade By Name

Returns a single accolade by `class_name` or `tracked_stat_name` (case-insensitive).

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.accolade import Accolade
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
    api_instance = deadlock_api_client.AccoladesApi(api_client)
    name = 'name_example' # str | Accolade `class_name` (e.g. `kills`) or `tracked_stat_name`
    language = 'language_example' # str | Language code. Defaults to `english`. (optional)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # Get Accolade By Name
        api_response = api_instance.get_accolade_by_name(name, language=language, client_version=client_version)
        print("The response of AccoladesApi->get_accolade_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccoladesApi->get_accolade_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Accolade &#x60;class_name&#x60; (e.g. &#x60;kills&#x60;) or &#x60;tracked_stat_name&#x60; | 
 **language** | **str**| Language code. Defaults to &#x60;english&#x60;. | [optional] 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**Accolade**](Accolade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Unknown accolade name or client_version |  -  |
**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_accolades**
> List[Accolade] list_accolades(language=language, client_version=client_version)

List Accolades

Returns the per-accolade metadata used by the game client, parsed from the patch's KV3 source files.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.accolade import Accolade
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
    api_instance = deadlock_api_client.AccoladesApi(api_client)
    language = 'language_example' # str | Language code. Defaults to `english`. (optional)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # List Accolades
        api_response = api_instance.list_accolades(language=language, client_version=client_version)
        print("The response of AccoladesApi->list_accolades:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccoladesApi->list_accolades: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Language code. Defaults to &#x60;english&#x60;. | [optional] 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**List[Accolade]**](Accolade.md)

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

