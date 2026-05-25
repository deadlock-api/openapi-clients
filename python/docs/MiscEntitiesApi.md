# deadlock_api_client.MiscEntitiesApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_misc_entity**](MiscEntitiesApi.md#get_misc_entity) | **GET** /v1/assets/misc-entities/{id_or_classname} | Get Misc Entity
[**list_misc_entities**](MiscEntitiesApi.md#list_misc_entities) | **GET** /v1/assets/misc-entities | List Misc Entities


# **get_misc_entity**
> MiscEntity get_misc_entity(id_or_classname, client_version=client_version)

Get Misc Entity

Returns a single misc entity by numeric id or by `class_name` (case-insensitive).

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.misc_entity import MiscEntity
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
    api_instance = deadlock_api_client.MiscEntitiesApi(api_client)
    id_or_classname = 'id_or_classname_example' # str | Misc entity id (`murmurhash2(class_name)`) or `class_name`
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # Get Misc Entity
        api_response = api_instance.get_misc_entity(id_or_classname, client_version=client_version)
        print("The response of MiscEntitiesApi->get_misc_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscEntitiesApi->get_misc_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_classname** | **str**| Misc entity id (&#x60;murmurhash2(class_name)&#x60;) or &#x60;class_name&#x60; | 
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**MiscEntity**](MiscEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Unknown misc entity id/class_name or client_version |  -  |
**500** | Failed to load source assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_misc_entities**
> List[MiscEntity] list_misc_entities(client_version=client_version)

List Misc Entities

Returns the per-misc-entity metadata used by the game client, parsed from the patch's KV3 source files.

### Example


```python
import deadlock_api_client
from deadlock_api_client.models.misc_entity import MiscEntity
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
    api_instance = deadlock_api_client.MiscEntitiesApi(api_client)
    client_version = 56 # int | Client/game version (e.g. `6518`). Defaults to the latest known version. (optional)

    try:
        # List Misc Entities
        api_response = api_instance.list_misc_entities(client_version=client_version)
        print("The response of MiscEntitiesApi->list_misc_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscEntitiesApi->list_misc_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | **int**| Client/game version (e.g. &#x60;6518&#x60;). Defaults to the latest known version. | [optional] 

### Return type

[**List[MiscEntity]**](MiscEntity.md)

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

