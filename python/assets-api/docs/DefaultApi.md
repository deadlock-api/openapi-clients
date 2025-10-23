# assets-deadlock-api-client.DefaultApi

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_build_tags_v2_build_tags_get**](DefaultApi.md#get_build_tags_v2_build_tags_get) | **GET** /v2/build-tags | Get Build Tags
[**get_client_versions_v2_client_versions_get**](DefaultApi.md#get_client_versions_v2_client_versions_get) | **GET** /v2/client-versions | Get Client Versions
[**get_colors_v1_colors_get**](DefaultApi.md#get_colors_v1_colors_get) | **GET** /v1/colors | Get Colors
[**get_icons_v1_icons_get**](DefaultApi.md#get_icons_v1_icons_get) | **GET** /v1/icons | Get Icons
[**get_map_v1_map_get**](DefaultApi.md#get_map_v1_map_get) | **GET** /v1/map | Get Map
[**get_ranks_v2_ranks_get**](DefaultApi.md#get_ranks_v2_ranks_get) | **GET** /v2/ranks | Get Ranks
[**get_sounds_v1_sounds_get**](DefaultApi.md#get_sounds_v1_sounds_get) | **GET** /v1/sounds | Get Sounds
[**get_steam_info_v1_steam_info_get**](DefaultApi.md#get_steam_info_v1_steam_info_get) | **GET** /v1/steam-info | Get Steam Info


# **get_build_tags_v2_build_tags_get**
> List[BuildTagV2Output] get_build_tags_v2_build_tags_get(language=language, client_version=client_version)

Get Build Tags

### Example


```python
import assets-deadlock-api-client
from assets-deadlock-api-client.models.build_tag_v2_output import BuildTagV2Output
from assets-deadlock-api-client.models.deadlock_assets_api_routes_raw_valid_client_versions import DeadlockAssetsApiRoutesRawValidClientVersions
from assets-deadlock-api-client.models.language import Language
from assets-deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://assets.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = assets-deadlock-api-client.Configuration(
    host = "https://assets.deadlock-api.com"
)


# Enter a context with an instance of the API client
with assets-deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets-deadlock-api-client.DefaultApi(api_client)
    language = assets-deadlock-api-client.Language() # Language |  (optional)
    client_version = assets-deadlock-api-client.DeadlockAssetsApiRoutesRawValidClientVersions() # DeadlockAssetsApiRoutesRawValidClientVersions |  (optional)

    try:
        # Get Build Tags
        api_response = api_instance.get_build_tags_v2_build_tags_get(language=language, client_version=client_version)
        print("The response of DefaultApi->get_build_tags_v2_build_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_build_tags_v2_build_tags_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | [**Language**](.md)|  | [optional] 
 **client_version** | [**DeadlockAssetsApiRoutesRawValidClientVersions**](.md)|  | [optional] 

### Return type

[**List[BuildTagV2Output]**](BuildTagV2Output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_versions_v2_client_versions_get**
> List[int] get_client_versions_v2_client_versions_get()

Get Client Versions

### Example


```python
import assets-deadlock-api-client
from assets-deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://assets.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = assets-deadlock-api-client.Configuration(
    host = "https://assets.deadlock-api.com"
)


# Enter a context with an instance of the API client
with assets-deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets-deadlock-api-client.DefaultApi(api_client)

    try:
        # Get Client Versions
        api_response = api_instance.get_client_versions_v2_client_versions_get()
        print("The response of DefaultApi->get_client_versions_v2_client_versions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_client_versions_v2_client_versions_get: %s\n" % e)
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
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_colors_v1_colors_get**
> Dict[str, ColorV1] get_colors_v1_colors_get(client_version=client_version)

Get Colors

### Example


```python
import assets-deadlock-api-client
from assets-deadlock-api-client.models.color_v1 import ColorV1
from assets-deadlock-api-client.models.deadlock_assets_api_routes_raw_valid_client_versions import DeadlockAssetsApiRoutesRawValidClientVersions
from assets-deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://assets.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = assets-deadlock-api-client.Configuration(
    host = "https://assets.deadlock-api.com"
)


# Enter a context with an instance of the API client
with assets-deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets-deadlock-api-client.DefaultApi(api_client)
    client_version = assets-deadlock-api-client.DeadlockAssetsApiRoutesRawValidClientVersions() # DeadlockAssetsApiRoutesRawValidClientVersions |  (optional)

    try:
        # Get Colors
        api_response = api_instance.get_colors_v1_colors_get(client_version=client_version)
        print("The response of DefaultApi->get_colors_v1_colors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_colors_v1_colors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | [**DeadlockAssetsApiRoutesRawValidClientVersions**](.md)|  | [optional] 

### Return type

[**Dict[str, ColorV1]**](ColorV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_icons_v1_icons_get**
> Dict[str, str] get_icons_v1_icons_get(client_version=client_version)

Get Icons

### Example


```python
import assets-deadlock-api-client
from assets-deadlock-api-client.models.deadlock_assets_api_routes_raw_valid_client_versions import DeadlockAssetsApiRoutesRawValidClientVersions
from assets-deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://assets.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = assets-deadlock-api-client.Configuration(
    host = "https://assets.deadlock-api.com"
)


# Enter a context with an instance of the API client
with assets-deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets-deadlock-api-client.DefaultApi(api_client)
    client_version = assets-deadlock-api-client.DeadlockAssetsApiRoutesRawValidClientVersions() # DeadlockAssetsApiRoutesRawValidClientVersions |  (optional)

    try:
        # Get Icons
        api_response = api_instance.get_icons_v1_icons_get(client_version=client_version)
        print("The response of DefaultApi->get_icons_v1_icons_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_icons_v1_icons_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | [**DeadlockAssetsApiRoutesRawValidClientVersions**](.md)|  | [optional] 

### Return type

**Dict[str, str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_map_v1_map_get**
> MapV1 get_map_v1_map_get(client_version=client_version)

Get Map

### Example


```python
import assets-deadlock-api-client
from assets-deadlock-api-client.models.deadlock_assets_api_routes_raw_valid_client_versions import DeadlockAssetsApiRoutesRawValidClientVersions
from assets-deadlock-api-client.models.map_v1 import MapV1
from assets-deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://assets.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = assets-deadlock-api-client.Configuration(
    host = "https://assets.deadlock-api.com"
)


# Enter a context with an instance of the API client
with assets-deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets-deadlock-api-client.DefaultApi(api_client)
    client_version = assets-deadlock-api-client.DeadlockAssetsApiRoutesRawValidClientVersions() # DeadlockAssetsApiRoutesRawValidClientVersions |  (optional)

    try:
        # Get Map
        api_response = api_instance.get_map_v1_map_get(client_version=client_version)
        print("The response of DefaultApi->get_map_v1_map_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_map_v1_map_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | [**DeadlockAssetsApiRoutesRawValidClientVersions**](.md)|  | [optional] 

### Return type

[**MapV1**](MapV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ranks_v2_ranks_get**
> List[RankV2Output] get_ranks_v2_ranks_get(language=language, client_version=client_version)

Get Ranks

### Example


```python
import assets-deadlock-api-client
from assets-deadlock-api-client.models.deadlock_assets_api_routes_raw_valid_client_versions import DeadlockAssetsApiRoutesRawValidClientVersions
from assets-deadlock-api-client.models.language import Language
from assets-deadlock-api-client.models.rank_v2_output import RankV2Output
from assets-deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://assets.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = assets-deadlock-api-client.Configuration(
    host = "https://assets.deadlock-api.com"
)


# Enter a context with an instance of the API client
with assets-deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets-deadlock-api-client.DefaultApi(api_client)
    language = assets-deadlock-api-client.Language() # Language |  (optional)
    client_version = assets-deadlock-api-client.DeadlockAssetsApiRoutesRawValidClientVersions() # DeadlockAssetsApiRoutesRawValidClientVersions |  (optional)

    try:
        # Get Ranks
        api_response = api_instance.get_ranks_v2_ranks_get(language=language, client_version=client_version)
        print("The response of DefaultApi->get_ranks_v2_ranks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_ranks_v2_ranks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | [**Language**](.md)|  | [optional] 
 **client_version** | [**DeadlockAssetsApiRoutesRawValidClientVersions**](.md)|  | [optional] 

### Return type

[**List[RankV2Output]**](RankV2Output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sounds_v1_sounds_get**
> Dict[str, object] get_sounds_v1_sounds_get(client_version=client_version)

Get Sounds

### Example


```python
import assets-deadlock-api-client
from assets-deadlock-api-client.models.deadlock_assets_api_routes_raw_valid_client_versions import DeadlockAssetsApiRoutesRawValidClientVersions
from assets-deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://assets.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = assets-deadlock-api-client.Configuration(
    host = "https://assets.deadlock-api.com"
)


# Enter a context with an instance of the API client
with assets-deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets-deadlock-api-client.DefaultApi(api_client)
    client_version = assets-deadlock-api-client.DeadlockAssetsApiRoutesRawValidClientVersions() # DeadlockAssetsApiRoutesRawValidClientVersions |  (optional)

    try:
        # Get Sounds
        api_response = api_instance.get_sounds_v1_sounds_get(client_version=client_version)
        print("The response of DefaultApi->get_sounds_v1_sounds_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_sounds_v1_sounds_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | [**DeadlockAssetsApiRoutesRawValidClientVersions**](.md)|  | [optional] 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_steam_info_v1_steam_info_get**
> object get_steam_info_v1_steam_info_get(client_version=client_version)

Get Steam Info

### Example


```python
import assets-deadlock-api-client
from assets-deadlock-api-client.models.deadlock_assets_api_routes_raw_valid_client_versions import DeadlockAssetsApiRoutesRawValidClientVersions
from assets-deadlock-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://assets.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = assets-deadlock-api-client.Configuration(
    host = "https://assets.deadlock-api.com"
)


# Enter a context with an instance of the API client
with assets-deadlock-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets-deadlock-api-client.DefaultApi(api_client)
    client_version = assets-deadlock-api-client.DeadlockAssetsApiRoutesRawValidClientVersions() # DeadlockAssetsApiRoutesRawValidClientVersions |  (optional)

    try:
        # Get Steam Info
        api_response = api_instance.get_steam_info_v1_steam_info_get(client_version=client_version)
        print("The response of DefaultApi->get_steam_info_v1_steam_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_steam_info_v1_steam_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | [**DeadlockAssetsApiRoutesRawValidClientVersions**](.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

