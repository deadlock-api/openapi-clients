# deadlock_api_client.BuildTagsApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_build_tag**](BuildTagsApi.md#get_build_tag) | **GET** /v1/assets/build-tags/{build_tag_id} | Get Build Tag
[**get_build_tag_by_name**](BuildTagsApi.md#get_build_tag_by_name) | **GET** /v1/assets/build-tags/by-name/{name} | Get Build Tag By Name
[**list_build_tags**](BuildTagsApi.md#list_build_tags) | **GET** /v1/assets/build-tags | List Build Tags


# **get_build_tag**
> BuildTag get_build_tag(build_tag_id, language=language, client_version=client_version)

Get Build Tag

Returns a single build tag by id.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.build_tag import BuildTag
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
    api_instance = deadlock_api_client.BuildTagsApi(api_client)
    build_tag_id = 56 # int | Build tag id (murmurhash2 of `class_name`)
    language = 'language_example' # str | Language code. Defaults to `english`. (optional)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # Get Build Tag
        api_response = api_instance.get_build_tag(build_tag_id, language=language, client_version=client_version)
        print("The response of BuildTagsApi->get_build_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildTagsApi->get_build_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_tag_id** | **int**| Build tag id (murmurhash2 of &#x60;class_name&#x60;) | 
 **language** | **str**| Language code. Defaults to &#x60;english&#x60;. | [optional] 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**BuildTag**](BuildTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Unknown build tag id or client_version |  -  |
**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build_tag_by_name**
> BuildTag get_build_tag_by_name(name, language=language, client_version=client_version)

Get Build Tag By Name

Returns a single build tag by `class_name` (case-insensitive).

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.build_tag import BuildTag
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
    api_instance = deadlock_api_client.BuildTagsApi(api_client)
    name = 'name_example' # str | Build tag `class_name` (e.g. `citadel_build_tag_weapon`)
    language = 'language_example' # str | Language code. Defaults to `english`. (optional)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # Get Build Tag By Name
        api_response = api_instance.get_build_tag_by_name(name, language=language, client_version=client_version)
        print("The response of BuildTagsApi->get_build_tag_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildTagsApi->get_build_tag_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Build tag &#x60;class_name&#x60; (e.g. &#x60;citadel_build_tag_weapon&#x60;) | 
 **language** | **str**| Language code. Defaults to &#x60;english&#x60;. | [optional] 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**BuildTag**](BuildTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Unknown build tag name or client_version |  -  |
**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_build_tags**
> List[BuildTag] list_build_tags(language=language, client_version=client_version)

List Build Tags

Returns the build tag taxonomy used by the game client, derived from per-version localization keys.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.build_tag import BuildTag
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
    api_instance = deadlock_api_client.BuildTagsApi(api_client)
    language = 'language_example' # str | Language code. Defaults to `english`. (optional)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # List Build Tags
        api_response = api_instance.list_build_tags(language=language, client_version=client_version)
        print("The response of BuildTagsApi->list_build_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildTagsApi->list_build_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Language code. Defaults to &#x60;english&#x60;. | [optional] 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**List[BuildTag]**](BuildTag.md)

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

